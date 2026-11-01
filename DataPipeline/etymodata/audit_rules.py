# -*- coding: utf-8 -*-
"""İçerik denetimi kuralları (2026-11-01 denetimi).

Bu modül, korpus DSL'lerine dokunmadan `build_database.py` sırasında uygulanan düzeltmeleri toplar:

1. `resolve_direction` — ortak sözcük satırının geçiş yönünü, başlığın köken diline ve hedef dile göre yeniden
   hesaplar. DSL'de yön başlık başına tek verildiğinden "@israf into_turkish" bloğundaki Azerice satır da
   "into_turkish" oluyordu; oysa Azerice/Özbekçe/Kazakça satırları Türkçeyle ortak miras ya da koşut alıntıdır.
2. `EXCLUDED_COGNATES` — akraba sözcük değil yalnızca çeviri karşılığı olan satırlar (badem ↔ Gürcüce nuşi,
   kâğıt ↔ Moğolca tsaas). Elle incelenmiş; her satırın gerekçesi yanında. Biçimce benzeyen ama anlamca ilgisiz
   sesteşler (su ↔ Macarca só, çorba ↔ csorba) "yalancı arkadaş" notuyla kalır; onlar dışlanmaz.

Kurallar yalnızca yapısal olgulara dayanır; telifli sözlük metni içermez.
"""

# Türkçeyle ortak miras taşıyan Türk dilleri: bu dillerle hiçbir satır "into_turkish" olamaz
TURKIC_TARGETS = {"az", "uz", "kk", "ky", "tk"}
# Arapça/Farsça sözcükleri büyük ölçüde Osmanlı Türkçesi yoluyla alan diller
VIA_OTTOMAN_TARGETS = {"bg", "sr", "sq", "ro", "mk", "el", "hu"}
# Köken dili kodu → hedef dil kodu (aynı dil)
ORIGIN_TO_TARGET = {"ar": "ar", "fa": "fa", "fr": "fr", "it": "it", "el": "el", "en": "en", "de": "de", "es": "es",
                    "pt": "pt", "hy": "hy", "ka": "ka", "hu": "hu", "mn": "mn", "he": "he", "ro": "ro"}
SLAVIC_TARGETS = {"bg", "sr", "mk", "ru", "uk", "pl"}


def resolve_direction(origin: str, lang: str, block_direction: str) -> str:
    """Satır düzeyinde geçiş yönü.

    origin: başlık sözcüğünün köken dili kodu (words.origin_language_code), lang: hedef dil kodu,
    block_direction: DSL başlığındaki yön. Dönen değer: from_turkish / into_turkish / shared_ancestor.
    """
    if lang in TURKIC_TARGETS:
        return "shared_ancestor"
    same_language = ORIGIN_TO_TARGET.get(origin) == lang or (origin == "sl" and lang in SLAVIC_TARGETS)
    if same_language and origin != "tr":
        return "into_turkish"
    if block_direction == "into_turkish":
        if origin in ("ar", "fa") and lang in VIA_OTTOMAN_TARGETS:
            return "from_turkish"
        if origin == "tr":
            return "shared_ancestor"
        return "shared_ancestor"
    return block_direction or "shared_ancestor"


# (lemma, hedef dil, yabancı biçim) → gerekçe. Yabancı biçim küçük harfle karşılaştırılır.
EXCLUDED_COGNATES = {
    # --- Gürcüce: çeviri karşılığı, akraba değil
    ("badem", "ka", "ნუში"): "Gürcüce nuşi yerli sözcük; badem Farsça bādām",
    ("fasulye", "ka", "ლობიო"): "lobio ≠ fasulye (Yunanca phasḗolos)",
    ("fındık", "ka", "თხილი"): "tkhili yerli sözcük",
    ("kestane", "ka", "წაბლი"): "ts'abli yerli sözcük",
    ("kiraz", "ka", "ბალი"): "bali yerli sözcük",
    ("kitap", "ka", "წიგნი"): "ts'igni yerli sözcük",
    ("nar", "ka", "ბროწეული"): "brots'euli yerli sözcük",
    # --- İbranice
    ("cumartesi", "he", "שבת"): "cumartesi = cuma + ertesi; şabat ile akraba değil",
    ("deve", "he", "גמל"): "deve öz Türkçe; gamal Sami kökü",
    ("hahambaşı", "he", "רב"): "haham < ḥakham; rav ayrı sözcük",
    ("keten", "he", "כותנה"): "keten < Ar. kattān; kutna (pamuk) ayrı sözcük",
    # --- Moğolca
    ("ana", "mn", "ээж"): "eej ayrı sözcük",
    ("at", "mn", "адуу"): "aduu ile ilişkisi tartışmalı Altay varsayımı",
    ("gümüş", "mn", "мөнгө"): "möngö ≠ gümüş",
    ("kâğıt", "mn", "цаас"): "tsaas ayrı sözcük",
    ("kımız", "mn", "айраг"): "ayrag ayrı sözcük",
    ("yurt", "mn", "гэр"): "ger ayrı sözcük",
    # --- Macarca
    ("ay", "hu", "hó"): "Ural kökenli", ("ayna", "hu", "tükör"): "çeviri karşılığı",
    ("bal", "hu", "méz"): "Ural kökenli", ("balık", "hu", "hal"): "Ural kökenli",
    ("biber", "hu", "bors"): "çeviri karşılığı", ("göz", "hu", "szem"): "Ural kökenli",
    ("kılıç", "hu", "kard"): "kard İran kökenli", ("kiraz", "hu", "cseresznye"): "Slav kökenli",
    ("limon", "hu", "citrom"): "citrom < Lat. citrus", ("kravat", "hu", "nyakkendő"): "çeviri karşılığı",
    ("yağ", "hu", "vaj"): "Ural kökenli", ("ana", "hu", "anya"): "Ural kökenli",
    ("ata", "hu", "atya"): "Ural kökenli", ("ocak", "hu", "ocsak"): "Macarcada böyle sözcük saptanamadı",
    ("mehter", "hu", "mehter"): "Macarca söz varlığında yok", ("tımar", "hu", "tímár"): "tímár (derici) kökeni belirsiz",
    ("tercüman", "hu", "tolmács"): "tolmács Türkçe tılmaç; tercüman Aramice — ayrı kökler",
    ("tütün", "hu", "dohány"): "dohány < duhan; tütün ile akraba değil",
    ("tanrı", "hu", "tenger"): "tenger = deniz (Türkçe teŋiz); tanrı ile ilgisiz",
    # --- Arapça
    ("berber", "ar", "حلاق"): "çeviri karşılığı", ("biber", "ar", "فلفل"): "çeviri karşılığı",
    ("fes", "ar", "طربوش"): "çeviri karşılığı", ("fotoğraf", "ar", "صورة"): "çeviri karşılığı",
    ("kervan", "ar", "قافلة"): "çeviri karşılığı", ("pırasa", "ar", "كراث"): "çeviri karşılığı",
    ("telefon", "ar", "هاتف"): "çeviri karşılığı",
    # --- Farsça
    ("biber", "fa", "فلفل"): "çeviri karşılığı", ("ekmek", "fa", "نان"): "çeviri karşılığı",
    ("fotoğraf", "fa", "عکس"): "çeviri karşılığı", ("jips", "fa", "گچ"): "çeviri karşılığı",
    ("kestane", "fa", "شاه‌بلوط"): "çeviri karşılığı", ("kimyon", "fa", "زیره"): "çeviri karşılığı",
    ("patates", "fa", "سیب‌زمینی"): "çeviri karşılığı",
    # --- Urduca
    ("darphane", "ur", "ٹکسال"): "çeviri karşılığı", ("ekmek", "ur", "نان"): "çeviri karşılığı",
    ("kına", "ur", "مہندی"): "çeviri karşılığı", ("patates", "ur", "آلو"): "çeviri karşılığı",
    ("tüfek", "ur", "توپ"): "top ≠ tüfek", ("çakal", "ur", "گیدڑ"): "çeviri karşılığı",
    # --- Yunanca
    ("badem", "el", "αμύγδαλο"): "çeviri karşılığı", ("banka", "el", "τράπεζα"): "çeviri karşılığı",
    ("depresyon", "el", "κατάθλιψη"): "çeviri karşılığı", ("dönüm", "el", "στρέμμα"): "çeviri karşılığı",
    ("haydi", "el", "άντε"): "ánte ayrı ünlem", ("nane", "el", "δυόσμος"): "çeviri karşılığı",
    ("nohut", "el", "ρεβίθι"): "çeviri karşılığı", ("otobüs", "el", "λεωφορείο"): "çeviri karşılığı",
    ("tavus", "el", "παγώνι"): "çeviri karşılığı",
    # --- İngilizce
    ("alize", "en", "trade wind"): "çeviri karşılığı", ("firuze", "en", "turquoise"): "turquoise 'Türk taşı'; firuze Farsça",
    ("fıçı", "en", "butt"): "akrabalık kurulamıyor", ("kilit", "en", "key"): "key Cermen kökenli",
    ("lokum", "en", "turkish delight"): "çeviri karşılığı", ("muskat", "en", "nutmeg"): "çeviri karşılığı",
    ("muz", "en", "banana"): "çeviri karşılığı", ("peri", "en", "fairy"): "fairy < Lat. fata",
    # --- Fransızca / İtalyanca / İspanyolca / Almanca / Lehçe / Portekizce
    ("firuze", "fr", "turquoise"): "turquoise 'Türk taşı'; firuze Farsça", ("kalbur", "fr", "crible"): "çeviri karşılığı",
    ("fıçı", "it", "botte"): "akrabalık kurulamıyor", ("kalbur", "it", "crivello"): "çeviri karşılığı",
    ("çek", "it", "assegno"): "çeviri karşılığı",
    ("fasulye", "es", "frijol"): "çeviri karşılığı", ("kaju", "es", "anacardo"): "çeviri karşılığı",
    ("tungsten", "es", "wolframio"): "çeviri karşılığı",
    ("mika", "de", "glimmer"): "çeviri karşılığı", ("sabun", "de", "seife"): "Cermen kökenli; uzak",
    ("tercüman", "de", "dolmetscher"): "Dolmetscher < tılmaç; tercüman Aramice", ("tungsten", "de", "wolfram"): "çeviri karşılığı",
    ("tungsten", "pl", "wolfram"): "çeviri karşılığı",
    # --- Ermenice
    ("badem", "hy", "նուշ"): "çeviri karşılığı", ("ejderha", "hy", "վիշապ"): "çeviri karşılığı",
    ("fasulye", "hy", "լոբի"): "çeviri karşılığı", ("incir", "hy", "թուզ"): "çeviri karşılığı",
    ("kahve", "hy", "սուրճ"): "çeviri karşılığı", ("portakal", "hy", "նարինջ"): "portakal 'Portekiz'; narinj nārang",
    ("telefon", "hy", "հեռախոս"): "çeviri karşılığı", ("tren", "hy", "գնացք"): "çeviri karşılığı",
    # --- Balkan dilleri
    ("davul", "mk", "тапан"): "çeviri karşılığı", ("fasulye", "mk", "грав"): "çeviri karşılığı",
    ("akçe", "ro", "aspru"): "aspru < Yun. áspron; ayrı sözcük", ("cep", "ro", "gebea"): "Rumencede saptanamadı",
    ("cezve", "ro", "ibric"): "ibric < ibrik; cezve ile ilgisiz", ("kilit", "ro", "cheie"): "Lat. clavis",
    ("pamuk", "ro", "bumbac"): "Lat. bombax", ("saat", "ro", "ceas"): "Slav kökenli", ("top", "ro", "tun"): "Lat. tonus",
    ("kürek", "sq", "lopatë"): "Slav kökenli", ("zeytin", "sq", "ulli"): "Lat. oliva",
    ("zeytinyağı", "sq", "vaj ulliri"): "çeviri karşılığı", ("ütü", "sq", "hekur"): "hekur = demir",
    ("bacanak", "sr", "pašenog"): "çeviri karşılığı", ("defne", "sr", "ловор"): "Lat. laurus",
    # --- Rusça
    ("amatör", "ru", "любитель"): "çeviri karşılığı", ("havyar", "ru", "икра"): "çeviri karşılığı",
    ("kravat", "ru", "галстук"): "Alm. Halstuch", ("sabun", "ru", "мыло"): "çeviri karşılığı",
    ("tungsten", "ru", "вольфрам"): "çeviri karşılığı", ("turkuaz", "ru", "бирюза"): "biryuza < Far. pīrūza; turkuaz 'Türk taşı'",
    # --- Azerice
    ("altın", "az", "qızıl"): "çeviri karşılığı", ("bakır", "az", "mis"): "çeviri karşılığı",
    ("başak", "az", "sünbül"): "çeviri karşılığı", ("düğün", "az", "toy"): "çeviri karşılığı",
    ("fasulye", "az", "lobya"): "çeviri karşılığı", ("güz", "az", "payız"): "çeviri karşılığı",
    ("karnabahar", "az", "gül kələm"): "çeviri karşılığı", ("kayısı", "az", "ərik"): "çeviri karşılığı",
    ("kepçe", "az", "çömçə"): "çeviri karşılığı", ("kestane", "az", "şabalıd"): "çeviri karşılığı",
    ("kimyon", "az", "cirə"): "çeviri karşılığı", ("kravat", "az", "qalstuk"): "çeviri karşılığı",
    ("kuyumculuk", "az", "zərgərlik"): "çeviri karşılığı", ("marul", "az", "kahı"): "çeviri karşılığı",
    ("muz", "az", "banan"): "çeviri karşılığı", ("pabuç", "az", "başmaq"): "çeviri karşılığı",
    ("papağan", "az", "tutuquşu"): "çeviri karşılığı", ("pirinç", "az", "düyü"): "çeviri karşılığı",
    ("pırasa", "az", "kəvər"): "çeviri karşılığı", ("susam", "az", "küncüt"): "çeviri karşılığı",
    ("sülük", "az", "zəli"): "çeviri karşılığı", ("tere", "az", "vəzəri"): "çeviri karşılığı",
    ("toynak", "az", "dırnaq"): "dırnaq = tırnak; toynak ayrı",
    ("yoğurt", "az", "qatıq"): "çeviri karşılığı", ("şımarık", "az", "ərköyün"): "çeviri karşılığı",
    # --- Kazakça
    ("anahtar", "kk", "кілт"): "çeviri karşılığı", ("bakır", "kk", "мыс"): "çeviri karşılığı",
    ("böğürmek", "kk", "мөңіреу"): "akrabalık kurulamıyor", ("büyü", "kk", "бақсы"): "çeviri karşılığı",
    ("ceviz", "kk", "жаңғақ"): "çeviri karşılığı", ("civciv", "kk", "балапан"): "çeviri karşılığı",
    ("düğün", "kk", "той"): "çeviri karşılığı", ("ekmek", "kk", "нан"): "çeviri karşılığı",
    ("fincan", "kk", "пиялa"): "çeviri karşılığı", ("halı", "kk", "кілем"): "çeviri karşılığı",
    ("inek", "kk", "сиыр"): "çeviri karşılığı", ("insan", "kk", "адам"): "çeviri karşılığı",
    ("kayısı", "kk", "өрік"): "çeviri karşılığı", ("köpek", "kk", "ит"): "çeviri karşılığı",
    ("melemek", "kk", "маңырау"): "akrabalık kurulamıyor", ("mercimek", "kk", "жасымық"): "çeviri karşılığı",
    ("pamuk", "kk", "мақта"): "çeviri karşılığı", ("sanat", "kk", "өнер"): "çeviri karşılığı",
    ("sanayi", "kk", "өнеркәсіп"): "çeviri karşılığı", ("serçe", "kk", "торғай"): "çeviri karşılığı",
    ("soğan", "kk", "пияз"): "çeviri karşılığı", ("susam", "kk", "күнжіт"): "çeviri karşılığı",
    ("söğüt", "kk", "тал"): "çeviri karşılığı", ("tereyağı", "kk", "сары май"): "çeviri karşılığı",
    ("tüfek", "kk", "мылтық"): "çeviri karşılığı", ("tütün", "kk", "темекі"): "çeviri karşılığı",
    ("yasa", "kk", "заң"): "çeviri karşılığı", ("yoğurt", "kk", "қатық"): "çeviri karşılığı",
    ("yüzgeç", "kk", "қанат"): "çeviri karşılığı", ("çekirdek", "kk", "дән"): "çeviri karşılığı",
    ("çilek", "kk", "құлпынай"): "çeviri karşılığı", ("çorap", "kk", "шұлық"): "çeviri karşılığı",
    # --- Kırgızca
    ("abdest", "ky", "даарат"): "daarat < Ar. ṭahārat; abdest Farsça", ("anahtar", "ky", "ачкыч"): "çeviri karşılığı",
    ("bakır", "ky", "жез"): "çeviri karşılığı", ("ceviz", "ky", "жаңгак"): "çeviri karşılığı",
    ("düğün", "ky", "той"): "çeviri karşılığı", ("ekmek", "ky", "нан"): "çeviri karşılığı",
    ("inek", "ky", "уй"): "çeviri karşılığı", ("peynir", "ky", "быштак"): "çeviri karşılığı",
    ("soğan", "ky", "пияз"): "çeviri karşılığı", ("yüzük", "ky", "шакек"): "çeviri karşılığı",
    # --- Türkmence
    ("boynuz", "tk", "şah"): "çeviri karşılığı", ("buzağı", "tk", "göle"): "çeviri karşılığı",
    ("ceviz", "tk", "hoz"): "çeviri karşılığı", ("civciv", "tk", "jüýje"): "çeviri karşılığı",
    ("delikanlı", "tk", "ýigit"): "çeviri karşılığı", ("düğün", "tk", "toý"): "çeviri karşılığı",
    ("gülümsemek", "tk", "ýylgyrmak"): "çeviri karşılığı", ("inek", "tk", "sygyr"): "çeviri karşılığı",
    ("kaşık", "tk", "çemçe"): "çeviri karşılığı", ("kene", "tk", "sakyrtga"): "çeviri karşılığı",
    ("kimlik", "tk", "şahsyýetnama"): "çeviri karşılığı", ("pirinç", "tk", "tüwi"): "çeviri karşılığı",
    ("çilek", "tk", "ýer tudanasy"): "çeviri karşılığı",
    # --- "farklı sözcük kullanılır" notuyla eklenmiş, akraba olmayan satırlar
    ("boza", "ro", "bragă"): "Slav kökenli ayrı sözcük",
    ("tren", "az", "qatar"): "qatar < Ar. qiṭār; ayrı sözcük", ("peynir", "kk", "пенир?"): "kayıt belirsiz (soru işaretli)", ("torna", "ru", "токарный"): "akraba değil",
    ("ada", "kk", "арал"): "çeviri karşılığı", ("gizlice", "uz", "yashirincha"): "farklı kök", ("erinmek", "tk", "ýaltanmak"): "farklı kök",
    # --- Özbekçe
    ("ada", "uz", "orol"): "çeviri karşılığı", ("akrep", "uz", "chayon"): "çeviri karşılığı",
    ("anahtar", "uz", "kalit"): "çeviri karşılığı", ("armut", "uz", "nok"): "çeviri karşılığı",
    ("ayva", "uz", "behi"): "çeviri karşılığı", ("bakır", "uz", "mis"): "çeviri karşılığı",
    ("barut", "uz", "porox"): "porox Rusça; barut Yunanca", ("biber", "uz", "murch"): "çeviri karşılığı",
    ("ceviz", "uz", "yong'oq"): "çeviri karşılığı", ("cıva", "uz", "simob"): "çeviri karşılığı",
    ("düğün", "uz", "toʻy"): "çeviri karşılığı", ("ekmek", "uz", "non"): "çeviri karşılığı",
    ("inek", "uz", "sigir"): "çeviri karşılığı", ("kayısı", "uz", "o'rik"): "çeviri karşılığı",
    ("kiraz", "uz", "gilos"): "çeviri karşılığı", ("peynir", "uz", "pishloq"): "çeviri karşılığı",
    ("serçe", "uz", "chumchuq"): "çeviri karşılığı", ("soğan", "uz", "piyoz"): "çeviri karşılığı",
    ("söğüt", "uz", "tol"): "çeviri karşılığı", ("çilek", "uz", "qulupnay"): "çeviri karşılığı",
    ("ütü", "uz", "dazmol"): "çeviri karşılığı",
}


def is_excluded(lemma: str, lang: str, foreign: str) -> bool:
    return (lemma, lang, foreign.strip().lower()) in _EXCLUDED_KEYS


_EXCLUDED_KEYS = {(l, g, f.lower()) for (l, g, f) in EXCLUDED_COGNATES}
