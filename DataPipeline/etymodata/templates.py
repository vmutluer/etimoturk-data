# -*- coding: utf-8 -*-
"""SQL şeması ve özgün etimolojik künye şablonları."""
import json
from .languages import ORIGIN_LANGUAGES, STAGE_NAMES, ATTESTATIONS, PERIODS
from .derivation import SUFFIX_LABELS

SCHEMA_SQL = """
PRAGMA page_size = 4096;
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE origin_languages (
    code TEXT PRIMARY KEY, name TEXT NOT NULL, color_hex TEXT NOT NULL, sort_order INTEGER NOT NULL,
    name_en TEXT NOT NULL DEFAULT '');
CREATE TABLE languages (
    code TEXT PRIMARY KEY, name TEXT NOT NULL, flag TEXT NOT NULL, region_group TEXT NOT NULL,
    script TEXT NOT NULL, country TEXT NOT NULL, name_en TEXT NOT NULL DEFAULT '', region_group_en TEXT NOT NULL DEFAULT '');
CREATE TABLE root_families (
    id INTEGER PRIMARY KEY, root_code TEXT NOT NULL UNIQUE, origin_language TEXT NOT NULL,
    origin_language_name TEXT NOT NULL, core_meaning TEXT NOT NULL, explanation TEXT NOT NULL,
    member_count INTEGER NOT NULL DEFAULT 0,
    core_meaning_en TEXT NOT NULL DEFAULT '', explanation_en TEXT NOT NULL DEFAULT '');
CREATE TABLE words (
    id INTEGER PRIMARY KEY,
    lemma TEXT NOT NULL,
    normalized_lemma TEXT NOT NULL,
    pos TEXT NOT NULL,
    origin_language_code TEXT NOT NULL REFERENCES origin_languages(code),
    origin_language_name TEXT NOT NULL,
    origin_period TEXT NOT NULL,
    root_family_id INTEGER REFERENCES root_families(id),
    source_form TEXT NOT NULL,
    source_meaning TEXT NOT NULL,
    etymology_summary TEXT NOT NULL,
    phonetic_evolution_json TEXT NOT NULL,
    historical_attestation TEXT NOT NULL,
    is_turcism_exporter INTEGER NOT NULL DEFAULT 0,
    is_disputed INTEGER NOT NULL DEFAULT 0,
    derived_from_id INTEGER REFERENCES words(id),
    derivation_suffix TEXT,
    cognate_count INTEGER NOT NULL DEFAULT 0,
    data_source TEXT NOT NULL DEFAULT 'curated' CHECK (data_source IN ('curated','derived','wiktionary')),
    original_script TEXT NOT NULL DEFAULT '',
    original_script_name TEXT NOT NULL DEFAULT '',
    transliteration TEXT NOT NULL DEFAULT '',
    ipa TEXT NOT NULL DEFAULT '',
    arabic_pattern TEXT,
    script_source TEXT NOT NULL DEFAULT '' CHECK (script_source IN ('', 'curated','generated_old_turkic','wiktionary','generated_arabic','generated_cyrillic','latin')),
    english_gloss TEXT NOT NULL DEFAULT '',
    etymology_summary_en TEXT NOT NULL DEFAULT '',
    source_meaning_en TEXT NOT NULL DEFAULT '',
    historical_attestation_en TEXT NOT NULL DEFAULT '',
    origin_period_en TEXT NOT NULL DEFAULT '');
CREATE INDEX idx_words_normalized ON words(normalized_lemma);
CREATE INDEX idx_words_script_name ON words(original_script_name);
CREATE INDEX idx_words_family ON words(root_family_id);
CREATE INDEX idx_words_origin ON words(origin_language_code);
CREATE INDEX idx_words_derived ON words(derived_from_id);
CREATE INDEX idx_words_source ON words(data_source);
CREATE TABLE shared_cognates (
    id INTEGER PRIMARY KEY,
    word_id INTEGER NOT NULL REFERENCES words(id),
    target_language_code TEXT NOT NULL REFERENCES languages(code),
    target_language_name TEXT NOT NULL,
    country_flag TEXT NOT NULL,
    region_group TEXT NOT NULL,
    foreign_word TEXT NOT NULL,
    romanization TEXT NOT NULL,
    meaning_in_target TEXT NOT NULL,
    borrowing_direction TEXT NOT NULL CHECK (borrowing_direction IN ('from_turkish','into_turkish','shared_ancestor')),
    false_friend_note TEXT,
    meaning_in_target_en TEXT NOT NULL DEFAULT '',
    false_friend_note_en TEXT,
    target_language_name_en TEXT NOT NULL DEFAULT '',
    region_group_en TEXT NOT NULL DEFAULT '');
CREATE INDEX idx_cognates_word ON shared_cognates(word_id);
CREATE INDEX idx_cognates_lang ON shared_cognates(target_language_code);
CREATE INDEX idx_cognates_region ON shared_cognates(region_group);
CREATE TABLE sample_texts (
    id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT NOT NULL, era TEXT NOT NULL, body TEXT NOT NULL);
CREATE TABLE data_sources (
    id INTEGER PRIMARY KEY,
    kind TEXT NOT NULL CHECK (kind IN ('public_domain','open_license','linguistic_fact','generated')),
    name TEXT NOT NULL, author TEXT NOT NULL, year TEXT NOT NULL, license TEXT NOT NULL,
    url TEXT NOT NULL, license_url TEXT NOT NULL, usage TEXT NOT NULL, fields TEXT NOT NULL,
    usage_en TEXT NOT NULL DEFAULT '');
CREATE VIRTUAL TABLE words_fts USING fts5(
    lemma, normalized_lemma, etymology_summary, source_form, source_meaning, original_script, english_gloss,
    content='words', content_rowid='id', tokenize='unicode61 remove_diacritics 2');

-- ---------------------------------------------------------------- Faz 4 (şema 3): yer adları
CREATE TABLE toponym_origins (
    code TEXT PRIMARY KEY, name TEXT NOT NULL, color_hex TEXT NOT NULL, sort_order INTEGER NOT NULL,
    era_note TEXT NOT NULL, name_en TEXT NOT NULL DEFAULT '', era_note_en TEXT NOT NULL DEFAULT '');
CREATE TABLE toponyms (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    normalized_name TEXT NOT NULL,
    kind TEXT NOT NULL,
    kind_name TEXT NOT NULL,
    province TEXT NOT NULL,
    region TEXT NOT NULL,
    plate_code INTEGER,
    origin_language_code TEXT NOT NULL REFERENCES toponym_origins(code),
    origin_language_name TEXT NOT NULL,
    oldest_form TEXT NOT NULL,
    oldest_stage TEXT NOT NULL,
    name_evolution_json TEXT NOT NULL,
    layer_count INTEGER NOT NULL,
    ancient_forms TEXT NOT NULL DEFAULT '',
    meaning TEXT NOT NULL,
    summary TEXT NOT NULL,
    story TEXT NOT NULL,
    source_note TEXT NOT NULL,
    era TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    meaning_en TEXT NOT NULL DEFAULT '',
    summary_en TEXT NOT NULL DEFAULT '',
    story_en TEXT NOT NULL DEFAULT '',
    kind_name_en TEXT NOT NULL DEFAULT '',
    region_en TEXT NOT NULL DEFAULT '',
    origin_language_name_en TEXT NOT NULL DEFAULT '');
CREATE INDEX idx_toponyms_normalized ON toponyms(normalized_name);
CREATE INDEX idx_toponyms_region ON toponyms(region);
CREATE INDEX idx_toponyms_province ON toponyms(province);
CREATE INDEX idx_toponyms_origin ON toponyms(origin_language_code);
CREATE INDEX idx_toponyms_kind ON toponyms(kind);
CREATE VIRTUAL TABLE toponyms_fts USING fts5(
    name, normalized_name, ancient_forms, meaning, story, meaning_en, story_en,
    content='toponyms', content_rowid='id', tokenize='unicode61 remove_diacritics 2');

-- ---------------------------------------------------------------- Faz 4 (şema 3): deyim kökenleri
CREATE TABLE idiom_domains (
    code TEXT PRIMARY KEY, name TEXT NOT NULL, symbol TEXT NOT NULL, color_hex TEXT NOT NULL,
    description TEXT NOT NULL, sort_order INTEGER NOT NULL,
    name_en TEXT NOT NULL DEFAULT '', description_en TEXT NOT NULL DEFAULT '');
CREATE TABLE idiom_origins (
    id INTEGER PRIMARY KEY,
    phrase TEXT NOT NULL UNIQUE,
    normalized_phrase TEXT NOT NULL,
    kind TEXT NOT NULL CHECK (kind IN ('deyim','atasözü','tabir','kalıp söz')),
    domain_code TEXT NOT NULL REFERENCES idiom_domains(code),
    domain_name TEXT NOT NULL,
    meaning TEXT NOT NULL,
    literal_sense TEXT NOT NULL,
    origin_story TEXT NOT NULL,
    era_code TEXT NOT NULL,
    origin_period TEXT NOT NULL,
    historical_attestation TEXT NOT NULL,
    source_note TEXT NOT NULL,
    confidence TEXT NOT NULL CHECK (confidence IN ('kesin','olası','halk_etimolojisi')),
    confidence_name TEXT NOT NULL,
    key_words TEXT NOT NULL,
    word_count INTEGER NOT NULL,
    meaning_en TEXT NOT NULL DEFAULT '',
    literal_sense_en TEXT NOT NULL DEFAULT '',
    origin_story_en TEXT NOT NULL DEFAULT '',
    domain_name_en TEXT NOT NULL DEFAULT '',
    origin_period_en TEXT NOT NULL DEFAULT '',
    historical_attestation_en TEXT NOT NULL DEFAULT '',
    confidence_name_en TEXT NOT NULL DEFAULT '');
CREATE INDEX idx_idioms_normalized ON idiom_origins(normalized_phrase);
CREATE INDEX idx_idioms_domain ON idiom_origins(domain_code);
CREATE INDEX idx_idioms_kind ON idiom_origins(kind);
CREATE TABLE idiom_words (
    idiom_id INTEGER NOT NULL REFERENCES idiom_origins(id),
    word_id INTEGER NOT NULL REFERENCES words(id),
    lemma TEXT NOT NULL,
    PRIMARY KEY (idiom_id, word_id));
CREATE INDEX idx_idiom_words_word ON idiom_words(word_id);
CREATE VIRTUAL TABLE idioms_fts USING fts5(
    phrase, normalized_phrase, meaning, origin_story, key_words, meaning_en, origin_story_en,
    content='idiom_origins', content_rowid='id', tokenize='unicode61 remove_diacritics 2');
CREATE TABLE person_names (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    normalized_name TEXT NOT NULL,
    gender TEXT NOT NULL CHECK (gender IN ('k','e','u')),
    origin_language_code TEXT NOT NULL REFERENCES origin_languages(code),
    origin_language_name TEXT NOT NULL,
    origin_language_name_en TEXT NOT NULL DEFAULT '',
    source_form TEXT NOT NULL,
    meaning TEXT NOT NULL,
    meaning_en TEXT NOT NULL DEFAULT '',
    components_json TEXT NOT NULL,
    root_family_id INTEGER REFERENCES root_families(id),
    related_word_id INTEGER REFERENCES words(id),
    related_lemma TEXT NOT NULL DEFAULT '',
    story TEXT NOT NULL,
    story_en TEXT NOT NULL DEFAULT '',
    note TEXT NOT NULL DEFAULT '',
    note_en TEXT NOT NULL DEFAULT '',
    is_disputed INTEGER NOT NULL DEFAULT 0);
CREATE INDEX idx_person_names_normalized ON person_names(normalized_name);
CREATE INDEX idx_person_names_origin ON person_names(origin_language_code);
CREATE INDEX idx_person_names_family ON person_names(root_family_id);
"""

POS_NAMES = {
    "n": "ad", "v": "eylem", "adj": "sıfat", "adv": "zarf", "pron": "adıl", "conj": "bağlaç",
    "num": "sayı", "intj": "ünlem", "postp": "ilgeç", "prop": "özel ad",
}
# "bir ad-dır", "bir sıfat-tır" gibi ek fiil biçimleri
POS_PREDICATE = {
    "n": "addır", "v": "eylemdir", "adj": "sıfattır", "adv": "zarftır", "pron": "adıldır",
    "conj": "bağlaçtır", "num": "sayıdır", "intj": "ünlemdir", "postp": "ilgeçtir", "prop": "özel addır",
}

# Ara durak: hangi dönem anahtarları Osmanlı Türkçesi aşaması gerektirir
OTTOMAN_ERAS = {"EAT", "YE", "DK", "OSM", "MEN", "EVL", "LO", "LOS", "KT", "OSM19", "RH"}
OLD_TURKIC_ERAS = {"ORH", "UYG", "DLT", "KB", "CC"}

_TR_CHARS = str.maketrans({"â": "a", "î": "i", "û": "u", "Â": "a", "Î": "i", "Û": "u", "I": "ı", "İ": "i"})


def normalize(text: str) -> str:
    return text.translate(_TR_CHARS).lower().replace("'", "").replace("’", "").strip()


def stage_name(code: str) -> str:
    return STAGE_NAMES.get(code, code)


def build_chain(entry):
    """[(aşama adı, biçim)] listesi üretir."""
    if entry.chain:
        chain = [(stage_name(c), f) for c, f in entry.chain]
        if entry.chain[-1][0] != "tr":
            chain.append((stage_name("tr"), entry.lemma))
        return chain
    chain = []
    o = entry.origin
    if o == "tr":
        if entry.era in OLD_TURKIC_ERAS:
            chain.append((stage_name("otk"), entry.source_form))
        elif entry.era in OTTOMAN_ERAS:
            # Eski Türkçe biçimi ayrıca belgelenmemiş bir sözcüğe "Eski Türkçe" aşaması yakıştırılmaz; kaynak biçim
            # ilk tanıklandığı dönemin adıyla verilir (bileşikler ve türetmeler için de doğru olan budur).
            chain.append((turkic_source_stage(entry), entry.source_form))
        elif entry.era in ("DD", "TDK", "CUM", "MOD", "NEW"):
            chain.append(("Türetme kökü", entry.source_form))
        else:
            chain.append((stage_name("otk"), entry.source_form))
    else:
        chain.append((stage_name(o), entry.source_form))
        # Not: Osmanlı Türkçesi aşaması yalnızca ayrı bir Osmanlıca biçim verildiğinde (zincir DSL'i) gösterilir;
        # Arapça/Farsça kaynak biçimi aynen kopyalayan yapay bir Osmanlıca aşaması üretilmez.
    if chain and chain[-1][1] == entry.lemma and chain[-1][0] != stage_name("tr"):
        chain[-1] = (stage_name("tr"), entry.lemma)
    else:
        chain.append((stage_name("tr"), entry.lemma))
    return chain


def turkic_source_stage(entry) -> str:
    """Osmanlı dönemlerinde ilk tanıklanan öz Türkçe sözcükler için kaynak biçimin aşama adı.

    Kaynak biçim sözcüğün kendisiyse ilk tanıklandığı dönem (Eski Anadolu / Osmanlı Türkçesi) verilir; kök, gövde
    ya da öbek ise dönem iddiası yapılmadan "Türkçe kaynak biçim" denir.
    """
    if entry.source_form.strip() == entry.lemma:
        return stage_name("eat") if entry.era in ("EAT", "YE", "DK") else stage_name("ota")
    return "Türkçe kaynak biçim"


def chain_to_json(chain):
    return json.dumps([{"stage": s, "form": f} for s, f in chain], ensure_ascii=False)


def chain_to_text(chain):
    return " → ".join(f"{s} *{f}*" for s, f in chain)


def summary_for(entry, family_code: str | None) -> str:
    o = entry.origin
    name = ORIGIN_LANGUAGES.get(o, ("Bilinmeyen",))[0]
    pos = POS_PREDICATE.get(entry.pos, entry.pos + "tır")
    src, meaning = entry.source_form, entry.source_meaning
    chain = build_chain(entry)
    if o == "tr":
        if entry.era == "DD":
            core = (f"{entry.lemma}, Dil Devrimi döneminde (1932 sonrası) Türkçe {src} kökünden türetilmiş bir {pos}; "
                    f"anlamı \"{meaning}\" olup yabancı kökenli karşılığının yerine önerilmiştir.")
        elif entry.era in ("MOD", "NEW", "TDK", "CUM"):
            core = (f"{entry.lemma}, 20. yüzyılda Türkçe {src} kökünden türetilmiş bir {pos} (\"{meaning}\").")
        elif entry.era in OLD_TURKIC_ERAS:
            core = (f"{entry.lemma}, Eski Türkçe {src} (\"{meaning}\") biçiminden ses değişimleriyle gelişen öz Türkçe bir {pos}.")
        elif " " in src or "-" in src.strip("-") or src == entry.lemma:
            core = (f"{entry.lemma}, Türkçe {src} (\"{meaning}\") öğelerinden oluşmuş öz Türkçe bir {pos}; "
                    f"ilk yazılı kaydı {ATTESTATIONS.get(entry.era, entry.era)} dönemindedir.")
        else:
            core = (f"{entry.lemma}, Türkçe {src} (\"{meaning}\") biçiminden gelişen öz Türkçe bir {pos}; "
                    f"ilk yazılı kaydı {ATTESTATIONS.get(entry.era, entry.era)} dönemindedir.")
    elif o == "ar":
        core = (f"{entry.lemma}, Arapça {src} (\"{meaning}\") sözcüğünden Türkçeye geçmiştir; "
                f"Arapçanın kalıp sistemine göre türemiş bir {pos}.")
    elif o == "fa":
        core = (f"{entry.lemma}, Farsça {src} (\"{meaning}\") sözcüğünden alınmıştır; "
                f"Türkçeye İran kültür çevresiyle temas sonucu girmiş bir {pos}.")
    elif o == "fr":
        core = (f"{entry.lemma}, Fransızca {src} (\"{meaning}\") sözcüğünden 19.–20. yüzyılda Batılılaşma döneminde alınmıştır.")
    elif o == "it":
        core = (f"{entry.lemma}, İtalyanca (Venedik/Ceneviz ticaret dili) {src} (\"{meaning}\") sözcüğünden Akdeniz ticareti yoluyla alınmıştır.")
    elif o == "el":
        core = (f"{entry.lemma}, Yunanca (Rumca) {src} (\"{meaning}\") sözcüğünden Anadolu'daki yüzyıllar süren komşuluk sonucu alınmıştır.")
    elif o == "en":
        core = (f"{entry.lemma}, İngilizce {src} (\"{meaning}\") sözcüğünden 20. yüzyılda küresel kültür ve teknoloji yoluyla alınmıştır.")
    elif o == "mn":
        core = (f"{entry.lemma}, Moğolca {src} (\"{meaning}\") sözcüğünden Orta Asya'daki Türk-Moğol etkileşimiyle alınmıştır.")
    elif o == "sog":
        core = (f"{entry.lemma}, Soğdca {src} (\"{meaning}\") sözcüğünden İpek Yolu ticareti döneminde Eski Türkçeye girmiştir.")
    elif o == "sl":
        core = (f"{entry.lemma}, Slav dillerinden ({src}, \"{meaning}\") Balkan ve Karadeniz komşuluğu yoluyla alınmıştır.")
    elif o == "hy":
        core = (f"{entry.lemma}, Ermenice {src} (\"{meaning}\") sözcüğünden Anadolu'daki uzun komşuluk sonucu alınmıştır.")
    elif o == "unk":
        core = (f"{entry.lemma} (\"{meaning}\") sözcüğünün kaynak dili kesin olarak saptanamamıştır; "
                f"ilk yazılı kaydı {ATTESTATIONS.get(entry.era, entry.era)} dönemindedir.")
    else:
        core = (f"{entry.lemma}, {name} kökenli {src} (\"{meaning}\") sözcüğünden Türkçeye geçmiştir.")
    parts = [core]
    if len(chain) > 1:
        parts.append("Yolculuğu: " + chain_to_text(chain) + ".")
    if family_code:
        parts.append(f"Kök ailesi: {family_code}.")
    if entry.disputed:
        parts.append("Not: Bu sözcüğün kökeni dilbilimciler arasında tartışmalıdır.")
    return " ".join(parts)


def make_word_row(wid: int, entry, family_ids, turcism_lemmas, cognate_count):
    fam_id = family_ids.get(entry.family) if entry.family else None
    chain = build_chain(entry)
    return {
        "id": wid,
        "lemma": entry.lemma,
        "normalized_lemma": normalize(entry.lemma),
        "pos": entry.pos,
        "origin_language_code": entry.origin,
        "origin_language_name": ORIGIN_LANGUAGES.get(entry.origin, ("Bilinmeyen",))[0],
        "origin_period": PERIODS.get(entry.era, entry.era),
        "root_family_id": fam_id,
        "source_form": entry.source_form,
        "source_meaning": entry.source_meaning,
        "etymology_summary": summary_for(entry, entry.family or None),
        "phonetic_evolution_json": chain_to_json(chain),
        "historical_attestation": ATTESTATIONS.get(entry.era, entry.era),
        "is_turcism_exporter": 1 if entry.lemma in turcism_lemmas else 0,
        "is_disputed": 1 if entry.disputed else 0,
        "derived_from_id": None,
        "derivation_suffix": None,
        "cognate_count": cognate_count.get(entry.lemma, 0),
        "data_source": "curated",
        "original_script": "", "original_script_name": "", "transliteration": "", "ipa": "",
        "arabic_pattern": None, "script_source": "",
        "english_gloss": "", "etymology_summary_en": "", "source_meaning_en": "", "historical_attestation_en": "", "origin_period_en": "",
    }


def make_derived_row(wid: int, base, d, base_id: int, family_ids):
    label, desc = SUFFIX_LABELS[d.suffix_key]
    name = ORIGIN_LANGUAGES.get(base.origin, ("Bilinmeyen",))[0]
    summary = (f"{d.lemma}, {base.lemma} sözcüğünden {d.suffix_surface} ({desc}) ile türetilmiştir. "
               f"Kök sözcük {name} kökenlidir: {base.source_form} (\"{base.source_meaning}\").")
    chain = build_chain(base)
    chain.append(("Türkçe yapım eki", f"{base.lemma} + {d.suffix_surface}"))
    period = "Türkçe türetme (ek: " + label + ")"
    return {
        "id": wid,
        "lemma": d.lemma,
        "normalized_lemma": normalize(d.lemma),
        "pos": d.pos,
        "origin_language_code": base.origin,
        "origin_language_name": name,
        "origin_period": period,
        "root_family_id": family_ids.get(base.family) if base.family else None,
        "source_form": base.source_form,
        "source_meaning": base.source_meaning,
        "etymology_summary": summary,
        "phonetic_evolution_json": chain_to_json(chain),
        "historical_attestation": "Türetilmiş sözcük – kök: " + ATTESTATIONS.get(base.era, base.era),
        "is_turcism_exporter": 0,
        "is_disputed": 1 if base.disputed else 0,
        "derived_from_id": base_id,
        "derivation_suffix": d.suffix_surface,
        "cognate_count": 0,
        "data_source": "derived",
        "original_script": "", "original_script_name": "", "transliteration": "", "ipa": "",
        "arabic_pattern": None, "script_source": "",
        "english_gloss": "", "etymology_summary_en": "", "source_meaning_en": "", "historical_attestation_en": "", "origin_period_en": "",
    }


WIKT_ORIGIN_SENTENCE = {
    "tr": "Eski Türkçeden kalıtılan öz Türkçe bir sözcüktür",
    "ar": "Arapça kökenli olup Osmanlı Türkçesi yoluyla Türkçeye girmiştir",
    "fa": "Farsça kökenli olup Osmanlı Türkçesi yoluyla Türkçeye girmiştir",
    "fr": "Fransızcadan 19.–20. yüzyılda alınmıştır",
    "it": "İtalyancadan (Akdeniz ticaret dili) alınmıştır",
    "el": "Yunancadan (Rumca) Anadolu komşuluğuyla alınmıştır",
    "en": "İngilizceden 20. yüzyılda alınmıştır",
    "ota": "Türkçeye Osmanlı Türkçesi üzerinden geçmiş bir sözcüktür; asıl kaynak dili açık bir kaynakla henüz doğrulanmadı",
}


def make_wiktionary_row(wid: int, w: dict, cognate_count: int):
    """ETL (Kaikki.org / Wiktionary) kaydından özgün künye satırı üretir; yalnızca yapısal olgular kullanılır."""
    origin = w["origin"]
    name = ORIGIN_LANGUAGES.get(origin, ("Bilinmeyen",))[0]
    pos = POS_PREDICATE.get(w["pos"], "sözcüktür")
    src = w.get("source_form") or w["lemma"]
    script = w.get("source_script") or ""
    gloss = w.get("gloss_en") or ""
    chain = [(stage_name(c), f) for c, f in w.get("chain", []) if f]
    if not chain or chain[-1][0] != stage_name("tr"):
        chain.append((stage_name("tr"), w["lemma"]))
    sentence = WIKT_ORIGIN_SENTENCE.get(origin, f"{name} kökenli bir sözcüktür")
    src_text = f"{src}" + (f" ({script})" if script and script != src else "")
    parts = [f"{w['lemma']}, {sentence}; kaynak biçim {src_text}" + (f", İng. \"{gloss}\"" if gloss else "") + f". Sözcük türü: {pos.replace('dır', '').replace('dir', '').replace('tır', '').replace('tir', '')}."]
    if len(chain) > 1:
        parts.append("Yolculuğu: " + chain_to_text(chain) + ".")
    method = w.get("method", "")
    if method.startswith("internal:"):
        parts.append(f"Türkçe içi türetme: {method.split(':', 1)[1]} sözcüğünden.")
    parts.append("Yapısal veri: Wiktionary (Kaikki.org dökümü), CC BY-SA 4.0.")
    return {
        "id": wid,
        "lemma": w["lemma"],
        "normalized_lemma": normalize(w["lemma"]),
        "pos": w["pos"],
        "origin_language_code": origin,
        "origin_language_name": name,
        "origin_period": PERIODS["WIKT"],
        "root_family_id": None,
        "source_form": src,
        "source_meaning": ("İng. " + gloss) if gloss else "",
        "etymology_summary": " ".join(parts),
        "phonetic_evolution_json": chain_to_json(chain),
        "historical_attestation": ATTESTATIONS["WIKT"],
        "is_turcism_exporter": 0,
        "is_disputed": 1 if origin == "ota" else 0,
        "derived_from_id": None,
        "derivation_suffix": None,
        "cognate_count": cognate_count,
        "data_source": "wiktionary",
        "original_script": "", "original_script_name": "", "transliteration": "", "ipa": "",
        "arabic_pattern": None, "script_source": "",
        "english_gloss": "", "etymology_summary_en": "", "source_meaning_en": "", "historical_attestation_en": "", "origin_period_en": "",
    }
