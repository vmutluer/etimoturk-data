# -*- coding: utf-8 -*-
"""Ham veri dizelerini ayrıştıran yardımcılar."""
from dataclasses import dataclass, field
from typing import List, Optional

from .lexicon_tr import LEXICON_TR
from .lexicon_ar import LEXICON_AR
from .lexicon_fa import LEXICON_FA
from .lexicon_eu import LEXICON_EU
from .lexicon_extra import LEXICON_EXTRA
from .root_families import ROOT_FAMILIES_RAW
from .cognates_a import COGNATES_A
from .cognates_b import COGNATES_B
from .cognates_c import COGNATES_C

import glob
import importlib
import json
import os
import sys

MULTIWORD_ALLOW = {"ya da"}
CORPORA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "corpora")


def corpora_modules():
    """DataPipeline/corpora/*.py modüllerini ada göre sıralı yükler."""
    mods = []
    for path in sorted(glob.glob(os.path.join(CORPORA_DIR, "*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        if name.startswith("_"):
            continue
        mods.append(importlib.import_module(f"corpora.{name}"))
    return mods


def corpora_blocks(attr: str):
    return [getattr(m, attr) for m in corpora_modules() if hasattr(m, attr)]


def load_generated(name: str):
    """corpora/generated/<name>.json varsa yükler, yoksa None."""
    path = os.path.join(CORPORA_DIR, "generated", name + ".json")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


@dataclass
class LexEntry:
    lemma: str
    pos: str
    origin: str
    disputed: bool
    source_form: str
    source_meaning: str
    era: str
    family: str
    chain: List[tuple] = field(default_factory=list)  # [(stage_code, form)]


@dataclass
class FamilyEntry:
    code: str
    origin: str
    core_meaning: str
    explanation: str


@dataclass
class CognateEntry:
    lemma: str
    direction: str
    lang: str
    foreign: str
    romanization: str
    meaning: str
    false_friend: str


def parse_lexicon() -> List[LexEntry]:
    entries: List[LexEntry] = []
    seen = set()
    for block in (LEXICON_TR, LEXICON_AR, LEXICON_FA, LEXICON_EU, LEXICON_EXTRA, *corpora_blocks("WORDS")):
        for raw in block.strip().splitlines():
            raw = raw.strip()
            if not raw or raw.startswith("#"):
                continue
            parts = raw.split("|")
            if len(parts) != 8:
                raise ValueError(f"Hatalı sözlük satırı: {raw}")
            lemma, pos, origin, src, meaning, era, family, chain = parts
            if " " in lemma and lemma not in MULTIWORD_ALLOW:
                continue
            key = (lemma, pos)
            if key in seen:
                continue
            seen.add(key)
            disputed = origin.endswith("?")
            origin = origin.rstrip("?")
            chain_list = []
            if chain:
                for stage in chain.split(">"):
                    code, _, form = stage.partition(":")
                    chain_list.append((code.strip(), form.strip()))
            entries.append(LexEntry(lemma, pos, origin, disputed, src, meaning, era, family, chain_list))
    return entries


def parse_families() -> List[FamilyEntry]:
    out = []
    seen = set()
    for block in (ROOT_FAMILIES_RAW, *corpora_blocks("FAMILIES")):
        for raw in block.strip().splitlines():
            raw = raw.strip()
            if not raw or raw.startswith("#"):
                continue
            code, origin, meaning, explanation = raw.split("|", 3)
            if code in seen:
                # farklı korpus modüllerinde yinelenen aile: ilk kayıt kazanır (sözcüklerdeki kuralla aynı)
                print(f"uyarı: yinelenen kök ailesi atlandı: {code}", file=sys.stderr)
                continue
            seen.add(code)
            out.append(FamilyEntry(code, origin, meaning, explanation))
    return out


def parse_cognates() -> List[CognateEntry]:
    out: List[CognateEntry] = []
    lemma: Optional[str] = None
    direction = ""
    for block in (COGNATES_A, COGNATES_B, COGNATES_C, *corpora_blocks("COGNATES")):
        for raw in block.splitlines():
            if not raw.strip():
                continue
            if raw.startswith("@"):
                head, direction = raw[1:].rsplit(" ", 1)
                lemma = head.strip()
                continue
            line = raw.strip()
            code, _, rest = line.partition(" ")
            segs = [s.strip() for s in rest.split(";")]
            foreign_part = segs[0]
            roman = ""
            if "[" in foreign_part and foreign_part.endswith("]"):
                foreign, _, roman = foreign_part.partition("[")
                foreign = foreign.strip()
                roman = roman[:-1].strip()
            else:
                foreign = foreign_part.strip()
            meaning = segs[1] if len(segs) > 1 else ""
            ff = ""
            for s in segs[2:]:
                if s.startswith("ff:"):
                    ff = s[3:].strip()
            out.append(CognateEntry(lemma, direction, code, foreign, roman, meaning, ff))
    return out


# ----------------------------------------------------------------------------------------------
# Faz 4: yer adları (TOPONYMS) ve deyim kökenleri (IDIOMS) kayıt DSL'i
#
#   @Ad|tür|il|bölge|plaka|köken          <- yer adı başlığı (plaka boş bırakılabilir)
#   chain: hit:Mazaka>la:Caesarea>tr:Kayseri
#   meaning: ...   story: ...   source: ...   coords: enlem,boylam   era: ...
#
#   @deyim metni|tür|alan                 <- deyim başlığı (tür: deyim / atasözü / tabir / kalıp söz)
#   meaning: ...  literal: ...  story: ...  era: OSM  source: ...  words: a, b  confidence: kesin
# Bir kayıt "@" ile başlar; sonraki "anahtar: değer" satırları o kayda aittir. Çok satırlı değer
# için aynı anahtar yinelenmez; "#" ile başlayan satırlar yorumdur.
# ----------------------------------------------------------------------------------------------

@dataclass
class ToponymEntry:
    name: str
    kind: str
    province: str
    region: str
    plate: Optional[int]
    origin: str
    chain: List[tuple]          # [(stage_code, form)]
    meaning: str
    story: str
    source: str
    era: str
    lat: Optional[float]
    lon: Optional[float]
    module: str = ""


@dataclass
class IdiomEntry:
    phrase: str
    kind: str
    domain: str
    meaning: str
    literal: str
    story: str
    era: str
    source: str
    words: List[str]
    confidence: str
    module: str = ""


def _parse_records(block: str):
    """DSL bloğunu (başlık, {anahtar: değer}) çiftlerine böler."""
    records = []
    head, fields = None, {}
    for raw in block.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("@"):
            if head is not None:
                records.append((head, fields))
            head, fields = line[1:], {}
            continue
        if head is None:
            raise ValueError(f"Başlıksız DSL satırı: {line}")
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"'anahtar: değer' biçiminde olmayan satır ({head}): {line}")
        key = key.strip()
        if key in fields:
            raise ValueError(f"Yinelenen anahtar '{key}' ({head})")
        fields[key] = value.strip()
    if head is not None:
        records.append((head, fields))
    return records


def _parse_chain(text: str):
    out = []
    for stage in text.split(">"):
        code, _, form = stage.partition(":")
        code, form = code.strip(), form.strip()
        if not code or not form:
            raise ValueError(f"Hatalı zincir aşaması: {stage!r} ({text})")
        out.append((code, form))
    return out


def parse_toponyms(blocks=None) -> List[ToponymEntry]:
    """corpora/*.py içindeki TOPONYMS bloklarını ayrıştırır; aynı (ad, il) için ilk kayıt kazanır."""
    out: List[ToponymEntry] = []
    seen = set()
    mods = corpora_modules() if blocks is None else []
    sources = blocks if blocks is not None else [(m.__name__, m.TOPONYMS) for m in mods if hasattr(m, "TOPONYMS")]
    for module_name, block in sources:
        for head, f in _parse_records(block):
            parts = [p.strip() for p in head.split("|")]
            if len(parts) != 6:
                raise ValueError(f"Yer adı başlığı 6 alan olmalı (ad|tür|il|bölge|plaka|köken): {head}")
            name, kind, province, region, plate, origin = parts
            key = (name, province)
            if key in seen:
                continue
            seen.add(key)
            for req in ("chain", "meaning", "story", "source"):
                if not f.get(req):
                    raise ValueError(f"Yer adı '{name}': '{req}' alanı eksik")
            lat = lon = None
            if f.get("coords"):
                a, _, b = f["coords"].partition(",")
                lat, lon = float(a), float(b)
            out.append(ToponymEntry(name, kind, province, region, int(plate) if plate else None, origin,
                                    _parse_chain(f["chain"]), f["meaning"], f["story"], f["source"],
                                    f.get("era", ""), lat, lon, module_name))
    return out


def parse_idioms(blocks=None) -> List[IdiomEntry]:
    """corpora/*.py içindeki IDIOMS bloklarını ayrıştırır; aynı deyim için ilk kayıt kazanır."""
    out: List[IdiomEntry] = []
    seen = set()
    mods = corpora_modules() if blocks is None else []
    sources = blocks if blocks is not None else [(m.__name__, m.IDIOMS) for m in mods if hasattr(m, "IDIOMS")]
    for module_name, block in sources:
        for head, f in _parse_records(block):
            parts = [p.strip() for p in head.split("|")]
            if len(parts) != 3:
                raise ValueError(f"Deyim başlığı 3 alan olmalı (deyim|tür|alan): {head}")
            phrase, kind, domain = parts
            if phrase in seen:
                continue
            seen.add(phrase)
            for req in ("meaning", "literal", "story", "era", "source", "words", "confidence"):
                if not f.get(req):
                    raise ValueError(f"Deyim '{phrase}': '{req}' alanı eksik")
            words = [w.strip() for w in f["words"].split(",") if w.strip()]
            out.append(IdiomEntry(phrase, kind, domain, f["meaning"], f["literal"], f["story"], f["era"],
                                  f["source"], words, f["confidence"], module_name))
    return out
