# -*- coding: utf-8 -*-
"""Faz 4 satır üreticileri: yer adı ve deyim kayıtlarını özgün şablon metinleriyle veritabanı satırına çevirir."""
import json

from .languages import ATTESTATIONS, PERIODS
from .phase4 import (TOPONYM_ORIGIN_LANGUAGES, TOPONYM_STAGE_NAMES, TOPONYM_KINDS, IDIOM_DOMAINS, IDIOM_CONFIDENCE)
from .templates import normalize


def toponym_stage_name(code: str) -> str:
    return TOPONYM_STAGE_NAMES.get(code, code)


def _chain_text(chain) -> str:
    return " → ".join(f"{toponym_stage_name(c)} *{f}*" for c, f in chain)


def toponym_summary(t) -> str:
    """Yer adı için şablonla üretilen kısa künye (telifli metin kullanılmaz)."""
    origin_name = TOPONYM_ORIGIN_LANGUAGES[t.origin][0]
    kind_name = TOPONYM_KINDS[t.kind]
    first_code, first_form = t.chain[0]
    parts = []
    if t.kind == "il":
        parts.append(f"{t.name}, {t.region} Bölgesi'nde bir il merkezidir; adı {origin_name} kökenlidir.")
    else:
        parts.append(f"{t.name}, {t.province} ilinde bir {kind_name.lower()}dir; adı {origin_name} kökenlidir.")
    if len(t.chain) > 1:
        parts.append(f"En eski bilinen biçimi {toponym_stage_name(first_code)} *{first_form}* olup adın yolculuğu: {_chain_text(t.chain)}.")
    parts.append(f"Anlamı: {t.meaning}.")
    return " ".join(parts)


def make_toponym_row(tid: int, t) -> dict:
    origin_name = TOPONYM_ORIGIN_LANGUAGES[t.origin][0]
    first_code, first_form = t.chain[0]
    return {
        "id": tid,
        "name": t.name,
        "normalized_name": normalize(t.name),
        "kind": t.kind,
        "kind_name": TOPONYM_KINDS[t.kind],
        "province": t.province,
        "region": t.region,
        "plate_code": t.plate,
        "origin_language_code": t.origin,
        "origin_language_name": origin_name,
        "oldest_form": first_form,
        "oldest_stage": toponym_stage_name(first_code),
        "name_evolution_json": json.dumps([{"stage": toponym_stage_name(c), "form": f} for c, f in t.chain], ensure_ascii=False),
        "layer_count": len(t.chain),
        "ancient_forms": " ".join(f for _, f in t.chain[:-1]),
        "meaning": t.meaning,
        "summary": toponym_summary(t),
        "story": t.story,
        "source_note": t.source,
        "era": t.era,
        "latitude": t.lat,
        "longitude": t.lon,
        "meaning_en": "", "summary_en": "", "story_en": "", "kind_name_en": "", "region_en": "", "origin_language_name_en": "",
    }


def make_idiom_row(iid: int, i) -> dict:
    dom = IDIOM_DOMAINS[i.domain]
    return {
        "id": iid,
        "phrase": i.phrase,
        "normalized_phrase": normalize(i.phrase),
        "kind": i.kind,
        "domain_code": i.domain,
        "domain_name": dom[0],
        "meaning": i.meaning,
        "literal_sense": i.literal,
        "origin_story": i.story,
        "era_code": i.era,
        "origin_period": PERIODS.get(i.era, i.era),
        "historical_attestation": ATTESTATIONS.get(i.era, i.era),
        "source_note": i.source,
        "confidence": i.confidence,
        "confidence_name": IDIOM_CONFIDENCE[i.confidence],
        "key_words": ", ".join(i.words),
        "word_count": len(i.phrase.split()),
        "meaning_en": "", "literal_sense_en": "", "origin_story_en": "", "domain_name_en": "", "origin_period_en": "",
        "historical_attestation_en": "", "confidence_name_en": "",
    }
