# -*- coding: utf-8 -*-
"""Korpus 18 — Ekonomi, ticaret ve para."""

WORDS = r"""
# --- Çarşı, pazar ve ticaret örgütlenmesi ------------------------------------------
ticarethane|n|ar|ticāret-ḫāne|ticaret evi|OSM19|-hāne|ar:ticāra>fa:ticāret-ḫāne>tr:ticarethane
ticaretgâh|n|ar|ticāret-gāh|ticaret yeri|OSM|-gāh|ar:ticāra>fa:ticāret-gāh>tr:ticaretgâh
ticari|adj|ar|ticārī|ticarete ilişkin|OSM19|T-C-R|
tacirlik|n|ar|tācir|tacir olma|OSM|T-C-R|
tüccarlık|n|ar|tuccār|tüccar olma|OSM|T-C-R|
meta|n|ar|matāʿ|yararlanılan mal|OSM|M-T-A|
emtia|n|ar|amtiʿa|mallar|OSM19|M-T-A|
temettü|n|ar|tamattuʿ|yararlanma; kâr payı|OSM19|M-T-A|
bezirgân|n|fa|bāzārgān|pazarcı, tüccar|EAT|bāzār|
bezirgânlık|n|fa|bāzārgān|tüccarlık; çıkarcılık|OSM|bāzār|
pazarlama|n|fa|bāzār|satışa sunma işi|MOD|bāzār|
pazarlamacı|n|fa|bāzār|pazarlama yapan|MOD|bāzār|
pazarbaşı|n|fa|bāzār|pazar denetçisi|OSM|bāzār|
pazarcılık|n|fa|bāzār|pazarda satıcılık|OSM|bāzār|
bitpazarı|n|tr|bit pazarı|eski eşya pazarı|OSM19||
kapan|n|ar|qabbān|büyük kantar; toptan erzak pazarı|OSM||
kapancı|n|ar|qabbān|kapan hanında tartıcı|OSM||
bedestenci|n|fa|bezzāzistān|bedestende satıcı|OSM|-istān|
hancı|n|fa|ḫān|han işleten|EAT||
kervanbaşı|n|fa|kārvān|kervan önderi|OSM||
tezgâhtarlık|n|fa|dastgāh-dār|tezgâh başında satıcılık|OSM19|dār-|
çarşılı|adj|fa|çahār-sū|çarşısı olan; çarşı esnafından|OSM||
esnaflık|n|ar|aṣnāf|esnaf olma|OSM||
lonca|n|it|loggia|üstü örtülü yer; esnaf birliği|OSM||ger:laubja>it:loggia>tr:lonca
loncacı|n|it|loggia|lonca üyesi|OSM||
ahi|n|tr?|akı|cömert; esnaf teşkilatı üyesi|EAT||
ahilik|n|tr?|akı|ahi teşkilatı|EAT||
gedik|n|tr|gedik|yarık; esnafın tekel hakkı|OSM|*ged-|
gedikli|adj|tr|gedik|gedik sahibi; kıdemli|OSM|*ged-|
narh|n|fa|narḫ|resmî fiyat|EAT||
ihtisap|n|ar|iḥtisāb|hesaba çekme; çarşı denetimi|OSM|H-S-B|
muhtesip|n|ar|muḥtasib|çarşı denetçisi|EAT|H-S-B|
kethüda|n|fa|kad-ḫudā|ev sahibi; lonca temsilcisi|OSM|ḫudā|
kethüdalık|n|fa|kad-ḫudā|kethüda görevi|OSM|ḫudā|
peştemal|n|fa|puşt-māl|bel örtüsü; ustalık kuşağı|OSM||
yiğitbaşı|n|tr|yigit başı|lonca yöneticisi|OSM||
esnafbaşı|n|ar|aṣnāf|esnaf temsilcisi|OSM||
ustabaşı|n|fa|ustād|baş usta|OSM19||
ustalık|n|fa|ustād|usta olma|EAT||
kalfalık|n|ar|ḫalīfa|kalfa olma|OSM|H-L-F|
halef|n|ar|ḫalaf|ardından gelen|OSM|H-L-F|
halife|n|ar|ḫalīfa|yerine geçen|EAT|H-L-F|
hilaf|n|ar|ḫilāf|karşıtlık|EAT|H-L-F|
ihtilaf|n|ar|iḫtilāf|anlaşmazlık|OSM|H-L-F|
çıraklık|n|fa|çarāġ|çırak olma|OSM||
şakirt|n|fa|şāgird|öğrenci, çırak|EAT||
pir|n|fa|pīr|yaşlı; mesleğin kurucu ulusu|EAT||
fütüvvet|n|ar|futuwwa|yiğitlik; esnaf ahlak kuralları|EAT|F-T-W|
erbap|n|ar|arbāb|sahipler; bir işin ehli|OSM||
ehil|adj|ar|ahl|aile; bir işte yeterli kişi|EAT|A-H-L|
ehli|adj|ar|ahlī|evcil|OSM|A-H-L|
maharet|n|ar|mahāra|ustalık|OSM|M-H-R|
mahir|adj|ar|māhir|usta, becerikli|OSM|M-H-R|
hirfet|n|ar|ḥirfa|zanaat|OSM|H-R-F|
meslek|n|ar|maslak|gidilen yol|OSM19|S-L-K|
mesleki|adj|ar|maslakī|mesleğe ilişkin|CUM|S-L-K|
meslektaş|n|ar|maslak|aynı meslekten kişi|CUM|S-L-K|
sülûk|n|ar|sulūk|yola girme|OSM|S-L-K|
destur|n|fa|dastūr|izin; kural|EAT|dast|
helallik|n|ar|ḥalāl|helal etme|OSM|H-L-L|
ihvan|n|ar|iḫwān|kardeşler|OSM|A-H-W|
uhuvvet|n|ar|uḫuwwa|kardeşlik|OSM|A-H-W|
siftah|n|ar|istiftāḥ|açılış; günün ilk satışı|OSM|F-T-H|
iftitah|n|ar|iftitāḥ|açılış|OSM|F-T-H|
miftah|n|ar|miftāḥ|anahtar|OSM|F-T-H|
fettah|adj|ar|fattāḥ|açan|OSM|F-T-H|
kepenk|n|unk|kepenk|dükkân kapağı|OSM||
çığırtkan|n|tr|çıġır-|bağırarak müşteri çağıran|OSM19||
halci|n|fr|halle|toptancı halinde satıcı|MOD||ger:halla>fr:halle>tr:halci
ilan|n|ar|iʿlān|duyurma|OSM19|A-L-N|
aleni|adj|ar|ʿalanī|açık, herkesin gözü önünde|OSM|A-L-N|
alenen|adv|ar|ʿalanan|açıkça|OSM|A-L-N|
afiş|n|fr|affiche|duvar ilanı|CUM||la:affigere>fr:affiche>tr:afiş
logo|n|en|logo|işaret|MOD|logos|grc:lógos>en:logotype>tr:logo
barkod|n|en|barcode|çubuk kod|NEW||
irsaliye|n|ar|irsāliyya|gönderi belgesi|OSM19|R-S-L|
irsal|n|ar|irsāl|gönderme|OSM|R-S-L|
mürsel|adj|ar|mursal|gönderilmiş|OSM|R-S-L|
risale|n|ar|risāla|mektup; küçük kitap|EAT|R-S-L|
bordro|n|fr|bordereau|kenar notu; ödeme cetveli|CUM|bord-|
sipariş|n|fa|sipāriş|ısmarlama|OSM|sipurden|
siparişçi|n|fa|sipāriş|sipariş alan|MOD|sipurden|
ısmarlamak|v|tr|ısmarla-|sipariş etmek|EAT|*ısmarla-|
ısmarlama|n|tr|ısmarla-|sipariş|OSM|*ısmarla-|
tedarik|n|ar|tadāruk|yetişip ele geçirme; sağlama|OSM|D-R-K|
tedarikçi|n|ar|tadāruk|mal sağlayan|NEW|D-R-K|
idrak|n|ar|idrāk|ulaşma, kavrama|EAT|D-R-K|
müdrik|adj|ar|mudrik|kavrayan|OSM|D-R-K|
toptan|adv|tr|top|bütün olarak|OSM|*top-|
toptancı|n|tr|top|toptan satan|OSM19|*top-|
toptancılık|n|tr|top|toptan satış işi|CUM|*top-|
perakende|n|fa|parākanda|dağınık, saçılmış|OSM|parākande|
perakendeci|n|fa|parākanda|perakende satıcı|CUM|parākande|
perakendecilik|n|fa|parākanda|perakende satış işi|MOD|parākande|
çerçi|n|tr?|çerçi|gezgin satıcı|OSM||
çerçilik|n|tr?|çerçi|gezgin satıcılık|OSM||
simsar|n|ar|simsār|aracı|OSM|S-M-S-R|
simsariye|n|ar|simsāriyya|aracılık ücreti|OSM19|S-M-S-R|
simsarlık|n|ar|simsār|aracılık|OSM|S-M-S-R|
tellal|n|ar|dallāl|yol gösteren; çığırtkan|EAT|D-L-L|
tellallık|n|ar|dallāl|tellal işi|OSM|D-L-L|
dellaliye|n|ar|dallāliyya|tellal ücreti|OSM|D-L-L|
mezat|n|ar|mazād|artırma|OSM|Z-Y-D|
mezatçı|n|ar|mazād|mezat yapan|OSM19|Z-Y-D|
müzayede|n|ar|muzāyada|artırma ile satış|OSM19|Z-Y-D|
ziyade|adj|ar|ziyāda|fazla|EAT|Z-Y-D|
tezyit|n|ar|tazyīd|artırma|OSM|Z-Y-D|
ihale|n|ar|iḥāla|havale etme; eksiltme ile verme|OSM19|H-W-L|
artırma|n|tr|art-|açık artırma|TDK||
eksiltme|n|tr|eksil-|açık eksiltme|TDK|*eksi-|
eksiltmek|v|tr|eksilt-|azaltmak|DLT|*eksi-|
tuhafiye|n|ar|tuḥafiyya|nadir, hoş eşya|OSM19|T-H-F|
tuhafiyeci|n|ar|tuḥafiyya|tuhafiye satıcısı|CUM|T-H-F|
zücaciye|n|ar|zucāciyya|cam eşya|OSM19||
manifaturacı|n|it|manifattura|kumaş satıcısı|OSM19|manus|la:manufactura>it:manifattura>tr:manifaturacı
bezzaz|n|ar|bazzāz|bez satıcısı|EAT|B-Z-Z|
bezzaziye|n|ar|bazzāziyya|bezcilik|OSM|B-Z-Z|
çuha|n|fa|çūḫā|yünlü kumaş|EAT||
çuhacı|n|fa|çūḫā|çuha satan|OSM||
kumaşçı|n|ar|qumāş|kumaş satıcısı|OSM||
ipekçi|n|tr|yipek|ipek üreten ya da satan|OSM||
yüncü|n|tr|yuŋ|yün satıcısı|OSM||
pamukçu|n|fa|panba|pamuk satıcısı|OSM||
kürkçü|n|tr|kürk|kürk satıcısı|OSM||
derici|n|tr|teri|deri işleyen|OSM||
debbağ|n|ar|dabbāġ|deri sepileyen|EAT|D-B-G|
tabakhane|n|ar|dabbāġ-ḫāne|deri işleme yeri|OSM|-hāne|ar:dabbāġ>fa:dabbāġ-ḫāne>tr:tabakhane
dibagat|n|ar|dibāġa|deri sepileme|OSM|D-B-G|
saraç|n|ar|sarrāc|eyer yapan|EAT|S-R-C|
saraçlık|n|ar|sarrāc|eyercilik|OSM|S-R-C|
siraç|n|ar|sirāc|kandil|EAT|S-R-C|
nalbur|n|fa|naʿl-bur|nal kesen; hırdavatçı|OSM|naʿl|ar:naʿl>fa:naʿl-bur>tr:nalbur
nalburiye|n|fa|naʿl-bur|hırdavat eşyası|OSM19|naʿl|
celep|n|ar|callāb|getiren; kasaplık hayvan tüccarı|OSM|C-L-B|
celp|n|ar|calb|çekme, getirme|OSM|C-L-B|
celbetmek|v|ar|calb|çekmek|OSM|C-L-B|
kasaplık|n|ar|qaṣṣāb|kasap işi; kesimlik|OSM||
bakkaliye|n|ar|baqqāliyya|bakkal malları|OSM19|B-K-L|
bakkallık|n|ar|baqqāl|bakkal işi|OSM|B-K-L|
bakliyat|n|ar|baqliyyāt|baklagiller|OSM19|B-K-L|
manavlık|n|unk|manav|manav işi|OSM||
sütçü|n|tr|süt|süt satan|OSM||
yoğurtçu|n|tr|yoġurt|yoğurt satan|OSM||
peynirci|n|fa|panīr|peynir satan|OSM||
sebzeci|n|fa|sabza|sebze satan|OSM19||
meyveci|n|fa|mīva|meyve satan|OSM||
baharatçı|n|ar|bahārāt|baharat satan|OSM19||
tütüncü|n|tr|tütün|tütün satan|OSM||
şarapçı|n|ar|şarāb|şarap yapan ya da satan|OSM|Ş-R-B|
meyhaneci|n|fa|may-ḫāne|meyhane işleten|OSM|-hāne|
simitçi|n|ar|samīd|simit satan|OSM||
börekçi|n|tr|bürek|börek yapan|OSM||
çörekçi|n|tr|çörek|çörek yapan|OSM||
bozacı|n|fa|būza|boza satan|OSM||
dondurmacı|n|tr|toŋ-|dondurma satan|OSM19|*don-|
şekerci|n|fa|şakar|şeker satan|OSM||
kahveci|n|ar|qahwa|kahve satan|OSM||
çaycı|n|zh|chá|çay satan|OSM19||zh:chá>fa:çāy>tr:çaycı
lokantacı|n|it|locanda|lokanta işleten|OSM19||
aktar|n|ar|ʿaṭṭār|güzel koku ve baharat satıcısı|EAT|A-T-R|
ıtriyat|n|ar|ʿiṭriyyāt|güzel kokular|OSM19|A-T-R|
ıtır|n|ar|ʿiṭr|güzel koku|OSM|A-T-R|
sahaf|n|ar|ṣaḥḥāf|kitap satıcısı|OSM|S-H-F|
sahife|n|ar|ṣaḥīfa|yaprak, sayfa|EAT|S-H-F|
mushaf|n|ar|muṣḥaf|yapraklar; Kur'an nüshası|EAT|S-H-F|
mücellit|n|ar|mucallid|ciltçi|OSM|C-L-D|
teclit|n|ar|taclīd|ciltleme|OSM|C-L-D|
ciltçi|n|ar|cild|kitap ciltleyen|OSM19|C-L-D|
nakkaş|n|ar|naqqāş|nakış işleyen|EAT|N-K-Ş|
münakkaş|adj|ar|munaqqaş|nakışlı|OSM|N-K-Ş|
kuyum|n|tr|kuyum|dökme değerli maden işi|OSM|*kuy-|
kuyumculuk|n|tr|kuyumcı|kuyumcu işi|OSM|*kuy-|
gümüşçü|n|tr|kümüş|gümüş işleyen|OSM||
bakırcı|n|tr|bakır|bakır işleyen|OSM||
kazancı|n|tr|kazġan|kazan yapan|OSM||
semerci|n|el|samárion|semer yapan|OSM||
keçeci|n|tr|kidiz|keçe yapan|OSM||
çömlekçi|n|tr|çölmek|çömlek yapan|OSM||
mumcu|n|fa|mūm|mum yapan|OSM||
sabuncu|n|ar|ṣābūn|sabun yapan|OSM||la:sapo>ar:ṣābūn>tr:sabuncu
sıvacı|n|tr|sıva-|sıva yapan|OSM19||
camcı|n|fa|cām|cam satan ya da takan|OSM||
ayakkabıcı|n|tr|adak kap|ayakkabı yapan ya da satan|OSM19||
hurda|n|fa|ḫurda|ufak, kırıntı|OSM||
hurdacı|n|fa|ḫurda|hurda alıp satan|CUM||
eskici|n|tr|eski|eski eşya alıp satan|OSM||
arabacı|n|ar|ʿaraba|araba süren|OSM||
kayıkçı|n|tr|kayġuk|kayık işleten|OSM||
deveci|n|tr|tebe|deve güden ya da kiralayan|OSM||
katırcı|n|tr|katır|katırla yük taşıyan|OSM||
oduncu|n|tr|otuŋ|odun satan|OSM||
kömürcü|n|tr|kömür|kömür satan|OSM||
mücevher|n|ar|mucawhar|cevherle süslü|OSM|C-W-H-R|fa:gōhar>ar:cawhar>tr:mücevher
mücevherat|n|ar|mucawharāt|mücevherler|OSM19|C-W-H-R|
cevher|n|ar|cawhar|öz; değerli taş|EAT|C-W-H-R|fa:gōhar>ar:cawhar>tr:cevher
cevahir|n|ar|cawāhir|değerli taşlar|OSM|C-W-H-R|
elmas|n|ar|almās|elmas|EAT||grc:adámas>ar:almās>tr:elmas
pırlanta|n|it|brillante|parlayan|OSM19||
# --- Para, sikke, darphane ------------------------------------------------------
kuruş|n|de|Groschen|iri sikke|OSM|grossus|la:grossus>de:Groschen>tr:kuruş
kuruşluk|n|de|Groschen|kuruş değerinde|OSM19|grossus|
mangır|n|mn|möŋgün|gümüş; bakır para|OSM||
sikke|n|ar|sikka|damga kalıbı; madeni para|EAT|S-K-K|
meskûk|adj|ar|maskūk|basılmış (para)|OSM|S-K-K|
sikkezen|n|fa|sikka-zan|sikke basan|OSM|S-K-K|ar:sikka>fa:sikka-zan>tr:sikkezen
dinar|n|ar|dīnār|altın para|EAT||la:denarius>ar:dīnār>tr:dinar
dirhem|n|ar|dirham|gümüş para; ağırlık birimi|EAT|drakhmē|grc:drakhmḗ>ar:dirham>tr:dirhem
drahmi|n|el|drakhmí|Yunan para birimi|OSM19|drakhmē|
darphane|n|ar|ḍarb-ḫāne|para basım evi|OSM|-hāne|ar:ḍarb>fa:ḍarb-ḫāne>tr:darphane
darp|n|ar|ḍarb|vurma; para basma|OSM|D-R-B|
darbe|n|ar|ḍarba|vuruş|OSM|D-R-B|
darbımesel|n|ar|ḍarb-i maṯal|atasözü|OSM|D-R-B|
ızdırap|n|ar|iḍṭirāb|çalkalanma; acı|OSM|D-R-B|
muzdarip|adj|ar|muḍṭarib|acı çeken|OSM|D-R-B|
lira|n|it|lira|libre; para birimi|OSM19|libra|la:libra>it:lira>tr:lira
liret|n|it|lire|İtalyan lirası|CUM|libra|
libre|n|fr|livre|yarım kilo|OSM19|libra|la:libra>fr:livre>tr:libre
banknot|n|en|banknote|banka kâğıdı|OSM19|banca|
banko|n|it|banco|tezgâh|OSM19|banca|
kaime|n|ar|qāʾima|ayakta duran; kâğıt para|OSM19|K-W-M|
evrak|n|ar|awrāq|yapraklar; belgeler|OSM|W-R-K|
varak|n|ar|waraq|yaprak; ince levha|OSM|W-R-K|
varaka|n|ar|waraqa|tek yaprak; belge|OSM|W-R-K|
madeni|adj|ar|maʿdinī|madenden yapılmış|OSM19|M-D-N|
bozuk|adj|tr|buz-|bozulmuş; ufak para|OSM|*boz-|
bozukluk|n|tr|buz-|bozuk para|OSM19|*boz-|
bozmak|v|tr|buz-|yıkmak; büyük parayı ufaklamak|ORH|*boz-|
bozdurmak|v|tr|buz-|parayı ufaklatmak|OSM|*boz-|
ufaklık|n|tr|ufak|küçük para|OSM19||
metelik|n|fr|métallique|madeni (para)|OSM19||grc:métallon>fr:métallique>tr:metelik
mecidiye|n|ar|macīdiyya|Abdülmecid dönemi gümüş parası|OSM19||
beşlik|n|tr|béş|beş kuruşluk para|OSM19||
onluk|n|tr|on|on paralık|OSM19||
altılık|n|tr|altı|altı kuruşluk para|OSM19||
zolota|n|sl|złoty|altın (Leh sikkesi)|OSM||
sent|n|en|cent|yüzde bir|CUM|centum|la:centum>en:cent>tr:sent
santim|n|fr|centime|yüzde bir frank|OSM19|centum|la:centum>fr:centime>tr:santim
dolar|n|en|dollar|Joachimsthal gümüşü|OSM19||de:Taler>en:dollar>tr:dolar
sterlin|n|en|sterling|İngiliz para birimi|OSM19||
mark|n|de|Mark|işaret; Alman para birimi|OSM19||
frank|n|fr|franc|Frank; Fransız para birimi|OSM19||
ruble|n|sl|rubl'|kesilmiş parça; Rus para birimi|OSM19||
yen|n|ja|en|yuvarlak|CUM||zh:yuán>ja:en>tr:yen
yuan|n|zh|yuán|yuvarlak|MOD||
rupi|n|en|rupee|gümüş para|OSM19||sa:rūpya>hi:rupayā>en:rupee>tr:rupi
riyal|n|ar|riyāl|kraliyet parası|OSM19||la:regalis>es:real>ar:riyāl>tr:riyal
peso|n|es|peso|ağırlık|MOD|pendere|la:pensum>es:peso>tr:peso
avro|n|fr|euro|Avrupa parası|NEW|Eurṓpē|grc:Eurṓpē>fr:euro>tr:avro
euro|n|en|euro|Avrupa parası|NEW|Eurṓpē|grc:Eurṓpē>en:euro>tr:euro
kumbara|n|fa|ḫumpāra|küçük küp; para kutusu|OSM||
meblağ|n|ar|mablaġ|ulaşılan miktar|OSM|B-L-G|
belagat|n|ar|balāġa|söz ustalığı|OSM|B-L-G|
mübalağa|n|ar|mubālaġa|abartma|OSM|B-L-G|
bâliğ|adj|ar|bāliġ|ulaşan; erişkin|OSM|B-L-G|
tebliğ|n|ar|tablīġ|ulaştırma, bildirme|OSM|B-L-G|
yekûn|n|ar|yakūn|olur; toplam|OSM|K-W-M|
anapara|n|tr|ana para|kapital|TDK||
ödünç|n|tr|ötünç|geri verilmek üzere alınan|DLT||
# --- Faiz, borç, kredi, banka ---------------------------------------------------
fayda|n|ar|fāʾida|yarar|EAT|F-Y-D|
istifade|n|ar|istifāda|yararlanma|OSM|F-Y-D|
müfit|adj|ar|mufīd|yararlı|OSM|F-Y-D|
feyiz|n|ar|fayḍ|taşma; bereket|EAT|F-Y-Z|
feyezan|n|ar|fayaḍān|taşkın|OSM|F-Y-Z|
faizli|adj|ar|fāʾiḍ|faiz içeren|OSM19|F-Y-Z|
faizsiz|adj|ar|fāʾiḍ|faiz içermeyen|CUM|F-Y-Z|
faizci|n|ar|fāʾiḍ|faizle borç veren|OSM19|F-Y-Z|
riba|n|ar|ribā|artma; tefecilik|EAT|R-B-W|
ribacı|n|ar|ribā|tefeci|OSM|R-B-W|
mürebbi|n|ar|murabbī|yetiştiren, eğitmen|OSM|R-B-W|
mürebbiye|n|ar|murabbiya|kadın eğitmen|OSM19|R-B-W|
tefeci|n|unk|tefe|aşırı faizle borç veren|OSM19||
tefecilik|n|unk|tefe|aşırı faizcilik|CUM||
murabaha|n|ar|murābaḥa|kârla satış; tefecilik|OSM|R-B-H|
ribh|n|ar|ribḥ|kâr|OSM|R-B-H|
rabıh|adj|ar|rābiḥ|kârlı|OSM|R-B-H|
banker|n|fr|banquier|banka sahibi|OSM19|banca|it:banca>fr:banquier>tr:banker
bankacı|n|it|banca|bankada çalışan|CUM|banca|
bankacılık|n|it|banca|banka işleri|CUM|banca|
kredili|adj|fr|crédit|kredi ile alınan|MOD|credere|
kreditör|n|fr|créditeur|alacaklı|MOD|credere|la:creditor>fr:créditeur>tr:kreditör
kredibilite|n|fr|crédibilité|güvenilirlik|NEW|credere|
akreditif|n|fr|accréditif|kredi mektubu|CUM|credere|
sermayedar|n|fa|sarmāya-dār|sermaye sahibi|OSM19|dār-|
kapitalist|n|fr|capitaliste|sermayeci|CUM|caput|la:caput>fr:capitaliste>tr:kapitalist
borsacı|n|it|borsa|borsada işlem yapan|CUM||la:bursa>it:borsa>tr:borsacı
prim|n|fr|prime|ilk; ödül|CUM|primus|la:primus>fr:prime>tr:prim
primli|adj|fr|prime|prim ödenen|MOD|primus|
primitif|adj|fr|primitif|ilkel|CUM|primus|
acentelik|n|it|agente|acente işi|CUM|agere|la:agens>it:agente>tr:acentelik
ajanda|n|fr|agenda|yapılacak şeyler|CUM|agere|la:agenda>fr:agenda>tr:ajanda
aktif|adj|fr|actif|etkin; varlıklar|CUM|agere|la:activus>fr:actif>tr:aktif
komisyoncu|n|fr|commission|komisyonla çalışan|CUM|mittere|
komisyonculuk|n|fr|commission|komisyonculuk işi|CUM|mittere|
bilanço|n|it|bilancio|terazi; denge|OSM19|bilanx|la:bilanx>it:bilancio>tr:bilanço
balans|n|fr|balance|terazi; denge|CUM|bilanx|la:bilanx>fr:balance>tr:balans
maliyet|n|ar|māliyya|mala ilişkin; üretim gideri|CUM|M-W-L|
mali|adj|ar|mālī|mala, paraya ilişkin|OSM19|M-W-L|
maliyeci|n|ar|māliyya|maliye çalışanı|CUM|M-W-L|
emval|n|ar|amwāl|mallar|OSM|M-W-L|
mütemevvil|adj|ar|mutamawwil|varlıklı|OSM|M-W-L|
temvil|n|ar|tamwīl|mal verme; finanse etme|OSM|M-W-L|
mallı|adj|ar|māl|malı olan|OSM|M-W-L|
makbuz|n|ar|maqbūḍ|alınmış; alındı belgesi|OSM|K-B-D|
kabz|n|ar|qabḍ|tutma, alma|OSM|K-B-D|
kabız|n|ar|qabḍ|tutulma|OSM|K-B-D|
kabzımal|n|ar|qābiḍ-i māl|mal alıcı; hal komisyoncusu|OSM19|K-B-D|
kabzetmek|v|ar|qabḍ|ele geçirmek, almak|OSM|K-B-D|
tahsilat|n|ar|taḥṣīlāt|toplanan paralar|OSM19|H-S-L|
muhassıl|n|ar|muḥaṣṣil|vergi toplayan|OSM|H-S-L|
hâsıla|n|ar|ḥāṣila|elde edilen; toplam ürün|OSM19|H-S-L|
ödeme|n|tr|öte-|borç verme işi|OSM|*öde-|
ödenek|n|tr|öte-|ayrılan para|DD|*öde-|
ödenti|n|tr|öte-|aidat|DD|*öde-|
ödemeli|adj|tr|öte-|ücreti alıcıdan alınan|MOD|*öde-|
ödeşmek|v|tr|öte-|karşılıklı borcu kapatmak|OSM|*öde-|
alacaklı|n|tr|alacak|alacağı olan|OSM|*al-|
verecek|n|tr|ber-|borç|OSM|*ver-|
vade|n|ar|waʿd|söz verme; süre|OSM|W-A-D|
vadeli|adj|ar|waʿd|süresi belirli|OSM19|W-A-D|
vadesiz|adj|ar|waʿd|süresi olmayan|CUM|W-A-D|
mevut|adj|ar|mawʿūd|vadedilmiş|OSM|W-A-D|
vaat|n|ar|waʿd|söz verme|EAT|W-A-D|
temerrüt|n|ar|tamarrud|direnme; borcu geciktirme|OSM19||
mütemerrit|adj|ar|mutamarrid|direnen|OSM19||
mevduat|n|ar|mawdūʿāt|bırakılmış şeyler; banka parası|CUM|W-D-A|
mudi|n|ar|mūdiʿ|bırakan; mevduat sahibi|CUM|W-D-A|
tevdi|n|ar|tawdīʿ|bırakma, emanet etme|OSM|W-D-A|
tevdiat|n|ar|tawdīʿāt|bırakılan paralar|OSM19|W-D-A|
vedia|n|ar|wadīʿa|emanet|OSM|W-D-A|
veda|n|ar|wadāʿ|ayrılış selamı|EAT|W-D-A|
karz|n|ar|qarḍ|ödünç|OSM|K-R-D|
ikraz|n|ar|iqrāḍ|ödünç verme|OSM|K-R-D|
istikraz|n|ar|istiqrāḍ|ödünç alma|OSM19|K-R-D|
mukriz|n|ar|muqriḍ|ödünç veren|OSM19|K-R-D|
karzen|adv|ar|qarḍan|ödünç olarak|OSM|K-R-D|
borçlanmak|v|sog|pwrc|borç altına girmek|OSM|borç|
borçlanma|n|sog|pwrc|borçlanmak işi|CUM|borç|
borçsuz|adj|sog|pwrc|borcu olmayan|OSM|borç|
yatırmak|v|tr|yat-|bankaya para koymak|OSM|*yat-|
yatırımcılık|n|tr|yat-|yatırım yapma işi|MOD|*yat-|
plasman|n|fr|placement|yerleştirme; yatırım|CUM||
likidite|n|fr|liquidité|akışkanlık; nakde çevrilebilirlik|MOD|liquere|la:liquidus>fr:liquidité>tr:likidite
likit|adj|fr|liquide|akışkan; nakit|MOD|liquere|la:liquidus>fr:liquide>tr:likit
likidasyon|n|fr|liquidation|tasfiye|CUM|liquere|
dövizci|n|fr|devise|döviz alıp satan|MOD||
parite|n|fr|parité|eşitlik|MOD||la:paritas>fr:parité>tr:parite
endeks|n|fr|index|gösterge|MOD||la:index>fr:index>tr:endeks
portföy|n|fr|portefeuille|yaprak taşıyan; cüzdan|CUM|portare|
kârlılık|n|fa|kār|kâr getirme|MOD|kār|
kârlı|adj|fa|kār|kazanç getiren|OSM|kār|
kârsız|adj|fa|kār|kazanç getirmeyen|OSM19|kār|
kârhane|n|fa|kār-ḫāne|iş yeri; işlik|OSM|kār|
kârgir|adj|fa|kār-gīr|taş ya da tuğlayla yapılmış|OSM|kār|
itibari|adj|ar|iʿtibārī|saymaca, nominal|OSM19|A-B-R|
ibret|n|ar|ʿibra|ders alınacak şey|EAT|A-B-R|
muteber|adj|ar|muʿtabar|geçerli, saygın|OSM|A-B-R|
tedavül|n|ar|tadāwul|elden ele dolaşma|OSM19|D-W-L|
mütedavil|adj|ar|mutadāwil|dolaşımda olan|OSM19|D-W-L|
düvel|n|ar|duwal|devletler|OSM|D-W-L|
devletçi|adj|ar|dawla|devletçilik yanlısı|CUM|D-W-L|
devletleştirme|n|ar|dawla|kamuya geçirme|CUM|D-W-L|
konkordato|n|it|concordato|uzlaşma|CUM||la:concordare>it:concordato>tr:konkordato
tasfiye|n|ar|taṣfiya|arıtma; kapatma|OSM|S-F-W|
tasfiyeci|n|ar|taṣfiya|tasfiye yapan|CUM|S-F-W|
musaffa|adj|ar|muṣaffā|arıtılmış|OSM|S-F-W|
safi|adj|ar|ṣāfī|arı, katıksız; net|OSM|S-F-W|
mahsup|n|ar|maḥsūb|hesaba geçirilmiş|OSM19|H-S-B|
mahsuplaşmak|v|ar|maḥsūb|karşılıklı borçları düşmek|MOD|H-S-B|
takas|n|ar|taqāṣṣ|ödeşme|OSM|K-S-S|
kısas|n|ar|qiṣāṣ|misilleme cezası|EAT|K-S-S|
kıssa|n|ar|qiṣṣa|öykü|EAT|K-S-S|
trampa|n|it|trampa|değiş tokuş|OSM19||
barter|n|en|barter|takas|NEW||
mübadele|n|ar|mubādala|karşılıklı değiştirme|OSM|B-D-L|
mübadil|n|ar|mubādil|değiştirilen; göçmen|CUM|B-D-L|
tebdil|n|ar|tabdīl|değiştirme|OSM|B-D-L|
tebeddül|n|ar|tabaddul|değişme|OSM|B-D-L|
mütebeddil|adj|ar|mutabaddil|değişen|OSM|B-D-L|
bedelli|adj|ar|badal|karşılığı ödenen|MOD|B-D-L|
bedelsiz|adj|ar|badal|karşılıksız|MOD|B-D-L|
virman|n|fr|virement|hesaptan hesaba aktarma|MOD||
avans|n|fr|avance|öne geçme; ön ödeme|CUM||la:abante>fr:avance>tr:avans
tediye|n|ar|taʾdiya|ödeme|OSM|A-D-Y|
eda|n|ar|adāʾ|yerine getirme; ödeme|EAT|A-D-Y|
ifa|n|ar|īfāʾ|yerine getirme|OSM|W-F-Y|
vefat|n|ar|wafāt|tam olma; ölüm|EAT|W-F-Y|
istifa|n|ar|istiʿfāʾ|bağışlanma isteme; görevden çekilme|OSM|A-F-W|
muaf|adj|ar|muʿāf|bağışlanmış|OSM|A-F-W|
muafiyet|n|ar|muʿāfiyya|bağışıklık|OSM19|A-F-W|
af|n|ar|ʿafw|bağışlama|EAT|A-F-W|
affetmek|v|ar|ʿafw|bağışlamak|EAT|A-F-W|
dekont|n|fr|décompte|hesap dökümü|MOD||
tazmin|n|ar|taḍmīn|zararı karşılama|OSM|D-M-N|
zımni|adj|ar|ḍimnī|içinde saklı, üstü kapalı|OSM|D-M-N|
zımnen|adv|ar|ḍimnan|üstü kapalı olarak|OSM|D-M-N|
mutazammın|adj|ar|mutaḍammin|içeren|OSM|D-M-N|
zamime|n|ar|ḍamīma|ek|OSM|Z-M-M|
zammetmek|v|ar|ḍamm|eklemek|OSM|Z-M-M|
munzam|adj|ar|munḍamm|eklenmiş|OSM|Z-M-M|
zamlanmak|v|ar|ḍamm|fiyatı artmak|MOD|Z-M-M|
zamlı|adj|ar|ḍamm|zam yapılmış|MOD|Z-M-M|
ucuzlamak|v|tr|uçuz|fiyatı düşmek|OSM|*ucuz|
ucuzlatmak|v|tr|uçuz|fiyatı düşürmek|OSM19|*ucuz|
paha|n|fa|bahā|değer, fiyat|EAT|bahā|
pahasız|adj|fa|bahā|paha biçilmez|OSM|bahā|
pahalanmak|v|fa|bahā|fiyatı artmak|OSM|bahā|
pahalılaşmak|v|fa|bahā|pahalı duruma gelmek|MOD|bahā|
fiyatlandırmak|v|ar|fiʾāt|fiyat belirlemek|MOD||
tenzil|n|ar|tanzīl|indirme|OSM|N-Z-L|
rayiç|adj|ar|rāʾic|geçerli (fiyat)|OSM19|R-W-C|
revaç|n|ar|rawāc|sürüm, geçerlik|OSM|R-W-C|
tervic|n|ar|tarwīc|sürümünü sağlama, destekleme|OSM|R-W-C|
rağbet|n|ar|raġba|istek, beğeni|EAT|R-G-B|
rağbetli|adj|ar|raġba|beğenilen|OSM|R-G-B|
mergup|adj|ar|marġūb|rağbet edilen|OSM|R-G-B|
kesat|n|ar|kasād|sürümsüzlük|OSM||
kesatlık|n|ar|kasād|durgunluk|OSM19||
durgunluk|n|tr|tur-|hareketsizlik; ekonomik yavaşlama|TDK|*dur-|
buhran|n|ar|buḥrān|bunalım, kriz|OSM19||
panik|n|fr|panique|Pan korkusu|CUM||grc:panikós>fr:panique>tr:panik
balon|n|fr|ballon|şişirilmiş top; aşırı değerlenme|OSM19||it:pallone>fr:ballon>tr:balon
spekülatör|n|fr|spéculateur|gözlemci; vurguncu|CUM|specere|la:speculator>fr:spéculateur>tr:spekülatör
manipülasyon|n|fr|manipulation|elle yönlendirme|MOD|manus|la:manipulus>fr:manipulation>tr:manipülasyon
manifesto|n|it|manifesto|elle vurulmuş; açık bildiri|OSM19|manus|la:manifestus>it:manifesto>tr:manifesto
manüel|adj|fr|manuel|elle yapılan|MOD|manus|la:manualis>fr:manuel>tr:manüel
vurgun|n|tr|ur-|vurma; haksız kazanç|OSM19|*vur-|
vurguncu|n|tr|ur-|vurgun yapan|CUM|*vur-|
vurgunculuk|n|tr|ur-|vurgun yapma|CUM|*vur-|
karaborsa|n|tr|kara borsa|yasa dışı piyasa|CUM||
karaborsacı|n|tr|kara borsa|karaborsada satan|CUM||
ihtikâr|n|ar|iḥtikār|stoklayıp pahalı satma|OSM|H-K-R|
muhtekir|n|ar|muḥtakir|vurguncu|OSM|H-K-R|
fahiş|adj|ar|fāḥiş|aşırı, ölçüsüz|OSM||
stok|n|fr|stock|kütük; yığılmış mal|CUM||en:stock>fr:stock>tr:stok
stokçu|n|fr|stock|mal yığan|MOD||
stokçuluk|n|fr|stock|mal yığma|MOD||
stoklamak|v|fr|stock|mal yığmak|MOD||
envanter|n|fr|inventaire|bulunanlar listesi|CUM||la:inventarium>fr:inventaire>tr:envanter
istif|n|el|stíva|yığın|OSM|stiba|
istifçi|n|el|stíva|mal yığan|OSM19|stiba|
istifçilik|n|el|stíva|mal yığma|CUM|stiba|
istiflemek|v|el|stíva|düzenli yığmak|OSM|stiba|
depolama|n|fr|dépôt|depoya koyma|MOD|ponere|
depocu|n|fr|dépôt|depo işleten|MOD|ponere|
antrepo|n|fr|entrepôt|ara depo|OSM19|ponere|la:interpositum>fr:entrepôt>tr:antrepo
ambarcı|n|fa|anbār|ambar görevlisi|OSM||
silo|n|fr|silo|tahıl deposu|CUM||grc:sirós>es:silo>fr:silo>tr:silo
mağazacılık|n|it|magazzino|büyük dükkân işletme|MOD|H-Z-N|ar:maḫzan>it:magazzino>tr:mağazacılık
hazne|n|ar|ḫazna|depo|OSM|H-Z-N|
hazinedar|n|fa|ḫazīne-dār|hazine görevlisi|OSM|dār-|ar:ḫazīna>fa:ḫazīne-dār>tr:hazinedar
defterdarlık|n|fa|daftar-dār|defterdar makamı|OSM|dār-|
veznedar|n|fa|vazna-dār|kasa görevlisi|OSM19|dār-|ar:wazn>fa:vazna-dār>tr:veznedar
kasadar|n|it|cassa|kasa görevlisi|OSM19|dār-|la:capsa>it:cassa>tr:kasadar
bacdar|n|fa|bāc-dār|baç toplayan|OSM|dār-|
baç|n|fa|bāc|geçiş vergisi|EAT||
sayman|n|tr|sa-|muhasip|DD|*say-|
saymanlık|n|tr|sa-|saymanın görevi|DD|*say-|
Sayıştay|prop|tr|sa-|hesap denetleme kurulu|DD|*say-|
kitabet|n|ar|kitāba|yazıcılık|OSM|K-T-B|
mülkiye|n|ar|mulkiyya|sivil yönetim|OSM19|M-L-K|
temellük|n|ar|tamalluk|mülk edinme|OSM|M-L-K|
emlakçı|n|ar|amlāk|taşınmaz satıcısı|MOD|M-L-K|
akaret|n|ar|ʿaqārāt|gelir getiren mülkler|OSM19||
gayrimenkul|n|ar|ġayr manqūl|taşınmaz|OSM19|N-K-L|
taşınmaz|n|tr|taşı-|gayrimenkul|DD|*taşı-|
taşınır|n|tr|taşı-|menkul|DD|*taşı-|
taşımacı|n|tr|taşı-|nakliyeci|TDK|*taşı-|
taşımacılık|n|tr|taşı-|nakliyat|TDK|*taşı-|
nakliyeci|n|ar|naqliyya|taşımacı|CUM|N-K-L|
nakletmek|v|ar|naql|taşımak, aktarmak|EAT|N-K-L|
hamule|n|ar|ḥamūla|yük|OSM|H-M-L|
tahmil|n|ar|taḥmīl|yükleme|OSM|H-M-L|
mahmul|adj|ar|maḥmūl|yüklenmiş|OSM|H-M-L|
hamallık|n|ar|ḥammāl|hamal işi|OSM|H-M-L|
hamaliye|n|ar|ḥammāliyya|taşıma ücreti|OSM19|H-M-L|
yükleme|n|tr|yük|yük koyma|OSM|*yük-|
yüklü|adj|tr|yük|yükü olan; çok|OSM|*yük-|
yükümlü|adj|tr|yük|borçlu, sorumlu|DD|*yük-|
yükümlülük|n|tr|yük|sorumluluk|DD|*yük-|
boşaltma|n|tr|boş|yükü indirme|OSM|*boş|
navlun|n|ar|nawlūn|gemi taşıma ücreti|OSM||grc:naûlon>ar:nawlūn>tr:navlun
konşimento|n|it|cognoscimento|tanıma belgesi; yük senedi|OSM19||la:cognoscere>it:cognoscimento>tr:konşimento
transit|adj|fr|transit|geçiş|CUM||la:transitus>fr:transit>tr:transit
aktarma|n|tr|aktar-|bir araçtan ötekine geçirme|OSM||
kargo|n|en|cargo|yük|MOD||es:cargo>en:cargo>tr:kargo
avarya|n|it|avaria|gemi ya da yük hasarı|OSM19||ar:ʿawār>it:avaria>tr:avarya
dispeç|n|en|dispatch|hızlı gönderme; avarya hesabı|MOD||
sigortacı|n|it|sicurtà|sigorta işi yapan|CUM|securus|la:securitas>it:sicurtà>tr:sigortacı
sigortalamak|v|it|sicurtà|sigorta ettirmek|CUM|securus|
reasürans|n|fr|réassurance|yeniden sigorta|MOD|securus|
ekspertiz|n|fr|expertise|uzman incelemesi|MOD|experiri|la:expertus>fr:expertise>tr:ekspertiz
eksper|n|fr|expert|uzman|CUM|experiri|la:expertus>fr:expert>tr:eksper
# --- Muhasebe, kazanç, zarar: Arapça kök aileleri ---------------------------------
hesaplaşmak|v|ar|ḥisāb|karşılıklı hesabı görmek|OSM|H-S-B|
hesaplı|adj|ar|ḥisāb|ölçülü, tutumlu|OSM|H-S-B|
hesapsız|adj|ar|ḥisāb|ölçüsüz|OSM|H-S-B|
hesaplama|n|ar|ḥisāb|hesap yapma|CUM|H-S-B|
hasbıhal|n|ar|ḥasb-i ḥāl|duruma göre; söyleşi|OSM|H-S-B|
muhasip|n|ar|muḥāsib|hesap tutan|OSM|H-S-B|
muhasebat|n|ar|muḥāsabāt|hesap işleri|OSM19|H-S-B|
sarfiyat|n|ar|ṣarfiyyāt|harcamalar|OSM19|S-R-F|
masarif|n|ar|maṣārif|giderler|OSM|S-R-F|
israf|n|ar|isrāf|savurganlık|EAT|S-R-F|
müsrif|adj|ar|musrif|savurgan|OSM|S-R-F|
sarraflık|n|ar|ṣarrāf|sarraf işi|OSM|S-R-F|
tasarruflu|adj|ar|taṣarruf|tutumlu|CUM|S-R-F|
hasar|n|ar|ḫasār|ziyan, zarar|OSM||
hüsran|n|ar|ḫusrān|zarara uğrama|OSM||
hasaret|n|ar|ḫasāra|zarar|OSM||
inhisar|n|ar|inḥiṣār|tekel|OSM19|H-S-R|
münhasır|adj|ar|munḥaṣir|sınırlı, özgü|OSM|H-S-R|
mazarrat|n|ar|maḍarra|zarar|OSM|D-R-R|
mutazarrır|adj|ar|mutaḍarrir|zarar gören|OSM|D-R-R|
kesp|n|ar|kasb|kazanç|EAT|K-S-B|
kâsıp|n|ar|kāsib|kazanan; esnaf|OSM|K-S-B|
iktisap|n|ar|iktisāb|edinme|OSM|K-S-B|
müktesep|adj|ar|muktasab|edinilmiş|OSM19|K-S-B|
müktesebat|n|ar|muktasabāt|edinilmiş bilgiler|OSM19|K-S-B|
kazanım|n|tr|kazġan-|edinilen şey|TDK|*kazan-|
kazançlı|adj|tr|kazġan-|kazanç getiren|OSM|*kazan-|
nafaka|n|ar|nafaqa|geçimlik|EAT|N-F-K|
infak|n|ar|infāq|harcama; geçindirme|EAT|N-F-K|
münafık|n|ar|munāfiq|ikiyüzlü|EAT|N-F-K|
selef|n|ar|salaf|önceki; peşin ödeme|OSM|S-L-F|
eslaf|n|ar|aslāf|öncekiler|OSM|S-L-F|
selefi|n|ar|salafī|öncekilere bağlı|OSM19|S-L-F|
selem|n|ar|salam|peşin ödemeli alış|OSM|S-L-M|
vârit|adj|ar|wārid|gelen; akla gelen|OSM|W-R-D|
varidat|n|ar|wāridāt|gelirler|OSM19|W-R-D|
irat|n|ar|īrād|gelir|OSM|W-R-D|
vürut|n|ar|wurūd|geliş|OSM|W-R-D|
deyn|n|ar|dayn|borç|OSM|D-Y-N|
medyun|adj|ar|madyūn|borçlu|OSM|D-Y-N|
dain|n|ar|dāʾin|alacaklı|OSM|D-Y-N|
istidane|n|ar|istidāna|borç alma|OSM|D-Y-N|
merhun|adj|ar|marhūn|rehin bırakılmış|OSM|R-H-N|
mürtehin|n|ar|murtahin|rehin alan|OSM|R-H-N|
rehine|n|ar|rahīna|tutak|OSM19|R-H-N|
kefaletname|n|ar|kafālat-nāme|kefillik belgesi|OSM|K-F-L|
tevkil|n|ar|tawkīl|vekil etme|OSM|W-K-L|
vekâleten|adv|ar|wakālatan|vekil olarak|OSM19|W-K-L|
şirketleşmek|v|ar|şirka|şirket durumuna gelmek|MOD|Ş-R-K|
şeriklik|n|ar|şarīk|ortaklık|OSM|Ş-R-K|
şira|n|ar|şirāʾ|satın alma|OSM|Ş-R-Y|
iştira|n|ar|iştirāʾ|satın alma|OSM|Ş-R-Y|
bayi|n|ar|bāʾiʿ|satıcı|OSM|B-Y-A|
bayilik|n|ar|bāʾiʿ|satıcılık|CUM|B-Y-A|
mebi|n|ar|mabīʿ|satılan|OSM|B-Y-A|
mübayaa|n|ar|mubāyaʿa|satın alma|OSM|B-Y-A|
biat|n|ar|bayʿa|bağlılık bildirme|EAT|B-Y-A|
ameliye|n|ar|ʿamaliyya|işlem|OSM19|A-M-L|
muamelat|n|ar|muʿāmalāt|işlemler|OSM19|A-M-L|
âmil|n|ar|ʿāmil|iş yapan; etken|OSM|A-M-L|
imal|n|ar|iʿmāl|işletme, yapma|OSM|A-M-L|
imalat|n|ar|iʿmālāt|yapımlar|OSM19|A-M-L|
imalatçı|n|ar|iʿmālāt|üretici|CUM|A-M-L|
imalathane|n|ar|iʿmālāt-ḫāne|üretim yeri|OSM19|-hāne|ar:iʿmālāt>fa:iʿmālāt-ḫāne>tr:imalathane
nakdi|adj|ar|naqdī|nakit olarak|OSM19|N-K-D|
nükut|n|ar|nuqūd|paralar|OSM|N-K-D|
tezkiye|n|ar|tazkiya|arıtma; aklama|OSM||
cibayet|n|ar|cibāya|vergi toplama|OSM|C-B-Y|
cabi|n|ar|cābī|vergi toplayan|OSM|C-B-Y|
# --- Vergi ve Osmanlı maliyesi --------------------------------------------------
haraç|n|ar|ḫarāc|toprak vergisi|EAT|H-R-C|
harcama|n|ar|ḫarc|para sarfı|CUM|H-R-C|
harcırah|n|ar|ḫarc-i rāh|yol gideri|OSM|H-R-C|
harcıâlem|adj|ar|ḫarc-i ʿālam|herkesin kullandığı|OSM|H-R-C|
ihracatçı|n|ar|iḫrācāt|dışarıya mal satan|CUM|H-R-C|
ithal|n|ar|idḫāl|içeri sokma|OSM19|D-H-L|
ithalatçı|n|ar|idḫālāt|dışarıdan mal getiren|CUM|D-H-L|
dahil|adj|ar|dāḫil|içinde|EAT|D-H-L|
dahili|adj|ar|dāḫilī|içe ilişkin|OSM|D-H-L|
müdahale|n|ar|mudāḫala|karışma|OSM19|D-H-L|
medhal|n|ar|madḫal|giriş|OSM|D-H-L|
öşür|n|ar|ʿuşr|onda bir|EAT|A-Ş-R|
aşar|n|ar|aʿşār|onda birler|OSM|A-Ş-R|
âşir|n|ar|ʿāşir|öşür toplayan|OSM|A-Ş-R|
aşari|adj|ar|ʿaşārī|ondalık|OSM19|A-Ş-R|
muaşeret|n|ar|muʿāşara|birlikte yaşama|OSM|A-Ş-R|
aşiret|n|ar|ʿaşīra|kabile|EAT|A-Ş-R|
cizye|n|ar|cizya|gayrimüslim baş vergisi|EAT||
gümrükçü|n|el|kommérkion|gümrük görevlisi|OSM|merx|la:commercium>el:kommérkion>tr:gümrükçü
gümrükleme|n|el|kommérkion|gümrük işlemi|MOD|merx|
gümrüklü|adj|el|kommérkion|gümrüğü ödenmiş|OSM19|merx|
merkantilizm|n|fr|mercantilisme|ticaretçilik|CUM|merx|la:mercari>it:mercante>fr:mercantilisme>tr:merkantilizm
merkantilist|adj|fr|mercantiliste|merkantilizm yanlısı|CUM|merx|
hipermarket|n|fr|hypermarché|büyük market|NEW|merx|
kaçakçı|n|tr|kaç-|kaçak mal taşıyan|OSM19|*kaç-|
kaçakçılık|n|tr|kaç-|kaçak mal ticareti|CUM|*kaç-|
iltizam|n|ar|iltizām|üstlenme; vergi toplama hakkı|OSM|L-Z-M|
mültezim|n|ar|multazim|iltizam sahibi|OSM|L-Z-M|
elzem|adj|ar|alzam|çok gerekli|OSM|L-Z-M|
lüzumlu|adj|ar|luzūm|gerekli|OSM|L-Z-M|
mülazım|n|ar|mulāzim|yanından ayrılmayan; teğmen|OSM|L-Z-M|
tımar|n|fa|tīmār|bakım; dirlik|EAT|tīmār|
tımarlı|adj|fa|tīmār|tımar sahibi|OSM|tīmār|
dirlik|n|tr|tirig|geçimlik; tımar|EAT||
zeamet|n|ar|zaʿāma|önderlik; büyük dirlik|OSM|Z-A-M|
zaim|n|ar|zaʿīm|önder; zeamet sahibi|OSM|Z-A-M|
has|n|ar|ḫāṣṣ|özel; padişah dirliği|OSM|H-S-S|
hassa|n|ar|ḫāṣṣa|özel; padişaha ait|OSM|H-S-S|
husus|n|ar|ḫuṣūṣ|özel durum, konu|OSM|H-S-S|
hususi|adj|ar|ḫuṣūṣī|özel|OSM|H-S-S|
hususiyet|n|ar|ḫuṣūṣiyya|özellik|OSM|H-S-S|
mahsus|adj|ar|maḫṣūṣ|özgü|EAT|H-S-S|
tahsis|n|ar|taḫṣīṣ|ayırma|OSM|H-S-S|
tahsisat|n|ar|taḫṣīṣāt|ayrılan ödenek|OSM19|H-S-S|
mukataa|n|ar|muqāṭaʿa|kesime verilen gelir|OSM|K-T-A|
avarız|n|ar|ʿawāriḍ|olağanüstü vergi|OSM|A-R-D|
arızi|adj|ar|ʿāriḍī|geçici, rastlantısal|OSM|A-R-D|
rüsum|n|ar|rusūm|resimler, harçlar|OSM|R-S-M|
vergilendirme|n|tr|ber-|vergi koyma|TDK|*ver-|
vergilendirmek|v|tr|ber-|vergi koymak|TDK|*ver-|
salyane|n|fa|sāliyāna|yıllık ödenek|OSM||
ulufe|n|ar|ʿulūfa|yem; asker maaşı|OSM||
mevacip|n|ar|mawācib|maaşlar|OSM|W-C-B|
vacip|adj|ar|wācib|gerekli|EAT|W-C-B|
icap|n|ar|īcāb|gerekme|OSM|W-C-B|
mucip|adj|ar|mūcib|gerektiren|OSM|W-C-B|
vücup|n|ar|wucūb|gereklilik|OSM|W-C-B|
tamga|n|tr|tamga|damga; vergi mührü|ORH|*tamga|
damgalamak|v|tr|tamga|damga vurmak|OSM|*tamga|
damgalı|adj|tr|tamga|damga vurulmuş|OSM|*tamga|
kesenek|n|tr|kes-|aidat|TDK|*kes-|
aidat|n|ar|ʿāʾidāt|gelirler; üyelik ödentisi|OSM19|A-W-D|
iade|n|ar|iʿāda|geri verme|OSM|A-W-D|
iadeli|adj|ar|iʿāda|iade edilen|MOD|A-W-D|
avdet|n|ar|ʿawda|dönüş|OSM|A-W-D|
mutat|adj|ar|muʿtād|alışılmış|OSM|A-W-D|
itiyat|n|ar|iʿtiyād|alışkanlık|OSM|A-W-D|
mükellef|adj|ar|mukallaf|yükümlü|OSM|K-L-F|
mükellefiyet|n|ar|mukallafiyya|yükümlülük|OSM19|K-L-F|
teklif|n|ar|taklīf|yükleme; öneri|OSM|K-L-F|
külfet|n|ar|kulfa|zahmet|OSM|K-L-F|
tekellüf|n|ar|takalluf|zahmete girme|OSM|K-L-F|
tekâlif|n|ar|takālīf|vergiler|OSM|K-L-F|
beyanat|n|ar|bayānāt|açıklamalar|OSM19|B-Y-N|
tebyin|n|ar|tabyīn|açıklama|OSM|B-Y-N|
mübeyyin|adj|ar|mubayyin|açıklayan|OSM|B-Y-N|
istisna|n|ar|istiṯnāʾ|ayrı tutma|OSM|S-N-Y|
istisnai|adj|ar|istiṯnāʾī|ayrıksı|OSM19|S-N-Y|
müstesna|adj|ar|mustaṯnā|ayrı tutulmuş|OSM|S-N-Y|
matrah|n|ar|maṭraḥ|atılan yer; vergi tabanı|OSM19|T-R-H|
tarh|n|ar|ṭarḥ|atma; vergi koyma; çıkarma|OSM|T-R-H|
tarhiyat|n|ar|ṭarḥiyyāt|vergi koyma işlemleri|CUM|T-R-H|
stopaj|n|fr|stoppage|durdurma; kaynakta kesinti|MOD||
tevkif|n|ar|tawqīf|durdurma; tutuklama|OSM|W-K-F|
tevkifat|n|ar|tawqīfāt|kesintiler|OSM19|W-K-F|
vakıf|n|ar|waqf|durdurma; hayır kurumu|EAT|W-K-F|
vakfiye|n|ar|waqfiyya|vakıf belgesi|OSM|W-K-F|
vâkıf|adj|ar|wāqif|bilen; vakfeden|OSM|W-K-F|
vakfetmek|v|ar|waqf|adamak|OSM|W-K-F|
mevkuf|adj|ar|mawqūf|durdurulmuş; tutuklu|OSM|W-K-F|
evkaf|n|ar|awqāf|vakıflar|OSM|W-K-F|
tevakkuf|n|ar|tawaqquf|durma, bekleme|OSM|W-K-F|
denge|n|tr|teŋ|eşit ağırlık durumu|DD|*teng|
dengeli|adj|tr|teŋ|dengesi olan|DD|*teng|
denklik|n|tr|teŋ|eşitlik|TDK|*teng|
denkleştirmek|v|tr|teŋ|eşitlemek|TDK|*teng|
zenginlik|n|fa|sangīn|varlıklı olma|OSM||
varlıklı|adj|tr|bar|zengin|OSM|*var-|
varsıl|adj|tr|bar|zengin|DD|*var-|
fakirlik|n|ar|faqīr|yoksulluk|OSM||
yoksulluk|n|tr|yok|yoksul olma|DD||
sefil|adj|ar|safīl|alçak; düşkün|OSM|S-F-L|
esfel|adj|ar|asfal|en alçak|OSM|S-F-L|
süfli|adj|ar|suflī|aşağılık|OSM|S-F-L|
refah|n|ar|rafāh|bolluk, gönenç|OSM|R-F-H|
müreffeh|adj|ar|muraffah|gönençli|OSM19|R-F-H|
terfih|n|ar|tarfīh|gönendirme|OSM|R-F-H|
bolluk|n|tr|bol|çokluk|OSM||
kıt|adj|tr|kıt|az, yetersiz|DLT||
bereketli|adj|ar|baraka|bol, verimli|EAT|B-R-K|
ferah|adj|ar|faraḥ|sevinç; geniş|EAT|F-R-H|
ferahlamak|v|ar|faraḥ|rahatlamak|OSM|F-R-H|
ferahlık|n|ar|faraḥ|genişlik; rahatlık|OSM|F-R-H|
darlık|n|tr|tar|sıkıntı; geçim güçlüğü|OSM||
sıkıntı|n|tr|sık-|darlık|OSM||
geçimlik|n|tr|keç-|geçinmeye yetecek kadar|OSM|*geç-|
geçindirmek|v|tr|keç-|geçimini sağlamak|OSM|*geç-|
satım|n|tr|sat-|satma|OSM|*sat-|
satılık|adj|tr|sat-|satışa çıkarılmış|OSM|*sat-|
kiralık|adj|ar|kirāʾ|kiraya verilecek|OSM||
kiralamak|v|ar|kirāʾ|kira ile tutmak|OSM19||
yevmiye|n|ar|yawmiyya|günlük|OSM|Y-W-M|
eyyam|n|ar|ayyām|günler|OSM|Y-W-M|
hakediş|n|tr|hak ediş|yapılan iş karşılığı ödeme|MOD||
bahşetmek|v|fa|baḫşīdan|bağışlamak|OSM||
peşinat|n|fa|pīşīn|ön ödeme|MOD||
taksitli|adj|ar|taqsīṭ|taksitle ödenen|MOD|K-S-T|
kıst|n|ar|qisṭ|pay; adalet|OSM|K-S-T|
kıymetli|adj|ar|qīma|değerli|OSM|K-W-M|
kıymetsiz|adj|ar|qīma|değersiz|OSM|K-W-M|
değersiz|adj|tr|teg-|değeri olmayan|OSM|*değ-|
değerleme|n|tr|teg-|değer biçme|TDK|*değ-|
değerlendirmek|v|tr|teg-|değer biçmek; yararlanmak|TDK|*değ-|
ehven|adj|ar|ahwan|daha ucuz, daha kolay|OSM||
# --- İktisat bilimi ve çağdaş ekonomi terimleri ---------------------------------
iktisadi|adj|ar|iqtiṣādī|ekonomiye ilişkin|OSM19|K-S-D|
iktisadiyat|n|ar|iqtiṣādiyyāt|ekonomi bilimi|OSM19|K-S-D|
iktisatçı|n|ar|iqtiṣād|ekonomist|CUM|K-S-D|
ekonomik|adj|fr|économique|ekonomiye ilişkin|CUM|oikos|grc:oikonomikós>fr:économique>tr:ekonomik
ekonomist|n|fr|économiste|ekonomi bilgini|CUM|oikos|grc:oikonomía>fr:économiste>tr:ekonomist
ekonometri|n|fr|économétrie|ekonomi ölçümü|MOD|oikos|
deflasyon|n|fr|déflation|havasını alma; fiyat düşüşü|MOD|flare|la:deflatio>fr:déflation>tr:deflasyon
stagflasyon|n|en|stagflation|durgunluk içinde enflasyon|MOD|flare|
devalüasyon|n|fr|dévaluation|değer düşürme|MOD|valere|la:valere>fr:dévaluation>tr:devalüasyon
revalüasyon|n|fr|réévaluation|değer yükseltme|MOD|valere|
valör|n|fr|valeur|değer; faiz başlangıç tarihi|MOD|valere|la:valor>fr:valeur>tr:valör
resesyon|n|fr|récession|geri çekilme|MOD||la:recessio>fr:récession>tr:resesyon
kota|n|fr|quota|pay|MOD||la:quota>fr:quota>tr:kota
kontenjan|n|fr|contingent|pay, sınırlı sayı|CUM||la:contingens>fr:contingent>tr:kontenjan
sübvansiyon|n|fr|subvention|yardım, destek|MOD||la:subventio>fr:subvention>tr:sübvansiyon
damping|n|en|dumping|boşaltma; ucuza mal sürme|MOD||
teşvik|n|ar|taşwīq|isteklendirme|OSM|Ş-W-K|
şevk|n|ar|şawq|istek, coşku|EAT|Ş-W-K|
müşevvik|n|ar|muşawwiq|özendiren|OSM|Ş-W-K|
istihdam|n|ar|istiḫdām|hizmette kullanma|OSM19|H-D-M|
hizmetli|n|ar|ḫidma|hizmet gören|CUM|H-D-M|
işsiz|adj|tr|iş|işi olmayan|OSM|*iş|
işsizlik|n|tr|iş|iş bulamama|CUM|*iş|
işçilik|n|tr|iş|işçi emeği|OSM19|*iş|
işletmeci|n|tr|iş|işletme yöneten|MOD|*iş|
işletmecilik|n|tr|iş|işletme yönetimi|MOD|*iş|
işlik|n|tr|iş|atölye|DD|*iş|
verimli|adj|tr|ber-|çok ürün veren|DD|*ver-|
verimsiz|adj|tr|ber-|az ürün veren|DD|*ver-|
verimlilik|n|tr|ber-|üretkenlik|TDK|*ver-|
üretken|adj|tr|ür-|çok üreten|DD|*ür-|
üretkenlik|n|tr|ür-|üretme gücü|TDK|*ür-|
tüketim|n|tr|tüke-|kullanıp bitirme|DD|*tüke-|
tükenmek|v|tr|tüke-|bitmek|DLT|*tüke-|
tükenmez|adj|tr|tüke-|bitmeyen|OSM|*tüke-|
dağıtım|n|tr|tagıt-|dağıtma işi|DD|*dağıl-|
dağıtıcı|n|tr|tagıt-|dağıtan|TDK|*dağıl-|
hammadde|n|fa|ḫām mādda|işlenmemiş madde|CUM|M-D-D|
sanayici|n|ar|ṣanāʾiʿ|sanayi işletmecisi|CUM|S-N-A|
sanayileşmek|v|ar|ṣanāʾiʿ|sanayi ülkesi olmak|MOD|S-N-A|
sanayileşme|n|ar|ṣanāʾiʿ|sanayileşmek işi|MOD|S-N-A|
endüstri|n|fr|industrie|çalışkanlık; sanayi|CUM|struere|la:industria>fr:industrie>tr:endüstri
endüstriyel|adj|fr|industriel|sanayiye ilişkin|MOD|struere|
endüstrileşme|n|fr|industrie|sanayileşme|MOD|struere|
teşebbüs|n|ar|taşabbuṯ|tutunma; girişim|OSM19||
girişimcilik|n|tr|kir-|girişimci olma|MOD|*gir-|
kooperatif|n|fr|coopératif|birlikte çalışan|CUM|opus|la:cooperari>fr:coopératif>tr:kooperatif
kooperatifçi|n|fr|coopératif|kooperatif üyesi|CUM|opus|
operasyon|n|fr|opération|işlem; harekât|CUM|opus|la:operatio>fr:opération>tr:operasyon
holding|n|en|holding|elinde tutan şirket|MOD||
limited|adj|en|limited|sınırlı|MOD||la:limes>en:limited>tr:limited
ortaklık|n|tr|orta|ortak olma|OSM||
ortaklaşa|adv|tr|orta|ortak olarak|TDK||
patronluk|n|fr|patron|patron olma|CUM|pater|
patronaj|n|fr|patronage|koruyuculuk|MOD|pater|la:patronus>fr:patronage>tr:patronaj
emekçi|n|tr|emgek|emeğiyle geçinen|DD||
ücretli|adj|ar|ucra|ücret alan|OSM19|A-C-R|
ücretsiz|adj|ar|ucra|karşılıksız|CUM|A-C-R|
icar|n|ar|īcār|kiraya verme|OSM|A-C-R|
ecir|n|ar|acr|karşılık, sevap|EAT|A-C-R|
isticar|n|ar|istiʾcār|kiralama|OSM|A-C-R|
müstecir|n|ar|mustaʾcir|kiracı|OSM19|A-C-R|
maaşlı|adj|ar|maʿāş|maaş alan|OSM19|A-Y-Ş|
maişet|n|ar|maʿīşa|geçim|OSM|A-Y-Ş|
iaşe|n|ar|iʿāşa|yedirip içirme|OSM19|A-Y-Ş|
asgari|adj|ar|aṣġarī|en küçük|OSM19|S-G-R|
tasgir|n|ar|taṣġīr|küçültme|OSM|S-G-R|
sagir|adj|ar|ṣaġīr|küçük|OSM|S-G-R|
azami|adj|ar|aʿẓamī|en büyük|OSM19||
sendikacı|n|fr|syndicat|sendika yöneticisi|MOD|dikē|grc:sýndikos>fr:syndicat>tr:sendikacı
sendikal|adj|fr|syndical|sendikaya ilişkin|MOD|dikē|
grevci|n|fr|grève|grev yapan|CUM||
lokavt|n|en|lockout|işveren kapatması|MOD||
mesai|n|ar|masāʿī|çalışmalar|OSM19||
kıdem|n|ar|qidam|öncelik, eskilik|OSM|K-D-M|
kıdemli|adj|ar|qidam|eski, deneyimli|OSM19|K-D-M|
kadim|adj|ar|qadīm|eski|EAT|K-D-M|
takdim|n|ar|taqdīm|sunma|OSM|K-D-M|
mukaddem|adj|ar|muqaddam|önce gelen|OSM|K-D-M|
kadem|n|ar|qadam|ayak; ayak ölçüsü|OSM|K-D-M|
yüzdelik|adj|tr|yüz|yüzde oranı|TDK||
bileşik|adj|tr|bir|birleşmiş (faiz)|DD||
kamu|n|tr|kamuġ|hep, bütün; halk|ORH|*kamu|
kamulaştırma|n|tr|kamuġ|kamuya geçirme|DD|*kamu|
kamulaştırmak|v|tr|kamuġ|kamuya geçirmek|DD|*kamu|
özelleştirme|n|tr|öz|özel kesime devretme|MOD|*öz|
özelleştirmek|v|tr|öz|özel kesime devretmek|MOD|*öz|
sektör|n|fr|secteur|kesim|MOD|secare|la:sector>fr:secteur>tr:sektör
sektörel|adj|fr|sectoriel|kesime ilişkin|NEW|secare|
seksiyon|n|fr|section|bölüm|CUM|secare|la:sectio>fr:section>tr:seksiyon
marj|n|fr|marge|kenar; kâr payı|MOD|margo|la:margo>fr:marge>tr:marj
marjinal|adj|fr|marginal|kenarda olan|MOD|margo|
liberal|adj|fr|libéral|özgürlükçü|OSM19|liber|la:liberalis>fr:libéral>tr:liberal
liberalizm|n|fr|libéralisme|özgürlükçülük|CUM|liber|
liberalleşme|n|fr|libéral|serbestleşme|MOD|liber|
sosyalizm|n|fr|socialisme|toplumculuk|OSM19|socius|la:socius>fr:socialisme>tr:sosyalizm
sosyalist|n|fr|socialiste|toplumcu|OSM19|socius|
sosyete|n|fr|société|toplum; seçkinler|OSM19|socius|la:societas>fr:société>tr:sosyete
kolektif|adj|fr|collectif|ortaklaşa|CUM|legere|la:collectivus>fr:collectif>tr:kolektif
koleksiyon|n|fr|collection|derleme|CUM|legere|la:collectio>fr:collection>tr:koleksiyon
kolektivizm|n|fr|collectivisme|ortaklaşacılık|MOD|legere|
fizyokrat|n|fr|physiocrate|doğa egemenliği yanlısı|CUM|kratos|grc:phýsis>fr:physiocrate>tr:fizyokrat
planlama|n|fr|plan|tasarlama|MOD||
boykot|n|en|boycott|dışlama|CUM||
blokaj|n|fr|blocage|dondurma|MOD|bloc|
bloke|adj|fr|bloqué|dondurulmuş|MOD|bloc|
büyüme|n|tr|bedü-|gelişme; ekonomik genişleme|OSM||
kalkınmak|v|tr|kalk-|gelişmek|DD|*kalk-|
istikrar|n|ar|istiqrār|yerleşme; kararlılık|OSM19|K-R-R|
dalgalanma|n|tr|talga|iniş çıkış|TDK||
esneklik|n|tr|esne-|bükülebilirlik|TDK||
finans|n|fr|finance|ödeme; para işleri|CUM|finis|la:finis>fr:finance>tr:finans
finansman|n|fr|financement|para sağlama|MOD|finis|
finansal|adj|fr|finance|para işlerine ilişkin|MOD|finis|
finansör|n|fr|financier|para sağlayan|MOD|finis|
finanse|adj|fr|financé|para sağlanmış|MOD|finis|
final|n|fr|final|son|CUM|finis|la:finalis>fr:final>tr:final
turizm|n|fr|tourisme|gezi işletmeciliği|CUM|tornos|grc:tórnos>fr:tourisme>tr:turizm
turist|n|fr|touriste|gezgin|CUM|tornos|
tur|n|fr|tour|dönüş; gezi|CUM|tornos|
turne|n|fr|tournée|sanatçı gezisi|CUM|tornos|
fuar|n|fr|foire|panayır|CUM|feria|la:feria>fr:foire>tr:fuar
fuarcılık|n|fr|foire|fuar düzenleme işi|NEW|feria|
sergileme|n|tr|ser-|sergi düzenleme|TDK|*ser-|
sergici|n|tr|ser-|sergi açan|TDK|*ser-|
tekelci|n|tr|tek el|tekel kuran|MOD|*tek|
tekelcilik|n|tr|tek el|tekel kurma|MOD|*tek|
oligopol|n|fr|oligopole|az satıcılı piyasa|MOD|pōlein|grc:olígoi>fr:oligopole>tr:oligopol
monopol|n|fr|monopole|tek satıcılı piyasa|CUM|pōlein|grc:monopṓlion>fr:monopole>tr:monopol
kartel|n|fr|cartel|yazılı anlaşma; şirket birliği|CUM|charta|la:charta>it:cartello>fr:cartel>tr:kartel
kartela|n|it|cartella|örnek kartı|CUM|charta|la:charta>it:cartella>tr:kartela
tröst|n|en|trust|güven; şirket birliği|CUM||
rekabetçi|adj|ar|raqāba|yarışmacı|MOD|R-K-B|
murakabe|n|ar|murāqaba|denetleme|OSM|R-K-B|
merkep|n|ar|markab|binek; eşek|OSM|R-K-B|
reklamcı|n|fr|réclame|reklam yapan|CUM|clamare|
reklamcılık|n|fr|réclame|reklam işi|MOD|clamare|
deklarasyon|n|fr|déclaration|bildirge|CUM|clamare|la:declaratio>fr:déclaration>tr:deklarasyon
markalı|adj|it|marca|markası olan|MOD||
markalaşma|n|it|marca|marka olma|NEW||
patent|n|fr|patente|açık (belge)|OSM19||la:patens>fr:patente>tr:patent
lisans|n|fr|licence|izin|CUM||la:licentia>fr:licence>tr:lisans
lisanslı|adj|fr|licence|izinli|MOD||
imtiyazlı|adj|ar|imtiyāz|ayrıcalıklı|OSM19|M-Y-Z|
ruhsatlı|adj|ar|ruḫṣa|izinli|OSM19|R-H-S|
ruhsatsız|adj|ar|ruḫṣa|izinsiz|CUM|R-H-S|
ruhsatname|n|ar|ruḫṣat-nāme|izin belgesi|OSM|-nāme|
standart|n|en|standard|ölçün|CUM||fro:estandart>en:standard>tr:standart
standartlaşma|n|en|standard|ölçünleşme|MOD||
kaliteli|adj|fr|qualité|nitelikli|CUM|qualis|
kalitesiz|adj|fr|qualité|niteliksiz|CUM|qualis|
kalifiye|adj|fr|qualifié|nitelikli|MOD|qualis|
garanti|n|fr|garantie|güvence|CUM||ger:warjan>fr:garantie>tr:garanti
garantili|adj|fr|garantie|güvenceli|MOD||
servis|n|fr|service|hizmet|CUM|servus|la:servitium>fr:service>tr:servis
serf|n|fr|serf|toprak kölesi|CUM|servus|la:servus>fr:serf>tr:serf
köle|n|tr?|küle|tutsak hizmetçi|EAT||
kölelik|n|tr?|küle|köle olma|OSM||
esir|n|ar|asīr|tutsak|EAT||
esaret|n|ar|asāra|tutsaklık|OSM||
ganimet|n|ar|ġanīma|savaşta ele geçirilen mal|EAT||
yağma|n|tr|yaġma|talan|EAT||
yağmacı|n|tr|yaġma|yağma yapan|OSM||
talan|n|fa|tālān|yağma|OSM||
talancı|n|fa|tālān|yağmacı|OSM||
çapul|n|tr|çap-|yağma|OSM|*çap-|
çapulcu|n|tr|çap-|yağmacı|OSM|*çap-|
çapkın|adj|tr|çap-|hızlı koşan; hovarda|OSM|*çap-|
hibe|n|ar|hiba|bağış|OSM||
teberru|n|ar|tabarruʿ|gönüllü bağış|OSM||
iane|n|ar|iʿāna|yardım parası|OSM19|A-W-N|
caize|n|ar|cāʾiza|armağan, bahşiş|OSM|C-W-Z|
atiye|n|ar|ʿaṭiyya|bağış|OSM||
lütuf|n|ar|luṭf|iyilik|EAT|L-T-F|
latif|adj|ar|laṭīf|hoş, ince|EAT|L-T-F|
lütufkâr|adj|ar|luṭf|iyiliksever|OSM|L-T-F|
mültefit|adj|ar|multafit|ilgi gösteren|OSM|L-T-F|
sehavet|n|ar|saḫāwa|cömertlik|OSM|S-H-W|
sahi|adj|ar|saḫī|cömert|OSM|S-H-W|
cömertlik|n|fa|cuvānmard|eli açıklık|OSM||
cimrilik|n|fa|cimrī|eli sıkılık|OSM||
hasislik|n|ar|ḫasīs|cimrilik|OSM||
savurgan|adj|tr|savur-|çok harcayan|DD||
savurganlık|n|tr|savur-|israf|DD||
tutumlu|adj|tr|tut-|idareli|DD|*tut-|
idareli|adj|ar|idāra|tutumlu|OSM19|D-W-R|
hayrat|n|ar|ḫayrāt|hayır işleri|OSM|H-Y-R|
destek|n|fa|dastak|küçük el; dayanak|OSM|dast|
destekli|adj|fa|dastak|desteği olan|MOD|dast|
dest|n|fa|dast|el|OSM|dast|
fon|n|fr|fonds|dip; para kaynağı|CUM|fundus|la:fundus>fr:fonds>tr:fon
fonlamak|v|fr|fonds|fon sağlamak|NEW|fundus|
sponsor|n|en|sponsor|kefil; destekçi|NEW||la:sponsor>en:sponsor>tr:sponsor
sponsorluk|n|en|sponsor|destekçilik|NEW||
promosyon|n|fr|promotion|ileri götürme; tanıtım|MOD|movere|la:promotio>fr:promotion>tr:promosyon
abone|n|fr|abonné|sürekli alıcı|OSM19||
abonman|n|fr|abonnement|abonelik|CUM||
proletarya|n|fr|prolétariat|işçi sınıfı|CUM||la:proletarius>fr:prolétariat>tr:proletarya
burjuva|n|fr|bourgeois|kentli; orta sınıf üyesi|CUM||ger:burg>fr:bourgeois>tr:burjuva
burjuvazi|n|fr|bourgeoisie|orta sınıf|CUM||
kapora|n|it|caparra|pey akçesi|OSM19||
pey|n|fa|pay|iz; ön ödeme|OSM|pā|
net|adj|fr|net|temiz; kesintisiz|CUM||la:nitidus>fr:net>tr:net
brüt|adj|fr|brut|işlenmemiş; kesintisiz|CUM||la:brutus>fr:brut>tr:brüt
reel|adj|fr|réel|gerçek|MOD||la:realis>fr:réel>tr:reel
arbitraj|n|fr|arbitrage|hakemlik; fiyat farkından yararlanma|MOD||la:arbiter>fr:arbitrage>tr:arbitraj
leasing|n|en|leasing|kiralama|NEW||
faktoring|n|en|factoring|alacak satışı|NEW|facere|la:factor>en:factoring>tr:faktoring
amortisman|n|fr|amortissement|yıpranma payı|CUM||la:mors>fr:amortissement>tr:amortisman
denetim|n|tr|tene-|kontrol|DD||
denetçi|n|tr|tene-|kontrol eden|DD||
# --- Ölçü ve tartı ------------------------------------------------------------
kantar|n|ar|qinṭār|yüz rıtl; büyük terazi|EAT||la:centenarium>ar:qinṭār>tr:kantar
kantarcı|n|ar|qinṭār|kantar tartan|OSM||
kantariye|n|ar|qinṭāriyya|tartı ücreti|OSM||
terazi|n|fa|tarāzū|tartı|EAT||
tevzin|n|ar|tawzīn|dengeleme|OSM|W-Z-N|
mevzun|adj|ar|mawzūn|ölçülü, düzgün|OSM|W-Z-N|
tartı|n|tr|tart-|ağırlık ölçme|OSM|*tart-|
tartıcı|n|tr|tart-|tartan|OSM19|*tart-|
okka|n|ar|ūqiyya|ağırlık birimi|EAT||la:uncia>ar:ūqiyya>tr:okka
okkalı|adj|ar|ūqiyya|ağır; iri|OSM19||
kıyye|n|ar|ūqiyya|okka|OSM||
arşın|n|tr?|arşun|uzunluk ölçüsü|EAT||
arşınlamak|v|tr?|arşun|büyük adımlarla ölçmek|OSM19||
endaze|n|fa|andāza|ölçü|EAT||
kile|n|ar|kayl|tahıl ölçeği|EAT||
batman|n|tr|batman|ağırlık birimi|DLT||
dönüm|n|tr|tön-|alan ölçüsü|OSM|*dön-|
çeki|n|tr|çek-|odun ağırlık birimi|OSM|*çek-|
miskal|n|ar|miṯqāl|ağırlık birimi|EAT|S-K-L|
sıklet|n|ar|ṯiqla|ağırlık|OSM|S-K-L|
sakil|adj|ar|ṯaqīl|ağır; kaba|OSM|S-K-L|
müd|n|ar|mudd|tahıl ölçeği|OSM||
şinik|n|el|khoînix|tahıl ölçeği|OSM||
evlek|n|el|aulákion|tarla bölümü|OSM||
fersah|n|fa|farsang|uzunluk ölçüsü|EAT||
karış|n|tr|karış|el açıklığı ölçüsü|DLT||
kulaç|n|tr|kulaç|açılmış kol ölçüsü|DLT||
parmak|n|tr|barmak|el parmağı; ölçü birimi|ORH||
gram|n|fr|gramme|küçük ağırlık|OSM19|graphein|grc:grámma>fr:gramme>tr:gram
kilogram|n|fr|kilogramme|bin gram|OSM19|graphein|
ton|n|fr|tonne|fıçı; bin kilo|OSM19||
litre|n|fr|litre|hacim ölçüsü|OSM19||grc:lítra>fr:litre>tr:litre
hektar|n|fr|hectare|yüz ar|CUM||
mil|n|en|mile|bin adım|OSM19|mille|la:mille>en:mile>tr:mil
milimetre|n|fr|millimètre|binde bir metre|OSM19|mille|
ölçüm|n|tr|ölç-|ölçme işi|TDK||
desi|n|fr|déci|onda bir|MOD||
"""

FAMILIES = r"""
# --- Arapça üçlü kökler: ticaret, kazanç, borç ---
M-T-A|ar|yararlanmak|Arapça m-t-ʿ kökü; metâ (yararlanılan mal), emtia (mallar) ve temettü (kâr payı) aynı kökten türer.
K-S-B|ar|kazanmak|Arapça k-s-b kökü; kesp (kazanç), kâsıp (kazanan), iktisap (edinme), müktesep ve müktesebat aynı kökten gelir.
R-B-H|ar|kâr etmek|Arapça r-b-ḥ kökü; ribh (kâr), rabıh (kârlı) ve murabaha (kârla satış) aynı kökten türer.
N-F-K|ar|harcamak, tüketmek|Arapça n-f-q kökü; nafaka (geçimlik), infak (harcama) ve münafık (iki yüzü tüketen) aynı kökten gelir.
S-L-F|ar|önce olmak; peşin vermek|Arapça s-l-f kökü; selef (önceki; peşin ödeme), eslaf (öncekiler) ve selefi aynı kökten türer.
W-R-D|ar|gelmek, ulaşmak|Arapça w-r-d kökü; vârit (gelen), varidat (gelirler), irat (gelir) ve vürut (geliş) aynı kökten gelir.
D-Y-N|ar|borç|Arapça d-y-n kökü; deyn (borç), medyun (borçlu), dain (alacaklı) ve istidane (borç alma) aynı kökten türer.
R-H-N|ar|rehin bırakmak|Arapça r-h-n kökü; rehin, merhun (rehinli), mürtehin (rehin alan) ve rehine (tutak) aynı kökten gelir.
Ş-R-Y|ar|satın almak|Arapça ş-r-y kökü; şira ve iştira (satın alma) aynı kökten gelir; müşteri de bu kökle ilişkilidir.
B-Y-A|ar|satmak; bağlılık sözü vermek|Arapça b-y-ʿ kökü; bayi (satıcı), mebi (satılan), mübayaa (satın alma) ve biat (el sıkışarak bağlanma) aynı kökten türer.
S-K-K|ar|damga kalıbı|Arapça s-k-k kökü; sikke (basılmış para), meskûk (basılmış) ve sikkezen (para basan) aynı kökten gelir.
C-B-Y|ar|vergi toplamak|Arapça c-b-y kökü; cibayet (vergi toplama) ve cabi (vergi toplayan) aynı kökten türer.
A-Ş-R|ar|on; birlikte yaşamak|Arapça ʿ-ş-r kökü; öşür (onda bir), aşar, âşir, aşari (ondalık) ile muaşeret ve aşiret (birlikte yaşayan topluluk) aynı kökten gelir.
K-B-D|ar|tutmak, almak|Arapça q-b-ḍ kökü; kabz (alma), makbuz (alınmış; alındı), kabzımal ve kabzetmek aynı kökten türer.
A-D-Y|ar|yerine getirmek|Arapça ʾ-d-y kökü; eda (yerine getirme), tediye (ödeme) ve edat (araç) aynı kökten gelir.
W-D-A|ar|bırakmak, emanet etmek|Arapça w-d-ʿ kökü; tevdi (emanet etme), mevduat (bırakılan paralar), mudi, tevdiat, vedia (emanet) ve veda (bırakıp ayrılma) aynı kökten türer.
K-R-D|ar|ödünç vermek|Arapça q-r-ḍ kökü; karz (ödünç), ikraz (ödünç verme), istikraz (ödünç alma), mukriz ve karzen aynı kökten gelir.
R-B-W|ar|artmak, büyütmek|Arapça r-b-w kökü; riba (faiz), ribacı ile mürebbi ve mürebbiye (büyütüp yetiştiren) aynı kökten türer.
F-Y-D|ar|yarar sağlamak|Arapça f-y-d kökü; fayda, istifade (yararlanma) ve müfit (yararlı) aynı kökten gelir.
F-Y-Z|ar|taşmak|Arapça f-y-ḍ kökü; faiz (artan, taşan), faizli, faizci, feyiz (taşan bereket) ve feyezan (taşkın) aynı kökten türer.
W-A-D|ar|söz vermek|Arapça w-ʿ-d kökü; vaat, vade (söz verilen süre), vadeli, vadesiz ve mevut (vadedilmiş) aynı kökten gelir.
M-W-L|ar|mal, varlık|Arapça m-w-l kökü; mal, maliye, mali, maliyet, emval (mallar), temvil ve mütemevvil (varlıklı) aynı kökten türer.
A-B-R|ar|geçmek; ders almak; saymak|Arapça ʿ-b-r kökü; itibar, itibari (saymaca), ibret (geçmişten alınan ders) ve muteber (geçerli sayılan) aynı kökten gelir.
D-W-L|ar|dönüp dolaşmak|Arapça d-w-l kökü; devlet (el değiştiren güç), düvel, tedavül (elden ele dolaşma), mütedavil ve devletçi aynı kökten türer.
S-F-W|ar|arı, duru olmak|Arapça ṣ-f-w kökü; saf, safi (katıksız), tasfiye (arıtma; kapatma), tasfiyeci ve musaffa aynı kökten gelir.
K-S-S|ar|izini sürmek; ödeşmek|Arapça q-ṣ-ṣ kökü; kısas (misilleme), takas (ödeşme) ve kıssa (izlenen olay; öykü) aynı kökten türer.
B-D-L|ar|değiştirmek|Arapça b-d-l kökü; bedel, mübadele (değiş tokuş), mübadil, tebdil, tebeddül, mütebeddil, bedelli ve bedelsiz aynı kökten gelir.
W-F-Y|ar|tam olmak; yerine getirmek|Arapça w-f-y kökü; vefa, ifa (yerine getirme) ve vefat (ömrün tamamlanması) aynı kökten türer.
A-F-W|ar|bağışlamak|Arapça ʿ-f-w kökü; af, affetmek, muaf (bağışlanmış), muafiyet ve istifa (bağışlanma isteme; çekilme) aynı kökten gelir.
D-M-N|ar|içermek; üstlenmek|Arapça ḍ-m-n kökü; tazmin (zararı üstlenme), zımni (içinde saklı), zımnen ve mutazammın aynı kökten türer.
Z-M-M|ar|eklemek, katmak|Arapça ḍ-m-m kökü; zam (ekleme), zamime (ek), zammetmek, munzam (eklenmiş) ve zamlanmak aynı kökten gelir.
R-W-C|ar|sürümü olmak|Arapça r-w-c kökü; revaç (sürüm), rayiç (geçerli fiyat) ve tervic (sürümünü sağlama) aynı kökten türer.
R-G-B|ar|istemek|Arapça r-ġ-b kökü; rağbet (istek), rağbetli ve mergup (istenen) aynı kökten gelir.
H-K-R|ar|stoklayıp pahalı satmak|Arapça ḥ-k-r kökü; ihtikâr (vurgunculuk) ve muhtekir (vurguncu) aynı kökten türer.
H-Z-N|ar|saklamak, depolamak|Arapça ḫ-z-n kökü; hazine, hazne, mahzen (depo) ve İtalyanca magazzino yoluyla gelen mağaza aynı kökten gelir.
D-H-L|ar|girmek|Arapça d-ḫ-l kökü; dahil, dahili, ithal (içeri sokma), ithalat, ithalatçı, müdahale ve medhal (giriş) aynı kökten türer.
L-Z-M|ar|gerekli olmak; ayrılmamak|Arapça l-z-m kökü; lüzum, lazım, elzem, lüzumlu, iltizam (üstlenme), mültezim ve mülazım aynı kökten gelir.
Z-A-M|ar|önderlik etmek|Arapça z-ʿ-m kökü; zeamet (büyük dirlik) ve zaim (zeamet sahibi; önder) aynı kökten türer.
H-S-S|ar|özel olmak, ayırmak|Arapça ḫ-ṣ-ṣ kökü; has, hassa, husus, hususi, hususiyet, mahsus, tahsis ve tahsisat aynı kökten gelir.
W-C-B|ar|gerekmek|Arapça w-c-b kökü; vacip (gerekli), vücup, icap, mucip ve mevacip (hak edilen maaşlar) aynı kökten türer.
A-W-D|ar|dönmek, geri gelmek|Arapça ʿ-w-d kökü; iade (geri verme), iadeli, aidat (geri dönen gelir), avdet, mutat ve itiyat (alışkanlık) aynı kökten gelir.
K-L-F|ar|yüklemek, zahmet vermek|Arapça k-l-f kökü; mükellef (yükümlü), mükellefiyet, teklif, külfet, tekellüf ve tekâlif (vergiler) aynı kökten türer.
B-Y-N|ar|açık olmak, ayırmak|Arapça b-y-n kökü; beyan, beyanname, beyanat, tebyin ve mübeyyin aynı kökten gelir.
S-N-Y|ar|ikilemek; ayrı tutmak|Arapça ṯ-n-y kökü; istisna (ayrı tutma), istisnai ve müstesna aynı kökten türer.
T-R-H|ar|atmak, koymak|Arapça ṭ-r-ḥ kökü; tarh (vergi koyma; çıkarma), tarhiyat ve matrah (vergi tabanı) aynı kökten gelir.
W-K-F|ar|durdurmak|Arapça w-q-f kökü; vakıf (durdurulup adanan mal), vakfiye, vâkıf, evkaf, tevkif, tevkifat, mevkuf ve tevakkuf aynı kökten türer.
S-F-L|ar|aşağı olmak|Arapça s-f-l kökü; sefil, sefalet, esfel (en alçak) ve süfli aynı kökten gelir.
R-F-H|ar|bolluk içinde olmak|Arapça r-f-h kökü; refah (gönenç), müreffeh ve terfih aynı kökten türer.
F-R-H|ar|sevinmek, genişlemek|Arapça f-r-ḥ kökü; ferah, ferahlık ve ferahlamak aynı kökten gelir.
Y-W-M|ar|gün|Arapça y-w-m kökü; yevmiye (günlük ücret) ve eyyam (günler) aynı kökten türer.
K-S-T|ar|pay etmek; adil olmak|Arapça q-s-ṭ kökü; kıst (pay), taksit (paylara bölme) ve taksitli aynı kökten gelir.
A-C-R|ar|ücret, karşılık|Arapça ʾ-c-r kökü; ücret, ücretli, ücretsiz, ecir (karşılık), icar (kiraya verme), isticar ve müstecir (kiracı) aynı kökten türer.
A-Y-Ş|ar|yaşamak, geçinmek|Arapça ʿ-y-ş kökü; maaş (geçimlik), maaşlı, maişet (geçim) ve iaşe (yedirip içirme) aynı kökten gelir.
S-G-R|ar|küçük olmak|Arapça ṣ-ġ-r kökü; sagir (küçük), asgari (en küçük) ve tasgir (küçültme) aynı kökten türer.
K-D-M|ar|önde olmak; eski olmak; ayak|Arapça q-d-m kökü; kadim, kıdem, kıdemli, takdim, mukaddem ve kadem (ayak) aynı kökten gelir.
R-K-B|ar|binmek; gözetmek|Arapça r-q-b ve r-k-b kökleri; rekabet (karşılıklı gözetme), rekabetçi, murakabe ile merkep (binek) ve mürekkep aynı kök ailesinde ele alınır.
R-H-S|ar|izin vermek|Arapça r-ḫ-ṣ kökü; ruhsat (izin), ruhsatlı, ruhsatsız ve ruhsatname aynı kökten türer.
L-T-F|ar|incelik, iyilik|Arapça l-ṭ-f kökü; lütuf, latif (ince, hoş), lütufkâr, iltifat ve mültefit aynı kökten gelir.
S-H-W|ar|cömert olmak|Arapça s-ḫ-w kökü; sehavet (cömertlik) ve sahi (cömert) aynı kökten türer.
H-L-F|ar|ardından gelmek, yerine geçmek|Arapça ḫ-l-f kökü; halife (yerine geçen), kalfa, kalfalık, halef, hilaf ve ihtilaf aynı kökten gelir.
A-H-L|ar|aile; yeterli olmak|Arapça ʾ-h-l kökü; ehil (bir işe yeterli), ehli (evcil) ve ehliyet aynı kökten türer.
M-H-R|ar|usta olmak|Arapça m-h-r kökü; mahir (usta) ve maharet (ustalık) aynı kökten gelir.
S-L-K|ar|yola girmek|Arapça s-l-k kökü; meslek (gidilen yol), mesleki, meslektaş ve sülûk aynı kökten türer.
A-H-W|ar|kardeş|Arapça ʾ-ḫ-w kökü; ihvan (kardeşler) ve uhuvvet (kardeşlik) aynı kökten gelir.
F-T-H|ar|açmak|Arapça f-t-ḥ kökü; fetih, fatih, siftah (günün ilk açılışı), iftitah, miftah (anahtar) ve fettah aynı kökten türer.
A-L-N|ar|açığa vurmak|Arapça ʿ-l-n kökü; ilan (duyuru), aleni (açık) ve alenen aynı kökten gelir.
R-S-L|ar|göndermek|Arapça r-s-l kökü; irsal (gönderme), irsaliye, mürsel, resul ve risale (gönderilen yazı) aynı kökten türer.
D-R-K|ar|ulaşmak, kavramak|Arapça d-r-k kökü; idrak (kavrama), müdrik, tedarik (yetişip sağlama) ve tedarikçi aynı kökten gelir.
S-M-S-R|ar|aracılık|Arapça dörtlü s-m-s-r kökü; simsar (aracı), simsariye (aracılık ücreti) ve simsarlık aynı kökten türer.
Z-Y-D|ar|artmak|Arapça z-y-d kökü; ziyade (fazla), mezat ve müzayede (artırma ile satış), mezatçı ve tezyit aynı kökten gelir.
T-H-F|ar|armağan; nadir şey|Arapça t-ḥ-f kökü; tuhaf (nadir, şaşırtıcı), tuhafiye (hoş küçük eşya) ve tuhafiyeci aynı kökten türer.
B-Z-Z|ar|bez, kumaş|Arapça b-z-z kökü; bez, bezzaz (bez satıcısı), bezzaziye ve Farsça -istan ekiyle bedesten aynı kökten gelir.
D-B-G|ar|deri sepilemek|Arapça d-b-ġ kökü; debbağ (deri işleyen), dibagat ve tabakhane aynı kökten türer.
S-R-C|ar|eyer; kandil|Arapça s-r-c kökü; saraç (eyerci), saraçlık ve siraç (kandil) aynı kökten gelir.
C-L-B|ar|çekmek, getirmek|Arapça c-l-b kökü; celp (çekme), celbetmek ve celep (hayvan getirip satan) aynı kökten türer.
B-K-L|ar|baklagil, sebze|Arapça b-q-l kökü; bakla, bakkal (sebze satıcısı), bakkaliye, bakkallık ve bakliyat aynı kökten gelir.
A-T-R|ar|güzel koku|Arapça ʿ-ṭ-r kökü; ıtır (koku), ıtriyat, attar ve aktar (koku ve baharat satıcısı) aynı kökten türer.
S-H-F|ar|yaprak, sayfa|Arapça ṣ-ḥ-f kökü; sahife, sayfa, mushaf (yapraklar) ve sahaf (kitapçı) aynı kökten gelir.
C-L-D|ar|deri, cilt|Arapça c-l-d kökü; cilt, ciltçi, mücellit (ciltçi) ve teclit (ciltleme) aynı kökten türer.
N-K-Ş|ar|işlemek, nakşetmek|Arapça n-q-ş kökü; nakış, nakkaş (nakış işleyen) ve münakkaş (nakışlı) aynı kökten gelir.
C-W-H-R|ar|cevher, değerli taş|Farsça gōhar'dan Arapçaya geçen c-w-h-r kökü; cevher, cevahir, mücevher ve mücevherat aynı kökten türer.
D-R-B|ar|vurmak|Arapça ḍ-r-b kökü; darp (vurma; para basma), darbe, darbımesel (örnek vurma), ızdırap ve muzdarip aynı kökten gelir.
W-R-K|ar|yaprak|Arapça w-r-q kökü; varak (yaprak), varaka (belge) ve evrak (belgeler) aynı kökten türer.
B-L-G|ar|ulaşmak|Arapça b-l-ġ kökü; meblağ (ulaşılan tutar), bâliğ, tebliğ (ulaştırma), belagat ve mübalağa aynı kökten gelir.
Ş-W-K|ar|istek, özendirme|Arapça ş-w-q kökü; şevk (istek), teşvik (özendirme) ve müşevvik aynı kökten türer.
S-K-L|ar|ağır olmak|Arapça ṯ-q-l kökü; sıklet (ağırlık), sakil (ağır) ve miskal (ağırlık birimi) aynı kökten gelir.
# --- Farsça ögeler ---
bāzār|fa|pazar|Farsça bāzār "çarşı, pazar"; pazar, pazarlık, pazarlama, pazarlamacı, pazarbaşı ve bāzārgān'dan gelen bezirgân aynı kökten türer.
ḫudā|fa|efendi, sahip|Farsça ḫudā "sahip, efendi"; kethüda (kad-ḫudā: ev sahibi) ve kethüdalık bu ögeyi taşır; kâhya da aynı sözcüğün halk biçimidir.
dast|fa|el|Farsça dast "el"; dest, destek (dastak: dayanak), destekli ve destur (el verme, izin) aynı kökten gelir.
sipurden|fa|ısmarlamak, emanet etmek|Farsça sipurden "emanet etmek"; sipariş ve siparişçi bu fiilden türer.
parākande|fa|dağınık, saçılmış|Farsça parākande "dağılmış"; perakende (parça parça satış), perakendeci ve perakendecilik aynı sözcükten gelir.
kār|fa|iş, kazanç|Farsça kār "iş; kazanç"; kâr, kârlı, kârsız, kârlılık, kârhane (işlik) ve kârgir aynı kökten türer.
bahā|fa|değer, fiyat|Farsça bahā "değer"; paha, pahalı, pahasız, pahalanmak ve pahalılaşmak aynı kökten gelir.
tīmār|fa|bakım|Farsça tīmār "bakım, hizmet"; tımar (bakım; dirlik), tımarlı ve tımarhane aynı kökten türer.
# --- Türkçe kökler ---
*ged-|tr|çentik, yarık|Eski Türkçe kedük/gedik "yarık"; gedik (duvar yarığı; esnaf tekel hakkı) ve gedikli aynı kökten gelir.
*ısmarla-|tr|sipariş etmek|Eski Anadolu Türkçesi ısmarla- "emanet etmek, sipariş etmek"; ısmarlamak ve ısmarlama aynı kökten türer.
*eksi-|tr|azalmak|Eski Türkçe eksü- "azalmak"; eksik, eksilmek, eksiltmek ve eksiltme (açık eksiltme) aynı kökten gelir.
*kuy-|tr|dökmek|Eski Türkçe kuy- "sıvı ya da maden dökmek"; kuyum, kuyumcu ve kuyumculuk aynı kökten türer.
*boz-|tr|yıkmak, parçalamak|Orhun Yazıtları'ndaki buz- "yıkmak"; bozmak, bozuk (ufak para), bozukluk ve bozdurmak aynı kökten gelir.
*ucuz|tr|düşük fiyatlı|Eski Türkçe uçuz "değersiz, kolay"; ucuz, ucuzluk, ucuzlamak ve ucuzlatmak aynı kökten türer.
*vur-|tr|vurmak|Eski Türkçe ur- "vurmak" (ön ses v- türemesiyle); vurmak, vurgun (haksız kazanç), vurguncu ve vurgunculuk aynı kökten gelir.
*kazan-|tr|elde etmek|Eski Türkçe kazġan- "elde etmek"; kazanmak, kazanç, kazançlı ve kazanım aynı kökten türer.
*tamga|tr|damga, işaret|Orhun Yazıtları'ndaki tamga "mühür, işaret"; damga, tamga, damgalamak ve damgalı aynı kökten gelir; Moğolcaya ve Rusçaya da geçmiştir.
*teng|tr|eşit, denk|Eski Türkçe teŋ "eşit"; denk, denge, dengeli, denklik ve denkleştirmek aynı kökten türer.
*değ-|tr|değmek; değerinde olmak|Eski Türkçe teg- "ulaşmak, değmek"; değmek, değer, değersiz, değerleme ve değerlendirmek aynı kökten gelir.
*iş|tr|çalışma|Eski Türkçe iş "iş"; işçi, işsiz, işsizlik, işçilik, işlik, işletme, işletmeci ve işletmecilik aynı kökten türer.
*tüke-|tr|bitmek|Eski Türkçe tüke- "bitmek"; tükenmek, tüketmek, tüketim, tüketici ve tükenmez aynı kökten gelir.
*dağıl-|tr|yayılmak, saçılmak|Eski Türkçe tagıl- "dağılmak"; dağılmak, dağıtmak, dağıtım ve dağıtıcı aynı kökten türer.
*kamu|tr|hep, bütün|Orhun Yazıtları'ndaki kamuġ "hep, bütün"; kamu (halk), kamulaştırma ve kamulaştırmak aynı kökten gelir.
*ser-|tr|yaymak|Eski Türkçe ser- "yaymak"; sermek, sergi, sergileme ve sergici aynı kökten türer.
*tek|tr|yalnız, bir|Eski Türkçe tek "yalnız"; tek, tekel (tek el), tekelci ve tekelcilik aynı kökten gelir.
*çap-|tr|hızla koşmak, akın etmek|Eski Türkçe çap- "koşmak, akın etmek"; çapul (akın, yağma), çapulcu ve çapkın aynı kökten türer.
*tart-|tr|tartmak|Eski Türkçe tart- "çekmek, tartmak"; tartmak, tartı ve tartıcı aynı kökten türer.
borç|sog|ödünç, borç|Soğdca pwrc "borç" sözcüğünden; borç, borçlu, borçlanmak, borçlanma ve borçsuz aynı kökten gelir.
# --- Batı dilleri ---
grossus|la|kalın, iri|Latince grossus "kalın"; Almanca Groschen (iri sikke) yoluyla kuruş ve kuruşluk aynı kökten türer.
drakhmē|el|avuç dolusu|Eski Yunanca drakhmḗ "avuç; para birimi"; Arapça dirham yoluyla dirhem ve Yunanca drahmi aynı kökten gelir.
libra|la|terazi; libre|Latince libra "terazi, ağırlık birimi"; İtalyanca lira, liret ve Fransızca livre yoluyla libre aynı kökten türer.
banca|it|tezgâh, sıra|İtalyanca banca "sarraf tezgâhı" (Cermence bank "sıra"); banka, banker, bankacı, bankacılık, banko ve banknot aynı kökten gelir.
centum|la|yüz|Latince centum "yüz"; sent (yüzde bir dolar) ve santim (yüzde bir frank) aynı kökten türer.
Eurṓpē|el|Avrupa|Eski Yunanca Eurṓpē "Avrupa"; Avrupa para biriminin adı avro ve euro bu addan kısaltılmıştır.
credere|la|inanmak, güvenmek|Latince credere "güvenmek"; kredi (güven), kredili, kreditör, kredibilite ve akreditif aynı kökten gelir.
primus|la|ilk|Latince primus "ilk"; prim (ilk ödül), primli ve primitif aynı kökten türer.
agere|la|yapmak, sürmek|Latince agere "yapmak"; acente (iş gören), acentelik, ajanda (yapılacaklar) ve aktif aynı kökten gelir.
bilanx|la|iki kefeli terazi|Latince bilanx "iki kefeli"; İtalyanca bilancio yoluyla bilanço ve Fransızca balance yoluyla balans aynı kökten türer.
liquere|la|akışkan olmak|Latince liquere "akmak"; likit, likidite (nakde dönüşebilme) ve likidasyon aynı kökten gelir.
manus|la|el|Latince manus "el"; manifatura (el yapımı), manifaturacı, manifesto, manipülasyon ve manüel aynı kökten türer.
stiba|el|yığın|Eski Yunanca stíba "yığın"; istif, istifçi, istifçilik ve istiflemek aynı kökten gelir.
merx|la|mal, ticaret eşyası|Latince merx "mal"; commercium'dan Rumca kommérkion yoluyla gümrük, gümrükçü, gümrüklü, gümrükleme ile market, hipermarket ve merkantilizm aynı kökten türer.
flare|la|üflemek|Latince flare "üflemek"; enflasyon (şişme), deflasyon ve stagflasyon aynı kökten gelir.
valere|la|değerli olmak|Latince valere "güçlü, değerli olmak"; valör, devalüasyon ve revalüasyon aynı kökten türer.
struere|la|kurmak, yığmak|Latince struere "kurmak"; industria'dan endüstri, endüstriyel ve endüstrileşme aynı kökten gelir.
opus|la|iş, yapıt|Latince opus "iş"; operasyon (işlem), kooperatif (birlikte çalışan) ve kooperatifçi aynı kökten türer.
pater|la|baba|Latince pater "baba"; patron (koruyucu baba), patronluk ve patronaj aynı kökten gelir.
dikē|el|hak, adalet|Eski Yunanca díkē "hak"; sýndikos'tan sendika, sendikacı ve sendikal aynı kökten türer.
secare|la|kesmek|Latince secare "kesmek"; sektör (kesim), sektörel ve seksiyon aynı kökten gelir.
margo|la|kenar|Latince margo "kenar"; marj (kenar payı) ve marjinal aynı kökten türer.
liber|la|özgür|Latince liber "özgür"; liberal, liberalizm ve liberalleşme aynı kökten gelir.
socius|la|ortak, arkadaş|Latince socius "ortak"; sosyal, sosyalizm, sosyalist ve sosyete aynı kökten türer.
legere|la|toplamak, seçmek, okumak|Latince legere "toplamak"; kolektif, kolektivizm ve koleksiyon aynı kökten gelir.
bloc|fr|yığın, kütle|Fransızca bloc "kütle" (Felemenkçe blok); blok, blokaj ve bloke aynı kökten türer.
finis|la|son, sınır|Latince finis "son"; final ile borcun sonlandırılması anlamından finans, finansman, finansal, finansör ve finanse aynı kökten gelir.
tornos|el|torna, dönüş|Eski Yunanca tórnos "torna"; Fransızca tour yoluyla tur, turne, turist ve turizm aynı kökten türer.
feria|la|bayram günü|Latince feria "bayram, tatil günü"; Fransızca foire yoluyla fuar ve fuarcılık aynı kökten gelir.
pōlein|el|satmak|Eski Yunanca pōleîn "satmak"; monopol (tek satıcı) ve oligopol (az satıcı) aynı kökten türer.
charta|la|kâğıt|Latince charta "kâğıt" (Yunanca khártēs); kart, kartel (yazılı anlaşma) ve kartela aynı kökten gelir.
clamare|la|bağırmak|Latince clamare "bağırmak"; reklam (çağrı), reklamcı, reklamcılık ve deklarasyon aynı kökten türer.
qualis|la|ne türden|Latince qualis "nasıl"; kalite, kaliteli, kalitesiz ve kalifiye aynı kökten gelir.
servus|la|köle|Latince servus "köle"; servis (hizmet) ve serf (toprak kölesi) aynı kökten türer.
fundus|la|dip, temel|Latince fundus "dip"; fon (para kaynağı) ve fonlamak aynı kökten gelir.
mille|la|bin|Latince mille "bin"; mil (bin adım), milimetre ve milyon aynı kökten türer.
experiri|la|denemek|Latince experiri "denemek"; eksper (denenmiş, uzman) ve ekspertiz aynı kökten gelir.
securus|la|kaygısız, güvenli|Latince securus "güvenli"; İtalyanca sicurtà yoluyla sigorta, sigortacı, sigortalamak ve reasürans aynı kökten türer.
naʿl|ar|nal, ayakkabı|Arapça naʿl "ayakkabı, nal"; nal, nalbant (nal bağlayan) ve nalbur (nal kesen; hırdavatçı), nalburiye aynı kökten gelir.
"""

COGNATES = r"""@pazar into_turkish
  fa بازار [bāzār] ; pazar, çarşı
  ar بازار [bāzār] ; pazar (Farsçadan)
  ur بازار [bāzār] ; çarşı
  az bazar ; pazar
  kk базар [bazar] ; pazar
  uz bozor ; pazar
  ky базар [bazar] ; pazar
  tk bazar ; pazar
  bg пазар [pazar] ; pazar; alışveriş
  sr пазар [pazar] ; pazar; alışveriş ; ff:Sırpçada pazar hem "pazar yeri" hem "yapılan alışveriş, ciro" anlamındadır
  mk пазар [pazar] ; pazar
  sq pazar ; pazar; pazarlık
  ro bazar ; bitpazarı, hediyelik eşya çarşısı ; ff:Romencede bazar "ucuz eşya satılan dükkân" anlamına daralmıştır
  el παζάρι [pazári] ; pazar; pazarlık ; ff:Yunancada pazári hem "pazar yeri" hem "pazarlık" (kánо pazári: pazarlık etmek)
  hu vásár ; pazar, panayır ; ff:Macarca vásár Türkçeden değil, doğrudan bir İran dilinden erken dönemde alınmıştır; vasárnap (pazar günü) de buradan gelir
  ru базар [bazar] ; pazar; gürültülü kalabalık ; ff:Rusçada bazar ayrıca "gürültü, kargaşa" anlamında kullanılır
  ka ბაზარი [bazari] ; pazar
  hy բազար [bazar] ; pazar
@çarşı from_turkish
  bg чаршия [çarşiya] ; çarşı
  sr чаршија [čaršija] ; çarşı; eski kent merkezi ; ff:Sırpçada čaršija ayrıca "kasaba kamuoyu, dedikodu çevresi" anlamını taşır
  mk чаршија [čaršija] ; çarşı
  sq çarshi ; çarşı
  el τσαρσί [tsarsí] ; çarşı (eskicil)
@dükkân into_turkish
  ar دكان [dukkān] ; dükkân; sedir ; ff:Arapçada dukkān "dükkân" yanında "taş seki, sedir" anlamını korur
  fa دکان [dokkān] ; dükkân
  ur دکان [dukān] ; dükkân
  az dükan ; dükkân
  uz do'kon ; dükkân
  kk дүкен [düken] ; dükkân, mağaza
  ky дүкөн [dükön] ; dükkân
  tk dükan ; dükkân
  bg дюкян [dyukyan] ; dükkân
  sr дућан [dućan] ; dükkân
  mk дуќан [duḱan] ; dükkân
  sq dyqan ; dükkân
  ro dugheană ; derme çatma dükkân ; ff:Romencede dugheană "küçük, bakımsız dükkân" küçümseyici anlam kazanmıştır
@esnaf from_turkish
  ar أصناف [aṣnāf] ; sınıflar, türler ; ff:Arapçada aṣnāf yalnızca "çeşitler, sınıflar" demektir; esnaf anlamı Türkçede gelişmiştir
  fa اصناف [aṣnāf] ; esnaf; meslek birlikleri
  bg еснаф [esnaf] ; esnaf; lonca
  sr еснаф [esnaf] ; lonca; zanaatkâr birliği ; ff:Sırpçada esnaf "lonca" anlamındadır; esnaf kişi için zanatlija kullanılır
  mk еснаф [esnaf] ; lonca
  sq esnaf ; esnaf, lonca
  ro isnaf ; lonca (eskicil)
  el εσνάφι [esnáfi] ; lonca, meslek birliği ; ff:Yunancada esnáfi "lonca" anlamındadır, tek esnaf için kullanılmaz
@para into_turkish
  fa پاره [pāre] ; parça ; ff:Farsça pāre "parça" demektir; para anlamı Osmanlı sikkesinin adından gelişmiştir
  bg пари [pari] ; para
  sr пара [para] ; para; kuruşun kırkta biri ; ff:Sırpçada para hem "para" (çoğul pare) hem dinarın yüzde biridir
  mk пари [pari] ; para
  sq para ; para
  ro para ; para (eskicil); kuruş ; ff:Romencede para bugün "n-am nicio para" (tek kuruşum yok) deyiminde yaşar
  el παράς [parás] ; para (halk dili)
  hu para ; para (argo) ; ff:Macar argosunda para "para" anlamındadır; ölçünlü dilde pénz kullanılır
  kk пара [para] ; rüşvet ; ff:Kazakçada para "rüşvet" anlamına kaymıştır
  ky пара [para] ; rüşvet ; ff:Kırgızcada para "rüşvet" demektir
  uz pora ; rüşvet ; ff:Özbekçede pora "rüşvet" anlamındadır
@kuruş into_turkish
  de Groschen ; eski Alman sikkesi; on fenik ; ff:Almanca Groschen "iri sikke" Latince grossus'tan; Türkçe kuruşun kaynağıdır
  pl grosz ; kuruş; złotynin yüzde biri ; ff:Lehçede grosz bugün de geçerli para alt birimidir
  bg грош [groş] ; eski sikke
  sr грош [groš] ; eski sikke; kuruş
  mk грош [groš] ; eski sikke
  sq grosh ; kuruş; eski sikke
  ro groș ; eski gümüş sikke
  el γρόσι [grósi] ; kuruş
  hu garas ; eski sikke; metelik ; ff:Macarcada garas "değersiz para" anlamında deyimlerde yaşar
  ar قرش [qirş] ; kuruş (Mısır, Ürdün, Suudi Arabistan alt birimi) ; ff:Arapça qirş Osmanlı kuruşundan alınmıştır; Mısır lirasının yüzde biridir
@bakkal into_turkish
  ar بقال [baqqāl] ; sebzeci; bakkal ; ff:Arapçada baqqāl asıl anlamıyla "sebze satıcısı"dır (baql: sebze)
  fa بقال [baqqāl] ; bakkal
  ur بقال [baqqāl] ; bakkal
  az baqqal ; bakkal
  uz baqqol ; bakkal
  bg бакалин [bakalin] ; bakkal
  sr бакалин [bakalin] ; bakkal
  mk бакал [bakal] ; bakkal
  sq bakall ; bakkal
  ro băcan ; bakkal ; ff:Romencede băcan "bakkal", băcănie "bakkal dükkânı" anlamındadır
  el μπακάλης [bakális] ; bakkal
@kasap into_turkish
  ar قصاب [qaṣṣāb] ; kasap
  fa قصاب [qaṣṣāb] ; kasap
  ur قصاب [qaṣṣāb] ; kasap
  az qəssab ; kasap
  uz qassob ; kasap
  bg касапин [kasapin] ; kasap
  sr касапин [kasapin] ; kasap
  mk касап [kasap] ; kasap
  sq kasap ; kasap
  ro casap ; kasap (eskicil)
  el χασάπης [hasápis] ; kasap
@hamal into_turkish
  ar حمال [ḥammāl] ; hamal
  fa حمال [ḥammāl] ; hamal
  ur حمال [ḥammāl] ; hamal
  az hambal ; hamal
  uz hammol ; hamal
  bg хамалин [hamalin] ; hamal
  sr амалин [amalin] ; hamal
  mk амал [amal] ; hamal
  sq hamall ; hamal
  ro hamal ; hamal
  el χαμάλης [hamális] ; hamal; kaba adam ; ff:Yunancada hamális mecazen "kaba, görgüsüz adam" anlamını da taşır
@terazi into_turkish
  fa ترازو [tarāzū] ; terazi
  ur ترازو [tarāzū] ; terazi
  az tərəzi ; terazi
  uz tarozi ; terazi
  kk таразы [tarazı] ; terazi
  ky тараза [taraza] ; terazi
  tk terezi ; terazi
  sr теразије [terazije] ; terazi ; ff:Belgrad'ın merkezi Terazije meydanı adını Osmanlı dönemindeki su terazisinden alır
  mk теразија [terazija] ; terazi
  sq terezi ; terazi; denge
  bg терезия [tereziya] ; terazi (halk dili)
@okka into_turkish
  ar أوقية [ūqiyya] ; ağırlık birimi (yaklaşık 30 gram) ; ff:Arapça ūqiyya çok daha hafif bir birimdir; Osmanlı okkası 1283 gramdır
  bg ока [oka] ; okka
  sr ока [oka] ; okka
  mk ока [oka] ; okka
  sq okë ; okka
  ro oca ; okka ; ff:Romencede "a prinde cu ocaua mică" (küçük okka ile yakalamak) deyimi "hile yaparken yakalamak" demektir
  el οκά [oká] ; okka
  hu okka ; okka (eski ölçü)
@kantar into_turkish
  ar قنطار [qinṭār] ; yüz rıtl (ağırlık birimi) ; ff:Arapçada qinṭār bir ağırlık birimidir; tartı aleti anlamı Türkçede gelişmiştir
  fa قنطار [qenṭār] ; ağırlık birimi
  az qantar ; kantar
  bg кантар [kantar] ; kantar
  sr кантар [kantar] ; kantar
  mk кантар [kantar] ; kantar
  sq kandar ; kantar
  ro cântar ; terazi, tartı ; ff:Romencede cântar her türlü tartı aleti için genel addır
  el καντάρι [kantári] ; kantar
  hu kantár ; dizgin ; ff:Macarca kantár "dizgin" anlamındadır ve farklı bir kökten gelir; ses benzerliği rastlantısaldır
  it cantaro ; eski ağırlık birimi
@usta into_turkish
  fa استاد [ustād] ; usta; öğretmen
  ar أستاذ [ustāḏ] ; öğretmen, profesör ; ff:Arapçada ustāḏ "öğretmen, profesör, beyefendi" demektir; zanaat ustası anlamı yoktur
  ur استاد [ustād] ; öğretmen; üstat
  az usta ; usta
  uz usta ; usta
  kk ұста [usta] ; demirci; usta ; ff:Kazakçada usta öncelikle "demirci" demektir
  ky уста [usta] ; usta, zanaatkâr
  tk ussa ; usta
  sq usta ; usta
  bg уста [usta] ; ağız ; ff:Bulgarca уста "ağız" demektir; Türkçe usta ile yalnızca eş seslidir
  sr уста [usta] ; ağız ; ff:Sırpça usta "ağız" anlamındadır; köken bağı yoktur
@kalfa into_turkish
  ar خليفة [ḫalīfa] ; halife; vekil ; ff:Arapça ḫalīfa "yerine geçen, halife" demektir; kalfa anlamı Türkçede gelişmiştir
  bg калфа [kalfa] ; kalfa
  sr калфа [kalfa] ; kalfa
  mk калфа [kalfa] ; kalfa
  sq kallfë ; kalfa
  ro calfă ; kalfa
  el κάλφας [kálfas] ; kalfa
@çırak into_turkish
  fa چراغ [çerāġ] ; lamba, kandil ; ff:Farsça çerāġ "lamba" demektir; çırak anlamı "ustanın ışığını taşıyan" mecazından Türkçede gelişmiştir
  ur چراغ [çirāġ] ; lamba ; ff:Urducada çirāġ yalnızca "kandil, lamba" anlamındadır
  az çıraq ; lamba ; ff:Azerbaycanca çıraq "lamba" anlamını korur; çırak için şagird kullanılır
  bg чирак [çirak] ; çırak
  sr чирак [čirak] ; çırak
  mk чирак [čirak] ; çırak
  sq çirak ; çırak
  ro cirac ; çömez, yandaş ; ff:Romencede cirac "birinin adamı, yandaş" anlamına kaymıştır
  el τσιράκι [tsiráki] ; çömez; yardakçı ; ff:Yunancada tsiráki küçümseyici "yardakçı, uşak" anlamındadır
@lonca into_turkish
  it loggia ; sütunlu açık galeri; loca ; ff:İtalyanca loggia "üstü örtülü galeri" demektir; esnaf birliği anlamı Türkçede gelişmiştir
  fr loge ; loca; kulübe
  en lodge ; kulübe; mason locası
  de Loge ; loca
  es logia ; mason locası
  bg лонджа [londja] ; lonca (tarihî)
@bedesten from_turkish
  bg безистен [bezisten] ; bedesten
  sr безистан [bezistan] ; bedesten
  mk безистен [bezisten] ; bedesten
  sq bezistan ; bedesten
  el μπεζεστένι [bezesténi] ; bedesten
  ar بزستان [bazistān] ; bedesten (Filistin, Suriye)
@han into_turkish
  fa خان [ḫān] ; kervansaray; han ; ff:Farsçada ḫān "kervansaray" ile ḫān "hükümdar" ayrı sözcüklerdir
  ar خان [ḫān] ; han, kervansaray
  bg хан [han] ; han
  sr хан [han] ; han
  mk ан [an] ; han
  sq han ; han
  ro han ; han
  el χάνι [háni] ; han
@kervan into_turkish
  fa کاروان [kārvān] ; kervan
  ur کارواں [kārvāṉ] ; kervan
  az karvan ; kervan
  uz karvon ; kervan
  kk керуен [keruen] ; kervan
  ky кербен [kerben] ; kervan
  tk kerwen ; kervan
  en caravan ; kervan; karavan ; ff:İngilizce caravan ayrıca "çekme ev, karavan" demektir
  fr caravane ; kervan; karavan
  it carovana ; kervan
  de Karawane ; kervan
  es caravana ; kervan; araç kuyruğu ; ff:İspanyolca caravana "trafik sıkışıklığı" anlamında da kullanılır
  bg керван [kervan] ; kervan
  sr караван [karavan] ; kervan
  sq karvan ; kervan
  ro caravană ; kervan
  el καραβάνι [karaváni] ; kervan
  hu karaván ; kervan
  ru караван [karavan] ; kervan
  pl karawana ; kervan
@kervansaray into_turkish
  fa کاروانسرا [kārvānsarā] ; kervansaray
  en caravanserai ; kervansaray
  fr caravansérail ; kervansaray
  bg кервансарай [kervansaray] ; kervansaray
  sr каравансарај [karavansaraj] ; kervansaray
  ro caravanserai ; kervansaray
@kese into_turkish
  fa کیسه [kīse] ; kese, torba
  ar كيس [kīs] ; torba, poşet
  ur کیسہ [kīsa] ; kese
  az kisə ; kese
  uz kissa ; cep ; ff:Özbekçede kissa "cep" anlamına kaymıştır
  bg кесия [kesiya] ; kese; cüzdan
  sr кеса [kesa] ; torba, poşet ; ff:Sırpçada kesa her tür torba ve naylon poşet için kullanılır
  mk кеса [kesa] ; torba
  sq qese ; kese; torba
  ro chisea ; tütün kesesi
  el κεσές [kesés] ; hamam kesesi
@kasa into_turkish
  it cassa ; kasa; kutu
  es caja ; kutu; kasa
  pt caixa ; kutu; kasa
  fr caisse ; kasa; sandık
  en cash ; nakit ; ff:İngilizce cash "nakit" aynı Latince capsa'dan türemiştir; kutu anlamı yitmiştir
  de Kasse ; kasa; gişe
  bg каса [kasa] ; kasa; gişe
  sr каса [kasa] ; kasa
  ro casă ; ev; kasa ; ff:Romencede casă "ev" (Latince casa) ile "kasa" (capsa) iki ayrı kökten eş seslidir
  el κάσα [kása] ; kasa; tabut ; ff:Yunancada kása "tabut" anlamında da kullanılır
  hu kassza ; kasa
  ru касса [kassa] ; gişe; kasa ; ff:Rusçada kassa öncelikle "bilet gişesi, vezne" demektir
  pl kasa ; kasa; para (argo)
  az kassa ; kasa
@fatura into_turkish
  it fattura ; fatura; yapım
  es factura ; fatura
  pt fatura ; fatura
  fr facture ; fatura; yapı tarzı
  bg фактура [faktura] ; fatura
  sr фактура [faktura] ; fatura
  ro factură ; fatura
  hu faktúra ; fatura
  ru фактура [faktura] ; doku, yüzey yapısı ; ff:Rusçada faktura "doku, malzeme yapısı" anlamındadır; fatura için sçot kullanılır
  pl faktura ; fatura
  az faktura ; fatura
  uz faktura ; fatura
@banka into_turkish
  it banca ; banka
  fr banque ; banka
  en bank ; banka; kıyı ; ff:İngilizce bank "nehir kıyısı" anlamı ayrı bir Cermen köktendir
  de Bank ; banka; sıra ; ff:Almanca Bank hem "oturma sırası" hem "banka"dır; iki anlam aynı Cermen kökten gelir
  es banco ; banka; sıra
  pt banco ; banka; sıra
  bg банка [banka] ; banka
  sr банка [banka] ; banka
  mk банка [banka] ; banka
  sq bankë ; banka
  ro bancă ; banka; sıra ; ff:Romencede bancă hem "banka" hem "oturma sırası"dır
  hu bank ; banka
  ru банк [bank] ; banka
  pl bank ; banka
  az bank ; banka
  kk банк [bank] ; banka
  uz bank ; banka
  ur بینک [baink] ; banka
@kredi into_turkish
  fr crédit ; kredi; güven
  it credito ; kredi
  en credit ; kredi; itibar
  de Kredit ; kredi
  es crédito ; kredi
  bg кредит [kredit] ; kredi
  sr кредит [kredit] ; kredi
  ro credit ; kredi
  ru кредит [kredit] ; kredi
  pl kredyt ; kredi
  az kredit ; kredi
  uz kredit ; kredi
@faiz into_turkish
  ar فائض [fāʾiḍ] ; fazla, artık ; ff:Arapçada fāʾiḍ "fazla, artan" demektir; faiz için fāʾida ya da ribā kullanılır
  az faiz ; faiz; yüzde ; ff:Azerbaycanca faiz ayrıca "yüzde (%)" demektir
  uz foiz ; yüzde ; ff:Özbekçede foiz "yüzde" anlamındadır; faiz için foiz stavkasi kullanılır
  kk пайыз [payız] ; yüzde ; ff:Kazakçada payız "yüzde (%)" demektir
  ky пайыз [payız] ; yüzde ; ff:Kırgızcada payız "yüzde" anlamındadır
@fayda into_turkish
  ar فائدة [fāʾida] ; yarar; faiz ; ff:Arapçada fāʾida bugün "banka faizi" anlamında da kullanılır
  fa فایده [fāyede] ; yarar
  ur فائدہ [fāʾida] ; yarar
  az fayda ; yarar
  uz foyda ; yarar; kâr
  kk пайда [payda] ; yarar; kâr
  ky пайда [payda] ; yarar
  tk peýda ; yarar
  bg файда [fayda] ; yarar (halk dili)
  sr вајда [vajda] ; yarar ; ff:Sırpçada vajda "yarar, fayda" halk dilinde yaşar (nema vajde: faydası yok)
  mk фајде [fajde] ; yarar
  sq fajde ; yarar; faiz ; ff:Arnavutçada fajde hem "yarar" hem "faiz" anlamındadır
@sermaye into_turkish
  fa سرمایه [sarmāye] ; sermaye
  ur سرمایہ [sarmāya] ; sermaye
  az sərmayə ; sermaye
  uz sarmoya ; sermaye
  bg сермия [sermiya] ; sermaye (eskicil)
  sr сермија [sermija] ; sermaye (eskicil)
  el σερμαγιά [sermayá] ; sermaye (eskicil)
@borç shared_ancestor
  az borc ; borç
  kk борыш [borış] ; borç; görev ; ff:Kazakçada borış "borç" yanında "ödev, görev" anlamındadır
  tk bergi ; borç
  bg борч [borç] ; borç
  mk борч [borč] ; borç
  sq borxh ; borç
  sr борч [borč] ; borç (halk dili)
@veresiye from_turkish
  bg вересия [veresiya] ; veresiye
  sr вересија [veresija] ; veresiye
  mk вересија [veresija] ; veresiye
  sq veresi ; veresiye
  el βερεσέ [veresé] ; veresiye
@pazarlık from_turkish
  bg пазарлък [pazarlık] ; pazarlık
  mk пазарлак [pazarlak] ; pazarlık
  sq pazarllëk ; pazarlık
  sr пазарлук [pazarluk] ; pazarlık (halk dili)
@sarraf into_turkish
  ar صراف [ṣarrāf] ; sarraf; vezne görevlisi ; ff:Arapçada ṣarrāf bugün "banka veznedarı" anlamında da kullanılır
  fa صراف [ṣarrāf] ; sarraf
  ur صراف [ṣarrāf] ; sarraf; kuyumcu
  az sərraf ; sarraf
  uz sarrof ; sarraf
  bg сараф [saraf] ; sarraf
  sr сараф [saraf] ; sarraf
  mk сараф [saraf] ; sarraf
  sq saraf ; sarraf
  ro zaraf ; sarraf
  el σαράφης [saráfis] ; sarraf
@kuyumcu from_turkish
  bg куюмджия [kuyumdjiya] ; kuyumcu
  sr кујунџија [kujundžija] ; kuyumcu
  mk кујунџија [kujundžija] ; kuyumcu
  sq kujunxhi ; kuyumcu
@dirhem into_turkish
  ar درهم [dirham] ; dirhem; Fas ve BAE para birimi
  fa درهم [derham] ; dirhem
  ur درہم [dirham] ; dirhem
  az dirhəm ; dirhem
  el δραχμή [drakhmí] ; drahmi ; ff:Yunanca drakhmḗ dirhemin uzak kaynağıdır; drahmi biçimi Türkçeye ayrıca girmiştir
  hy դրամ [dram] ; para; Ermenistan para birimi ; ff:Ermenice dram aynı Yunanca kökten gelir ve genel olarak "para" demektir
  bg драм [dram] ; dirhem (ağırlık)
  sr драм [dram] ; dirhem; zerre ; ff:Sırpçada dram mecazen "zerre, azıcık" anlamında da kullanılır
  ro dram ; zerre, azıcık ; ff:Romencede dram "azıcık" anlamına kaymıştır (un dram de noroc: bir parça şans)
  en dram ; küçük içki ölçüsü ; ff:İngilizce dram "bir yudum içki" anlamında yaşar; aynı Yunanca köktendir
@dinar into_turkish
  ar دينار [dīnār] ; dinar (Irak, Ürdün, Kuveyt para birimi)
  fa دینار [dīnār] ; dinar; riyalin yüzde biri
  ur دینار [dīnār] ; dinar
  sr динар [dinar] ; Sırbistan para birimi
  mk денар [denar] ; Makedonya para birimi
  sq dinar ; dinar
  es dinero ; para ; ff:İspanyolca dinero "para" aynı Latince denarius'tan gelir
  pt dinheiro ; para ; ff:Portekizce dinheiro "para" demektir
  it denaro ; para
  fr denier ; eski sikke
@altın shared_ancestor
  az qızıl ; altın ; ff:Azerbaycancada altın için qızıl (kızıl) kullanılır; altun eskicildir
  kk алтын [altın] ; altın
  uz oltin ; altın
  ky алтын [altın] ; altın
  tk altyn ; altın
  mn алт [alt] ; altın
  ru алтын [altın] ; üç kapiklik eski sikke ; ff:Rusçada altın değerli maden değil, üç kapik değerinde eski bir sikkedir
  bg алтън [altın] ; altın sikke ; ff:Bulgarcada altın "altın lira, altın sikke" anlamındadır
  sq alltën ; altın sikke
@akçe from_turkish
  bg акче [akçe] ; akçe (tarihî)
  sr акча [akča] ; akçe (tarihî)
  hu akcse ; akçe (tarihî)
  ro aspru ; akçe ; ff:Romencede akçe için Yunanca áspron (beyaz) kökenli aspru kullanılır
@mangır from_turkish
  bg мангър [mangır] ; bakır para (tarihî)
  sr мангура [mangura] ; bakır para (tarihî)
  mn мөнгө [möngö] ; gümüş; para; Moğolistan para alt birimi ; ff:Moğolca möngö "gümüş; para" mangırın olası kaynağıdır
@lira into_turkish
  it lira ; lira
  el λίρα [líra] ; lira
  bg лира [lira] ; lira
  sr лира [lira] ; lira
  sq lirë ; lira
  ro liră ; lira
  hu líra ; lira
  ar ليرة [līra] ; lira (Lübnan, Suriye para birimi)
  fa لیره [līre] ; lira
  fr livre ; libre; kitap ; ff:Fransızca livre hem "kitap" (liber) hem "libre, lira" (libra) anlamında iki ayrı Latince kökten eş seslidir
  es libra ; libre; sterlin
  pt libra ; libre
@hesap into_turkish
  ar حساب [ḥisāb] ; hesap
  fa حساب [hesāb] ; hesap
  ur حساب [hisāb] ; hesap
  az hesab ; hesap
  uz hisob ; hesap
  kk есеп [esep] ; hesap
  ky эсеп [esep] ; hesap
  tk hasap ; hesap
  sr хесап [hesap] ; hesap (halk dili)
  mk есап [esap] ; hesap
  sq hesap ; hesap
  he חשבון [ḥeshbon] ; hesap ; ff:İbranice ḥeshbon aynı Sami kökünden (ḥ-ş-b) bağımsız olarak gelişmiştir
@defter into_turkish
  el δεφτέρι [deftéri] ; defter ; ff:Yunanca diphthéra "deri" Arapça daftar'ın kaynağıdır; deftéri biçimi Türkçeden geri alınmadır
  ar دفتر [daftar] ; defter
  fa دفتر [daftar] ; ofis, büro; defter ; ff:Farsçada daftar öncelikle "büro, ofis" anlamındadır
  ur دفتر [daftar] ; ofis ; ff:Urducada daftar "ofis, iş yeri" demektir; defter için kāpī kullanılır
  az dəftər ; defter
  uz daftar ; defter
  kk дәптер [däpter] ; defter
  ky дептер [depter] ; defter
  tk depder ; defter
  bg тефтер [tefter] ; defter
  sr тефтер [tefter] ; defter
  mk тефтер [tefter] ; defter
  sq defter ; defter
@muhasebe into_turkish
  ar محاسبة [muḥāsaba] ; muhasebe; hesap sorma
  fa محاسبه [mohāsebe] ; hesaplama ; ff:Farsçada mohāsebe "hesaplama" anlamındadır; muhasebe için hesābdārī kullanılır
  ur محاسبہ [muḥāsaba] ; hesap sorma; denetim
  az mühasibat ; muhasebe
@vergi from_turkish
  az vergi ; vergi
  bg вергия [vergiya] ; vergi (tarihî)
  sq vergji ; vergi (tarihî)
@haraç into_turkish
  ar خراج [ḫarāc] ; toprak vergisi
  fa خراج [ḫarāc] ; haraç
  bg харач [haraç] ; haraç
  sr харач [harač] ; haraç
  mk арач [arač] ; haraç
  sq haraç ; haraç
  ro haraci ; haraç
  el χαράτσι [harátsi] ; ağır vergi ; ff:Yunancada harátsi bugün "haksız, ağır vergi" anlamında kullanılır
  hu harács ; yağma ; ff:Macarcada harács "yağma", harácsol "yağmalamak, kazanç biriktirmek" anlamına kaymıştır
  pl haracz ; haraç; zorla alınan para ; ff:Lehçede haracz özellikle suç örgütlerinin aldığı "koruma parası"dır
@cizye into_turkish
  ar جزية [cizya] ; cizye
  fa جزیه [cezye] ; cizye
  ur جزیہ [cizya] ; cizye
  sq xhizje ; cizye
  bg джизие [cizie] ; cizye (tarihî)
  sr џизја [džizja] ; cizye (tarihî)
@gümrük into_turkish
  el κομμέρκιον [kommérkion] ; ticaret vergisi (Bizans) ; ff:Bizans Rumcasında kommérkion "ticaret vergisi" Latince commercium'dan gelir
  it commercio ; ticaret ; ff:İtalyanca commercio "ticaret" demektir; vergi anlamı yalnızca Bizans kullanımında vardır
  en commerce ; ticaret
  fr commerce ; ticaret
  es comercio ; ticaret
  az gömrük ; gümrük
  tk gümrük ; gümrük
  bg гюмрук [gyumruk] ; gümrük (tarihî)
  sr ђумрук [đumruk] ; gümrük (tarihî)
  mk ѓумрук [ǵumruk] ; gümrük
  sq gjymryk ; gümrük (tarihî)
@ticaret into_turkish
  ar تجارة [ticāra] ; ticaret
  fa تجارت [tecārat] ; ticaret
  ur تجارت [tijārat] ; ticaret
  az ticarət ; ticaret
  uz tijorat ; ticaret
@tacir into_turkish
  ar تاجر [tācir] ; tacir
  fa تاجر [tācer] ; tacir
  ur تاجر [tājir] ; tacir
  az tacir ; tacir
  uz tojir ; tacir
@tüccar into_turkish
  ar تجار [tuccār] ; tacirler ; ff:Arapça tuccār "tacirler" çoğuludur; Türkçede tekil kullanılır
  fa تجار [toccār] ; tacirler
  bg туджар [tudjar] ; tüccar (halk dili)
  sq tyxhar ; tüccar
@kâr into_turkish
  fa کار [kār] ; iş ; ff:Farsça kār "iş, çalışma" demektir; kazanç anlamı Türkçede gelişmiştir
  ur کار [kār] ; iş ; ff:Urducada kār "iş" anlamındadır (kārobār: ticaret)
  bg кяр [kyar] ; kâr (halk dili)
  sr ћар [ćar] ; kâr, çıkar
  mk ќар [ḱar] ; kâr
  sq qar ; kâr
@zarar into_turkish
  ar ضرر [ḍarar] ; zarar
  fa ضرر [żarar] ; zarar
  ur ضرر [zarar] ; zarar
  az zərər ; zarar
  uz zarar ; zarar
  bg зарар [zarar] ; zarar (halk dili)
  sq zarar ; zarar (halk dili)
@hasar into_turkish
  ar خسارة [ḫasāra] ; kayıp, zarar
  fa خسارت [ḫesārat] ; hasar, tazminat
  ur خسارہ [ḫasāra] ; zarar
  az xəsarət ; hasar
@masraf into_turkish
  ar مصرف [maṣraf] ; banka ; ff:Arapçada maṣraf bugün "banka" anlamındadır; masraf için maṣrūf kullanılır
  fa مصرف [maṣraf] ; tüketim, kullanım ; ff:Farsçada maṣraf "tüketim, kullanım" demektir
  ur مصرف [maṣraf] ; kullanım
  az məsrəf ; masraf
  bg масраф [masraf] ; masraf (halk dili)
  sq masraf ; masraf
@israf into_turkish
  ar إسراف [isrāf] ; israf
  fa اسراف [esrāf] ; israf
  ur اسراف [isrāf] ; israf
  az israf ; israf
  uz isrof ; israf
@nafaka into_turkish
  ar نفقة [nafaqa] ; nafaka; harcama
  fa نفقه [nafaqe] ; nafaka
  ur نفقہ [nafqa] ; nafaka
  uz nafaqa ; emekli aylığı ; ff:Özbekçede nafaqa "emekli maaşı" anlamına kaymıştır
  sq nafakë ; kısmet, nasip ; ff:Arnavutçada nafakë "kısmet, alın yazısı" anlamındadır
@kefil into_turkish
  ar كفيل [kafīl] ; kefil; sponsor
  fa کفیل [kafīl] ; kefil; vekil
  ur کفیل [kafīl] ; kefil
  az kəfil ; kefil
  uz kafil ; kefil
  kk кепіл [kepil] ; güvence, teminat ; ff:Kazakçada kepil "güvence, garanti" anlamındadır; kefil kişi için kepilgerlik türetilir
  ky кепил [kepil] ; güvence
@vekil into_turkish
  ar وكيل [wakīl] ; vekil; avukat ; ff:Arapçada wakīl aynı zamanda "avukat" demektir
  fa وکیل [vakīl] ; avukat; milletvekili ; ff:Farsçada vakīl "avukat" ve "milletvekili" anlamlarındadır
  ur وکیل [vakīl] ; avukat ; ff:Urducada vakīl yalnızca "avukat" demektir
  az vəkil ; avukat; vekil ; ff:Azerbaycanca vəkil öncelikle "avukat" anlamındadır
  uz vakil ; temsilci
  kk уәкіл [uäkil] ; temsilci
  ky өкүл [ökül] ; temsilci
@şirket into_turkish
  ar شركة [şarika] ; şirket
  fa شرکت [şerkat] ; şirket; katılım ; ff:Farsçada şerkat ayrıca "katılma, iştirak" demektir
  ur شرکت [şirkat] ; katılım; şirket
  az şirkət ; şirket
  uz shirkat ; şirket
  kk серіктестік [seriktestik] ; şirket, ortaklık ; ff:Kazakçada aynı kökten serik "ortak" sözcüğüyle türetilmiştir
@müşteri into_turkish
  ar مشتري [muştarī] ; satın alan; Jüpiter ; ff:Arapçada al-Muştarī aynı zamanda Jüpiter gezegeninin adıdır
  fa مشتری [moştarī] ; müşteri; Jüpiter
  ur مشتری [muştarī] ; müşteri
  az müştəri ; müşteri
  bg мющерия [myuşteriya] ; müşteri
  sr муштерија [mušterija] ; müşteri
  mk муштерија [mušterija] ; müşteri
  sq mushteri ; müşteri
  ro muşteriu ; müşteri
  el μουστερής [mousterís] ; müşteri
@bedava into_turkish
  fa باد هوا [bād-e havā] ; boş, havadan ; ff:Farsça bād-e havā sözcüğü sözcüğüne "hava rüzgârı", mecazen "boşuna" demektir
  bg бадева [badeva] ; bedava; boşuna
  sr бадава [badava] ; bedava; boşuna ; ff:Sırpçada badava "boşuna, nafile" anlamı öne çıkar
  mk бадијала [badijala] ; boşuna
  sq badihava ; bedava
@kira into_turkish
  ar كراء [kirāʾ] ; kira
  fa کرایه [kerāye] ; kira; taksi ücreti
  ur کرایہ [kirāya] ; kira; bilet ücreti ; ff:Urducada kirāya ayrıca "yol, bilet ücreti" demektir
  az kirayə ; kira
  bg кирия [kiriya] ; kira
  sr кирија [kirija] ; kira
  mk кирија [kirija] ; kira
  sq qira ; kira
  ro chirie ; kira
@paha into_turkish
  fa بها [bahā] ; değer, fiyat
  ur بہا [bahā] ; değer
  az baha ; pahalı ; ff:Azerbaycanca baha "pahalı" sıfatıdır; Türkçe paha ise "değer" adıdır
  kk баға [bağa] ; fiyat ; ff:Kazakçada bağa "fiyat" anlamındadır
  ky баа [baa] ; fiyat
  uz baho ; fiyat; değer; not ; ff:Özbekçede baho ayrıca "okul notu" demektir
  tk baha ; fiyat
@hazine into_turkish
  ar خزينة [ḫazīna] ; hazine; kasa
  fa خزانه [ḫazāne] ; hazine
  ur خزانہ [ḫazāna] ; hazine
  az xəzinə ; hazine
  uz xazina ; hazine
  kk қазына [qazına] ; hazine
  ky казына [kazına] ; hazine
  tk hazyna ; hazine
  bg хазна [hazna] ; hazine; devlet kasası
  sr хазна [hazna] ; hazine
  sq hazine ; hazine
  ro hazna ; hazine; lağım çukuru ; ff:Romencede hazna "fosseptik, lağım çukuru" anlamına kaymıştır
  el χαζνές [haznés] ; hazine (eskicil)
@mağaza into_turkish
  it magazzino ; depo ; ff:İtalyanca magazzino "depo" demektir; mağaza anlamı Fransızca magasin yoluyla gelişmiştir
  fr magasin ; mağaza
  en magazine ; dergi; şarjör ; ff:İngilizce magazine "dergi" (bilgi deposu) ve "şarjör" anlamlarına kaymıştır
  de Magazin ; dergi; depo
  es almacén ; depo ; ff:İspanyolca almacén Arapça al-maḫzan'dan doğrudan alınmıştır, "depo" demektir
  ru магазин [magazin] ; mağaza
  bg магазин [magazin] ; mağaza
  sr магацин [magacin] ; depo ; ff:Sırpçada magacin "depo" anlamındadır; mağaza için radnja kullanılır
  ro magazin ; mağaza
  el μαγαζί [magazí] ; dükkân
  hu magazin ; dergi ; ff:Macarca magazin "dergi" anlamındadır
  pl magazyn ; depo; dergi
  ar مخزن [maḫzan] ; depo
  fa مخزن [maḫzan] ; depo; tank
  az mağaza ; mağaza
  uz magazin ; mağaza
@ambar into_turkish
  fa انبار [anbār] ; ambar, depo
  ur انبار [ambār] ; yığın ; ff:Urducada ambār "yığın, küme" anlamındadır
  az anbar ; ambar
  uz ombor ; ambar
  ru амбар [ambar] ; ambar
  bg хамбар [hambar] ; ambar
  sr амбар [ambar] ; ambar
  mk амбар [ambar] ; ambar
  sq hambar ; ambar
  ro hambar ; ambar
  el αμπάρι [ambári] ; gemi ambarı ; ff:Yunancada ambári "gemi ambarı" anlamındadır
  hu hombár ; ambar (eskicil)
@depo into_turkish
  fr dépôt ; depo; tortu
  en depot ; depo; garaj
  it deposito ; depo; mevduat ; ff:İtalyanca deposito ayrıca "banka mevduatı" demektir
  de Depot ; depo
  ru депо [depo] ; lokomotif garajı ; ff:Rusçada depo yalnızca "lokomotif, tramvay garajı" anlamındadır
  bg депо [depo] ; depo; garaj
  sr депо [depo] ; depo
  ro depou ; garaj
@arşın from_turkish
  ru аршин [arşin] ; eski uzunluk ölçüsü (71 cm)
  uk аршин [arşın] ; eski uzunluk ölçüsü
  bg аршин [arşin] ; arşın
  sr аршин [aršin] ; arşın
  mk аршин [aršin] ; arşın
  sq arshin ; arşın
  ro arşin ; arşın
  az arşın ; arşın
  uz arshin ; arşın
  kk аршын [arşın] ; arşın
@batman shared_ancestor
  ru батман [batman] ; eski ağırlık ölçüsü
  az batman ; batman
  uz botmon ; batman
  kk батпан [batpan] ; batman
  ky батман [batman] ; batman
@dönüm from_turkish
  bg дюнюм [dyunyum] ; dönüm
  sr дунум [dunum] ; dönüm
  mk дунум [dunum] ; dönüm
  sq dynym ; dönüm
  ar دونم [dūnum] ; dönüm (Filistin, Ürdün, Irak)
  he דונם [dunam] ; dönüm (1000 m²) ; ff:İbranice dunam Osmanlı'dan kalan bu ölçüyü İsrail'de resmî birim olarak sürdürür
@endaze into_turkish
  fa اندازه [andāze] ; ölçü, boyut
  ur اندازہ [andāza] ; tahmin, kestirim ; ff:Urducada andāza "tahmin" anlamındadır
  az əndazə ; ölçü
  uz andoza ; kalıp, ölçü
@kâhya into_turkish
  fa کدخدا [kadḫodā] ; köy muhtarı; ev sahibi ; ff:Farsçada kadḫodā "köy ağası, muhtar" anlamındadır
  bg кехая [kehaya] ; kâhya
  sr ћехаја [ćehaja] ; kâhya
  mk ќеаја [ḱeaja] ; kâhya
  sq qehaja ; kâhya
  ro chihaie ; kâhya
  el κεχαγιάς [kehayás] ; kâhya
@tellal into_turkish
  ar دلال [dallāl] ; komisyoncu, simsar ; ff:Arapçada dallāl "emlak ya da mal simsarı" demektir
  fa دلال [dallāl] ; simsar
  ur دلال [dallāl] ; simsar; pezevenk ; ff:Urducada dallāl ayrıca "pezevenk" anlamını taşır
  az dəllal ; tellal; simsar
  bg телял [telyal] ; tellal
  sr телал [telal] ; tellal
  mk телал [telal] ; tellal
  sq tellall ; tellal
  ro telal ; eskici; tellal ; ff:Romencede telal "eski eşya satıcısı" anlamına kaymıştır
  el τελάλης [telális] ; tellal
@simsar into_turkish
  ar سمسار [simsār] ; simsar
  fa سمسار [semsār] ; eskici ; ff:Farsçada semsār "ikinci el eşya satıcısı" anlamındadır
  ur سمسار [simsār] ; simsar
@mezat into_turkish
  ar مزاد [mazād] ; mezat, açık artırma
  fa مزایده [mozāyede] ; mezat
  bg мезат [mezat] ; mezat
  sq mezat ; mezat
@vakıf into_turkish
  ar وقف [waqf] ; vakıf
  fa وقف [vaqf] ; vakıf
  ur وقف [vaqf] ; vakıf
  az vəqf ; vakıf
  uz vaqf ; vakıf
  bg вакъф [vakıf] ; vakıf
  sr вакуф [vakuf] ; vakıf
  mk вакаф [vakaf] ; vakıf
  sq vakëf ; vakıf
  el βακούφι [vakoúfi] ; vakıf
@zekât into_turkish
  ar زكاة [zakāt] ; zekât
  fa زکات [zakāt] ; zekât
  ur زکوٰۃ [zakāt] ; zekât
  az zəkat ; zekât
  uz zakot ; zekât
  kk зекет [zeket] ; zekât
  ky зекет [zeket] ; zekât
  sq zeqat ; zekât
@sadaka into_turkish
  ar صدقة [ṣadaqa] ; sadaka
  fa صدقه [ṣadaqe] ; sadaka
  ur صدقہ [ṣadqa] ; sadaka
  az sədəqə ; sadaka
  uz sadaqa ; sadaka
  kk садақа [sadaqa] ; sadaka
  ky садага [sadaga] ; sadaka
  bg садака [sadaka] ; sadaka (halk dili)
  sr садака [sadaka] ; sadaka
  sq sadaka ; sadaka
  he צדקה [tsedaka] ; hayır, bağış ; ff:İbranice tsedaka "adalet; hayırseverlik" anlamında aynı Sami kökten gelir
@bahşiş into_turkish
  fa بخشش [baḫşeş] ; bağış; af ; ff:Farsçada baḫşeş "bağışlama, af" demektir; bahşiş için anʿām kullanılır
  ur بخشش [baḫşiş] ; bağış; af
  ar بقشيش [baqşīş] ; bahşiş (Mısır ve Levant Arapçası)
  en baksheesh ; bahşiş
  fr bakchich ; bahşiş; rüşvet
  de Bakschisch ; bahşiş; rüşvet
  bg бакшиш [bakşiş] ; bahşiş
  sr бакшиш [bakšiš] ; bahşiş
  mk бакшиш [bakšiš] ; bahşiş
  sq bakshish ; bahşiş
  ro bacşiş ; bahşiş
  el μπαξίσι [baksísi] ; bahşiş
  hu baksis ; bahşiş
  ru бакшиш [bakşiş] ; bahşiş; rüşvet
  az bəxşiş ; bahşiş
@hediye into_turkish
  ar هدية [hadiyya] ; hediye
  fa هدیه [hedye] ; hediye
  ur ہدیہ [hadiya] ; hediye; bağış
  az hədiyyə ; hediye
  uz hadya ; hediye
@rüşvet into_turkish
  ar رشوة [rişwa] ; rüşvet
  fa رشوه [reşve] ; rüşvet
  ur رشوت [rişvat] ; rüşvet
  az rüşvət ; rüşvet
  bg рушвет [ruşvet] ; rüşvet
  mk рушвет [rušvet] ; rüşvet
  sq ryshfet ; rüşvet
  el ρουσφέτι [rousféti] ; siyasi kayırma, torpil ; ff:Yunancada rousféti "oy karşılığı siyasi kayırma" anlamına kaymıştır
@kesat into_turkish
  ar كساد [kasād] ; durgunluk, sürümsüzlük
  fa کساد [kasād] ; durgunluk
  ur کساد [kasād] ; durgunluk
@revaç into_turkish
  ar رواج [rawāc] ; sürüm, yaygınlık
  fa رواج [ravāc] ; yaygınlık, moda ; ff:Farsçada ravāc "yaygınlık, moda olma" anlamındadır
  ur رواج [rivāj] ; görenek, âdet ; ff:Urducada rivāj "gelenek, görenek" demektir
  az rəvac ; revaç
  uz ravoj ; gelişme, refah ; ff:Özbekçede ravoj "gelişme, ilerleme" anlamına kaymıştır
@rağbet into_turkish
  ar رغبة [raġba] ; istek, arzu
  fa رغبت [raġbat] ; istek
  ur رغبت [raġbat] ; istek, eğilim
  az rəğbət ; sempati; rağbet ; ff:Azerbaycanca rəğbət "sempati, yakınlık" anlamındadır
  uz rag'bat ; istek, heves
@nakit into_turkish
  ar نقد [naqd] ; peşin para; eleştiri ; ff:Arapçada naqd hem "nakit" hem "eleştiri" anlamındadır (aynı kök: ayıklamak)
  fa نقد [naqd] ; nakit; eleştiri
  ur نقد [naqd] ; nakit
  az nağd ; nakit
  uz naqd ; nakit
  kk нақты [naqtı] ; kesin, gerçek ; ff:Kazakçada naqtı "kesin, somut" anlamına kaymıştır; nakit için qolma-qol aqşa kullanılır
@sikke into_turkish
  ar سكة [sikka] ; demiryolu; sikke ; ff:Arapçada sikka bugün çoğunlukla "demiryolu" (sikkat al-ḥadīd) anlamındadır
  fa سکه [sekke] ; madeni para
  ur سکہ [sikka] ; madeni para; para birimi
  az sikkə ; sikke
  uz sikka ; sikke (tarihî)
@darphane into_turkish
  fa ضرابخانه [żarrābḫāne] ; darphane
  az zərbxana ; darphane
  uz zarbxona ; darphane
  ur ٹکسال [ṭaksāl] ; darphane ; ff:Urducada darphane için Sanskrit kökenli ṭaksāl kullanılır; köken bağı yoktur
@kumbara into_turkish
  fa خمپاره [ḫompāre] ; havan mermisi ; ff:Farsçada ḫompāre "havan topu mermisi" demektir (Türkçe humbara); para kutusu anlamı Türkçede gelişmiştir
  bg кумбара [kumbara] ; kumbara
  el κουμπαράς [koumbarás] ; kumbara
  sq kumbara ; kumbara
@cüzdan into_turkish
  ar جزدان [cuzdān] ; cüzdan; çanta (Mısır)
  fa جزدان [cozdān] ; Kur'an kılıfı ; ff:Farsçada cozdān "cüz kılıfı, kitap kılıfı" anlamındadır
  ur جزدان [juzdān] ; kılıf, kutu
  sq xhyzdan ; cüzdan
  bg джузданче [cuzdançe] ; cüzdan
@murabaha into_turkish
  ar مرابحة [murābaḥa] ; kârlı satış (İslami finans)
  fa مرابحه [morābeḥe] ; murabaha
  ur مرابحہ [murābaḥa] ; murabaha
  en murabaha ; İslami finans sözleşmesi
@riba into_turkish
  ar ربا [ribā] ; faiz, tefecilik
  fa ربا [rebā] ; faiz
  ur ربا [ribā] ; faiz
  he ריבית [ribit] ; faiz ; ff:İbranice ribbit "faiz" aynı Sami kökten (r-b-y: artmak) bağımsız gelişmiştir
@bono into_turkish
  it buono ; iyi; fiş, kupon ; ff:İtalyanca buono "iyi" sıfatı ve "fiş, kupon" adıdır
  es bono ; bono; kupon
  fr bon ; fiş; iyi
  ro bon ; fiş
  en bond ; tahvil ; ff:İngilizce bond "bağ" anlamındaki Cermen kökten gelir; bono ile köken bağı yoktur
@poliçe into_turkish
  it polizza ; poliçe
  fr police ; sigorta poliçesi; polis ; ff:Fransızca police "poliçe" (polizza) ile "polis" (polis) iki ayrı kökten eş seslidir
  en policy ; sigorta poliçesi; politika ; ff:İngilizce policy'nin "politika" anlamı Yunanca politeia'dan ayrı bir köktür
  es póliza ; poliçe
  bg полица [politsa] ; poliçe; raf ; ff:Bulgarcada politsa ayrıca "raf" demektir
  sr полиса [polisa] ; poliçe
  ro poliţă ; poliçe; raf ; ff:Romencede poliţă hem "poliçe" hem "raf" anlamındadır
  ru полис [polis] ; sigorta poliçesi
@çek into_turkish
  en cheque ; çek
  fr chèque ; çek
  de Scheck ; çek
  es cheque ; çek
  it assegno ; çek ; ff:İtalyancada çek için assegno (atanan) kullanılır; köken bağı yoktur
  ru чек [çek] ; kasa fişi; çek ; ff:Rusçada çek öncelikle "kasa fişi" anlamındadır
  bg чек [çek] ; çek
  sr чек [ček] ; çek
  ro cec ; çek
  hu csekk ; çek
  pl czek ; çek
  az çek ; çek
  ar شيك [şīk] ; çek
  fa چک [çek] ; çek ; ff:Farsça çek "mühürlü belge" sözcüğü İngilizce cheque'in uzak kaynağı sayılır
  ur چیک [çek] ; çek
@borsa into_turkish
  it borsa ; çanta; borsa ; ff:İtalyanca borsa önce "kese, çanta" demektir
  fr bourse ; borsa; burs ; ff:Fransızca bourse hem "borsa" hem "burs" anlamındadır
  en bourse ; borsa (Avrupa)
  de Börse ; borsa; cüzdan
  es bolsa ; çanta; borsa ; ff:İspanyolca bolsa "poşet, çanta" ve "borsa" anlamlarındadır
  pt bolsa ; çanta; burs; borsa
  ro bursă ; borsa; burs ; ff:Romencede bursă hem "borsa" hem "burs" demektir
  bg борса [borsa] ; borsa
  sr берза [berza] ; borsa
  mk берза [berza] ; borsa
  sq bursë ; borsa; burs
  ru биржа [birja] ; borsa
  ar بورصة [būrṣa] ; borsa
  az birja ; borsa
@kambiyo into_turkish
  it cambio ; değişim; vites; döviz ; ff:İtalyanca cambio genel "değişim" ve "vites" anlamlarındadır
  es cambio ; değişim; bozuk para; döviz
  fr change ; döviz bozdurma
  en exchange ; değişim; döviz
@iskonto into_turkish
  it sconto ; indirim
  fr escompte ; iskonto
  en discount ; indirim
  de Skonto ; peşin ödeme indirimi
  es descuento ; indirim
@acente into_turkish
  it agente ; temsilci; ajan
  fr agent ; temsilci; ajan
  en agent ; temsilci; ajan
  de Agent ; ajan
  es agente ; temsilci
  ru агент [agent] ; ajan; temsilci
  bg агент [agent] ; ajan
  ro agent ; ajan; temsilci
  az agent ; ajan
@komisyon into_turkish
  fr commission ; komisyon; kurul
  it commissione ; komisyon
  en commission ; komisyon; kurul
  de Kommission ; kurul
  es comisión ; komisyon
  ru комиссия [komissiya] ; kurul; komisyon
  bg комисия [komisiya] ; kurul
  ro comision ; komisyon
  sq komision ; kurul
  az komissiya ; kurul
@sigorta into_turkish
  it sicurtà ; güvence (eskicil) ; ff:İtalyancada sigorta için bugün assicurazione kullanılır; sicurtà eskimiştir
  en security ; güvenlik; menkul kıymet ; ff:İngilizce security "güvenlik" ve "menkul kıymet" demektir; sigorta için insurance kullanılır
  fr sécurité ; güvenlik
  es seguro ; sigorta; güvenli
  pt seguro ; sigorta; güvenli
  sq sigurim ; sigorta
@manifatura into_turkish
  it manifattura ; imalat; fabrika
  en manufacture ; imalat
  fr manufacture ; imalathane
  es manufactura ; imalat
  ru мануфактура [manufaktura] ; imalathane; kumaş ; ff:Rusçada manufaktura ayrıca "dokuma kumaş" anlamındadır
  bg манифактура [manifaktura] ; manifatura
  ro manufactură ; imalathane
@fabrika into_turkish
  it fabbrica ; fabrika
  fr fabrique ; imalathane
  de Fabrik ; fabrika
  es fábrica ; fabrika
  ru фабрика [fabrika] ; fabrika
  bg фабрика [fabrika] ; fabrika
  sr фабрика [fabrika] ; fabrika
  ro fabrică ; fabrika
  el φάμπρικα [fámprika] ; fabrika; dalavere ; ff:Yunanca halk dilinde fámprika "hile, dalavere" anlamında da kullanılır
  pl fabryka ; fabrika
  az fabrik ; fabrika
  uz fabrika ; fabrika
  kk фабрика [fabrika] ; fabrika
@sanayi into_turkish
  ar صناعة [ṣināʿa] ; sanayi; zanaat ; ff:Arapçada ṣināʿa tekildir; Türkçe sanayi çoğul ṣanāʾiʿ biçiminden gelir
  fa صنایع [ṣanāyeʿ] ; sanayi
  ur صنعت [ṣanʿat] ; sanayi
  az sənaye ; sanayi
  uz sanoat ; sanayi
@firma into_turkish
  it firma ; imza ; ff:İtalyanca firma "imza" demektir; şirket anlamı Almanca Firma'dan yayılmıştır
  de Firma ; şirket
  en firm ; şirket; sağlam
  fr firme ; şirket
  es firma ; imza; şirket ; ff:İspanyolca firma öncelikle "imza"dır
  ru фирма [firma] ; şirket
  bg фирма [firma] ; şirket
  sr фирма [firma] ; şirket; tabela
  ro firmă ; şirket; dükkân tabelası ; ff:Romencede firmă ayrıca "dükkân tabelası" anlamındadır
  pl firma ; şirket
  az firma ; şirket
@manifesto into_turkish
  it manifesto ; bildiri; afiş
  en manifesto ; bildiri
  fr manifeste ; bildiri; yük listesi
  es manifiesto ; bildiri; açık
  ru манифест [manifest] ; bildiri
  bg манифест [manifest] ; bildiri
  de Manifest ; bildiri
@tarife into_turkish
  ar تعريف [taʿrīf] ; tanımlama ; ff:Arapçada taʿrīf "tanımlama, bildirme" demektir; ücret listesi anlamı Avrupa dillerinde gelişmiştir
  it tariffa ; tarife
  fr tarif ; tarife
  en tariff ; gümrük vergisi ; ff:İngilizce tariff özellikle "gümrük vergisi" anlamındadır
  de Tarif ; tarife; toplu sözleşme ücreti
  es tarifa ; tarife
  ru тариф [tarif] ; tarife
  bg тарифа [tarifa] ; tarife
  ro tarif ; tarife
  hu tarifa ; tarife
  pl taryfa ; tarife
  az tarif ; tarife
@bütçe into_turkish
  fr budget ; bütçe
  en budget ; bütçe
  de Budget ; bütçe
  ru бюджет [byudjet] ; bütçe
  bg бюджет [byudjet] ; bütçe
  sr буџет [budžet] ; bütçe
  ro buget ; bütçe
  hu büdzsé ; bütçe
  pl budżet ; bütçe
  az büdcə ; bütçe
  uz byudjet ; bütçe
  kk бюджет [byudjet] ; bütçe
@bilanço into_turkish
  it bilancio ; bilanço; denge
  fr bilan ; bilanço; sonuç
  en balance ; denge; bakiye ; ff:İngilizce balance "denge, bakiye" demektir; bilanço için balance sheet kullanılır
  de Bilanz ; bilanço
  es balance ; bilanço; denge
  ru баланс [balans] ; denge; bilanço
  bg баланс [balans] ; denge
  ro bilanţ ; bilanço
  az balans ; denge
@enflasyon into_turkish
  fr inflation ; enflasyon
  en inflation ; enflasyon; şişme
  it inflazione ; enflasyon
  de Inflation ; enflasyon
  es inflación ; enflasyon
  ru инфляция [inflyatsiya] ; enflasyon
  bg инфлация [inflatsiya] ; enflasyon
  sr инфлација [inflacija] ; enflasyon
  ro inflaţie ; enflasyon
  hu infláció ; enflasyon
  pl inflacja ; enflasyon
  az inflyasiya ; enflasyon
  kk инфляция [inflyatsiya] ; enflasyon
@piyasa into_turkish
  it piazza ; meydan ; ff:İtalyanca piazza "meydan" demektir; piyasa anlamı Türkçede gelişmiştir
  fr place ; meydan; yer
  es plaza ; meydan; pazar yeri
  bg пиаца [piatsa] ; pazar yeri
  sr пијаца [pijaca] ; açık pazar ; ff:Sırpçada pijaca "pazar yeri" anlamındadır
  mk пијаца [pijaca] ; pazar yeri
  ro piaţă ; meydan; pazar; piyasa
  el πιάτσα [piátsa] ; taksi durağı; meydan ; ff:Yunancada piátsa "taksi durağı" anlamı öne çıkar
  hu piac ; pazar ; ff:Macarca piac "pazar yeri" aynı İtalyanca piazza'dan gelir
@ekonomi into_turkish
  fr économie ; ekonomi; tasarruf
  en economy ; ekonomi; tasarruf
  de Ökonomie ; ekonomi
  it economia ; ekonomi
  es economía ; ekonomi
  ru экономика [ekonomika] ; ekonomi
  bg икономика [ikonomika] ; ekonomi
  ro economie ; ekonomi; tasarruf
  el οικονομία [ikonomía] ; ekonomi; tasarruf ; ff:Yunanca ikonomía ayrıca "tasarruf" demektir (kánо ikonomía: tasarruf etmek)
  hu ökonómia ; ekonomi
  pl ekonomia ; ekonomi
  kk экономика [ekonomika] ; ekonomi
@iktisat into_turkish
  ar اقتصاد [iqtiṣād] ; ekonomi
  fa اقتصاد [eqteṣād] ; ekonomi
  az iqtisad ; ekonomi
  uz iqtisod ; ekonomi
@inhisar into_turkish
  ar انحصار [inḥiṣār] ; sınırlanma, kısıtlanma
  fa انحصار [enḥeṣār] ; tekel
  ur انحصار [inḥiṣār] ; bağlı olma, dayanma ; ff:Urducada inḥiṣār "bir şeye bağlı olma" anlamındadır
  az inhisar ; tekel
@rekabet into_turkish
  ar رقابة [raqāba] ; denetim; sansür ; ff:Arapçada raqāba "gözetim, sansür" demektir; rekabet için munāfasa kullanılır
  fa رقابت [reqābat] ; rekabet
  ur رقابت [raqābat] ; rekabet; kıskançlık
  az rəqabət ; rekabet
  uz raqobat ; rekabet
@ihracat into_turkish
  ar إخراج [iḫrāc] ; çıkarma; film yönetmenliği ; ff:Arapçada iḫrāc bugün "film yönetimi" anlamında da kullanılır
  az ixracat ; ihracat
@ithalat into_turkish
  ar إدخال [idḫāl] ; içeri sokma; veri girişi ; ff:Arapçada idḫāl "sokma, giriş" demektir; ithalat için istīrād kullanılır
  az idxalat ; ithalat
@döviz into_turkish
  fr devise ; slogan, parola; döviz ; ff:Fransızca devise hem "düstur, slogan" hem "yabancı para" demektir
  en device ; aygıt ; ff:İngilizce device "aygıt" aynı Latince dividere'den türemiştir; para anlamı yoktur
  de Devisen ; döviz
  it divisa ; üniforma; döviz ; ff:İtalyanca divisa öncelikle "üniforma" anlamındadır
  es divisa ; döviz; slogan
  ru девиз [deviz] ; slogan, düstur ; ff:Rusçada deviz yalnızca "slogan, düstur" demektir
  bg девиз [deviz] ; slogan
  ro deviză ; slogan; döviz
  hu deviza ; döviz
  pl dewiza ; slogan
@kur into_turkish
  fr cours ; akış; ders; kur
  en course ; ders; yol ; ff:İngilizce course "ders, rota" demektir; kur için exchange rate kullanılır
  de Kurs ; kur; kurs; rota
  ru курс [kurs] ; kur; kurs; rota ; ff:Rusçada kurs hem "döviz kuru" hem "ders kursu" hem "rota"dır
  bg курс [kurs] ; kur; kurs
  ro curs ; kur; ders
  pl kurs ; kur; kurs
  az kurs ; kurs (ders) ; ff:Azerbaycanca kurs "ders kursu" anlamındadır; döviz kuru için məzənnə kullanılır
@kota into_turkish
  fr quota ; kota
  en quota ; kota
  it quota ; pay; aidat; rakım ; ff:İtalyanca quota ayrıca "rakım, yükselti" demektir
  de Quote ; oran, kota
  es cuota ; aidat; taksit ; ff:İspanyolca cuota "aidat, taksit" anlamındadır
  ru квота [kvota] ; kota
  bg квота [kvota] ; kota
  ro cotă ; pay; kota; rakım
  pl kwota ; tutar, miktar ; ff:Lehçede kwota "para tutarı" anlamına kaymıştır
  hu kvóta ; kota
@sübvansiyon into_turkish
  fr subvention ; sübvansiyon
  en subvention ; sübvansiyon
  de Subvention ; sübvansiyon
  it sovvenzione ; sübvansiyon
  es subvención ; sübvansiyon
  ru субвенция [subventsiya] ; sübvansiyon
  ro subvenţie ; sübvansiyon
  pl subwencja ; sübvansiyon
  hu szubvenció ; sübvansiyon
@teşvik into_turkish
  ar تشويق [taşwīq] ; merak uyandırma ; ff:Arapçada taşwīq "heyecanlandırma, merak uyandırma" demektir
  fa تشویق [taşvīq] ; teşvik; alkışlama ; ff:Farsçada taşvīq ayrıca "alkışlamak" anlamında kullanılır
  az təşviq ; teşvik
  uz tashviq ; teşvik
@tasarruf into_turkish
  ar تصرف [taṣarruf] ; davranış, tutum; kullanım ; ff:Arapçada taṣarruf "davranış; tasarruf yetkisi" demektir; biriktirme anlamı Türkçede gelişmiştir
  fa تصرف [taṣarrof] ; el koyma, işgal ; ff:Farsçada taṣarrof "ele geçirme, işgal" anlamındadır
  ur تصرف [taṣarruf] ; kullanım; tasarruf yetkisi
  az təsərrüfat ; tarım işletmesi; ekonomi ; ff:Azerbaycanca təsərrüfat "işletme, ekonomi" (kənd təsərrüfatı: tarım) anlamındadır
@istihdam into_turkish
  ar استخدام [istiḫdām] ; kullanım ; ff:Arapçada istiḫdām "kullanma" (cihaz, sözcük) demektir; istihdam için tawẓīf kullanılır
  fa استخدام [esteḫdām] ; işe alma
  ur استخدام [istiḫdām] ; kullanım
@reklam into_turkish
  fr réclame ; reklam (eskicil) ; ff:Fransızcada réclame yerini publicité'ye bırakmıştır
  en reclaim ; geri istemek ; ff:İngilizce reclaim "geri almak, ıslah etmek" demektir; reklam için advertisement kullanılır
  de Reklame ; reklam
  ru реклама [reklama] ; reklam
  bg реклама [reklama] ; reklam
  sr реклама [reklama] ; reklam
  ro reclamă ; reklam
  el ρεκλάμα [rekláma] ; reklam
  hu reklám ; reklam
  pl reklama ; reklam
  az reklam ; reklam
  uz reklama ; reklam
@marka into_turkish
  it marca ; marka
  fr marque ; marka; işaret
  en mark ; işaret ; ff:İngilizce mark "işaret" demektir; marka için brand kullanılır
  de Marke ; marka; pul
  es marca ; marka; rekor
  ru марка [marka] ; posta pulu; marka ; ff:Rusçada marka öncelikle "posta pulu" anlamındadır
  bg марка [marka] ; pul; marka
  sr марка [marka] ; pul; marka
  ro marcă ; marka; pul
  hu márka ; marka
  pl marka ; marka
  az marka ; marka; pul
@kapital into_turkish
  fr capital ; sermaye; başlıca
  en capital ; sermaye; başkent; büyük harf ; ff:İngilizce capital ayrıca "başkent" ve "büyük harf" demektir
  de Kapital ; sermaye
  it capitale ; sermaye; başkent
  es capital ; sermaye; başkent
  ru капитал [kapital] ; sermaye
  bg капитал [kapital] ; sermaye
  ro capital ; sermaye
  pl kapitał ; sermaye
  az kapital ; sermaye
  uz kapital ; sermaye
@finans into_turkish
  fr finance ; finans
  en finance ; finans
  de Finanz ; finans
  it finanza ; finans; maliye
  es finanzas ; finans
  ru финансы [finansı] ; finans
  bg финанси [finansi] ; finans
  ro finanţe ; finans
  pl finanse ; finans
@likidite into_turkish
  fr liquidité ; likidite
  en liquidity ; likidite
  de Liquidität ; likidite
  it liquidità ; likidite
  es liquidez ; likidite
  ru ликвидность [likvidnost'] ; likidite
  ro lichiditate ; likidite
  az likvidlik ; likidite
@kartel into_turkish
  fr cartel ; kartel
  en cartel ; kartel
  de Kartell ; kartel
  it cartello ; tabela, afiş ; ff:İtalyanca cartello "tabela, pankart" demektir; kartel için cartello yanında intesa da kullanılır
  es cártel ; kartel
  ru картель [kartel'] ; kartel
  bg картел [kartel] ; kartel
  ro cartel ; kartel
  hu kartell ; kartel
  pl kartel ; kartel
@tröst into_turkish
  en trust ; güven; vakıf; tröst ; ff:İngilizce trust öncelikle "güven" demektir; şirket birliği anlamı ikincildir
  de Trust ; tröst
  fr trust ; tröst
  ru трест [trest] ; tröst
  bg тръст [trıst] ; tröst
  ro trust ; tröst
  pl trust ; tröst
@holding into_turkish
  en holding ; holding; elinde tutma
  fr holding ; holding
  de Holding ; holding
  ru холдинг [holding] ; holding
  bg холдинг [holding] ; holding
  ro holding ; holding
  pl holding ; holding
  az holdinq ; holding
@monopol into_turkish
  fr monopole ; tekel
  en monopoly ; tekel
  de Monopol ; tekel
  it monopolio ; tekel
  es monopolio ; tekel
  ru монополия [monopoliya] ; tekel
  bg монопол [monopol] ; tekel
  ro monopol ; tekel
  el μονοπώλιο [monopólio] ; tekel
  hu monopólium ; tekel
  pl monopol ; tekel
@lisans into_turkish
  fr licence ; izin; lisans
  en license ; ruhsat, lisans
  de Lizenz ; lisans
  it licenza ; izin; lise diploması ; ff:İtalyanca licenza ayrıca "diploma, mezuniyet" anlamındadır
  es licencia ; izin; ruhsat
  ru лицензия [litsenziya] ; lisans
  bg лиценз [litsenz] ; lisans
  ro licenţă ; lisans
  pl licencja ; lisans
  az lisenziya ; lisans
@patent into_turkish
  fr patente ; patent; işyeri vergisi
  en patent ; patent
  de Patent ; patent
  it patente ; sürücü belgesi ; ff:İtalyanca patente "sürücü belgesi, ehliyet" demektir
  es patente ; patent; apaçık
  ru патент [patent] ; patent
  bg патент [patent] ; patent
  pl patent ; patent
  az patent ; patent
@kooperatif into_turkish
  fr coopérative ; kooperatif
  en cooperative ; kooperatif; iş birlikçi
  de Kooperative ; kooperatif
  it cooperativa ; kooperatif
  es cooperativa ; kooperatif
  ru кооператив [kooperativ] ; kooperatif
  bg кооператив [kooperativ] ; kooperatif
  ro cooperativă ; kooperatif
  az kooperativ ; kooperatif
  uz kooperativ ; kooperatif
  kk кооператив [kooperativ] ; kooperatif
@sosyalizm into_turkish
  fr socialisme ; sosyalizm
  en socialism ; sosyalizm
  de Sozialismus ; sosyalizm
  it socialismo ; sosyalizm
  es socialismo ; sosyalizm
  ru социализм [sotsializm] ; sosyalizm
  bg социализъм [sotsializım] ; sosyalizm
  ro socialism ; sosyalizm
  el σοσιαλισμός [sosialismós] ; sosyalizm
  hu szocializmus ; sosyalizm
  pl socjalizm ; sosyalizm
  az sosializm ; sosyalizm
@liberal into_turkish
  fr libéral ; liberal
  en liberal ; liberal; cömert, bol ; ff:İngilizce liberal ayrıca "cömert, bol" anlamındadır
  de liberal ; liberal
  it liberale ; liberal
  es liberal ; liberal
  ru либерал [liberal] ; liberal
  bg либерал [liberal] ; liberal
  ro liberal ; liberal
  pl liberał ; liberal
  hu liberális ; liberal
@dolar into_turkish
  en dollar ; dolar
  de Dollar ; dolar
  fr dollar ; dolar
  ru доллар [dollar] ; dolar
  bg долар [dolar] ; dolar
  sr долар [dolar] ; dolar
  ro dolar ; dolar
  hu dollár ; dolar
  pl dolar ; dolar
  el δολάριο [dolário] ; dolar
  az dollar ; dolar
  kk доллар [dollar] ; dolar
  uz dollar ; dolar
  ar دولار [dūlār] ; dolar
  fa دلار [dolār] ; dolar
  ur ڈالر [ḍālar] ; dolar
@avro into_turkish
  fr euro ; avro
  en euro ; avro
  de Euro ; avro
  it euro ; avro
  es euro ; avro
  ru евро [yevro] ; avro
  bg евро [evro] ; avro
  ro euro ; avro
  el ευρώ [evró] ; avro
  hu euró ; avro
  pl euro ; avro
  az avro ; avro
  kk еуро [euro] ; avro
@sent into_turkish
  en cent ; sent
  fr cent ; sent; yüz
  de Cent ; sent
  it centesimo ; sent
  es centavo ; sent
  ru цент [tsent] ; sent
  bg цент [tsent] ; sent
  ro cent ; sent
  pl cent ; sent
  az sent ; sent
@kriz into_turkish
  fr crise ; kriz
  en crisis ; kriz
  de Krise ; kriz
  it crisi ; kriz
  es crisis ; kriz
  ru кризис [krizis] ; kriz
  bg криза [kriza] ; kriz
  sr криза [kriza] ; kriz
  ro criză ; kriz
  el κρίση [krísi] ; kriz; yargı ; ff:Yunanca krísi "yargı, karar; kriz" anlamlarını birlikte taşır
  hu krízis ; kriz
  pl kryzys ; kriz
@buhran into_turkish
  ar بحران [buḥrān] ; hastalığın dönüm noktası; kriz ; ff:Arapçada buḥrān tıpta "hastalığın dönüm noktası" demektir; ekonomik kriz anlamı Türkçede yaygındır
  fa بحران [boḥrān] ; kriz
  ur بحران [buḥrān] ; kriz
  az böhran ; kriz
@fuar into_turkish
  fr foire ; fuar; panayır
  en fair ; panayır; adil ; ff:İngilizce fair "panayır" (feria) ile "adil" (Cermen) iki ayrı kökten eş seslidir
  it fiera ; fuar
  es feria ; panayır; fuar; bayram
  pt feira ; pazar; fuar ; ff:Portekizce feira "haftalık pazar" demektir (segunda-feira: pazartesi)
@panayır into_turkish
  el πανηγύρι [paniyíri] ; şenlik, panayır
  bg панаир [panair] ; panayır
  sr панађур [panađur] ; panayır
  mk панаѓур [panaǵur] ; panayır
  sq panair ; panayır
@narh into_turkish
  fa نرخ [nerḫ] ; fiyat; döviz kuru ; ff:Farsçada nerḫ bugün "fiyat; kur" anlamındadır
  ur نرخ [narḫ] ; fiyat, oran
  az nırx ; fiyat
  uz narx ; fiyat ; ff:Özbekçede narx genel olarak "fiyat" demektir
  kk нарық [narıq] ; piyasa ; ff:Kazakçada narıq "piyasa, pazar ekonomisi" anlamına kaymıştır
  ky нарк [nark] ; fiyat, değer
@muhtesip into_turkish
  ar محتسب [muḥtasib] ; çarşı denetçisi
  fa محتسب [moḥtaseb] ; muhtesip
  ur محتسب [muḥtasib] ; ombudsman ; ff:Pakistan'da muḥtasib "ombudsman, kamu denetçisi" unvanıdır
@öşür into_turkish
  ar عشر [ʿuşr] ; onda bir
  fa عشر [ʿoşr] ; öşür
  ur عشر [ʿuşr] ; öşür
  bg юшур [yuşur] ; öşür (tarihî)
  sr ушур [ušur] ; değirmen hakkı ; ff:Sırpçada ušur "değirmencinin öğütme payı" anlamına kaymıştır
  mk ушур [ušur] ; öşür
  sq ushur ; öşür
@tımar into_turkish
  fa تیمار [tīmār] ; hasta bakımı ; ff:Farsçada tīmār "hasta bakımı, hemşirelik" demektir; dirlik anlamı Osmanlı kurumudur
  ur تیمار [tīmār] ; bakım
  az timar ; bakım (hayvan)
  bg тимар [timar] ; tımar (tarihî)
  sr тимар [timar] ; tımar (tarihî)
  sq timar ; tımar (tarihî)
  hu tímár ; derici, tabakçı ; ff:Macarca tímár "derici" başka bir kökten gelir; ses benzerliği rastlantısaldır
@defterdar into_turkish
  fa دفتردار [daftardār] ; defterdar
  ar دفتردار [daftardār] ; defterdar (Osmanlı Mısırı)
  ur دفتردار [daftardār] ; kayıt memuru
  az dəftərdar ; defterdar
  bg дефтердар [defterdar] ; defterdar (tarihî)
  sr дефтердар [defterdar] ; defterdar (tarihî)
  sq defterdar ; defterdar
@vezne into_turkish
  ar وزن [wazn] ; ağırlık; şiir ölçüsü ; ff:Arapçada wazn "ağırlık, ölçü" demektir; kasa anlamı Türkçede gelişmiştir
  fa وزن [vazn] ; ağırlık; vezin
  ur وزن [vazan] ; ağırlık
  az vəzn ; ağırlık; vezin
  uz vazn ; ağırlık
@fersah into_turkish
  fa فرسنگ [farsang] ; fersah
  ar فرسخ [farsaḫ] ; fersah
  ur فرسنگ [farsang] ; fersah
  en parasang ; fersah
  el παρασάγγης [parasángis] ; fersah
  uz farsax ; fersah
@karış shared_ancestor
  az qarış ; karış
  kk қарыс [qarıs] ; karış
  uz qarich ; karış
  ky карыш [karış] ; karış
  tk garyş ; karış
  hu arasz ; karış ; ff:Macarca arasz Eski Türkçe karış'tan erken dönemde alınmıştır
@kulaç shared_ancestor
  az qulac ; kulaç
  kk құлаш [qulaş] ; kulaç
  uz quloch ; kulaç
  ky кулач [kulaç] ; kulaç
  tk gulaç ; kulaç
@parmak shared_ancestor
  az barmaq ; parmak
  kk бармақ [barmaq] ; başparmak ; ff:Kazakçada barmaq "başparmak" anlamına daralmıştır; parmak için sausaq kullanılır
  uz barmoq ; parmak
  ky бармак [barmak] ; parmak
  tk barmak ; parmak
@gram into_turkish
  fr gramme ; gram
  en gram ; gram
  de Gramm ; gram
  it grammo ; gram
  es gramo ; gram
  ru грамм [gramm] ; gram
  bg грам [gram] ; gram
  ro gram ; gram
  el γραμμάριο [grammário] ; gram
  hu gramm ; gram
  pl gram ; gram
  az qram ; gram
  kk грамм [gramm] ; gram
  ar غرام [ġrām] ; gram
  fa گرم [geram] ; gram
@kilo into_turkish
  fr kilo ; kilo
  en kilo ; kilo
  de Kilo ; kilo
  it chilo ; kilo
  es kilo ; kilo
  ru кило [kilo] ; kilo
  bg кило [kilo] ; kilo
  el κιλό [kiló] ; kilo
  hu kiló ; kilo
  az kilo ; kilo
  ar كيلو [kīlū] ; kilo
  fa کیلو [kīlū] ; kilo
  ur کلو [kilo] ; kilo
@litre into_turkish
  fr litre ; litre
  en litre ; litre
  de Liter ; litre
  it litro ; litre
  es litro ; litre
  ru литр [litr] ; litre
  bg литър [litır] ; litre
  ro litru ; litre
  el λίτρο [lítro] ; litre
  hu liter ; litre
  pl litr ; litre
  az litr ; litre
  kk литр [litr] ; litre
  uz litr ; litre
  ar لتر [litr] ; litre
  fa لیتر [lītr] ; litre
@ton into_turkish
  fr tonne ; ton
  en ton ; ton
  de Tonne ; ton; fıçı
  it tonnellata ; ton
  es tonelada ; ton
  ru тонна [tonna] ; ton
  bg тон [ton] ; ton
  ro tonă ; ton
  el τόνος [tónos] ; ton; vurgu ; ff:Yunanca tónos "vurgu, ses tonu" ile ağırlık birimi eş seslidir
  hu tonna ; ton
  pl tona ; ton
  az ton ; ton
  kk тонна [tonna] ; ton
@mil into_turkish
  en mile ; mil
  fr mille ; mil; bin
  de Meile ; mil
  it miglio ; mil
  es milla ; mil
  ru миля [milya] ; mil
  bg миля [milya] ; mil
  ro milă ; mil; merhamet ; ff:Romencede milă "merhamet" ile "mil" eş seslidir
  pl mila ; mil
  az mil ; mil
  ar ميل [mīl] ; mil
@hektar into_turkish
  fr hectare ; hektar
  en hectare ; hektar
  de Hektar ; hektar
  it ettaro ; hektar
  es hectárea ; hektar
  ru гектар [gektar] ; hektar
  bg хектар [hektar] ; hektar
  ro hectar ; hektar
  hu hektár ; hektar
  pl hektar ; hektar
  az hektar ; hektar
  uz gektar ; hektar
  kk гектар [gektar] ; hektar
@sterlin into_turkish
  en sterling ; sterlin
  fr sterling ; sterlin
  de Sterling ; sterlin
  bg стерлинг [sterling] ; sterlin
  ro sterlină ; sterlin
  el στερλίνα [sterlína] ; sterlin
  ar إسترليني [istarlīnī] ; sterlin
  az sterlinq ; sterlin
@frank into_turkish
  fr franc ; frank; açık sözlü ; ff:Fransızca franc "özgür, açık sözlü" sıfatı ile para birimi aynı Frank halk adından gelir
  en franc ; frank
  de Franken ; frank (İsviçre)
  it franco ; frank; açık sözlü
  es franco ; frank; açık
  ru франк [frank] ; frank
  bg франк [frank] ; frank
  ro franc ; frank
  hu frank ; frank
  pl frank ; frank
  ar فرنك [farank] ; frank
  fa فرانک [ferānk] ; frank
  az frank ; frank
@ruble into_turkish
  ru рубль [rubl'] ; ruble
  uk рубль [rubl'] ; ruble
  en rouble ; ruble
  fr rouble ; ruble
  de Rubel ; ruble
  bg рубла [rubla] ; ruble
  ro rublă ; ruble
  kk рубль [rubl'] ; ruble
  az rubl ; ruble
  fa روبل [rūbl] ; ruble
  ar روبل [rūbl] ; ruble
  mn рубль [rubl'] ; ruble
@rupi into_turkish
  en rupee ; rupi
  fr roupie ; rupi
  de Rupie ; rupi
  ru рупия [rupiya] ; rupi
  ur روپیہ [rūpiya] ; rupi
  fa روپیه [rūpiye] ; rupi
  ar روبية [rūbiya] ; rupi
  bg рупия [rupiya] ; rupi
  ro rupie ; rupi
@riyal into_turkish
  ar ريال [riyāl] ; riyal
  fa ریال [riyāl] ; riyal
  ur ریال [riyāl] ; riyal
  en riyal ; riyal
  es real ; eski İspanyol sikkesi; kraliyete ait ; ff:İspanyolca real "kraliyete ait" (regalis) sıfatı riyalin kaynağıdır
  pt real ; Brezilya para birimi
  ru риал [rial] ; riyal
@peso into_turkish
  es peso ; ağırlık; peso ; ff:İspanyolca peso önce "ağırlık" demektir (Latince pensum)
  en peso ; peso
  fr peso ; peso
  it peso ; ağırlık ; ff:İtalyanca peso yalnızca "ağırlık" anlamındadır
  pt peso ; ağırlık
  ru песо [peso] ; peso
@drahmi into_turkish
  el δραχμή [drakhmí] ; drahmi
  en drachma ; drahmi
  fr drachme ; drahmi
  de Drachme ; drahmi
  it dracma ; drahmi
  ru драхма [drahma] ; drahmi
  bg драхма [drahma] ; drahmi
  ro drahmă ; drahmi
@zolota into_turkish
  pl złoty ; altın (renkli); Polonya para birimi ; ff:Lehçe złoty "altın" sıfatından; Osmanlı'da zolota adıyla dolaşan Leh sikkesidir
  ru злотый [zlotıy] ; zloti
  uk злотий [zlotıy] ; zloti
  ro zlot ; zloti
  hu zloty ; zloti
  en zloty ; zloti
  de Zloty ; zloti
@banknot into_turkish
  en banknote ; banknot
  de Banknote ; banknot
  it banconota ; banknot
  ru банкнота [banknota] ; banknot
  bg банкнота [banknota] ; banknot
  ro bancnotă ; banknot
  pl banknot ; banknot
  az banknot ; banknot
@ipotek into_turkish
  fr hypothèque ; ipotek
  de Hypothek ; ipotek
  it ipoteca ; ipotek
  es hipoteca ; ipotek
  ru ипотека [ipoteka] ; ipotek; konut kredisi
  bg ипотека [ipoteka] ; ipotek
  sr хипотека [hipoteka] ; ipotek
  ro ipotecă ; ipotek
  el υποθήκη [ipothíki] ; ipotek; öğüt ; ff:Yunanca ipothíki ayrıca "öğüt, nasihat" demektir
  pl hipoteka ; ipotek
  az ipoteka ; ipotek
@kefalet into_turkish
  ar كفالة [kafāla] ; kefalet; sponsorluk ; ff:Körfez ülkelerinde kafāla göçmen işçilerin sponsorluk sistemidir
  fa کفالت [kefālat] ; kefalet
  ur کفالت [kafālat] ; geçindirme, bakma ; ff:Urducada kafālat "birinin geçimini üstlenme" anlamındadır
  az kəfalət ; kefalet
  uz kafolat ; garanti ; ff:Özbekçede kafolat "garanti, teminat" demektir
  kk кепілдік [kepildik] ; garanti
@iflas into_turkish
  ar إفلاس [iflās] ; iflas
  ar فلس [fils] ; en küçük para birimi (Irak, Ürdün) ; ff:iflas sözcüğü "tek filsi kalmamak" anlamından türemiştir
  az iflas ; iflas
  sq iflas ; iflas (halk dili)
@hisse into_turkish
  ar حصة [ḥiṣṣa] ; pay; ders saati ; ff:Arapçada ḥiṣṣa ayrıca "okul dersi, ders saati" demektir
  fa حصه [heṣṣe] ; pay
  ur حصہ [ḥiṣṣa] ; pay, bölüm
  az hissə ; parça, bölüm ; ff:Azerbaycanca hissə "parça, bölüm" anlamındadır; hisse senedi için səhm kullanılır
  uz hissa ; pay, katkı
  sq hise ; pay
@tahvil into_turkish
  ar تحويل [taḥwīl] ; dönüştürme; para transferi ; ff:Arapçada taḥwīl "havale, dönüştürme" demektir; tahvil anlamı Türkçede gelişmiştir
  fa تحویل [taḥvīl] ; teslim etme ; ff:Farsçada taḥvīl "teslim" anlamındadır
  ur تحویل [taḥvīl] ; gözaltı; muhafaza ; ff:Urducada taḥvīl "gözetim, muhafaza" anlamına kaymıştır
  az təhvil ; teslim ; ff:Azerbaycanca təhvil "teslim" demektir
@emlak into_turkish
  ar أملاك [amlāk] ; mülkler
  fa املاک [amlāk] ; emlak
  ur املاک [amlāk] ; mülkler
  az əmlak ; emlak
@vade into_turkish
  ar وعد [waʿd] ; söz, vaat ; ff:Arapçada waʿd "söz" demektir; süre anlamı Türkçede gelişmiştir
  fa وعده [vaʿde] ; söz; randevu ; ff:Farsçada vaʿde ayrıca "randevu" anlamındadır
  ur وعدہ [vaʿda] ; söz
  az vədə ; söz; vade
  uz va'da ; söz
  kk уәде [uäde] ; söz
@arz into_turkish
  ar عرض [ʿarḍ] ; sunum; en, genişlik ; ff:Arapçada ʿarḍ "sunma" ile "en, genişlik" aynı köktendir; ekonomik arz için ʿarḍ wa ṭalab denir
  fa عرض [ʿarż] ; en, genişlik ; ff:Farsçada ʿarż öncelikle "en, genişlik" demektir
  ur عرض [ʿarz] ; dilekçe, arz
  az ərz ; arz
@talep into_turkish
  ar طلب [ṭalab] ; istek; sipariş
  fa طلب [ṭalab] ; alacak ; ff:Farsçada ṭalab "alacak" anlamını da taşır (ṭalabkār: alacaklı)
  ur طلب [ṭalab] ; istek; çağrı
  az tələb ; talep
  uz talab ; talep
  kk талап [talap] ; gereklilik, şart ; ff:Kazakçada talap "gereklilik, koşul" anlamındadır
  ky талап [talap] ; istek, gereklilik
@kıymet into_turkish
  ar قيمة [qīma] ; değer
  fa قیمت [qeymat] ; fiyat ; ff:Farsçada qeymat "fiyat" demektir
  ur قیمت [qīmat] ; fiyat ; ff:Urducada qīmat "fiyat" anlamındadır
  az qiymət ; fiyat; not ; ff:Azerbaycanca qiymət "fiyat" ve "okul notu" anlamlarındadır
  uz qiymat ; değer
  kk қымбат [qımbat] ; pahalı ; ff:Kazakçada qımbat "pahalı" sıfatıdır
  ky кымбат [kımbat] ; pahalı ; ff:Kırgızcada kımbat "pahalı" anlamına kaymıştır
  tk gymmat ; pahalı ; ff:Türkmencede gymmat "pahalı" demektir
@bedel into_turkish
  ar بدل [badal] ; karşılık; takım elbise ; ff:Mısır Arapçasında badla "takım elbise" demektir
  fa بدل [badal] ; sahte, taklit ; ff:Farsçada badal "imitasyon, sahte" anlamındadır (badal-e cevāher: imitasyon mücevher)
  ur بدل [badal] ; değişim; karşılık
  az bədəl ; bedel
  uz badal ; karşılık
@mübadele into_turkish
  ar مبادلة [mubādala] ; değiş tokuş
  fa مبادله [mobādele] ; değiş tokuş
  ur مبادلہ [mubādala] ; değiş tokuş
  az mübadilə ; mübadele
@takas into_turkish
  ar تقاص [taqāṣṣ] ; ödeşme; mahsup
  fa تقاص [taqāṣ] ; intikam ; ff:Farsçada taqāṣ "intikam alma, öç" anlamındadır
@ücret into_turkish
  ar أجرة [ucra] ; kira; yol ücreti ; ff:Arapçada ucra özellikle "taksi ücreti, kira" anlamındadır
  fa اجرت [ocrat] ; ücret
  ur اجرت [ujrat] ; ücret
@maaş into_turkish
  ar معاش [maʿāş] ; emekli aylığı; geçim ; ff:Arapçada maʿāş "emekli aylığı" anlamındadır; maaş için rātib kullanılır
  fa معاش [maʿāş] ; geçim ; ff:Farsçada maʿāş "geçim" demektir; maaş için ḥoqūq kullanılır
  ur معاش [maʿāş] ; geçim; ekonomi ; ff:Urducada maʿāşiyāt "ekonomi bilimi" demektir
  az maaş ; maaş
  uz maosh ; maaş
@harç into_turkish
  ar خرج [ḫarc] ; masraf; cep harçlığı
  fa خرج [ḫarc] ; masraf
  ur خرچ [ḫarç] ; masraf
  az xərc ; masraf
  uz xarj ; masraf
  kk қаржы [qarjı] ; finans, para ; ff:Kazakçada qarjı "finans, mali kaynak" anlamına kaymıştır
  ky каржы [karjı] ; finans
  bg харч [harç] ; masraf
  sr харчити [harčiti] ; harcamak
  mk харчи [harči] ; harcar
  sq harxh ; masraf
  el χαρτζιλίκι [hartzilíki] ; cep harçlığı
@harçlık from_turkish
  bg харчлък [harçlık] ; harçlık
  sq harçllëk ; harçlık
@mal into_turkish
  ar مال [māl] ; mal; para
  fa مال [māl] ; mal; -ın (iyelik) ; ff:Farsçada māl ayrıca iyelik ilgeci olarak kullanılır (māl-e man: benimki)
  ur مال [māl] ; mal; servet
  az mal ; mal; sığır
  uz mol ; sığır, hayvan ; ff:Özbekçede mol "sığır, davar" anlamına daralmıştır
  kk мал [mal] ; evcil hayvan, davar ; ff:Kazakçada mal "hayvan sürüsü" demektir
  ky мал [mal] ; hayvan
  tk mal ; hayvan; mal
  mn мал [mal] ; hayvan sürüsü ; ff:Moğolca mal "evcil hayvan" anlamındadır
  sq mall ; mal, eşya
@fakir into_turkish
  ar فقير [faqīr] ; yoksul
  fa فقیر [faqīr] ; yoksul
  ur فقیر [faqīr] ; derviş; dilenci ; ff:Urducada faqīr "derviş, gezgin dilenci" anlamı öne çıkar
  en fakir ; fakir, derviş ; ff:İngilizce fakir "Hint dervişi, hokkabaz" demektir
  uz faqir ; yoksul
  bg факир [fakir] ; hokkabaz ; ff:Bulgarcada fakir "sihirbaz, hokkabaz" anlamındadır
  sr факир [fakir] ; hokkabaz ; ff:Sırpçada fakir "hokkabaz" demektir
  ru факир [fakir] ; hokkabaz ; ff:Rusçada fakir "sirk hokkabazı" anlamında kullanılır
  el φακίρης [fakíris] ; hokkabaz ; ff:Yunancada fakíris "hokkabaz, sihirbaz" anlamındadır
@zengin into_turkish
  fa سنگین [sangīn] ; ağır ; ff:Farsça sangīn "taş gibi ağır" demektir; varlıklı anlamı Türkçede gelişmiştir
  az zəngin ; zengin
  bg зенгин [zengin] ; zengin (halk dili)
  sq zengjin ; zengin
@elmas into_turkish
  ar ألماس [almās] ; elmas
  fa الماس [almās] ; elmas
  ur الماس [almās] ; elmas
  az almaz ; elmas
  uz olmos ; elmas
  kk алмас [almas] ; elmas
  ky алмаз [almaz] ; elmas
  tk almaz ; elmas
  ru алмаз [almaz] ; işlenmemiş elmas ; ff:Rusçada almaz "ham elmas"tır; işlenmiş elmas için brilliant kullanılır
  sq elmaz ; elmas
  ka ალმასი [almasi] ; elmas
  hy ադամանդ [adamand] ; elmas ; ff:Ermenice adamand Yunanca adámas'tan doğrudan alınmıştır
@cevher into_turkish
  ar جوهر [cawhar] ; öz, töz; mücevher
  fa گوهر [gowhar] ; mücevher; öz
  ur جوہر [jauhar] ; öz; mücevher
  az cövhər ; cevher
  uz javhar ; cevher
@pırlanta into_turkish
  it brillante ; parlak; pırlanta
  fr brillant ; parlak; pırlanta
  en brilliant ; parlak; zekice ; ff:İngilizce brilliant sıfattır; pırlanta için diamond kullanılır
  de Brillant ; pırlanta
  ru бриллиант [brilliant] ; pırlanta
  bg брилянт [brilyant] ; pırlanta
  ro briliant ; pırlanta
  az brilyant ; pırlanta
@gümüş shared_ancestor
  az gümüş ; gümüş
  kk күміс [kümis] ; gümüş
  uz kumush ; gümüş
  ky күмүш [kümüş] ; gümüş
  tk kümüş ; gümüş
@ipek shared_ancestor
  az ipək ; ipek
  kk жібек [jibek] ; ipek
  uz ipak ; ipek
  ky жибек [jibek] ; ipek
  tk ýüpek ; ipek
@yün shared_ancestor
  az yun ; yün
  kk жүн [jün] ; yün
  uz jun ; yün
  ky жүн [jün] ; yün
  tk ýüň ; yün
@deri shared_ancestor
  az dəri ; deri
  kk тері [teri] ; deri
  uz teri ; deri
  ky тери [teri] ; deri
  tk deri ; deri
@kürk shared_ancestor
  az kürk ; kürk
  bg кюрк [kyurk] ; kürk
  sr ћурак [ćurak] ; kürk kaftan
  mk ќурк [ḱurk] ; kürk
@pamuk into_turkish
  fa پنبه [panbe] ; pamuk
  az pambıq ; pamuk
  hu pamut ; pamuk ; ff:Macarca pamut Osmanlı Türkçesinden alınmıştır
  bg памук [pamuk] ; pamuk
  sr памук [pamuk] ; pamuk
  mk памук [pamuk] ; pamuk
  sq pambuk ; pamuk
  el μπαμπάκι [bambáki] ; pamuk
  ro bumbac ; pamuk ; ff:Romence bumbac aynı Farsça kökten ayrı bir yolla (Orta Latince bombax) gelmiştir
@kumaş into_turkish
  ar قماش [qumāş] ; kumaş
  fa قماش [qomāş] ; kumaş; çeşit
  az qumaş ; kumaş
  bg кумаш [kumaş] ; kumaş (halk dili)
  sq kumash ; kumaş
@tezgâh into_turkish
  fa دستگاه [dastgāh] ; aygıt, makine; sistem ; ff:Farsçada dastgāh "cihaz, makine; sistem" anlamındadır
  az dəzgah ; tezgâh
  bg тезгях [tezgyah] ; tezgâh
  sr тезга [tezga] ; pazar tezgâhı; kayıt dışı iş ; ff:Sırpçada tezga mecazen "kaçak ek iş" anlamında da kullanılır
  mk тезга [tezga] ; tezgâh
  sq tezgë ; tezgâh
  ro tejghea ; tezgâh
  el τεζιάκι [teziáki] ; tezgâh
@raf into_turkish
  ar رف [raff] ; raf
  fa رف [raf] ; raf
  bg рафт [raft] ; raf
  sr раф [raf] ; raf
  mk раф [raf] ; raf
  sq raft ; raf
  ro raft ; raf
  el ράφι [ráfi] ; raf
@dolap into_turkish
  ar دولاب [dūlāb] ; tekerlek; dolap ; ff:Arapçada dūlāb öncelikle "tekerlek, çark" demektir
  fa دولاب [dūlāb] ; dolap; çark
  bg долап [dolap] ; dolap
  sr долап [dolap] ; dolap; su çarkı
  mk долап [dolap] ; dolap
  sq dollap ; dolap
  ro dulap ; dolap
  el ντουλάπα [doulápa] ; dolap
@vitrin into_turkish
  fr vitrine ; vitrin
  en vitrine ; cam dolap
  de Vitrine ; vitrin
  ru витрина [vitrina] ; vitrin
  bg витрина [vitrina] ; vitrin
  ro vitrină ; vitrin
  az vitrin ; vitrin
@kepenk from_turkish
  bg кепенк [kepenk] ; kepenk
  sr ћепенак [ćepenak] ; dükkân kepengi; tezgâh
  mk ќепенок [ḱepenok] ; kepenk
  sq qepen ; kepenk
  el κεπέγκι [kepéngi] ; kepenk
@siftah from_turkish
  bg сефте [sefte] ; ilk satış
  sr сефте [sefte] ; ilk satış; ilk kez
  mk сефте [sefte] ; ilk kez
  sq sefte ; ilk kez
  ro saftea ; ilk satış
  el σεφτές [seftés] ; ilk satış
@kapora into_turkish
  it caparra ; kapora
  bg капаро [kaparo] ; kapora
  sr капара [kapara] ; kapora
  mk капар [kapar] ; kapora
  sq kapar ; kapora
  el καπάρο [kapáro] ; kapora
@taksit into_turkish
  ar تقسيط [taqsīṭ] ; taksitlendirme
  fa قسط [qesṭ] ; taksit
  ur قسط [qisṭ] ; taksit
  bg таксит [taksit] ; taksit
@peşin into_turkish
  fa پیشین [pīşīn] ; önceki, eski ; ff:Farsçada pīşīn "önceki, eski" demektir; peşin ödeme anlamı Türkçede gelişmiştir
  bg пешин [peşin] ; peşin
  mk пешин [pešin] ; peşin
  sq peshin ; peşin
@servet into_turkish
  ar ثروة [ṯarwa] ; servet
  fa ثروت [servat] ; servet
  az sərvət ; servet
@maliye into_turkish
  ar مالية [māliyya] ; maliye; finans
  fa مالیه [māliye] ; maliye
  ur مالیات [māliyāt] ; vergi ; ff:Urducada māliyāt "vergi, vergilendirme" anlamındadır
  az maliyyə ; finans
  uz moliya ; finans
@tamga shared_ancestor
  mn тамга [tamga] ; mühür
  kk таңба [tañba] ; işaret; damga
  az damğa ; damga
  uz tamg'a ; damga
  ky тамга [tamga] ; damga
  ru таможня [tamojnya] ; gümrük ; ff:Rusça tamojnya "gümrük" Türkçe tamga'dan türemiştir; damga vurulan vergi anlamından
@satmak shared_ancestor
  az satmaq ; satmak
  kk сату [satu] ; satmak
  uz sotmoq ; satmak
  ky сатуу [satuu] ; satmak
  tk satmak ; satmak
@almak shared_ancestor
  az almaq ; almak
  kk алу [alu] ; almak
  uz olmoq ; almak
  ky алуу [aluu] ; almak
  tk almak ; almak
@ödemek shared_ancestor
  az ödəmək ; ödemek
  kk өтеу [öteu] ; ödemek; telafi etmek ; ff:Kazakçada öteu "ödemek; karşılığını vermek, telafi etmek" anlamındadır
  ky өтөө [ötöö] ; ödemek; yerine getirmek
  tk ödemek ; ödemek
@kazanç shared_ancestor
  az qazanc ; kazanç
  tk gazanç ; kazanç
  uz qozonmoq ; kazanmak
@yük shared_ancestor
  az yük ; yük
  kk жүк [jük] ; yük
  uz yuk ; yük
  ky жүк [jük] ; yük
  tk ýük ; yük
@emek shared_ancestor
  az əmək ; emek
  kk еңбек [eñbek] ; emek
  ky эмгек [emgek] ; emek
@işçi shared_ancestor
  az işçi ; işçi; çalışan
  uz ishchi ; işçi
  tk işçi ; işçi
@yağma into_turkish
  fa یغما [yaġmā] ; yağma
  az yağma ; yağma
  uz yag'mo ; yağma
@ganimet into_turkish
  ar غنيمة [ġanīma] ; ganimet
  fa غنیمت [ġanīmat] ; ganimet; fırsat
  ur غنیمت [ġanīmat] ; fırsat; şükredilecek şey ; ff:Urducada ġanīmat "iyi ki, fırsat" anlamına kaymıştır
  az qənimət ; ganimet
  uz g'animat ; ganimet
@istif into_turkish
  el στοίβα [stíva] ; yığın
  el στοιβάζω [stivázo] ; istiflemek
@stok into_turkish
  en stock ; stok; hisse senedi ; ff:İngilizce stock ayrıca "hisse senedi" demektir
  fr stock ; stok
  ro stoc ; stok
  ru сток [stok] ; akıntı, gider ; ff:Rusça stok "akış, drenaj" başka bir köktendir; ses benzerliği rastlantısaldır
@envanter into_turkish
  fr inventaire ; envanter
  en inventory ; envanter
  de Inventar ; demirbaş
  it inventario ; envanter
  es inventario ; envanter
  ru инвентарь [inventar'] ; demirbaş, donatım ; ff:Rusçada inventar' "demirbaş eşya" anlamındadır
  bg инвентар [inventar] ; envanter
  ro inventar ; envanter
  pl inwentarz ; envanter; hayvan varlığı
@kargo into_turkish
  en cargo ; yük
  es cargo ; görev, makam; suçlama ; ff:İspanyolca cargo "görev, makam" ve "suçlama" demektir; yük için carga kullanılır
  fr cargo ; yük gemisi ; ff:Fransızca cargo "yük gemisi" anlamındadır
  it carico ; yük
  pt carga ; yük
@navlun into_turkish
  el ναύλος [návlos] ; navlun
  ar نولون [nawlūn] ; navlun
  it nolo ; kiralama; navlun ; ff:İtalyanca nolo aynı Yunanca kökten "kiralama ücreti" anlamındadır
@transit into_turkish
  fr transit ; transit
  en transit ; geçiş; toplu taşıma ; ff:İngilizce transit ayrıca "toplu taşıma" demektir
  de Transit ; transit
  it transito ; geçiş
  es tránsito ; trafik ; ff:İspanyolca tránsito "trafik" anlamındadır
  ru транзит [tranzit] ; transit
  bg транзит [tranzit] ; transit
  ro tranzit ; transit
  pl tranzyt ; transit
  hu tranzit ; transit
  az tranzit ; transit
@sendika into_turkish
  fr syndicat ; sendika
  en syndicate ; suç örgütü; konsorsiyum ; ff:İngilizce syndicate "şirketler birliği; çete" demektir; sendika için union kullanılır
  de Syndikat ; konsorsiyum
  it sindacato ; sendika
  es sindicato ; sendika
  ru синдикат [sindikat] ; şirket birliği ; ff:Rusçada sindikat "tekelci şirket birliği" anlamındadır
  bg синдикат [sindikat] ; sendika
  ro sindicat ; sendika
  el συνδικάτο [sindikáto] ; sendika
  pl syndykat ; konsorsiyum
@grev into_turkish
  fr grève ; grev; çakıllı kıyı ; ff:Fransızca grève önce "çakıllı kıyı" demektir; Paris'teki Place de Grève işsizlerin toplandığı yerdi
  ro grevă ; grev
  sq grevë ; grev
  pt greve ; grev
@patron into_turkish
  fr patron ; patron; kalıp
  en patron ; hami; müşteri ; ff:İngilizce patron "hami, destekçi; sürekli müşteri" demektir; işveren için boss kullanılır
  it padrone ; patron; sahip
  es patrón ; patron; kalıp
  ru патрон [patron] ; fişek; hami ; ff:Rusçada patron öncelikle "fişek" anlamındadır
  bg патрон [patron] ; fişek; hami
  ro patron ; patron
  sq patron ; patron
@meta into_turkish
  ar متاع [matāʿ] ; eşya, mal
  fa متاع [matāʿ] ; mal, meta
  ur متاع [matāʿ] ; eşya; servet
@emtia into_turkish
  ar أمتعة [amtiʿa] ; bagaj, eşya ; ff:Arapçada amtiʿa bugün "bagaj, kişisel eşya" anlamındadır
  az əmtəə ; ticaret malı
@müzayede into_turkish
  ar مزايدة [muzāyada] ; müzayede
  fa مزایده [mozāyede] ; müzayede
@mültezim into_turkish
  ar ملتزم [multazim] ; bağlı; sorumluluk üstlenen ; ff:Arapçada multazim "taahhüt eden, bağlı" demektir; vergi toplama hakkı anlamı Osmanlı kurumudur
  fa ملتزم [moltazem] ; yükümlü
@senet into_turkish
  ar سند [sanad] ; dayanak; belge
  fa سند [sanad] ; belge; tapu ; ff:Farsçada sanad "belge, tapu" anlamındadır
  ur سند [sanad] ; belge, sertifika
  az sənəd ; belge ; ff:Azerbaycanca sənəd genel olarak "belge" demektir
@akar into_turkish
  ar عقار [ʿaqār] ; taşınmaz
  fa عقار [ʿaqār] ; taşınmaz
  ur عقار [ʿaqār] ; taşınmaz
"""
