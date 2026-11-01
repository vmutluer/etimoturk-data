# -*- coding: utf-8 -*-
"""Kişi adları: parçalardan Türkçe ve İngilizce köken hikâyesi üretir ve `person_names` satırlarını kurar.

Hikâyeler yalnızca dilbilimsel olgulardan (köken dili, parçalar ve anlamları, kök ailesi) şablonla yazılır;
telifli ad sözlüğü metni kullanılmaz.
"""
import json

from .languages import ORIGIN_LANGUAGES
from .templates import normalize
from .english_vocab import ORIGIN_LANGUAGES_EN as ORIGIN_LANGUAGE_EN

# Ad kökeni anlatımında dil adları ("Öz Türkçe" yerine "Türkçe")
_LANG_TR = {code: v[0] for code, v in ORIGIN_LANGUAGES.items()}
_LANG_TR["tr"] = "Türkçe"
_LANG_EN = dict(ORIGIN_LANGUAGE_EN)
_LANG_EN["tr"] = "Turkish"

GENDER_TR = {"k": "kadın adı", "e": "erkek adı", "u": "hem kadın hem erkek adı"}
GENDER_EN = {"k": "feminine given name", "e": "masculine given name", "u": "unisex given name"}


def lang_tr(code: str) -> str:
    return _LANG_TR.get(code, code)


def lang_en(code: str) -> str:
    return _LANG_EN.get(code, code)


def _is_suffix(form: str) -> bool:
    return form.startswith("-")


def story_tr(n) -> str:
    origin = lang_tr(n.origin)
    if getattr(n, "disputed", False) and n.origin == "unk":
        s = f"{n.name}, kökeni kesin olarak bilinmeyen bir {GENDER_TR[n.gender]}dır; kaynak dili belirlenememiştir. "
    elif getattr(n, "disputed", False):
        s = f"{n.name}, kökeni kesin olarak bilinmeyen bir {GENDER_TR[n.gender]}dır; en yaygın açıklamaya göre {origin} kökenlidir. "
    else:
        s = f"{n.name}, {origin} kökenli bir {GENDER_TR[n.gender]}dır. "
    parts = n.parts
    if len(parts) == 1:
        p = parts[0]
        s += f"Kaynak biçimi {p.form} “{p.meaning}” anlamındadır"
        s += "." if normalize(p.meaning) == normalize(n.meaning) else f"; ad “{n.meaning}” anlamına gelir."
    else:
        bits = []
        for p in parts:
            tag = "" if p.origin == n.origin else f"{lang_tr(p.origin)} "
            bits.append(f"{tag}{p.form} “{p.meaning}”")
        s += "Ad, " + (" ve ".join([", ".join(bits[:-1]), bits[-1]]) if len(bits) > 2 else " ile ".join(bits))
        s += f" öğelerinden kurulmuştur; “{n.meaning}” anlamına gelir."
        langs = {p.origin for p in parts}
        if len(langs) > 1:
            s += " Farklı dillerden öğelerin birleştiği karma bir addır."
    if n.related:
        if normalize(n.related) == normalize(n.name):
            s += f" Günlük dildeki {n.related} sözcüğünün kendisidir."
        else:
            s += f" Türkçedeki {n.related} sözcüğüyle aynı kökten gelir."
    if n.note:
        s += (" Öteki görüşler: " if getattr(n, "disputed", False) else " ") + n.note
    return s


def story_en(n) -> str:
    origin = lang_en(n.origin)
    if getattr(n, "disputed", False) and n.origin == "unk":
        s = f"{n.name} is a {GENDER_EN[n.gender]} whose origin is not firmly established; its source language has not been determined. "
    elif getattr(n, "disputed", False):
        s = f"{n.name} is a {GENDER_EN[n.gender]} whose origin is not firmly established; the most common account makes it {origin}. "
    else:
        s = f"{n.name} is a {GENDER_EN[n.gender]} of {origin} origin. "
    parts = n.parts
    if len(parts) == 1:
        p = parts[0]
        s += f"Its source form {p.form} means “{p.meaning_en}”"
        s += "." if normalize(p.meaning_en) == normalize(n.meaning_en) else f"; the name means “{n.meaning_en}”."
    else:
        bits = []
        for p in parts:
            tag = "" if p.origin == n.origin else f"{lang_en(p.origin)} "
            bits.append(f"{tag}{p.form} “{p.meaning_en}”")
        s += "It is formed from " + (", ".join(bits[:-1]) + " and " + bits[-1]) + f"; the name means “{n.meaning_en}”."
        if len({p.origin for p in parts}) > 1:
            s += " It is a hybrid name combining elements from different languages."
    if n.related:
        if normalize(n.related) == normalize(n.name):
            s += f" It is the same word as the everyday noun {n.related}."
        else:
            s += f" It shares its root with the Turkish word {n.related}."
    if n.note_en:
        s += (" Other views: " if getattr(n, "disputed", False) else " ") + n.note_en
    return s


def make_name_row(i: int, n, family_ids: dict, lexicon_index: dict) -> dict:
    """`person_names` tablosu satırı. `lexicon_index`: normalize(lemma) → word id."""
    source_form = " + ".join(p.form for p in n.parts)
    related_id = lexicon_index.get(normalize(n.related)) if n.related else None
    return {
        "id": i,
        "name": n.name,
        "normalized_name": normalize(n.name),
        "gender": n.gender,
        "origin_language_code": n.origin,
        "origin_language_name": lang_tr(n.origin),
        "origin_language_name_en": lang_en(n.origin),
        "source_form": source_form,
        "meaning": n.meaning,
        "meaning_en": n.meaning_en,
        "components_json": json.dumps([{"form": p.form, "origin": p.origin, "meaning": p.meaning, "meaning_en": p.meaning_en}
                                       for p in n.parts], ensure_ascii=False),
        "root_family_id": family_ids.get(n.family) if n.family else None,
        "related_word_id": related_id,
        "related_lemma": n.related,
        "story": story_tr(n),
        "story_en": story_en(n),
        "note": n.note,
        "note_en": n.note_en,
        "is_disputed": 1 if getattr(n, "disputed", False) else 0,
    }
