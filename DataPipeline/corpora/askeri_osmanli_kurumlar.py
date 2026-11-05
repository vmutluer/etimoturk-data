# -*- coding: utf-8 -*-
"""Korpus 19 — Askerlik, Osmanlı devlet kurumları ve unvanlar."""

WORDS = r"""
# --- Rütbeler ve askerî birlikler -------------------------------------------------
onbaşı|n|tr|on başı|on erin başı|OSM|*baş|
yüzbaşı|n|tr|yüz başı|yüz erin başı|OSM|*baş|
binbaşı|n|tr|biŋ başı|bin erin başı|OSM|*baş|
başçavuş|n|tr|baş çavuş|çavuşların başı|CUM|*baş|
albay|n|tr|alay beyi|alay komutanı|DD|*bek|
yarbay|n|tr|yar(dımcı) bay|albay yardımcısı|DD|*bek|
general|n|fr|général|genel komutan|OSM19|genus|la:generalis>fr:général>tr:general
tuğgeneral|n|tr|tuğ general|tuğay komutanı general|DD|*tuğ|
tümgeneral|n|tr|tüm(en) general|tümen komutanı general|DD|*tüm|
korgeneral|n|tr|kor general|kolordu komutanı general|DD|*kor|
orgeneral|n|tr|or(du) general|ordu komutanı general|DD|*ordu|
mareşal|n|fr|maréchal|at bakıcısı; en üst komutan|OSM19||ger:marah-skalk>fro:mareschal>fr:maréchal>tr:mareşal
amiral|n|fr|amiral|deniz komutanı|OSM|E-M-R|ar:amīr al-baḥr>fr:amiral>tr:amiral
tuğamiral|n|tr|tuğ amiral|en alt rütbeli amiral|DD|*tuğ|
tümamiral|n|tr|tüm amiral|tümgeneral karşılığı amiral|DD|*tüm|
koramiral|n|tr|kor amiral|korgeneral karşılığı amiral|DD|*kor|
oramiral|n|tr|or amiral|orgeneral karşılığı amiral|DD|*ordu|
teğmen|n|tr|teğmen|değen, denk gelen; en alt subay|DD|*teg-|
üsteğmen|n|tr|üst teğmen|teğmenin üstü|DD|*teg-|
asteğmen|n|tr|ast teğmen|teğmenin altı|DD|*teg-|
astsubay|n|tr|ast subay|subayın altı|DD|*sü|
erbaş|n|tr|er baş|erlerin başı|DD|*er|
erat|n|tr|er|erler topluluğu|DD|*er|
erlik|n|tr|erlik|er olma, yiğitlik|DLT|*er|
komutan|n|fr|commandant|buyuran|CUM|mandare|la:commendare>fr:commandant>tr:komutan
kumandan|n|fr|commandant|buyuran|OSM19|mandare|la:commendare>fr:commandant>tr:kumandan
komuta|n|fr|commande|buyruk|CUM|mandare|
kumanda|n|fr|commande|buyruk; uzaktan yönetim|OSM19|mandare|
komut|n|fr|commande|buyruk|DD|mandare|
komando|n|en|commando|komuta altındaki vurucu birlik|MOD||
mandat|n|fr|mandat|yetki belgesi|CUM|mandare|
kolordu|n|tr|kol ordu|ordunun bir kolu|DD|*kol|
tugay|n|tr|tuğay|tuğ sahibi birlik|DD|*tuğ|
alay|n|el|allágion|tören topluluğu; askerî birlik|EAT||
manga|n|it|manga|sürü; küçük asker takımı|OSM19||la:manica>it:manga>tr:manga
birlik|n|tr|birlik|bir olma; askerî bölüm|OSM||
liva|n|ar|liwāʾ|sancak; tugay|OSM||
mirliva|n|fa|mīr-i liwā|sancak beyi; tuğgeneral|OSM|mīr|ar:liwāʾ>fa:mīr-i liwā>tr:mirliva
miralay|n|fa|mīr-i alay|alay beyi|OSM19|mīr|
kolağası|n|tr|kol ağası|kolun ağası; binbaşı altı rütbe|OSM19|*kol|
mülazım|n|ar|mulāzim|yanında duran; teğmen|OSM19|L-Z-M|
zabit|n|ar|ḍābiṭ|düzen tutan; subay|OSM|Z-B-T|
nefer|n|ar|nafar|kişi; er|OSM|N-F-R|
bölükbaşı|n|tr|bölük başı|bölük komutanı|OSM|*baş|
odabaşı|n|tr|oda başı|yeniçeri odasının başı|OSM|*baş|
başbuğ|n|tr|baş buğ|ordunun başı|DLT|*baş|
başkomutan|n|tr|baş komutan|komutanların başı|CUM|*baş|
muvazzaf|adj|ar|muwaẓẓaf|görevlendirilmiş|OSM19|W-Z-F|
tevzif|n|ar|tawẓīf|görevlendirme|OSM19|W-Z-F|
yedek|n|tr|yedek|yedilen, yanında götürülen|DLT|*yed-|
yedmek|v|tr|yed-|yanında götürmek|DLT|*yed-|
ihtiyat|n|ar|iḥtiyāṭ|sakınma; yedek|OSM|H-W-T|
ihata|n|ar|iḥāṭa|çevreleme; kavrama|OSM|H-W-T|
muhit|n|ar|muḥīṭ|çevreleyen; çevre|OSM|H-W-T|
kıdem|n|ar|qidam|öncelik, eskilik|OSM|K-D-M|
kıdemli|adj|ar|qidam|önce gelen|OSM19|K-D-M|
kadim|adj|ar|qadīm|eski|EAT|K-D-M|
takdim|n|ar|taqdīm|öne alma; sunma|OSM|K-D-M|
kademe|n|ar|qadama|basamak|OSM|K-D-M|
mukaddem|adj|ar|muqaddam|öne alınmış|OSM|K-D-M|
rütbeli|adj|ar|rutba|rütbesi olan|OSM19|R-T-B|
mürettep|adj|ar|murattab|düzenlenmiş|OSM|R-T-B|
terfi|n|ar|tarfīʿ|yükseltme|OSM19|R-F-A|
irtifa|n|ar|irtifāʿ|yükselme; yükseklik|OSM|R-F-A|
merfu|adj|ar|marfūʿ|yükseltilmiş|OSM|R-F-A|
tenzil|n|ar|tanzīl|indirme|OSM|N-Z-L|
azil|n|ar|ʿazl|görevden alma|OSM|A-Z-L|
azletmek|v|ar|ʿazl|görevden almak|OSM|A-Z-L|
mazul|adj|ar|maʿzūl|görevden alınmış|OSM|A-Z-L|
uzlet|n|ar|ʿuzla|köşeye çekilme|OSM|A-Z-L|
inziva|n|ar|inziwāʾ|köşeye çekilme|OSM|Z-W-Y|
münzevi|adj|ar|munzawī|köşeye çekilmiş|OSM|Z-W-Y|
nasp|n|ar|naṣb|dikme; atama|OSM|N-S-B|
mansıp|n|ar|manṣib|dikilen yer; makam|OSM|N-S-B|
tayin|n|ar|taʿyīn|belirleme; atama|OSM|A-Y-N|
tayın|n|ar|taʿyīn|belirlenmiş pay; asker azığı|OSM19|A-Y-N|
atama|n|tr|ata-|göreve getirme|DD|*ata-|
atamak|v|tr|ata-|ad vermek; göreve getirmek|DLT|*ata-|
paye|n|fa|pāya|basamak; rütbe|OSM|pā|
unvan|n|ar|ʿunwān|başlık; san|OSM||
madalya|n|it|medaglia|yarım dinar; nişan|OSM19||la:medalia>it:medaglia>tr:madalya
apolet|n|fr|épaulette|omuzluk|OSM19||la:spatula>fr:épaulette>tr:apolet
terhis|n|ar|tarḫīṣ|izin verme; salıverme|OSM19|R-H-S|
celp|n|ar|calb|çekme; çağırma|OSM19|C-L-B|
celbetmek|v|ar|calb|çekmek; çağırmak|OSM19|C-L-B|
sevk|n|ar|sawq|sürme, gönderme|OSM|S-W-K|
sevkiyat|n|ar|sawqiyyāt|gönderimler|OSM19|S-W-K|
askerî|adj|ar|ʿaskarī|askere ilişkin|OSM|A-S-K-R|
askerlik|n|ar|ʿaskar|asker olma durumu|OSM|A-S-K-R|
askeriye|n|ar|ʿaskariyya|ordu kurumu|OSM19|A-S-K-R|
muasker|n|ar|muʿaskar|ordugâh|OSM|A-S-K-R|
leşker|n|fa|laşkar|ordu|EAT||
sipehsalar|n|fa|sipah-sālār|ordu başı|EAT||
süvari|n|fa|suwārī|ata binen|EAT||
cündi|n|ar|cundī|asker; atlı|EAT||
koşun|n|tr|koşun|dizilmiş saf; ordu|DK|*koş-|
çerik|n|tr|çerig|ordu|ORH||
# --- Modern ordu, donanma ve hava gücü ------------------------------------------------
garnizon|n|fr|garnison|donatılmış birlik|OSM19||
tatbikat|n|ar|taṭbīqāt|uygulamalar|CUM|T-B-K|
tatbik|n|ar|taṭbīq|uygulama|OSM|T-B-K|
mutabık|adj|ar|muṭābiq|uyuşan|OSM|T-B-K|
manevra|n|it|manovra|el işi; harekât|OSM19|manus|la:manu operari>it:manovra>tr:manevra
manüel|adj|fr|manuel|elle yapılan|MOD|manus|
manifesto|n|it|manifesto|elle vurulan; açık bildirge|CUM|manus|la:manifestus>it:manifesto>tr:manifesto
teçhizat|n|ar|tachīzāt|donatımlar|OSM19|C-H-Z|
teçhiz|n|ar|tachīz|donatma|OSM19|C-H-Z|
mücehhez|adj|ar|mucahhaz|donatılmış|OSM19|C-H-Z|
cihaz|n|ar|cihāz|donanım; aygıt|OSM|C-H-Z|
mühimmat|n|ar|muhimmāt|gerekli şeyler; cephane|OSM19||
levazım|n|ar|lawāzim|gerekli şeyler|OSM|L-Z-M|
iltizam|n|ar|iltizām|üstlenme; vergi kiralama|OSM|L-Z-M|
mültezim|n|ar|multazim|vergi toplamayı üstlenen|OSM|L-Z-M|
ilzam|n|ar|ilzām|susturma, bağlama|OSM|L-Z-M|
iaşe|n|ar|iʿāşa|yaşatma; besleme|OSM19|A-Y-Ş|
maişet|n|ar|maʿīşa|geçim|OSM|A-Y-Ş|
ibate|n|ar|ibāta|barındırma|OSM19|B-Y-T|
erzak|n|ar|arzāq|rızıklar|OSM|R-Z-K|
rezzak|n|ar|razzāq|rızık veren|EAT|R-Z-K|
merzuk|adj|ar|marzūq|rızıklanmış|OSM|R-Z-K|
karavana|n|it|caravana|kervan; asker yemek kabı|OSM19||fa:kārwān>it:caravana>tr:karavana
konvoy|n|fr|convoi|birlikte yola çıkan|CUM||la:conviare>fr:convoi>tr:konvoy
kafile|n|ar|qāfila|dönen topluluk; kervan|EAT||
strateji|n|fr|stratégie|ordu komutanlığı sanatı|OSM19|stratos|grc:stratēgía>fr:stratégie>tr:strateji
stratejik|adj|fr|stratégique|stratejiye ilişkin|CUM|stratos|
stratejist|n|fr|stratégiste|strateji uzmanı|MOD|stratos|
taktik|n|fr|tactique|dizme sanatı|OSM19|taxis|grc:taktikḗ>fr:tactique>tr:taktik
taktiksel|adj|fr|tactique|taktiğe ilişkin|MOD|taxis|
sentaks|n|fr|syntaxe|birlikte dizme|MOD|taxis|grc:sýntaxis>fr:syntaxe>tr:sentaks
operasyon|n|fr|opération|iş, işlem|CUM|opus|la:operatio>fr:opération>tr:operasyon
operatör|n|fr|opérateur|işleten|MOD|opus|
cephane|n|fa|cebe-ḫāne|silah evi|OSM|-hāne|mn:cebe>fa:cebe-ḫāne>tr:cephane
cephanelik|n|fa|cebe-ḫāne|cephane deposu|CUM|-hāne|
tophane|n|fa|ṭop-ḫāne|top dökümevi|OSM|-hāne|
baruthane|n|fa|bārūt-ḫāne|barut yapımevi|OSM|-hāne|
cebehane|n|fa|cebe-ḫāne|zırh ve silah deposu|OSM|-hāne|
mehterhane|n|fa|mehter-ḫāne|mehter takımının yeri|OSM|-hāne|
menzilhane|n|fa|manzil-ḫāne|konak evi|OSM|-hāne|
nezarethane|n|fa|naẓārat-ḫāne|gözaltı yeri|CUM|-hāne|
talimgâh|n|fa|taʿlīm-gāh|eğitim yeri|OSM19|-gāh|
nişangâh|n|fa|nişān-gāh|hedef yeri; namlu üstü arpacık|OSM|-gāh|
cengâh|n|fa|cang-gāh|savaş yeri|OSM|-gāh|
talimname|n|fa|taʿlīm-nāme|eğitim kitabı|OSM19|-nāme|
muallem|adj|ar|muʿallam|eğitilmiş|OSM|İ-L-M|
teyakkuz|n|ar|tayaqquẓ|uyanıklık|OSM19||
alarm|n|fr|alarme|silah başına|CUM|arma|it:all'arme>fr:alarme>tr:alarm
armada|n|es|armada|donatılmış donanma|OSM19|arma|
ikaz|n|ar|īqāẓ|uyandırma|OSM19||
seferî|adj|ar|safarī|sefere ilişkin|OSM|S-F-R|
seferli|n|ar|safar|sefere giden; Enderun odası|OSM|S-F-R|
tekmil|n|ar|takmīl|tamamlama; rapor|OSM|K-M-L|
yoklama|n|tr|yokla-|yoklayıp sayma|OSM||
hiza|n|ar|ḥiḏāʾ|karşı; aynı doğrultu|OSM||
hazırol|intj|ar|ḥāḍir|hazır dur|CUM|H-D-R|
hazret|n|ar|ḥaḍra|huzur; yüce kişi|EAT|H-D-R|
ihzar|n|ar|iḥḍār|hazır etme; getirtme|OSM|H-D-R|
muhzır|n|ar|muḥḍir|mahkemeye getiren|OSM|H-D-R|
hazirun|n|ar|ḥāḍirūn|hazır bulunanlar|OSM|H-D-R|
marş|n|fr|marche|yürüyüş|OSM19||
resmigeçit|n|ar|rasm-i geçit|tören geçişi|OSM19|R-S-M|
zırhlı|adj|fa|zirih|zırh giymiş; zırhla kaplı|OSM|zirih|
zırh|n|fa|zirih|demir giysi|EAT|zirih|
mekanize|adj|fr|mécanisé|makineli|MOD|mekhane|
motorize|adj|fr|motorisé|motorlu|MOD|movere|
paraşüt|n|fr|parachute|düşmeye karşı|CUM||it:para>fr:parachute>tr:paraşüt
paraşütçü|n|fr|parachute|paraşütle atlayan|CUM||
helikopter|n|fr|hélicoptère|burgu kanat|MOD||grc:hélix+pterón>fr:hélicoptère>tr:helikopter
jet|n|en|jet|fışkırtma|MOD||la:iactare>fr:jet>en:jet>tr:jet
bombardıman|n|fr|bombardement|bomba yağdırma|OSM19|bombos|
bomba|n|it|bomba|gümbürtü|OSM19|bombos|grc:bómbos>la:bombus>it:bomba>tr:bomba
bombacı|n|it|bomba|bomba atan|CUM|bombos|
füze|n|fr|fusée|iğ; roket|MOD||la:fusus>fr:fusée>tr:füze
uçaksavar|n|tr|uçak savar|uçağı savan|DD|*sav-|
tanksavar|n|tr|tank savar|tankı savan|MOD|*sav-|
mayın|n|en|mine|maden ocağı; patlayıcı|CUM||fro:mine>en:mine>tr:mayın
torpido|n|it|torpedine|uyuşturan balık; deniz bombası|OSM19|torpere|la:torpedo>it:torpedine>tr:torpido
torpil|n|fr|torpille|uyuşturan balık; deniz bombası|OSM19|torpere|la:torpedo>fr:torpille>tr:torpil
denizaltı|n|tr|deniz altı|denizin altında giden gemi|CUM||
muhrip|n|ar|muḫrib|yıkıcı; destroyer|CUM||
destroyer|n|en|destroyer|yıkıcı|MOD||la:destruere>en:destroyer>tr:destroyer
kruvazör|n|fr|croiseur|dolaşan gemi|CUM|crux|la:crux>fr:croiseur>tr:kruvazör
kruvaze|adj|fr|croisé|çaprazlanmış|MOD|crux|
hücumbot|n|tr|hücum bot|saldırı teknesi|MOD|H-C-M|
nükleer|adj|fr|nucléaire|çekirdeğe ilişkin|MOD||la:nucleus>fr:nucléaire>tr:nükleer
kimyasal|adj|ar|kīmiyā|kimyaya ilişkin|DD||grc:khēmeía>ar:kīmiyā>tr:kimyasal
radarcı|n|en|radar|radar görevlisi|MOD||
sinyal|n|fr|signal|işaret|CUM|signum|la:signum>fr:signal>tr:sinyal
sinyalizasyon|n|fr|signalisation|işaretleme|MOD|signum|
dürbün|n|fa|dūr-bīn|uzağı gören|OSM||
telsiz|n|tr|tel-siz|telsiz haberleşme aygıtı|CUM||
# --- Osmanlı ordusu: ocaklar, sınıflar, görevliler ------------------------------------
akıncı|n|tr|akınçı|akın yapan|EAT|*ak-|
azap|n|ar|ʿazab|bekâr; bekâr yaya askeri|EAT||
cebeci|n|mn|cebe|zırh ve silah bakımcısı|OSM|*cebe|
cebecibaşı|n|tr|cebeci başı|cebeci ocağının başı|OSM|*baş|
topçu|n|tr|top-çu|top atan asker|OSM|*top-|
topçubaşı|n|tr|topçu başı|topçu ocağının başı|OSM|*baş|
topuz|n|tr|topuz|yuvarlak başlı sopa|EAT|*top-|
humbaracı|n|fa|ḫunbara|humbara atan|OSM|ḫunb|
humbara|n|fa|ḫunbara|küpçük; el bombası|OSM|ḫunb|
kumbara|n|fa|ḫunbara|küpçük; para kutusu|OSM|ḫunb|
humbaracıbaşı|n|tr|humbaracı başı|humbaracı ocağının başı|OSM|*baş|
lağımcı|n|ar|laġm|tünel kazan asker|OSM|L-Ğ-M|
lağım|n|ar|laġm|yer altı yolu; pis su yolu|OSM|L-Ğ-M|
serdengeçti|n|fa|ser-den geçti|başından geçen; fedai|OSM|ser|
bostancı|n|fa|bostān|saray bahçıvanı; saray muhafızı|OSM||
bostancıbaşı|n|tr|bostancı başı|bostancı ocağının başı|OSM|*baş|
solak|n|tr|sol-ak|solak; padişah yaya muhafızı|EAT|*sol|
solakbaşı|n|tr|solak başı|solakların başı|OSM|*baş|
solcu|n|tr|sol-cu|sol görüşlü|MOD|*sol|
peyk|n|fa|payk|haberci; padişah yanında koşan|EAT||
peykbaşı|n|tr|peyk başı|peyklerin başı|OSM|*baş|
kapıkulu|n|tr|kapı kulu|saray kapısının kulu|OSM|*kul|
kapıağası|n|tr|kapı ağası|saray kapısının ağası|OSM|*ağa|
kapıcıbaşı|n|tr|kapıcı başı|saray kapıcılarının başı|OSM|*baş|
kulluk|n|tr|kul-luk|kul olma; karakol|DLT|*kul|
kulbaşı|n|tr|kul başı|kulların başı|OSM|*baş|
tımar|n|fa|tīmār|bakım; gelir karşılığı toprak|EAT|tīmār|
tımarlı|adj|fa|tīmār|tımar sahibi|OSM|tīmār|
zeamet|n|ar|zaʿāma|önderlik; büyük tımar|OSM|Z-A-M|
zaim|n|ar|zaʿīm|önder; zeamet sahibi|OSM|Z-A-M|
has|n|ar|ḫāṣṣ|özel; padişaha özgü gelir|EAT|H-S-S|
hassa|n|ar|ḫāṣṣa|özel birlik|OSM|H-S-S|
hasoda|n|ar|ḫāṣṣ oda|padişahın özel odası|OSM|H-S-S|
hasodabaşı|n|tr|hasoda başı|hasodanın başı|OSM|*baş|
hususi|adj|ar|ḫuṣūṣī|özel|OSM|H-S-S|
haseki|n|ar|ḫāṣṣagī|özel hizmetli; padişah gözdesi|OSM|H-S-S|
devşirme|n|tr|devşir-|toplanan; Hristiyan çocuk toplama|OSM|*der-|
devşirmek|v|tr|dévşür-|toplamak|EAT|*der-|
dermek|v|tr|tér-|toplamak|DLT|*der-|
acemi|n|ar|aʿcamī|Arap olmayan; toy|EAT|A-C-M|
Acem|prop|ar|ʿacam|Arap olmayan; İranlı|EAT|A-C-M|
yamak|n|tr|yamak|yardımcı|OSM|*yama-|
çorbacı|n|fa|şūrbā|çorba dağıtan; yeniçeri bölük komutanı|OSM||
kazancı|n|tr|kazan-çı|kazan bakıcısı|OSM|*kaz-|
aşçıbaşı|n|tr|aşçı başı|aşçıların başı|OSM|*baş|
sekban|n|fa|sag-bān|köpek bakıcısı; yeniçeri bölüğü|OSM|-bān|
seymen|n|fa|sag-bān|sekban; köy yiğitleri|OSM|-bān|
sarıca|n|tr|sarıca|sarımtırak; eyalet askeri|OSM||
kalyoncu|n|it|galeone|kalyon tayfası|OSM||
kaptanıderya|n|fa|kapudān-ı daryā|deniz kaptanı|OSM||
kapudan|n|it|capitano|baş olan|OSM|caput|
mehter|n|fa|mihtar|daha büyük; çalgıcı|OSM||
nevbet|n|ar|nawba|sıra; mehter vuruşu|EAT|N-W-B|
nöbet|n|ar|nawba|sıra; bekleme görevi|EAT|N-W-B|
nöbetçi|n|ar|nawba|nöbet tutan|OSM|N-W-B|
münavebe|n|ar|munāwaba|sırayla değişme|OSM19|N-W-B|
naip|n|ar|nāʾib|yerine geçen|EAT|N-W-B|
niyabet|n|ar|niyāba|vekillik|OSM|N-W-B|
kös|n|fa|kūs|büyük davul|EAT||
nakkare|n|ar|naqqāra|küçük çifte davul|EAT||
nefir|n|ar|nafīr|boru; toplanma çağrısı|EAT|N-F-R|
borazan|n|fa|būrī-zan|boru çalan|OSM||
boru|n|tr|borġuy|üflemeli çalgı|DLT||
alem|n|ar|ʿalam|bayrak; işaret|EAT|İ-L-M|
alemdar|n|fa|ʿalam-dār|bayrak taşıyan|OSM|dār-|
tuğcu|n|tr|tuğ-çu|tuğ taşıyan|OSM|*tuğ|
kılavuzluk|n|tr|kulaġuz|yol gösterme|OSM||
casus|n|ar|cāsūs|gizlice araştıran|EAT|C-S-S|
casusluk|n|ar|cāsūs|casus işi|OSM19|C-S-S|
tecessüs|n|ar|tacassus|gizlice araştırma; merak|OSM|C-S-S|
ulufe|n|ar|ʿulūfa|yem; asker maaşı|OSM||
ulufeci|n|ar|ʿulūfa|ulufe alan sipahi|OSM||
mevacip|n|ar|mawācib|gerekli ödemeler; maaş|OSM|W-C-B|
vacip|adj|ar|wācib|gerekli|EAT|W-C-B|
icap|n|ar|īcāb|gerekme|OSM|W-C-B|
mucip|adj|ar|mūcib|gerektiren|OSM|W-C-B|
cülus|n|ar|culūs|tahta oturma|OSM|C-L-S|
dirlik|n|tr|diri-lik|geçim; tımar geliri|EAT|*tirig|
diri|adj|tr|tirig|canlı|ORH|*tirig|
dirilmek|v|tr|tiril-|canlanmak|DLT|*tirig|
mukataa|n|ar|muqāṭaʿa|kesime verilen gelir|OSM|K-T-A|
cizye|n|ar|cizya|karşılık; gayrimüslim vergisi|EAT||
haraç|n|ar|ḫarāc|çıkan şey; toprak vergisi|EAT|H-R-C|
öşür|n|ar|ʿuşr|onda bir|EAT|A-Ş-R|
aşar|n|ar|aʿşār|onda birler|OSM|A-Ş-R|
aşiret|n|ar|ʿaşīra|on kişilik topluluk; oymak|EAT|A-Ş-R|
muaşeret|n|ar|muʿāşara|birlikte yaşama|OSM|A-Ş-R|
avarız|n|ar|ʿawāriḍ|arızî vergiler|OSM|A-R-D|
pençik|n|fa|panc-yak|beşte bir|OSM|panc|
pençe|n|fa|panca|beş parmak|EAT|panc|
bac|n|fa|bāc|vergi, geçiş resmi|DLT||
yasavul|n|mn|casaġul|düzen görevlisi|CC|*yasa-|
yasakçı|n|tr|yasaḳ-çı|yasağı koruyan; muhafız|OSM|*yasa-|
yasaklamak|v|tr|yasaḳ-la-|yasak koymak|DD|*yasa-|
derbent|n|fa|dar-band|geçit; geçidi tutan kale|OSM|-bend|
derbentçi|n|fa|dar-band|geçit bekçisi|OSM|-bend|
bent|n|fa|band|bağ; su seti|EAT|-bend|
bende|n|fa|banda|bağlı; kul|EAT|-bend|
kalebent|n|fa|qalʿa-band|kaleye bağlı; kale sürgünü|OSM|-bend|
kemerbent|n|fa|kamar-band|bel bağı|OSM|-bend|
martolos|n|el|armatolós|silahlı; Hristiyan sınır askeri|OSM||
voynuk|n|sl|vojnik|asker; Hristiyan yardımcı asker|OSM||
yörük|n|tr|yorı-|yürüyen; göçer|EAT|*yürü-|
müsellem|n|ar|musallam|vergiden bağışık asker|OSM|S-L-M|
gureba|n|ar|ġurabāʾ|yabancılar; sipahi bölüğü|OSM|Ğ-R-B|
gurbet|n|ar|ġurba|yabancı diyar|EAT|Ğ-R-B|
noyan|n|mn|noyan|Moğol komutanı|CC||
atabey|n|tr|ata beg|şehzade eğitmeni|EAT|*bek|
ilhan|n|tr|il ḫan|ülke hanı|OSM|*el-|
tegin|n|tr|tégin|prens|ORH||
yabgu|n|tr|yabġu|kağan vekili|ORH||
tarkan|n|tr|tarkan|yüksek unvan|ORH||
tudun|n|tr|tudun|vali|ORH||
buyruk|n|tr|buyruḳ|emir; yüksek görevli|ORH|*buyur-|
buyurmak|v|tr|buyur-|emretmek|ORH|*buyur-|
buyruldu|n|tr|buyur-|vezir emri|OSM|*buyur-|
bahadır|n|fa|bahādur|yiğit|EAT|*batur|fa:bahādur>tr:bahadır
batur|n|mn|baġatur|yiğit|UYG|*batur|
alpagut|n|tr|alpaġut|tek başına saldıran yiğit|DLT|*alp|
alperen|n|tr|alp eren|yiğit derviş|OSM|*alp|
alplık|n|tr|alp-lık|yiğitlik|DLT|*alp|
toy|n|tr|toy|şölen; kurultay|ORH||
uruk|n|tr|uruġ|soy; tohum|DLT||
taife|n|ar|ṭāʾifa|topluluk|EAT||
kabile|n|ar|qabīla|birbirine dönük topluluk|EAT|K-B-L|
mukabele|n|ar|muqābala|karşılık verme|OSM|K-B-L|
ikbal|n|ar|iqbāl|öne dönme; talih|OSM|K-B-L|
istikbal|n|ar|istiqbāl|karşılama; gelecek|OSM|K-B-L|
kızılbaş|n|tr|kızıl baş|kızıl sarıklı|OSM|*baş|
# --- Silahlar ve donanım ----------------------------------------------------------------
mızrak|n|ar|mizrāq|fırlatılan kargı|EAT||
kargı|n|tr|kargu|uzun saplı sivri silah|EAT||
süngü|n|tr|süŋü|mızrak; tüfek ucu bıçağı|DLT||
cida|n|mn|cida|mızrak|OSM||
pusat|n|tr|pusat|silah; donanım|EAT||
sadak|n|mn|saġadaq|ok kılıfı|EAT||
tirkeş|n|fa|tīr-keş|ok çeken; ok kılıfı|EAT|-keş|
kemankeş|n|fa|kamān-keş|yay çeken|OSM|-keş|
serkeş|adj|fa|ser-keş|baş çeken; dik başlı|OSM|-keş|
cefakeş|adj|fa|cafā-keş|eziyet çeken|OSM|-keş|
tirendaz|n|fa|tīr-andāz|ok atan|OSM||
temren|n|tr|temürgen|demirden yapılmış; ok ucu|DLT||
gez|n|tr|kez|ok çentiği|DLT||
okçu|n|tr|oḳçı|ok yapan; ok atan|DLT|*ok|
okluk|n|tr|oḳluḳ|ok kabı|DLT|*ok|
yaycı|n|tr|yaçı|yay yapan|DLT||
yaylım|n|tr|yay-lım|toplu atış|OSM||
kement|n|fa|kamand|ilmikli ip|EAT||
urgan|n|tr|uruḳ|kalın ip|DLT||
bukağı|n|tr|buḳaġu|ayak zinciri|DLT||
kelepçe|n|fa|kalab-ça|küçük çengel; el zinciri|OSM||
kın|n|tr|kın|kılıç kılıfı|DLT||
kabza|n|ar|qabḍa|tutulan yer; sap|OSM|K-B-D|
kabız|n|ar|qabḍ|tutma; peklik|OSM|K-B-D|
makbuz|n|ar|maqbūḍ|alınmış; alındı belgesi|OSM|K-B-D|
kabzımal|n|ar|qabḍ-ı māl|mal tutan; toptancı|OSM19|K-B-D|
balçak|n|tr|balçak|kılıç siperliği|EAT||
yalman|n|tr|yalman|kılıç ağzı|DLT||
hançer|n|ar|ḫancar|kısa eğri bıçak|EAT||
pala|n|it?|pala|geniş ağızlı kısa kılıç|OSM||
yatağan|n|tr|Yatağan|Yatağan ilçesinde yapılan kılıç|OSM||
kama|n|tr|kama|kıskı; iki yüzlü bıçak|DLT||
gürz|n|fa|gurz|demir topuz|EAT||
bozdoğan|n|tr|boz toğan|boz doğan; doğan başlı topuz|OSM||
şeşper|n|fa|şaş-par|altı kanatlı topuz|OSM||
teber|n|fa|tabar|balta|EAT||
nacak|n|fa|nāçaḫ|küçük balta|EAT||
miğfer|n|ar|miġfar|baş zırhı|EAT||
tolga|n|tr|tuġulġa|miğfer|DLT||
cevşen|n|fa|cawşan|zırh gömlek|OSM||
kolçak|n|tr|kolçak|kol zırhı|EAT||
dizçek|n|tr|dizçek|diz zırhı|OSM||
tüfekçi|n|fa|tufang|tüfek yapan; tüfekli muhafız|OSM||
filinta|n|de|Flinte|çakmaklı tüfek|OSM19||
karabina|n|it|carabina|hafif tüfek|OSM19||
piştov|n|hu|pisztoly|tabanca|OSM||cs:píšťala>hu:pisztoly>tr:piştov
revolver|n|en|revolver|döner silah|OSM19||la:volvere>en:revolver>tr:revolver
mitralyöz|n|fr|mitrailleuse|saçma atan|OSM19||
otomatik|adj|fr|automatique|kendiliğinden işleyen|CUM|autos|grc:autómatos>fr:automatique>tr:otomatik
otomat|n|fr|automate|kendiliğinden işleyen aygıt|MOD|autos|
namlu|n|fa|nāmlū|tüfek borusu|OSM||
tetik|n|tr|tetik|çevik; ateşleme dili|DLT||
şarjör|n|fr|chargeur|yükleyen|CUM|carrus|la:carrus>fr:chargeur>tr:şarjör
şarj|n|fr|charge|yük|MOD|carrus|
fişek|n|fa|fişang|patlayıcı tüp|OSM||
fişeklik|n|fa|fişang|fişek kemeri|OSM19||
gülle|n|fa|gulūla|yuvarlak; top mermisi|OSM||
şarapnel|n|fr|shrapnel|parçalı top mermisi|OSM19||en:shrapnel>fr:shrapnel>tr:şarapnel
obüs|n|fr|obus|kısa namlulu top|OSM19||cs:houfnice>de:Haubitze>fr:obus>tr:obüs
mancınık|n|ar|mancanīq|taş atan düzenek|EAT||grc:manganikón>ar:mancanīq>tr:mancınık
fitil|n|ar|fatīl|bükülmüş ip|EAT||
fünye|n|fr?|fusée|ateşleyici|OSM19||
kapsül|n|fr|capsule|küçük kutu|CUM||la:capsula>fr:capsule>tr:kapsül
kükürt|n|fa|gūgird|sarı yanıcı madde|DLT||
güherçile|n|fa|gawhar-çīla|barut tuzu|OSM||
cop|n|fa|çūb|değnek|OSM||
kırbaç|n|tr|kırbaç|kamçı|EAT||
kamçı|n|tr|kamçı|vurma aracı|DLT||
# --- Kale, istihkâm ve ordugâh -----------------------------------------------------------
tabya|n|ar|ṭābiya|düzenlenmiş siper|OSM|A-B-E|
tabiye|n|ar|taʿbiya|düzenleme; savaş düzeni|OSM|A-B-E|
palanka|n|hu|palánk|ahşap kale|OSM||it:palanca>hu:palánk>tr:palanka
şarampol|n|hu|sorompó|engel; kazıklı siper|OSM||
tahkimat|n|ar|taḥkīmāt|sağlamlaştırmalar|OSM19|H-K-M|
istihkâm|n|ar|istiḥkām|sağlamlaştırma; siper yapısı|OSM|H-K-M|
mevzi|n|ar|mawḍiʿ|konulan yer|OSM|W-Ḍ-A|
mevzu|n|ar|mawḍūʿ|konulmuş; konu|OSM|W-Ḍ-A|
vaziyet|n|ar|waḍʿiyya|konum, durum|OSM19|W-Ḍ-A|
vazetmek|v|ar|waḍʿ|koymak|OSM|W-Ḍ-A|
cenah|n|ar|canāḥ|kanat|OSM|C-N-H|
cünha|n|ar|cunḥa|hafif suç|OSM19|C-N-H|
merkez|n|ar|markaz|dikilen yer; orta|OSM||
artçı|n|tr|art-çı|arkada kalan|DD|*art|
ardıl|n|tr|ard-ıl|ardından gelen|DD|*art|
pişdar|n|fa|pīş-dār|önde tutan; öncü birlik|OSM|dār-|
dümdar|n|fa|dum-dār|kuyrukta tutan; artçı|OSM|dār-|
dizdar|n|fa|diz-dār|kale tutan|EAT|dār-|
mustahfız|n|ar|mustaḥfiẓ|koruyan; kale askeri|OSM|H-F-Z|
koğuş|n|tr|koğuş|büyük yatakhane|OSM||
mazgal|n|tr|mazgal|duvar deliği|OSM||
siperlik|n|fa|sipar|siper eden şey|OSM||
kalebentlik|n|fa|qalʿa-band|kale sürgünü cezası|OSM|-bend|
# --- Sefer, savaş ve zafer ----------------------------------------------------------------
gaza|n|ar|ġazw|akın; din uğruna savaş|EAT|G-Z-W|
gazve|n|ar|ġazwa|akın|EAT|G-Z-W|
gazavat|n|ar|ġazawāt|gazalar|OSM|G-Z-W|
mücahede|n|ar|mucāhada|çabalama; savaşma|EAT|C-H-D|
fethetmek|v|ar|fatḥ|açmak; ele geçirmek|EAT|F-T-H|
fütuhat|n|ar|futūḥāt|fetihler|OSM|F-T-H|
miftah|n|ar|miftāḥ|açan; anahtar|EAT|F-T-H|
iftitah|n|ar|iftitāḥ|açılış|OSM|F-T-H|
fettah|adj|ar|fattāḥ|açan|EAT|F-T-H|
muzaffer|adj|ar|muẓaffar|zafer kazanmış|EAT|Z-F-R|
zafername|n|fa|ẓafar-nāme|zafer yazısı|OSM|Z-F-R|
zaferyab|adj|fa|ẓafar-yāb|zafer bulan|OSM|Z-F-R|
hezimet|n|ar|hazīma|bozgun|OSM|H-Z-M|
inhizam|n|ar|inhizām|bozguna uğrama|OSM|H-Z-M|
münhezim|adj|ar|munhazim|bozguna uğramış|OSM|H-Z-M|
galip|adj|ar|ġālib|üstün gelen|EAT|Ğ-L-B|
galibiyet|n|ar|ġālibiyya|üstün gelme|OSM|Ğ-L-B|
mağlup|adj|ar|maġlūb|yenilmiş|EAT|Ğ-L-B|
mağlubiyet|n|ar|maġlūbiyya|yenilme|OSM|Ğ-L-B|
galebe|n|ar|ġalaba|üstünlük|EAT|Ğ-L-B|
tagallüp|n|ar|taġallub|zorla üstün gelme|OSM|Ğ-L-B|
nusret|n|ar|nuṣra|yardım; zafer|EAT|N-S-R|
mansur|adj|ar|manṣūr|yardım görmüş; zafer kazanmış|EAT|N-S-R|
ensar|n|ar|anṣār|yardımcılar|EAT|N-S-R|
esir|n|ar|asīr|bağlanmış; tutsak|EAT|E-S-R|
esaret|n|ar|asāra|tutsaklık|OSM|E-S-R|
üsera|n|ar|usarāʾ|tutsaklar|OSM|E-S-R|
ganimet|n|ar|ġanīma|savaşta ele geçen mal|EAT|Ğ-N-M|
iğtinam|n|ar|iġtinām|ganimet alma; fırsat bilme|OSM|Ğ-N-M|
yağma|n|tr|yaġma|çapul|EAT|*yağma|
yağmacı|n|tr|yaġma-çı|yağma yapan|OSM|*yağma|
yağmalamak|v|tr|yaġma-la-|yağma etmek|OSM|*yağma|
talan|n|fa|tālān|çapul|OSM||
talancı|n|fa|tālān|talan eden|OSM19||
çapul|n|tr|çapul|yağma akını|EAT|*çap-|
çapulcu|n|tr|çapul-cu|yağmacı|OSM|*çap-|
çapkın|adj|tr|çap-kın|koşturan; hovarda|OSM|*çap-|
çapar|n|tr|çap-ar|koşan; ulak|EAT|*çap-|
çapmak|v|tr|çap-|hızla koşmak; vurmak|DLT|*çap-|
pusu|n|tr|busuġ|gizlenip bekleme|DLT|*bus-|
pusmak|v|tr|bus-|sinmek, gizlenmek|DLT|*bus-|
pusucu|n|tr|busuġ-çı|pusu kuran|OSM|*bus-|
kuşatmak|v|tr|kuşat-|çevresini sarmak|EAT|*kuşa-|
kuşatma|n|tr|kuşat-|çevreleme|OSM|*kuşa-|
kuşanmak|v|tr|kuşan-|beline bağlamak|DLT|*kuşa-|
istila|n|ar|istīlāʾ|ele geçirme|OSM|W-L-Y|
işgal|n|ar|işġāl|meşgul etme; ele geçirme|OSM19|Ş-Ğ-L|
işgalci|n|ar|işġāl|işgal eden|CUM|Ş-Ğ-L|
iştigal|n|ar|iştiġāl|uğraşma|OSM|Ş-Ğ-L|
meşgul|adj|ar|maşġūl|uğraşan|EAT|Ş-Ğ-L|
meşguliyet|n|ar|maşġūliyya|uğraş|OSM19|Ş-Ğ-L|
ilhak|n|ar|ilḥāq|katma|OSM19|L-H-K|
mülhak|adj|ar|mulḥaq|katılmış|OSM|L-H-K|
lahika|n|ar|lāḥiqa|ek|OSM|L-H-K|
tecavüz|n|ar|tacāwuz|haddi aşma|OSM|C-W-Z|
mütecaviz|adj|ar|mutacāwiz|haddi aşan|OSM|C-W-Z|
taarruz|n|ar|taʿarruḍ|karşı çıkma; saldırı|OSM|A-R-D|
hücum|n|ar|hucūm|saldırı|EAT|H-C-M|
muhacim|n|ar|muhācim|saldıran|OSM|H-C-M|
tehacüm|n|ar|tahācum|üşüşme|OSM|H-C-M|
saldırmak|v|tr|saldur-|üzerine salmak|EAT|*sal-|
saldırı|n|tr|saldur-|hücum|DD|*sal-|
saldırgan|adj|tr|saldur-|saldıran|DD|*sal-|
salmak|v|tr|sal-|bırakmak; göndermek|DLT|*sal-|
salgın|n|tr|sal-gın|yayılan hastalık; olağanüstü vergi|EAT|*sal-|
müdafaa|n|ar|mudāfaʿa|savunma|OSM|D-F-A|
müdafi|n|ar|mudāfiʿ|savunan|OSM|D-F-A|
defetmek|v|ar|dafʿ|uzaklaştırmak|EAT|D-F-A|
indifa|n|ar|indifāʿ|püskürme|OSM19|D-F-A|
mukabil|adj|ar|muqābil|karşılık olan|OSM|K-B-L|
direniş|n|tr|diren-|karşı koyma|DD||
ricat|n|ar|ricʿat|geri dönme|OSM|R-C-A|
rücu|n|ar|rucūʿ|geri dönme|OSM|R-C-A|
irtica|n|ar|irticāʿ|geriye dönme|CUM|R-C-A|
mürteci|n|ar|murtaciʿ|geriye dönen|CUM|R-C-A|
firar|n|ar|firār|kaçma|OSM|F-R-R|
firari|n|ar|firārī|kaçak|OSM|F-R-R|
teslimiyet|n|ar|taslīmiyya|kendini bırakma|OSM19|S-L-M|
müsalemet|n|ar|musālama|barış içinde olma|OSM|S-L-M|
yenilgi|n|tr|yéŋ-il-|yenilme|DD|*yen-|
yengi|n|tr|yéŋ-|yenme|DD|*yen-|
yenik|adj|tr|yéŋ-ik|yenilmiş|OSM|*yen-|
bozgun|n|tr|boz-gun|dağılma|OSM|*boz-|
bozmak|v|tr|buz-|dağıtmak|ORH|*boz-|
bozuk|adj|tr|buz-uk|dağılmış|DLT|*boz-|
bozulmak|v|tr|buz-ul-|dağılmak|DLT|*boz-|
bozguncu|n|tr|boz-gun-cu|düzen bozan|CUM|*boz-|
vurgun|n|tr|ur-gun|vurulmuş; haksız kazanç|OSM|*ur-|
uruş|n|tr|uruş|vuruşma|DLT|*ur-|
vurdurmak|v|tr|ur-dur-|vurmasını sağlamak|EAT|*ur-|
dövüş|n|tr|tög-üş|dövüşme|OSM|*döv-|
çarpışmak|v|tr|çarp-ış-|birbirine çarpmak|OSM|*çarp-|
çarpışma|n|tr|çarp-ış-|çatışma|DD|*çarp-|
çarpan|n|tr|çarp-an|çarpan sayı|DD|*çarp-|
püskürmek|v|tr|püskür-|dışarı fışkırmak|EAT|*püskür-|
püskürtmek|v|tr|püskür-t-|geri atmak|EAT|*püskür-|
ilerlemek|v|tr|ileri-le-|öne gitmek|OSM|*ileri|
ilerleme|n|tr|ileri-le-|öne gitme|DD|*ileri|
gerilemek|v|tr|geri-le-|geriye gitmek|OSM|*geri|
gerileme|n|tr|geri-le-|geriye gitme|DD|*geri|
kurtarmak|v|tr|kurtar-|kurtulmasını sağlamak|DLT|*kurtul-|
kurtuluş|n|tr|kurtul-|kurtulma|OSM|*kurtul-|
kurtarıcı|n|tr|kurtar-|kurtaran|DD|*kurtul-|
kurtulmak|v|tr|kurtul-|serbest kalmak|DLT|*kurtul-|
kırım|n|tr|kır-ım|toplu öldürme|DD|*kır-|
soykırım|n|tr|soy kırım|bir soyu yok etme|TDK|*kır-|
mukatele|n|ar|muqātala|karşılıklı öldürme|OSM|K-T-L|
muharip|n|ar|muḥārib|savaşan|OSM|H-R-B|
harbi|adj|ar|ḥarbī|savaşa ilişkin; dürüst|OSM|H-R-B|
cengâver|n|fa|cangāwar|savaşçı|OSM|cang|
cenkçi|n|fa|cang|savaşçı|OSM|cang|
cenkleşmek|v|fa|cang|savaşmak|EAT|cang|
savaşçı|n|tr|savaş-çı|savaşan|DD|*sav-|
savaşmak|v|tr|savaş-|birbirini savmak|EAT|*sav-|
savmak|v|tr|sav-|uzaklaştırmak|DLT|*sav-|
savuşmak|v|tr|sav-uş-|sıyrılıp kaçmak|EAT|*sav-|
savuşturmak|v|tr|sav-uş-tur-|atlatmak|OSM|*sav-|
# --- Osmanlı devlet kurumları ve unvanlar -------------------------------------------
veziriazam|n|ar|wazīr-i aʿẓam|en büyük vezir|OSM|W-Z-R|
kazasker|n|ar|qāḍī ʿaskar|ordu kadısı|OSM|K-D-Y|
nişancı|n|fa|nişān|tuğra çeken; hedefi vuran|OSM|nişān|
nişanlamak|v|fa|nişān|hedef almak|OSM|nişān|
reisülküttap|n|ar|raʾīs al-kuttāb|kâtiplerin başı|OSM|K-T-B|
şeyhülislam|n|ar|şayḫ al-islām|İslam'ın şeyhi|OSM|Ş-Y-H|
meşihat|n|ar|maşīḫa|şeyhlik; şeyhülislamlık|OSM19|Ş-Y-H|
şeyhlik|n|ar|şayḫ|şeyh olma|OSM|Ş-Y-H|
beylerbeyi|n|tr|begler begi|beylerin beyi|EAT|*bek|
sancakbeyi|n|tr|sancak begi|sancak yöneticisi|OSM|*bek|
uçbeyi|n|tr|uç begi|sınır beyi|EAT|*bek|
beylik|n|tr|beg-lik|bey yönetimi|DLT|*bek|
begüm|n|tr|beg-üm|beyim; hanım|OSM|*bek|
derebeyi|n|tr|dere begi|vadi beyi; zorba|OSM19|*bek|
subaşı|n|tr|sü başı|ordu başı; kolluk amiri|DLT|*sü|
sü|n|tr|sü|asker, ordu|ORH|*sü|
kethüda|n|fa|kad-ḫudā|ev sahibi; vekil|EAT||
çavuşbaşı|n|tr|çavuş başı|çavuşların başı|OSM|*baş|
silahtar|n|fa|silāḥ-dār|silah tutan|OSM|dār-|
çuhadar|n|fa|çūḫa-dār|çuha tutan; giyim görevlisi|OSM|dār-|
rikabdar|n|fa|rikāb-dār|üzengi tutan|OSM|dār-|
hazinedar|n|fa|ḫazīna-dār|hazine tutan|OSM|dār-|
mühürdar|n|fa|muhr-dār|mühür tutan|OSM|dār-|
enderun|n|fa|andarūn|iç; saray iç bölümü|OSM||
birun|n|fa|bīrūn|dış; saray dış bölümü|OSM||
haremağası|n|tr|harem ağası|harem görevlisi|OSM|*ağa|
kızlarağası|n|tr|kızlar ağası|harem ağalarının başı|OSM|*ağa|
yeniçeriağası|n|tr|yeniçeri ağası|yeniçeri ocağı komutanı|OSM|*ağa|
akağa|n|tr|ak ağa|beyaz hadım ağa|OSM|*ağa|
karaağa|n|tr|kara ağa|siyah hadım ağa|OSM|*ağa|
ağalık|n|tr|aġa-lık|ağa olma|OSM|*ağa|
ağabey|n|tr|aġa beg|büyük erkek kardeş|OSM|*ağa|
darüssaade|n|ar|dār al-saʿāda|mutluluk evi; harem|OSM|D-W-R|
hadım|n|ar|ḫādim|hizmet eden; kısırlaştırılmış|EAT|H-D-M|
lala|n|fa|lālā|şehzade eğitmeni|OSM||
hünkâr|n|fa|ḫunkār|hükümdar|EAT||
hümayun|adj|fa|humāyūn|kutlu; padişaha ait|OSM||
hilafet|n|ar|ḫilāfa|ardından gelme; halifelik|EAT|H-L-F|
halife|n|ar|ḫalīfa|ardıl|EAT|H-L-F|
halef|n|ar|ḫalaf|ardından gelen|OSM|H-L-F|
ihtilaf|n|ar|iḫtilāf|ayrılık|OSM|H-L-F|
saltanat|n|ar|salṭana|egemenlik|EAT|S-L-T|
musallat|adj|ar|musallaṭ|üstüne salınmış|OSM|S-L-T|
tasallut|n|ar|tasalluṭ|sataşma|OSM|S-L-T|
biat|n|ar|bayʿa|bağlılık sözü|EAT|B-Y-A|
bayi|n|ar|bāyiʿ|satıcı|OSM19|B-Y-A|
mübayaa|n|ar|mubāyaʿa|satın alma|OSM|B-Y-A|
sikke|n|ar|sikka|damga; madeni para|EAT|S-K-K|
meskûkat|n|ar|maskūkāt|basılmış paralar|OSM19|S-K-K|
babıali|n|ar|bāb-ı ʿālī|yüce kapı; hükümet|OSM|B-W-B|
babüssaade|n|ar|bāb al-saʿāda|mutluluk kapısı|OSM|B-W-B|
bab|n|ar|bāb|kapı; bölüm|EAT|B-W-B|
divanıhümayun|n|fa|dīwān-ı humāyūn|padişah divanı|OSM||
kubbealtı|n|tr|kubbe altı|divan toplantı yeri|OSM|Q-B-B|
sadaret|n|ar|ṣadāra|baş olma; sadrazamlık|OSM|S-D-R|
sadır|n|ar|ṣadr|göğüs; baş yer|OSM|S-D-R|
musadere|n|ar|muṣādara|el koyma|OSM|S-D-R|
mabeyin|n|ar|mā bayn|iki şey arası; saray dairesi|OSM|B-Y-N|
mabeyinci|n|ar|mā bayn|padişah ile dış dünya arasındaki görevli|OSM19|B-Y-N|
tebeyyün|n|ar|tabayyun|belli olma|OSM|B-Y-N|
kalemiye|n|ar|qalamiyya|yazı sınıfı|OSM|K-L-M|
seyfiye|n|ar|sayfiyya|kılıç sınıfı|OSM|S-Y-F|
seyf|n|ar|sayf|kılıç|EAT|S-Y-F|
ilmiye|n|ar|ʿilmiyya|bilgin sınıfı|OSM|İ-L-M|
ulema|n|ar|ʿulamāʾ|bilginler|EAT|İ-L-M|
mülkiye|n|ar|mulkiyya|sivil yönetim sınıfı|OSM19|M-L-K|
memlük|n|ar|mamlūk|sahip olunan; köle asker|EAT|M-L-K|
tıbbiye|n|ar|ṭıbbiyya|tıp okulu|OSM19|T-B-B|
nizamiye|n|ar|niẓāmiyya|düzenli ordu|OSM19|N-Z-M|
nizami|adj|ar|niẓāmī|düzenli|OSM|N-Z-M|
tanzimat|n|ar|tanẓīmāt|düzenlemeler|OSM19|N-Z-M|
nizamıcedit|n|ar|niẓām-ı cadīd|yeni düzen|OSM|N-Z-M|
cedit|adj|ar|cadīd|yeni|OSM|C-D-D|
tecdit|n|ar|tacdīd|yenileme|OSM|C-D-D|
müceddit|n|ar|mucaddid|yenileyen|OSM|C-D-D|
ıslahat|n|ar|iṣlāḥāt|düzeltmeler|OSM19|S-L-H|
meşrutiyet|n|ar|maşrūṭiyya|şarta bağlı yönetim|OSM19|Ş-R-T|
meşrut|adj|ar|maşrūṭ|şarta bağlanmış|OSM|Ş-R-T|
şartname|n|fa|şarṭ-nāme|şartlar yazısı|OSM19|Ş-R-T|
mutlakiyet|n|ar|muṭlaqiyya|sınırsız yönetim|OSM19|T-L-K|
mutlak|adj|ar|muṭlaq|bağsız; kesin|EAT|T-L-K|
ıtlak|n|ar|iṭlāq|salıverme; genelleme|OSM|T-L-K|
istibdat|n|ar|istibdād|tek başına yönetme|OSM19|B-D-D|
müstebit|adj|ar|mustabidd|tek başına yöneten|OSM19|B-D-D|
hüccet|n|ar|ḥucca|kanıt; belge|EAT||
sicil|n|ar|sicill|kayıt defteri|OSM||
vakıf|n|ar|waqf|durdurma; bağış kurumu|EAT|W-K-F|
evkaf|n|ar|awqāf|vakıflar|OSM|W-K-F|
mevkuf|adj|ar|mawqūf|durdurulmuş; tutuklu|OSM|W-K-F|
tevkif|n|ar|tawqīf|durdurma; tutuklama|OSM|W-K-F|
mütevelli|n|ar|mutawallī|işi üstlenen|OSM|W-L-Y|
mevleviyet|n|ar|mawlawiyya|büyük kadılık|OSM|W-L-Y|
valilik|n|ar|wālī|vali makamı|OSM19|W-L-Y|
velayet|n|ar|wilāya|koruyuculuk|OSM|W-L-Y|
mutasarrıf|n|ar|mutaṣarrif|tasarruf eden; sancak yöneticisi|OSM19|S-R-F|
mutasarrıflık|n|ar|mutaṣarrif|sancak yönetimi|OSM19|S-R-F|
kaymakamlık|n|ar|qāʾim-maqām|kaymakam makamı|OSM19|K-W-M|
emaret|n|ar|imāra|emirlik|EAT|E-M-R|
emirlik|n|ar|amīr|emir yönetimi|OSM|E-M-R|
emirname|n|fa|amr-nāme|buyruk yazısı|OSM|E-M-R|
ümera|n|ar|umarāʾ|emirler; komutanlar|OSM|E-M-R|
hanlık|n|tr|ḫan-lık|han yönetimi|OSM||
hakanlık|n|tr|ḫaḳan-lık|hakan yönetimi|OSM||
imparator|n|it|imperatore|buyuran|OSM|imperare|la:imperator>it:imperatore>tr:imparator
imparatorluk|n|it|imperatore|imparator yönetimi|OSM19|imperare|
emperyalizm|n|fr|impérialisme|imparatorluk siyaseti|CUM|imperare|
emperyalist|adj|fr|impérialiste|imparatorluk yanlısı|CUM|imperare|
prens|n|fr|prince|ilk gelen|OSM19|princeps|la:princeps>fr:prince>tr:prens
prenses|n|fr|princesse|prens eşi veya kızı|OSM19|princeps|
prensip|n|fr|principe|başlangıç; ilke|CUM|princeps|la:principium>fr:principe>tr:prensip
kont|n|fr|comte|yoldaş; bölge yöneticisi|OSM19|comes|la:comes>fr:comte>tr:kont
kontes|n|fr|comtesse|kont eşi|OSM19|comes|
kontluk|n|fr|comte|kont yönetimi|CUM|comes|
baron|n|fr|baron|adam; soylu|OSM19||
şövalye|n|fr|chevalier|atlı|OSM19|caballus|la:caballarius>fr:chevalier>tr:şövalye
kavalye|n|fr|cavalier|atlı; dans eşi|CUM|caballus|
senyör|n|fr|seigneur|yaşlı; efendi|OSM19|senior|la:senior>fr:seigneur>tr:senyör
senatör|n|fr|sénateur|yaşlılar kurulu üyesi|OSM19|senior|
feodal|adj|fr|féodal|tımara ilişkin|CUM|feudum|la:feudum>fr:féodal>tr:feodal
feodalizm|n|fr|féodalisme|tımar düzeni|CUM|feudum|
feodalite|n|fr|féodalité|tımar düzeni|CUM|feudum|
beyzade|n|fa|beg-zāde|bey oğlu|OSM|-zāde|
paşazade|n|fa|pāşā-zāde|paşa oğlu|OSM|-zāde|
ağazade|n|fa|āġā-zāde|ağa oğlu|OSM|-zāde|
çelebi|n|tr|çalab|Tanrı'ya ait; kibar kişi|EAT||
tebaa|n|ar|tabaʿa|uyanlar|OSM|T-B-A|
azat|n|fa|āzād|özgür|EAT|āzād|
azatlı|adj|fa|āzād|özgür bırakılmış|OSM|āzād|
azade|adj|fa|āzāda|özgür; kurtulmuş|OSM|āzād|
gulam|n|ar|ġulām|oğlan; köle|EAT||
eşraf|n|ar|aşrāf|soylular|OSM|Ş-R-F|
şerif|n|ar|şarīf|soylu|EAT|Ş-R-F|
teşrifat|n|ar|taşrīfāt|onurlandırmalar; tören kuralları|OSM|Ş-R-F|
teşrif|n|ar|taşrīf|onurlandırma|OSM|Ş-R-F|
müşerref|adj|ar|muşarraf|onurlandırılmış|OSM|Ş-R-F|
mirahur|n|fa|mīr-āḫūr|ahır beyi|OSM|mīr|
imrahor|n|fa|mīr-āḫūr|ahır beyi|OSM|mīr|
mir|n|fa|mīr|bey, komutan|EAT|mīr|
çaşnigir|n|fa|çāşnī-gīr|tadımcı|OSM|-gīr|
dilgir|adj|fa|dil-gīr|gönlü tutulmuş; kırgın|OSM|-gīr|
baltacı|n|tr|balta-cı|baltalı saray hizmetlisi|OSM||
zülüflü|adj|fa|zulf|zülüflü; saray baltacısı|OSM||
zülüf|n|fa|zulf|şakak saçı|EAT||
kilerci|n|el|kellári|kiler görevlisi|OSM||
derban|n|fa|dar-bān|kapıcı|OSM|-bān|
pasban|n|fa|pās-bān|bekçi|OSM|-bān|
nigehban|n|fa|nigāh-bān|gözcü|OSM|-bān|
sayeban|n|fa|sāya-bān|gölgelik|OSM|-bān|
asayiş|n|fa|āsāyiş|dinginlik; güvenlik|OSM|āsūdan|
asude|adj|fa|āsūda|dinlenmiş; dingin|EAT|āsūdan|
arzuhalci|n|fa|ʿarḍ-i ḥāl|dilekçe yazan|OSM19|A-R-D|
istida|n|ar|istidʿāʾ|dilekçe|OSM|D-A-W|
maruzat|n|ar|maʿrūḍāt|sunulanlar|OSM|A-R-D|
mazbata|n|ar|maḍbaṭa|tutanak|OSM|Z-B-T|
zabıt|n|ar|ḍabṭ|tutanak|OSM19|Z-B-T|
zapt|n|ar|ḍabṭ|tutma; ele geçirme|EAT|Z-B-T|
zaptetmek|v|ar|ḍabṭ|ele geçirmek|EAT|Z-B-T|
zaptiye|n|ar|ḍabṭiyya|kolluk kuvveti|OSM19|Z-B-T|
inzibat|n|ar|inḍibāṭ|düzen; askerî polis|OSM19|Z-B-T|
telhis|n|ar|talḫīṣ|özetleme; sadrazam özeti|OSM||
halas|n|ar|ḫalāṣ|kurtulma|EAT|H-L-S|
muhlis|adj|ar|muḫliṣ|içten|EAT|H-L-S|
ahitname|n|fa|ʿahd-nāme|antlaşma yazısı|OSM|A-H-D|
mühimme|n|ar|muhimma|önemli iş; divan defteri|OSM||
temlikname|n|fa|tamlīk-nāme|mülk verme yazısı|OSM|-nāme|
paşalık|n|tr|paşa-lık|paşa yönetimi|OSM||
mülteci|n|ar|multacī|sığınan|OSM19|L-C-A|
iltica|n|ar|ilticāʾ|sığınma|OSM|L-C-A|
melce|n|ar|malcaʾ|sığınak|OSM|L-C-A|
muhacir|n|ar|muhācir|göç eden|OSM|H-C-R|
muhaceret|n|ar|muhācara|göç|OSM19|H-C-R|
hicret|n|ar|hicra|göç|EAT|H-C-R|
hicri|adj|ar|hicrī|hicrete ilişkin|OSM|H-C-R|
tehcir|n|ar|tahcīr|göç ettirme|OSM19|H-C-R|
göç|n|tr|köç|yer değiştirme|DLT|*köç-|
göçmek|v|tr|köç-|yer değiştirmek|ORH|*köç-|
göçebe|n|tr|köçebe|göçerek yaşayan|OSM|*köç-|
göçmen|n|tr|köç-men|göç eden|DD|*köç-|
göçer|adj|tr|köç-er|göç eden|EAT|*köç-|
# --- Kolluk, güvenlik ve istihbarat -------------------------------------------------------
karakol|n|mn|qaraġul|gözcü; nöbet yeri|CC||
komiser|n|fr|commissaire|görevlendirilmiş|OSM19|mittere|la:commissarius>fr:commissaire>tr:komiser
başkomiser|n|tr|baş komiser|komiserlerin başı|CUM|*baş|
devriye|n|ar|dawriyya|dolaşan|OSM19|D-W-R|
kolcu|n|tr|kol-cu|kol gezen; gümrük bekçisi|OSM|*kol|
kolluk|n|tr|kol-luk|kol görevi; güvenlik gücü|OSM|*kol|
kolaçan|n|tr|kol açan|dolaşıp bakma|OSM|*kol|
korucu|n|tr|korı-çı|koruyan|OSM|*koru-|
gözetlemek|v|tr|közet-le-|gizlice izlemek|OSM|*kör-|
gözetleme|n|tr|közet-le-|gizlice izleme|DD|*kör-|
ases|n|ar|ʿasas|gece bekçisi|OSM|A-S-S|
asesbaşı|n|tr|ases başı|gece bekçilerinin başı|OSM|A-S-S|
ajan|n|fr|agent|iş yapan|CUM|agere|la:agens>fr:agent>tr:ajan
ajans|n|fr|agence|iş yeri|CUM|agere|
ajanda|n|fr|agenda|yapılacak işler|CUM||
aktif|adj|fr|actif|etkin|CUM|agere|
aktör|n|fr|acteur|oynayan|CUM|agere|
muhbir|n|ar|muḫbir|haber veren|OSM|H-B-R|
keşfetmek|v|ar|kaşf|örtüyü açmak; bulmak|OSM|K-Ş-F|
sorgulamak|v|tr|sor-gu-la-|sorguya çekmek|DD|*sor-|
tutuklamak|v|tr|tut-uk-la-|gözaltına almak|DD|*tut-|
tutuklama|n|tr|tut-uk-la-|gözaltına alma|DD|*tut-|
müfettiş|n|ar|mufattiş|arayan; denetleyen|OSM19|F-T-Ş|
teftiş|n|ar|taftīş|arama; denetleme|OSM|F-T-Ş|
operasyonel|adj|fr|opérationnel|işleme ilişkin|MOD|opus|
siren|n|fr|sirène|deniz kızı; uyarı düdüğü|CUM||grc:seirḗn>fr:sirène>tr:siren
projektör|n|fr|projecteur|ileri atan|CUM|iacere|la:proicere>fr:projecteur>tr:projektör
enjeksiyon|n|fr|injection|içe atma|CUM|iacere|
tuzak|n|tr|tuzak|yem; kapan|DLT||
# --- İsyan, darbe ve siyasal şiddet -------------------------------------------------------
isyan|n|ar|ʿiṣyān|karşı gelme|EAT|A-S-Y|
asi|adj|ar|ʿāṣī|karşı gelen|EAT|A-S-Y|
isyankâr|adj|fa|ʿiṣyān-kār|isyan eden|OSM|A-S-Y|
masiyet|n|ar|maʿṣiya|günah|EAT|A-S-Y|
ayaklanma|n|tr|ayak-lan-|başkaldırı|DD||
ayaklanmak|v|tr|ayak-lan-|başkaldırmak|OSM||
ihtilal|n|ar|iḫtilāl|bozulma; devrim|OSM||
devrim|n|ar|dawr|dönüş; köklü değişim|TDK|D-W-R|
darbe|n|ar|ḍarba|vuruş|OSM|D-R-B|
darp|n|ar|ḍarb|vurma|EAT|D-R-B|
ızdırap|n|ar|iḍṭirāb|çalkalanma; acı|OSM|D-R-B|
muzdarip|adj|ar|muḍṭarib|acı çeken|OSM|D-R-B|
mızrap|n|ar|miḍrāb|vurma aracı|OSM|D-R-B|
darbımesel|n|ar|ḍarb-ı maṯal|örnek vuruşu; atasözü|OSM|D-R-B|
darbeci|n|ar|ḍarba|darbe yapan|MOD|D-R-B|
cunta|n|es|junta|birleşmiş kurul|MOD|iungere|la:iuncta>es:junta>tr:cunta
konjonktür|n|fr|conjoncture|birleşme durumu|MOD|iungere|
eşkıya|n|ar|aşqiyāʾ|bedbahtlar; haydutlar|OSM|Ş-Q-W|
şaki|n|ar|şaqī|bedbaht; haydut|OSM|Ş-Q-W|
şekavet|n|ar|şaqāwa|bedbahtlık; haydutluk|OSM|Ş-Q-W|
harami|n|ar|ḥarāmī|haram işleyen; haydut|EAT|H-R-M|
zorbalık|n|fa|zūr-bā|zorba davranışı|OSM19||
çeteci|n|tr|çete-ci|çete üyesi|CUM||
komita|n|sl|komita|komite; gizli örgüt|OSM19||fr:comité>bg:комита>tr:komita
komitacı|n|sl|komita|komita üyesi|OSM19||
gerilla|n|fr|guérilla|küçük savaş|MOD||
partizan|n|fr|partisan|taraftar; çeteci|MOD||it:partigiano>fr:partisan>tr:partizan
milis|n|fr|milice|askerlik; halk ordusu|CUM|miles|la:militia>fr:milice>tr:milis
militan|n|fr|militant|savaşan|MOD|miles|
militarizm|n|fr|militarisme|ordu yanlılığı|CUM|miles|
militarist|adj|fr|militariste|ordu yanlısı|CUM|miles|
gönüllü|adj|tr|köŋül-lü|isteyerek yapan|EAT||
fedai|n|ar|fidāʾī|kendini feda eden|OSM||
intihar|n|ar|intiḥār|kendini boğazlama|OSM19||
terör|n|fr|terreur|dehşet|CUM|terrere|la:terror>fr:terreur>tr:terör
terörist|n|fr|terroriste|dehşet saçan|CUM|terrere|
terörizm|n|fr|terrorisme|dehşet siyaseti|CUM|terrere|
anarşist|n|fr|anarchiste|yönetimsizlik yanlısı|OSM19|arkhein|
anarşizm|n|fr|anarchisme|yönetimsizlik öğretisi|CUM|arkhein|
sabotaj|n|fr|sabotage|takunyayla bozma|CUM|sabot|
sabotör|n|fr|saboteur|bozan|CUM|sabot|
suikast|n|ar|sūʾ-i qaṣd|kötü niyet|OSM|K-S-D|
suikastçı|n|ar|sūʾ-i qaṣd|suikast yapan|CUM|K-S-D|
hıyanet|n|ar|ḫiyāna|güveni bozma|EAT|H-W-N|
hainlik|n|ar|ḫāʾin|hain davranışı|OSM|H-W-N|
itaat|n|ar|iṭāʿa|boyun eğme|EAT|T-W-A|
taat|n|ar|ṭāʿa|boyun eğme; ibadet|EAT|T-W-A|
muti|adj|ar|muṭīʿ|boyun eğen|OSM|T-W-A|
disiplin|n|fr|discipline|öğrenim; düzen|CUM||la:disciplina>fr:discipline>tr:disiplin
kahır|n|ar|qahr|ezme; üzüntü|EAT|K-H-R|
kahretmek|v|ar|qahr|ezmek; lanet etmek|EAT|K-H-R|
kahhar|adj|ar|qahhār|ezen|EAT|K-H-R|
makhur|adj|ar|maqhūr|ezilmiş|OSM|K-H-R|
kahramanlık|n|fa|qahramān|yiğitlik|OSM||
yiğitlik|n|tr|yigit-lik|yiğit olma|DLT||
korkaklık|n|tr|korḳ-ak-lık|korkak olma|OSM|*kork-|
cesaretli|adj|ar|casāra|yürekli|OSM19||
ürkütmek|v|tr|ürk-üt-|korkutmak|DLT|*ürk-|
şenlik|n|tr|şen-lik|bayram; kalabalık|OSM||
# --- Ordu yaşamı ve tören ------------------------------------------------------------------
kışlamak|v|tr|kışla-|kışı geçirmek|DLT|*kış|
izinli|adj|tr|izin-li|izin almış|OSM||
nöbetleşe|adv|ar|nawba|sırayla|OSM19|N-W-B|
yoklamak|v|tr|yokla-|var mı diye bakmak|DLT||
andiçmek|v|tr|and iç-|yemin etmek|DLT|*ant|
tekmilli|adj|ar|takmīl|tamam|OSM19|K-M-L|
sıralı|adj|tr|sıra-lı|sırası olan|OSM||
üniformalı|adj|fr|uniforme|üniforma giymiş|CUM|unus|
kaputlu|adj|fr|capote|kaput giymiş|CUM|caput|
kasketli|adj|fr|casquette|kasket giymiş|CUM|caput|
püskül|n|tr|püskül|saçaklı süs|OSM||
kordonlu|adj|fr|cordon|kordonu olan|CUM|korda|
çizmeli|adj|tr|çizme-li|çizme giymiş|OSM||
kuşaklı|adj|tr|kuşak-lı|kuşak bağlamış|OSM|*kuşa-|
börklü|adj|tr|börk-lü|börk giymiş|DLT||
serpuş|n|fa|ser-pūş|baş örtüsü; başlık|OSM|ser|
serçeşme|n|fa|ser-çaşma|pınar başı; başbuğ|OSM|ser|
serleşker|n|fa|ser-laşkar|ordu başı|OSM|ser|
serbölük|n|fa|ser-bölük|bölük başı|OSM|ser|
ordubozan|adj|tr|ordu boz-an|düzen bozan|OSM|*ordu|
orda|n|tr|ordu|hanlık merkezi; Altın Orda|OSM|*ordu|
tümbay|n|tr|tüm-bay|tümgeneral (eski ad)|DD|*tüm|
korbay|n|tr|kor-bay|korgeneral (eski ad)|DD|*kor|
teğmenlik|n|tr|teğmen-lik|teğmen rütbesi|DD|*teg-|
kolbaşı|n|tr|kol başı|kolun başı|OSM|*baş|
elebaşı|n|tr|ele başı|topluluğun başı|OSM|*baş|
sübaşılık|n|tr|sü başı-lık|subaşı görevi|OSM|*sü|
erkeklik|n|tr|erkek-lik|erkek olma|DLT|*er|
eren|n|tr|eren|erişmiş kişi; ermiş|EAT|*er|
yedeklemek|v|tr|yed-ek-le-|yedeğe almak|DD|*yed-|

cebelü|n|mn|cebe|zırhlı asker|OSM|*cebe|
dövüşken|adj|tr|tög-üş-ken|dövüşmeyi seven|OSM|*döv-|
yamalı|adj|tr|yama-lı|yaması olan|EAT|*yama-|
ürküntü|n|tr|ürk-üntü|ürkme duygusu|OSM|*ürk-|
ruhsatiye|n|ar|ruḫṣatiyya|izin harcı|OSM19|R-H-S|
"""

FAMILIES = r"""
*baş|tr|baş, önder|Orhun Yazıtları'ndaki baş "baş, tepe; önder"; onbaşı, yüzbaşı, binbaşı, başçavuş, başbuğ, bölükbaşı, odabaşı, kapıcıbaşı, bostancıbaşı, topçubaşı gibi Osmanlı görev adları ve kızılbaş aynı kökten gelir.
*bek|tr|bey, hükümdar|Orhun Yazıtları'ndaki beg "bey"; beylik, beylerbeyi, sancakbeyi, uçbeyi, derebeyi, begüm, atabey ile Dil Devrimi'nin bay sözünden yaptığı albay ve yarbay aynı kökten türer.
*tuğ|tr|at kuyruğu sancak|Eski Türkçe tuğ "hükümdarlık alameti olan at kuyruğu"; tuğcu, tugay (tuğ sahibi birlik), tuğgeneral ve tuğamiral aynı kökten gelir.
*tüm|tr|bütün; on bin|Eski Türkçe tüm "bütün" ile akraba tümen "on bin"; tümgeneral, tümamiral ve tümbay (tümen komutanı) aynı kökten türetilmiştir.
*kor|tr|kolordu|Dil Devrimi'nde kolordu sözünün kısaltılmasıyla oluşan kor; korgeneral, koramiral ve korbay aynı kısaltmadan türetilmiştir.
*ordu|tr|ordu, hükümdar karargâhı|Orhun Yazıtları'ndaki ordu "hükümdarın karargâhı"; orda (Altın Orda), ordubozan, orgeneral ve oramiral aynı kökten gelir; Avrupa dillerindeki horde de buradan yayılmıştır.
*teg-|tr|değmek, denk gelmek|Eski Türkçe teg- "değmek, erişmek"; Dil Devrimi'nin teğmen (denk gelen), üsteğmen, asteğmen ve teğmenlik sözleri bu kökten türetilmiştir.
*sü|tr|asker, ordu|Orhun Yazıtları'ndaki sü "ordu"; subaşı (sü başı: ordu komutanı), sübaşılık, astsubay ve Dil Devrimi'nin subay sözü aynı kökten gelir.
*er|tr|erkek, asker|Orhun Yazıtları'ndaki er "erkek, yiğit"; erlik, erat, erbaş, eren ve erkeklik aynı kökten türer.
*kol|tr|kol; askerî birlik|Eski Türkçe kol "kol, yan"; kolordu, kolağası, kolcu, kolluk, kolaçan ve kolbaşı askerlik dilinde aynı kökten türemiştir.
*yed-|tr|yanında götürmek|Eski Türkçe yet- "yedeğinde götürmek"; yedmek, yedek (yanında götürülen at) ve yedeklemek aynı kökten gelir.
*ata-|tr|ad vermek, atamak|Eski Türkçe ata- "ad vermek"; atamak ve atama (göreve getirme) aynı kökten türer.
*cebe|mn|zırh, silah|Moğolca cebe "zırh, silah"; cebeci (silah bakımcısı) ve cebelü (zırhlı asker) aynı kökten gelir; cebehane ve cephane ise Farsça ḫāne ile kurulmuştur.
*sol|tr|sol yan|Eski Türkçe sol "sol taraf"; solak (sol elini kullanan; padişah muhafızı) ve solcu aynı kökten türer.
*kul|tr|köle, hizmetkâr|Orhun Yazıtları'ndaki kul "köle"; kulluk (kul olma; karakol) ve kapıkulu (saray kapısının kulu) aynı kökten gelir.
*ağa|tr|büyük kardeş; reis|Eski Türkçe aka/ağa "büyük erkek kardeş, reis"; ağalık, ağabey, yeniçeriağası, haremağası, kızlarağası, kapıağası, akağa ve karaağa aynı kökten türer.
*der-|tr|toplamak|Eski Türkçe tér- "toplamak"; dermek, devşirmek (dévşür-), devşirme ve derleme aynı kökten gelir.
*yama-|tr|yama vurmak|Eski Türkçe yama- "ekleyerek onarmak"; yamak (yardımcı) ve yamalı aynı kökten türer.
*tirig|tr|canlı|Orhun Yazıtları'ndaki tirig "canlı"; diri, dirilmek ve dirlik (geçim; tımar geliri) aynı kökten gelir.
*yasa-|mn|düzenlemek|Moğolca casa- "düzenlemek"; yasa, yasak ile yasavul (düzen görevlisi), yasakçı ve yasaklamak aynı kökten türer.
*buyur-|tr|emretmek|Orhun Yazıtları'ndaki buyur- "emretmek"; buyruk (emir; yüksek görevli) ve buyruldu (vezir emri) aynı kökten gelir.
*batur|mn|yiğit|Eski Türkçe ve Moğolca baġatur "yiğit"; batur ve Farsça yoluyla gelen bahadır aynı köktendir; Rusça bogatır ve Macarca bátor da buradan yayılmıştır.
*alp|tr|yiğit|Orhun Yazıtları'ndaki alp "yiğit, kahraman"; alplık, alpagut (tek başına saldıran yiğit) ve alperen aynı kökten türer.
*ok|tr|ok|Orhun Yazıtları'ndaki ok; okçu, okluk ve okçuluk aynı kökten gelir.
*art|tr|arka|Eski Türkçe art "arka, sırt"; artçı (arkada kalan birlik) ve ardıl aynı kökten türetilmiştir.
*yağma|tr|çapul|Eski Türkçe yaġma "çapul"; yağmacı ve yağmalamak aynı kökten gelir; Farsça yaġmā da Türkçeden alınmıştır.
*çap-|tr|hızla koşmak, akın etmek|Eski Türkçe çap- "vurmak; at koşturmak"; çapmak, çapul (akın), çapulcu, çapar (ulak) ve çapkın aynı kökten türer.
*bus-|tr|gizlenip beklemek|Eski Türkçe bus- "pusuda beklemek"; pusmak, pusu (busuġ) ve pusucu aynı kökten gelir.
*kuşa-|tr|çevresini sarmak|Eski Türkçe kurşa- "çevrelemek"; kuşanmak, kuşatmak, kuşatma ve kuşaklı aynı kökten türer.
*sal-|tr|bırakmak, göndermek|Eski Türkçe sal- "bırakmak, üzerine göndermek"; salmak, saldırmak, saldırı, saldırgan ve salgın (salınan hastalık; olağanüstü vergi) aynı kökten gelir.
*yen-|tr|üstün gelmek|Eski Türkçe yéŋ- "yenmek"; yengi, yenik ve yenilgi aynı kökten türetilmiştir.
*boz-|tr|dağıtmak, bozmak|Eski Türkçe buz- "yıkmak, dağıtmak"; bozmak, bozuk, bozulmak, bozgun ve bozguncu aynı kökten gelir.
*ur-|tr|vurmak|Eski Türkçe ur- "vurmak"; vurmak, uruş, vurgun ve vurdurmak aynı kökten türer.
*döv-|tr|dövmek|Eski Türkçe tög- "dövmek"; dövüş ve dövüşken aynı kökten gelir.
*çarp-|tr|çarpmak|Eski Türkçe çarp- "vurmak"; çarpışmak, çarpışma ve çarpan aynı kökten türer.
*püskür-|tr|dışarı fışkırmak|Eski Anadolu Türkçesi püskür- "fışkırmak"; püskürmek ve püskürtmek (geri atmak) aynı kökten gelir.
*ileri|tr|ön taraf|Eski Türkçe ilgerü "ileri"; ilerlemek ve ilerleme aynı kökten türer.
*geri|tr|arka taraf|Eski Türkçe kérü "geri"; gerilemek ve gerileme aynı kökten gelir.
*kurtul-|tr|serbest kalmak|Eski Türkçe kurtul- "kurtulmak"; kurtulmak, kurtarmak, kurtuluş ve kurtarıcı aynı kökten türer.
*sav-|tr|uzaklaştırmak, defetmek|Eski Türkçe sav- "uzaklaştırmak"; savmak, savaşmak, savaşçı, savuşmak, savuşturmak ile Dil Devrimi'nin uçaksavar ve tanksavar sözleri aynı kökten gelir.
*köç-|tr|yer değiştirmek|Orhun Yazıtları'ndaki köç- "göçmek"; göç, göçmek, göçer, göçebe ve göçmen aynı kökten türer.
*ürk-|tr|korkup kaçmak|Eski Türkçe ürk- "ürkmek"; ürkütmek ve ürküntü aynı kökten gelir.
-bend|fa|bağ, bağlayan|Farsça band "bağ, set"; bent, bende (bağlı, kul), derbent (geçit bağlayan), derbentçi, kalebent, kalebentlik ve kemerbent aynı kökten türer.
-bān|fa|bakan, koruyan|Farsça -bān "bakıcı, bekçi" eki; sekban (sag-bān: köpek bakıcısı), seymen, derban, pasban, nigehban ve sayeban aynı ekle kurulmuştur.
-gīr|fa|tutan, alan|Farsça giriftan "tutmak" fiilinin -gīr türevi; çaşnigir (tat tutan) ve dilgir (gönlü tutulmuş) aynı ekle kurulmuştur.
-keş|fa|çeken|Farsça kaşīdan "çekmek" fiilinin -keş türevi; tirkeş (ok çeken), kemankeş (yay çeken), serkeş (baş çeken) ve cefakeş aynı ekle kurulmuştur.
-zāde|fa|oğlu|Farsça zāde "doğmuş, oğul"; beyzade, paşazade ve ağazade aynı ekle kurulmuştur.
A-B-E|ar|düzenlemek, dizmek|Arapça ʿ-b-ʾ kökü; tabya (düzenlenmiş siper) ve tabiye (savaş düzeni) aynı kökten türer.
A-C-M|ar|Arap olmayan|Arapça ʿ-c-m kökü; Acem (İranlı) ve acemi (yabancı; toy) aynı kökten gelir.
A-S-K-R|ar|ordu|Arapça ʿ-s-k-r kökü; asker, askerî, askerlik, askeriye ve muasker (ordugâh) aynı kökten türer.
A-S-S|ar|gece gezmek|Arapça ʿ-s-s kökü; ases (gece bekçisi) ve asesbaşı aynı kökten gelir.
A-S-Y|ar|karşı gelmek|Arapça ʿ-ṣ-y kökü; asi, isyan, isyankâr ve masiyet (günah) aynı kökten türer.
A-Y-Ş|ar|yaşamak|Arapça ʿ-y-ş kökü; iaşe (besleme), maişet (geçim) ve maaş aynı kökten gelir.
A-Z-L|ar|ayırmak, uzaklaştırmak|Arapça ʿ-z-l kökü; azil, azletmek, mazul ve uzlet aynı kökten türer. İnziva ve münzevi, z-w-y "köşeye çekilmek" kökünden gelen ayrı bir ailedir.
A-Ş-R|ar|on; topluluk|Arapça ʿ-ş-r kökü; öşür (onda bir), aşar, aşiret (topluluk), muaşeret ve aşure (onuncu gün) aynı kökten gelir.
B-D-D|ar|tek başına olmak|Arapça b-d-d kökü; istibdat (tek başına yönetme) ve müstebit aynı kökten türer.
B-W-B|ar|kapı|Arapça b-w-b kökü; bab (kapı; bölüm), Babıali (yüce kapı) ve Babüssaade aynı kökten gelir.
B-Y-A|ar|alıp satmak; bağlanmak|Arapça b-y-ʿ kökü; biat (bağlılık sözü), bayi (satıcı) ve mübayaa aynı kökten türer.
B-Y-N|ar|ara; açık olmak|Arapça b-y-n kökü; mabeyin (iki şey arası; saray dairesi), mabeyinci ve tebeyyün aynı kökten gelir.
C-D-D|ar|yeni olmak|Arapça c-d-d kökü; cedit, tecdit (yenileme) ve müceddit aynı kökten türer.
C-H-Z|ar|donatmak|Arapça c-h-z kökü; cihaz, teçhiz, teçhizat ve mücehhez aynı kökten gelir.
C-L-B|ar|çekmek|Arapça c-l-b kökü; celp (askere çağırma) ve celbetmek aynı kökten türer.
C-N-H|ar|kanat; eğilmek|Arapça c-n-ḥ kökü; cenah (kanat) ve cünha (hafif suç) aynı kökten gelir.
C-S-S|ar|yoklamak|Arapça c-s-s kökü; casus, casusluk ve tecessüs aynı kökten türer.
D-F-A|ar|itmek, uzaklaştırmak|Arapça d-f-ʿ kökü; müdafaa, müdafi, defetmek ve indifa aynı kökten gelir.
D-R-B|ar|vurmak|Arapça ḍ-r-b kökü; darp, darbe, darbeci, darbımesel, mızrap, ızdırap ve muzdarip aynı kökten türer.
E-S-R|ar|bağlamak|Arapça ʾ-s-r kökü; esir (bağlanmış), esaret ve üsera aynı kökten gelir.
F-R-R|ar|kaçmak|Arapça f-r-r kökü; firar ve firari aynı kökten türer.
F-T-H|ar|açmak|Arapça f-t-ḥ kökü; fetih, fethetmek, fütuhat, fettah, miftah (anahtar) ve iftitah aynı kökten gelir.
F-T-Ş|ar|aramak|Arapça f-t-ş kökü; teftiş ve müfettiş aynı kökten türer.
G-Z-W|ar|akın etmek|Arapça ġ-z-w kökü; gaza, gazve, gazavat ve gazi aynı kökten gelir.
H-C-M|ar|saldırmak|Arapça h-c-m kökü; hücum, muhacim, tehacüm ve hücumbot aynı kökten türer.
H-C-R|ar|ayrılmak, göç etmek|Arapça h-c-r kökü; hicret, hicri, muhacir, muhaceret ve tehcir aynı kökten gelir.
H-D-R|ar|hazır bulunmak|Arapça ḥ-ḍ-r kökü; hazır, hazırol, hazret (huzur), hazirun, ihzar ve muhzır aynı kökten türer.
H-L-F|ar|ardından gelmek|Arapça ḫ-l-f kökü; halife (ardıl), hilafet, halef, ihtilaf ve muhalif aynı kökten gelir.
H-S-S|ar|özel olmak|Arapça ḫ-ṣ-ṣ kökü; has, hassa, hasoda, haseki ve hususi aynı kökten gelir.
H-W-N|ar|güveni bozmak|Arapça ḫ-w-n kökü; hain, hainlik, hıyanet ve ihanet aynı kökten türer.
H-W-T|ar|çevrelemek|Arapça ḥ-w-ṭ kökü; ihata (çevreleme), muhit (çevre) ve ihtiyat (sakınma; yedek) aynı kökten gelir.
H-Z-M|ar|bozguna uğratmak|Arapça h-z-m kökü; hezimet, inhizam ve münhezim aynı kökten türer.
K-B-D|ar|tutmak, kavramak|Arapça q-b-ḍ kökü; kabza (sap), kabız, makbuz ve kabzımal aynı kökten gelir.
K-B-L|ar|karşılamak; öne dönmek|Arapça q-b-l kökü; kabile, mukabele, mukabil, ikbal ve istikbal aynı kökten türer.
K-D-M|ar|önce gelmek|Arapça q-d-m kökü; kadim, kıdem, kıdemli, kademe, takdim ve mukaddem aynı kökten gelir.
K-H-R|ar|ezmek, üstün gelmek|Arapça q-h-r kökü; kahır, kahretmek, kahhar ve makhur aynı kökten türer.
L-C-A|ar|sığınmak|Arapça l-c-ʾ kökü; iltica, mülteci ve melce (sığınak) aynı kökten gelir.
L-H-K|ar|katılmak|Arapça l-ḥ-q kökü; ilhak, mülhak ve lahika (ek) aynı kökten türer.
L-Z-M|ar|gerekli olmak|Arapça l-z-m kökü; levazım, mülazım (yanında duran), iltizam, mültezim ve ilzam aynı kökten gelir.
L-Ğ-M|ar|tünel kazmak|Arapça l-ġ-m kökü; lağım ve lağımcı aynı kökten türer.
N-F-R|ar|kişi; toplanma çağrısı|Arapça n-f-r kökü; nefer (kişi, er) ve nefir (toplanma borusu) aynı kökten gelir.
N-S-R|ar|yardım etmek|Arapça n-ṣ-r kökü; nusret, mansur ve ensar aynı kökten türer.
N-W-B|ar|sıra ile gelmek|Arapça n-w-b kökü; nöbet, nevbet, nöbetçi, nöbetleşe, münavebe, naip (yerine geçen) ve niyabet aynı kökten gelir.
R-C-A|ar|geri dönmek|Arapça r-c-ʿ kökü; ricat, rücu, irtica ve mürteci aynı kökten türer.
R-F-A|ar|yükseltmek|Arapça r-f-ʿ kökü; terfi, irtifa ve merfu aynı kökten gelir.
R-H-S|ar|izin vermek|Arapça r-ḫ-ṣ kökü; ruhsat, ruhsatiye ve terhis (salıverme) aynı kökten türer.
R-Z-K|ar|rızık vermek|Arapça r-z-q kökü; rızık, erzak, rezzak ve merzuk aynı kökten gelir.
S-D-R|ar|göğüs; baş yer|Arapça ṣ-d-r kökü; sadır, sadaret, sadrazam ve musadere aynı kökten türer.
S-K-K|ar|damga vurmak|Arapça s-k-k kökü; sikke ve meskûkat aynı kökten gelir.
S-L-T|ar|güç, egemenlik|Arapça s-l-ṭ kökü; sultan, saltanat, musallat ve tasallut aynı kökten türer.
S-W-K|ar|sürmek|Arapça s-w-q kökü; sevk ve sevkiyat aynı kökten gelir.
S-Y-F|ar|kılıç|Arapça s-y-f kökü; seyf (kılıç) ve seyfiye (kılıç sınıfı) aynı kökten türer.
T-B-K|ar|üst üste koymak, uygulamak|Arapça ṭ-b-q kökü; tatbik, tatbikat, mutabık ve tabaka aynı kökten gelir.
T-L-K|ar|salıvermek|Arapça ṭ-l-q kökü; mutlak, mutlakiyet, ıtlak ve talak aynı kökten türer.
T-W-A|ar|boyun eğmek|Arapça ṭ-w-ʿ kökü; itaat, taat ve muti aynı kökten gelir.
W-C-B|ar|gerekli olmak|Arapça w-c-b kökü; vacip, icap, mucip ve mevacip (asker maaşı) aynı kökten türer.
W-K-F|ar|durdurmak|Arapça w-q-f kökü; vakıf, evkaf, tevkif ve mevkuf aynı kökten türer.
W-Z-F|ar|görevlendirmek|Arapça w-ẓ-f kökü; vazife, muvazzaf ve tevzif aynı kökten gelir.
Z-A-M|ar|önderlik etmek|Arapça z-ʿ-m kökü; zaim ve zeamet aynı kökten türer.
Z-B-T|ar|tutmak, düzen vermek|Arapça ḍ-b-ṭ kökü; zapt, zaptetmek, zabit, zabıta, zaptiye, zabıt, mazbata ve inzibat aynı kökten gelir.
Z-F-R|ar|üstün gelmek|Arapça ẓ-f-r kökü; zafer, muzaffer, zafername ve zaferyab aynı kökten türer.
Ğ-L-B|ar|üstün gelmek|Arapça ġ-l-b kökü; galip, galibiyet, galebe, tagallüp, mağlup ve mağlubiyet aynı kökten gelir.
Ğ-N-M|ar|ganimet almak|Arapça ġ-n-m kökü; ganimet ve iğtinam aynı kökten türer.
Ğ-R-B|ar|yabancı olmak|Arapça ġ-r-b kökü; garip, gurbet ve gureba (yabancılar; sipahi bölüğü) aynı kökten gelir.
Ş-Q-W|ar|bedbaht olmak|Arapça ş-q-w kökü; şaqī (bedbaht; haydut) > şaki, eşkıya (çoğulu) ve şekavet aynı kökten türer. Şikâyet ise ş-k-w "yakınmak" kökünden gelen ayrı bir ailedir.
Ş-R-F|ar|yüce olmak|Arapça ş-r-f kökü; şeref, şerif, eşraf, teşrif, teşrifat ve müşerref aynı kökten gelir.
Ş-R-T|ar|şart koşmak|Arapça ş-r-ṭ kökü; şart, meşrut, meşrutiyet ve şartname aynı kökten türer.
Ş-Y-H|ar|yaşlı, önder|Arapça ş-y-ḫ kökü; şeyh, şeyhlik, şeyhülislam ve meşihat aynı kökten gelir.
Ş-Ğ-L|ar|uğraştırmak|Arapça ş-ġ-l kökü; meşgul, meşguliyet, iştigal, işgal ve işgalci aynı kökten türer.
ḫunb|fa|küp|Farsça ḫunb "küp"; humbara (küpçük: el bombası), kumbara ve humbaracı aynı kökten gelir.
tīmār|fa|bakım|Farsça tīmār "bakım"; tımar (bakım; gelir karşılığı toprak) ve tımarlı aynı kökten türer.
zirih|fa|zırh|Farsça zirih "demir giysi"; zırh ve zırhlı aynı kökten gelir.
panc|fa|beş|Farsça panc "beş"; pençe (beş parmak) ve pençik (beşte bir vergisi) aynı kökten türer.
nişān|fa|işaret|Farsça nişān "işaret, hedef"; nişan, nişancı, nişanlamak ve nişangâh aynı kökten gelir.
mīr|fa|bey, komutan|Farsça mīr (Arapça amīr'den) "bey"; mir, mirliva, miralay, mirahur ve imrahor aynı kökten türer.
cang|fa|savaş|Farsça cang "savaş"; cenk, cengâver, cenkçi, cenkleşmek ve cengâh aynı kökten gelir.
āzād|fa|özgür|Farsça āzād "özgür"; azat, azatlı ve azade aynı kökten türer.
āsūdan|fa|dinlenmek|Farsça āsūdan "dinlenmek"; asayiş (dinginlik, güvenlik) ve asude aynı kökten gelir.
mandare|la|buyurmak|Latince mandare "ele vermek, buyurmak"; komutan, kumandan, komuta, kumanda, komut, komando ve mandat aynı kökten türer.
manus|la|el|Latince manus "el"; manevra (el işi), manüel ve manifesto aynı kökten gelir.
imperare|la|buyurmak|Latince imperare "buyurmak"; imparator, imparatorluk, emperyalizm ve emperyalist aynı kökten türer.
princeps|la|ilk gelen|Latince princeps "ilk, önder"; prens, prenses ve prensip aynı kökten gelir.
comes|la|yoldaş; vali|Latince comes "yoldaş, maiyet"; kont, kontes ve kontluk aynı kökten türer.
caballus|la|at|Latince caballus "at"; şövalye (atlı) ve kavalye aynı kökten gelir.
senior|la|yaşlı|Latince senior "daha yaşlı"; senyör ve senatör aynı kökten türer.
feudum|la|tımar|Orta Çağ Latincesi feudum "tımar"; feodal, feodalizm ve feodalite aynı kökten gelir.
miles|la|asker|Latince miles "asker"; milis, militan, militarizm ve militarist aynı kökten türer.
terrere|la|korkutmak|Latince terrere "korkutmak"; terör, terörist ve terörizm aynı kökten gelir.
sabot|fr|takunya|Fransızca sabot "takunya"; sabotaj (takunyayla makine bozma) ve sabotör aynı kökten türer.
agere|la|yapmak, sürmek|Latince agere "yapmak"; ajan, ajans, ajanda, aktif ve aktör aynı kökten gelir.
iacere|la|atmak|Latince iacere "atmak"; projektör (ileri atan) ve enjeksiyon (içe atma) aynı kökten türer.
iungere|la|birleştirmek|Latince iungere "bağlamak"; cunta (birleşmiş kurul) ve konjonktür aynı kökten gelir.
opus|la|iş|Latince opus "iş"; operasyon, operatör ve operasyonel aynı kökten türer.
stratos|el|ordu|Eski Yunanca stratós "ordu"; strateji (ordu komutanlığı sanatı), stratejik ve stratejist aynı kökten gelir.
taxis|el|dizme|Eski Yunanca táxis "dizme, düzen"; taktik, taktiksel ve sentaks aynı kökten türer.
autos|el|kendi|Eski Yunanca autós "kendi"; otomatik ve otomat aynı kökten gelir.
bombos|el|gümbürtü|Eski Yunanca bómbos "gümbürtü"; bomba, bombacı ve bombardıman aynı kökten türer.
torpere|la|uyuşmak|Latince torpere "uyuşmak"; torpedo (uyuşturan balık) yoluyla torpil ve torpido aynı kökten gelir.
crux|la|haç|Latince crux "haç"; kruvazör (dolaşan gemi) ve kruvaze aynı kökten türer.
signum|la|işaret|Latince signum "işaret"; sinyal ve sinyalizasyon aynı kökten gelir.
carrus|la|araba|Latince carrus "araba"; şarj (yük) ve şarjör aynı kökten türer.
"""

COGNATES = r"""@paşa from_turkish
  pl pasza ; paşa
  uk паша [paşa] ; paşa
  mk паша [paşa] ; paşa
  hy փաշա [p'aşa] ; paşa
  ka ფაშა [p'aşa] ; paşa
  pt paxá ; paşa
  fa پاشا [pāşā] ; paşa (Osmanlı unvanı)
@ağa from_turkish
  fa آقا [āqā] ; bey, efendi; erkeklere genel saygı sözü ; ff:Farsçada āqā her erkek için "bay, efendi" anlamına genelleşmiştir
  ar أغا [āġā] ; ağa; harem ağası
  pl aga ; ağa
  uk ага [aha] ; ağa
  hy աղա [ağa] ; ağa; zengin
  ka აღა [ağa] ; ağa
  ur آغا [āġā] ; bey, efendi (saygı sözü)
@çavuş from_turkish
  fa چاووش [çāvoş] ; kervan öncüsü; münadi ; ff:Farsçada çāvoş "kervanın önünde ilahi okuyan kişi" anlamına kaymıştır
  pl czausz ; Osmanlı elçisi, ulak ; ff:Lehçede czausz "padişahın yabancı ülkelere gönderdiği ulak" demektir
  uk чауш [çauş] ; çavuş
  az çavuş ; çavuş
  kk шабуыл? [şabuıl] ; hücum ; ff:Kazakça шабуыл Türkçe çavuş ile aynı kökten (çap-) gelir ama "saldırı" demektir
  uz chovush ; çavuş
  hy չավուշ [çavuş] ; çavuş
@onbaşı from_turkish
  ar أومباشي [ombāşī] ; onbaşı (Mısır ordusu ve polisi)
  bg онбашия [onbaşiya] ; onbaşı (Osmanlı dönemi)
  sr онбаша [onbaša] ; onbaşı
  sq onbash ; onbaşı
  ro ombașă ; onbaşı (eski)
@yüzbaşı from_turkish
  ar يوزباشي [yūzbāşī] ; yüzbaşı (Mısır ordusunda 1952 öncesi rütbe)
  bg юзбашия [yuzbaşiya] ; yüzbaşı
  sr јузбаша [juzbaša] ; yüzbaşı
  sq jyzbash ; yüzbaşı
  ro iuzbașă ; yüzbaşı (eski)
@binbaşı from_turkish
  ar بكباشي [bikbāşī] ; binbaşı (Mısır ordusu, eski)
  bg бинбашия [binbaşiya] ; binbaşı
  sr бинбаша [binbaša] ; binbaşı
  sq binbash ; binbaşı
  el μπιμπασής [bimbasís] ; binbaşı
@başçavuş from_turkish
  ar باشجاويش [bāşcāwīş] ; başçavuş (Mısır polisi)
  bg башчауш [başçauş] ; başçavuş
@başbuğ shared_ancestor
  az başbuğ ; başkomutan
@bölük from_turkish
  sr буљук [buljuk] ; kalabalık, sürü ; ff:Sırpçada buljuk askerî anlamını yitirip "kalabalık, yığın" olmuştur
  bg бюлюк [byulyuk] ; bölük; kalabalık
  mk булук [buluk] ; yığın, kalabalık ; ff:Makedoncada "kalabalık, sürü" anlamındadır
  sq bylyk ; bölük; grup
  ro buluc ; yığın; topluca ; ff:Rumencede buluc "yığın" ve "buluc" zarfı "hep birden, üşüşerek" demektir
  el μπουλούκι [bulúki] ; gezici çalgıcı veya işçi topluluğu ; ff:Yunancada bulúki "gezici tiyatro kumpanyası, mevsimlik işçi grubu" anlamındadır
  fa بلوک [bolūk] ; nahiye, idari birim ; ff:Farsçada bolūk askerî birlik değil "ilçe, nahiye" demektir
  hu bölük ; bölük (tarih)
@tabur from_turkish
  ar طابور [ṭābūr] ; kuyruk, sıra ; ff:Arapçada ṭābūr "bekleme kuyruğu" anlamına kaymıştır; "beşinci kol" ṭābūr ḫāmis denir
  uk табір [tabir] ; kamp ; ff:Ukraynacada табір "kamp, ordugâh" demektir
  mk табор [tabor] ; kamp; tabur
  el ταμπούρι [tabúri] ; tabya, siperli mevzi ; ff:Yunancada tabúri "siper, istihkâm" anlamındadır
  sq tabor ; tabur; kamp
  az tabor ; tabur (tarih)
@karakol from_turkish
  ru караул [karaul] ; nöbet; nöbetçi birliği ; ff:Rusçada караул "nöbet" demektir; "караул!" ünlemi "imdat!" anlamına gelir
  uk караул [karaul] ; nöbet, muhafız
  bg караул [karaul] ; nöbet, nöbetçi
  sr караула [karaula] ; sınır karakolu, gözetleme kulesi
  mk караула [karaula] ; sınır karakolu
  ro caraulă ; nöbetçi
  sq karakoll ; karakol
  el καραούλι [karaúli] ; gözetleme yeri, nöbet
  ka ყარაული [qarauli] ; nöbetçi, bekçi
  hy ղարավուլ [ğaravul] ; nöbetçi (ağızlarda)
  fa قراول [qarāvol] ; nöbetçi, öncü
  pl karauł ; nöbet (tarih)
@karakol into_turkish
  mn харуул [haruul] ; nöbetçi, gözcü
@yeniçeri from_turkish
  ar إنكشاري [inkişārī] ; yeniçeri
  uk яничар [yanıçar] ; yeniçeri
  mk јаничар [janičar] ; yeniçeri
  hy ենիչերի [yeniçeri] ; yeniçeri
  ka იანიჩარი [ianiçari] ; yeniçeri
  pt janízaro ; yeniçeri
  es jenízaro ; yeniçeri; melez ; ff:İspanyolcada jenízaro ayrıca "farklı soydan anne babadan doğan" demektir
@sipahi from_turkish
  el σπαχής [spachís] ; sipahi
  mk спахија [spahija] ; sipahi; toprak ağası
  pt sipaio ; Hint askeri ; ff:Portekizce sipaio ve İngilizce sepoy, aynı Farsça kökten Hindistan'daki yerli askerleri adlandırır
  pl spahis ; sipahi
  uk спагі [spahi] ; sipahi
@sipahi into_turkish
  fa سپاهی [sepāhī] ; asker
  ur سپاہی [sipāhī] ; asker; polis eri ; ff:Urducada sipāhī bugün "er, polis memuru" demektir
@akıncı from_turkish
  bg акънджия [akındjiya] ; akıncı
  sr акинџија [akindžija] ; akıncı
  hu akindzsi ; akıncı
  ro achingiu ; akıncı
  mk акинџија [akindžija] ; akıncı
@azap from_turkish
  sr азап [azap] ; azap askeri
  bg азапин [azapin] ; azap askeri
  hu azab ; azap askeri
@deli from_turkish
  hu deli ; yiğit; boylu poslu ; ff:Macarcada deli "boylu poslu, yakışıklı" demektir; delilik anlamı yoktur
  el ντελής [delís] ; azgın, gözü pek ; ff:Yunancada delís "gözü kara, azgın" anlamındadır
  uk делі [deli] ; deli süvarisi (tarih)
@levent from_turkish
  el λεβέντης [levéndis] ; boylu poslu yiğit ; ff:Yunancada levéndis "yakışıklı, mert delikanlı" anlamına kaymıştır
  bg левент [levent] ; boylu poslu yiğit
  sq levend ; yiğit, çevik
  mk левент [levent] ; yiğit
  ro levent ; cömert, yiğit ; ff:Rumencede levent "cömert, eli açık" anlamı da taşır
@martolos into_turkish
  el αρματολός [armatolós] ; silahlı; Osmanlı hizmetindeki Hristiyan asker
  sr мартолос [martolos] ; martolos
  hu martalóc ; haydut, yağmacı ; ff:Macarcada martalóc "çapulcu, haydut" anlamına kaymıştır
@voynuk into_turkish
  bg войник [voynik] ; asker
  sr војник [vojnik] ; asker
  mk војник [vojnik] ; asker
  pl wojownik ; savaşçı
  uk воїн [voyin] ; savaşçı
@sekban from_turkish
  bg сеймен [seymen] ; sekban; silahlı muhafız
  sr сејмен [sejmen] ; sekban
  mk сејмен [sejmen] ; sekban
  ro seimen ; sekban (Eflak-Boğdan paralı askeri)
  hu szejmen ; sekban
@seymen from_turkish
  bg сеймен [seymen] ; sekban
  sr сејмен [sejmen] ; sekban
@çorbacı from_turkish
  bg чорбаджия [çorbacíya] ; zengin, ağa, patron ; ff:Bulgarcada çorbacı "zengin toprak sahibi, patron" anlamına kaymıştır
  sr чорбаџија [čorbadžija] ; zengin, hali vakti yerinde kişi ; ff:Sırpçada "zengin ev sahibi" demektir
  mk чорбаџија [čorbadžija] ; zengin, ağa
  el τσορμπατζής [tsorbatzís] ; zengin, kodaman ; ff:Yunancada "nüfuzlu zengin" anlamındadır
  sq çorbaxhi ; zengin, ağa
  ro ciorbagiu ; zengin, patron (eski)
@subaşı from_turkish
  sr субаша [subaša] ; nahiye yöneticisi; köy kâhyası ; ff:Sırpçada subaša "ağanın kâhyası, köy amiri" demektir
  bg субашия [subaşiya] ; subaşı
  mk субаша [subaša] ; subaşı
  hu szubasa ; subaşı
  ro subașă ; subaşı (eski)
@beylerbeyi from_turkish
  sr беглербег [beglerbeg] ; beylerbeyi
  bg бейлербей [beylerbey] ; beylerbeyi
  hu beglerbég ; beylerbeyi
  ro beilerbei ; beylerbeyi
  en beylerbey ; beylerbeyi
  pl bejlerbej ; beylerbeyi
@sancakbeyi from_turkish
  sr санџакбег [sandžakbeg] ; sancakbeyi
  hu szandzsákbég ; sancakbeyi
  bg санджакбей [sancakbey] ; sancakbeyi
  ro sangeacbei ; sancakbeyi
@kethüda from_turkish
  bg кехая [kehaya] ; çoban başı; kâhya ; ff:Bulgarcada kehaya "büyük sürü sahibi, çobanbaşı" anlamına kaymıştır
  sr ћехаја [ćehaja] ; kâhya; çobanbaşı
  mk ќеаја [kjeaja] ; kâhya
  el κεχαγιάς [kechagiás] ; kâhya; çobanbaşı
  sq qehaja ; kâhya
  ro chehaia ; kâhya; vekil
  hu kihája ; kethüda
@kaymakam from_turkish
  bg каймакам [kaymakam] ; kaymakam
  sr кајмакам [kajmakam] ; kaymakam
  mk кајмакам [kajmakam] ; kaymakam
  ro caimacam ; voyvoda vekili ; ff:Rumencede caimacam "Eflak-Boğdan'da voyvodanın vekili" demektir
  el καϊμακάμης [kaïmakámis] ; kaymakam
  sq kajmekam ; kaymakam
  ar قائمقام [qāʾimmaqām] ; ilçe yöneticisi (Lübnan, Irak); yarbay ; ff:Arapçada qāʾimmaqām "yarbay" rütbesi için de kullanılır
  hu kajmakám ; kaymakam
@vali from_turkish
  bg валия [valiya] ; vali
  sr валија [valija] ; vali
  el βαλής [valís] ; vali
  sq vali ; vali
  mk валија [valija] ; vali
  ro valiu ; vali
@vali into_turkish
  ar والي [wālī] ; vali
  fa والی [vālī] ; vali
@vilayet from_turkish
  bg вилает [vilaet] ; vilayet
  sr вилајет [vilajet] ; vilayet
  mk вилает [vilaet] ; vilayet
  ro vilaiet ; vilayet
  el βιλαέτι [vilaéti] ; vilayet
  sq vilajet ; vilayet
  ru вилайет [vilayet] ; vilayet
  hu vilajet ; vilayet
  uk вілаєт [vilaiet] ; vilayet
@vilayet into_turkish
  ar ولاية [wilāya] ; eyalet; ABD eyaleti ; ff:Arapçada wilāya ABD eyaletleri için de kullanılır (al-Wilāyāt al-Muttaḥida)
  fa ولایت [velāyat] ; il, eyalet
  ur ولایت [vilāyat] ; yabancı ülke; İngiltere ; ff:Urducada vilāyat "yabancı diyar, özellikle İngiltere" demektir; İngilizce Blighty buradan gelir
@ferman from_turkish
  bg ферман [ferman] ; ferman
  sr ферман [ferman] ; ferman
  mk ферман [ferman] ; ferman
  sq ferman ; ferman
  ro firman ; ferman
  el φιρμάνι [firmáni] ; ferman
  ru фирман [firman] ; ferman
  hu fermán ; ferman
  en firman ; ferman
  fr firman ; ferman
  pl ferman ; ferman
@ferman into_turkish
  fa فرمان [farmān] ; buyruk; direksiyon ; ff:Farsçada farmān bugün "araba direksiyonu" anlamında da kullanılır
  ur فرمان [farmān] ; buyruk
@defterdar from_turkish
  sr дефтердар [defterdar] ; defterdar
  bg дефтердар [defterdar] ; defterdar
  hu defterdár ; defterdar
  el δεφτερδάρης [defterdáris] ; defterdar
  ro tefterdar ; defterdar
  sq defterdar ; defterdar
@sadrazam from_turkish
  bg садразам [sadrazam] ; sadrazam
  sr садразам [sadrazam] ; sadrazam
  hu szadrazam ; sadrazam
  ro sadrazam ; sadrazam
  el σαδραζάμης [sadrazámis] ; sadrazam
@serasker from_turkish
  bg сераскер [serasker] ; serasker
  sr сераскер [serasker] ; serasker
  ro serascher ; serasker
  el σερασκέρης [seraskéris] ; serasker
  en seraskier ; serasker
  fr sérasquier ; serasker
@serdar from_turkish
  sr сердар [serdar] ; serdar; Karadağ'da kabile reisi ; ff:Karadağ ve Sırbistan'da serdar "kabile reisi, yerel komutan" unvanı olarak kullanılmıştır
  bg сердар [serdar] ; serdar
  sq serdar ; serdar
  ro serdar ; serdar; Eflak'ta süvari komutanı
  mk сердар [serdar] ; serdar
  hu szerdár ; serdar
@serdar into_turkish
  fa سردار [sardār] ; komutan, önder
  ur سردار [sardār] ; reis, önder; Sih erkeği ; ff:Urducada sardār Sih erkekleri için saygı sözü olarak da kullanılır
@mehter from_turkish
  bg мехтер [mehter] ; mehter
  sr мехтер [mehter] ; mehter
  hu mehter ; mehter
  ro mehter ; mehter müzisyeni
  el μεχτέρης [mechtéris] ; mehter
@kös into_turkish
  fa کوس [kūs] ; büyük davul
  az kos ; kös
  uz koʻs ; kös
@kös from_turkish
@nefir into_turkish
  ar نفير [nafīr] ; boru; toplanma çağrısı
  fa نفیر [nafīr] ; boru
@zurna from_turkish
  ru зурна [zurna] ; zurna
  uk зурна [zurna] ; zurna
  mk зурла [zurla] ; zurna
  ro zurnă ; zurna
  az zurna ; zurna
  uz surnay ; zurna
  kk сырнай [sırnay] ; zurna; akordeon ; ff:Kazakçada сырнай bugün "akordeon" için de kullanılır
@zurna into_turkish
  fa سرنا [sornā] ; zurna
@davul from_turkish
  ro daul ; davul (eski)
  hy դահուլ [dahul] ; davul (ağızlarda)
  mk даул [daul] ; davul
@davul into_turkish
  ar طبل [ṭabl] ; davul
  fa دهل [dohol] ; davul
@boru shared_ancestor
  az boru ; boru
  uz burgʻu ; boru
  tk bory ; boru
@alem into_turkish
  ar علم [ʿalam] ; bayrak
  fa علم [ʿalam] ; bayrak
  az ələm ; bayrak
@alemdar from_turkish
  bg алемдар [alemdar] ; bayraktar
  sr алемдар [alemdar] ; bayraktar
  sq alemdar ; bayraktar
@bayraktar from_turkish
  sr барјактар [barjaktar] ; bayraktar; düğün bayrakçısı ; ff:Sırpçada barjaktar ayrıca düğün alayında bayrağı taşıyan kişidir
  bg байрактар [bayraktar] ; bayraktar
  sq bajraktar ; bayraktar; kabile reisi ; ff:Kuzey Arnavutluk'ta bajraktar "bayrak altında toplanan boyun reisi" demektir
  mk бајрактар [bajraktar] ; bayraktar
  el μπαϊρακτάρης [baïraktáris] ; bayraktar
  ro bairactar ; bayraktar
  hu bajraktár ; bayraktar
@bayrak from_turkish
  el μπαϊράκι [baïráki] ; bayrak; isyan sancağı ; ff:Yunanca "sikóno baïráki" (bayrak kaldırmak) "isyan etmek" demektir
  ro bairac ; bayrak (eski)
  ar بيرق [bayraq] ; bayrak
  fa بیرق [beyraq] ; bayrak
  ur بیرق [bairaq] ; bayrak
  hy բայրաղ [bayrağ] ; bayrak (ağızlarda)
  ka ბაირაღი [bairaği] ; bayrak
  uk байрак [bayrak] ; vadi, dere yatağı ; ff:Ukraynaca байрак "ormanlı vadi" demektir; Türkçe bayır ile ilgilidir, bayrak ile değil
@sancak from_turkish
  ar سنجق [sancaq] ; sancak; idari birim
  fa سنجاق [sancāq] ; çengelli iğne ; ff:Farsçada sancāq "çengelli iğne, toplu iğne" anlamına kaymıştır
  el σαντζάκι [santzáki] ; sancak
  ro sangeac ; sancak
  ru санджак [sancak] ; sancak
  pl sandżak ; sancak
  uk санджак [sancak] ; sancak
  en sanjak ; sancak
  hy սանջակ [sancak] ; sancak
  uz sanjoq ; sancak
@ordu from_turkish
  fa اردو [ordū] ; ordu; kamp
  ur اردو [urdū] ; Urdu dili ; ff:Urduca dilinin adı "ordu dili" (zabān-i urdū) tamlamasından gelmiştir
  ro hoardă ; sürü, kalabalık ; ff:Avrupa dillerinde horde "düzensiz kalabalık" anlamına kaymıştır
  el ορδή [ordí] ; sürü, kalabalık ; ff:Yunancada ordí "vahşi kalabalık" demektir
  bg орда [orda] ; sürü, kalabalık
  sr хорда [horda] ; sürü, kalabalık
  sq ordi ; ordu, sürü
  pt horda ; sürü
  ky ордо [ordo] ; hanlık merkezi
  tk orda ; ordu; sürü
@orda shared_ancestor
  ru орда [orda] ; Altın Orda; kalabalık
  mn орд [ord] ; saray, hükümdar karargâhı
  kk орда [orda] ; hanlık merkezi; karargâh
@otağ from_turkish
  fa اتاق [otāq] ; oda ; ff:Farsça otāq "oda" Türkçe otağ sözünün alıntısıdır
  az otaq ; oda
  kk отау [otaw] ; yeni evlilerin çadırı
  ky отоо [otoo] ; yurt çadırı
  uz oʻtov ; yurt çadırı
  tk otag ; oda; çadır
@tuğ shared_ancestor
  kk ту [tu] ; bayrak
  ky туу [tuu] ; bayrak
  uz tugʻ ; tuğ, sancak
  az tuğ ; tuğ
  tk tug ; tuğ
@tümen shared_ancestor
  mn түмэн [tümen] ; on bin; kalabalık
  ru тьма [t'ma] ; on bin (eski); karanlık ; ff:Eski Rusçada тьма "on bin kişilik birlik" anlamıyla Türkçe tümen'den alınmıştır; "karanlık" anlamındaki тьма ayrı bir sözcüktür
  kk түмен [tümen] ; on bin
  ky түмөн [tümön] ; on bin; sayısız
  uz tuman ; on bin; ilçe ; ff:Özbekçede tuman bugün "ilçe" demektir
  az tümən ; on bin
  fa تومان [tūmān] ; İran para birimi ; ff:Farsçada tūmān "on bin dinar" değerindeki para biriminin adı olmuştur
  hu tömény ; yoğun, saf ; ff:Macarcada tömény "sayısız" anlamından "yoğun, konsantre" anlamına kaymıştır
@ulus shared_ancestor
  mn улс [uls] ; devlet, ülke ; ff:Moğolcada uls "devlet" demektir (Mongol Uls: Moğolistan Devleti)
  kk ұлыс [ulıs] ; ulus; idari bölge (tarih)
  ky улут [ulut] ; ulus, millet
  uz ulus ; ulus
  az ulus ; ulus
  ru улус [ulus] ; Sibirya'da köy, bölge ; ff:Rusçada улус Yakut ve Buryat bölgelerindeki idari birimi adlandırır
@elçi shared_ancestor
  mn элч [elç] ; elçi
  kk елші [elşi] ; elçi
  ky элчи [elçi] ; elçi
  uz elchi ; elçi
  az elçi ; elçi
  tk ilçi ; elçi
@alp shared_ancestor
  kk алып [alıp] ; dev, kocaman ; ff:Kazakçada алып "dev, devasa" anlamına kaymıştır
  ky алп [alp] ; dev; bahadır
  uz alp ; yiğit, bahadır
  az alp ; yiğit
  tk alp ; yiğit
@bahadır shared_ancestor
  mn баатар [baatar] ; kahraman ; ff:Ulan Batur (Ulaanbaatar) "Kızıl Kahraman" demektir
  ru богатырь [bogatır'] ; destan kahramanı
  uk богатир [bohatır] ; kahraman
  pl bohater ; kahraman ; ff:Lehçe bohater "kahraman" sözü Ukraynaca yoluyla Türkçe-Moğolca bağatur'dan gelir
  hu bátor ; cesur ; ff:Macarcada bátor sıfatı "cesur" demektir
  fa بهادر [bahādor] ; yiğit
  ur بہادر [bahādur] ; cesur, yiğit
  kk батыр [batır] ; yiğit, kahraman
  ky баатыр [baatır] ; yiğit, kahraman
  uz botir ; yiğit
  az bahadır ; yiğit
  tk batyr ; yiğit
@batur shared_ancestor
  mn баатар [baatar] ; kahraman
  kk батыр [batır] ; yiğit
  tk batyr ; yiğit
  bg батур [batur] ; Bulgar unvanı (tarih)
@tarkan shared_ancestor
  mn дархан [darhan] ; demirci; dokunulmaz ; ff:Moğolcada darhan "demirci usta; vergiden bağışık kişi" anlamındadır
  ru тархан [tarhan] ; vergiden bağışık toprak sahibi ; ff:Rusçada тархан "vergi ayrıcalığı olan kişi" demekti
  hu tárkány ; demirci (eski); yer adı ; ff:Macarcada tárkány eski bir meslek ve yer adı olarak kalmıştır
  kk тархан [tarhan] ; vergiden bağışık soylu
  bg таркан [tarkan] ; Bulgar unvanı (tarih)
@nöker shared_ancestor
  mn нөхөр [nöhör] ; arkadaş, yoldaş; koca ; ff:Moğolcada nöhör "arkadaş, yoldaş; eş" demektir; Türkçede "uşak, köle" anlamına kaymıştır
  ru нукер [nuker] ; koruma, paralı asker
  kk нөкер [nöker] ; maiyet, yoldaş
  ky нөкөр [nökör] ; yoldaş; hizmetkâr
  uz navkar ; hizmetçi asker
  az nökər ; uşak, hizmetçi
  fa نوکر [nowkar] ; hizmetçi
  ur نوکر [naukar] ; hizmetçi
@noyan shared_ancestor
  mn ноён [noyon] ; bey, soylu
  kk ноян [noyan] ; bey (tarih)
  ru нойон [noyon] ; Moğol beyi
@yasak from_turkish
  ru ясак [yasak] ; kürk vergisi ; ff:Rusçada ясак "Sibirya halklarından alınan kürk vergisi" demekti
  uk ясак [yasak] ; haraç, vergi (tarih)
  pl jasak ; vergi (tarih)
@yasak shared_ancestor
  mn засаг [zasag] ; hükûmet; yasa ; ff:Moğolcada zasag "hükûmet, yönetim" demektir
  kk жасақ [jasaq] ; milis, silahlı birlik ; ff:Kazakçada жасақ "silahlı birlik, milis" anlamındadır
  ky жасак [jasak] ; ordu birliği
  az yasaq ; yasak
  uz yasoq ; yasa; vergi
@yasavul from_turkish
  ru есаул [yesaul] ; Kazak subayı ; ff:Rusçada есаул "Kazak süvari yüzbaşısı" rütbesine dönüşmüştür
  uk осавул [osavul] ; Kazak subayı
  pl asauł ; Kazak subayı
@yasavul shared_ancestor
  mn засуул [zasuul] ; düzen görevlisi, hakem
  kk жасауыл [jasawıl] ; düzen görevlisi (tarih)
  uz yasovul ; muhafız, düzen görevlisi
@çapul from_turkish
  pl czambuł ; Tatar akın birliği ; ff:Lehçede czambuł "Tatar süvarilerinin yağma akını" demektir; "w czambuł" deyimi "toptan, hepsini birden" anlamındadır
  uk чамбул [çambul] ; akın birliği (tarih)
  ru чамбул [çambul] ; Tatar akın birliği (tarih)
@sadak from_turkish
  uk сагайдак [sahaydak] ; ok kılıfı
  ru саадак [saadak] ; ok ve yay kılıfı
  pl sajdak ; ok kılıfı
@sadak shared_ancestor
  mn саадаг [saadag] ; ok kılıfı
  kk садақ [sadaq] ; yay ; ff:Kazakçada садақ "yay" anlamına kaymıştır
  ky саадак [saadak] ; ok kılıfı; yay
  uz sadoq ; ok kılıfı
@cida from_turkish
  sr џида [džida] ; mızrak
  hu dzsida ; mızrak
  pl dzida ; mızrak
  bg джида [cida] ; mızrak
  uk джида [cıda] ; mızrak
@cida into_turkish
  mn жад [jad] ; mızrak
@bozdoğan from_turkish
  hu buzogány ; topuz ; ff:Macarca buzogány "topuz, gürz" Türkçe bozdoğan'dan gelir
  sr буздован [buzdovan] ; topuz
  bg боздуган [bozdugan] ; topuz
  ro buzdugan ; topuz
  pl buzdygan ; topuz; komutan asası ; ff:Lehçede buzdygan Polonya ordusunda rütbe asası olmuştur
  mk буздован [buzdovan] ; topuz
  uk буздиган [buzdıhan] ; topuz
@topuz from_turkish
  sr топуз [topuz] ; topuz
  bg топуз [topuz] ; topuz; ağırlık
  mk топуз [topuz] ; topuz
  sq topuz ; topuz
  el τοπούζι [topúzi] ; topuz
  ro topuz ; topuz
@hançer from_turkish
  sr ханџар [handžar] ; hançer
  bg ханджар [hancar] ; hançer
  mk анџар [andžar] ; hançer
  sq hanxhar ; hançer
  ro hanger ; hançer
  el χαντζάρι [chantzári] ; hançer
  hu handzsár ; hançer
  ru кинжал [kinjal] ; hançer ; ff:Rusça кинжал Kafkas dilleri yoluyla aynı Arapça ḫancar sözünden gelir
  uk кинджал [kındjal] ; hançer
  ka ხანჯალი [khanjali] ; hançer
  hy խանչալ [khançal] ; hançer
  pl kindżał ; hançer
@hançer into_turkish
  ar خنجر [ḫancar] ; hançer
  fa خنجر [ḫancar] ; hançer
  az xəncər ; hançer
  uz xanjar ; hançer
  kk қанжар [qanjar] ; hançer
  ky канжар [kanjar] ; hançer
  tk hanjar ; hançer
@yatağan from_turkish
  sr јатаган [jatagan] ; yatağan
  bg ятаган [yatagan] ; yatağan
  mk јатаган [jatagan] ; yatağan
  sq jatagan ; yatağan
  ro iatagan ; yatağan
  el γιαταγάνι [giatagáni] ; yatağan
  hu jatagán ; yatağan
  ru ятаган [yatagan] ; yatağan
  uk ятаган [yatahan] ; yatağan
  pl jatagan ; yatağan
  en yataghan ; yatağan
  fr yatagan ; yatağan
  de Jatagan ; yatağan
@kama from_turkish
  sr кама [kama] ; hançer, kama
  bg кама [kama] ; hançer
  mk кама [kama] ; hançer
  sq kamë ; kama
  ru кама [kama] ; Kafkas hançeri
  ro cama ; kama (eski)
@pala from_turkish
  sr пала [pala] ; pala
  bg пала [pala] ; pala
  hu pallos ; pala, geniş kılıç
  ro pală ; pala
@gürz into_turkish
  fa گرز [gorz] ; topuz
  az gürz ; gürz
  uz gurzi ; gürz
@teber into_turkish
  fa تبر [tabar] ; balta
  az təbər ; balta
  uz tabar ; balta
  ur تبر [tabar] ; balta
@zırh into_turkish
  fa زره [zereh] ; zırh
  az zireh ; zırh
  uz zirh ; zırh
  ur زرہ [zirah] ; zırh
@miğfer into_turkish
  ar مغفر [miġfar] ; miğfer
  az mığfər ; miğfer
@tolga shared_ancestor
  az dübilğə ; miğfer
  kk дулыға [dulığa] ; miğfer
  ky туулга [tuulga] ; miğfer
  uz dubulgʻa ; miğfer
  tk tuwulga ; miğfer
  mn дуулга [duulga] ; miğfer
@süngü shared_ancestor
  az süngü ; süngü
  kk сүңгі [süñgi] ; süngü
  ky сүңгү [süñgü] ; süngü
  tk süňňi ; süngü
  uz sanchqi ; süngü (sanç- kökünden) ; ff:Özbekçe sanchqi başka bir kökten (sanç-) türemiştir
@kargı shared_ancestor
  az qarğı ; kargı; kamış
  kk қарғы [qarğı] ; kargı
  tk garkı ; kargı
@kın shared_ancestor
  az qın ; kın
  kk қын [qın] ; kın
  ky кын [kın] ; kın
  uz qin ; kın
  tk gyn ; kın
@temren shared_ancestor
  kk темір [temir] ; demir ; ff:Kazakça темір "demir" demektir; temren "demirden yapılmış ok ucu" aynı kökün türevidir
  az təmrən ; ok ucu
@okçu shared_ancestor
  az oxçu ; okçu
  kk оқшы [oqşı] ; okçu
  uz oʻqchi ; okçu
  ky окчу [okçu] ; okçu
  tk okçy ; okçu
@urgan from_turkish
  ru аркан [arkan] ; kement ; ff:Rusça аркан "kement" Türkçe urgan/arkan'dan gelir
  uk аркан [arkan] ; kement
  pl arkan ; kement
  ro arcan ; kement
@urgan shared_ancestor
  az örkən ; urgan
  kk арқан [arqan] ; urgan; kement
  ky аркан [arkan] ; urgan
  uz arqon ; urgan
  tk arkan ; urgan
@kement into_turkish
  fa کمند [kamand] ; kement
  az kəmənd ; kement
  uz kamand ; kement
@bukağı shared_ancestor
  az buxov ; bukağı
  kk бұғау [buğaw] ; bukağı; zincir
  ky бугоо [bugoo] ; bukağı
  tk bugaw ; bukağı
@kamçı from_turkish
  ru камча [kamça] ; kamçı
  uk камча [kamça] ; kamçı
  hu kancsuka ; kamçı
  bg камшик [kamşik] ; kamçı
  sr камџија [kamdžija] ; kamçı
  mk камшик [kamşik] ; kamçı
  sq kamxhik ; kamçı
  ro camcie ; kamçı
@kamçı shared_ancestor
  az qamçı ; kamçı
  kk қамшы [qamşı] ; kamçı
  ky камчы [kamçı] ; kamçı
  uz qamchi ; kamçı
  tk gamçy ; kamçı
@kırbaç from_turkish
  bg кърбач [kırbaç] ; kırbaç
  sr корбач [korbač] ; kırbaç
  hu korbács ; kırbaç
  ro gârbaci ; kırbaç
  pl karbacz ; kırbaç
  uk карбач [karbaç] ; kırbaç
  mk корбач [korbač] ; kırbaç
@fişek from_turkish
  sr фишек [fišek] ; fişek; külah ; ff:Sırpçada fišek ayrıca "külah biçiminde kâğıt" demektir
  bg фишек [fişek] ; fişek; havai fişek
  mk фишек [fišek] ; fişek
  sq fishek ; fişek
  el φυσέκι [fyséki] ; fişek
  ro fișic ; fişek; para tomarı ; ff:Rumencede fișic "sarılmış madeni para tomarı" anlamı da taşır
  hu fisek ; fişek (eski)
@fişek into_turkish
  fa فشنگ [feşang] ; fişek
  az fişəng ; fişek
  uz fishang ; fişek
@gülle from_turkish
  sr ђуле [đule] ; top mermisi
  bg гюлле [gyulle] ; top mermisi; gülle
  mk ѓуле [gjule] ; top mermisi
  sq gjyle ; top mermisi
  ro ghiulea ; top mermisi
  el γκιουλές [giulés] ; top mermisi
@gülle into_turkish
  fa گلوله [golūle] ; mermi, kurşun
  az güllə ; mermi, kurşun ; ff:Azericede güllə "tüfek mermisi, kurşun" demektir
@barut from_turkish
@barut into_turkish
  fa باروت [bārūt] ; barut
  ar بارود [bārūd] ; barut
  az barıt ; barut
  uz porox ; barut (Rusçadan) ; ff:Özbekçe porox Rusça порох alıntısıdır; barut sözü eski metinlerde kalmıştır
  ur بارود [bārūd] ; barut
@barut shared_ancestor
  el πυρίτις [pyrítis] ; barut; çakmaktaşı ; ff:Eski Yunanca pyrítis "ateş taşı" Arapça bārūd'un kaynağı sayılır
  uk барут [barut] ; barut (ağızlarda)
@tüfek from_turkish
  ru тюфяк [tyufyak] ; erken ateşli silah (eski) ; ff:Eski Rusçada тюфяк bir tür top anlamında Türkçe tüfek'ten gelir; bugünkü "şilte" anlamı başka bir Türkçe sözcükten (döşek) alınmıştır
  uk тюфяк [tyufyak] ; erken ateşli silah (tarih)
  kk мылтық [mıltıq] ; tüfek ; ff:Kazakçada tüfek için мылтық kullanılır; tüfek sözü yoktur
  ky мылтык [mıltık] ; tüfek
  tk tüpeň ; tüfek
@topçu from_turkish
  bg топчия [topçiya] ; topçu
  sr тобџија [tobdžija] ; topçu
  mk топчија [topčija] ; topçu
  sq topçi ; topçu
  el τοπτσής [toptsís] ; topçu
  ro topciu ; topçu (eski)
  ar طوبجي [ṭōbcī] ; topçu (Mısır, eski)
@top from_turkish
  el τόπι [tópi] ; top (oyuncak); kumaş topu ; ff:Yunancada tópi yalnızca "oyun topu, kumaş topu" anlamındadır; silah için kanóni kullanılır
  hy թոփ [t'op'] ; top (silah)
  ka თოფი [topi] ; tüfek ; ff:Gürcücede topi "tüfek" anlamına kaymıştır
  ky топ [top] ; top
  tk top ; top
  uk топ [top] ; top (eski)
@piştov into_turkish
  hu pisztoly ; tabanca
  bg пищов [piştov] ; tabanca ; ff:Bulgarca пищов Türkçe piştov'dan geri alınmıştır
  sr пиштољ [pištolj] ; tabanca
  mk пиштол [pištol] ; tabanca
  ro pistol ; tabanca
  en pistol ; tabanca
  fr pistolet ; tabanca
  ru пистолет [pistolet] ; tabanca
@kalkan from_turkish
  sr калкан [kalkan] ; çatı alınlığı; kalkan balığı ; ff:Sırpçada kalkan "çatının üçgen alnı" anlamındadır
  bg калкан [kalkan] ; kalkan balığı; alınlık ; ff:Bulgarcada kalkan "kalkan balığı" ve "çatı alınlığı" demektir
  ro calcan ; kalkan balığı; alınlık ; ff:Rumencede calcan "kalkan balığı" ve "evin yan duvarı" anlamındadır
  el καλκάνι [kalkáni] ; kalkan balığı ; ff:Yunancada kalkáni yalnızca "kalkan balığı" demektir
  ru калкан [kalkan] ; kalkan balığı ; ff:Rusçada калкан Karadeniz kalkan balığının adıdır
  mk калкан [kalkan] ; kalkan balığı; alınlık
  uk калкан [kalkan] ; kalkan balığı
@kalkan shared_ancestor
  az qalxan ; kalkan
  kk қалқан [qalqan] ; kalkan
  ky калкан [kalkan] ; kalkan
  uz qalqon ; kalkan
  tk galkan ; kalkan
@kılıç from_turkish
  ru клыч [klıç] ; kılıç (eski, ağızlarda)
  bg кълъч [kılıç] ; kılıç (ağızlarda)
@hendek from_turkish
  bg хендек [hendek] ; hendek
  sr хендек [hendek] ; hendek
  mk ендек [endek] ; hendek
  sq hendek ; hendek
  ro hindichi ; hendek
@hendek into_turkish
  ar خندق [ḫandaq] ; hendek
  fa خندق [ḫandaq] ; hendek
  el χαντάκι [chandáki] ; hendek ; ff:Yunanca chandáki Arapçadan alınmıştır; Türkçeye ayrıca Osmanlı yoluyla da geçmiştir
  az xəndək ; hendek
  uz xandaq ; hendek
@tabya from_turkish
  bg табия [tabiya] ; tabya; taktik ; ff:Bulgarcada табия hem "tabya" hem "strateji, taktik" anlamında kullanılır
  sr табија [tabija] ; tabya
  mk табија [tabija] ; tabya
  sq tabje ; tabya
  el ταμπιά [tabiá] ; tabya
  ro tabie ; tabya
@tabya into_turkish
  ar طابية [ṭābiya] ; tabya
@palanka into_turkish
  hu palánk ; tahta perde; ahşap kale
  sr паланка [palanka] ; kasaba ; ff:Sırpçada palanka "küçük kasaba" anlamına kaymıştır (Smederevska Palanka)
  bg паланка [palanka] ; kasaba; ahşap kale
  ro palancă ; ahşap kale; çit
  it palanca ; kazık, kalas
@şarampol into_turkish
  hu sorompó ; bariyer, geçit engeli
@derbent from_turkish
  el ντερβένι [dervéni] ; dağ geçidi ; ff:Yunancada dervéni "dar dağ geçidi" demektir
  bg дервент [dervent] ; dağ geçidi; geçit bekçiliği
  sr дервента [derventa] ; geçit (yer adı Derventa) ; ff:Bosna'daki Derventa kenti adını Türkçe derbent'ten alır
  sq dervend ; geçit
  ro dervent ; geçit (eski)
  ru Дербент [Derbent] ; Dağıstan'daki Derbent kenti ; ff:Derbent kenti adı Farsça "kapı bağı, geçit kalesi" demektir
@derbent into_turkish
  fa دربند [darband] ; geçit; dar sokak
@kışla from_turkish
  ar قشلاق [qişlāq] ; kışla ; ff:Mısır Arapçasında qişlāq "kışla" Türkçeden alınmıştır
  bg къшла [kışla] ; ağıl, kışlak ; ff:Bulgarcada къшла "koyun ağılı" anlamındadır
  ro câșlă ; koyun ağılı, kışlak ; ff:Rumencede câșlă "çoban barınağı" demektir
  ru кишлак [kişlak] ; Orta Asya köyü ; ff:Rusçada кишлак "Özbek-Tacik köyü" anlamına kaymıştır
  uz qishloq ; köy ; ff:Özbekçede qishloq "köy" demektir
  kk қыстақ [qıstaq] ; kışlak
  az qışlaq ; kışlak
  fa قشلاق [qeşlāq] ; kışlak
@tersane from_turkish
  ar ترسانة [tarsāna] ; tersane; cephanelik ; ff:Arapçada tarsāna "silah deposu" anlamında da kullanılır
  el ταρσανάς [tarsanás] ; tersane
  bg терсане [tersane] ; tersane
  sq tersane ; tersane
@baltacı from_turkish
  ar بلطجي [balṭagī] ; kabadayı, zorba ; ff:Mısır Arapçasında balṭagī "sokak zorbası, haydut" anlamına kaymıştır
  bg балтаджия [baltaciya] ; baltacı; oduncu
  sr балтаџија [baltadžija] ; baltacı
  ro băltăgiu ; baltacı
@bostancı from_turkish
  bg бостанджия [bostanciya] ; bostancı; karpuzcu ; ff:Bulgarcada бостанджия "karpuz-kavun yetiştiren" demektir
  sr бостанџија [bostandžija] ; bostancı
  mk бостанџија [bostandžija] ; bostancı
  el μποστανιτζής [bostanitzís] ; bostancı
  ro bostangiu ; bostancı; saray muhafızı
@haraç from_turkish
  bg харач [haraç] ; haraç
  sr харач [harač] ; haraç
  mk арач [arač] ; haraç
  sq haraç ; haraç
  ro haraci ; haraç
  el χαράτσι [charátsi] ; haraç; ağır vergi ; ff:Yunancada charátsi "ağır, haksız vergi" anlamında yaşar
  hu harács ; haraç; yağma ; ff:Macarcada harács "yağma, talan" anlamına kaymıştır; harácsol "yağmalamak" demektir
  pl haracz ; haraç; zorla alınan para ; ff:Lehçede haracz bugün "mafyaya ödenen koruma parası" demektir
  uk харач [haraç] ; haraç
  ru харадж [haradj] ; haraç (tarih)
@haraç into_turkish
  ar خراج [ḫarāc] ; toprak vergisi
  fa خراج [ḫarāc] ; vergi
@cizye into_turkish
  ar جزية [cizya] ; gayrimüslim baş vergisi
  fa جزیه [cezye] ; cizye
  az cizyə ; cizye
@esir from_turkish
  pl jasyr ; Tatar tutsaklığı ; ff:Lehçede jasyr "Tatar akınlarında esir alınma" anlamında Türkçe esir'den gelir
  uk ясир [yasır] ; esir, tutsaklık
  ru ясырь [yasır'] ; esir (tarih)
@esir into_turkish
  ar أسير [asīr] ; esir
  fa اسیر [asīr] ; esir
  az əsir ; esir
  uz asir ; esir
  ur اسیر [asīr] ; esir
@ganimet into_turkish
  ar غنيمة [ġanīma] ; ganimet
  fa غنیمت [ġanīmat] ; ganimet; fırsat
  az qənimət ; ganimet
  uz gʻanimat ; ganimet; fırsat ; ff:Özbekçede gʻanimat "fırsat, kaçırılmaması gereken şey" anlamında yaygındır
  ur غنیمت [ġanīmat] ; ganimet; fırsat
@yağma from_turkish
  fa یغما [yaġmā] ; yağma
  ur یغما [yaġmā] ; yağma
  az yağma ; yağma
  uz yagʻmo ; yağma
@talan into_turkish
  fa تالان [tālān] ; yağma
  az talan ; yağma
  uz talon ; yağma
  kk талан [talan] ; yağma
@pusu from_turkish
  sr бусија [busija] ; pusu
  bg пусия [pusiya] ; pusu
  mk пусија [pusija] ; pusu
  sq pusi ; pusu
@pusu shared_ancestor
  az pusqu ; pusu
  tk busgy ; pusu
"""
