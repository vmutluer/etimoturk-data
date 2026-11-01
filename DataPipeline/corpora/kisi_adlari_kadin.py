# -*- coding: utf-8 -*-
"""Korpus 33 — Kişi Adları Köken Sözlüğü (A): kadın adları ve ortak (unisex) adlar.

DSL (parsing.parse_names), satır başına bir ad:
  Ad | cins | köken | parçalar | anlam | anlam_en | aile | ilgili sözcük | not | not_en
  cins: k (kadın), e (erkek), u (her ikisi)      köken: başlıca köken dili kodu
  parçalar: biçim:dil:anlam:anlam_en [+ biçim:dil:anlam:anlam_en …]   (bileşik adlarda her öğe ayrı)
  aile: kök ailesi kodu (sözlükteki aileyle bağ; boş olabilir)   ilgili: aynı kökten sözlük maddesi (boş olabilir)
  not / not_en: isteğe bağlı ek olgu (adaş, kaynak metin, ses değişimi)

Köken hikâyeleri `etymodata/names.py` şablonlarıyla parçalardan özgün olarak üretilir; telifli ad sözlüğü metni kullanılmaz.
Köken dili tartışmalı ya da belgelenemeyen adlar (Aylin, Selin, Sibel, Yeliz…) bilerek alınmamıştır.
"""

NAMES = r"""
# ── Öz Türkçe kadın adları ───────────────────────────────────────────────────────────
Ayla|k|tr|ay:tr:ay:moon + -la:tr:ad eki (ay ağılı, hale):noun suffix (halo)|ayın çevresindeki ışık halkası, hale|the halo of light around the moon|*ay|ay||
Aysel|k|tr|ay:tr:ay:moon + sel:tr:taşkın su:flood|ay ışığı seli, ay gibi gür|a flood of moonlight|*ay|ay||
Aysun|k|tr|ay:tr:ay:moon + sun-:tr:sunmak, uzatmak:to offer|ay gibi (güzellik) sunan|offering (beauty) like the moon|*ay|ay||
Ayça|k|tr|ay:tr:ay:moon + -ça:tr:küçültme eki:diminutive suffix|küçük ay, hilal|little moon, crescent|*ay|ay||
Aynur|k|tr|ay:tr:ay:moon + nūr:ar:ışık:light|ay ışığı|moonlight|*ay|nur||
Aygül|k|tr|ay:tr:ay:moon + gul:fa:gül:rose|ay gibi parlak gül|a rose as bright as the moon|*ay|gül||
Ayten|k|tr|ay:tr:ay:moon + tan:fa:beden:body|ay tenli, ay gibi parlak bedenli|moon-skinned, as bright as the moon|*ay|ay||
Aybike|k|tr|ay:tr:ay:moon + bike:tr:hanım, prenses (Eski Türkçe):lady, princess (Old Turkic)|ay hanım|moon lady|*ay|ay|Bike/büke, Dede Korkut anlatılarında hanım unvanıdır.|Bike/büke is a title for noble ladies in the Book of Dede Korkut.
Gökçe|k|tr|gök:tr:gök; mavi:sky; blue + -çe:tr:benzerlik eki:suffix of likeness|gök mavisi, gökçe güzel|sky-blue; fair, beautiful|*kök|gök||
Gökçen|k|tr|gök:tr:gök; mavi:sky; blue + -çen:tr:ad eki:noun suffix|gök renkli, mavi|sky-coloured, blue|*kök|gök||
Sevgi|k|tr|sev-:tr:sevmek:to love + -gi:tr:ad eki:noun suffix|sevgi, sevme duygusu|love, affection|*sev-|sevgi||
Sevim|k|tr|sev-:tr:sevmek:to love + -im:tr:ad eki:noun suffix|sevimlilik, sevilen|lovableness, the loved one|*sev-|sevimli||
Sevil|k|tr|sevil-:tr:sevilmek:to be loved|sevilen, sevil (dilek)|beloved; "be loved" (a wish)|*sev-|sevmek||
Sevinç|k|tr|sevin-:tr:sevinmek:to rejoice + -ç:tr:ad eki:noun suffix|sevinç, mutluluk|joy, delight|*sev-|sevinç||
Özlem|k|tr|özle-:tr:özlemek:to long for + -m:tr:ad eki:noun suffix|özleyiş, hasret|longing, yearning|*özle-|özlemek||
Özge|k|tr|öz:tr:öz, kendi:self + -ge:tr:başka, farklı anlamı veren ek:suffix "other"|başka, farklı; eşsiz|other, different; unique|*öz|öz||
Özden|u|tr|öz:tr:öz, cevher:essence + -den:tr:ayrılma eki:ablative suffix|özden gelen, soylu|from the essence; noble|*öz|öz||
Ece|k|tr|eçe:tr:kraliçe, ana, büyük kız kardeş (Eski Türkçe):queen, mother, elder sister (Old Turkic)|kraliçe, hanım|queen, lady||||
Damla|k|tr|damla:tr:damla, su damlası:drop of water|damla, su damlası|a drop of water|*tam-|damlamak||
Duygu|k|tr|duy-:tr:duymak, hissetmek:to feel + -gu:tr:ad eki:noun suffix|his, duygu|feeling, emotion||duygu||
Dilek|k|tr|dile-:tr:dilemek:to wish + -k:tr:ad eki:noun suffix|dilek, istek|wish, desire||dilek||
Esin|k|tr|es-:tr:esmek:to blow + -in:tr:ad eki:noun suffix|esinti; ilham|breeze; inspiration|*es-|esinti||
Esen|u|tr|esen:tr:sağ, sağlıklı, esenlikte:healthy, safe|esen, sağlıklı|hale, in good health||||
Ezgi|k|tr|ezgi:tr:ezgi, makam:melody, tune|ezgi, nağme|melody, tune||ezgi||
Gizem|k|tr|giz:tr:sır (Dil Devrimi türetmesi):secret (Language Reform coinage) + -em:tr:ad eki:noun suffix|sır, giz|mystery, secret||||
İlknur|k|tr|ilk:tr:ilk, birinci:first + nūr:ar:ışık:light|ilk ışık, tan ışığı|first light, dawn light|*ilk|nur||
İpek|k|tr|yipek:tr:ipek (Eski Türkçe):silk (Old Turkic)|ipek|silk||ipek||
Irmak|k|tr|ırmak:tr:akarsu, nehir:river|ırmak, nehir|river||ırmak||
Kader|k|ar|qadar:ar:ölçü; alın yazısı:measure; fate|alın yazısı, yazgı|destiny, fate|K-D-R|kader||
Nuray|k|tr|nūr:ar:ışık:light + ay:tr:ay:moon|ışıklı ay, ay ışığı|luminous moon, moonlight|*ay|nur||
Nurten|k|tr|nūr:ar:ışık:light + tan:fa:beden:body|ışık tenli, bedeni ışıklı|light-skinned, with a luminous body|N-W-R|nur||
Pınar|k|tr|bıŋar:tr:kaynak, çeşme (Eski Türkçe):spring (Old Turkic)|kaynak, su gözü|spring, fountainhead||pınar||
Serpil|k|tr|serpil-:tr:serpilmek, gelişip büyümek:to flourish, to grow up|serpilen, gelişip güzelleşen|flourishing, growing up gracefully|*ser-|||
Su|k|tr|sub:tr:su (Eski Türkçe):water (Old Turkic)|su|water|*sub|su||
Tuğçe|k|tr|tuğ:tr:at kuyruğundan sancak:horsetail standard + -çe:tr:küçültme eki:diminutive suffix|küçük tuğ, tuğ gibi|little standard, like a tuğ|*tuğ|tuğ||
Tülay|k|tr|tulle:fr:tül:tulle + ay:tr:ay:moon|tül gibi ince ay|a moon as fine as tulle|*ay|tül||
Yıldız|k|tr|yultuz:tr:yıldız (Eski Türkçe):star (Old Turkic)|yıldız|star|*yultuz|yıldız||
Yaprak|k|tr|yaprak:tr:yaprak:leaf|yaprak|leaf|*yaprak|yaprak||
Yağmur|u|tr|yağmur:tr:yağmur:rain|yağmur|rain|*yağ-|yağmur||
Çiğdem|k|tr|çiğdem:tr:ilkbaharda açan soğanlı çiçek:crocus|çiğdem çiçeği|crocus flower||çiğdem||
Çiçek|k|tr|çeçek:tr:çiçek (Eski Türkçe):flower (Old Turkic)|çiçek|flower|*çiçek|çiçek||
Bilge|u|tr|bilge:tr:bilgili, hakîm (Eski Türkçe):wise (Old Turkic)|bilge, bilgili|wise, sage|*bil-|bilge|Orhun Yazıtları'nda Bilge Kağan'ın unvanıdır.|The title of Bilge Kağan in the Orkhon inscriptions.
Sezen|u|tr|sez-:tr:sezmek:to sense + -en:tr:ortaç eki:participle suffix|sezen, sezgili|one who senses, intuitive|*sez-|sezmek||
Oya|k|tr|oya:tr:iğneyle işlenen dantel:needle lace|oya işi, incelikle işlenmiş süs|needle lace, a delicately worked ornament||oya||
Tansu|k|tr|tan:tr:şafak:dawn + su:tr:su:water|tan vaktinin suyu, şafak|dawn water, daybreak|*sub|tan||
Songül|k|tr|son:tr:son:last + gul:fa:gül:rose|son gül, en son açan gül|the last rose|*son|gül||
Birgül|k|tr|bir:tr:bir, tek:one + gul:fa:gül:rose|tek gül, biricik gül|the one rose, the only rose|*bir|gül||
Şengül|k|tr|şen:fa:neşeli:cheerful + gul:fa:gül:rose|neşeli gül|cheerful rose||gül||
Ülkü|k|tr|ülkü:tr:ideal, mefkûre (Dil Devrimi türetmesi):ideal (Language Reform coinage)|ülkü, ideal|ideal, aspiration||||
Türkan|k|tr|türk:tr:Türk:Turk + -ān:fa:çoğul eki:plural suffix|Türkler; Türk hanımı|the Turks; Turkish lady||||
İlke|k|tr|ilk:tr:ilk, birinci:first + -e:tr:ad eki:noun suffix|ilke, prensip|principle|*ilk|ilke||
Suna|k|tr|suna:tr:yaban ördeği, boylu boslu:wild duck; tall and graceful|boylu boslu, güzel|tall and graceful, beautiful||||
Deniz|u|tr|teŋiz:tr:deniz (Eski Türkçe):sea (Old Turkic)|deniz|sea|*teŋiz|deniz||
Evren|u|tr|evir-:tr:evirmek, döndürmek:to turn + -en:tr:ad eki:noun suffix|kâinat, dönen gök|universe, the turning sky|*evir-|evren||
Umut|u|tr|um-:tr:ummak, beklemek:to hope + -ut:tr:ad eki:noun suffix|umut, ümit|hope|*um-|umut||

# ── Farsça kökenli kadın adları ──────────────────────────────────────────────────────
Nilgün|k|fa|nīl:fa:çivit:indigo + gūn:fa:renk:colour|çivit renkli, koyu mavi|indigo-coloured, deep blue||||
Nilüfer|k|fa|nīlūfar:fa:su zambağı (Sanskritçe nīlotpala "mavi lotus"):water lily (Sanskrit nīlotpala "blue lotus")|nilüfer çiçeği|water lily||nilüfer||
Derya|k|fa|daryā:fa:deniz:sea|deniz|sea||derya||
Dilara|k|fa|dil:fa:gönül:heart + ārā:fa:süsleyen:adorning|gönül süsleyen, sevgili|heart-adorning, beloved|dil|dilber||
Ebru|k|fa|abrī:fa:bulut gibi (abr "bulut"):cloud-like (abr "cloud")|bulut desenli; kâğıt süsleme sanatı|cloud-patterned; the marbling art||ebru||
Gamze|k|fa|ġamza:fa:göz süzme, çene çukuru:side glance, dimple|göz süzüşü; gamze|a coquettish glance; dimple||||
Gonca|k|fa|ġonca:fa:tomurcuk:bud|gül tomurcuğu|rosebud||gonca||
Gül|k|fa|gul:fa:gül:rose|gül|rose||gül||
Gülşen|k|fa|gul:fa:gül:rose + şan:fa:yer eki, bahçe:place suffix, garden|gül bahçesi|rose garden||gül||
Gülizar|k|fa|gul:fa:gül:rose + ʿiẕār:ar:yanak:cheek|gül yanaklı|rose-cheeked||gül||
Gülten|k|fa|gul:fa:gül:rose + tan:fa:beden:body|gül tenli|rose-skinned||gül||
Gülçin|k|fa|gul:fa:gül:rose + çīn:fa:toplayan (çīdan):gatherer (from çīdan)|gül toplayan|rose-gatherer||gül||
Gülbahar|k|fa|gul:fa:gül:rose + bahār:fa:ilkbahar:spring|gül mevsimi, ilkbahar gülü|rose season, spring rose||bahar||
Hande|k|fa|ḫanda:fa:gülüş:laughter|gülüş, tebessüm|laughter, smile||||
Jale|k|fa|žāla:fa:çiy, kırağı:dew|çiy damlası|dewdrop||||
Lale|k|fa|lāla:fa:lale:tulip|lale çiçeği|tulip||lale|Lâle sözcüğü Osmanlı tezhibinde ve 18. yüzyıl "Lâle Devri" adında da yaşar.|The word also survives in Ottoman illumination and in the name of the 18th-century "Tulip Era".
Mine|k|fa|mīnā:fa:cam, sırça; mavi sır:glass; blue enamel|sırça, mine işi|enamel, glass-like ornament||mine||
Nazlı|k|fa|nāz:fa:naz, işve:coquetry + -lı:tr:sahiplik eki:possessive suffix|nazlı, işveli|coquettish, delicate|nāz|naz||
Nazan|k|fa|nāzān:fa:nazlanan:coy, coquettish|nazlanan, nazlı|coy, coquettish|nāz|naz||
Naz|k|fa|nāz:fa:naz, işve:coquetry|naz, işve|coquetry, grace|nāz|naz||
Nesrin|k|fa|nasrīn:fa:yaban gülü:wild rose|yaban gülü|wild rose||||
Nihal|k|fa|nihāl:fa:fidan, taze filiz:sapling, young shoot|fidan, ince uzun boylu|sapling; slender||||
Nergis|k|fa|nargis:fa:nergis (Eski Yunanca nárkissos):narcissus (Ancient Greek nárkissos)|nergis çiçeği|narcissus flower|Narkissos|nergis||
Nevin|k|fa|navīn:fa:yeni:new|yeni|new||||
Pakize|k|fa|pākīza:fa:tertemiz:pure, clean|tertemiz, saf|pure, spotless||pak||
Perihan|k|fa|parī:fa:peri:fairy + ḫān:tr:han, hükümdar:ruler|perilerin hükümdarı|ruler of the fairies||peri||
Şebnem|k|fa|şab:fa:gece:night + nam:fa:nem:moisture|gece nemi, çiy|night dew||||
Şirin|k|fa|şīrīn:fa:tatlı:sweet|tatlı, sevimli|sweet, lovely||şirin|Ferhat ile Şirin hikâyesinin kadın kahramanıdır.|The heroine of the romance of Ferhat and Şirin.
Yasemin|k|fa|yāsamīn:fa:yasemin:jasmine|yasemin çiçeği|jasmine||yasemin||
Zerrin|k|fa|zarrīn:fa:altından, altın renkli:golden|altın renkli, sarı|golden, golden-yellow||||
Buse|k|fa|būsa:fa:öpücük:kiss|öpücük|kiss||||
Begüm|k|fa|begam:fa:hanım, prenses (Türkçe beg "bey"in dişil biçimi):lady, princess (feminine of Turkic beg "lord")|hanımefendi, prenses|lady, princess||bey||
Berna|k|fa|barnā:fa:genç, delikanlı:young|genç|young||||
Canan|k|fa|cānān:fa:sevgili (cān "can"dan):beloved (from cān "soul")|sevgili, gönül verilen|beloved|cān|can||
Cansu|k|fa|cān:fa:can:soul + su:tr:su:water|can suyu, hayat veren su|life-giving water|cān|can||
Didem|k|fa|dīdam:fa:gözüm (dīda "göz"):my eye (dīda "eye")|gözüm, gözbebeğim|my eye, apple of my eye||||
Figen|k|fa|figan:fa:atan, saçan (gul-figan "gül saçan"):scattering (gul-figan "rose-scattering")|gül saçan|rose-scattering||||
Kezban|k|fa|kad:fa:ev:house + bānū:fa:hanım:lady|ev hanımı, evin hanımı|lady of the house||||
Nalan|k|fa|nālān:fa:inleyen, ağlayan:lamenting|inleyen, yanık sesli|lamenting, plaintive||||
Kumru|k|fa|qumrī:fa:kumru kuşu:turtledove|kumru|turtledove||kumru||
Zişan|k|ar|zī:ar:sahip:owner of + şān:ar:şan:glory|şanlı, şan sahibi|glorious||şan||
Şule|k|ar|şuʿla:ar:alev, ışık:flame|alev, ışık|flame, light||||
Peri|k|fa|parī:fa:peri:fairy|peri|fairy||peri||
Bahar|k|fa|bahār:fa:ilkbahar:spring|ilkbahar|spring||bahar||
Günay|k|tr|gün:tr:güneş, gün:sun, day + ay:tr:ay:moon|güneş ve ay|sun and moon|*kün|gün||

# ── Arapça kökenli kadın adları ──────────────────────────────────────────────────────
Elif|k|ar|alif:ar:Arap alfabesinin ilk harfi:the first letter of the Arabic alphabet|elif harfi; ince uzun boylu|the letter alif; slender||||
Esra|k|ar|isrāʾ:ar:gece yürüyüşü:night journey|gece yolculuğu|night journey|||Kur'an'da Hz. Muhammed'in gece yolculuğunu anlatan sûrenin adıdır.|The name of the Quranic chapter on the Prophet's night journey.
Hale|k|ar|hāla:ar:ayın çevresindeki ışık halkası:halo around the moon|hale, ay ağılı|halo||||
Hatice|k|ar|Ḫadīca:ar:erken doğan:born early|erken doğan|born early|||Hz. Muhammed'in ilk eşi Hatice bint Hüveylid'in adıdır.|The name of Khadija bint Khuwaylid, first wife of the Prophet Muhammad.
Hülya|k|ar|ḥulyā:ar:tatlı düş, hayal:sweet dream, reverie|tatlı hayal, düş|sweet dream||||
Kübra|k|ar|kubrā:ar:en büyük (kabīr'in dişil üstünlüğü):the greatest (feminine superlative of kabīr)|en büyük, ulu|the greatest|K-B-R|kibir||
Leyla|k|ar|laylā:ar:gece; kara saçlı:night; dark-haired|gece|night|||Leyla ile Mecnun hikâyesinin kadın kahramanıdır.|The heroine of the romance of Leyla and Majnun.
Melek|k|ar|malak:ar:melek:angel|melek|angel|M-L-K|melek||
Melis|k|el|mélissa:el:bal arısı:honeybee|bal arısı|honeybee||||
Merve|k|ar|Marwa:ar:Mekke'de Kâbe yakınındaki tepe:a hill near the Kaaba in Mecca|Merve tepesi|the hill of Marwa||||
Meryem|k|he|Miryam:he:Meryem (İbranice):Mary (Hebrew)|Hz. Meryem'in adı|the name of the Virgin Mary|||Arapça Maryam biçimiyle Türkçeye girmiştir.|Entered Turkish through the Arabic form Maryam.
Neslihan|k|ar|nasl:ar:soy:lineage + ḫān:tr:han, hükümdar:ruler|han soyundan|of the ruler's lineage|N-S-L|nesil||
Nur|k|ar|nūr:ar:ışık:light|ışık|light|N-W-R|nur||
Rabia|k|ar|rābiʿa:ar:dördüncü:fourth|dördüncü|fourth|R-B-A||Basralı sufi Rabia el-Adeviyye ile yaygınlaşmıştır.|Popularized through the Basran Sufi Rabia al-Adawiyya.
Reyhan|u|ar|rayḥān:ar:fesleğen:basil|fesleğen, güzel kokulu bitki|basil, fragrant herb|R-W-H|reyhan||
Seda|k|ar|ṣadā:ar:yankı, ses:echo, voice|yankı, ses|echo, voice||||
Selma|k|ar|salmā:ar:esen, sağlıklı; barış içinde:safe, sound; peaceful|esen, barış içinde|safe, at peace|S-L-M|selam||
Semra|k|ar|samrāʾ:ar:esmer:dark-complexioned|esmer|dark-complexioned||||
Serap|k|ar|sarāb:ar:serap, ılgım:mirage|serap|mirage||||
Sultan|k|ar|sulṭān:ar:hükümdar:ruler|hükümdar, sultan|sovereign, sultan|S-L-T|sultan|Osmanlı'da hanedanın kadın üyeleri için de unvandı: Mihrimah Sultan.|Also a title for female members of the Ottoman dynasty: Mihrimah Sultan.
Tuba|k|ar|ṭūbā:ar:cennet ağacı; ne mutlu:the tree of paradise; blessedness|cennet ağacı|the tree of paradise||||
Zehra|k|ar|zahrāʾ:ar:parlak, çiçek gibi:radiant, flower-like|parlak yüzlü|radiant|Z-H-R||Hz. Fatıma'nın "Fatımatü'z-Zehra" lakabından yaygınlaşmıştır.|Popularized through Fatima's epithet "Fatima al-Zahra".
Zeynep|k|ar|zaynab:ar:güzel kokulu bir ağaç; süs:a fragrant tree; adornment|güzel kokulu ağaç; süs|fragrant tree; adornment|||Hz. Muhammed'in kızı Zeynep'in adıdır.|The name of Zaynab, a daughter of the Prophet Muhammad.
Zuhal|k|ar|zuḥal:ar:Satürn gezegeni:the planet Saturn|Satürn|Saturn||||
Zümrüt|k|ar|zumurrud:ar:zümrüt (Eski Yunanca smáragdos):emerald (Ancient Greek smáragdos)|zümrüt taşı|emerald||zümrüt||
Betül|k|ar|batūl:ar:bakire, erdemli kadın:virgin, chaste woman|iffetli, erdemli|chaste, virtuous|||Hz. Meryem'in ve Hz. Fatıma'nın sıfatıdır.|An epithet of the Virgin Mary and of Fatima.
Beyza|k|ar|bayḍāʾ:ar:beyaz, lekesiz:white, spotless|beyaz, lekesiz|white, spotless||beyaz||
Büşra|k|ar|buşrā:ar:müjde:good news|müjde, sevindirici haber|good tidings||||
Ceyda|k|ar|jaydāʾ:ar:uzun boyunlu, güzel:long-necked, graceful|uzun boyunlu, endamlı|long-necked, graceful||||
Emel|k|ar|amal:ar:umut, arzu:hope, aspiration|umut, arzu|hope, aspiration|A-M-L|||
Emine|k|ar|amīna:ar:güvenilir, emin:trustworthy|güvenilir|trustworthy|A-M-N|emin|Hz. Muhammed'in annesi Âmine'nin adıyla aynı köktendir.|Shares its root with Āmina, the name of the Prophet's mother.
Esma|k|ar|asmāʾ:ar:adlar (ism "ad"ın çoğulu):names (plural of ism "name")|adlar; güzel adlar|names|S-M-W|isim||
Fatma|k|ar|Fāṭima:ar:sütten kesen:she who weans|sütten kesen|she who weans|||Hz. Muhammed'in kızı Fatıma'nın adının Türkçe biçimidir.|The Turkish form of the name of Fatima, the Prophet's daughter.
Feride|k|ar|farīda:ar:eşsiz, tek:unique|eşsiz, tek|unique, peerless|F-R-D|fert||
Gaye|k|ar|ġāya:ar:amaç, son nokta:aim, goal|amaç|aim, purpose|Ğ-Y-Y|gaye||
Hacer|k|ar|Hājar:ar:Hacer (Hz. İsmail'in annesi):Hagar (mother of Ishmael)|Hz. Hacer'in adı|the name of Hagar||||
Halime|k|ar|ḥalīma:ar:yumuşak huylu, sabırlı:gentle, forbearing|yumuşak huylu|gentle|H-L-M|||
Havva|k|he|Ḥawwā:he:yaşayan (İbranice):living (Hebrew)|yaşayan, hayat veren|living, life-giving|||Arapça Ḥawwāʾ biçimiyle Türkçeye girmiştir.|Entered Turkish through the Arabic form Ḥawwāʾ.
Hilal|u|ar|hilāl:ar:yeni ay:crescent moon|hilal, yeni ay|crescent moon||hilal||
Hümeyra|k|ar|ḥumayrāʾ:ar:küçük kırmızı, al yanaklı:little red one, rosy-cheeked|al yanaklı|rosy-cheeked|H-M-R|||
İclal|k|ar|ijlāl:ar:ululama, saygı gösterme:honouring, reverence|ululuk, saygınlık|majesty, dignity||||
İrem|k|ar|Iram:ar:Kur'an'da anılan efsanevi bağ:a legendary garden mentioned in the Quran|İrem bağı, cennet gibi bahçe|the garden of Iram||||
Kadriye|k|ar|qadr:ar:değer, kıymet:worth + -iyya:ar:nispet eki:relational suffix|değerli, kıymetli|precious|K-D-R|kadir||
Kiraz|k|el|kerásion:el:kiraz:cherry|kiraz|cherry||kiraz||
Latife|k|ar|laṭīfa:ar:ince, zarif; nükte:delicate; witticism|zarif, ince|delicate, graceful|L-T-F|latif||
Leman|k|ar|lamaʿān:ar:parıltı:gleam, glitter|parıltı, ışıltı|gleam, shimmer||||
Makbule|k|ar|maqbūla:ar:kabul edilmiş, beğenilen:accepted, pleasing|beğenilen, makbul|accepted, pleasing|K-B-L|kabul||
Melike|k|ar|malika:ar:kraliçe:queen|kraliçe|queen|M-L-K|mülk||
Melahat|k|ar|malāḥa:ar:güzellik, yüz güzelliği:beauty, comeliness|güzellik|beauty||||
Mualla|k|ar|muʿallā:ar:yüceltilmiş, yüksek:exalted|yüce, yüksek|exalted|A-L-W|âli||
Müge|k|fr|muguet:fr:inci çiçeği:lily of the valley|inci çiçeği|lily of the valley||||
Nil|k|ar|Nīl:ar:Nil nehri (Eski Yunanca Neîlos):the river Nile (Ancient Greek Neîlos)|Nil nehri|the Nile||||
Nimet|k|ar|niʿma:ar:iyilik, bağış, bolluk:blessing, bounty|nimet, bolluk|blessing, bounty|N-A-M|nimet||
Nisa|k|ar|nisāʾ:ar:kadınlar:women|kadınlar|women|||Kur'an'ın dördüncü sûresinin adıdır.|The name of the fourth chapter of the Quran.
Rana|k|ar|raʿnāʾ:ar:güzel, göz alıcı:beautiful, eye-catching|göz alıcı güzel|strikingly beautiful||||
Rüya|k|ar|ruʾyā:ar:görme; düş:seeing; dream|düş|dream|R-ʾ-Y|rüya||
Saadet|k|ar|saʿāda:ar:mutluluk:happiness|mutluluk|happiness, felicity|S-A-D|saadet||
Sabiha|k|ar|ṣabīḥa:ar:güzel yüzlü (ṣubḥ "sabah"dan):fair-faced (from ṣubḥ "morning")|güzel yüzlü|fair-faced|S-B-H|sabah||
Safiye|k|ar|ṣafiyya:ar:arı, saf; seçkin:pure; chosen|arı, saf|pure|S-F-W|safi||
Sanem|k|ar|ṣanam:ar:put, heykel; sevgili:idol; beloved|put kadar güzel sevgili|a beloved as fair as an idol||||
Sedef|k|ar|ṣadaf:ar:sedef, inci kabuğu:mother-of-pearl|sedef|mother-of-pearl|S-D-F|sedef||
Sema|k|ar|samāʾ:ar:gök:sky|gök, gökyüzü|sky, heaven|S-M-W|sema||
Semiha|k|ar|samīḥa:ar:cömert:generous|cömert|generous||||
Şerife|k|ar|şarīfa:ar:soylu, şerefli:noble|soylu, şerefli|noble|Ş-R-F|şeref||
Şeyma|k|ar|şaymāʾ:ar:benli, vücudunda ben olan:having a beauty mark|benli|with a beauty mark||||
Vildan|k|ar|wildān:ar:çocuklar, gençler (walad'ın çoğulu):children, youths (plural of walad)|çocuklar, cennet gençleri|children, youths of paradise|W-L-D|velet||
Zeliha|k|ar|Zulayḫā:ar:Züleyha (Hz. Yusuf kıssasının kadın kahramanı):Zulaykha (the woman in the story of Joseph)|Züleyha|Zulaykha|||Yusuf ile Züleyha mesnevilerinin kadın kahramanıdır.|The heroine of the Yusuf and Zulaykha romances.
Elvan|k|ar|alwān:ar:renkler (lawn "renk"in çoğulu):colours (plural of lawn "colour")|renkler, rengârenk|colours, colourful||||
Nehir|k|ar|nahr:ar:ırmak:river|ırmak|river||nehir||
Rukiye|k|ar|Ruqayya:ar:yükselen (raqiya):ascending|yükselen|ascending|||Hz. Muhammed'in kızı Rukiye'nin adıdır.|The name of Ruqayya, a daughter of the Prophet Muhammad.
Ayşe|k|ar|ʿĀʾişa:ar:yaşayan, hayat dolu (ʿāşa "yaşamak"):living, full of life (from ʿāşa "to live")|yaşayan, hayat dolu|living, full of life|A-Y-Ş|maişet|Hz. Muhammed'in eşi Ayşe bint Ebu Bekir'in adıdır.|The name of Aisha bint Abi Bakr, wife of the Prophet Muhammad.
Ayşegül|k|ar|ʿĀʾişa:ar:yaşayan:living + gul:fa:gül:rose|Ayşe ile gül|Ayşe and rose|A-Y-Ş|gül||
Hayriye|k|ar|ḫayr:ar:iyilik:goodness + -iyya:ar:nispet eki:relational suffix|hayırlı, iyilik sahibi|good, beneficent|Ḫ-Y-R|hayır||
Nazife|k|ar|naẓīfa:ar:temiz:clean|temiz, pak|clean, pure||||
Nermin|k|fa|narmīn:fa:yumuşak, nazik (narm "yumuşak"):soft, gentle (narm "soft")|yumuşak huylu|soft, gentle||||
Nükhet|k|ar|nukhat:ar:güzel koku:fragrance|güzel koku|fragrance||||
Perran|k|fa|parrān:fa:uçan:flying|uçan, uçucu|flying||||
Şükran|k|ar|şukrān:ar:teşekkür, şükretme:gratitude|şükran, minnet|gratitude|Ş-K-R|şükür||
Sevda|k|ar|sawdāʾ:ar:kara; kara safra (aşk hastalığı):black; black bile (love-sickness)|kara sevda, tutkulu aşk|passionate love||sevda||
Gülsüm|k|ar|kulṯūm:ar:dolgun yüzlü:full-faced|dolgun yüzlü|full-faced|||Hz. Muhammed'in kızı Ümmü Gülsüm'ün adından.|From the name of Umm Kulthum, a daughter of the Prophet Muhammad.
Ümmühan|k|ar|umm:ar:anne:mother + ḫān:tr:han:ruler|hanın annesi|mother of the ruler|A-M-M|ümmet||
Afet|k|ar|āfa:ar:felaket; (mecaz) öldürücü güzellik:calamity; (fig.) a devastating beauty|çok güzel kadın|a devastating beauty||afet||
Nilay|k|fa|nīl:fa:çivit:indigo + ay:tr:ay:moon|mavi ay|blue moon|*ay|||
"""
