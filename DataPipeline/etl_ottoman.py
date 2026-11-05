#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Osmanlı Türkçesi aşamasında kalan Wiktionary kökenlerini (``ota`` = "kaynak dil belirsiz") Wiktionary'nin
Osmanlı Türkçesi maddeleriyle sonuna kadar izler.

Wiktionary'nin Türkçe maddeleri çoğu zaman yalnızca "Osmanlı Türkçesi یكپاره'den" der; asıl kaynak (Farsça
yek-pāre) Osmanlı Türkçesi maddesindedir. Bu ETL, ``etl_wiktionary.py`` çıktısındaki ``ota`` kayıtlarını Kaikki.org
Osmanlı Türkçesi dökümündeki maddelerle eşleştirir ve yalnızca maddenin *açık* etimoloji bilgisi (ety/bor/der/inh
şablonları ya da "Borrowed from Arabic …" cümlesi) varsa kökeni çözer. Eşleşme belirsizse (aynı yazılışlı, farklı
kökenli maddeler) kayıt ``ota`` olarak bırakılır — sezgiyle köken atanmaz.

Kullanım:
    python3 -I DataPipeline/etl_ottoman.py --dump DataPipeline/cache/kaikki.org-dictionary-OttomanTurkish.jsonl

Döküm: https://kaikki.org/dictionary/Ottoman%20Turkish/ (wiktextract; Wiktionary içeriği CC BY-SA 4.0).
Çıktı: ``corpora/generated/ottoman_resolution.json`` — ``build_database.py`` bu dosyayı varsa uygular; döküm
depoda tutulmaz (``cache/`` gitignore'da), çözümler tutulur, böylece veritabanı dökümsüz de yeniden üretilebilir.
"""
import argparse
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from etl_wiktionary import ORIGIN_MAP, STAGE_CODE_MAP, TEXT_LANG_MAP, TREE_LANG_MAP, TURKIC_CODES  # noqa: E402

WIKT_JSON = os.path.join(HERE, "corpora", "generated", "wiktionary_tr.json")
OUT_JSON = os.path.join(HERE, "corpora", "generated", "ottoman_resolution.json")

ARABIC_RE = re.compile(r"[؀-ۿﭐ-﷿ﹰ-﻿]")
HARAKAT_RE = re.compile(r"[ً-ٰٟـ‌‍‎‏\s]")
REF_RE = re.compile(r"^\s*([A-Za-z][A-Za-z\-\.]*):([^<\n]*)")
# Türkçe içi kökene işaret eden Wiktionary dilleri (Proto-Turkic, Eski Anadolu Türkçesi …)
AFFIX_KINDS = (":af", ":af<surf>", ":com", ":suf", ":compound")
LOAN_KINDS = (":bor", ":der", ":inh", ":lbor", ":slbor", ":uder", ":bor<unc>", ":der<unc>", ":inh<unc>",
              ":der<conj:and>", ":bor<conj:and>", ":pcal")


def norm_script(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    s = s.replace("ك", "ک").replace("ي", "ی").replace("ى", "ی").replace("ۀ", "ه").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    return HARAKAT_RE.sub("", s)


# Osmanlı Türkçesi çevriyazı işaretleri (â, ā, ḳ, ḥ, ż, ñ …) atılır; Türkçe harflerin işaretleri (ç ş ğ ö ü) korunur,
# yoksa "keşir" ile "kesir", "cayır" ile "çayır" eşleşir.
DROP_MARKS = {"̀", "́", "̂", "̃", "̄", "̇", "̣", "̱", "̲", "̮"}


def norm_roman(s: str) -> str:
    s = (s or "").replace("I", "ı").replace("İ", "i").lower().replace("ġ", "ğ").replace("ḡ", "ğ").replace("ñ", "n")
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if ch not in DROP_MARKS)
    s = unicodedata.normalize("NFC", s)
    return re.sub(r"[\s\-'’ʼʻ‘·.ʿʾ]", "", s)


CHAIN_START_RE = re.compile(r"\b(?:Borrowed|Inherited|Derived|Learned borrowing|Semi-learned borrowing|Orthographic borrowing|From)\b")
CHAIN_STOP_RE = re.compile(r"\b(?:Cognate|Compare|Doublet|Akin|Cf\.|See also|Displaced|Related to|Equivalent to)\b")
FROM_LANG_RE = re.compile(r"\b[Ff]rom\s+((?:[A-Z][a-z]+[ -]){0,3}[A-Z][a-z]+)")
HEDGE_RE = re.compile(r"\b(?:possibly|probably|perhaps|uncertain|unknown|unclear|disputed|obscure|may be|might be)\b", re.I)
# Türkçe tarihsel geçiş aşamaları: kökeni belirlemez, zincirde bir sonraki dile bakılır
PASS_THROUGH = {"Ottoman Turkish", "Old Anatolian Turkish", "Chagatai", "Turkish"}
NATIVE = {"Proto-Turkic", "Old Turkic", "Proto-Oghuz", "Old Uyghur", "Karakhanid", "Proto-Common Turkic", "Kipchak"}


def etymology_core(text: str) -> str:
    """Etimoloji metninin "Etymology tree" dökümü ve "Cognate with …" kısmı dışındaki zincir cümlesi."""
    m = CHAIN_START_RE.search(text or "")
    if not m:
        return ""
    core = text[m.start():]
    stop = CHAIN_STOP_RE.search(core)
    return core[:stop.start()] if stop else core


def text_chain(core: str) -> list:
    """"from X" ifadelerindeki dil adları, metindeki sırasıyla."""
    out = []
    for m in FROM_LANG_RE.finditer(core):
        name = m.group(1).strip()
        words = name.split()
        for i in range(len(words)):  # "Classical Persian" → "Persian" geri düşüşü
            cand = " ".join(words[i:])
            if cand in TREE_LANG_MAP or cand in TEXT_LANG_MAP or cand in PASS_THROUGH or cand in NATIVE:
                out.append(cand)
                break
    return out


def lang_class(name: str):
    if name in NATIVE:
        return "tr"
    cls = (TREE_LANG_MAP.get(name) or (None, None))[1]
    return cls or TEXT_LANG_MAP.get(name)


def source_term(templates: list, cls: str) -> str:
    """Seçilen köken dilindeki kaynak biçim (şablon argümanlarından)."""
    for t in templates:
        for v in (t.get("args") or {}).values():
            for m in re.finditer(r"(?:^|<ety:[^<]*<|,\s*)([A-Za-z][\w\-\.]*):([^<>,\n]+)", str(v)):
                code, term = m.group(1), m.group(2).strip()
                if term and term != "-" and (ORIGIN_MAP.get(code) == cls or (cls == "tr" and code in TURKIC_CODES and code not in ("ota", "trk-oat"))):
                    return term
        a = t.get("args") or {}
        if t.get("name") in ("bor", "bor+", "der", "der+", "inh", "inh+") and ORIGIN_MAP.get(a.get("2", "")) == cls and a.get("3"):
            return a["3"].strip()
    return ""


def pick_origin(seq: list, method: str):
    for i, name in enumerate(seq):
        if name in PASS_THROUGH:
            continue
        cls = lang_class(name)
        if not cls or cls == "ota":
            return None
        if cls == "fa" and i + 1 < len(seq) and lang_class(seq[i + 1]) == "ar":
            return ("ar", seq[i + 1], "", method + ":fa>ar")
        return (cls, name, "", method)
    return None


def romanizations(e: dict) -> list:
    return [f["form"] for f in e.get("forms") or [] if "romanization" in (f.get("tags") or []) and f.get("form")]


def is_affix_entry(e: dict) -> bool:
    return e.get("pos") in ("suffix", "prefix", "infix", "affix", "interfix") or (e.get("word") or "").startswith(("ـ", "-")) \
        or (e.get("word") or "").endswith(("ـ", "-"))


class OttomanIndex:
    def __init__(self, dump_path: str):
        self.by_script = defaultdict(list)
        self.by_roman = defaultdict(list)
        with open(dump_path, encoding="utf-8") as fh:
            for line in fh:
                try:
                    e = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if e.get("lang_code") != "ota":
                    continue
                self.by_script[norm_script(e["word"])].append(e)
                for r in romanizations(e):
                    self.by_roman[norm_roman(r)].append(e)

    # ------------------------------------------------------------------
    def origin_of(self, e: dict, depth: int = 0, seen=None):
        """Osmanlı Türkçesi maddesinin kökeni: (köken sınıfı, dil, kaynak biçim, yöntem) ya da None.

        Etimoloji cümlesindeki "… from X …, from Y" zinciri sırayla izlenir. Eski Anadolu Türkçesi ve Osmanlı
        Türkçesi yalnızca *geçiş* aşamasıdır: "Inherited from Old Anatolian Turkish عشق, from Arabic عِشْق" →
        Arapça. Farsça üzerinden gelen Arapça sözcükler (Farsça X, Arapça Y'den) Türk etimoloji geleneğine ve
        elle yazılmış sözlüğe uygun olarak Arapça sayılır. "Possibly/probably/uncertain" içeren tahminler alınmaz.
        """
        seen = seen or set()
        key = (e["word"], e.get("pos"), e.get("etymology_number"))
        if key in seen or depth > 3:
            return None
        seen.add(key)
        text = etymology_core(e.get("etymology_text") or "")
        if HEDGE_RE.search(text):
            return None
        templates = e.get("etymology_templates") or []
        for t in templates:
            name, a = t.get("name"), t.get("args") or {}
            affix_ety = name == "ety" and a.get("1") == "ota" and (a.get("2") or "").strip() in AFFIX_KINDS
            if affix_ety or (name in ("af", "affix", "suffix", "compound", "com", "surf") and a.get("1") == "ota"):
                first = 3 if name == "ety" else 2
                refs = [v for k, v in sorted(a.items(), key=lambda kv: kv[0]) if k.isdigit() and int(k) >= first]
                return self._components(refs, depth, seen)
            if name == "prefix" and a.get("1") == "ota":
                return self._components([a.get("3") or ""], depth, seen)
        seq = text_chain(text)
        res = pick_origin(seq, "text") if seq else None
        if res:
            return (res[0], res[1], source_term(templates, res[0]), res[3])
        return None

    def _lang_result(self, lang: str, term: str, method: str):
        term = re.sub(r"<.*", "", term, flags=re.S).strip()
        if lang in ("ota", "trk-oat", "chg"):
            return None  # geçiş aşaması: bileşenin kendi kökeni bilinmiyor
        if lang in TURKIC_CODES:
            return ("tr", lang, term, method)
        cls = ORIGIN_MAP.get(lang)
        return (cls, lang, term, method) if cls else None

    def _components(self, refs, depth, seen, strict=False):
        """Ekli ya da birleşik madde: eklerin dışındaki sözlüksel bileşenlerin kökeni.

        Ekler (ـجی, ـلو …) Türkçe dilbilgisi öğesidir ve kökeni belirlemez. Birden çok sözlüksel bileşen varsa
        (kara + kuş) hepsi aynı köken sınıfındaysa kabul edilir; karışık birleşiklere köken atanmaz.
        """
        found = []
        for ref in refs:
            ref = (ref or "").strip()
            if not ref:
                continue
            m = REF_RE.match(ref)
            if m:  # bileşen başka bir dilden: "fa:..."
                res = self._lang_result(m.group(1), m.group(2).strip(), "affix")
                if not res:
                    return None
                found.append((res, m.group(2).strip()))
                continue
            comp = re.sub(r"<.*", "", ref, flags=re.S).strip()
            if not comp or comp.startswith(("ـ", "-")) or comp.endswith(("ـ", "-")):
                continue
            cands = [c for c in self.by_script.get(norm_script(comp), []) if not is_affix_entry(c)]
            if not cands:
                if strict:
                    return None  # boşluklu birleşikte her sözcük izlenebilmeli
                continue  # bileşenin maddesi yok (çoğunlukla ek): diğer bileşenlere bak
            origins = {self.origin_of(c, depth + 1, set(seen)) for c in cands}
            origins.discard(None)
            classes = {o[0] for o in origins}
            if len(classes) != 1:
                return None  # bileşenin kökeni belirsiz
            found.append((sorted(origins)[0], comp))
        if not found or len({o[0] for o, _ in found}) != 1:
            return None
        o, comp = found[0]
        return (o[0], o[1], o[2], "component:" + comp)

    # ------------------------------------------------------------------
    def resolve(self, w: dict):
        """wiktionary_tr.json kaydı için (çözüm, gerekçe) döndürür."""
        method = w.get("method", "")
        base = method.split(":", 1)[1] if method.startswith("internal:") else ""
        script = w.get("source_script") or ""
        if not script and ARABIC_RE.search(w.get("source_form") or ""):
            script = w["source_form"]
        romans = {norm_roman(x) for x in (base, w.get("source_form") if not ARABIC_RE.search(w.get("source_form") or "") else "",
                                          "" if base else w["lemma"]) if x}
        cands = list(self.by_script.get(norm_script(script), [])) if script else []
        via = "script"
        if cands and romans:
            # Osmanlı yazısı çok anlamlıdır (بین: beyn "ara" / beyin): çevriyazısı uyuşmayan madde alınmaz
            matched = [c for c in cands if {norm_roman(r) for r in romanizations(c)} & romans]
            cands = matched or [c for c in cands if not romanizations(c)]
        if not cands and romans:
            cands = [c for r in romans for c in self.by_roman.get(r, [])]
            via = "roman"
        cands = [c for c in cands if not is_affix_entry(c)]
        if not cands and script and " " in script.strip():
            # Osmanlıca yazımı boşluklu birleşik (قره قوش): bileşenleri ayrı ayrı izle
            res = self._components(script.split(), 0, set(), strict=True)
            if res:
                return {"origin": res[0], "source_lang": res[1], "source_term": res[2], "ota_word": script.strip(),
                        "ota_roman": w.get("source_form") or "", "method": f"ota-words:{res[3]}"}, "resolved"
            return None, "no_entry"
        if not cands:
            return None, "no_entry"
        results = {}
        for c in cands:
            o = self.origin_of(c)
            if o:
                results.setdefault(o[0], []).append((c, o))
        if not results and script and " " in script.strip():
            res = self._components(script.split(), 0, set(), strict=True)
            if res:
                return {"origin": res[0], "source_lang": res[1], "source_term": res[2], "ota_word": script.strip(),
                        "ota_roman": w.get("source_form") or "", "method": f"ota-words:{res[3]}"}, "resolved"
        if not results:
            return None, "no_etymology"
        if len(results) > 1:
            # Aynı yazılışlı farklı kökenli maddeler: İngilizce anlam örtüşmesiyle seç, yoksa çözme
            gloss = set(re.findall(r"[a-z]{3,}", (w.get("gloss_en") or "").lower()))
            scored = []
            for cls, items in results.items():
                words = set()
                for c, _ in items:
                    for s in c.get("senses") or []:
                        for g in s.get("glosses") or []:
                            words |= set(re.findall(r"[a-z]{3,}", g.lower()))
                scored.append((len(gloss & words), cls))
            scored.sort(reverse=True)
            if not gloss or scored[0][0] == 0 or scored[0][0] == scored[1][0]:
                return None, "ambiguous"
            results = {scored[0][1]: results[scored[0][1]]}
        cls, items = next(iter(results.items()))
        c, (_, lang, term, how) = items[0]
        roman = (romanizations(c) or [""])[0]
        return {
            "origin": cls, "source_lang": lang, "source_term": term, "ota_word": c["word"], "ota_roman": roman,
            "method": f"ota-{via}:{how}",
        }, "resolved"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dump", default=os.path.join(HERE, "cache", "kaikki.org-dictionary-OttomanTurkish.jsonl"))
    ap.add_argument("--wikt", default=WIKT_JSON)
    ap.add_argument("--out", default=OUT_JSON)
    args = ap.parse_args()
    if not os.path.exists(args.dump):
        print(f"Osmanlı Türkçesi dökümü yok: {args.dump}", file=sys.stderr)
        return 1
    idx = OttomanIndex(args.dump)
    wikt = json.load(open(args.wikt, encoding="utf-8"))
    out, stats = {}, Counter()
    for w in wikt["words"]:
        if w.get("origin") != "ota":
            continue
        res, why = idx.resolve(w)
        stats[why] += 1
        if res:
            stats[f"origin_{res['origin']}"] += 1
            out[f"{w['lemma']}|{w['pos']}"] = res
    payload = {
        "meta": {
            "source": "Kaikki.org Osmanlı Türkçesi dökümü (wiktextract) — Wiktionary katkıcıları, CC BY-SA 4.0",
            "dump": os.path.basename(args.dump),
            "stats": dict(sorted(stats.items())),
        },
        "resolutions": dict(sorted(out.items())),
    }
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print(json.dumps(payload["meta"]["stats"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
