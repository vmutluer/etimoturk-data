#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İçerik denetçisi: üretilmiş etymoturk.sqlite dosyasının doğruluk ve tutarlılığını ölçer.

`validate_corpora.py` yalnızca biçimsel denetim yapar (alan sayısı, kod geçerliliği); bu araç içeriğe bakar:

  1. curated ↔ Wiktionary çapraz kontrolü: her iki kaynağın da kesin köken dili iddiası olan sözcüklerde uyum oranı
  2. Wiktionary katmanı: harf tabanlı (script-heuristic) köken ataması kalmamalı
  3. Türetme katmanı: her türetme açık lisanslı bir sözlükte madde başı olarak tanıklanmış olmalı
  4. Ortak sözcükler: Türk dilleriyle "into_turkish" yönü olamaz; dışlanmış çeviri çiftleri bulunmamalı;
     biçim benzerliği çok düşük satırlar incelenmek üzere raporlanır
  5. Deyimler: "kesin" güven düzeyi yalnızca köken anlatısını belgeleyen kaynakla
  6. Künye zincirleri: Arapça/Farsça kaynak biçimi aynen kopyalayan yapay Osmanlıca aşaması ve modern Türkçe
     bileşiklere yakıştırılmış "Eski Türkçe" aşaması bulunmamalı
  7. Yer adları: koordinatlar Türkiye sınırları içinde; 81 il eksiksiz
  8. Bütünlük: yetim kayıtlar, boş zorunlu alanlar

Kullanım: python3 DataPipeline/audit_database.py [--db App/Resources/etymoturk.sqlite] [--report rapor.csv] [--min-agreement 0.90]
Çıkış kodu 0 = tüm eşikler sağlandı; 1 = en az bir hata. Uyarılar (W) çıkış kodunu etkilemez.
"""
import argparse
import csv
import difflib
import json
import os
import sqlite3
import sys
import unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from etymodata.audit_rules import TURKIC_TARGETS, is_excluded
from etymodata.phase4 import IDIOM_NARRATIVE_SOURCES
from etymodata.parsing import load_generated
from etymodata.templates import normalize

errors, warnings, report_rows = [], [], []


def E(msg):
    errors.append(msg)


def W(msg):
    warnings.append(msg)


def _norm_form(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    table = {"ş": "s", "ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ü": "u", "ł": "l", "đ": "d", "ț": "t", "ș": "s", "ż": "z", "ś": "s"}
    s = "".join(table.get(ch, ch) for ch in s)
    return "".join(ch for ch in s if ch.isalnum())


def form_similarity(a: str, b: str) -> float:
    a, b = _norm_form(a), _norm_form(b)
    if not a or not b:
        return 0.0
    full = difflib.SequenceMatcher(None, a, b).ratio()
    head = difflib.SequenceMatcher(None, a[:4], b[:4]).ratio() * 0.9
    return max(full, head)


def check_cross_source(conn, wikt, min_agreement):
    by_key = {}
    for w in wikt.get("words", []):
        by_key.setdefault((w["lemma"].lower(), w["pos"]), w)
    agree = disagree = 0
    for lemma, pos, origin, src, disputed in conn.execute(
            "SELECT lemma, pos, origin_language_code, source_form, is_disputed FROM words WHERE data_source='curated'"):
        w = by_key.get((lemma.lower(), pos))
        if not w or w["origin"] in ("ota", "tr") or w["method"].startswith("internal"):
            continue
        if origin == w["origin"]:
            agree += 1
        else:
            disagree += 1
            report_rows.append(["curated_vs_wiktionary", lemma, pos, origin, src, w["origin"], w["source_form"],
                                "tartışmalı işaretli" if disputed else "elle karar ver (yakın/uzak kaynak farkı olabilir)"])
    total = agree + disagree
    rate = agree / total if total else 1.0
    print(f"[1] curated ↔ Wiktionary: {total} ortak sözcük, uyum {rate:.1%} ({disagree} uyuşmazlık raporda)")
    if rate < min_agreement:
        E(f"curated ↔ Wiktionary uyumu {rate:.1%} < {min_agreement:.0%}")
    return rate


def check_wiktionary_layer(conn, wikt):
    by_key = {(w["lemma"].lower(), w["pos"]): w for w in wikt.get("words", [])}
    heuristic = 0
    for lemma, pos, origin in conn.execute("SELECT lemma, pos, origin_language_code FROM words WHERE data_source='wiktionary'"):
        w = by_key.get((lemma.lower(), pos))
        if w and "script-heuristic" in w.get("method", "") and origin in ("ar", "fa"):
            heuristic += 1
            report_rows.append(["wiktionary_script_heuristic", lemma, pos, origin, "", w["origin"], w["source_form"], "harf sezgisi"])
    ota = conn.execute("SELECT COUNT(*) FROM words WHERE data_source='wiktionary' AND origin_language_code='ota'").fetchone()[0]
    undisputed_ota = conn.execute("SELECT COUNT(*) FROM words WHERE origin_language_code='ota' AND is_disputed=0").fetchone()[0]
    print(f"[2] Wiktionary katmanı: {heuristic} harf-sezgisi kökeni, {ota} kayıt 'ota' (Osmanlı Türkçesi üzerinden, asıl kaynak doğrulanmadı)")
    if heuristic:
        E(f"{heuristic} Wiktionary kaydı harf sezgisiyle Arapça/Farsça sayılmış")
    if undisputed_ota:
        E(f"{undisputed_ota} 'ota' kaydı tartışmalı işaretlenmemiş")


def check_derived(conn, wikt, glosses):
    attested = {normalize(w["lemma"]) for w in wikt.get("words", [])}
    attested |= {normalize(k) for k in (glosses or {}).get("glosses", {})}
    rows = conn.execute("""SELECT lemma, cognate_count, (SELECT COUNT(*) FROM idiom_words i WHERE i.word_id = words.id)
                           FROM words WHERE data_source='derived'""").fetchall()
    # ortak sözcük ya da deyim kaydının başvurduğu türetmeler elle seçilmiş sayılır
    bad = [r[0] for r in rows if attested and normalize(r[0]) not in attested and not (r[1] or r[2])]
    print(f"[3] türetme katmanı: {len(rows)} kayıt, {len(bad)} tanıklanmamış")
    for lemma in bad[:50]:
        report_rows.append(["derived_unattested", lemma, "", "", "", "", "", "sözlükte madde başı değil"])
    if bad:
        E(f"{len(bad)} türetilmiş sözcük açık lisanslı sözlükte tanıklanmamış")


def check_cognates(conn):
    rows = conn.execute("""SELECT w.lemma, s.target_language_code, s.foreign_word, s.romanization, s.meaning_in_target,
                                  s.borrowing_direction, w.origin_language_code
                           FROM shared_cognates s JOIN words w ON w.id = s.word_id""").fetchall()
    wrong_dir = [r for r in rows if r[1] in TURKIC_TARGETS and r[5] == "into_turkish"]
    excluded = [r for r in rows if is_excluded(r[0], r[1], r[2])]
    placeholder = sum(1 for r in rows if r[4] == r[0])
    low = []
    for lemma, lang, fw, rom, meaning, direction, origin in rows:
        s = form_similarity(lemma, rom or fw)
        if s < 0.34:
            low.append((lang, lemma, fw, rom, meaning, direction, round(s, 2)))
    print(f"[4] ortak sözcükler: {len(rows)} satır; yön hatası {len(wrong_dir)}; dışlanmış çift {len(excluded)}; "
          f"anlam alanı lemma ile aynı {placeholder} ({placeholder / max(len(rows), 1):.0%}); düşük benzerlik {len(low)} (uyarı)")
    for r in wrong_dir:
        report_rows.append(["cognate_direction", r[0], "", r[1], r[2], "", "", "Türk diliyle into_turkish"])
    for r in low:
        report_rows.append(["cognate_low_similarity", r[1], "", r[0], r[2], "", r[3], f"benzerlik {r[6]} — akraba mı, çeviri mi? incele"])
    if wrong_dir:
        E(f"{len(wrong_dir)} ortak sözcük satırında Türk diliyle 'into_turkish' yönü")
    if excluded:
        E(f"{len(excluded)} dışlanmış çeviri çifti hâlâ veritabanında")
    if low:
        W(f"{len(low)} ortak sözcük satırında biçim benzerliği düşük (raporda cognate_low_similarity)")


def check_idioms(conn):
    rows = conn.execute("SELECT phrase, confidence, source_note FROM idiom_origins").fetchall()
    over = [r for r in rows if r[1] == "kesin" and not any(k in r[2] for k in IDIOM_NARRATIVE_SOURCES)]
    dist = Counter(r[1] for r in rows)
    print(f"[5] deyimler: {len(rows)} kayıt; güven dağılımı {dict(dist)}; kaynaksız 'kesin' {len(over)}")
    for r in over:
        report_rows.append(["idiom_overconfident", r[0], "", r[1], "", "", "", r[2]])
    if over:
        E(f"{len(over)} deyimde köken anlatısı belgelenmeden 'kesin' güven düzeyi")


def check_chains(conn):
    ota_copy = old_turkic_modern = 0
    for lemma, origin, src, chain, period in conn.execute(
            "SELECT lemma, origin_language_code, source_form, phonetic_evolution_json, origin_period FROM words WHERE data_source='curated'"):
        stages = json.loads(chain)
        if origin in ("ar", "fa") and any(st["stage"] == "Osmanlı Türkçesi" and st["form"] == src for st in stages):
            ota_copy += 1
        old_turkic_period = period.startswith(("Eski Türkçe", "Karahanlı", "Kıpçak"))
        # elle yazılmış çok aşamalı zincirler (ör. otk:batrak > fa:bayrak-dār > tr) denetim dışıdır
        if origin == "tr" and len(stages) == 2 and stages[0]["stage"] == "Eski Türkçe" and not old_turkic_period:
            old_turkic_modern += 1
            report_rows.append(["chain_old_turkic_label", lemma, "", origin, src, "", "", "modern/bileşik sözcüğe 'Eski Türkçe' aşaması"])
    print(f"[6] künye zincirleri: Osmanlıca kopya aşaması {ota_copy}; modern sözcükte 'Eski Türkçe' etiketi {old_turkic_modern}")
    if ota_copy:
        E(f"{ota_copy} zincirde Arapça/Farsça biçimi kopyalayan yapay Osmanlıca aşaması")
    if old_turkic_modern:
        E(f"{old_turkic_modern} modern/bileşik sözcüğe 'Eski Türkçe' aşaması yakıştırılmış")


def check_toponyms(conn):
    rows = conn.execute("SELECT name, kind, latitude, longitude FROM toponyms").fetchall()
    out = [r for r in rows if not (35.5 <= r[2] <= 42.3 and 25.5 <= r[3] <= 45.0)]
    provinces = conn.execute("SELECT COUNT(DISTINCT plate_code) FROM toponyms WHERE kind='il'").fetchone()[0]
    print(f"[7] yer adları: {len(rows)} kayıt, {provinces} il, sınır dışı koordinat {len(out)}")
    for r in out:
        report_rows.append(["toponym_coords", r[0], r[1], "", f"{r[2]},{r[3]}", "", "", "Türkiye sınırları dışında"])
    if out:
        E(f"{len(out)} yer adının koordinatı Türkiye sınırları dışında")
    if provinces != 81:
        E(f"il sayısı {provinces} ≠ 81")


def check_names(conn):
    """[9] kişi adları: sayı, cins dağılımı, kök ailesi/ilgili sözcük bağı oranı, çift dilli hikâye, boş alan."""
    n = conn.execute("SELECT COUNT(*) FROM person_names").fetchone()[0]
    if n == 0:
        print("[9] kişi adları: tablo boş")
        return
    g = dict(conn.execute("SELECT gender, COUNT(*) FROM person_names GROUP BY gender").fetchall())
    linked = conn.execute("SELECT COUNT(*) FROM person_names WHERE root_family_id IS NOT NULL OR related_word_id IS NOT NULL").fetchone()[0]
    empty = conn.execute("SELECT COUNT(*) FROM person_names WHERE story='' OR story_en='' OR meaning='' OR meaning_en='' OR components_json='[]'").fetchone()[0]
    bad_fam = conn.execute("""SELECT COUNT(*) FROM person_names p JOIN root_families f ON f.id=p.root_family_id
                              WHERE f.origin_language <> p.origin_language_code AND p.origin_language_code NOT IN ('tr')""").fetchone()[0]
    origins = conn.execute("SELECT COUNT(DISTINCT origin_language_code) FROM person_names").fetchone()[0]
    print(f"[9] kişi adları: {n} kayıt (kadın {g.get('k',0)}, erkek {g.get('e',0)}, ortak {g.get('u',0)}); {origins} köken dili; "
          f"sözlüğe bağlı {linked} ({linked*100//n}%); boş alan {empty}; köken dili aileyle çelişen {bad_fam}")
    if empty:
        E(f"{empty} kişi adında boş zorunlu alan")
    if bad_fam:
        for r in conn.execute("""SELECT p.name, p.origin_language_code, f.root_code, f.origin_language FROM person_names p
                                 JOIN root_families f ON f.id=p.root_family_id WHERE f.origin_language <> p.origin_language_code
                                 AND p.origin_language_code NOT IN ('tr')""").fetchall():
            W(f"kişi adı {r[0]} ({r[1]}) ailesi {r[2]} ({r[3]}) ile farklı dilde")


def check_integrity(conn):
    fk = conn.execute("PRAGMA foreign_key_check").fetchall()
    orphan_cog = conn.execute("SELECT COUNT(*) FROM shared_cognates s LEFT JOIN words w ON w.id=s.word_id WHERE w.id IS NULL").fetchone()[0]
    empty = conn.execute("SELECT COUNT(*) FROM words WHERE lemma='' OR source_form='' OR etymology_summary=''").fetchone()[0]
    print(f"[8] bütünlük: foreign_key_check {len(fk)}, yetim ortak sözcük {orphan_cog}, boş zorunlu alan {empty}")
    if fk or orphan_cog or empty:
        E("bütünlük hatası (foreign key / yetim kayıt / boş alan)")


def check_provenance(conn):
    """Şema 6: her sözcüğün künye kaynağı dolu ve tutarlı olmalı."""
    cols = {r[1] for r in conn.execute("PRAGMA table_info(words)")}
    if "provenance" not in cols:
        print("[10] künye kaynağı: şema 6 öncesi veritabanı, atlandı")
        return
    empty = conn.execute("SELECT COUNT(*) FROM words WHERE provenance = ''").fetchone()[0]
    wrong_source = conn.execute("""SELECT COUNT(*) FROM words WHERE
        (provenance IN ('curated') AND data_source <> 'curated') OR
        (provenance = 'derived' AND data_source <> 'derived') OR
        (provenance IN ('wiktionary','wiktionary_ottoman','review') AND data_source <> 'wiktionary')""").fetchone()[0]
    basis_outside_review = conn.execute("SELECT COUNT(*) FROM words WHERE provenance_basis <> '' AND provenance <> 'review'").fetchone()[0]
    ota_resolved = conn.execute("SELECT COUNT(*) FROM words WHERE provenance IN ('wiktionary_ottoman','review') AND origin_language_code = 'ota'").fetchone()[0]
    print(f"[10] künye kaynağı: boş {empty}, kaynak türüyle çelişen {wrong_source}, inceleme dışı dayanak {basis_outside_review}, "
          f"çözülmüş görünüp ota kalan {ota_resolved}")
    if empty or wrong_source or basis_outside_review or ota_resolved:
        E("künye kaynağı tutarsız (provenance)")


def main():
    ap = argparse.ArgumentParser(description="EtimoTürk içerik denetçisi")
    ap.add_argument("--db", default=os.path.join(HERE, "..", "data", "etymoturk.sqlite"))
    ap.add_argument("--report", default=None, help="şüpheli kayıtların CSV raporu")
    ap.add_argument("--min-agreement", type=float, default=0.90)
    args = ap.parse_args()
    conn = sqlite3.connect(args.db)
    wikt = load_generated("wiktionary_tr") or {"words": []}
    glosses = load_generated("glosses_en")
    meta = dict(conn.execute("SELECT key, value FROM meta").fetchall())
    print(f"veritabanı: {args.db} (şema {meta.get('schema_version')}, {meta.get('generated_at')})")
    check_cross_source(conn, wikt, args.min_agreement)
    check_wiktionary_layer(conn, wikt)
    check_derived(conn, wikt, glosses)
    check_cognates(conn)
    check_idioms(conn)
    check_chains(conn)
    check_toponyms(conn)
    check_names(conn)
    check_integrity(conn)
    check_provenance(conn)
    if args.report:
        with open(args.report, "w", newline="", encoding="utf-8") as fh:
            wr = csv.writer(fh)
            wr.writerow(["kategori", "lemma", "pos", "mevcut_koken/dil", "mevcut_kaynak_bicim", "wiktionary_koken", "wiktionary_bicim", "not"])
            wr.writerows(report_rows)
        print(f"rapor: {args.report} ({len(report_rows)} satır)")
    for w in warnings:
        print("W", w)
    for e in errors:
        print("E", e)
    print(f"{len(errors)} hata, {len(warnings)} uyarı")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
