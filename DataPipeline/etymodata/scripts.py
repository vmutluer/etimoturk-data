# -*- coding: utf-8 -*-
"""Tarihsel alfabe ve fonetik gösterim üreticileri.

Bu modül yalnızca *dilbilimsel olgulardan* (kaynak biçimin bilimsel çevriyazısı, ünlü uyumu,
Türkçe yazımın sesçil doğası) yola çıkar; hiçbir sözlük metni kopyalanmaz.

  • old_turkic()      – Eski Türkçe biçimi Göktürk (Orhun) damgalarıyla yazar (öğretici tam yazım).
  • arabic_script()   – Bilimsel çevriyazıdan (kitāb, ḥakīm, maktūb…) Arap/Fars/Osmanlı harflerine döner.
  • arabic_pattern()  – Üçlü (sülasi) kökten vezin kalıbını çıkarır (maktūb → mafʿūl).
  • cyrillic_from_slavic_latin() – Sırp/Hırvat Latin yazımını Kiril'e çevirir.
  • turkish_ipa()     – Türkçe sözlük biçimi için IPA okunuşu üretir (vurgu dâhil).
  • script_name_of()  – Herhangi bir dizenin yazı sistemini Unicode bloklarından tanır.
"""
import re
import unicodedata

# --------------------------------------------------------------------------- Göktürk (Orhun)
# Unicode Old Turkic bloğu (U+10C00–U+10C48), Orhun biçimleri. Yazı sağdan sola akar; dizge
# mantıksal sırada saklanır, görüntüleyici (iOS/CoreText) yönü kendisi çözer.
_OT_VOWEL = {"a": "\U00010C00", "e": "\U00010C00", "ä": "\U00010C00",
             "ı": "\U00010C03", "i": "\U00010C03", "é": "\U00010C03",
             "o": "\U00010C06", "u": "\U00010C06",
             "ö": "\U00010C07", "ü": "\U00010C07"}
# ünsüz: (art/kalın biçim, ön/ince biçim)
_OT_CONS = {
    "b": ("\U00010C09", "\U00010C0B"),
    "d": ("\U00010C11", "\U00010C13"),
    "g": ("\U00010C0D", "\U00010C0F"),
    "ğ": ("\U00010C0D", "\U00010C0F"),
    "l": ("\U00010C1E", "\U00010C20"),
    "n": ("\U00010C23", "\U00010C24"),
    "r": ("\U00010C3A", "\U00010C3C"),
    "s": ("\U00010C3D", "\U00010C3E"),
    "t": ("\U00010C43", "\U00010C45"),
    "y": ("\U00010C16", "\U00010C18"),
    "k": ("\U00010C34", "\U00010C1A"),   # 𐰴 (q, kalın) / 𐰚 (k, ince)
    "q": ("\U00010C34", "\U00010C34"),
    "z": ("\U00010C14", "\U00010C14"),
    "m": ("\U00010C22", "\U00010C22"),
    "p": ("\U00010C2F", "\U00010C2F"),
    "ç": ("\U00010C32", "\U00010C32"),
    "ş": ("\U00010C41", "\U00010C41"),
    "ŋ": ("\U00010C2D", "\U00010C2D"),
    "ñ": ("\U00010C2A", "\U00010C2A"),
    "v": ("\U00010C09", "\U00010C0B"),   # Eski Türkçede v yoktur; b ile yazılır (bér- > ver-)
    "w": ("\U00010C09", "\U00010C0B"),
}
_OT_LIGATURE = {("nç", 0): "\U00010C28", ("nç", 1): "\U00010C28",
                ("nt", 0): "\U00010C26", ("nt", 1): "\U00010C26",
                ("lt", 0): "\U00010C21", ("lt", 1): "\U00010C21"}
_OT_BACK = set("aıouâ")
_OT_FRONT = set("eiöüé")
_OT_VOWELS = set(_OT_VOWEL) | {"â"}


def _strip_marks(text: str) -> str:
    """Çevriyazı işaretlerini (uzunluk, nokta) atar; Türkçe harfleri korur."""
    keep = {"ç", "ğ", "ı", "ö", "ş", "ü", "ŋ", "ñ", "é", "â", "ä"}
    out = []
    for ch in text:
        if ch in keep:
            out.append(ch)
            continue
        base = unicodedata.normalize("NFD", ch)
        out.append(base[0] if base else ch)
    return "".join(out)


def old_turkic(form: str) -> str:
    """Eski Türkçe çevriyazı biçimini Göktürk damgalarıyla yazar.

    Öğretici "tam yazım" uygulanır: bütün ünlüler yazılır, ünsüz damgaları sözcüğün ünlü
    sınıfına (kalın/ince) göre seçilir; ok/uk, ök/ük, ık ve iç heceleri için Orhun bitişik
    damgaları kullanılır. Eski Türkçede bulunmayan sesler (h, f, c, j) geçerse boş döner.
    """
    if not form:
        return ""
    s = _strip_marks(form.lower().strip()).rstrip("-")
    if not s or " " in s or any(ch in s for ch in "hfcjx?'"):
        return ""
    back = next((ch in _OT_BACK for ch in s if ch in _OT_BACK or ch in _OT_FRONT), True)
    cls = 0 if back else 1
    out = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        nxt = s[i + 1] if i + 1 < n else ""
        two = s[i:i + 2]
        if (two, cls) in _OT_LIGATURE and (i + 2 >= n or s[i + 2] not in _OT_VOWELS):
            out.append(_OT_LIGATURE[(two, cls)])
            i += 2
            continue
        if ch in _OT_VOWELS and nxt in ("k", "q") and (i + 2 >= n or s[i + 2] not in _OT_VOWELS):
            lig = None
            if ch in "ou" and cls == 0:
                lig = "\U00010C38"          # 𐰸 ok/uk
            elif ch in "öü" and cls == 1:
                lig = "\U00010C1C"          # 𐰜 ök/ük
            elif ch == "ı" and cls == 0:
                lig = "\U00010C36"          # 𐰶 ık
            if lig:
                out.append(lig)
                i += 2
                continue
        if ch == "i" and nxt == "ç" and (i + 2 >= n or s[i + 2] not in _OT_VOWELS) and cls == 1:
            out.append("\U00010C31")        # 𐰱 iç
            i += 2
            continue
        if ch == "â":
            out.append(_OT_VOWEL["a"])
        elif ch in _OT_VOWEL:
            out.append(_OT_VOWEL[ch])
        elif ch in _OT_CONS:
            out.append(_OT_CONS[ch][cls])
        else:
            return ""
        i += 1
    return "".join(out)


# --------------------------------------------------------------------------- Arap / Fars harfleri
_AR_CONS = {
    "b": "ب", "p": "پ", "t": "ت", "ṯ": "ث", "c": "ج", "ǧ": "ج", "ç": "چ", "ḥ": "ح", "ḫ": "خ",
    "d": "د", "ḏ": "ض", "ḍ": "ض", "ż": "ض", "r": "ر", "z": "ز", "ẕ": "ظ", "ẓ": "ظ", "ž": "ژ", "j": "ژ",
    "s": "س", "ş": "ش", "š": "ش", "ṣ": "ص", "ṭ": "ط", "ʿ": "ع", "ġ": "غ", "f": "ف", "q": "ق",
    "k": "ك", "g": "گ", "l": "ل", "m": "م", "n": "ن", "ñ": "ڭ", "h": "ه", "w": "و", "v": "و", "y": "ي",
}
_AR_LONG = {"ā": "ا", "ī": "ي", "ū": "و", "ō": "و", "ē": "ي", "â": "ا", "î": "ي", "û": "و"}
_AR_SHORT = set("aeiou")
_PERSIAN_SWAP = {"ك": "ک", "ي": "ی"}


def arabic_script(form: str, persian: bool = False) -> str:
    """Bilimsel çevriyazıdan Arap harflerine (Osmanlı/Fars yazımı için `persian=True`) döner.

    Kısa ünlüler yazılmaz (yalnızca söz başında elif), uzun ünlüler ا/ي/و ile yazılır, ikiz ünsüz
    harekesiz yazımda tek harfle gösterilir; sözcük sonu kısa -a Arapça için ة, Farsça/Osmanlıca için ه olur.
    Çevrilemeyen bir karakter varsa boş döner.
    """
    if not form:
        return ""
    s = form.strip().lower().replace("’", "ʾ").replace("'", "ʾ")
    if any(ch in s for ch in "?()[]"):
        return ""
    words = []
    for word in re.split(r"[\s]+", s):
        word = word.strip("-")
        if not word:
            continue
        out = []
        i = 0
        n = len(word)
        prev_cons = ""
        while i < n:
            ch = word[i]
            two = word[i:i + 2]
            if ch == "-":
                i += 1
                continue
            if ch == "ʾ":
                if i == 0:
                    if i + 1 < n and word[i + 1] == "ā":
                        out.append("آ"); i += 2; continue
                    i += 1
                    if i < n and word[i] in _AR_SHORT:
                        out.append("ا"); i += 1
                    continue
                if i == n - 1:
                    out.append("ء")
                else:
                    nxt = word[i + 1]
                    prv = word[i - 1]
                    if nxt in "iī" or prv in "iī":
                        out.append("ئ")
                    elif nxt in "uū" or prv in "uū":
                        out.append("ؤ")
                    elif prv in "āa" and nxt in "āa":
                        out.append("ء")
                    else:
                        out.append("أ")
                i += 1
                continue
            if ch in _AR_LONG:
                if i == 0:
                    out.append({"ā": "آ", "â": "آ", "ī": "اي", "î": "اي", "ū": "او", "û": "او", "ō": "او", "ē": "اي"}[ch])
                else:
                    out.append(_AR_LONG[ch])
                i += 1
                prev_cons = ""
                continue
            if ch in _AR_SHORT:
                if i == 0:
                    out.append("ا")
                elif i == n - 1:
                    if ch == "a":
                        out.append("ه" if persian else "ة")
                    elif ch == "e":
                        out.append("ه")
                    elif ch in "iı":
                        out.append("ي")
                    elif ch in "uo":
                        out.append("و")
                i += 1
                prev_cons = ""
                continue
            if ch in "ıü":
                if i == 0:
                    out.append("ا")
                elif i == n - 1:
                    out.append("ي" if ch == "ı" else "و")
                i += 1
                prev_cons = ""
                continue
            if ch in _AR_CONS:
                # ikiz ünsüz tek harfle yazılır (harekesiz yazım; şedde gösterilmez)
                if not (prev_cons == ch and out):
                    out.append(_AR_CONS[ch])
                prev_cons = ch
                i += 1
                continue
            return ""
        words.append("".join(out))
    text = " ".join(words)
    if persian:
        text = "".join(_PERSIAN_SWAP.get(ch, ch) for ch in text)
    return text


# Kök kodundaki Türkçe büyük harf → çevriyazıda karşılayabileceği ünsüzler
_ROOT_LETTER = {
    "K": "kq", "H": "hḥḫ", "S": "sṣṯš", "T": "tṭ", "D": "dḏḍż", "Z": "zẕẓḏ", "İ": "ʿ", "A": "ʿʾ", "E": "ʿʾ",
    "Ş": "şš", "C": "cǧj", "G": "gġ", "N": "n", "M": "m", "L": "l", "R": "r", "B": "b", "F": "f",
    "W": "wv", "V": "wv", "Y": "y", "P": "pb", "Ğ": "ġ", "Ẕ": "ẕẓḏ", "Ḏ": "ḏḍ", "Q": "q", "O": "ʿ", "U": "ʿ", "I": "ʿ",
}
_PATTERN_SUBST = ["f", "ʿ", "l"]


def arabic_pattern(form: str, root_code: str):
    """Sülasi (üçlü) kökün vezin kalıbını çıkarır: maktūb + K-T-B → mafʿūl.

    Kök harfleri kaynak biçimde sırayla aranır; bulunan radikaller f-ʿ-l ile değiştirilir,
    kalıp eki ve ünlüler korunur. Üç radikal bulunamazsa None döner.
    """
    if not form or not root_code:
        return None
    letters = [p for p in re.split(r"[-\s]+", root_code.strip()) if p]
    if len(letters) != 3 or any(len(p) > 1 for p in letters):
        return None
    cands = []
    for p in letters:
        c = _ROOT_LETTER.get(p.upper())
        if not c:
            return None
        cands.append(set(c))
    s = form.lower().replace("-", "").replace("’", "ʾ").replace("'", "ʾ")
    s = s.split(" ")[0]
    out = []
    idx = 0
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if idx < 3 and ch in cands[idx]:
            out.append(_PATTERN_SUBST[idx])
            # ikiz radikal (şedde): muʿallim → mufaʿʿil
            if i + 1 < n and s[i + 1] == ch:
                out.append(_PATTERN_SUBST[idx])
                i += 1
            idx += 1
        else:
            out.append(ch)
        i += 1
    if idx != 3:
        return None
    pattern = "".join(out)
    # yalnızca Arapça vezin harfleri kalmış olmalı
    if not re.fullmatch(r"[fʿlaiuāīūmtsn]+", pattern):
        return None
    return pattern


# --------------------------------------------------------------------------- Kiril (Slav Latin → Kiril)
_SR_CYR = {"a": "а", "b": "б", "v": "в", "g": "г", "d": "д", "đ": "ђ", "e": "е", "ž": "ж", "z": "з", "i": "и",
           "j": "ј", "k": "к", "l": "л", "m": "м", "n": "н", "o": "о", "p": "п", "r": "р", "s": "с", "t": "т",
           "ć": "ћ", "u": "у", "f": "ф", "h": "х", "c": "ц", "č": "ч", "š": "ш", "y": "ы", "ě": "е", "ę": "ę"}
_SR_DIGRAPH = {"lj": "љ", "nj": "њ", "dž": "џ"}


def cyrillic_from_slavic_latin(form: str) -> str:
    s = form.strip().lower()
    out = []
    i = 0
    while i < len(s):
        two = s[i:i + 2]
        if two in _SR_DIGRAPH:
            out.append(_SR_DIGRAPH[two]); i += 2; continue
        ch = s[i]
        if ch in _SR_CYR:
            out.append(_SR_CYR[ch])
        elif ch in " -":
            out.append(ch)
        else:
            return ""
        i += 1
    return "".join(out)


# --------------------------------------------------------------------------- IPA (Türkiye Türkçesi)
_VOWEL_IPA = {"a": "a", "e": "e", "ı": "ɯ", "i": "i", "o": "o", "ö": "ø", "u": "u", "ü": "y",
              "â": "aː", "î": "iː", "û": "uː"}
_CONS_IPA = {"b": "b", "c": "dʒ", "ç": "tʃ", "d": "d", "f": "f", "h": "h", "j": "ʒ", "m": "m", "n": "n",
             "p": "p", "r": "ɾ", "s": "s", "ş": "ʃ", "t": "t", "v": "v", "y": "j", "z": "z",
             "w": "v", "q": "k", "x": "ks"}
_TR_VOWELS = set(_VOWEL_IPA)
_FRONT_V = set("eiöüîâ")   # â önündeki k/g/l ince söylenir (kâtip, dükkân, lâle)
_BACK_V = set("aıouû")
_TR_LOWER = str.maketrans({"I": "ı", "İ": "i"})


def _syllable_starts(word: str):
    """Türkçe hece başlarının (indeks) listesi: V.V, V.CV, VC.CV, VCC.CV."""
    vowel_idx = [i for i, ch in enumerate(word) if ch in _TR_VOWELS]
    if len(vowel_idx) < 2:
        return [0]
    starts = [0]
    for a, b in zip(vowel_idx, vowel_idx[1:]):
        gap = b - a - 1
        if gap <= 1:
            starts.append(b - gap)           # V.V veya V.CV
        else:
            starts.append(b - 1)             # VC.CV, VCC.CV
    return starts


def _ipa_word(word: str) -> str:
    w = word.translate(_TR_LOWER).lower().replace("'", "").replace("’", "").replace("-", "")
    w = "".join(ch for ch in w if ch.isalpha())
    if not w:
        return ""
    starts = _syllable_starts(w)
    stress_at = starts[-1] if len(starts) > 1 else -1
    out = []
    n = len(w)
    for i, ch in enumerate(w):
        if i == stress_at:
            out.append("ˈ")
        prev_v = next((w[j] for j in range(i - 1, -1, -1) if w[j] in _TR_VOWELS), "")
        next_v = next((w[j] for j in range(i + 1, n) if w[j] in _TR_VOWELS), "")
        nxt = w[i + 1] if i + 1 < n else ""
        if ch in _VOWEL_IPA:
            out.append(_VOWEL_IPA[ch])
        elif ch == "ğ":
            if prev_v and nxt in _TR_VOWELS:
                out.append("j" if (prev_v in _FRONT_V and nxt in _FRONT_V) else "")
            elif prev_v:
                out.append("ː")
        elif ch in ("k", "g"):
            ref = next_v or prev_v
            front = ref in _FRONT_V
            out.append({"k": "c" if front else "k", "g": "ɟ" if front else "g"}[ch])
        elif ch == "l":
            ref = next_v or prev_v
            out.append("l" if ref in _FRONT_V else "ɫ")
        elif ch in _CONS_IPA:
            out.append(_CONS_IPA[ch])
        else:
            # yabancı harf: olduğu gibi
            out.append(ch)
    return "".join(out)


def turkish_ipa(lemma: str) -> str:
    """Sözlük biçimi için IPA (vurgu son hecede; çok sözcüklü maddelerde her sözcük ayrı)."""
    parts = [_ipa_word(p) for p in lemma.split()]
    return " ".join(p for p in parts if p)


# --------------------------------------------------------------------------- Yazı sistemi tanıma
_SCRIPT_TR = {
    "ARABIC": "Arap", "GREEK": "Yunan", "ARMENIAN": "Ermeni", "CYRILLIC": "Kiril", "LATIN": "Latin",
    "CJK": "Çin (Han)", "HEBREW": "İbrani", "GEORGIAN": "Gürcü", "OLD": "Göktürk (Orhun)", "SOGDIAN": "Soğd",
    "SYRIAC": "Süryani", "DEVANAGARI": "Devanagari", "HIRAGANA": "Japon", "KATAKANA": "Japon", "MONGOLIAN": "Moğol",
    "HANGUL": "Kore", "THAI": "Tay", "COPTIC": "Kıpti", "CUNEIFORM": "Çivi yazısı", "EGYPTIAN": "Hiyeroglif",
    "PHOENICIAN": "Fenike", "OLD_PERSIAN": "Eski Fars çivi yazısı",
}


def script_name_of(text: str) -> str:
    """Metindeki ilk harfin Unicode bloğundan Türkçe yazı sistemi adı döndürür."""
    for ch in text:
        if ch.isalpha() or unicodedata.category(ch).startswith("Lo"):
            name = unicodedata.name(ch, "")
            if not name:
                continue
            first = name.split()[0]
            if first == "OLD" and "TURKIC" in name:
                return "Göktürk (Orhun)"
            if first == "OLD" and "PERSIAN" in name:
                return "Eski Fars çivi yazısı"
            if first == "CJK":
                return "Çin (Han)"
            return _SCRIPT_TR.get(first, first.title())
    return ""


def strip_arabic_diacritics(text: str) -> str:
    """Hareke ve şeddeyi atar (Wiktionary biçimleri karışık işaretlenmiştir)."""
    return "".join(ch for ch in text if not (0x064B <= ord(ch) <= 0x0652 or ord(ch) in (0x0670, 0x0640)))


# --------------------------------------------------------------------------- Köken diline göre yazı adı
ORIGIN_SCRIPT_NAME = {
    "ar": "Arap", "fa": "Fars (Arap harfleri)", "ota": "Osmanlı Türkçesi (Arap harfleri)",
    "el": "Yunan", "hy": "Ermeni", "sl": "Kiril", "zh": "Çin (Han)", "ja": "Japon", "he": "İbrani",
    "ka": "Gürcü", "sog": "Soğd", "sa": "Devanagari", "mn": "Moğol (Kiril)", "ku": "Latin (Kürtçe)",
    "fr": "Latin", "it": "Latin", "en": "Latin", "de": "Latin", "la": "Latin", "es": "Latin", "pt": "Latin",
    "nl": "Latin", "hu": "Latin", "ro": "Latin",
}
LATIN_ORIGINS = {"fr", "it", "en", "de", "la", "es", "pt", "nl", "hu", "ro", "ku"}
