#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kaikki.org (Wiktionary) Türkçe dökümünden madde başı → İngilizce gloss sözlüğü çıkarır.

Kullanım:  python3 DataPipeline/etl_glosses.py [--dump DataPipeline/cache/kaikki.org-dictionary-Turkish.jsonl]
Çıktı:     DataPipeline/corpora/generated/glosses_en.json  { "lemma": "gloss", ... }

Yalnızca yapısal olgu (madde başının kısa İngilizce anlamı) alınır; çekimli biçimler ve yazım değişkeleri atlanır.
Lisans: Wiktionary katkıcıları, CC BY-SA 4.0 (meta.wiktionary_attribution ile atfedilir).
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DUMP = os.path.join(HERE, "cache", "kaikki.org-dictionary-Turkish.jsonl")
OUT = os.path.join(HERE, "corpora", "generated", "glosses_en.json")

_PAREN = re.compile(r"\s*\([^)]*\)")
_SKIP_TAGS = {"form-of", "alt-of", "misspelling", "obsolete", "archaic", "rare", "dated"}
_POS_ORDER = {"noun": 0, "verb": 1, "adj": 2, "adv": 3, "name": 4, "num": 5, "pron": 6, "intj": 7, "conj": 8, "postp": 9}


def clean_gloss(g: str) -> str:
    g = _PAREN.sub("", g).strip()
    g = re.sub(r"\s+", " ", g)
    g = g.rstrip(".;:, ")
    if len(g) > 90:
        cut = g[:90]
        g = cut[: cut.rfind(" ")] if " " in cut else cut
    return g


def best_gloss(entry: dict):
    for s in entry.get("senses") or []:
        tags = set(s.get("tags") or [])
        if s.get("form_of") or s.get("alt_of") or tags & _SKIP_TAGS:
            continue
        for g in s.get("glosses") or []:
            c = clean_gloss(g)
            if c and not c.lower().startswith(("alternative form", "alternative spelling", "obsolete form", "misspelling")):
                return c
    return ""


def run(dump: str, out: str):
    glosses, rank = {}, {}
    n = 0
    with open(dump, encoding="utf-8") as fh:
        for line in fh:
            n += 1
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            if e.get("lang_code") != "tr":
                continue
            lemma = (e.get("word") or "").strip()
            if not lemma or " " in lemma and len(lemma.split()) > 3:
                continue
            g = best_gloss(e)
            if not g:
                continue
            r = _POS_ORDER.get(e.get("pos"), 20)
            if lemma not in glosses or r < rank[lemma]:
                glosses[lemma] = g
                rank[lemma] = r
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump({"meta": {"source": "https://kaikki.org/dictionary/Turkish/", "license": "CC BY-SA 4.0", "entries": len(glosses)},
                   "glosses": dict(sorted(glosses.items()))}, fh, ensure_ascii=False, separators=(",", ":"))
    print(f"{n} satır okundu, {len(glosses)} madde başı için İngilizce gloss yazıldı → {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", default=DEFAULT_DUMP)
    ap.add_argument("--out", default=OUT)
    args = ap.parse_args()
    if not os.path.exists(args.dump):
        print("döküm yok; python3 DataPipeline/etl_wiktionary.py ile indirin", file=sys.stderr)
        sys.exit(1)
    run(args.dump, args.out)


if __name__ == "__main__":
    main()
