# -*- coding: utf-8 -*-
"""Kural tabanlı yapım eki türetimi (ünlü uyumu + ünsüz benzeşmesi).

Yalnızca çok işlek ve her zaman dilbilgisel sonuç veren ekler kullanılır:
  ad      -> -lI (sıfat), -sIz (sıfat), -lIk (ad)
  sıfat   -> -lIk (ad), -cA (zarf)
  eylem   -> -mA (eylem adı), -(y)Iş (eylem adı)
"""
from dataclasses import dataclass
from typing import List

VOWELS = "aeıioöuüâîû"
BACK = set("aıouâû")
ROUND = set("oöuüû")
VOICELESS_FINAL = set("fstkçşhp")

SUFFIX_LABELS = {
    "lI":  ("-lı", "sahiplik / nitelik sıfatı eki"),
    "sIz": ("-sız", "yokluk sıfatı eki"),
    "lIk": ("-lık", "soyut ad / yer adı eki"),
    "cA":  ("-ca", "biçim ve ölçü zarfı eki"),
    "mA":  ("-ma", "eylemden ad yapma eki"),
    "Iş":  ("-ış", "eylemden ad yapma eki"),
}


@dataclass
class Derived:
    lemma: str
    pos: str
    suffix_key: str
    suffix_surface: str


def last_vowel(word: str):
    for ch in reversed(word):
        if ch in VOWELS:
            return ch
    return None


def harmony_a(word: str) -> str:
    v = last_vowel(word)
    return "a" if (v is None or v in BACK) else "e"


def harmony_i(word: str) -> str:
    v = last_vowel(word)
    if v is None:
        return "ı"
    back = v in BACK
    rnd = v in ROUND
    if back:
        return "u" if rnd else "ı"
    return "ü" if rnd else "i"


def is_voiceless_final(word: str) -> bool:
    return word[-1] in VOICELESS_FINAL


def attach(stem: str, pattern: str) -> str:
    """pattern içindeki A/I/C/D arkifonemlerini stem'e göre gerçekleştirir."""
    out = []
    for ch in pattern:
        if ch == "A":
            out.append(harmony_a(stem))
        elif ch == "I":
            out.append(harmony_i(stem))
        elif ch == "C":
            out.append("ç" if is_voiceless_final(stem) else "c")
        elif ch == "D":
            out.append("t" if is_voiceless_final(stem) else "d")
        else:
            out.append(ch)
    return stem + "".join(out)


def _eligible(lemma: str) -> bool:
    if len(lemma) < 3 or " " in lemma or "'" in lemma:
        return False
    if lemma[0].isupper():
        return False
    return all(ch.isalpha() for ch in lemma)


_BLOCK_ENDINGS = ("lık", "lik", "luk", "lük", "lı", "li", "lu", "lü",
                  "sız", "siz", "suz", "süz", "cı", "ci", "cu", "cü", "çı", "çi", "çu", "çü",
                  "ca", "ce", "ça", "çe")


def derive(entry) -> List[Derived]:
    lemma = entry.lemma
    if not _eligible(lemma):
        return []
    results: List[Derived] = []
    if entry.pos == "n":
        if lemma.endswith(_BLOCK_ENDINGS):
            return []
        results.append(Derived(attach(lemma, "lI"), "adj", "lI", attach("", "lI") if False else _surface(lemma, "lI")))
        results.append(Derived(attach(lemma, "sIz"), "adj", "sIz", _surface(lemma, "sIz")))
        results.append(Derived(attach(lemma, "lIk"), "n", "lIk", _surface(lemma, "lIk")))
    elif entry.pos == "adj":
        results.append(Derived(attach(lemma, "lIk"), "n", "lIk", _surface(lemma, "lIk")))
        if not lemma.endswith(_BLOCK_ENDINGS):
            results.append(Derived(attach(lemma, "CA"), "adv", "cA", _surface(lemma, "CA")))
    elif entry.pos == "v" and (lemma.endswith("mek") or lemma.endswith("mak")):
        stem = lemma[:-3]
        if len(stem) < 2:
            return []
        results.append(Derived(attach(stem, "mA"), "n", "mA", _surface(stem, "mA")))
        if stem[-1] in VOWELS:
            results.append(Derived(attach(stem, "yIş"), "n", "Iş", _surface(stem, "yIş")))
        else:
            soft = stem
            if stem in ("git", "et", "tat", "güt", "dit"):
                soft = stem[:-1] + "d"
            results.append(Derived(attach(soft, "Iş"), "n", "Iş", _surface(soft, "Iş")))
    return results


def _surface(stem: str, pattern: str) -> str:
    return "-" + attach(stem, pattern)[len(stem):]
