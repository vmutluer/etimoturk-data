# -*- coding: utf-8 -*-
"""Korpus 8 — Denizcilik: gemi ve donanım (İtalyanca/Venedikçe), balık ve kıyı adları (Rumca), rüzgârlar,
Öz Türkçe deniz söz varlığı."""

WORDS = r"""
# --- Gemi ve donanım: İtalyanca / Venedikçe --------------------------------------------
iskele|n|it|scala|merdiven; yanaşma yeri|EAT|scala|la:scala>ven:scala>tr:iskele
skala|n|it|scala|ölçek|MOD|scala|
eskalasyon|n|fr|escalation|tırmanma|MOD|scala|
kaptan|n|it|capitano|baş, önder|EAT|caput|la:caput>it:capitano>tr:kaptan
kamara|n|it|camera|oda|OSM|camera|la:camera>it:camera>tr:kamara
kamarot|n|it|camerotto|kamara görevlisi|OSM19|camera|
kamera|n|fr|caméra|karanlık oda|CUM|camera|la:camera>fr:caméra>tr:kamera
güverte|n|it|coverta|örtü|OSM|cooperire|la:cooperta>it:coverta>tr:güverte
kuvertür|n|fr|couverture|örtü|MOD|cooperire|
dümen|n|it|timone|dümen|OSM||la:temo>it:timone>tr:dümen
serdümen|n|fa|ser|dümen başı|OSM|ser|fa:ser>it:timone>tr:serdümen
pusula|n|it|bussola|kutucuk|OSM||la:buxis>it:bussola>tr:pusula
fırtına|n|it|fortuna|talih; şiddetli rüzgâr|EAT|fortuna|la:fortuna>it:fortuna>tr:fırtına
fortüne|n|fr|fortune|servet|MOD|fortuna|
borda|n|it|bordo|gemi yanı|OSM|bord-|
abordaj|n|fr|abordage|yanaşıp saldırma|OSM19|bord-|
bordür|n|fr|bordure|kenar|MOD|bord-|
filika|n|it|feluca|küçük tekne|OSM||ar:falūka>it:feluca>tr:filika
kadırga|n|el|kátergon|kürekli savaş gemisi|EAT||
kalyon|n|it|galeone|büyük yelkenli|OSM||
fırkateyn|n|it|fregata|hızlı savaş gemisi|OSM||
korvet|n|fr|corvette|küçük savaş gemisi|OSM19||
gondol|n|it|gondola|Venedik kayığı|OSM19||
yat|n|en|yacht|av gemisi|CUM||nl:jacht>en:yacht>tr:yat
vapur|n|fr|vapeur|buhar|OSM19||la:vapor>fr:vapeur>tr:vapur
tanker|n|en|tanker|depo gemisi|MOD||
feribot|n|en|ferry-boat|geçiş teknesi|MOD||
mavna|n|ar|maʿūna|yardım gemisi|OSM|A-W-N|
muavin|n|ar|muʿāwin|yardımcı|OSM19|A-W-N|
muavenet|n|ar|muʿāwana|yardım|OSM|A-W-N|
avene|n|ar|aʿwana|yardakçılar|OSM|A-W-N|
çapa|n|it|zappa|kazma; demir|OSM||
ıskarmoz|n|it|scarmo|kürek pimi|OSM||
ıskota|n|it|scotta|yelken ipi|OSM||
palamar|n|it|palamara|kalın halat|OSM||
gabya|n|it|gabbia|kafes; direk sepeti|OSM||
flok|n|it|fiocco|ön yelken|OSM||
mizana|n|it|mezzana|arka direk|OSM||
trinket|n|it|trinchetto|ön direk yelkeni|OSM||
lostromo|n|it|nostromo|güverte başı|OSM19||
tayfa|n|ar|ṭāʾifa|topluluk; gemi ekibi|EAT|T-W-F|
tavaf|n|ar|ṭawāf|çevresinde dönme|EAT|T-W-F|
mürettebat|n|ar|murattabāt|düzenlenmişler|OSM19|R-T-B|
rütbe|n|ar|rutba|derece|OSM|R-T-B|
tertip|n|ar|tartīb|düzenleme|OSM|R-T-B|
mertebe|n|ar|martaba|basamak|EAT|R-T-B|
kılavuz|n|tr|kulabuz|yol gösteren|DLT||
rota|n|it|rotta|kırılmış yol|OSM19||la:rupta>it:rotta>tr:rota
seyir|n|ar|sayr|gidiş|EAT|S-Y-R|
seyyar|adj|ar|sayyār|gezen|OSM|S-Y-R|
seyran|n|ar|sayarān|gezinti|EAT|S-Y-R|
seyyah|n|ar|sayyāḥ|gezgin|OSM|S-Y-H|
seyahat|n|ar|siyāḥa|gezi|OSM|S-Y-H|
pruva|n|it|prua|gemi başı|OSM||
pupa|n|it|poppa|gemi kıçı|OSM||
sancak|n|tr|sançak|bayrak; sağ yan|DLT|*sanç-|
sançmak|v|tr|sanç-|saplamak|DLT|*sanç-|
kıç|n|tr|kıç|arka|DLT||
karina|n|it|carena|gemi altı|OSM||
sintine|n|it|sentina|gemi dibi|OSM||
kaporta|n|it|caporta|baş kapak|OSM19|caput|
ambar|n|fa|anbār|depo|EAT||
lenger|n|fa|langar|çapa|OSM||
bandıra|n|it|bandiera|bayrak|OSM19||
forsa|n|it|forza|zorla çalıştırılan kürekçi|OSM|fortis|la:fortia>it:forza>tr:forsa
kürek|n|tr|kürgek|kazma aracı; kayık küreği|DLT||
levent|n|it|levante|doğulu; deniz askeri|OSM||
korsan|n|it|corsaro|akıncı|OSM|currere|la:cursus>it:corsaro>tr:korsan
tersane|n|it|darsena|yapım evi|OSM||ar:dāru'ṣ-ṣināʿa>it:darsena>tr:tersane
armatör|n|fr|armateur|donatan|OSM19|arma|
arma|n|it|arma|donanım; simge|OSM|arma|
ordu|n|tr|ordu|karargâh; asker topluluğu|ORH||
donanma|n|tr|donan-|donanmış filo|OSM||
filo|n|it|flotta|gemi topluluğu|OSM19||
ada|n|tr|ataġ|çevresi su kara|DLT||
yarımada|n|tr|yarım ataġ|yarı ada|CUM||
kıyı|n|tr|kıdıg|kenar|DLT||
sahil|n|ar|sāḥil|kıyı|EAT||
plaj|n|fr|plage|kumsal|CUM||
kumsal|n|tr|kum|kumlu kıyı|TDK||
dalga|n|tr|dalga|su kabarması|EAT||
gelgit|n|tr|gel git|med cezir|DD||
cezir|n|ar|cazr|çekilme|OSM||
mercan|n|ar|marcān|kırmızı deniz canlısı|EAT||
sünger|n|el|sfoungári|deniz süngeri|EAT||
şamandıra|n|el|sēmadoúra|işaret; yüzen işaret|OSM19||
olta|n|el|vólta|dönüş; balık ipi|OSM||
# --- Rüzgârlar ve hava ---------------------------------------------------------------
poyraz|n|el|boréas|kuzey rüzgârı|EAT||
lodos|n|el|nótos|güney rüzgârı|EAT||
karayel|n|tr|kara yel|kuzeybatı rüzgârı|OSM||
meltem|n|it|maltempo|kötü hava; yaz rüzgârı|OSM19||it:maltempo>el:meltémi>tr:meltem
imbat|n|el|embátēs|içe giren rüzgâr|OSM||
kasırga|n|tr|kasırga|dönen fırtına|EAT||
hortum|n|ar|ḫurṭūm|fil burnu; sütun biçimli fırtına|OSM||
tayfun|n|en|typhoon|büyük rüzgâr|MOD||zh:dàfēng>en:typhoon>tr:tayfun
siklon|n|fr|cyclone|dönen|CUM|kyklos|
# --- Balık ve deniz ürünleri: Rumca / İtalyanca -----------------------------------------
kefal|n|el|kéfalos|baş|EAT||
lüfer|n|el|loúfaros|lüfer|OSM||
çipura|n|el|tsipoúra|çipura|OSM19||
barbunya|n|el|barboúni|sakallı balık|OSM||
sardalya|n|it|sardella|Sardunya balığı|OSM19||
orkinos|n|el|orkýnos|ton balığı|OSM||
torik|n|el|toríki|iri palamut|OSM||
istakoz|n|el|astakós|istakoz|OSM||
kalamar|n|it|calamaro|mürekkep balığı|OSM19||la:calamarius>it:calamaro>tr:kalamar
sübye|n|el|soupiá|mürekkep balığı|OSM||
yengeç|n|tr|yengeç|kabuklu deniz canlısı|DLT||
kalkan|n|tr|kalkan|siper; yassı balık|DLT|*kalk-|
kalkmak|v|tr|kalk-|yükselmek|DLT|*kalk-|
kalkınma|n|tr|kalkın-|gelişme|DD|*kalk-|
mezgit|n|el|mezítis|mezgit|OSM||
tekir|n|tr|tekir|çizgili|OSM||
alabalık|n|tr|ala balık|benekli balık|DLT||
sazan|n|tr|sazan|tatlı su balığı|OSM||
turna|n|tr|turna|turna kuşu; turna balığı|DLT||
ringa|n|it|aringa|ringa balığı|MOD||
morina|n|it|morena|morina balığı|OSM19||
fok|n|fr|phoque|deniz memelisi|CUM||grc:phṑkē>la:phoca>fr:phoque>tr:fok
yunus|n|ar|yūnus|Yunus peygamber; yunus balığı|EAT||
dalyan|n|el|dalián|balık tuzağı|OSM||
ağ|n|tr|ag|örgü|DLT||
balık|n|tr|balık|suda yaşayan omurgalı|ORH||
balıkçı|n|tr|balıkçı|balık tutan|DLT||
yosun|n|tr|yosun|su bitkisi|EAT||
deniz|n|tr|teŋiz|büyük su|ORH||
denizci|n|tr|teŋizçi|deniz işçisi|OSM||
derya|n|fa|daryā|deniz|EAT||
bahir|n|ar|baḥr|deniz|EAT|B-H-R|
bahriye|n|ar|baḥriyya|deniz kuvvetleri|OSM19|B-H-R|
bahriyeli|n|ar|baḥriyya|deniz askeri|OSM19|B-H-R|
umman|n|ar|ʿummān|okyanus|EAT||
okyanus|n|fr|océan|dünyayı çevreleyen su|OSM19||grc:ōkeanós>la:oceanus>fr:océan>tr:okyanus
"""

FAMILIES = r"""
*sanç-|tr|saplamak|Eski Türkçe sanç- "saplamak"; sancak (saplanan bayrak direği; sonra gemide sağ yan) ve sançmak aynı kökten gelir.
*kalk-|tr|yükselmek|Eski Türkçe kalk- "yükselmek"; kalkan (yükseltilen siper; yassı balık) ve kalkınma aynı kökten türer.
scala|la|merdiven, basamak|Latince scala "merdiven"; Venedikçe yoluyla iskele, ölçek anlamında skala ve eskalasyon aynı kökten gelir.
camera|la|oda, kubbeli yer|Latince camera "kemerli oda"; kamara (gemi odası), kamarot ve kamera (karanlık oda) aynı kökten türer.
cooperire|la|örtmek|Latince cooperire "örtmek"; güverte (örtü) ve kuvertür aynı kökten gelir.
fortuna|la|talih|Latince fortuna "talih"; denizcilerin "fortuna di mare" (deniz kazası) deyişinden fırtına ve fortüne aynı kökten türer.
bord-|it|kenar, gemi yanı|Cermence *bord "kenar, tahta"; İtalyanca bordo yoluyla borda, Fransızca yoluyla abordaj ve bordür aynı kökten gelir.
A-W-N|ar|yardım etmek|Arapça ʿ-w-n kökü; muavin, muavenet, avene ve mavna (yardım gemisi) aynı kökten türer.
T-W-F|ar|dolaşmak|Arapça ṭ-w-f kökü; tavaf (çevresinde dönme) ve tayfa (dolaşan topluluk, gemi ekibi) aynı kökten gelir.
R-T-B|ar|sıralamak|Arapça r-t-b kökü; rütbe, tertip, mertebe ve mürettebat aynı kökten türer.
S-Y-R|ar|gitmek, gezmek|Arapça s-y-r kökü; seyir, seyyar ve seyran aynı kökten gelir.
S-Y-H|ar|gezmek|Arapça s-y-ḥ kökü; seyahat ve seyyah aynı kökten türer.
fortis|la|güçlü|Latince fortis "güçlü"; forsa (zorla kürek çeken) ve İtalyanca forza aynı kökten gelir.
arma|la|silah, donanım|Latince arma "silahlar"; arma (gemi donanımı; simge) ve armatör (donatan) aynı kökten türer.
B-H-R|ar|deniz|Arapça b-ḥ-r kökü; bahir (deniz), bahriye ve bahriyeli aynı kökten gelir.
"""
