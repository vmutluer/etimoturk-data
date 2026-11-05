#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EtimoTürk veri üretim hattı.

Kullanım:  python3 DataPipeline/build_database.py [--out App/Resources]

Girdi: etymodata/ ve corpora/ altındaki dilbilimsel kural setleri, sözlük listeleri, özgün alfabe tabloları, yer adı ve
deyim kökeni kayıtları (Faz 4) ve Kaikki.org ETL çıktısı.
Çıktı: etymoturk.sqlite (FTS5 ile) ve yedek etymoturk.json paketi.
"""
import argparse
import json
import os
import re
import sqlite3
import sys
import time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from etymodata.languages import (ORIGIN_LANGUAGES, STAGE_NAMES, TARGET_LANGUAGES,
                                 ATTESTATIONS, PERIODS)
from etymodata.parsing import (parse_lexicon, parse_families, parse_cognates, parse_toponyms, parse_idioms, parse_names,
                               LexEntry, load_generated, corpora_blocks)
from etymodata.phase4 import TOPONYM_ORIGIN_LANGUAGES, IDIOM_DOMAINS, calibrated_confidence
from etymodata.phase4_rows import make_toponym_row, make_idiom_row
from etymodata.names import make_name_row
from etymodata.english_loader import EnglishData
from etymodata import templates_en
from etymodata.english_vocab import (ORIGIN_LANGUAGES_EN, ATTESTATIONS_EN, PERIODS_EN, TARGET_LANGUAGES_EN, REGION_GROUPS_EN,
                                     TOPONYM_ORIGINS_EN, TOPONYM_KINDS_EN, REGIONS_EN, IDIOM_DOMAINS_EN, IDIOM_CONFIDENCE_EN)
from etymodata.samples import SAMPLE_TEXTS
from etymodata.sources import DATA_SOURCES, WIKTIONARY_ATTRIBUTION
from etymodata.enrich import ScriptEnricher
from etymodata import derivation, templates, audit_rules
from etymodata.templates import normalize

SCHEMA_VERSION = 6

_REF_MARKUP = re.compile(r"\s*<[a-z]+[:\s].*$", re.S)  # <ref:…>, <pos:…>, <ety:…>, <alt:…> şablon kalıntıları
_TAGS = re.compile(r"<[^>]*>")


def clean_wiktionary_text(text):
    """Kaikki dökümünden sızan <ref …> kaynak göstergelerini ve HTML etiketlerini atar (yalnızca biçim kalır)."""
    if not isinstance(text, str):
        return text
    text = _REF_MARKUP.sub("", text)
    text = _TAGS.sub("", text)
    return text.strip()


def sanitize_wiktionary(wikt: dict):
    for w in wikt.get("words", []):
        w["source_form"] = clean_wiktionary_text(w.get("source_form") or "")
        w["source_script"] = clean_wiktionary_text(w.get("source_script") or "")
        w["chain"] = [[c, clean_wiktionary_text(f)] for c, f in w.get("chain", []) if clean_wiktionary_text(f)]
    for c in wikt.get("cognates", []):
        c["foreign"] = clean_wiktionary_text(c.get("foreign") or "")
        c["romanization"] = clean_wiktionary_text(c.get("romanization") or "")
    wikt["cognates"] = [c for c in wikt.get("cognates", []) if c["foreign"]]


# Osmanlı Türkçesi maddelerinin köken dilleri (etl_ottoman.py) → zincir aşama kodu
OTTOMAN_STAGE = {"tr": "otk", "ar": "ar", "fa": "fa", "el": "el", "fr": "fr", "it": "it", "en": "en", "hy": "hy", "mn": "mn",
                 "sl": "sl", "la": "la", "de": "de", "es": "es", "he": "he", "hu": "hu", "ro": "ro", "zh": "zh", "sog": "sog"}
OTTOMAN_STAGE_BY_LANG = {"Proto-Turkic": "otk", "Old Turkic": "otk", "Ancient Greek": "grc", "Koine Greek": "grc",
                         "Middle Persian": "pal", "Classical Persian": "fa", "Venetian": "ven", "Latin": "la"}


def apply_ottoman_resolutions(wikt: dict) -> int:
    """Osmanlı Türkçesi aşamasında kalan (ota) Wiktionary kayıtlarına, Osmanlı Türkçesi maddelerinden izlenen asıl
    kökeni uygular (corpora/generated/ottoman_resolution.json, etl_ottoman.py çıktısı). Zincirin başına kaynak dil
    aşaması eklenir; Osmanlı yazımı (özgün yazım kartı) korunur."""
    data = load_generated("ottoman_resolution")
    if not data:
        return 0
    res = data.get("resolutions", {})
    applied = 0
    for w in wikt.get("words", []):
        r = res.get(f"{w['lemma']}|{w['pos']}")
        if not r or w.get("origin") != "ota":
            continue
        stage = OTTOMAN_STAGE_BY_LANG.get(r.get("source_lang", ""), OTTOMAN_STAGE.get(r["origin"], r["origin"]))
        term = clean_wiktionary_text(r.get("source_term") or "").lstrip("*")
        chain = w.get("chain", [])
        if chain and chain[0][0] == "ota" and r.get("ota_roman") and not re.search(r"[\u0600-\u06FF]", r["ota_roman"]):
            # Osmanlı aşamasında Arap harfli biçim yerine çevriyazı
            if re.search(r"[\u0600-\u06FF]", chain[0][1]):
                chain[0] = ["ota", clean_wiktionary_text(r["ota_roman"])]
        if term and term != "-":
            chain = [[stage, term]] + chain
        w["chain"] = chain
        w["origin"] = r["origin"]
        w["ottoman_resolved"] = True
        if not w.get("method", "").startswith("internal:"):
            w["method"] = "ota-chain"
        applied += 1
    return applied


def apply_ottoman_reviews(wikt: dict) -> int:
    """Elle incelenmiş köken kararları (corpora/generated/ottoman_review.json): Osmanlı Türkçesi maddesiyle de
    çözülemeyen (ota) kayıtlara, Türkçeye doğrudan veren dili uygular. Yalnızca hâlâ ota olan kayıtlara dokunur."""
    data = load_generated("ottoman_review")
    if not data:
        return 0
    decisions = data.get("decisions", {})
    applied = 0
    for w in wikt.get("words", []):
        d = decisions.get(f"{w['lemma']}|{w['pos']}")
        if not d or w.get("origin") != "ota" or d.get("origin") not in ORIGIN_LANGUAGES or d["origin"] == "ota":
            continue
        w["origin"] = d["origin"]
        w["reviewed"] = True
        # Kaynağın "olabilir, kesin değil" dediği kararlar tartışmalı işaretlenir
        w["disputed"] = bool(d.get("disputed"))
        # Kararın dayanağı: "nisanyan" (Nişanyan Sözlük maddesiyle karşılaştırıldı) ya da "editor" (yapı açık; kaynak yok)
        w["review_basis"] = d.get("basis", "") if d.get("basis") in ("nisanyan", "editor") else ""
        if not w.get("method", "").startswith("internal:"):
            w["method"] = "review"
        applied += 1
    return applied


def apply_provenance(word_rows, derived_rows, wikt_rows, wikt_by_row, wikt) -> None:
    """Her sözcüğe künye kaynağını yazar (şema 6):
    - provenance: curated (EtimoTürk editör kaydı), derived (editör kaydından Türkçe içi türetme), wiktionary,
      wiktionary_ottoman (asıl köken Wiktionary'nin Osmanlı Türkçesi maddesinden izlendi), review (ek inceleme kararı);
    - provenance_basis: incelemenin dayanağı ("nisanyan" | "editor" | "");
    - wiktionary_title: sözcüğün Wiktionary'deki Türkçe madde başlığı (bağlantı için; yoksa boş);
    - wiktionary_origin: editör kayıtlarında Wiktionary'nin verdiği köken (karşılaştırma; çözülmemiş/bilinmeyen ise boş)."""
    words = (wikt or {}).get("words", [])
    title_by_norm = {}
    for w in words:
        title_by_norm.setdefault(normalize(w["lemma"]), w["lemma"])
    for lemma in ((load_generated("glosses_en") or {}).get("glosses", {}) or {}):
        title_by_norm.setdefault(normalize(lemma), lemma)
    origin_by_key, origin_by_lemma = {}, {}
    for w in words:
        origin_by_key.setdefault((w["lemma"], w["pos"]), w["origin"])
        origin_by_lemma.setdefault(w["lemma"], w["origin"])
    for kind, rows in (("curated", word_rows), ("derived", derived_rows)):
        for r in rows:
            r["provenance"], r["provenance_basis"] = kind, ""
            r["wiktionary_title"] = title_by_norm.get(normalize(r["lemma"]), "")
            wo = origin_by_key.get((r["lemma"], r["pos"])) or origin_by_lemma.get(r["lemma"], "")
            r["wiktionary_origin"] = wo if wo and wo not in ("ota", "unk") else ""
    for r in wikt_rows:
        w = wikt_by_row[r["id"]]
        r["provenance"] = "review" if w.get("reviewed") else ("wiktionary_ottoman" if w.get("ottoman_resolved") else "wiktionary")
        r["provenance_basis"] = w.get("review_basis", "") if w.get("reviewed") else ""
        r["wiktionary_title"] = title_by_norm.get(normalize(r["lemma"]), w["lemma"])
        r["wiktionary_origin"] = ""


def attested_lemmas() -> set:
    """Açık lisanslı sözlük dökümlerinde madde başı olarak geçen lemmalar (normalize edilmiş); boş küme = denetim kapalı."""
    out = set()
    wikt = load_generated("wiktionary_tr")
    for w in (wikt or {}).get("words", []):
        out.add(normalize(w["lemma"]))
    glosses = load_generated("glosses_en")
    for lemma in (glosses or {}).get("glosses", {}):
        out.add(normalize(lemma))
    return out


def build(out_dir: str, data_commit: str = "") -> dict:
    t0 = time.time()
    EN = EnglishData()
    lexicon = parse_lexicon()
    cognates = parse_cognates()
    # üyesi olmayan kök aileleri (üyeleri başka modülde ilk kayıt olarak kazanılmış olabilir) tabloya alınmaz
    used_family_codes = {e.family for e in lexicon if e.family}
    families = []
    for fam in parse_families():
        if fam.code in used_family_codes:
            families.append(fam)
        else:
            print(f"uyarı: üyesi olmayan kök ailesi atlandı: {fam.code}", file=sys.stderr)

    # --- kök aileleri ---------------------------------------------------
    family_ids = {}
    family_rows = []
    for i, fam in enumerate(families, start=1):
        family_ids[fam.code] = i
        origin_name = ORIGIN_LANGUAGES.get(fam.origin, ("Bilinmeyen",))[0]
        family_rows.append([i, fam.code, fam.origin, origin_name, fam.core_meaning, fam.explanation, "", ""])

    # --- çekirdek sözcükler --------------------------------------------
    turcism_lemmas = {c.lemma for c in cognates if c.direction == "from_turkish"}
    cognate_count = defaultdict(int)
    for c in cognates:
        cognate_count[c.lemma] += 1

    word_rows = []
    lemma_to_id = {}
    next_id = 1
    for e in lexicon:
        row = templates.make_word_row(next_id, e, family_ids, turcism_lemmas, cognate_count)
        src_en = EN.translate_meaning(e.source_meaning)
        gloss_en = EN.gloss(e.lemma) or src_en
        row["english_gloss"] = gloss_en
        row["source_meaning_en"] = src_en
        row["etymology_summary_en"] = templates_en.summary_en_for(e, gloss_en, src_en, e.family or None, templates.build_chain(e))
        row["historical_attestation_en"] = ATTESTATIONS_EN.get(e.era, e.era)
        row["origin_period_en"] = PERIODS_EN.get(e.era, e.era)
        word_rows.append(row)
        lemma_to_id.setdefault(e.lemma, next_id)
        next_id += 1

    # --- türetilmiş sözcükler ------------------------------------------
    # Kural tabanlı türetim biçimsel olarak geçerli ama sözlükte bulunmayan biçimler de üretir (gergedanlık,
    # mililitresiz…). Yalnızca açık lisanslı bir sözlükte (Wiktionary/Kaikki.org dökümü: yapısal kayıtlar ya da
    # İngilizce anlam listesi) madde başı olarak tanıklanmış türetmeler veritabanına alınır; gerisi atlanır.
    attested = attested_lemmas()
    # Ortak sözcük ya da deyim kaydının başvurduğu türetmeler elle seçilmiş sayılır ve her zaman korunur
    referenced = {c.lemma for c in cognates} | {w for idiom in parse_idioms() for w in idiom.words}
    existing = {(r["lemma"], r["pos"]) for r in word_rows}
    existing_lemmas = {r["lemma"] for r in word_rows}
    derived_rows = []
    derived_skipped = 0
    for e in lexicon:
        base_id = lemma_to_id[e.lemma]
        for d in derivation.derive(e):
            if d.lemma in existing_lemmas or (d.lemma, d.pos) in existing:
                continue
            if attested and normalize(d.lemma) not in attested and d.lemma not in referenced:
                derived_skipped += 1
                continue
            existing_lemmas.add(d.lemma)
            row = templates.make_derived_row(next_id, e, d, base_id, family_ids)
            base_row = word_rows[base_id - 1]
            src_en = base_row["source_meaning_en"]
            row["english_gloss"] = EN.gloss(d.lemma) or templates_en.derived_gloss_en(d, base_row["english_gloss"])
            row["source_meaning_en"] = src_en
            row["etymology_summary_en"] = templates_en.derived_summary_en(e, d, base_row["english_gloss"], src_en)
            row["historical_attestation_en"] = "Derived word – base: " + ATTESTATIONS_EN.get(e.era, e.era)
            row["origin_period_en"] = "Turkish derivation (suffix: " + d.suffix_surface + ")"
            derived_rows.append(row)
            lemma_to_id.setdefault(d.lemma, next_id)
            next_id += 1
    # --- Wiktionary (Kaikki.org) ETL çıktısı -----------------------------
    wikt = load_generated("wiktionary_tr")
    ottoman_resolved = 0
    if wikt:
        sanitize_wiktionary(wikt)
        ottoman_resolved = apply_ottoman_resolutions(wikt)
        apply_ottoman_reviews(wikt)
    wikt_rows = []
    wikt_cognates = []
    wikt_by_row = {}
    if wikt:
        wikt_cog_count = defaultdict(int)
        for c in wikt.get("cognates", []):
            wikt_cog_count[c["lemma"]] += 1
        for w in wikt.get("words", []):
            if (w["lemma"], w["pos"]) in existing or w["lemma"] in existing_lemmas:
                continue  # elle yazılmış korpus önceliklidir
            existing.add((w["lemma"], w["pos"]))
            existing_lemmas.add(w["lemma"])
            wrow = templates.make_wiktionary_row(next_id, w, wikt_cog_count.get(w["lemma"], 0))
            wgloss = (w.get("gloss_en") or EN.gloss(w["lemma"]) or "").strip()
            wrow["english_gloss"] = wgloss
            wrow["source_meaning_en"] = wgloss
            wchain = [(templates.stage_name(c), f) for c, f in w.get("chain", []) if f]
            if not wchain or wchain[-1][0] != templates.stage_name("tr"):
                wchain.append((templates.stage_name("tr"), w["lemma"]))
            wrow["etymology_summary_en"] = templates_en.wiktionary_summary_en(w, wgloss, wchain)
            wrow["historical_attestation_en"] = ATTESTATIONS_EN["WIKT"]
            wrow["origin_period_en"] = PERIODS_EN["WIKT"]
            wikt_rows.append(wrow)
            wikt_by_row[next_id] = w
            lemma_to_id.setdefault(w["lemma"], next_id)
            next_id += 1
        wikt_cognates = wikt.get("cognates", [])
    all_words = word_rows + derived_rows + wikt_rows

    # --- künye kaynağı (şema 6): bilginin nereden geldiği + Wiktionary sayfası ------------------
    apply_provenance(word_rows, derived_rows, wikt_rows, wikt_by_row, wikt)

    # --- özgün alfabe, vezin ve IPA zenginleştirmesi (şema 2) ----------------
    overrides, override_names = {}, {}
    for block in corpora_blocks("SCRIPTS"):
        overrides.update(block)
    for block in corpora_blocks("SCRIPT_NAMES"):
        override_names.update(block)
    wikt_scripts = {}
    for w in (wikt or {}).get("words", []):
        if w.get("source_script") and w["lemma"] not in wikt_scripts:
            wikt_scripts[w["lemma"]] = (w["source_script"], w.get("source_form") or "")
    enricher = ScriptEnricher(overrides, override_names, wikt_scripts)
    for e, row in zip(lexicon, word_rows):
        enricher.enrich_curated(row, e, e.family or None)
    for row in derived_rows:
        enricher.enrich_derived(row)
    for row in wikt_rows:
        enricher.enrich_wiktionary(row, wikt_by_row[row["id"]])

    # --- kök ailelerinin İngilizce alanları ------------------------------------
    members_by_family = defaultdict(list)
    for r in word_rows:
        if r["root_family_id"]:
            members_by_family[r["root_family_id"]].append(r["lemma"])
    family_entries = {f.code: f for f in families}
    for fr in family_rows:
        tr_en = EN.families.get(fr[1])
        if tr_en and tr_en[0] and tr_en[1]:
            fr[6], fr[7] = tr_en
        else:
            core_en = (tr_en[0] if tr_en else "") or EN.translate_meaning(fr[4])
            fr[6] = core_en
            fr[7] = (tr_en[1] if tr_en and tr_en[1] else "") or templates_en.family_explanation_en(family_entries[fr[1]], core_en, members_by_family.get(fr[0], []))
    gloss_by_id = {r["id"]: r["english_gloss"] for r in all_words}
    lemma_by_id = {r["id"]: r["lemma"] for r in all_words}

    def cognate_meaning_en(wid, meaning):
        if meaning == lemma_by_id.get(wid) and gloss_by_id.get(wid):
            return gloss_by_id[wid]
        t = EN.translate_meaning(meaning)
        if t:
            return t
        if meaning.startswith("Türkçe ile aynı anlamda") and gloss_by_id.get(wid):
            return gloss_by_id[wid] + " (same sense as Turkish; Wiktionary descendant record)"
        return f"'{meaning}' (Turkish gloss)"

    def ff_note_en(note, lang):
        if not note:
            return None
        return EN.false_friends.get(note) or f"The meaning has shifted in {TARGET_LANGUAGES_EN.get(lang, lang)}; see the Turkish note."

    # --- ortak sözcükler -----------------------------------------------
    cognate_rows = []
    cid = 1
    seen_pairs = set()
    origin_by_id = {r["id"]: r["origin_language_code"] for r in all_words}
    audit_stats = defaultdict(int)
    for c in cognates:
        wid = lemma_to_id.get(c.lemma)
        if wid is None:
            raise SystemExit(f"Ortak sözcük başlığı sözlükte yok: {c.lemma}")
        key = (wid, c.lang, c.foreign.lower())
        if key in seen_pairs:
            continue  # farklı korpus modüllerinde yinelenen satır
        seen_pairs.add(key)
        if audit_rules.is_excluded(c.lemma, c.lang, c.foreign):
            audit_stats["cognates_excluded"] += 1
            continue  # akraba değil, yalnızca çeviri karşılığı (bkz. etymodata/audit_rules.py)
        direction = audit_rules.resolve_direction(origin_by_id.get(wid, ""), c.lang, c.direction)
        if direction != c.direction:
            audit_stats["cognate_direction_fixed"] += 1
        name, flag, region, script, country = TARGET_LANGUAGES[c.lang]
        cognate_rows.append((cid, wid, c.lang, name, flag, region, c.foreign, c.romanization,
                             c.meaning, direction, c.false_friend or None,
                             cognate_meaning_en(wid, c.meaning), ff_note_en(c.false_friend or None, c.lang),
                             TARGET_LANGUAGES_EN.get(c.lang, name), REGION_GROUPS_EN.get(region, region)))
        cid += 1
    for c in wikt_cognates:
        wid = lemma_to_id.get(c["lemma"])
        if wid is None or c["lang"] not in TARGET_LANGUAGES:
            continue
        key = (wid, c["lang"], c["foreign"].lower())
        if key in seen_pairs:
            continue
        seen_pairs.add(key)
        if audit_rules.is_excluded(c["lemma"], c["lang"], c["foreign"]):
            audit_stats["cognates_excluded"] += 1
            continue
        name, flag, region, script, country = TARGET_LANGUAGES[c["lang"]]
        direction = "from_turkish" if c.get("borrowed") else "shared_ancestor"
        if c["lang"] in audit_rules.TURKIC_TARGETS:
            direction = "shared_ancestor"
        meaning = c.get("meaning") or "Türkçe ile aynı anlamda (Wiktionary soy kaydı)"
        cognate_rows.append((cid, wid, c["lang"], name, flag, region, c["foreign"], c.get("romanization", ""),
                             meaning, direction, None, cognate_meaning_en(wid, meaning), None,
                             TARGET_LANGUAGES_EN.get(c["lang"], name), REGION_GROUPS_EN.get(region, region)))
        cid += 1
    # cognate_count sütununu gerçek satır sayısıyla eşle
    per_word = defaultdict(int)
    for r in cognate_rows:
        per_word[r[1]] += 1
    exporters = {r[1] for r in cognate_rows if r[9] == "from_turkish"}
    for row in all_words:
        row["cognate_count"] = per_word.get(row["id"], 0)
        # bayrak yalnızca gerçekten Türkçeden başka dile geçmiş (from_turkish) satırı olan sözcüklerde kalır
        row["is_turcism_exporter"] = 1 if row["id"] in exporters else 0

    # --- Faz 4: yer adları ve deyim kökenleri ------------------------------
    toponym_rows = []
    en_counts = defaultdict(int)
    for i, t in enumerate(parse_toponyms(), start=1):
        row = make_toponym_row(i, t)
        tr_en = EN.toponyms.get(f"{t.name}|{t.province}")
        if tr_en and tr_en[0] and tr_en[1]:
            row["meaning_en"], row["story_en"] = tr_en
            en_counts["toponyms_translated"] += 1
        else:
            row["meaning_en"], row["story_en"] = templates_en.toponym_fallback_en(t)
        row["summary_en"] = templates_en.toponym_summary_en(t, row["meaning_en"])
        row["kind_name_en"] = TOPONYM_KINDS_EN.get(t.kind, t.kind)
        row["region_en"] = REGIONS_EN.get(t.region, t.region)
        row["origin_language_name_en"] = TOPONYM_ORIGINS_EN.get(t.origin, (t.origin, ""))[0]
        toponym_rows.append(row)
    idiom_rows, idiom_word_rows = [], []
    for i, idiom in enumerate(parse_idioms(), start=1):
        calibrated = calibrated_confidence(idiom.confidence, idiom.source)
        if calibrated != idiom.confidence:
            audit_stats["idiom_confidence_downgraded"] += 1
            idiom.confidence = calibrated
        irow = make_idiom_row(i, idiom)
        tr_en = EN.idioms.get(idiom.phrase)
        if tr_en and all(tr_en):
            irow["meaning_en"], irow["literal_sense_en"], irow["origin_story_en"] = tr_en
            en_counts["idioms_translated"] += 1
        else:
            irow["meaning_en"], irow["literal_sense_en"], irow["origin_story_en"] = templates_en.idiom_fallback_en(idiom)
        irow["domain_name_en"] = IDIOM_DOMAINS_EN.get(idiom.domain, (idiom.domain, ""))[0]
        irow["origin_period_en"] = PERIODS_EN.get(idiom.era, idiom.era)
        irow["historical_attestation_en"] = ATTESTATIONS_EN.get(idiom.era, idiom.era)
        irow["confidence_name_en"] = IDIOM_CONFIDENCE_EN.get(idiom.confidence, idiom.confidence)
        idiom_rows.append(irow)
        seen_w = set()
        for lemma in idiom.words:
            wid = lemma_to_id.get(lemma)
            if wid is None:
                raise SystemExit(f"Deyimdeki sözcük sözlükte yok: {lemma} ({idiom.phrase})")
            if wid in seen_w:
                continue
            seen_w.add(wid)
            idiom_word_rows.append((i, wid, lemma))

    # --- veritabanı -----------------------------------------------------
    os.makedirs(out_dir, exist_ok=True)
    db_path = os.path.join(out_dir, "etymoturk.sqlite")
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executescript(templates.SCHEMA_SQL)

    cur.executemany("INSERT INTO origin_languages VALUES (?,?,?,?,?)",
                    [(code, v[0], v[1], v[2], ORIGIN_LANGUAGES_EN.get(code, v[0])) for code, v in ORIGIN_LANGUAGES.items()])
    cur.executemany("INSERT INTO languages VALUES (?,?,?,?,?,?,?,?)",
                    [(code, v[0], v[1], v[2], v[3], v[4], TARGET_LANGUAGES_EN.get(code, v[0]), REGION_GROUPS_EN.get(v[2], v[2])) for code, v in TARGET_LANGUAGES.items()])
    cur.executemany("INSERT INTO root_families VALUES (?,?,?,?,?,?,0,?,?)", [(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]) for r in family_rows])
    cur.executemany(
        """INSERT INTO words (id, lemma, normalized_lemma, pos, origin_language_code, origin_language_name,
            origin_period, root_family_id, source_form, source_meaning, etymology_summary,
            phonetic_evolution_json, historical_attestation, is_turcism_exporter, is_disputed,
            derived_from_id, derivation_suffix, cognate_count, data_source,
            original_script, original_script_name, transliteration, ipa, arabic_pattern, script_source,
            english_gloss, etymology_summary_en, source_meaning_en, historical_attestation_en, origin_period_en,
            provenance, provenance_basis, wiktionary_title, wiktionary_origin)
           VALUES (:id,:lemma,:normalized_lemma,:pos,:origin_language_code,:origin_language_name,
            :origin_period,:root_family_id,:source_form,:source_meaning,:etymology_summary,
            :phonetic_evolution_json,:historical_attestation,:is_turcism_exporter,:is_disputed,
            :derived_from_id,:derivation_suffix,:cognate_count,:data_source,
            :original_script,:original_script_name,:transliteration,:ipa,:arabic_pattern,:script_source,
            :english_gloss,:etymology_summary_en,:source_meaning_en,:historical_attestation_en,:origin_period_en,
            :provenance,:provenance_basis,:wiktionary_title,:wiktionary_origin)""", all_words)
    cur.executemany("INSERT INTO shared_cognates VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", cognate_rows)
    cur.executemany("INSERT INTO sample_texts VALUES (:id,:title,:author,:era,:body)", SAMPLE_TEXTS)
    cur.executemany("INSERT INTO data_sources VALUES (:id,:kind,:name,:author,:year,:license,:url,:license_url,:usage,:fields,:usage_en)",
                    [dict(d, usage_en=d.get("usage_en", "")) for d in DATA_SOURCES])
    cur.execute("UPDATE root_families SET member_count = (SELECT COUNT(*) FROM words w WHERE w.root_family_id = root_families.id AND w.derived_from_id IS NULL)")
    cur.execute("INSERT INTO words_fts(rowid, lemma, normalized_lemma, etymology_summary, source_form, source_meaning, original_script, english_gloss) "
                "SELECT id, lemma, normalized_lemma, etymology_summary, source_form, source_meaning, original_script, english_gloss FROM words")
    # Faz 4 tabloları
    cur.executemany("INSERT INTO toponym_origins VALUES (?,?,?,?,?,?,?)",
                    [(code, v[0], v[1], v[2], v[3], TOPONYM_ORIGINS_EN.get(code, (v[0], v[3]))[0], TOPONYM_ORIGINS_EN.get(code, (v[0], v[3]))[1]) for code, v in TOPONYM_ORIGIN_LANGUAGES.items()])
    cur.executemany(
        """INSERT INTO toponyms (id, name, normalized_name, kind, kind_name, province, region, plate_code,
            origin_language_code, origin_language_name, oldest_form, oldest_stage, name_evolution_json, layer_count,
            ancient_forms, meaning, summary, story, source_note, era, latitude, longitude,
            meaning_en, summary_en, story_en, kind_name_en, region_en, origin_language_name_en)
           VALUES (:id,:name,:normalized_name,:kind,:kind_name,:province,:region,:plate_code,
            :origin_language_code,:origin_language_name,:oldest_form,:oldest_stage,:name_evolution_json,:layer_count,
            :ancient_forms,:meaning,:summary,:story,:source_note,:era,:latitude,:longitude,
            :meaning_en,:summary_en,:story_en,:kind_name_en,:region_en,:origin_language_name_en)""", toponym_rows)
    cur.execute("INSERT INTO toponyms_fts(rowid, name, normalized_name, ancient_forms, meaning, story, meaning_en, story_en) "
                "SELECT id, name, normalized_name, ancient_forms, meaning, story, meaning_en, story_en FROM toponyms")
    cur.executemany("INSERT INTO idiom_domains VALUES (?,?,?,?,?,?,?,?)",
                    [(code, v[0], v[1], v[2], v[3], i, IDIOM_DOMAINS_EN.get(code, (v[0], v[3]))[0], IDIOM_DOMAINS_EN.get(code, (v[0], v[3]))[1]) for i, (code, v) in enumerate(IDIOM_DOMAINS.items(), start=1)])
    cur.executemany(
        """INSERT INTO idiom_origins (id, phrase, normalized_phrase, kind, domain_code, domain_name, meaning, literal_sense,
            origin_story, era_code, origin_period, historical_attestation, source_note, confidence, confidence_name,
            key_words, word_count, meaning_en, literal_sense_en, origin_story_en, domain_name_en, origin_period_en,
            historical_attestation_en, confidence_name_en)
           VALUES (:id,:phrase,:normalized_phrase,:kind,:domain_code,:domain_name,:meaning,:literal_sense,
            :origin_story,:era_code,:origin_period,:historical_attestation,:source_note,:confidence,:confidence_name,
            :key_words,:word_count,:meaning_en,:literal_sense_en,:origin_story_en,:domain_name_en,:origin_period_en,
            :historical_attestation_en,:confidence_name_en)""", idiom_rows)
    cur.executemany("INSERT INTO idiom_words VALUES (?,?,?)", idiom_word_rows)
    # --- kişi adları ------------------------------------------------------
    lexicon_index = {normalize(lemma): wid for lemma, wid in lemma_to_id.items()}
    name_rows = []
    for i, n in enumerate(parse_names(), start=1):
        if n.family and n.family not in family_ids:
            raise SystemExit(f"Kişi adının kök ailesi sözlükte yok: {n.name} → {n.family}")
        if n.related and normalize(n.related) not in lexicon_index:
            raise SystemExit(f"Kişi adının ilgili sözcüğü sözlükte yok: {n.name} → {n.related}")
        name_rows.append(make_name_row(i, n, family_ids, lexicon_index))
    cur.executemany(
        """INSERT INTO person_names (id, name, normalized_name, gender, origin_language_code, origin_language_name,
            origin_language_name_en, source_form, meaning, meaning_en, components_json, root_family_id, related_word_id,
            related_lemma, story, story_en, note, note_en, is_disputed)
           VALUES (:id,:name,:normalized_name,:gender,:origin_language_code,:origin_language_name,
            :origin_language_name_en,:source_form,:meaning,:meaning_en,:components_json,:root_family_id,:related_word_id,
            :related_lemma,:story,:story_en,:note,:note_en,:is_disputed)""", name_rows)
    cur.execute("INSERT INTO idioms_fts(rowid, phrase, normalized_phrase, meaning, origin_story, key_words, meaning_en, origin_story_en) "
                "SELECT id, phrase, normalized_phrase, meaning, origin_story, key_words, meaning_en, origin_story_en FROM idiom_origins")
    meta = {
        "schema_version": str(SCHEMA_VERSION),
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "word_count": str(len(all_words)),
        "core_word_count": str(len(word_rows)),
        "derived_word_count": str(len(derived_rows)),
        "derived_skipped_unattested": str(derived_skipped),
        "derived_policy": "yalnızca Wiktionary (Kaikki.org) dökümünde madde başı olarak tanıklanmış kural tabanlı türetmeler",
        "wiktionary_word_count": str(len(wikt_rows)),
        "wiktionary_ottoman_resolved": str(sum(1 for r in wikt_rows if wikt_by_row[r["id"]].get("ottoman_resolved"))),
        "wiktionary_ottoman_unverified": str(sum(1 for r in wikt_rows if r["origin_language_code"] == "ota")),
        "wiktionary_ottoman_reviewed": str(sum(1 for r in wikt_rows if wikt_by_row[r["id"]].get("reviewed"))),
        "wiktionary_attribution": WIKTIONARY_ATTRIBUTION if wikt_rows else "",
        "provenance_counts": json.dumps(dict(sorted(Counter(r["provenance"] for r in all_words).items())), ensure_ascii=False),
        "provenance_nisanyan_count": str(sum(1 for r in all_words if r["provenance_basis"] == "nisanyan")),
        "wiktionary_title_count": str(sum(1 for r in all_words if r["wiktionary_title"])),
        "curated_wiktionary_agree_count": str(sum(1 for r in all_words if r["wiktionary_origin"] and r["wiktionary_origin"] == r["origin_language_code"])),
        "curated_wiktionary_differ_count": str(sum(1 for r in all_words if r["wiktionary_origin"] and r["wiktionary_origin"] != r["origin_language_code"])),
        "root_family_count": str(len(family_rows)),
        "cognate_count": str(len(cognate_rows)),
        "false_friend_count": str(sum(1 for r in cognate_rows if r[10])),
        "cognates_excluded_by_audit": str(audit_stats["cognates_excluded"]),
        "cognate_direction_fixed_by_audit": str(audit_stats["cognate_direction_fixed"]),
        "target_language_count": str(len(TARGET_LANGUAGES)),
        "original_script_count": str(sum(1 for r in all_words if r["original_script"])),
        "old_turkic_script_count": str(enricher.stats["generated_old_turkic"]),
        "arabic_pattern_count": str(enricher.stats["pattern"]),
        "ipa_count": str(sum(1 for r in all_words if r["ipa"])),
        "data_source_count": str(len(DATA_SOURCES)),
        "toponym_count": str(len(toponym_rows)),
        "province_count": str(sum(1 for r in toponym_rows if r["kind"] == "il")),
        "toponym_origin_count": str(len({r["origin_language_code"] for r in toponym_rows})),
        "idiom_count": str(len(idiom_rows)),
        "person_name_count": str(len(name_rows)),
        "person_name_female_count": str(sum(1 for r in name_rows if r["gender"] == "k")),
        "person_name_male_count": str(sum(1 for r in name_rows if r["gender"] == "e")),
        "person_name_disputed_count": str(sum(1 for r in name_rows if r["is_disputed"])),
        "idiom_domain_count": str(len({r["domain_code"] for r in idiom_rows})),
        "idiom_word_link_count": str(len(idiom_word_rows)),
        "idiom_confidence_downgraded_by_audit": str(audit_stats["idiom_confidence_downgraded"]),
        "languages_supported": "tr,en",
        "english_gloss_count": str(sum(1 for r in all_words if r["english_gloss"])),
        "english_summary_count": str(sum(1 for r in all_words if r["etymology_summary_en"])),
        "english_source_meaning_count": str(sum(1 for r in all_words if r["source_meaning_en"])),
        "english_cognate_meaning_count": str(sum(1 for r in cognate_rows if r[11] and not r[11].endswith("(Turkish gloss)"))),
        "english_false_friend_count": str(sum(1 for r in cognate_rows if r[12] and not r[12].startswith("The meaning has shifted in"))),
        "english_toponym_story_count": str(en_counts["toponyms_translated"]),
        "english_idiom_story_count": str(en_counts["idioms_translated"]),
        "english_family_count": str(sum(1 for r in family_rows if r[1] in EN.families)),
        "english_sources": json.dumps(EN.stats),
        "glosses_attribution": "English glosses: Wiktionary contributors via Kaikki.org (CC BY-SA 4.0); summaries generated by EtimoTürk templates",
        "script_sources": json.dumps(enricher.stats, ensure_ascii=False),
        "generator": "DataPipeline/build_database.py",
        "data_repository": "https://github.com/vmutluer/etimoturk-data",
        "data_commit": data_commit,
    }
    cur.executemany("INSERT INTO meta VALUES (?,?)", list(meta.items()))
    conn.commit()
    cur.execute("VACUUM")
    conn.close()

    # --- JSON yedeği ----------------------------------------------------
    json_path = os.path.join(out_dir, "etymoturk.json")
    payload = {
        "meta": meta,
        "origin_languages": [{"code": c, "name": v[0], "color": v[1], "sort_order": v[2], "name_en": ORIGIN_LANGUAGES_EN.get(c, v[0])} for c, v in ORIGIN_LANGUAGES.items()],
        "languages": [{"code": c, "name": v[0], "flag": v[1], "region_group": v[2], "script": v[3], "country": v[4], "name_en": TARGET_LANGUAGES_EN.get(c, v[0]), "region_group_en": REGION_GROUPS_EN.get(v[2], v[2])} for c, v in TARGET_LANGUAGES.items()],
        "root_families": [dict(zip(("id", "root_code", "origin_language", "origin_language_name", "core_meaning", "explanation", "core_meaning_en", "explanation_en"), r)) for r in family_rows],
        "words": all_words,
        "shared_cognates": [dict(zip(("id", "word_id", "target_language_code", "target_language_name", "country_flag", "region_group", "foreign_word", "romanization", "meaning_in_target", "borrowing_direction", "false_friend_note", "meaning_in_target_en", "false_friend_note_en", "target_language_name_en", "region_group_en"), r)) for r in cognate_rows],
        "sample_texts": SAMPLE_TEXTS,
        "data_sources": DATA_SOURCES,
        "toponym_origins": [{"code": c, "name": v[0], "color": v[1], "sort_order": v[2], "era_note": v[3]} for c, v in TOPONYM_ORIGIN_LANGUAGES.items()],
        "toponyms": toponym_rows,
        "idiom_domains": [{"code": c, "name": v[0], "symbol": v[1], "color": v[2], "description": v[3]} for c, v in IDIOM_DOMAINS.items()],
        "idiom_origins": idiom_rows,
        "person_names": name_rows,
        "idiom_words": [dict(zip(("idiom_id", "word_id", "lemma"), r)) for r in idiom_word_rows],
    }
    with open(json_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, separators=(",", ":"))

    meta["elapsed_s"] = f"{time.time() - t0:.2f}"
    meta["db_bytes"] = str(os.path.getsize(db_path))
    return meta


def main():
    ap = argparse.ArgumentParser(description="EtimoTürk SQLite/JSON veri üretici")
    ap.add_argument("--out", default=os.path.join(HERE, "..", "data"))
    ap.add_argument("--data-commit", default="", help="üretimde kullanılan etimoturk-data commit'i (meta.data_commit)")
    args = ap.parse_args()
    meta = build(os.path.abspath(args.out), args.data_commit)
    for k, v in meta.items():
        print(f"{k:>22}: {v}")


if __name__ == "__main__":
    main()
