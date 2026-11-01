# -*- coding: utf-8 -*-
"""Faz 4 meta verileri: yer adı köken dilleri, Türkiye bölgeleri, yer adı türleri, deyim alanları.

Telif notu: Buradaki tüm açıklama metinleri EtimoTürk şablonlarıyla özgün yazılmıştır; yalnızca
tarihsel/coğrafi olgular (antik kent adları, ses değişimleri) ve kamu malı kaynaklar (Strabon, Evliya Çelebi,
Dîvânu Lugâti't-Türk, Pîrî Reis) ile açık lisanslı yapısal veri (Wiktionary, CC BY-SA 4.0) kullanılır.
"""
from .languages import STAGE_NAMES

# Yer adı köken dilleri: kod -> (ad, renk, sıra, dönem notu)
TOPONYM_ORIGIN_LANGUAGES = {
    "hat": ("Hattice",                 "#6D4C41", 1,  "MÖ 3.–2. binyıl, Hitit öncesi Anadolu"),
    "hit": ("Hititçe",                 "#8D6E63", 2,  "MÖ 17.–12. yy, Hitit İmparatorluğu"),
    "xlu": ("Luvice",                  "#A1887F", 3,  "MÖ 2.–1. binyıl, Güney ve Batı Anadolu"),
    "xur": ("Urartuca",                "#5D4037", 4,  "MÖ 9.–6. yy, Van Gölü havzası"),
    "akk": ("Asurca / Akadca",         "#4E342E", 5,  "MÖ 2. binyıl, Asur ticaret kolonileri"),
    "phr": ("Frigce",                  "#795548", 6,  "MÖ 8.–4. yy, Orta Anadolu"),
    "lyd": ("Lidce",                   "#BCAAA4", 7,  "MÖ 7.–4. yy, Gediz havzası"),
    "xcr": ("Karca",                   "#9E9D24", 8,  "MÖ 1. binyıl, Güneybatı Anadolu"),
    "xlc": ("Likçe",                   "#827717", 9,  "MÖ 1. binyıl, Teke Yarımadası"),
    "thr": ("Trakça",                  "#558B2F", 10, "MÖ 1. binyıl, Trakya"),
    "pis": ("Pisidce",                 "#33691E", 10, "MÖ 1. binyıl, Göller Yöresi dağlık kentleri"),
    "el":  ("Yunanca",                 "#D68910", 11, "MÖ 8. yy – 20. yy, kıyı kolonileri ve Bizans"),
    "la":  ("Latince",                 "#B9770E", 12, "MÖ 1. yy – MS 7. yy, Roma eyaletleri"),
    "fa":  ("Farsça",                  "#8E44AD", 13, "Ahameniş satraplıkları ve Selçuklu dönemi"),
    "hy":  ("Ermenice",                "#A04000", 14, "Doğu Anadolu, Kilikya"),
    "syc": ("Süryanice / Aramice",     "#6C3483", 15, "Güneydoğu Anadolu, Tur Abdin"),
    "ar":  ("Arapça",                  "#C0392B", 16, "7. yy sonrası, Emevî-Abbasî sınır boyları"),
    "ka":  ("Gürcüce / Lazca",         "#4A235A", 17, "Doğu Karadeniz ve Çoruh havzası"),
    "ku":  ("Kürtçe",                  "#6E2C00", 18, "Doğu ve Güneydoğu Anadolu"),
    "it":  ("İtalyanca (Ceneviz / Venedik)", "#27AE60", 19, "13.–15. yy ticaret kolonileri"),
    "mn":  ("Moğolca",                 "#7D6608", 19, "13. yy İlhanlı dönemi ve Eski Türkçeye geçen sözcükler"),
    "tr":  ("Oğuz Türkçesi",           "#1E8E8E", 20, "1071 sonrası Selçuklu, Beylikler ve Osmanlı dönemi"),
    "unk": ("Bilinmeyen / tartışmalı", "#95A5A6", 99, "Kaynak dil kesin belirlenemiyor"),
}

TOPONYM_STAGE_NAMES = {
    **STAGE_NAMES,
    "hat": "Hattice", "hit": "Hititçe", "xlu": "Luvice", "xur": "Urartuca", "phr": "Frigce", "lyd": "Lidce",
    "xcr": "Karca", "xlc": "Likçe", "thr": "Trakça", "syc": "Süryanice", "byz": "Bizans Yunancası",
    "sel": "Selçuklu Türkçesi", "gen": "Cenevizce", "lzz": "Lazca", "ass": "Asurca", "pis": "Pisidce",
    "egy": "Eski Mısırca", "hur": "Hurrice", "cum": "Cumhuriyet Dönemi Türkçesi",
}

TOPONYM_KINDS = {
    "il": "İl", "ilçe": "İlçe", "semt": "Semt / Mahalle", "bölge": "Bölge", "antik_kent": "Antik Kent",
    "ada": "Ada", "boğaz": "Boğaz", "göl": "Göl", "dağ": "Dağ", "nehir": "Akarsu", "yarımada": "Yarımada",
    "körfez": "Körfez", "kale": "Kale", "köy": "Köy / Belde",
}

TURKISH_REGIONS = ["Marmara", "Ege", "Akdeniz", "İç Anadolu", "Karadeniz", "Doğu Anadolu", "Güneydoğu Anadolu"]

# Deyim alanları: kod -> (ad, SF Symbols simgesi, renk, açıklama)
IDIOM_DOMAINS = {
    "ahilik":    ("Ahilik ve Esnaf Geleneği",       "hammer",                  "#B9770E", "Ahi teşkilatı, lonca töreleri, çırak-kalfa-usta düzeni ve peştemal kuşanma"),
    "denizcilik": ("Osmanlı Denizciliği",            "sailboat",                "#1F618D", "Kadırga ve kalyon devri gemicilik dili, levent ve reisler, Pîrî Reis'in Kitâb-ı Bahriye'si"),
    "okculuk":   ("Okçuluk ve Avcılık",              "scope",                   "#1E8E8E", "Osmanlı kemankeşleri, Okmeydanı, menzil taşları, kuşçuluk ve av töreleri"),
    "tasavvuf":  ("Tasavvuf ve Tekke Kültürü",       "flame",                   "#8E44AD", "Mevlevî, Bektaşî ve diğer tarikatların dergâh dili, sema, çile ve erkân"),
    "tarim":     ("Tarım, Hayvancılık ve Göçebe Yaşamı", "leaf",               "#27AE60", "Harman, saban, yayla-kışlak döngüsü, koyun ve at kültürü"),
    "antik":     ("Antik Anadolu ve Akdeniz Gelenekleri", "building.columns",   "#D68910", "Antik Yunan, Roma ve Bizans döneminden kalan kalıp düşünceler ve törenler"),
    "askerlik":  ("Yeniçeri Ocağı ve Askerlik",      "shield",                  "#C0392B", "Kazan kaldırma, ocak töreleri, kılıç-kalkan, davul-zurna ve sefer dili"),
    "saray":     ("Saray, Divan ve Devlet",          "crown",                   "#C9A227", "Osmanlı sarayı, divan-ı hümâyun, teşrifat ve paşa-vezir ilişkileri"),
    "din":       ("Din, İbadet ve Halk İnanışları",  "moon.stars",              "#6C3483", "Kur'an ve hadis kaynaklı kalıplar, nazar, uğur ve halk inanışları"),
    "mutfak":    ("Mutfak ve Sofra",                 "fork.knife",              "#CA6F1E", "Osmanlı ve Anadolu mutfağı, sofra adabı, kahve ve çay kültürü"),
    "gundelik":  ("Hamam, Giyim ve Gündelik Yaşam",  "house",                   "#7D6608", "Hamam, kıyafet, ev düzeni, komşuluk ve misafirlik töreleri"),
    "ticaret":   ("Çarşı, Ticaret ve Para",          "banknote",                "#117A65", "Bedesten, kervan, akçe ve altın, pazarlık ve tartı dili"),
    "hukuk":     ("Hukuk, Kadılık ve Ceza",          "scale.3d",                "#2C5AA0", "Kadı mahkemeleri, şahitlik, kefalet, falaka ve ceza uygulamaları"),
    "beden":     ("Beden ve Halk Hekimliği",         "heart.text.square",       "#B03A2E", "Organlarla kurulan deyimler, hacamat, kırık-çıkık ve halk hekimliği"),
    "oyun":      ("Oyun, Eğlence ve Spor",           "gamecontroller",          "#0E6655", "Tavla, satranç, güreş, cirit, Karagöz-Hacivat ve meddah"),
    "hayvan":    ("Hayvanlar ve Doğa Gözlemi",       "pawprint",                "#5D6D7E", "Hayvan davranışlarından ve doğa olaylarından doğan benzetmeler"),
    "edebiyat":  ("Edebiyat, Masal ve Halk Hikâyeleri", "book",                 "#943126", "Nasreddin Hoca, Dede Korkut, masallar ve divan şiirinden kalan kalıplar"),
    "zanaat":    ("Zanaat ve Atölye",                "wrench.and.screwdriver",  "#616A6B", "Demirci, dokumacı, çömlekçi, kuyumcu ve hattat atölyelerinin dili"),
}

IDIOM_KINDS = ["deyim", "atasözü", "tabir", "kalıp söz"]
IDIOM_CONFIDENCE = {
    "kesin": "Belgelenmiş: köken anlatısı yazılı bir kaynağa (fıkra, destan, klasik metin, seyahatnâme) dayanır",
    "olası": "Olası: sözcük anlamları ve dönem bilgisiyle tutarlı; köken anlatısı yazılı kaynakla belgelenmemiştir",
    "halk_etimolojisi": "Halk arasında anlatılan, belgelenmemiş köken açıklaması (ihtiyatla aktarılır)",
}

# Köken anlatısının kendisini belgeleyen (yalnızca deyimin varlığını değil) kaynak türleri; bunlar dışındaki
# kaynaklar (sözlükler, "dilbilimsel olgu", "sözlü gelenek") deyimin kayıtlı olduğunu gösterir, köken hikâyesini değil.
IDIOM_NARRATIVE_SOURCES = (
    "Nasreddin Hoca", "Homeros", "Vergilius", "Arrianos", "Plutarkhos", "Statius", "Hesiodos", "Cicero", "Ovidius",
    "Tevrat", "İncil", "Suetonius", "Platon", "Kur'an", "Dede Korkut", "Köroğlu", "Dadaloğlu", "Evliya Çelebi",
    "Pîrî Reis", "Kâtip Çelebi", "Fütüvvetnâme", "Muhibbî", "Yunus Emre", "Muallim Naci", "Anadolu masalları",
)


def calibrated_confidence(confidence: str, source_note: str) -> str:
    """'kesin' yalnızca köken anlatısını belgeleyen bir kaynak varsa korunur; aksi hâlde 'olası'."""
    if confidence == "kesin" and not any(k in source_note for k in IDIOM_NARRATIVE_SOURCES):
        return "olası"
    return confidence
