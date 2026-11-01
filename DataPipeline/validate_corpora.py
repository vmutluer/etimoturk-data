#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Korpus doğrulayıcı: veritabanını üretmeden tüm DSL bloklarını ayrıştırır ve hataları listeler.

Kullanım:  python3 DataPipeline/validate_corpora.py [--module ad]
Çıkış kodu 0 = hata yok. Uyarılar (W) işi durdurmaz, hatalar (E) build_database.py'yi bozar ya da testleri kırar.
"""
import argparse
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from etymodata.languages import ORIGIN_LANGUAGES, STAGE_NAMES, TARGET_LANGUAGES, ATTESTATIONS, PERIODS
from etymodata.parsing import (parse_lexicon, parse_families, parse_cognates, parse_toponyms, parse_idioms,
                               corpora_modules, load_generated, MULTIWORD_ALLOW, _parse_records)
from etymodata.templates import POS_NAMES, normalize
from etymodata.phase4 import (TOPONYM_ORIGIN_LANGUAGES, TOPONYM_STAGE_NAMES, TOPONYM_KINDS, TURKISH_REGIONS,
                              IDIOM_DOMAINS, IDIOM_KINDS, IDIOM_CONFIDENCE)
from etymodata import derivation

errors, warnings = [], []


def E(msg): errors.append(msg)
def W(msg): warnings.append(msg)


def check_words(module_filter):
    """Her modülün WORDS bloğunu satır satır denetler (parse_lexicon sessizce atladığı sorunları da bildirir)."""
    family_codes = {f.code for f in parse_families()}
    stats = {}
    seen = set()
    for m in corpora_modules():
        name = m.__name__.split(".")[-1]
        if not hasattr(m, "WORDS"):
            continue
        n = 0
        for raw in m.WORDS.strip().splitlines():
            raw = raw.strip()
            if not raw or raw.startswith("#"):
                continue
            parts = raw.split("|")
            if len(parts) != 8:
                E(f"[{name}] WORDS satırı 8 alan değil ({len(parts)}): {raw[:80]}")
                continue
            lemma, pos, origin, src, meaning, era, family, chain = parts
            if " " in lemma and lemma not in MULTIWORD_ALLOW:
                W(f"[{name}] çok sözcüklü madde atlanacak: {lemma}")
                continue
            if pos not in POS_NAMES:
                E(f"[{name}] bilinmeyen sözcük türü '{pos}': {lemma}")
            o = origin.rstrip("?")
            if o not in ORIGIN_LANGUAGES:
                E(f"[{name}] bilinmeyen köken kodu '{origin}': {lemma}")
            if era not in PERIODS:
                E(f"[{name}] bilinmeyen dönem kodu '{era}': {lemma}")
            if not src:
                E(f"[{name}] kaynak biçim boş: {lemma}")
            if not meaning:
                E(f"[{name}] kaynak anlam boş: {lemma}")
            if family and family not in family_codes:
                E(f"[{name}] tanımsız kök ailesi '{family}': {lemma}")
            if chain:
                for stage in chain.split(">"):
                    code, _, form = stage.partition(":")
                    if code.strip() not in STAGE_NAMES:
                        W(f"[{name}] zincirde bilinmeyen aşama kodu '{code.strip()}': {lemma}")
                    if not form.strip():
                        E(f"[{name}] zincir aşamasında biçim boş: {lemma} ({stage})")
            if (lemma, pos) in seen:
                W(f"[{name}] yinelenen madde (ilk kayıt kazanır): {lemma}|{pos}")
            seen.add((lemma, pos))
            n += 1
        stats[name] = n
    return stats


def check_families(lexicon):
    members = defaultdict(int)
    for e in lexicon:
        if e.family:
            members[e.family] += 1
    stats = Counter()
    seen = set()
    stated_root = {}  # kod -> açıklamada yazılan kök (ör. "ḥ-c-r"); yinelenen tanımlarda farklı kök = karışma
    root_rx = re.compile(r"(?:Arapça|Farsça|Latince|Eski Yunanca|Yunanca|Eski Türkçe)\s+([^\s;,\"]+)")
    for m in corpora_modules():
        name = m.__name__.split(".")[-1]
        if not hasattr(m, "FAMILIES"):
            continue
        for raw in m.FAMILIES.strip().splitlines():
            raw = raw.strip()
            if not raw or raw.startswith("#"):
                continue
            parts = raw.split("|", 3)
            if len(parts) != 4:
                E(f"[{name}] FAMILIES satırı 4 alan değil: {raw[:80]}")
                continue
            code, origin, meaning, expl = parts
            if origin not in ORIGIN_LANGUAGES:
                E(f"[{name}] kök ailesinde bilinmeyen köken '{origin}': {code}")
            if not meaning or not expl:
                E(f"[{name}] kök ailesinde boş alan: {code}")
            if code in seen:
                W(f"[{name}] yinelenen kök ailesi (ilk kayıt kazanır): {code}")
            seen.add(code)
            rm = root_rx.search(expl)
            if rm:
                root = rm.group(1).lower().rstrip("'")
                if code in stated_root and stated_root[code][0] != root:
                    E(f"[{name}] aynı kod ({code}) farklı kökler için kullanılıyor: "
                      f"{stated_root[code][0]} ({stated_root[code][1]}) ↔ {root} — üyeler karışır; ayrı kod verin")
                stated_root.setdefault(code, (root, name))
            stats[name] += 1
    for f in parse_families():
        if members.get(f.code, 0) == 0:
            E(f"kök ailesinin hiç üyesi yok (testler bunu reddeder): {f.code}")
    return stats


# Aile kodu harfi -> kaynak biçim çevriyazısında kabul edilen harfler. Zayıf harfler (A/W/Y) düşebilir.
_ROOT_LETTERS = {"A": "ʾʿa", "B": "b", "C": "cj", "D": "dḍḏ", "F": "f", "G": "gġ", "Ğ": "ġğ", "H": "hḥḫ", "Ḥ": "ḥ", "Ḫ": "ḫ",
                 "K": "kq", "Q": "q", "L": "l", "M": "m", "N": "n", "R": "r", "S": "sṣṯş", "Ṣ": "ṣ", "Ṯ": "ṯ", "Ş": "ş",
                 "T": "tṭ", "W": "wvū", "Y": "yīi", "Z": "zẕḏḍẓ", "Ẕ": "ẕ", "Ḍ": "ḍ", "İ": "ʿ"}
_WEAK = set("AWYİ")


def check_arabic_roots(lexicon):
    """Arapça kökenli üyenin kaynak biçimi, ailesinin kök harflerini sırayla içermeli (ḥ/ḫ/h, q/k, ṣ/s gibi
    ayrı harflerin aynı koda toplanmasıyla doğan karışmaları yakalar). Uyarı verir; hata değil."""
    import unicodedata

    def matches(letters, src, pos=0):
        if not letters:
            return True
        l, rest = letters[0], letters[1:]
        for i in range(pos, len(src)):
            if src[i] in _ROOT_LETTERS[l] and matches(rest, src, i + 1):
                return True
        return l in _WEAK and matches(rest, src, pos)  # zayıf harf düşmüş olabilir

    n = 0
    for e in lexicon:
        if e.origin != "ar" or not e.family or e.family[0] in "*-" or "-" not in e.family:
            continue
        letters = e.family.split("-")
        if any(l not in _ROOT_LETTERS for l in letters):
            continue
        src = unicodedata.normalize("NFC", e.source_form.lower())
        variants = {src, src.replace("th", "ṯ"), src.replace("dh", "ḏ")}
        if not any(matches(letters, v) for v in variants):
            W(f"kaynak biçim kök harflerine uymuyor: {e.lemma} <{e.source_form}> ailesi {e.family}")
            n += 1
    return n


def check_cognates(lexicon):
    lemmas = {e.lemma for e in lexicon}
    for e in lexicon:  # build_database türetilmiş (-lı, -lık…) biçimlere de ortak sözcük bağlayabilir
        for d in derivation.derive(e):
            lemmas.add(d.lemma)
    stats = Counter()
    for m in corpora_modules():
        name = m.__name__.split(".")[-1]
        if not hasattr(m, "COGNATES"):
            continue
        lemma, direction = None, ""
        for raw in m.COGNATES.splitlines():
            if not raw.strip():
                continue
            if raw.startswith("@"):
                try:
                    head, direction = raw[1:].rsplit(" ", 1)
                except ValueError:
                    E(f"[{name}] COGNATES başlığı hatalı: {raw}")
                    lemma = None
                    continue
                lemma = head.strip()
                if lemma not in lemmas:
                    E(f"[{name}] ortak sözcük başlığı sözlükte yok: {lemma}")
                if direction not in ("from_turkish", "into_turkish", "shared_ancestor"):
                    E(f"[{name}] bilinmeyen yön '{direction}': {lemma}")
                continue
            if raw[0] not in " \t":
                E(f"[{name}] COGNATES satırı girintili değil ya da '@' eksik: {raw[:60]}")
            line = raw.strip()
            code, _, rest = line.partition(" ")
            if code not in TARGET_LANGUAGES:
                E(f"[{name}] bilinmeyen hedef dil kodu '{code}' ({lemma})")
            segs = [s.strip() for s in rest.split(";")]
            if not segs[0]:
                E(f"[{name}] yabancı biçim boş ({lemma}, {code})")
            if len(segs) < 2 or not segs[1]:
                E(f"[{name}] anlam boş ({lemma}, {code}) — testler boş anlamı reddeder")
            stats[name] += 1
    return stats


def check_toponyms():
    tops = parse_toponyms()
    stats = Counter()
    names = set()
    for t in tops:
        name = t.module.split(".")[-1]
        stats[name] += 1
        if t.kind not in TOPONYM_KINDS:
            E(f"[{name}] bilinmeyen yer adı türü '{t.kind}': {t.name}")
        if t.region not in TURKISH_REGIONS:
            E(f"[{name}] bilinmeyen bölge '{t.region}': {t.name}")
        if t.origin not in TOPONYM_ORIGIN_LANGUAGES:
            E(f"[{name}] bilinmeyen yer adı köken dili '{t.origin}': {t.name}")
        if t.kind == "il" and (t.plate is None or not 1 <= t.plate <= 81):
            E(f"[{name}] il için plaka kodu 1–81 olmalı: {t.name}")
        if t.kind == "il" and t.province != t.name:
            E(f"[{name}] il kaydında il alanı adla aynı olmalı: {t.name}")
        for code, form in t.chain:
            if code not in TOPONYM_STAGE_NAMES:
                W(f"[{name}] yer adı zincirinde bilinmeyen aşama kodu '{code}': {t.name}")
        if t.chain[-1][0] != "tr":
            E(f"[{name}] yer adı zinciri 'tr:' ile bitmeli: {t.name}")
        if len(t.chain) < 2:
            E(f"[{name}] yer adı zinciri en az iki aşama olmalı: {t.name}")
        if t.lat is None or t.lon is None:
            E(f"[{name}] koordinat eksik: {t.name}")
        elif not (35.5 <= t.lat <= 42.5 and 25.5 <= t.lon <= 45.0):
            E(f"[{name}] koordinat Türkiye sınırları dışında: {t.name} ({t.lat},{t.lon})")
        if len(t.story) < 120:
            W(f"[{name}] yer adı hikâyesi kısa (<120 karakter): {t.name}")
        if t.name in names:
            W(f"[{name}] aynı adlı ikinci yer adı (farklı il): {t.name}")
        names.add(t.name)
    provinces = [t for t in tops if t.kind == "il"]
    plates = Counter(t.plate for t in provinces)
    for p, c in plates.items():
        if c > 1:
            E(f"plaka kodu birden çok ile verilmiş: {p}")
    return stats, len(provinces), len(tops)


def check_names(lexicon):
    """Kişi adları: biçim, köken dili, cins, kök ailesi ve ilgili sözcük bağları; parça dilleri bilinen kodlardan."""
    from etymodata.parsing import parse_names
    lemmas = {normalize(e.lemma) for e in lexicon}
    fam_codes = {f.code for f in parse_families()}
    names = parse_names()
    stats = Counter()
    for n in names:
        stats[n.module.split(".")[-1]] += 1
        if n.origin not in ORIGIN_LANGUAGES:
            E(f"kişi adında bilinmeyen köken dili '{n.origin}': {n.name}")
        for p in n.parts:
            if p.origin not in ORIGIN_LANGUAGES:
                E(f"kişi adı '{n.name}': parça dili bilinmiyor '{p.origin}' ({p.form})")
            if not p.form or not p.meaning or not p.meaning_en:
                E(f"kişi adı '{n.name}': parça eksik ({p.form})")
        if n.family and n.family not in fam_codes:
            E(f"kişi adı '{n.name}': kök ailesi yok: {n.family}")
        if n.related and normalize(n.related) not in lemmas:
            E(f"kişi adı '{n.name}': ilgili sözcük sözlükte yok: {n.related}")
        if not n.name[:1].isupper():
            E(f"kişi adı büyük harfle başlamalı: {n.name}")
        if bool(n.note) != bool(n.note_en):
            W(f"kişi adı '{n.name}': not yalnızca tek dilde")
    return stats, len(names)


def check_idioms(lexicon):
    lemmas = {e.lemma for e in lexicon}
    wikt = load_generated("wiktionary_tr") or {}
    for w in wikt.get("words", []):
        lemmas.add(w["lemma"])
    for e in lexicon:
        for d in derivation.derive(e):
            lemmas.add(d.lemma)
    idioms = parse_idioms()
    stats = Counter()
    for i in idioms:
        name = i.module.split(".")[-1]
        stats[name] += 1
        if i.kind not in IDIOM_KINDS:
            E(f"[{name}] bilinmeyen deyim türü '{i.kind}': {i.phrase}")
        if i.domain not in IDIOM_DOMAINS:
            E(f"[{name}] bilinmeyen alan '{i.domain}': {i.phrase}")
        if i.confidence not in IDIOM_CONFIDENCE:
            E(f"[{name}] bilinmeyen güven düzeyi '{i.confidence}': {i.phrase}")
        if i.era not in ATTESTATIONS:
            E(f"[{name}] bilinmeyen dönem kodu '{i.era}': {i.phrase}")
        if len(i.story) < 100:
            W(f"[{name}] deyim hikâyesi kısa (<100 karakter): {i.phrase}")
        missing = [w for w in i.words if w not in lemmas]
        if missing:
            E(f"[{name}] deyimdeki sözcük(ler) sözlükte yok {missing}: {i.phrase}")
        if not i.words:
            E(f"[{name}] deyimde anahtar sözcük yok: {i.phrase}")
    return stats, len(idioms)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--module", help="yalnızca bu korpus modülünün istatistiklerini göster")
    args = ap.parse_args()
    try:
        lexicon = parse_lexicon()
    except Exception as ex:  # noqa: BLE001
        print(f"E sözlük ayrıştırılamadı: {ex}")
        sys.exit(1)
    w_stats = check_words(args.module)
    f_stats = check_families(lexicon)
    check_arabic_roots(lexicon)
    c_stats = check_cognates(lexicon)
    try:
        t_stats, n_prov, n_top = check_toponyms()
    except Exception as ex:  # noqa: BLE001
        E(f"yer adları ayrıştırılamadı: {ex}")
        t_stats, n_prov, n_top = {}, 0, 0
    try:
        i_stats, n_idiom = check_idioms(lexicon)
    except Exception as ex:  # noqa: BLE001
        E(f"deyimler ayrıştırılamadı: {ex}")
        i_stats, n_idiom = {}, 0
    try:
        n_stats, n_names = check_names(lexicon)
    except Exception as ex:  # noqa: BLE001
        E(f"kişi adları ayrıştırılamadı: {ex}")
        n_stats, n_names = {}, 0

    print("Modül istatistikleri (WORDS / FAMILIES / COGNATES / TOPONYMS / IDIOMS):")
    mods = sorted(set(w_stats) | set(f_stats) | set(c_stats) | set(t_stats) | set(i_stats))
    for m in mods:
        if args.module and m != args.module:
            continue
        print(f"  {m:36s} {w_stats.get(m,0):5d} {f_stats.get(m,0):5d} {c_stats.get(m,0):5d} {t_stats.get(m,0):5d} {i_stats.get(m,0):5d}")
    # --- Faz 6: İngilizce çeviri kapsamı ---------------------------------------------------------
    try:
        from etymodata.english_loader import EnglishData
        EN = EnglishData()
        fam_codes = {f.code for f in parse_families()}
        miss_fam = sorted(fam_codes - set(EN.families))
        if miss_fam:
            E(f"İngilizce karşılığı olmayan kök ailesi: {len(miss_fam)} ({', '.join(miss_fam[:8])}…)")
        tops = parse_toponyms()
        miss_top = [t.name for t in tops if f"{t.name}|{t.province}" not in EN.toponyms]
        if miss_top:
            E(f"İngilizce hikâyesi olmayan yer adı: {len(miss_top)} ({', '.join(miss_top[:8])}…)")
        idi = parse_idioms()
        miss_idi = [i.phrase for i in idi if i.phrase not in EN.idioms]
        if miss_idi:
            E(f"İngilizce hikâyesi olmayan deyim: {len(miss_idi)} ({', '.join(miss_idi[:8])}…)")
        miss_src = {e.source_meaning for e in lexicon if e.source_meaning and not EN.translate_meaning(e.source_meaning)}
        if miss_src:
            W(f"İngilizce karşılığı olmayan kaynak anlam: {len(miss_src)} (örn. {', '.join(sorted(miss_src)[:6])})")
        print(f"İngilizce kapsam: {EN.stats}")
    except Exception as ex:  # noqa: BLE001
        E(f"İngilizce çeviri dosyaları yüklenemedi: {ex}")

    cog = parse_cognates()
    print(f"\nToplam: {len(lexicon)} elle yazılmış sözcük, {len(parse_families())} kök ailesi, {len(cog)} ortak sözcük satırı, "
          f"{n_top} yer adı ({n_prov} il), {n_idiom} deyim, {n_names} kişi adı")
    shown = warnings if not args.module else [w for w in warnings if f"[{args.module}]" in w]
    # içerik uyarıları önce; biçimsel/yinelenen madde uyarıları sonra
    _late = ("yinelenen madde", "çok sözcüklü madde", "yinelenen kök ailesi")
    shown = sorted(shown, key=lambda w: any(k in w for k in _late))
    for w in shown[:60]:
        print("W", w)
    if len(shown) > 60:
        print(f"... {len(shown) - 60} uyarı daha")
    shown_e = errors if not args.module else [e for e in errors if f"[{args.module}]" in e or not e.startswith("[")]
    for e in shown_e[:200]:
        print("E", e)
    if len(shown_e) > 200:
        print(f"... {len(shown_e) - 200} hata daha")
    print(f"\n{len(errors)} hata, {len(warnings)} uyarı")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
