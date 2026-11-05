# -*- coding: utf-8 -*-
"""İngilizce künye şablon motoru (şema 4): words.etymology_summary_en, root_families.explanation_en,
toponyms.summary_en ve eksik kalan İngilizce alanlar için şablonlar. Telifli metin kullanılmaz; yalnızca
yapısal olgular İngilizce cümlelere dökülür."""
from .english_vocab import (ORIGIN_LANGUAGES_EN, STAGE_NAMES_EN, ATTESTATIONS_EN, PERIODS_EN, POS_EN, SUFFIX_LABELS_EN,
                            DERIVED_GLOSS_EN, TOPONYM_ORIGINS_EN, TOPONYM_KINDS_EN, REGIONS_EN, IDIOM_DOMAINS_EN,
                            stage_name_en_from_tr)
from .languages import STAGE_NAMES
from .templates import OLD_TURKIC_ERAS


def _article(pos_en: str) -> str:
    return "an" if pos_en[0] in "aeiou" else "a"


def chain_text_en(chain_tr):
    """[(Türkçe aşama adı, biçim)] → 'Arabic *kitāb* → Ottoman Turkish *kitāb* → Turkish *kitap*'."""
    return " → ".join(f"{stage_name_en_from_tr(s, STAGE_NAMES)} *{f}*" for s, f in chain_tr)


def first_gloss(g: str) -> str:
    return g.split(";")[0].split(",")[0].strip()


ORIGIN_SENTENCE_EN = {
    "ar": "was borrowed from Arabic {src}{meaning}, entering Turkish through Ottoman Turkish; it is formed on an Arabic root pattern",
    "fa": "was borrowed from Persian {src}{meaning}, entering Turkish through contact with the Iranian cultural sphere",
    "fr": "was borrowed from French {src}{meaning} during the 19th–20th-century period of Westernization",
    "it": "was borrowed from Italian (the Venetian–Genoese trading language) {src}{meaning} through Mediterranean commerce",
    "el": "was borrowed from Greek {src}{meaning} through centuries of neighborly contact in Anatolia",
    "en": "was borrowed from English {src}{meaning} in the 20th century through global culture and technology",
    "mn": "was borrowed from Mongolian {src}{meaning} through Turkic–Mongol contact in Central Asia",
    "sog": "was borrowed from Sogdian {src}{meaning} into Old Turkic during the Silk Road era",
    "sl": "was borrowed from the Slavic languages ({src}{meaning}) through Balkan and Black Sea contact",
    "hy": "was borrowed from Armenian {src}{meaning} through long coexistence in Anatolia",
}


def summary_en_for(entry, gloss_en: str, source_meaning_en: str, family_code, chain_tr) -> str:
    """Elle yazılmış (curated) sözcük için İngilizce künye."""
    o = entry.origin
    pos = POS_EN.get(entry.pos, "word")
    lemma = entry.lemma
    head = f"**{lemma}**" + (f" ('{first_gloss(gloss_en)}')" if gloss_en else "")
    meaning = f" ('{source_meaning_en}')" if source_meaning_en else ""
    src = f"*{entry.source_form}*"
    if o == "tr":
        if entry.era == "DD":
            core = f"{head} is {_article(pos)} {pos} coined in the Language Reform period (after 1932) from the native Turkish root {src}{meaning}, proposed to replace a foreign-derived equivalent."
        elif entry.era in ("MOD", "NEW", "TDK", "CUM"):
            core = f"{head} is {_article(pos)} {pos} derived in the 20th century from the Turkish root {src}{meaning}."
        elif entry.era in OLD_TURKIC_ERAS:
            core = f"{head} is a native Turkish {pos} that developed by regular sound change from Old Turkic {src}{meaning}."
        elif " " in entry.source_form or "-" in entry.source_form.strip("-") or entry.source_form == lemma:
            core = f"{head} is a native Turkish {pos} formed from the Turkish element(s) {src}{meaning}; its earliest written record is from the period {ATTESTATIONS_EN.get(entry.era, entry.era)}."
        else:
            core = f"{head} is a native Turkish {pos} that developed from the Turkish form {src}{meaning}; its earliest written record is from the period {ATTESTATIONS_EN.get(entry.era, entry.era)}."
    elif o in ORIGIN_SENTENCE_EN:
        core = f"{head} is {_article(pos)} {pos} that " + ORIGIN_SENTENCE_EN[o].format(src=src, meaning=meaning) + "."
    elif o == "unk":
        core = f"{head} is {_article(pos)} {pos} whose source language has not been established with certainty; its earliest written record is from the period {ATTESTATIONS_EN.get(entry.era, entry.era)}."
    else:
        name = ORIGIN_LANGUAGES_EN.get(o, "an unknown language")
        core = f"{head} is {_article(pos)} {pos} of {name} origin, from {src}{meaning}."
    parts = [core]
    if len(chain_tr) > 1:
        parts.append("Path of transmission: " + chain_text_en(chain_tr) + ".")
    parts.append("Earliest attestation: " + ATTESTATIONS_EN.get(entry.era, entry.era) + ".")
    if family_code:
        parts.append(f"Root family: {family_code}.")
    if entry.disputed:
        parts.append("Note: the origin of this word is disputed among linguists.")
    return " ".join(parts)


def derived_summary_en(base, d, base_gloss_en: str, source_meaning_en: str) -> str:
    label, desc = SUFFIX_LABELS_EN[d.suffix_key]
    name = ORIGIN_LANGUAGES_EN.get(base.origin, "unknown")
    meaning = f" ('{source_meaning_en}')" if source_meaning_en else ""
    base_g = f" ('{first_gloss(base_gloss_en)}')" if base_gloss_en else ""
    return (f"**{d.lemma}** is derived from {base.lemma}{base_g} with the suffix {d.suffix_surface} ({desc}). "
            f"The base word is of {name} origin: *{base.source_form}*{meaning}.")


def derived_gloss_en(d, base_gloss_en: str) -> str:
    g = first_gloss(base_gloss_en)
    if not g:
        return ""
    return DERIVED_GLOSS_EN[d.suffix_key].format(g=g)


WIKT_ORIGIN_SENTENCE_EN = {
    "tr": "is a native Turkish word inherited from Old Turkic",
    "ar": "is of Arabic origin and entered Turkish through Ottoman Turkish",
    "fa": "is of Persian origin and entered Turkish through Ottoman Turkish",
    "fr": "was borrowed from French in the 19th–20th centuries",
    "it": "was borrowed from Italian (the Mediterranean trading language)",
    "el": "was borrowed from Greek through contact in Anatolia",
    "en": "was borrowed from English in the 20th century",
    "ota": "came into Turkish through Ottoman Turkish; its ultimate source language has not yet been verified against an open source",
}


def wiktionary_summary_en(w: dict, gloss_en: str, chain_tr) -> str:
    origin = w["origin"]
    name = ORIGIN_LANGUAGES_EN.get(origin, "unknown")
    pos = POS_EN.get(w["pos"], "word")
    src = w.get("source_form") or w["lemma"]
    script = w.get("source_script") or ""
    sentence = WIKT_ORIGIN_SENTENCE_EN.get(origin, f"is of {name} origin")
    if w.get("reviewed") and origin == "tr":
        sentence = "is a native Turkish word built from Turkish roots and suffixes"
    if w.get("reviewed") and origin == "unk":
        sentence = "is a word whose origin is uncertain or disputed in the sources"
    src_text = f"*{src}*" + (f" ({script})" if script and script != src else "")
    head = f"**{w['lemma']}**" + (f" ('{first_gloss(gloss_en)}')" if gloss_en else "")
    parts = [f"{head} {sentence}; source form {src_text}. Part of speech: {pos}."]
    if len(chain_tr) > 1:
        parts.append("Path of transmission: " + chain_text_en(chain_tr) + ".")
    method = w.get("method", "")
    if method.startswith("internal:"):
        parts.append(f"Turkish-internal derivation from {method.split(':', 1)[1]}.")
    if w.get("disputed") and origin not in ("ota", "unk"):
        parts.append("Note: the sources do not give this origin with certainty; it is disputed.")
    parts.append("Structural data: Wiktionary (Kaikki.org dump), CC BY-SA 4.0.")
    return " ".join(parts)


def family_explanation_en(fam, core_en: str, members) -> str:
    """Çeviri yoksa kök ailesi için üye listesinden İngilizce açıklama."""
    name = ORIGIN_LANGUAGES_EN.get(fam.origin, "unknown")
    kind = {"tr": "native Turkish root", "ar": "Arabic triliteral root", "fa": "Persian compounding element"}.get(fam.origin, f"{name} root")
    core = f" meaning '{core_en}'" if core_en else ""
    lst = ", ".join(members[:10])
    tail = f"; among its Turkish members are {lst}" if lst else ""
    return f"{fam.code} is {_article(kind)} {kind}{core}{tail}."


def toponym_summary_en(t, meaning_en: str) -> str:
    origin_name = TOPONYM_ORIGINS_EN.get(t.origin, (t.origin, ""))[0]
    kind = TOPONYM_KINDS_EN.get(t.kind, t.kind).lower()
    region = REGIONS_EN.get(t.region, t.region)
    first_code, first_form = t.chain[0]
    parts = []
    if t.kind == "il":
        parts.append(f"{t.name} is a provincial capital in the {region} Region; its name is of {origin_name} origin.")
    else:
        parts.append(f"{t.name} is a {kind} in {t.province} Province; its name is of {origin_name} origin.")
    if len(t.chain) > 1:
        chain = " → ".join(f"{STAGE_NAMES_EN.get(c, c)} *{f}*" for c, f in t.chain)
        parts.append(f"Its earliest known form is {STAGE_NAMES_EN.get(first_code, first_code)} *{first_form}*; the name's journey: {chain}.")
    if meaning_en:
        parts.append(f"Meaning: {meaning_en}.")
    return " ".join(parts)


def toponym_fallback_en(t):
    """Çeviri gelmediyse anlam ve hikâye için yapısal İngilizce metin."""
    origin_name = TOPONYM_ORIGINS_EN.get(t.origin, (t.origin, ""))[0]
    forms = ", ".join(f"{STAGE_NAMES_EN.get(c, c)} {f}" for c, f in t.chain[:-1])
    meaning = f"name of {origin_name} origin; earlier forms: {forms}" if forms else f"name of {origin_name} origin"
    story = (f"The name {t.name} is of {origin_name} origin. Earlier attested forms are {forms}. "
             f"Sources: {t.source}. An English rendering of the full historical account is pending; the Turkish text carries the complete narrative.")
    return meaning, story


def idiom_fallback_en(i):
    dom = IDIOM_DOMAINS_EN.get(i.domain, (i.domain, ""))[0]
    kind = {"deyim": "idiom", "atasözü": "proverb", "tabir": "expression", "kalıp söz": "set phrase"}.get(i.kind, "phrase")
    words = ", ".join(i.words)
    meaning = f"Turkish {kind} from the sphere of {dom.lower()} (key words: {words})"
    literal = f"literal reading built on {words}"
    story = (f"This {kind} belongs to the tradition of {dom.lower()}. Its origin is dated to the period "
             f"'{PERIODS_EN.get(i.era, i.era)}' and documented in: {i.source}. An English rendering of the full origin story is pending; "
             f"the Turkish text carries the complete account.")
    return meaning, literal, story
