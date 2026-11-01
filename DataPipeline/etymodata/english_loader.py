# -*- coding: utf-8 -*-
"""`DataPipeline/english/*.tsv` çeviri dosyalarını ve Kaikki gloss sözlüğünü yükler.

Dosya adı öneki → tür:
  source_meanings_*.tsv   turkish_gloss \\t english_gloss
  cognate_meanings_*.tsv  turkish_gloss \\t english_gloss
  false_friends_*.tsv     turkish_note  \\t english_note
  families_*.tsv          code \\t core_meaning_en \\t explanation_en
  toponyms_*.tsv          name|province \\t meaning_en \\t story_en
  idioms_*.tsv            phrase \\t meaning_en \\t literal_en \\t story_en
Hatalı satırlar (eksik sütun) atlanır ve uyarı verilir; kısmi dosyalar kabul edilir (şablon motoru eksikleri doldurur).
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGLISH_DIR = os.path.join(HERE, "english")
GLOSSES_PATH = os.path.join(HERE, "corpora", "generated", "glosses_en.json")


def _read_tsv(prefix: str, columns: int):
    out = {}
    bad = 0
    for path in sorted(glob.glob(os.path.join(ENGLISH_DIR, prefix + "*.tsv"))):
        with open(path, encoding="utf-8") as fh:
            for raw in fh:
                line = raw.rstrip("\n")
                if not line.strip() or line.startswith("#"):
                    continue
                parts = line.split("\t")
                if len(parts) < columns or not parts[0].strip() or not parts[1].strip():
                    bad += 1
                    continue
                key = parts[0].strip()
                values = tuple(p.strip() for p in parts[1:columns])
                out.setdefault(key, values[0] if columns == 2 else values)
    if bad:
        print(f"uyarı: {prefix}*.tsv içinde {bad} eksik/hatalı satır atlandı", file=sys.stderr)
    return out


class EnglishData:
    def __init__(self):
        self.source_meanings = _read_tsv("source_meanings_", 2)
        self.cognate_meanings = _read_tsv("cognate_meanings_", 2)
        self.false_friends = _read_tsv("false_friends_", 2)
        self.families = _read_tsv("families_", 3)          # code -> (core_en, explanation_en)
        self.toponyms = _read_tsv("toponyms_", 3)          # name|province -> (meaning_en, story_en)
        self.idioms = _read_tsv("idioms_", 4)              # phrase -> (meaning_en, literal_en, story_en)
        self.glosses = {}
        if os.path.exists(GLOSSES_PATH):
            with open(GLOSSES_PATH, encoding="utf-8") as fh:
                self.glosses = json.load(fh).get("glosses", {})
        self.stats = {
            "source_meanings": len(self.source_meanings), "cognate_meanings": len(self.cognate_meanings),
            "false_friends": len(self.false_friends), "families": len(self.families), "toponyms": len(self.toponyms),
            "idioms": len(self.idioms), "glosses": len(self.glosses),
        }

    def gloss(self, lemma: str) -> str:
        """Kaikki İngilizce glossu (ilk anlam)."""
        return self.glosses.get(lemma, "")

    def translate_meaning(self, turkish: str) -> str:
        """Türkçe kaynak anlamı / ortak sözcük anlamını İngilizceye çevirir; sözlükte yoksa boş döner."""
        if not turkish:
            return ""
        if turkish in self.source_meanings:
            return self.source_meanings[turkish]
        if turkish in self.cognate_meanings:
            return self.cognate_meanings[turkish]
        if " " not in turkish and turkish in self.glosses:
            return self.glosses[turkish]
        # "a; b" biçimindeki alternatifler parça parça
        if ";" in turkish or "," in turkish:
            sep = ";" if ";" in turkish else ","
            parts = [self.translate_meaning(p.strip()) for p in turkish.split(sep)]
            if all(parts):
                return "; ".join(parts)
        return ""
