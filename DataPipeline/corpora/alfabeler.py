# -*- coding: utf-8 -*-
"""Korpus 13 — Özgün alfabe yazılışları (elle denetlenmiş).

SCRIPTS: kaynak biçimin bilimsel çevriyazısı -> özgün alfabedeki yazılışı.
Yunanca, Ermenice, Çince, Japonca, Moğolca, Soğdca ve Slav dilleri için ters çevriyazı belirsiz
olduğundan (ι/η/υ, ο/ω vb.) bu biçimler tek tek yazılmıştır. Bunlar dilbilimsel olgudur (sözcüğün
kendi dilindeki yazımı); hiçbir sözlük metni kopyalanmamıştır.

SCRIPT_NAMES: belirli bir kaynak biçimin yazı sistemi adı (Unicode tanımı yetersiz kaldığında).
"""

SCRIPTS = {
    # --- Yunanca (Rumca) ---------------------------------------------------------------
    "Aigaîon": "Αἰγαῖον", "Anatolḕ": "Ἀνατολή", "Asía": "Ἀσία", "Eurṑpē": "Εὐρώπη", "Smýrnē": "Σμύρνη",
    "Ánkyra": "Ἄγκυρα", "afthéntis": "αφέντης", "anoichtíri": "ανοιχτήρι", "avlí": "αυλή", "chapsí": "χαψί",
    "dalián": "νταλιάνι", "diphthéra-dār": "διφθέρα", "domátes": "ντομάτες", "eikóna": "εικόνα",
    "eis tḕn pólin": "εἰς τὴν Πόλιν", "ekklisía": "εκκλησία", "epískopos": "ἐπίσκοπος", "fanári": "φανάρι",
    "fasóli": "φασόλι", "foúrnos": "φούρνος", "fytáni": "φυτάνι", "garída": "γαρίδα", "ipódromos": "ιππόδρομος",
    "kaísi": "καΐσι", "kellári": "κελλάρι", "keramídi": "κεραμίδι", "kerási": "κεράσι", "kleidí": "κλειδί",
    "kommérkion": "κομμέρκιον", "kothórnoi": "κόθορνοι", "koukoúmi": "κουκούμι", "koumási": "κουμάσι",
    "koutí": "κουτί", "kástano": "κάστανο", "kólpos": "κόλπος", "kýminon": "κύμινον", "lavráki": "λαβράκι",
    "limáni": "λιμάνι", "láchano": "λάχανο", "lámpa": "λάμπα", "makedonísi": "μακεδονήσι", "manitári": "μανιτάρι",
    "maroúli": "μαρούλι", "monastíri": "μοναστήρι", "mármaro": "μάρμαρο", "mýdi": "μύδι", "oktapódi": "οκταπόδι",
    "oýa": "ούγια", "palamída": "παλαμίδα", "panḕgyris": "πανήγυρις", "papás": "παπάς", "patriárchis": "πατριάρχης",
    "patátes": "πατάτες", "pipéri": "πιπέρι", "prásso": "πράσο", "psōmí": "ψωμί", "píta": "πίτα", "schára": "σχάρα",
    "sfoungári": "σφουγγάρι", "skamní": "σκαμνί", "skoumbrí": "σκουμπρί", "stavrídi": "σταυρίδι",
    "themélio": "θεμέλιο", "tsókara": "τσόκαρα", "týpa": "τύπα",
    # Korpus 8–12 Yunanca biçimleri
    "kátergon": "κάτεργον", "sēmadoúra": "σημαδούρα", "vólta": "βόλτα", "boréas": "βορέας", "nótos": "νότος",
    "embátēs": "ἐμβάτης", "kéfalos": "κέφαλος", "loúfaros": "λούφαρος", "tsipoúra": "τσιπούρα", "barboúni": "μπαρμπούνι",
    "orkýnos": "ὄρκυνος", "toríki": "τορίκι", "astakós": "αστακός", "soupiá": "σουπιά", "mezítis": "μεζίτης",
    "pastíli": "παστίλι", "salamoúra": "σαλαμούρα", "vasilikón": "βασιλικόν", "ankinára": "αγκινάρα",
    "yialí": "γιαλί", "toúvlo": "τούβλο", "drepánē": "δρεπάνη", "kannábouri": "καννάβουρι", "meltémi": "μελτέμι",
    # Eski Yunanca zincir biçimleri
    "anatomḕ": "ἀνατομή", "átomos": "ἄτομος", "physiología": "φυσιολογία", "sympátheia": "συμπάθεια",
    "anaisthēsía": "ἀναισθησία", "aisthētikós": "αἰσθητικός", "bíos": "βίος", "baktḕrion": "βακτήριον",
    "klinikḕ": "κλινική", "syndromḕ": "συνδρομή", "enérgeia": "ἐνέργεια", "ásthma": "ἄσθμα", "diabḕtēs": "διαβήτης",
    "prôtos": "πρῶτος", "hormôn": "ὁρμῶν", "émbryon": "ἔμβρυον", "psykhḕ": "ψυχή", "orthódoxos": "ὀρθόδοξος",
    "optikós": "ὀπτικός", "ópion": "ὄπιον", "iṑdēs": "ἰώδης", "hygieinḕ": "ὑγιεινή", "díaita": "δίαιτα",
    "kanṑn": "κανών", "hypothḕkē": "ὑποθήκη", "díplōma": "δίπλωμα", "prōtókollon": "πρωτόκολλον",
    "arkheîon": "ἀρχεῖον", "rheûma": "ῥεῦμα", "phṑkē": "φώκη", "ōkeanós": "ὠκεανός", "pistákion": "πιστάκιον",
    "mouseîon": "μουσεῖον", "théatron": "θέατρον", "theōría": "θεωρία", "kínēma": "κίνημα", "stádion": "στάδιον",
    "klíma": "κλίμα", "geōgraphía": "γεωγραφία", "geōmetría": "γεωμετρία", "astronomía": "ἀστρονομία",
    "krýstallos": "κρύσταλλος", "oikonomía": "οἰκονομία", "botanikḕ": "βοτανική", "kōmōidía": "κωμῳδία",
    "tragōidía": "τραγῳδία", "drâma": "δρᾶμα", "kritikós": "κριτικός", "krísis": "κρίσις", "théma": "θέμα",
    "kharaktḕr": "χαρακτήρ", "týpos": "τύπος", "grammatikḕ": "γραμματική", "philosophía": "φιλοσοφία",
    "tà metà tà physiká": "τὰ μετὰ τὰ φυσικά", "ēthikós": "ἠθικός", "idéa": "ἰδέα", "eídōlon": "εἴδωλον",
    "empeirikós": "ἐμπειρικός", "amanítēs": "ἀμανίτης",
    # --- Ermenice ------------------------------------------------------------------------
    "hadig": "հատիկ", "havanag": "ավանակ", "madımak": "մատուտակ", "mor": "մոր", "panjar": "բանջար",
    "pozavag": "պոռնկավագ", "t'el": "թել", "thoṛn": "թոռն", "xačʿ": "խաչ", "ōrinak": "օրինակ",
    # --- Slav dilleri (Kiril) -------------------------------------------------------------
    "izba": "изба", "kapusta": "капуста", "kločka": "клочка", "kopča": "копча", "kosa": "коса", "kočan": "кочан",
    "kožuh": "кожух", "kralj": "краљ", "kraljica": "краљица", "kukurec": "кукурец", "mazut": "мазут",
    "pateka": "патека", "plug": "плуг", "samovar": "самовар", "višnja": "вишња", "vodka": "водка",
    "vojevoda": "војвода", "četa": "чета", "šapka": "шапка", "kefir": "кефир",
    # --- Çince / Japonca ---------------------------------------------------------------------
    "chá": "茶", "mántou": "饅頭", "zhēnzhū": "珍珠", "dàfēng": "大風", "kê-tsiap": "鮭汁",
    "kimono": "着物", "tōfu": "豆腐",
    # --- Moğolca (Klasik Moğol yazısı için font desteği sınırlı olduğundan Kiril) ------------
    "jebe": "зэв", "jegeren": "зээр", "maral": "марал", "nökür": "нөхөр", "qabirγa": "хавирга",
    "quriltai": "хуралдай", "serigün": "сэрүүн", "ulus": "улс", "yasaq": "засаг", "čaγ": "цаг",
    # --- Nahuatl / Tupi (Latin) ve diğer -----------------------------------------------------
    "xocolātl": "xocolātl", "cacahuatl": "cacahuatl", "nanas": "nanas",
}

# Kaynak biçimin yazı sistemi adı (SCRIPTS değeri olmadan da verilebilir)
SCRIPT_NAMES = {
    "knδ": "Soğd (Latin çevriyazı)", "pwrc": "Soğd (Latin çevriyazı)", "tmw": "Soğd (Latin çevriyazı)",
    "uştmax": "Soğd (Latin çevriyazı)", "xwatēn": "Soğd (Latin çevriyazı)",
    "xocolātl": "Latin (Nahuatl)", "cacahuatl": "Latin (Nahuatl)", "nanas": "Latin (Tupi)",
}
