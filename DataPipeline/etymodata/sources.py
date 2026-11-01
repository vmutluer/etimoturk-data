# -*- coding: utf-8 -*-
"""Veri kaynakları ve lisans künyeleri (`data_sources` tablosu, uygulamadaki Kaynakça ekranı).

Kurallar:
  • Telifli ticari sözlüklerden (Nişanyan Sözlük, Kubbealtı Lugati, TDK açıklama metinleri vb.)
    hiçbir metin kopyalanmaz, kazınmaz; bu tabloda da yer almazlar.
  • Dilbilimsel olgular (kaynak dil, kök harfleri, ses değişimleri) telife tabi değildir.
  • Kamu malı tarihî eserler ve açık lisanslı yapısal veri (Wiktionary / Kaikki.org, CC BY-SA 4.0)
    kullanılır; künye metinleri şablonlarla özgün olarak üretilir.
"""

# kind: public_domain | open_license | linguistic_fact | generated
DATA_SOURCES = [
    {
        "id": 1, "kind": "open_license", "name": "Wiktionary (Türkçe maddeler) – Kaikki.org dökümü",
        "author": "Wiktionary katkıcıları; makine okunur döküm: Tatu Ylonen / Kaikki.org",
        "year": "2026", "license": "CC BY-SA 4.0",
        "url": "https://kaikki.org/dictionary/Turkish/",
        "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
        "usage": "Yapısal etimoloji olguları (kaynak dil, kaynak biçim, özgün alfabe yazılışı, soy ağacı) ve İngilizce anlamlar. "
                 "Açıklama cümleleri kopyalanmaz; künye metinleri EtimoTürk şablonlarıyla yeniden üretilir. Kayıtlar "
                 "filtrelenmiş, yeniden yapılandırılmış ve düzeltilmiştir; bu kayıtlardan türetilen veriler aynı lisansla "
                 "(CC BY-SA 4.0) paylaşılır. EtimoTürk'ün Wikimedia Foundation ya da Kaikki.org ile resmî bağlantısı yoktur.",
        "fields": "words.data_source = 'wiktionary'; words.original_script (kaynak yazım); shared_cognates (soy kaydı)",
        "usage_en": "Structural etymology facts (source language, source form, original-script spelling, descendant tree) and English glosses. Explanatory sentences are not copied; entry texts are regenerated with EtimoTürk templates. The records were filtered, restructured and corrected; data derived from them is shared under the same license (CC BY-SA 4.0). EtimoTürk is not endorsed by or affiliated with the Wikimedia Foundation or Kaikki.org.",
    },
    {
        "id": 2, "kind": "public_domain", "name": "Orhun (Köktürk) Yazıtları",
        "author": "Bilge Kağan, Köl Tigin, Tonyukuk anıtları", "year": "8. yüzyıl (716–735)",
        "license": "Kamu malı", "url": "https://tr.wikipedia.org/wiki/Orhun_Yaz%C4%B1tlar%C4%B1", "license_url": "",
        "usage": "Eski Türkçe söz varlığının en eski yazılı tanıklığı; Göktürk damgalı yazımlar ve 8. yy tarihlendirmesi.",
        "fields": "words.historical_attestation = 'Orhun Yazıtları'; words.original_script (Göktürk)",
        "usage_en": "The oldest written witness of the Old Turkic lexicon; Old Turkic runiform spellings and 8th-century dating.",
    },
    {
        "id": 3, "kind": "public_domain", "name": "Dîvânu Lugâti't-Türk",
        "author": "Kâşgarlı Mahmud", "year": "1072–1074", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/D%C3%AEv%C3%A2nu_Lug%C3%A2ti%27t-T%C3%BCrk", "license_url": "",
        "usage": "Karahanlı dönemi Türkçe sözcüklerin ilk sözlük kaydı; sözcük biçimleri ve 11. yy tarihlendirmesi.",
        "fields": "words.historical_attestation = 'Dîvânu Lugâti\\'t-Türk'",
        "usage_en": "The first dictionary record of Karakhanid-period Turkish words; word forms and 11th-century dating.",
    },
    {
        "id": 4, "kind": "public_domain", "name": "Kutadgu Bilig",
        "author": "Yusuf Has Hacib", "year": "1069–1070", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Kutadgu_Bilig", "license_url": "",
        "usage": "Karahanlı Türkçesi edebî söz varlığı; soyut kavram ve devlet terimlerinin erken tanıklığı.",
        "fields": "words.historical_attestation = 'Kutadgu Bilig'",
        "usage_en": "The literary vocabulary of Karakhanid Turkic; early attestation of abstract and state terminology.",
    },
    {
        "id": 5, "kind": "public_domain", "name": "Eski Uygurca Metinler (Budist ve Maniheist çeviriler)",
        "author": "Anonim", "year": "9.–10. yüzyıl", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Eski_Uygurca", "license_url": "",
        "usage": "Soğdca ve Sanskritçe alıntıların Eski Türkçeye giriş tanıklığı.",
        "fields": "words.historical_attestation = 'Eski Uygurca Metinler'",
        "usage_en": "Attestation of Sogdian and Sanskrit loans entering Old Turkic.",
    },
    {
        "id": 6, "kind": "public_domain", "name": "Codex Cumanicus",
        "author": "Anonim (Ceneviz ve Fransisken derleyiciler)", "year": "1303", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Codex_Cumanicus", "license_url": "",
        "usage": "Kıpçak Türkçesi söz varlığı; Latin ve Fars dilleriyle karşılaştırmalı sözlükçe.",
        "fields": "words.historical_attestation = 'Codex Cumanicus'",
        "usage_en": "The Kipchak Turkic lexicon; a comparative glossary with Latin and Persian.",
    },
    {
        "id": 7, "kind": "public_domain", "name": "Dede Korkut Kitabı ve Eski Anadolu Türkçesi metinleri",
        "author": "Anonim; Yunus Emre Divanı", "year": "13.–15. yüzyıl", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Dede_Korkut_Kitab%C4%B1", "license_url": "",
        "usage": "Oğuz Türkçesi döneminde Arapça ve Farsça alıntıların yerleşme tanıklığı.",
        "fields": "words.historical_attestation = 'Dede Korkut Kitabı' / 'Yunus Emre Divanı'",
        "usage_en": "Attestation of Arabic and Persian loans settling in the Oghuz Turkish period.",
    },
    {
        "id": 8, "kind": "public_domain", "name": "Thesaurus Linguarum Orientalium",
        "author": "Franciscus à Mesgnien Meninski", "year": "1680", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Franciszek_Meninski", "license_url": "",
        "usage": "17. yy Osmanlı Türkçesi söz varlığının Latin harfli ilk kapsamlı kaydı.",
        "fields": "words.historical_attestation = 'Meninski'",
        "usage_en": "The first comprehensive Latin-script record of the 17th-century Ottoman Turkish lexicon.",
    },
    {
        "id": 9, "kind": "public_domain", "name": "Lehce-i Osmânî",
        "author": "Ahmed Vefik Paşa", "year": "1876", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Lehce-i_Osm%C3%A2n%C3%AE", "license_url": "",
        "usage": "19. yy Osmanlı Türkçesi sözlüğü; Türkçe kökenli sözcükleri ayrı işaretleyen ilk eser.",
        "fields": "words.historical_attestation = 'Lehce-i Osmânî'",
        "usage_en": "A 19th-century Ottoman Turkish dictionary; the first to mark words of Turkish origin separately.",
    },
    {
        "id": 10, "kind": "public_domain", "name": "A Turkish and English Lexicon",
        "author": "Sir James W. Redhouse", "year": "1890", "license": "Kamu malı",
        "url": "https://archive.org/details/ATurkishAndEnglishLexicon", "license_url": "",
        "usage": "Geç Osmanlı Türkçesi söz varlığının Arap harfli yazımları ve köken dili işaretleri.",
        "fields": "words.historical_attestation = 'Redhouse'",
        "usage_en": "Arabic-script spellings and source-language markers of the late Ottoman Turkish lexicon.",
    },
    {
        "id": 11, "kind": "public_domain", "name": "Kamus-ı Türkî",
        "author": "Şemseddin Sami", "year": "1901", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Kamus-%C4%B1_T%C3%BCrk%C3%AE", "license_url": "",
        "usage": "Osmanlı Türkçesinin köken bilgisi veren ilk büyük Türkçe sözlüğü; Arap harfli yazımlar.",
        "fields": "words.historical_attestation = 'Kamus-ı Türkî'",
        "usage_en": "The first major Turkish dictionary of Ottoman Turkish to give origin information; Arabic-script spellings.",
    },
    {
        "id": 14, "kind": "public_domain", "name": "Geographika",
        "author": "Strabon (Amaseialı)", "year": "MÖ 7 – MS 23", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Geographika", "license_url": "",
        "usage": "Anadolu kentlerinin antik adları, kurucu söylenceleri ve Roma dönemi yeniden adlandırmaları (Faz 4 yer adları).",
        "fields": "toponyms.name_evolution_json, toponyms.story, toponyms.source_note",
        "usage_en": "Ancient names of Anatolian cities, founding legends and Roman-period renamings (Phase 4 place names).",
    },
    {
        "id": 15, "kind": "public_domain", "name": "Seyahatnâme",
        "author": "Evliya Çelebi", "year": "1640–1685", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Seyahatn%C3%A2me", "license_url": "",
        "usage": "17. yy Osmanlı kent ve kasaba adlarının halk arasında anlatılan köken hikâyeleri; deyimlerin dönem tanıklığı.",
        "fields": "toponyms.story, toponyms.era; idiom_origins.source_note",
        "usage_en": "Folk accounts of the origins of 17th-century Ottoman town names; period attestation of idioms.",
    },
    {
        "id": 16, "kind": "public_domain", "name": "Kitâb-ı Bahriye",
        "author": "Pîrî Reis", "year": "1521", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Kit%C3%A2b-%C4%B1_Bahriye", "license_url": "",
        "usage": "Akdeniz ve Ege kıyılarındaki liman, ada ve burun adlarının 16. yy Osmanlı denizcilik biçimleri; denizcilik deyimlerinin kaynağı.",
        "fields": "toponyms (kıyı yer adları); idiom_origins.domain_code = 'denizcilik'",
        "usage_en": "16th-century Ottoman nautical forms of harbor, island and cape names on the Mediterranean and Aegean coasts; source of seafaring idioms.",
    },
    {
        "id": 17, "kind": "public_domain", "name": "Cihânnümâ",
        "author": "Kâtip Çelebi", "year": "1648–1657", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Cih%C3%A2nn%C3%BCm%C3%A2", "license_url": "",
        "usage": "Osmanlı coğrafya geleneğinde Anadolu sancak ve kaza adlarının 17. yy yazımları.",
        "fields": "toponyms.story, toponyms.source_note",
        "usage_en": "17th-century spellings of Anatolian sanjak and kaza names in the Ottoman geographical tradition.",
    },
    {
        "id": 18, "kind": "public_domain", "name": "Anabasis",
        "author": "Ksenophon", "year": "MÖ 4. yüzyıl", "license": "Kamu malı",
        "url": "https://tr.wikipedia.org/wiki/Anabasis_(Ksenophon)", "license_url": "",
        "usage": "Onbinlerin Anadolu'yu geçişinde kaydedilen kent ve ırmak adları (Trabzon, Kerasus, Sinop, Fırat, Dicle).",
        "fields": "toponyms.name_evolution_json (antik biçimler)",
        "usage_en": "City and river names recorded during the march of the Ten Thousand through Anatolia (Trabzon, Kerasus, Sinope, Euphrates, Tigris).",
    },
    {
        "id": 19, "kind": "open_license", "name": "Wikipedia / Wiktionary – yer adı ve deyim maddeleri (yapısal olgular)",
        "author": "Wikipedia ve Wiktionary katkıcıları", "year": "2026", "license": "CC BY-SA 4.0",
        "url": "https://tr.wikipedia.org/", "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
        "usage": "Yalnızca yapısal olgular: antik ad listeleri, plaka kodları, koordinatlar, deyimlerin yaygın biçimi. "
                 "Açıklama metinleri kopyalanmaz; hikâyeler EtimoTürk şablonlarıyla özgün yazılır.",
        "fields": "toponyms.plate_code, toponyms.latitude/longitude, toponyms.name_evolution_json; idiom_origins.phrase",
        "usage_en": "Structural facts only: lists of ancient names, license-plate codes, coordinates, the common form of idioms. Explanatory texts are not copied; the stories are written originally with EtimoTürk templates.",
    },
    {
        "id": 12, "kind": "linguistic_fact", "name": "Dilbilimsel olgular ve ses kanunları",
        "author": "Türkoloji ve karşılaştırmalı dilbilim literatürü (genel bilgi)", "year": "—",
        "license": "Telife tabi değil (olgu)", "url": "", "license_url": "",
        "usage": "Kaynak dil, kök harfleri, ünlü uyumu, k->g / t->d / b->v gibi ses değişimleri, Arapça vezin "
                 "kalıpları ve Hint-Avrupa kök eşleştirmeleri bilimsel olgudur; EtimoTürk bunları kendi şablonlarıyla anlatır.",
        "fields": "words.etymology_summary, words.phonetic_evolution_json, words.arabic_pattern, root_families; toponyms.summary; idiom_origins.origin_story",
        "usage_en": "Source language, root letters, vowel harmony, sound changes such as k>g / t>d / b>v, Arabic root patterns and Indo-European root correspondences are scientific facts; EtimoTürk narrates them in its own templates.",
    },
    {
        "id": 13, "kind": "generated", "name": "EtimoTürk kural tabanlı üretimler",
        "author": "EtimoTürk DataPipeline", "year": "2026", "license": "Projeyle birlikte dağıtılır",
        "url": "", "license_url": "",
        "usage": "Göktürk damgalı yazım (ünlü uyumuna göre damga seçimi), Arap harflerine dönüştürme, IPA okunuş, "
                 "yapım ekli türevler ve bütün künye metinleri algoritmik olarak üretilir.",
        "fields": "words.original_script (Göktürk / algoritmik Arap yazımı), words.ipa, words.data_source = 'derived'",
        "usage_en": "Old Turkic runiform spelling (sign choice by vowel harmony), Arabic-script conversion, IPA transcription, suffix-derived forms and all entry texts, including the English summaries, are generated algorithmically.",
    },
]

# Uygulamada bir cümlelik zorunlu atıf
WIKTIONARY_ATTRIBUTION = ("Wiktionary katkıcıları, Kaikki.org dökümü (CC BY-SA 4.0) – yalnızca yapısal etimoloji olguları; "
                          "türetilen veriler aynı lisansla paylaşılır")
