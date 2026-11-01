# -*- coding: utf-8 -*-
"""İngilizce kontrollü sözlükler (şema 4, çift dilli içerik).

Türkçe meta verilerin (köken dilleri, aşama adları, dönemler, kayıtlar, hedef diller, bölgeler, yer adı türleri,
deyim alanları, sözcük türleri, yapım ekleri) İngilizce karşılıkları. Serbest metinler (kaynak anlamlar, hikâyeler)
`DataPipeline/english/*.tsv` dosyalarından (english_loader) gelir; buradaki sözlükler şablon motorunun iskeletidir.
"""

# Köken dili sınıfları (origin_languages.name_en)
ORIGIN_LANGUAGES_EN = {
    "tr": "Old Turkic (native Turkish)", "ar": "Arabic", "fa": "Persian", "fr": "French", "it": "Italian",
    "el": "Greek (Rumeic)", "en": "English", "hy": "Armenian", "mn": "Mongolian", "sl": "Slavic languages",
    "sog": "Sogdian", "la": "Latin", "de": "German", "es": "Spanish", "pt": "Portuguese", "zh": "Chinese",
    "sa": "Sanskrit / Hindi", "he": "Hebrew / Aramaic", "ro": "Romanian", "hu": "Hungarian", "ka": "Georgian",
    "nl": "Dutch", "ja": "Japanese", "ku": "Kurdish", "ota": "Ottoman Turkish (source language uncertain)",
    "unk": "Unknown",
}

# Fonetik evrim aşamaları
STAGE_NAMES_EN = {
    "tr": "Turkish", "otk": "Old Turkic", "ota": "Ottoman Turkish", "eat": "Old Anatolian Turkish", "ar": "Arabic",
    "fa": "Persian", "pal": "Middle Persian (Pahlavi)", "fr": "French", "it": "Italian", "ven": "Venetian", "el": "Greek",
    "grc": "Ancient Greek", "la": "Latin", "en": "English", "hy": "Armenian", "mn": "Mongolian", "sl": "Slavic languages",
    "bg": "Bulgarian", "sr": "Serbian", "ru": "Russian", "sog": "Sogdian", "de": "German", "es": "Spanish",
    "pt": "Portuguese", "zh": "Chinese", "sa": "Sanskrit", "hi": "Hindi / Urdu", "he": "Hebrew", "arc": "Aramaic",
    "ro": "Romanian", "hu": "Hungarian", "ka": "Georgian", "nl": "Dutch", "ja": "Japanese", "ku": "Kurdish",
    "akk": "Akkadian", "sum": "Sumerian", "nah": "Nahuatl (Aztec)", "tai": "Taino", "tup": "Tupi", "cs": "Czech",
    "pie": "Proto-Indo-European", "ptk": "Proto-Turkic", "ml": "Malay", "ta": "Tamil", "ar-eg": "Egyptian Arabic",
    "ar-mag": "Maghrebi Arabic", "hr": "Croatian", "pl": "Polish", "cop": "Coptic", "egy": "Ancient Egyptian",
    "ber": "Berber", "ger": "Germanic", "fro": "Old French", "oc": "Occitan", "ca": "Catalan", "ga": "Irish", "ur": "Urdu", "sq": "Albanian", "evn": "Evenki", "unk": "Unknown",
    # yer adı aşamaları
    "hat": "Hattic", "hit": "Hittite", "xlu": "Luwian", "xur": "Urartian", "phr": "Phrygian", "lyd": "Lydian",
    "xcr": "Carian", "xlc": "Lycian", "thr": "Thracian", "syc": "Syriac", "byz": "Byzantine Greek",
    "sel": "Seljuk Turkish", "gen": "Genoese", "lzz": "Laz", "ass": "Assyrian", "pis": "Pisidian", "hur": "Hurrian",
    "cum": "Republican-era Turkish",
}

# Türkçe aşama adı → İngilizce (phonetic_evolution_json yalnızca Türkçe adları saklar; geri eşleme için)
def stage_name_en_from_tr(name_tr: str, tr_names: dict) -> str:
    """STAGE_NAMES (tr) sözlüğündeki Türkçe ada karşılık gelen İngilizce adı döndürür."""
    for code, tr in tr_names.items():
        if tr == name_tr:
            return STAGE_NAMES_EN.get(code, name_tr)
    return _EXTRA_STAGE_TR_EN.get(name_tr, name_tr)


_EXTRA_STAGE_TR_EN = {
    "Türetme kökü": "Derivational base", "Türkçe yapım eki": "Turkish derivational suffix",
    "Türkçe kaynak biçim": "Turkish source form",
}

# En eski kayıt (historical_attestation_en)
ATTESTATIONS_EN = {
    "ORH": "Orkhon Inscriptions (8th c.) – Old Turkic",
    "UYG": "Old Uyghur texts (9th–10th c.)",
    "DLT": "Dīwān Lughāt al-Turk, Maḥmūd al-Kāshgharī (1072)",
    "KB":  "Kutadgu Bilig, Yūsuf Khāṣṣ Ḥājib (1069)",
    "CC":  "Codex Cumanicus (1303) – Kipchak Turkic",
    "EAT": "Old Anatolian Turkish texts (13th–15th c.)",
    "YE":  "Dīvān of Yunus Emre (13th c.)",
    "DK":  "Book of Dede Korkut (15th c.)",
    "OSM": "Ottoman Turkish texts (16th–18th c.)",
    "MEN": "Meninski, Thesaurus Linguarum Orientalium (1680)",
    "EVL": "Evliya Çelebi's Seyahatnâme (17th c.)",
    "LO":  "Lehcetü'l-Lugat, Esad Efendi (1732)",
    "LOS": "Lehce-i Osmânî, Ahmed Vefik Paşa (1876)",
    "KT":  "Kamus-ı Türkî, Şemseddin Sami (1901)",
    "RH":  "Redhouse, A Turkish and English Lexicon (1890)",
    "OSM19": "19th-century Ottoman press and literature",
    "CUM": "Early Republican press (1923–1945)",
    "DD":  "Language Reform coinages (post-1932, Turkish Language Association)",
    "TDK": "TDK Türkçe Sözlük (1945)",
    "MOD": "Press and technical texts of the later 20th century",
    "NEW": "21st-century digital and technical Turkish",
    "WIKT": "Wiktionary (Kaikki.org dump) etymology record; earliest written attestation not specified",
}

PERIODS_EN = {
    "ORH": "Old Turkic (8th c.)", "UYG": "Old Turkic (9th–10th c.)", "DLT": "Karakhanid Turkic (11th c.)",
    "KB": "Karakhanid Turkic (11th c.)", "CC": "Kipchak Turkic (14th c.)", "EAT": "Old Anatolian Turkish (13th–15th c.)",
    "YE": "Old Anatolian Turkish (13th c.)", "DK": "Old Anatolian Turkish (15th c.)", "OSM": "Ottoman Turkish (16th–18th c.)",
    "MEN": "Ottoman Turkish (17th c.)", "EVL": "Ottoman Turkish (17th c.)", "LO": "Ottoman Turkish (18th c.)",
    "LOS": "Ottoman Turkish (19th c.)", "KT": "Late Ottoman Turkish (19th–20th c.)", "RH": "Late Ottoman Turkish (19th c.)",
    "OSM19": "Late Ottoman Turkish (19th c.)", "CUM": "Early Republican period (1923–1945)",
    "DD": "Language Reform period (1932–1950)", "TDK": "Republican period (post-1945)",
    "MOD": "Contemporary Turkish (post-1950)", "NEW": "Contemporary Turkish (post-2000)",
    "WIKT": "Period not specified (Wiktionary record)",
}

# Karşılaştırma dilleri (languages.name_en) ve bölge grupları
TARGET_LANGUAGES_EN = {
    "az": "Azerbaijani", "kk": "Kazakh", "uz": "Uzbek", "tk": "Turkmen", "ky": "Kyrgyz", "el": "Greek", "bg": "Bulgarian",
    "sr": "Serbian / Bosnian / Croatian", "sq": "Albanian", "ro": "Romanian", "mk": "Macedonian", "it": "Italian",
    "fa": "Persian", "ar": "Arabic", "hy": "Armenian", "ka": "Georgian", "ur": "Urdu / Hindi", "hu": "Hungarian",
    "ru": "Russian", "uk": "Ukrainian", "fr": "French", "en": "English", "de": "German", "pl": "Polish", "es": "Spanish",
    "pt": "Portuguese", "mn": "Mongolian", "he": "Hebrew",
}
REGION_GROUPS_EN = {
    "Türk Dünyası": "Turkic World", "Balkanlar": "Balkans", "Akdeniz": "Mediterranean", "Orta Doğu": "Middle East",
    "Kafkasya": "Caucasus", "Güney Asya": "South Asia", "Avrupa": "Europe", "Avrasya": "Eurasia",
}
BORROWING_DIRECTION_EN = {"from_turkish": "From Turkish to the world", "into_turkish": "From the world into Turkish", "shared_ancestor": "Shared origin"}

# Yer adları
TOPONYM_ORIGINS_EN = {
    "hat": ("Hattic", "3rd–2nd millennium BCE, pre-Hittite Anatolia"), "hit": ("Hittite", "17th–12th c. BCE, Hittite Empire"),
    "xlu": ("Luwian", "2nd–1st millennium BCE, southern and western Anatolia"), "xur": ("Urartian", "9th–6th c. BCE, Lake Van basin"),
    "akk": ("Assyrian / Akkadian", "2nd millennium BCE, Assyrian trade colonies"), "phr": ("Phrygian", "8th–4th c. BCE, central Anatolia"),
    "lyd": ("Lydian", "7th–4th c. BCE, Gediz basin"), "xcr": ("Carian", "1st millennium BCE, southwestern Anatolia"),
    "xlc": ("Lycian", "1st millennium BCE, Teke Peninsula"), "thr": ("Thracian", "1st millennium BCE, Thrace"),
    "pis": ("Pisidian", "1st millennium BCE, highland cities of the Lakes Region"),
    "el": ("Greek", "8th c. BCE – 20th c., coastal colonies and Byzantium"), "la": ("Latin", "1st c. BCE – 7th c. CE, Roman provinces"),
    "fa": ("Persian", "Achaemenid satrapies and the Seljuk period"), "hy": ("Armenian", "Eastern Anatolia, Cilicia"),
    "syc": ("Syriac / Aramaic", "Southeastern Anatolia, Tur Abdin"), "ar": ("Arabic", "after the 7th c., Umayyad–Abbasid frontier zones"),
    "ka": ("Georgian / Laz", "Eastern Black Sea and the Çoruh basin"), "ku": ("Kurdish", "Eastern and southeastern Anatolia"),
    "it": ("Italian (Genoese / Venetian)", "13th–15th c. trading colonies"), "mn": ("Mongolian", "13th-c. Ilkhanid period and words inherited into Old Turkic"),
    "tr": ("Oghuz Turkish", "Seljuk, Beylik and Ottoman periods after 1071"), "unk": ("Unknown / disputed", "Source language cannot be determined"),
}
TOPONYM_KINDS_EN = {
    "il": "Province", "ilçe": "District", "semt": "Quarter / Neighborhood", "bölge": "Region", "antik_kent": "Ancient City",
    "ada": "Island", "boğaz": "Strait", "göl": "Lake", "dağ": "Mountain", "nehir": "River", "yarımada": "Peninsula",
    "körfez": "Gulf", "kale": "Castle", "köy": "Village / Town",
}
REGIONS_EN = {
    "Marmara": "Marmara", "Ege": "Aegean", "Akdeniz": "Mediterranean", "İç Anadolu": "Central Anatolia",
    "Karadeniz": "Black Sea", "Doğu Anadolu": "Eastern Anatolia", "Güneydoğu Anadolu": "Southeastern Anatolia",
}

# Deyimler
IDIOM_DOMAINS_EN = {
    "ahilik": ("Ahi Brotherhood and Guild Tradition", "Ahi organization, guild customs, the apprentice–journeyman–master order and the girding of the apron"),
    "denizcilik": ("Ottoman Seafaring", "Galley- and galleon-era nautical language, levends and captains, Pîrî Reis's Kitâb-ı Bahriye"),
    "okculuk": ("Archery and Hunting", "Ottoman archers, the Okmeydanı range, distance stones, falconry and hunting customs"),
    "tasavvuf": ("Sufism and Lodge Culture", "The lodge language of the Mevlevi, Bektashi and other orders: sema, retreat and ritual"),
    "tarim": ("Farming, Herding and Nomadic Life", "Threshing, the plough, the summer-pasture–winter-quarters cycle, sheep and horse culture"),
    "antik": ("Ancient Anatolian and Mediterranean Traditions", "Set phrases and rites inherited from Greek, Roman and Byzantine antiquity"),
    "askerlik": ("Janissary Corps and Military Life", "Overturning the cauldron, corps customs, sword and shield, drum and zurna, campaign language"),
    "saray": ("Palace, Divan and State", "The Ottoman palace, the Imperial Council, protocol and pasha–vizier relations"),
    "din": ("Religion, Worship and Folk Belief", "Phrases from the Qur'an and hadith, the evil eye, luck and folk beliefs"),
    "mutfak": ("Kitchen and Table", "Ottoman and Anatolian cuisine, table manners, coffee and tea culture"),
    "gundelik": ("Bathhouse, Dress and Daily Life", "The hammam, clothing, household order, neighborliness and hospitality"),
    "ticaret": ("Bazaar, Trade and Money", "Covered markets, caravans, akçe and gold, bargaining and weighing"),
    "hukuk": ("Law, Kadis and Punishment", "Kadi courts, testimony, surety, the bastinado and penal practice"),
    "beden": ("Body and Folk Medicine", "Idioms built on body parts, cupping, bone-setting and folk healing"),
    "oyun": ("Games, Entertainment and Sport", "Backgammon, chess, wrestling, jereed, Karagöz–Hacivat and the storyteller"),
    "hayvan": ("Animals and Nature", "Similes drawn from animal behavior and natural phenomena"),
    "edebiyat": ("Literature, Tales and Folk Stories", "Nasreddin Hoca, Dede Korkut, folk tales and divan poetry"),
    "zanaat": ("Crafts and Workshop", "The language of the smith, weaver, potter, goldsmith and calligrapher"),
}
IDIOM_KINDS_EN = {"deyim": "idiom", "atasözü": "proverb", "tabir": "expression", "kalıp söz": "set phrase"}
IDIOM_CONFIDENCE_EN = {
    "kesin": "Documented: the origin narrative itself rests on a written source (anecdote, epic, classical text, travelogue)",
    "olası": "Probable: consistent with word meanings and period evidence; the origin narrative is not documented in writing",
    "halk_etimolojisi": "Popular (folk) explanation without documentary proof, reported with caution",
}

# Sözcük türleri ve yapım ekleri
POS_EN = {"n": "noun", "v": "verb", "adj": "adjective", "adv": "adverb", "pron": "pronoun", "conj": "conjunction",
          "num": "numeral", "intj": "interjection", "postp": "postposition", "prop": "proper noun"}
SUFFIX_LABELS_EN = {
    "lI": ("-lı", "adjective-forming suffix of possession or quality ('having, with')"),
    "sIz": ("-sız", "privative adjective suffix ('without, -less')"),
    "lIk": ("-lık", "abstract-noun / place-noun suffix ('-ness, -hood; place of')"),
    "cA": ("-ca", "adverbial suffix of manner and degree ('-ly, in the manner of')"),
    "mA": ("-ma", "verbal-noun suffix ('the act of …-ing')"),
    "Iş": ("-ış", "verbal-noun suffix ('the manner of …-ing')"),
}
# Türetilmiş sözcüğün İngilizce glossu için kural: ek anahtarı → (biçim, "{g}" = kök glossu)
DERIVED_GLOSS_EN = {
    "lI": "having {g}; with {g}", "sIz": "without {g}; {g}-less", "lIk": "{g}-ness; the state or place of {g}",
    "cA": "in the manner of {g}; {g}-ly", "mA": "the act of {g}", "Iş": "the manner of {g}; {g}",
}

# Veri kaynağı türleri
DATA_SOURCE_KINDS_EN = {"public_domain": "Public-domain historical works", "open_license": "Open-licensed data",
                        "linguistic_fact": "Linguistic facts", "generated": "EtimoTürk generated data"}
