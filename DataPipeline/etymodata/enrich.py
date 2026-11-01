# -*- coding: utf-8 -*-
"""Özgün alfabe, vezin ve IPA zenginleştirmesi (şema sürümü 2).

Öncelik sırası (sözcük başına):
  1. Elle denetlenmiş yazım (corpora/alfabeler.py SCRIPTS)            -> script_source = 'curated'
  2. Eski Türkçe dönemi Öz Türkçe sözcük: Göktürk damgaları              -> 'generated_old_turkic'
  3. Wiktionary (Kaikki.org) kaynak yazımı, köken diliyle uyumlu ise      -> 'wiktionary'
  4. Arapça/Farsça çevriyazıdan Arap harflerine algoritmik dönüşüm       -> 'generated_arabic'
  5. Slav Latin yazımından Kiril'e dönüşüm                                -> 'generated_cyrillic'
  6. Latin alfabeli köken dilleri: kaynak biçimin kendisi                 -> 'latin'
Türetilmiş (derived) satırlar yalnızca IPA alır; Arapça kökenli ve üçlü kök ailesine bağlı sözcüklerde vezin çıkarılır.
"""
from .scripts import (old_turkic, arabic_script, arabic_pattern, cyrillic_from_slavic_latin, turkish_ipa,
                      script_name_of, strip_arabic_diacritics, ORIGIN_SCRIPT_NAME, LATIN_ORIGINS)
from .templates import OLD_TURKIC_ERAS, OTTOMAN_ERAS, normalize

# Köken diline göre Wiktionary yazımının kabul edilebilir yazı sistemleri
_COMPATIBLE = {
    "ar": {"Arap"}, "fa": {"Arap"}, "ota": {"Arap"}, "tr": {"Arap", "Göktürk (Orhun)"},
    "el": {"Yunan"}, "hy": {"Ermeni"}, "sl": {"Kiril"}, "zh": {"Çin (Han)"}, "ja": {"Çin (Han)", "Japon"},
    "he": {"İbrani"}, "ka": {"Gürcü"}, "sog": {"Soğd"}, "sa": {"Devanagari"}, "mn": {"Moğol", "Kiril", "Çin (Han)"},
    "ku": {"Arap", "Latin"}, "it": {"Latin", "Yunan"}, "fr": {"Latin"}, "en": {"Latin"}, "la": {"Latin"},
    "de": {"Latin"}, "es": {"Latin"}, "pt": {"Latin"}, "nl": {"Latin"}, "hu": {"Latin"}, "ro": {"Latin"},
}


_PERSIAN_LETTERS = set("کیگچپژڭ")


def _script_name_for(origin: str, script: str, era: str = "") -> str:
    kind = script_name_of(script)
    if kind == "Arap":
        if origin == "tr" or origin == "ota":
            return "Osmanlı Türkçesi (Arap harfleri)"
        if origin == "fa":
            return "Fars (Arap harfleri)"
        if origin == "ar":
            # Wiktionary'nin Osmanlı yazımı (Fars harfleri) ile saf Arapça yazımı ayırt edilir
            return "Osmanlı Türkçesi (Arap harfleri)" if any(ch in _PERSIAN_LETTERS for ch in script) else "Arap"
        return "Osmanlı Türkçesi (Arap harfleri)"
    if kind == "Kiril" and origin == "mn":
        return "Moğol (Kiril)"
    return kind or ORIGIN_SCRIPT_NAME.get(origin, "")


class ScriptEnricher:
    def __init__(self, overrides: dict, override_names: dict, wikt_scripts: dict):
        """overrides: kaynak biçim -> yazım; override_names: kaynak biçim -> yazı adı; wikt_scripts: lemma -> (yazım, kaynak biçim)."""
        self.overrides = overrides
        self.override_names = override_names
        self.wikt = wikt_scripts
        self.stats = {"curated": 0, "generated_old_turkic": 0, "wiktionary": 0, "generated_arabic": 0,
                      "generated_cyrillic": 0, "latin": 0, "none": 0, "pattern": 0}

    # ------------------------------------------------------------------ elle yazılmış korpus satırı
    def enrich_curated(self, row: dict, entry, family_code: str | None):
        origin, src, era = entry.origin, entry.source_form, entry.era
        script = name = translit = source = ""
        # 1. elle denetlenmiş yazım
        if src in self.overrides:
            script = self.overrides[src]
            name = self.override_names.get(src) or _script_name_for(origin, script)
            source = "curated"
        elif src in self.override_names:
            script = src
            name = self.override_names[src]
            source = "curated"
        # 2. Göktürk
        if not script and origin == "tr" and era in OLD_TURKIC_ERAS:
            ot = old_turkic(src)
            if ot:
                script, name, source = ot, "Göktürk (Orhun)", "generated_old_turkic"
        # 3. Wiktionary kaynak yazımı (Öz Türkçe sözcükte yalnızca Osmanlı döneminde yazılmış ve
        #    sözcüğün kendisine ait bir yazım kabul edilir; kök sözcüğün yazımı devralınmaz)
        if not script:
            w = self.wikt.get(entry.lemma)
            if w:
                wscript, wsource = w
                kind = script_name_of(wscript)
                own = normalize(wsource or "") in ("", normalize(entry.lemma))
                tr_ok = origin != "tr" or (era in OTTOMAN_ERAS and own)
                if kind in _COMPATIBLE.get(origin, set()) and kind != "Latin" and tr_ok:
                    script = strip_arabic_diacritics(wscript) if kind == "Arap" else wscript
                    name = _script_name_for(origin, script)
                    source = "wiktionary"
        # 4. Arap harfleri (algoritmik)
        if not script and origin in ("ar", "fa"):
            ar = arabic_script(src, persian=(origin == "fa"))
            if ar:
                script, name, source = ar, ORIGIN_SCRIPT_NAME[origin], "generated_arabic"
        # 5. Kiril
        if not script and origin == "sl":
            cy = cyrillic_from_slavic_latin(src)
            if cy:
                script, name, source = cy, "Kiril", "generated_cyrillic"
        # 6. Latin
        if not script and origin in LATIN_ORIGINS and src:
            script, name, source = src, "Latin", "latin"
        if script and name != "Latin":
            translit = src.rstrip("-") if src else ""
        pattern = None
        if origin == "ar" and family_code and "-" in family_code and family_code.upper() == family_code:
            pattern = arabic_pattern(src, family_code)
        self._apply(row, script, name, translit, source, pattern, entry.lemma)

    # ------------------------------------------------------------------ türetilmiş satır
    def enrich_derived(self, row: dict):
        self._apply(row, "", "", "", "", None, row["lemma"])

    # ------------------------------------------------------------------ Wiktionary satırı
    def enrich_wiktionary(self, row: dict, w: dict):
        script = (w.get("source_script") or "").strip()
        name = source = translit = ""
        if script:
            kind = script_name_of(script)
            if kind == "Latin":
                script, name, source = script, "Latin", "wiktionary"
            else:
                if kind == "Arap":
                    script = strip_arabic_diacritics(script)
                name = _script_name_for(w["origin"], script)
                source = "wiktionary"
                translit = w.get("source_form") or ""
        self._apply(row, script, name, translit, source, None, row["lemma"])

    def _apply(self, row, script, name, translit, source, pattern, lemma):
        row["original_script"] = script
        row["original_script_name"] = name
        row["transliteration"] = translit
        row["ipa"] = turkish_ipa(lemma)
        row["arabic_pattern"] = pattern
        row["script_source"] = source
        self.stats[source or "none"] += 1
        if pattern:
            self.stats["pattern"] += 1
