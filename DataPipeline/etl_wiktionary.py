#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wiktionary (Kaikki.org) Türkçe dökümünden etimoloji ve soy ağacı (descendant) verisi çıkaran ETL.

Kullanım:
    python3 DataPipeline/etl_wiktionary.py [--cache DataPipeline/cache] [--out DataPipeline/corpora/generated/wiktionary_tr.json]
                                           [--limit N] [--no-download]

Kaynak: https://kaikki.org/dictionary/Turkish/kaikki.org-dictionary-Turkish.jsonl
        (wiktextract çıktısı; Wiktionary içeriği CC BY-SA 4.0 lisanslıdır.)

Çıktı yalnızca *yapısal* olgulardır: madde başı, tür, kaynak dil kodu, özgün biçim/okunuş, kısa anlam, geçiş
zinciri ve başka dillere geçen biçimler. Türkçe künye metinleri build_database.py tarafından özgün şablonlarla
üretilir; Wiktionary'nin düz metni kopyalanmaz.

Ağ erişimi yoksa script uyarı verip 0 koduyla çıkar; build_database.py yalnızca elle yazılmış korpuslarla çalışır.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from etymodata.languages import TARGET_LANGUAGES  # noqa: E402

DUMP_URL = "https://kaikki.org/dictionary/Turkish/kaikki.org-dictionary-Turkish.jsonl"
DUMP_NAME = "kaikki.org-dictionary-Turkish.jsonl"

# Wiktionary dil kodu -> EtimoTürk köken sınıfı
ORIGIN_MAP = {
    "ar": "ar", "arb": "ar", "ajp": "ar", "arz": "ar", "acm": "ar", "ary": "ar", "afb": "ar", "aeb": "ar", "apc": "ar", "ar-cls": "ar",
    "fa": "fa", "fa-cls": "fa", "pal": "fa", "peo": "fa", "fa-ira": "fa", "prs": "fa", "tg": "fa", "ira-pro": "fa", "xpr": "fa",
    "fr": "fr", "fro": "fr", "frm": "fr", "oc": "fr", "pro": "fr",
    "it": "it", "vec": "it", "lij": "it", "nap": "it", "scn": "it", "roa-oit": "it",
    "el": "el", "grc": "el", "gkm": "el", "grc-koi": "el", "pnt": "el", "cpg": "el",
    "en": "en", "enm": "en", "ang": "en",
    "hy": "hy", "xcl": "hy", "axm": "hy", "hyw": "hy",
    "mn": "mn", "xng": "mn", "cmg": "mn", "mkh": "mn", "xwo": "mn", "bua": "mn", "kha": "mn", "mn-pro": "mn", "xgn-pro": "mn",
    "ru": "sl", "bg": "sl", "sr": "sl", "sh": "sl", "hr": "sl", "bs": "sl", "mk": "sl", "uk": "sl", "pl": "sl", "cs": "sl", "sl": "sl",
    "cu": "sl", "orv": "sl", "sla-pro": "sl", "be": "sl", "sk": "sl",
    "sog": "sog", "xsc": "sog", "kho": "sog",
    "la": "la", "LL.": "la", "ML.": "la", "VL.": "la", "NL.": "la", "la-lat": "la", "la-vul": "la", "la-med": "la", "la-new": "la", "la-ecc": "la",
    "de": "de", "gmh": "de", "goh": "de", "nds": "de", "gsw": "de", "yi": "de", "got": "de", "gem-pro": "de",
    "es": "es", "osp": "es", "ca": "es", "pt": "pt", "gl": "pt",
    "zh": "zh", "ltc": "zh", "och": "zh", "cmn": "zh", "nan": "zh", "yue": "zh", "zhx": "zh",
    "sa": "sa", "hi": "sa", "ur": "sa", "pa": "sa", "inc-pro": "sa", "pra": "sa", "pi": "sa", "inc-ash": "sa", "bn": "sa", "ta": "sa", "ml": "sa",
    "he": "he", "arc": "he", "syc": "he", "hbo": "he", "sem-pro": "he", "akk": "he", "jpa": "he", "tmr": "he", "sem-wes-pro": "he", "phn": "he", "uga": "he",
    "ro": "ro", "rup": "ro", "hu": "hu", "ka": "ka", "nl": "nl", "dum": "nl", "af": "nl", "ja": "ja", "ku": "ku", "kmr": "ku", "ckb": "ku", "zza": "ku",
    "lzz": "ka", "xmf": "ka", "ab": "ka", "ady": "ka", "kbd": "ka", "ce": "ka", "av": "ka",
}
# Türkçe'nin kendi tarihsel evreleri: kalıtım → öz Türkçe
TURKIC_CODES = {"otk", "trk-pro", "trk-oat", "ota", "tr", "trk-ogz-pro", "oui", "xqa", "qwm", "kaa", "az", "kk", "uz", "ky", "tk", "tt", "ba", "cv", "sah", "ug", "trk", "trk-oat-pro", "trk-ogz", "trk-cmn", "trk-kip", "chg", "xbo", "trk-kar"}

POS_MAP = {"noun": "n", "verb": "v", "adj": "adj", "adv": "adv", "pron": "pron", "conj": "conj", "num": "num",
           "intj": "intj", "postp": "postp", "particle": "adv", "det": "adj"}

STAGE_CODE_MAP = {  # zincir aşaması kodları (STAGE_NAMES ile uyumlu)
    "ota": "ota", "otk": "otk", "trk-pro": "ptk", "trk-oat": "eat", "pal": "pal", "grc": "grc", "gkm": "el", "fro": "fro", "frm": "fr",
    "vec": "ven", "LL.": "la", "ML.": "la", "VL.": "la", "xcl": "hy", "hi": "hi", "ur": "hi", "arc": "arc", "akk": "akk", "sum": "sum",
    "nah": "nah", "tup": "tup", "cs": "cs", "ger": "ger", "gem-pro": "ger", "oc": "oc", "ca": "ca", "ml": "ml", "ta": "ta", "cop": "cop",
    "egy": "egy", "ber": "ber", "pl": "pl", "hr": "hr", "bg": "bg", "sr": "sr", "ru": "ru", "ine-pro": "pie",
}

# Soy ağacı (descendants) için Wiktionary kodu -> karşılaştırma dili kodu
DESC_LANG_MAP = {
    "az": "az", "kk": "kk", "uz": "uz", "tk": "tk", "ky": "ky", "el": "el", "bg": "bg", "sr": "sr", "sh": "sr", "hr": "sr", "bs": "sr",
    "sq": "sq", "ro": "ro", "mk": "mk", "it": "it", "fa": "fa", "ar": "ar", "arz": "ar", "ajp": "ar", "acm": "ar", "ary": "ar", "apc": "ar",
    "hy": "hy", "hyw": "hy", "ka": "ka", "ur": "ur", "hi": "ur", "hu": "hu", "ru": "ru", "uk": "uk", "fr": "fr", "en": "en", "de": "de",
    "pl": "pl", "es": "es", "pt": "pt", "mn": "mn",
}

TURKISH_LEMMA_RE = re.compile(r"^[a-zçğıöşüâîû]{2,32}$")
FROM_RE = re.compile(r"\b(?:From|from|Borrowed from|Inherited from|Ultimately from)\s+([A-Z][A-Za-z\- ]{2,30}?)\s+[\*\w؀-ۿͰ-ϿЀ-ӿ԰-֏Ⴀ-ჿ]")
TEXT_LANG_MAP = {
    "Arabic": "ar", "Persian": "fa", "Classical Persian": "fa", "Middle Persian": "fa", "French": "fr", "Italian": "it", "Venetian": "it",
    "Greek": "el", "Ancient Greek": "el", "Byzantine Greek": "el", "English": "en", "Armenian": "hy", "Old Armenian": "hy",
    "Mongolian": "mn", "Middle Mongolian": "mn", "Russian": "sl", "Bulgarian": "sl", "Serbo-Croatian": "sl", "Sogdian": "sog",
    "Latin": "la", "German": "de", "Spanish": "es", "Portuguese": "pt", "Chinese": "zh", "Sanskrit": "sa", "Hindi": "sa", "Urdu": "sa",
    "Hebrew": "he", "Aramaic": "he", "Romanian": "ro", "Hungarian": "hu", "Georgian": "ka", "Dutch": "nl", "Japanese": "ja", "Kurdish": "ku",
    "Northern Kurdish": "ku", "Old Turkic": "tr", "Proto-Turkic": "tr", "Old Anatolian Turkish": "tr", "Ottoman Turkish": "ota",
}

BORROW_TEMPLATES = {"bor", "bor+", "der", "inh", "inh+", "uder", "lbor", "slbor", "obor", "der+", "ubor", "learned borrowing", "borrowed", "derived", "inherited"}
INTERNAL_TEMPLATES = {"surf", "af", "affix", "suffix", "suf", "compound", "com", "prefix", "univerbation", "blend", "clipping", "back-formation", "backformation"}

# "Etymology tree" satırlarındaki dil adları -> (zincir aşama kodu, köken sınıfı)
TREE_LANG_MAP = {
    "Turkish": ("tr", "tr"), "Ottoman Turkish": ("ota", "ota"), "Old Anatolian Turkish": ("eat", "tr"), "Old Turkic": ("otk", "tr"),
    "Proto-Turkic": ("ptk", "tr"), "Proto-Oghuz": ("ptk", "tr"), "Old Uyghur": ("otk", "tr"), "Karakhanid": ("otk", "tr"), "Chagatai": ("otk", "tr"),
    "Kipchak": ("otk", "tr"), "Azerbaijani": ("otk", "tr"), "Proto-Common Turkic": ("ptk", "tr"), "Proto-Kipchak": ("otk", "tr"),
    "Arabic": ("ar", "ar"), "Classical Arabic": ("ar", "ar"), "Egyptian Arabic": ("ar-eg", "ar"), "Moroccan Arabic": ("ar-mag", "ar"), "Hijazi Arabic": ("ar", "ar"),
    "Levantine Arabic": ("ar", "ar"), "Iraqi Arabic": ("ar", "ar"), "Gulf Arabic": ("ar", "ar"), "Maghrebi Arabic": ("ar-mag", "ar"), "Proto-Semitic": ("he", "he"),
    "Persian": ("fa", "fa"), "Classical Persian": ("fa", "fa"), "Middle Persian": ("pal", "fa"), "Old Persian": ("pal", "fa"), "Parthian": ("pal", "fa"),
    "Iranian Persian": ("fa", "fa"), "Dari": ("fa", "fa"), "Proto-Iranian": ("pal", "fa"), "Proto-Indo-Iranian": ("pie", "fa"), "Bactrian": ("pal", "fa"),
    "French": ("fr", "fr"), "Old French": ("fro", "fr"), "Middle French": ("fr", "fr"), "Occitan": ("oc", "fr"), "Old Occitan": ("oc", "fr"),
    "Italian": ("it", "it"), "Venetian": ("ven", "it"), "Ligurian": ("it", "it"), "Neapolitan": ("it", "it"), "Sicilian": ("it", "it"), "Genoese": ("ven", "it"),
    "Greek": ("el", "el"), "Ancient Greek": ("grc", "el"), "Byzantine Greek": ("el", "el"), "Medieval Greek": ("el", "el"), "Koine Greek": ("grc", "el"),
    "Proto-Hellenic": ("grc", "el"), "Pontic Greek": ("el", "el"), "Cappadocian Greek": ("el", "el"), "Mycenaean Greek": ("grc", "el"),
    "English": ("en", "en"), "Middle English": ("en", "en"), "Old English": ("en", "en"), "American English": ("en", "en"),
    "Armenian": ("hy", "hy"), "Old Armenian": ("hy", "hy"), "Middle Armenian": ("hy", "hy"), "Western Armenian": ("hy", "hy"),
    "Mongolian": ("mn", "mn"), "Middle Mongol": ("mn", "mn"), "Middle Mongolian": ("mn", "mn"), "Proto-Mongolic": ("mn", "mn"), "Classical Mongolian": ("mn", "mn"),
    "Russian": ("ru", "sl"), "Bulgarian": ("bg", "sl"), "Serbo-Croatian": ("sr", "sl"), "Macedonian": ("sl", "sl"), "Ukrainian": ("ru", "sl"),
    "Polish": ("pl", "sl"), "Czech": ("cs", "sl"), "Old Church Slavonic": ("sl", "sl"), "Proto-Slavic": ("sl", "sl"), "Old East Slavic": ("ru", "sl"), "Slovene": ("sl", "sl"),
    "Sogdian": ("sog", "sog"), "Khotanese": ("sog", "sog"), "Saka": ("sog", "sog"),
    "Latin": ("la", "la"), "Late Latin": ("la", "la"), "Medieval Latin": ("la", "la"), "Vulgar Latin": ("la", "la"), "New Latin": ("la", "la"), "Proto-Italic": ("la", "la"),
    "German": ("de", "de"), "Middle High German": ("de", "de"), "Old High German": ("de", "de"), "Low German": ("de", "de"), "Yiddish": ("de", "de"),
    "Proto-Germanic": ("ger", "de"), "Gothic": ("ger", "de"), "Proto-West Germanic": ("ger", "de"), "Middle Low German": ("de", "de"),
    "Spanish": ("es", "es"), "Old Spanish": ("es", "es"), "Catalan": ("ca", "es"), "Portuguese": ("pt", "pt"), "Galician": ("pt", "pt"),
    "Chinese": ("zh", "zh"), "Middle Chinese": ("zh", "zh"), "Old Chinese": ("zh", "zh"), "Mandarin": ("zh", "zh"), "Cantonese": ("zh", "zh"), "Hokkien": ("zh", "zh"), "Min Nan": ("zh", "zh"),
    "Sanskrit": ("sa", "sa"), "Hindi": ("hi", "sa"), "Urdu": ("hi", "sa"), "Hindustani": ("hi", "sa"), "Proto-Indo-Aryan": ("sa", "sa"), "Prakrit": ("sa", "sa"), "Pali": ("sa", "sa"),
    "Gandhari": ("sa", "sa"), "Bengali": ("sa", "sa"), "Tamil": ("ta", "sa"), "Malayalam": ("ta", "sa"), "Marathi": ("sa", "sa"), "Punjabi": ("hi", "sa"), "Sinhalese": ("sa", "sa"),
    "Hebrew": ("he", "he"), "Biblical Hebrew": ("he", "he"), "Aramaic": ("arc", "he"), "Classical Syriac": ("arc", "he"), "Jewish Babylonian Aramaic": ("arc", "he"),
    "Akkadian": ("akk", "he"), "Sumerian": ("sum", "he"), "Phoenician": ("he", "he"), "Ugaritic": ("he", "he"), "Imperial Aramaic": ("arc", "he"),
    "Romanian": ("ro", "ro"), "Aromanian": ("ro", "ro"), "Hungarian": ("hu", "hu"), "Georgian": ("ka", "ka"), "Old Georgian": ("ka", "ka"), "Laz": ("ka", "ka"), "Mingrelian": ("ka", "ka"),
    "Dutch": ("nl", "nl"), "Middle Dutch": ("nl", "nl"), "Afrikaans": ("nl", "nl"), "Japanese": ("ja", "ja"), "Kurdish": ("ku", "ku"), "Northern Kurdish": ("ku", "ku"), "Central Kurdish": ("ku", "ku"), "Zazaki": ("ku", "ku"),
    "Albanian": ("sq", "sl"), "Coptic": ("cop", "he"), "Egyptian": ("egy", "he"), "Nahuatl": ("nah", "es"), "Classical Nahuatl": ("nah", "es"), "Taíno": ("tai", "es"), "Tupi": ("tup", "pt"), "Old Tupi": ("tup", "pt"),
    "Malay": ("ml", "nl"), "Tagalog": ("ml", "es"), "Quechua": ("es", "es"), "Guaraní": ("es", "es"), "Proto-Indo-European": ("pie", None), "Proto-Uralic": ("hu", "hu"), "Proto-Finno-Ugric": ("hu", "hu"),
}
TREE_LINE_RE = re.compile(r"^(?P<lang>[A-Z][A-Za-z\u00C0-\u024F\-' ]+?) (?P<term>\S+)(?: \((?P<roman>[^)]*)\))?(?P<kw>bor\.|inh\.|der\.|calq\.|calque\.|ubor\.|lbor\.|slbor\.|obor\.|cog\.|clq\.)?$")
TREE_LINE_NOTERM_RE = re.compile(r"^(?P<lang>[A-Z][A-Za-z\u00C0-\u024F\-' ]+?)(?P<kw>bor\.|inh\.|der\.|calq\.|ubor\.)?$")


def download(cache_dir: str, no_download: bool) -> str | None:
    path = os.path.join(cache_dir, DUMP_NAME)
    if os.path.exists(path) and os.path.getsize(path) > 1_000_000:
        return path
    if no_download:
        return None
    os.makedirs(cache_dir, exist_ok=True)
    print(f"İndiriliyor: {DUMP_URL}", file=sys.stderr)
    try:
        with urllib.request.urlopen(DUMP_URL, timeout=60) as resp, open(path + ".part", "wb") as fh:
            total = 0
            while True:
                chunk = resp.read(1 << 20)
                if not chunk:
                    break
                fh.write(chunk)
                total += len(chunk)
                if total % (50 << 20) < (1 << 20):
                    print(f"  {total / (1 << 20):.0f} MB", file=sys.stderr)
        os.replace(path + ".part", path)
        return path
    except Exception as exc:  # ağ kısıtı: sessizce vazgeç
        print(f"UYARI: Wiktionary dökümü indirilemedi ({exc}); ETL atlanıyor.", file=sys.stderr)
        return None


def template_args(t: dict) -> dict:
    return t.get("args") or {}


def parse_tree(text: str, lemma: str):
    """'Etymology tree' bloğunu [(dil adı, biçim, okunuş, anahtar)] listesine çevirir (kökten Türkçeye)."""
    if not text.startswith("Etymology tree"):
        return None
    rows = []
    for line in text.split("\n")[1:]:
        line = line.strip()
        if not line:
            continue
        m = TREE_LINE_RE.match(line)
        if m:
            term = re.sub(r"(bor|inh|der|calq|calque|ubor|lbor|slbor|obor|cog|clq)\.$", "", m.group("term"))
            rows.append((m.group("lang"), term, (m.group("roman") or "").strip(), (m.group("kw") or "").rstrip(".")))
            if m.group("lang") == "Turkish":
                break
            continue
        m2 = TREE_LINE_NOTERM_RE.match(line)
        if m2 and m2.group("lang") in TREE_LANG_MAP:
            rows.append((m2.group("lang"), "", "", (m2.group("kw") or "").rstrip(".")))
            continue
        break  # açıklama cümlesi başladı
    if not rows or rows[-1][0] != "Turkish":
        return None
    return rows


def origin_from_tree(rows, lemma: str):
    """Ağaçtan (köken, kaynak biçim, okunuş, zincir) üretir. Türkçe'ye en yakın yabancı aşama kökendir."""
    chain = []
    origin = None
    src_form, roman = "", ""
    for lang, term, rom, kw in rows:
        info = TREE_LANG_MAP.get(lang)
        if info is None:
            continue
        stage, cls = info
        chain.append((stage, rom or term or lemma))
    # Türkçe'den geriye yürü: ota/eat/otk aşamalarını atla, ilk yabancı sınıfı al
    turkic_only = True
    for lang, term, rom, kw in reversed(rows):
        info = TREE_LANG_MAP.get(lang)
        if info is None:
            continue
        stage, cls = info
        if cls in ("tr", "ota") or lang == "Turkish":
            continue
        if cls is None:
            continue
        origin = cls
        src_form, roman = (term or lemma), rom
        turkic_only = False
        break
    if turkic_only:
        origin = "tr"
        # kaynak biçim: en eski Türkçe aşama
        for lang, term, rom, kw in rows:
            if TREE_LANG_MAP.get(lang, (None, None))[1] == "tr" and (rom or term):
                src_form, roman = (term or lemma), rom
                break
        if not src_form:
            src_form = lemma
    return origin, src_form, roman, chain


def resolve_origin(entry: dict):
    """(origin_code, source_form, romanization, gloss, chain[(code, form)], method) ya da None."""
    text = entry.get("etymology_text") or ""
    tree = parse_tree(text, entry["word"])
    if tree:
        origin, src_form, roman, chain = origin_from_tree(tree, entry["word"])
        if origin:
            gloss = ""
            for t in entry.get("etymology_templates") or []:
                a = template_args(t)
                if a.get("t"):
                    gloss = a["t"]
                    break
            if not gloss:
                m = re.search(r"\u201c([^\u201d]{1,80})\u201d", text)
                gloss = m.group(1) if m else ""
            return origin, src_form, roman, gloss, chain, "tree"
    templates = entry.get("etymology_templates") or []
    # "ety" şablonu: {"2": ":bor", "3": "en:pound"}
    for t in templates:
        if t.get("name") == "ety":
            a = template_args(t)
            ref = a.get("3") or ""
            if ":" in ref:
                lang, _, term = ref.partition(":")
                if lang in TURKIC_CODES and lang != "ota":
                    return "tr", term or entry["word"], "", "", [(STAGE_CODE_MAP.get(lang, "otk"), term or entry["word"])], "ety"
                if lang != "ota" and ORIGIN_MAP.get(lang):
                    return ORIGIN_MAP[lang], term, "", "", [(STAGE_CODE_MAP.get(lang, ORIGIN_MAP[lang]), term)], "ety"
    chain = []
    current_lang = "tr"
    origin = None
    src_form = ""
    roman = ""
    gloss = ""
    hops = 0
    while hops < 6:
        hops += 1
        step = None
        for t in templates:
            name = t.get("name", "")
            a = template_args(t)
            if name in BORROW_TEMPLATES and a.get("1") == current_lang and a.get("2"):
                step = (name, a)
                break
        if step is None:
            break
        name, a = step
        src_lang = a["2"]
        form = (a.get("3") or "").strip()
        tr_ = (a.get("tr") or "").strip()
        g = (a.get("t") or a.get("4") or a.get("gloss") or "").strip()
        if src_lang in TURKIC_CODES and src_lang != "ota":
            # Öz Türkçe kalıtım
            chain.append((STAGE_CODE_MAP.get(src_lang, "otk"), tr_ or form or entry["word"]))
            if not src_form:
                src_form, roman, gloss = (form or entry["word"]), tr_, g
            origin = "tr"
            current_lang = src_lang
            # Proto-Turkic'ten öteye gitme
            if src_lang in ("trk-pro", "otk"):
                break
            continue
        if src_lang == "ota":
            chain.append(("ota", tr_ or form or entry["word"]))
            if not src_form:
                src_form, roman, gloss = (form or entry["word"]), tr_, g
            current_lang = "ota"
            origin = origin or None
            continue
        mapped = ORIGIN_MAP.get(src_lang)
        if mapped is None:
            break
        chain.append((STAGE_CODE_MAP.get(src_lang, mapped), tr_ or form))
        if origin is None or origin == "tr" and current_lang == "ota":
            origin = mapped
            src_form, roman, gloss = form, tr_, g
        current_lang = src_lang
        if name in ("inh", "inh+") and mapped != "tr":
            # Başka bir dilin kendi iç kalıtımı; bir adım daha derine izin ver
            continue
        # Doğrudan alıntı bulundu; daha derin tarihçe için bir adım daha dene (ör. fr < la)
        continue

    if origin is None and chain and chain[0][0] == "ota":
        origin = "ota"  # Osmanlı Türkçesi türetmesi (ar kökenli kalıp)
    method = "template"
    if origin is None:
        text = entry.get("etymology_text") or ""
        m = FROM_RE.search(text)
        if m:
            lang_name = m.group(1).strip()
            mapped = TEXT_LANG_MAP.get(lang_name)
            if mapped == "ota":
                m2 = re.search(r"from\s+(Arabic|Persian|Greek|French|Italian|Latin)\s", text)
                mapped = TEXT_LANG_MAP.get(m2.group(1)) if m2 else "ota"
            if mapped:
                origin = mapped
                method = "text"
    if origin is None:
        return None
    if origin == "tr" and not chain:
        chain = [("otk", entry["word"])]
    return origin, src_form, roman, gloss, chain, method


def internal_base(entry: dict):
    """surf/af/suffix şablonlarından Türkçe iç türetmenin kök sözcüğünü döndürür (ör. bakan → bakmak)."""
    for t in entry.get("etymology_templates") or []:
        if t.get("name") in INTERNAL_TEMPLATES:
            a = template_args(t)
            base = a.get("2") or ""
            base = re.sub(r"<[^>]*>", "", base).strip()
            base = base.replace("-", "").strip()
            if base and TURKISH_LEMMA_RE.match(base.lower()):
                return base
    return None


def is_coinage(entry: dict) -> bool:
    return any(t.get("name") in ("coin", "coinage") for t in entry.get("etymology_templates") or [])


def first_gloss(entry: dict) -> str:
    for s in entry.get("senses") or []:
        for g in s.get("glosses") or []:
            g = g.strip()
            if g:
                return g[:80]
    return ""


def is_inflected_form(entry: dict) -> bool:
    senses = entry.get("senses") or []
    if not senses:
        return True
    for s in senses:
        if not (s.get("form_of") or s.get("alt_of")):
            tags = set(s.get("tags") or [])
            if not tags & {"form-of", "alt-of", "misspelling", "obsolete", "archaic"}:
                return False
    return True


def descendants(entry: dict):
    """wiktextract 'descendants' listesi: {lang, lang_code, word, raw_tags} → karşılaştırma dili satırları."""
    rows = []
    for d in entry.get("descendants") or []:
        code = d.get("lang_code")
        form = (d.get("word") or "").strip()
        if not code or not form or code not in DESC_LANG_MAP:
            continue
        tags = set(d.get("raw_tags") or []) | set(d.get("tags") or [])
        roman = (d.get("roman") or "").strip()
        rows.append({"lang": DESC_LANG_MAP[code], "foreign": form, "romanization": roman, "meaning": "",
                     "borrowed": "borrowed" in tags or "borrowed" in (d.get("text") or "")})
    return rows


# Osmanlı yazımındaki harflerden köken çıkarsamak dilbilimsel olarak geçersizdir: Osmanlıca, öz Türkçe sözcükleri de
# Fars harfleriyle (چوجق çocuk, چپلاق çıplak) ve "Arap'a özgü" harflerle (صیقی sıkı, قات kat) yazar. Eski
# `classify_ottoman` sezgisi bu yüzden kaldırılmıştır (denetim: 502 kayıtta ~%70 yanlış atama). Osmanlı Türkçesi
# aşamasında kalan sözcükler `ota` ("kaynak dil belirsiz") olarak bırakılır; yalnızca eylemler Türkçe sayılır, çünkü
# Arapça/Farsça eylem kökleri Türkçeye ancak etmek/olmak bileşikleriyle girer.


def classify_ottoman(script_form: str) -> str:
    """Her zaman "ota" döndürür; harf tabanlı Arapça/Farsça sezgisi kasıtlı olarak kaldırılmıştır."""
    return "ota"


def run(dump_path: str, out_path: str, limit: int | None):
    t0 = time.time()
    words = {}
    cognates = defaultdict(list)
    stats = Counter()
    pending = []  # iç türetmeler (kök sözcüğün kökenine bağlı)
    with open(dump_path, "r", encoding="utf-8") as fh:
        for i, line in enumerate(fh):
            if limit and i >= limit:
                break
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                stats["json_error"] += 1
                continue
            if e.get("lang_code") != "tr":
                stats["other_lang"] += 1
                continue
            word = e.get("word", "")
            pos = POS_MAP.get(e.get("pos", ""))
            lemma_norm = word.lower().replace("I", "ı").replace("İ", "i")
            if not pos:
                stats["pos_skipped"] += 1
                continue
            if not TURKISH_LEMMA_RE.match(lemma_norm):
                stats["lemma_rejected"] += 1
                continue
            if is_inflected_form(e):
                stats["inflected_form"] += 1
                continue
            desc = descendants(e)
            resolved = resolve_origin(e)
            if resolved is None:
                base = internal_base(e)
                if base:
                    pending.append((word, pos, base, e, desc))
                    continue
                if is_coinage(e):
                    resolved = ("tr", word, "", first_gloss(e), [("tr", word)], "coin")
                else:
                    stats["no_etymology"] += 1
                    if desc:
                        cognates[(word, pos)].extend(desc)
                    continue
            origin, src_form, roman, gloss, chain, method = resolved
            if origin == "ota" and pos == "v":
                # Arapça/Farsça eylemler Türkçeye yalnızca etmek/olmak bileşikleriyle girer; yalın eylem öz Türkçedir
                origin, method = "tr", method + "+verb-rule"
                stats["ota_verb_reclassified"] += 1
            key = (word, pos)
            if key in words:
                stats["duplicate"] += 1
                # çakışma: daha uzun zinciri tut
                if len(chain) <= len(words[key]["chain"]):
                    continue
            words[key] = {
                "lemma": word, "pos": pos, "origin": origin,
                "source_form": (roman or src_form or word)[:60],
                "source_script": src_form[:60] if roman else "",
                "gloss_en": (gloss or first_gloss(e))[:80],
                "chain": [[c, f] for c, f in chain if f],
                "method": method,
            }
            stats["accepted"] += 1
            stats[f"origin_{origin}"] += 1
            if desc:
                cognates[key].extend(desc)
    # 2. geçiş: iç türetmeler kök sözcüğün kökenini alır (en çok 3 zincirleme)
    for _ in range(3):
        still = []
        for word, pos, base, e, desc in pending:
            found = None
            for cand in (base, base + "mek", base + "mak"):
                for p in ("v", "n", "adj", "adv"):
                    if (cand, p) in words:
                        found = words[(cand, p)]
                        break
                if found:
                    break
            if found is None:
                still.append((word, pos, base, e, desc))
                continue
            words[(word, pos)] = {
                "lemma": word, "pos": pos, "origin": found["origin"],
                "source_form": found["source_form"], "source_script": found.get("source_script", ""),
                "gloss_en": first_gloss(e)[:80],
                "chain": list(found["chain"]) + [["tr", f"{found['lemma']} → {word}"]],
                "method": "internal:" + found["lemma"],
            }
            stats["accepted"] += 1
            stats["internal_derivation"] += 1
            stats[f"origin_{found['origin']}"] += 1
            if desc:
                cognates[(word, pos)].extend(desc)
        pending = still
    stats["internal_unresolved"] = len(pending)
    cog_rows = []
    for (lemma, pos), rows in cognates.items():
        seen = set()
        for r in rows:
            k = (r["lang"], r["foreign"])
            if k in seen:
                continue
            seen.add(k)
            cog_rows.append({"lemma": lemma, "pos": pos, **r})
    out = {
        "meta": {
            "source": DUMP_URL,
            "license": "Wiktionary içeriği CC BY-SA 4.0 — yalnızca yapısal olgular çıkarılmıştır",
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "stats": dict(stats),
            "word_count": len(words),
            "cognate_count": len(cog_rows),
            "elapsed_s": round(time.time() - t0, 1),
        },
        "words": sorted(words.values(), key=lambda w: (w["lemma"], w["pos"])),
        "cognates": sorted(cog_rows, key=lambda c: (c["lemma"], c["lang"], c["foreign"])),
    }
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))
    return out["meta"]


def main():
    ap = argparse.ArgumentParser(description="Kaikki.org Türkçe Wiktionary ETL")
    ap.add_argument("--cache", default=os.path.join(HERE, "cache"))
    ap.add_argument("--out", default=os.path.join(HERE, "corpora", "generated", "wiktionary_tr.json"))
    ap.add_argument("--limit", type=int, default=None, help="yalnızca ilk N satır (deneme)")
    ap.add_argument("--no-download", action="store_true")
    args = ap.parse_args()
    dump = download(args.cache, args.no_download)
    if dump is None:
        print("Wiktionary dökümü yok; mevcut korpuslarla devam edilecek.", file=sys.stderr)
        return 0
    meta = run(dump, args.out, args.limit)
    for k, v in meta.items():
        print(f"{k:>14}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
