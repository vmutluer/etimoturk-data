# -*- coding: utf-8 -*-
"""Korpus 20 — Din, tasavvuf, ahlak ve halk inanışları."""

WORDS = r"""
mürit|n|ar|murīd|isteyen; şeyhe bağlanan|EAT|R-W-D|
keramet|n|ar|karāma|ikram; olağanüstü hâl|EAT|K-R-M|
# --- Allah, ilah ve temel inanç -------------------------------------------------------------
ilah|n|ar|ilāh|tapılan, tanrı|EAT|A-L-H|
ilahe|n|ar|ilāha|tanrıça|OSM|A-L-H|
ilahiyat|n|ar|ilāhiyyāt|tanrı bilgisi|OSM19|A-L-H|
uluhiyet|n|ar|ulūhiyya|tanrılık|OSM|A-L-H|
vallahi|intj|ar|wa-llāhi|Allah'a ant olsun|EAT|A-L-H|
billahi|intj|ar|bi-llāhi|Allah adına|EAT|A-L-H|
tanrıça|n|tr|tanrı|dişi tanrı|DD||
çalap|n|tr?|çalap|Tanrı|EAT||
yezdan|n|fa|yazdān|Tanrı|OSM||
ferişte|n|fa|firişte|melek|EAT||
rabbani|adj|ar|rabbānī|Tanrı'ya ait|OSM|R-B-B|
rububiyet|n|ar|rubūbiyya|rablık|OSM|R-B-B|
diyanet|n|ar|diyāna|dindarlık|OSM|D-Y-N|
mütedeyyin|adj|ar|mutadayyin|dindar|OSM|D-Y-N|
medyun|adj|ar|madyūn|borçlu|OSM|D-Y-N|
dinsiz|adj|tr|din|dini olmayan|OSM||
dindarlık|n|tr|dindar|dine bağlılık|OSM19|dār-|
imanlı|adj|tr|iman|inanan|OSM||
imansız|adj|ar|īmān|inancı olmayan|OSM||
müslim|adj|ar|muslim|teslim olmuş|EAT|S-L-M|
gayrimüslim|adj|ar|ġayr-i muslim|Müslüman olmayan|OSM|S-L-M|
teslimiyet|n|ar|taslīmiyya|kendini bırakma|OSM19|S-L-M|
müslümanlık|n|tr|müslüman|İslam dini|EAT||
gâvur|n|fa|gabr|Zerdüşt; kâfir|EAT||
frenk|n|fa|farang|Batı Avrupalı|EAT||ger:Frank>fa:farang>tr:frenk
ecnebi|n|ar|acnabī|yabancı|OSM|C-N-B|
cenup|n|ar|canūb|güney|OSM|C-N-B|
cenabet|n|ar|canāba|cünüplük|EAT|C-N-B|
ictinap|n|ar|ictināb|kaçınma|OSM|C-N-B|
canip|n|ar|cānib|yan, taraf|OSM|C-N-B|
zımmi|n|ar|ḏimmī|koruma altındaki|OSM|Z-M-M|
zem|n|ar|ḏamm|kınama, yerme|OSM|Z-M-M|
mezmum|adj|ar|maḏmūm|kınanmış|OSM|Z-M-M|
cizye|n|ar|cizya|baş vergisi|EAT||
tekfir|n|ar|takfīr|kâfir sayma|OSM|K-F-R|
münafık|n|ar|munāfiq|ikiyüzlü inançsız|EAT|N-F-K|
nifak|n|ar|nifāq|ikiyüzlülük|EAT|N-F-K|
nafaka|n|ar|nafaqa|geçimlik|EAT|N-F-K|
infak|n|ar|infāq|Allah yolunda harcama|OSM|N-F-K|
mürtet|n|ar|murtadd|dinden dönen|OSM|R-D-D|
irtidat|n|ar|irtidād|dinden dönme|OSM|R-D-D|
merdut|adj|ar|mardūd|reddedilmiş|OSM|R-D-D|
tereddüt|n|ar|taraddud|gidip gelme; kararsızlık|OSM|R-D-D|
reddetmek|v|ar|radd|geri çevirmek|EAT|R-D-D|
zındık|n|ar|zindīq|Mani dinli; dinsiz|EAT||fa:zandīk>ar:zindīq>tr:zındık
mülhit|n|ar|mulḥid|dinden sapan|OSM|L-H-D|
ilhat|n|ar|ilḥād|dinden sapma|OSM|L-H-D|
lahit|n|ar|laḥd|mezar oyuğu; taş mezar|EAT|L-H-D|
fasık|n|ar|fāsiq|günaha dalan|EAT|F-S-K|
fısk|n|ar|fisq|günaha dalma|OSM|F-S-K|
takva|n|ar|taqwā|Allah'tan sakınma|EAT|W-K-Y|
müttaki|adj|ar|muttaqī|sakınan|OSM|W-K-Y|
huşu|n|ar|ḫuşūʿ|boyun eğme; derin saygı|EAT|H-Ş-A|
haşyet|n|ar|ḫaşya|korku ile saygı|OSM|H-Ş-A|
itaat|n|ar|iṭāʿa|boyun eğme|EAT|T-W-A|
muti|adj|ar|muṭīʿ|boyun eğen|OSM|T-W-A|
istitaat|n|ar|istiṭāʿa|güç yetirme|OSM|T-W-A|
isyan|n|ar|ʿiṣyān|baş kaldırma|EAT|A-S-Y|
asi|adj|ar|ʿāṣī|baş kaldıran|EAT|A-S-Y|
ihlas|n|ar|iḫlāṣ|arınmış içtenlik|EAT|H-L-S|
halis|adj|ar|ḫāliṣ|katışıksız|EAT|H-L-S|
muhlis|adj|ar|muḫliṣ|içten bağlı|OSM|H-L-S|
halas|n|ar|ḫalāṣ|kurtuluş|OSM|H-L-S|
tahlis|n|ar|taḫlīṣ|kurtarma|OSM|H-L-S|
hülasa|n|ar|ḫulāṣa|öz, özet|OSM|H-L-S|
niyet|n|ar|niyya|kasıt, amaç|EAT||
rıza|n|ar|riḍā|hoşnutluk|EAT|R-D-Y|
razı|adj|ar|rāḍī|hoşnut|EAT|R-D-Y|
rıdvan|n|ar|riḍwān|hoşnutluk; cennet kapıcısı|OSM|R-D-Y|
salah|n|ar|ṣalāḥ|iyilik, düzelme|OSM|S-L-H|
dalalet|n|ar|ḍalāla|sapma|EAT||
sapkın|adj|tr|sap-|yoldan çıkmış|DD|*sap-|
sapık|adj|tr|sapık|doğru yoldan ayrılmış|OSM|*sap-|
sapak|n|tr|sapak|yoldan ayrılan yer|TDK|*sap-|
sapmak|v|tr|sap-|yoldan ayrılmak|DLT|*sap-|
batıl|adj|ar|bāṭil|boş, geçersiz|EAT|B-T-L|
iptal|n|ar|ibṭāl|geçersiz kılma|OSM|B-T-L|
battal|adj|ar|baṭṭāl|işsiz; hükümsüz; kocaman|EAT|B-T-L|
bidat|n|ar|bidʿa|sonradan çıkan şey|EAT|B-D-A|
ibda|n|ar|ibdāʿ|yoktan yaratma|OSM|B-D-A|
bedii|adj|ar|badīʿī|güzel, eşsiz|OSM19|B-D-A|
hurafe|n|ar|ḫurāfa|uydurma söz, masal|OSM||
fitne|n|ar|fitna|sınama; kargaşa|EAT|F-T-N|
fettan|adj|ar|fattān|fitne çıkaran; cilveli|OSM|F-T-N|
meftun|adj|ar|maftūn|tutkun|OSM|F-T-N|
fesat|n|ar|fasād|bozulma; kargaşa|EAT|F-S-D|
müfsit|n|ar|mufsid|bozguncu|OSM|F-S-D|
fasit|adj|ar|fāsid|bozuk|OSM|F-S-D|
ifsat|n|ar|ifsād|bozma|OSM|F-S-D|
# --- Mezhep ve topluluklar -----------------------------------------------------------------
mezhep|n|ar|maḏhab|gidilen yol|EAT|Z-H-B|
zehap|n|ar|ḏahāb|gidiş; sanı|OSM|Z-H-B|
meşrep|n|ar|maşrab|içilen yer; huy|OSM|Ş-R-B|
sünni|n|ar|sunnī|sünnete bağlı|EAT|S-N-N|
mesnun|adj|ar|masnūn|sünnete uygun|OSM|S-N-N|
şia|n|ar|şīʿa|taraftar topluluğu|EAT|Ş-Y-A|
şii|n|ar|şīʿī|Şia'dan olan|OSM|Ş-Y-A|
şayi|adj|ar|şāʾiʿ|yayılmış|OSM|Ş-Y-A|
alevi|n|ar|ʿalawī|Ali yanlısı|OSM|A-L-W|
ulvi|adj|ar|ʿulwī|yüce|OSM|A-L-W|
âli|adj|ar|ʿālī|yüksek|EAT|A-L-W|
teali|n|ar|taʿālī|yükselme|OSM|A-L-W|
hanefi|n|ar|ḥanafī|Ebu Hanife mezhebinden|EAT||
şafii|n|ar|şāfiʿī|İmam Şafii mezhebinden|EAT||
maliki|n|ar|mālikī|İmam Malik mezhebinden|OSM||
hanbeli|n|ar|ḥanbalī|İbn Hanbel mezhebinden|OSM||
caferi|n|ar|caʿfarī|İmam Cafer mezhebinden|OSM||
vehhabi|n|ar|wahhābī|Abdülvehhab yanlısı|OSM19||
selef|n|ar|salaf|öncekiler|OSM|S-L-F|
selefi|n|ar|salafī|öncekilere uyan|MOD|S-L-F|
halife|n|ar|ḫalīfa|ardıl, vekil|EAT|H-L-F|
hilafet|n|ar|ḫilāfa|halifelik|EAT|H-L-F|
halef|n|ar|ḫalaf|ardıl|OSM|H-L-F|
ihtilaf|n|ar|iḫtilāf|görüş ayrılığı|OSM|H-L-F|
şeyhülislam|n|ar|şayḫu'l-islām|İslam'ın şeyhi|OSM|Ş-Y-H|
meşihat|n|ar|maşīḫa|şeyhlik makamı|OSM19|Ş-Y-H|
kazasker|n|ar|qāḍī ʿaskar|ordu kadısı|OSM|K-D-Y|
nakip|n|ar|naqīb|başkan, vekil|OSM|N-K-B|
nikap|n|ar|niqāb|yüz örtüsü|OSM|N-K-B|
menkıbe|n|ar|manqaba|övülecek iş; ermiş öyküsü|OSM|N-K-B|
şerif|n|ar|şarīf|soylu; Peygamber soyundan|EAT|Ş-R-F|
eşraf|n|ar|aşrāf|ileri gelenler|OSM|Ş-R-F|
müşerref|adj|ar|muşarraf|onurlandırılmış|OSM|Ş-R-F|
teşrif|n|ar|taşrīf|onurlandırma; gelme|OSM|Ş-R-F|
seyyid|n|ar|sayyid|efendi; Peygamber soyundan|EAT||
ihvan|n|ar|iḫwān|kardeşler|OSM|A-H-W|
ahi|n|ar|aḫī|kardeşim; esnaf birliği üyesi|EAT|A-H-W|
uhuvvet|n|ar|uḫuwwa|kardeşlik|OSM|A-H-W|
ahilik|n|tr|ahi|ahi teşkilatı|OSM|A-H-W|
fütüvvet|n|ar|futuwwa|yiğitlik; esnaf ahlakı|EAT|F-T-W|
feta|n|ar|fatā|genç, yiğit|OSM|F-T-W|
ulema|n|ar|ʿulamāʾ|bilginler|EAT|İ-L-M|
allame|n|ar|ʿallāma|çok bilgin|OSM|İ-L-M|
ilmihal|n|ar|ʿilm-i ḥāl|hal bilgisi|OSM|İ-L-M|
akait|n|ar|ʿaqāʾid|inanç esasları|OSM|A-K-D|
müçtehit|n|ar|muctahid|içtihat eden|OSM|C-H-D|
icma|n|ar|icmāʿ|görüş birliği|OSM|C-M-A|
mütekellim|n|ar|mutakallim|kelam bilgini|OSM|K-L-M|
mutasavvıf|n|ar|mutaṣawwif|tasavvuf ehli|OSM|S-W-F|
tasavvufi|adj|ar|taṣawwufī|tasavvufa ilişkin|OSM19|S-W-F|
sofu|n|ar|ṣūfī|yünlü giyen; dindar|EAT|S-W-F|
sofi|n|ar|ṣūfī|tasavvuf ehli|EAT|S-W-F|
muhaddis|n|ar|muḥaddiṯ|hadis bilgini|OSM|H-D-S|
hadise|n|ar|ḥādiṯa|olay|OSM|H-D-S|
ihdas|n|ar|iḥdāṯ|yeniden ortaya koyma|OSM|H-D-S|
hudus|n|ar|ḥudūṯ|sonradan var olma|OSM|H-D-S|
müfessir|n|ar|mufassir|tefsir yazan|OSM||
kari|n|ar|qāriʾ|okuyan|OSM|K-R-A|
mukri|n|ar|muqriʾ|Kuran okutan|OSM|K-R-A|
kıraat|n|ar|qirāʾa|okuma|EAT|K-R-A|
Kuran|prop|ar|qurʾān|okunan|EAT|K-R-A|
hafızlık|n|tr|hafız|Kuran ezberi|OSM|H-F-Z|
mevize|n|ar|mawʿiẓa|öğüt|OSM||
nasihat|n|ar|naṣīḥa|öğüt|EAT||
irşat|n|ar|irşād|doğru yolu gösterme|OSM|R-Ş-D|
mürşit|n|ar|murşid|yol gösteren|EAT|R-Ş-D|
reşit|adj|ar|raşīd|olgun; doğru yolda|OSM|R-Ş-D|
rüşt|n|ar|ruşd|olgunluk|OSM|R-Ş-D|
tebliğ|n|ar|tablīġ|ulaştırma, bildirme|OSM|B-L-Ğ|
beliğ|adj|ar|balīġ|güzel ve etkili söyleyen|OSM|B-L-Ğ|
belagat|n|ar|balāġa|güzel söz söyleme|OSM|B-L-Ğ|
mübalağa|n|ar|mubālaġa|abartma|OSM|B-L-Ğ|
baliğ|adj|ar|bāliġ|erginliğe ulaşmış|OSM|B-L-Ğ|
kayyum|n|ar|qayyūm|ayakta tutan; cami görevlisi|OSM|K-W-M|
kayyım|n|ar|qayyim|yöneten; cami bakıcısı|OSM|K-W-M|
softa|n|fa|sūḫte|yanmış; medrese öğrencisi|OSM||
şakirt|n|fa|şāgird|öğrenci, çırak|EAT||
danişmend|n|fa|dānişmand|bilgi sahibi|EAT||
hace|n|fa|ḫʷāce|efendi, hoca|EAT||
# --- Namaz, abdest, temizlik ---------------------------------------------------------------
salat|n|ar|ṣalāt|namaz|EAT|S-L-W|
salavat|n|ar|ṣalawāt|namazlar; Peygamber'e dua|EAT|S-L-W|
musalla|n|ar|muṣallā|namaz kılınan yer|EAT|S-L-W|
musalli|n|ar|muṣallī|namaz kılan|OSM|S-L-W|
namazlık|n|tr|namaz|namaz için örtü|OSM||
namazgâh|n|fa|namāzgāh|namaz yeri|EAT|-gāh|
kamet|n|ar|iqāma|ayağa kaldırma; namaza çağrı|EAT|K-W-M|
tekbir|n|ar|takbīr|büyükleme|EAT|K-B-R|
mütekebbir|adj|ar|mutakabbir|büyüklenen|OSM|K-B-R|
tehlil|n|ar|tahlīl|lā ilāhe illallah deme|OSM|H-L-L|
tahiyyat|n|ar|taḥiyyāt|selamlar|OSM|H-Y-Y|
teşehhüt|n|ar|taşahhud|şehadet getirme|OSM|Ş-H-D|
rükû|n|ar|rukūʿ|eğilme|EAT||
kuud|n|ar|quʿūd|oturma|OSM|K-A-D|
kaide|n|ar|qāʿida|temel; kural|EAT|K-A-D|
vitir|n|ar|witr|tek sayılı namaz|EAT|W-T-R|
tevatür|n|ar|tawātur|ardı ardına gelme; yaygın söylenti|OSM|W-T-R|
mütevatir|adj|ar|mutawātir|pek çok kişice aktarılan|OSM|W-T-R|
nafile|n|ar|nāfila|fazladan yapılan|EAT|N-F-L|
enfal|n|ar|anfāl|ganimetler|OSM|N-F-L|
eda|n|ar|adāʾ|yerine getirme|OSM|A-D-Y|
tediye|n|ar|taʾdiya|ödeme|OSM19|A-D-Y|
iade|n|ar|iʿāda|geri verme|OSM|A-W-D|
avdet|n|ar|ʿawda|dönüş|OSM|A-W-D|
mutat|adj|ar|muʿtād|alışılmış|OSM|A-W-D|
itiyat|n|ar|iʿtiyād|alışkanlık|OSM|A-W-D|
teravih|n|ar|tarāwīḥ|dinlenmeler|EAT|R-W-H|
mukabele|n|ar|muqābala|karşılıklı okuma|OSM|K-B-L|
kabil|adj|ar|qābil|kabul eden; olabilir|EAT|K-B-L|
mukabil|adj|ar|muqābil|karşılık olan|OSM|K-B-L|
istikbal|n|ar|istiqbāl|karşılama; gelecek|OSM|K-B-L|
makbul|adj|ar|maqbūl|kabul edilmiş|EAT|K-B-L|
ikbal|n|ar|iqbāl|yönelme; talih|EAT|K-B-L|
tekabül|n|ar|taqābul|karşılık gelme|OSM19|K-B-L|
kıblegâh|n|fa|qibla-gāh|kıble yönü|OSM|-gāh|
ibadetgâh|n|fa|ʿibādat-gāh|tapınma yeri|OSM|-gāh|
ziyaretgâh|n|fa|ziyārat-gāh|ziyaret yeri|OSM|-gāh|
ibadethane|n|fa|ʿibādat-ḫāne|tapınma evi|OSM19|-hāne|
gusülhane|n|fa|ġusl-ḫāne|yıkanma yeri|OSM|-hāne|
abdestli|adj|tr|abdest|abdest almış|OSM||
abit|n|ar|ʿābid|kulluk eden|EAT|A-B-D|
mabude|n|ar|maʿbūda|tapılan dişi|OSM|A-B-D|
gusül|n|ar|ġusl|yıkanma|EAT|Ğ-S-L|
gasil|n|ar|ġasl|yıkama|OSM|Ğ-S-L|
gassal|n|ar|ġassāl|ölü yıkayıcı|OSM|Ğ-S-L|
taharet|n|ar|ṭahāra|temizlik|EAT|T-H-R|
tahir|adj|ar|ṭāhir|temiz|EAT|T-H-R|
tathir|n|ar|taṭhīr|temizleme|OSM|T-H-R|
mutahhar|adj|ar|muṭahhar|arındırılmış|OSM|T-H-R|
teyemmüm|n|ar|tayammum|yönelme; toprakla temizlenme|EAT||
necis|adj|ar|nacis|pis|EAT|N-C-S|
necaset|n|ar|nacāsa|pislik|EAT|N-C-S|
pak|adj|fa|pāk|temiz|EAT||
misvak|n|ar|miswāk|diş temizleme çubuğu|EAT||
imsak|n|ar|imsāk|tutma, kendini tutma|EAT|M-S-K|
mümsik|adj|ar|mumsik|eli sıkı|OSM|M-S-K|
# --- Oruç, takvim, kutsal günler ------------------------------------------------------------
savm|n|ar|ṣawm|oruç|EAT|S-W-M|
saim|n|ar|ṣāʾim|oruçlu|OSM|S-W-M|
oruçlu|adj|tr|oruç|oruç tutan|EAT||
ramazan|n|ar|ramaḍān|kavurucu sıcak ayı|EAT||
şevval|n|ar|şawwāl|hicri onuncu ay|EAT||
muharrem|n|ar|muḥarram|haram kılınmış ay|EAT|H-R-M|
mahrum|adj|ar|maḥrūm|yoksun bırakılmış|EAT|H-R-M|
safer|n|ar|ṣafar|hicri ikinci ay|EAT||
recep|n|ar|racab|hicri yedinci ay|EAT||
şaban|n|ar|şaʿbān|hicri sekizinci ay|EAT||
zilkade|n|ar|ḏū'l-qaʿda|oturma ayı|OSM|K-A-D|
zilhicce|n|ar|ḏū'l-ḥicca|hac ayı|OSM|H-C-C|
rebiyülevvel|n|ar|rabīʿu'l-awwal|ilk bahar ayı|OSM||
hicret|n|ar|hicra|göç|EAT|H-C-R|
muhacir|n|ar|muhācir|göç eden|EAT|H-C-R|
hicri|adj|ar|hicrī|hicrete göre|OSM19|H-C-R|
milat|n|ar|mīlād|doğum|OSM19|W-L-D|
miladi|adj|ar|mīlādī|doğuma göre|OSM19|W-L-D|
tevellüt|n|ar|tawallud|doğma|OSM|W-L-D|
veladet|n|ar|wilāda|doğum|OSM|W-L-D|
velet|n|ar|walad|çocuk|EAT|W-L-D|
mevlüt|n|ar|mawlid|doğum yeri ve zamanı|EAT|W-L-D|
mevlithan|n|fa|mawlid-ḫʷān|mevlit okuyan|OSM|-hān|
ayinhan|n|fa|āyīn-ḫʷān|ayin okuyan|OSM|-hān|
gazelhan|n|fa|ġazal-ḫʷān|gazel okuyan|OSM|-hān|
rumi|adj|ar|rūmī|Anadolu'ya ait; Rumi takvim|EAT||grc:Rhōmaîos>ar:rūmī>tr:rumi
miraç|n|ar|miʿrāc|merdiven; göğe yükselme|EAT||
regaip|n|ar|raġāʾib|çok istenen şeyler|OSM||
akika|n|ar|ʿaqīqa|doğum kurbanı|OSM||
kurbanlık|n|tr|kurban|kurban edilecek hayvan|OSM|K-R-B|
adak|n|tr|adak|adanan şey|EAT|*ada-|
adamak|v|tr|ata-|söz verip ayırmak|DLT|*ada-|
adanmak|v|tr|adan-|kendini vermek|OSM|*ada-|
# --- Hac ve kutsal yerler ---------------------------------------------------------------------
Kâbe|prop|ar|kaʿba|küp biçimli yapı|EAT||
umre|n|ar|ʿumra|ziyaret|EAT|A-M-R|
zemzem|n|ar|zamzam|Mekke'deki kuyu suyu|EAT||
Arafat|prop|ar|ʿarafāt|tanıma yeri|EAT|A-R-F|
Mina|prop|ar|minā|Mekke yakınındaki vadi|OSM||
Müzdelife|prop|ar|muzdalifa|yaklaşılan yer|OSM||
mikat|n|ar|mīqāt|belirlenmiş yer ve zaman|OSM||
telbiye|n|ar|talbiya|lebbeyk deme|OSM||
Kudüs|prop|ar|al-quds|kutsal yer|EAT|K-D-S|
mukaddes|adj|ar|muqaddas|kutsanmış|EAT|K-D-S|
takdis|n|ar|taqdīs|kutsama|OSM|K-D-S|
kutsi|adj|ar|qudsī|kutsal|OSM|K-D-S|
kuddüs|adj|ar|quddūs|çok kutsal|EAT|K-D-S|
kutsiyet|n|ar|qudsiyya|kutsallık|OSM19|K-D-S|
kutsamak|v|tr|kut|kutsal saymak|DD|*kut|
kutsanmak|v|tr|kut|kutsal kılınmak|DD|*kut|
teberrük|n|ar|tabarruk|uğur sayma|OSM|B-R-K|
ravza|n|ar|rawḍa|bahçe; Peygamber kabri|OSM||
# --- Zekât, sadaka, vakıf, hayır --------------------------------------------------------------
tezkiye|n|ar|tazkiya|arındırma|OSM||
vakıf|n|ar|waqf|durdurma; bağış kurumu|EAT|W-K-F|
vakfe|n|ar|waqfa|duruş|OSM|W-K-F|
vakfiye|n|ar|waqfiyya|vakıf senedi|OSM|W-K-F|
evkaf|n|ar|awqāf|vakıflar|OSM|W-K-F|
mevkuf|adj|ar|mawqūf|durdurulmuş; tutuklu|OSM|W-K-F|
tevkif|n|ar|tawqīf|durdurma; tutuklama|OSM|W-K-F|
mütevelli|n|ar|mutawallī|vakıf yöneticisi|OSM|W-L-Y|
hayrat|n|ar|ḫayrāt|iyilikler|EAT|H-Y-R|
hayırsever|adj|tr|hayır|iyilik seven|TDK|H-Y-R|
darülaceze|n|ar|dāru'l-ʿacaza|güçsüzler evi|OSM19|A-C-Z|
aciz|adj|ar|ʿāciz|güçsüz|EAT|A-C-Z|
acz|n|ar|ʿacz|güçsüzlük|OSM|A-C-Z|
icaz|n|ar|iʿcāz|aciz bırakma; mucizevi söz|OSM|A-C-Z|
taciz|n|ar|taʿcīz|aciz bırakma; rahatsız etme|OSM|A-C-Z|
mucize|n|ar|muʿciza|aciz bırakan şey|EAT|A-C-Z|
sebilhane|n|fa|sabīl-ḫāne|su dağıtma yeri|OSM|-hāne|
bimarhane|n|fa|bīmār-ḫāne|hasta evi|OSM|-hāne|
ecir|n|ar|acr|karşılık, sevap|EAT|A-C-R|
icar|n|ar|icār|kiralama|OSM|A-C-R|
müstecir|n|ar|mustaʾcir|kiracı|OSM|A-C-R|
mükâfat|n|ar|mukāfaʾa|karşılık, ödül|OSM||
azap|n|ar|ʿaḏāb|işkence; ceza|EAT|A-Z-B|
muazzep|adj|ar|muʿaḏḏab|azap çeken|OSM|A-Z-B|
ikab|n|ar|ʿiqāb|ceza|OSM||
# --- Kuran, hadis, dua ------------------------------------------------------------------------
mushaf|n|ar|muṣḥaf|sayfalar derlemesi|EAT|S-H-F|
sahife|n|ar|ṣaḥīfa|sayfa|EAT|S-H-F|
suhuf|n|ar|ṣuḥuf|sayfalar; küçük kutsal kitaplar|OSM|S-H-F|
sahaf|n|ar|ṣaḥḥāf|kitapçı|OSM|S-H-F|
tecvit|n|ar|tacwīd|güzelleştirme|OSM||
hizip|n|ar|ḥizb|bölük; Kuran bölümü|OSM||
besmele|n|ar|basmala|bismillah deme|OSM||
hamdele|n|ar|ḥamdala|elhamdülillah deme|OSM|H-M-D|
hamt|n|ar|ḥamd|övgü|EAT|H-M-D|
tahmit|n|ar|taḥmīd|elhamdülillah deme|OSM|H-M-D|
Muhammed|prop|ar|muḥammad|övülmüş|EAT|H-M-D|
sübhan|n|ar|subḥān|her kusurdan uzak|EAT|S-B-H|
sübhanallah|intj|ar|subḥāna'llāh|Allah her kusurdan uzaktır|EAT|S-B-H|
tesbihat|n|ar|tasbīḥāt|tesbihler|OSM|S-B-H|
estağfurullah|intj|ar|astaġfiru'llāh|Allah'tan bağışlanma dilerim|EAT|Ğ-F-R|
istiğfar|n|ar|istiġfār|bağışlanma dileme|EAT|Ğ-F-R|
mağfiret|n|ar|maġfira|bağışlama|EAT|Ğ-F-R|
gufran|n|ar|ġufrān|bağışlanma|OSM|Ğ-F-R|
gaffar|adj|ar|ġaffār|çok bağışlayan|EAT|Ğ-F-R|
gafur|adj|ar|ġafūr|bağışlayıcı|EAT|Ğ-F-R|
vird|n|ar|wird|düzenli okunan dua|OSM|W-R-D|
evrat|n|ar|awrād|virdler|OSM|W-R-D|
vürut|n|ar|wurūd|geliş|OSM|W-R-D|
varit|adj|ar|wārid|gelen; akla gelen|OSM|W-R-D|
niyaz|n|fa|niyāz|yalvarma|EAT||
münacat|n|ar|munācāt|fısıldaşma; Tanrı'ya yakarış|EAT|N-C-W|
necat|n|ar|nacāt|kurtuluş|OSM|N-C-W|
naat|n|ar|naʿt|niteleme; Peygamber övgüsü|OSM||
mersiye|n|ar|marṯiya|ağıt|OSM||
siyer|n|ar|siyar|gidişler; Peygamber yaşamı|OSM|S-Y-R|
hilye|n|ar|ḥilya|süs; Peygamber'in niteliklerini anlatan yazı|OSM||
tevhithane|n|fa|tawḥīd-ḫāne|zikir yeri|OSM|-hāne|
lanet|n|ar|laʿna|kovma, ilenç|EAT|L-A-N|
melun|adj|ar|malʿūn|lanetlenmiş|EAT|L-A-N|
beddua|n|fa|bad-duʿā|kötü dua|OSM|D-A-W|
kargış|n|tr|kargış|ilenç|DLT|*karga-|
kargımak|v|tr|karga-|ilenmek|DLT|*karga-|
ilenmek|v|tr|ilen-|beddua etmek|EAT|*ilen-|
ilenç|n|tr|ilenç|beddua|TDK|*ilen-|
alkış|n|tr|alkış|övgü, dua; el çırpma|DLT|*alka-|
alkışlamak|v|tr|alka-|övmek, dua etmek|DLT|*alka-|
yakarış|n|tr|yakar-|yalvarma|DD|*yakar-|
yakarı|n|tr|yakar-|dua|DD|*yakar-|
tapmak|v|tr|tap-|hizmet etmek, tapınmak|ORH|*tap-|
tapınmak|v|tr|tapın-|kulluk etmek|DLT|*tap-|
tapınak|n|tr|tapın-|ibadet yeri|DD|*tap-|
tapıncak|n|tr|tapın-|put|DD|*tap-|
# --- Peygamberler, melekler, ahiret --------------------------------------------------------
nebi|n|ar|nabī|haber getiren|EAT|N-B-A|
nübüvvet|n|ar|nubuwwa|peygamberlik|EAT|N-B-A|
enbiya|n|ar|anbiyāʾ|peygamberler|EAT|N-B-A|
resul|n|ar|rasūl|elçi|EAT|R-S-L|
risalet|n|ar|risāla|elçilik|EAT|R-S-L|
risale|n|ar|risāla|mektup; küçük kitap|OSM|R-S-L|
irsal|n|ar|irsāl|gönderme|OSM|R-S-L|
mürsel|adj|ar|mursal|gönderilmiş|OSM|R-S-L|
vahiy|n|ar|waḥy|gizli bildirim|EAT||
ilham|n|ar|ilhām|içe doğma|EAT|L-H-M|
mülhem|adj|ar|mulham|esinlenmiş|OSM|L-H-M|
sahabe|n|ar|ṣaḥāba|arkadaşlar|EAT|S-H-B|
ashap|n|ar|aṣḥāb|arkadaşlar|EAT|S-H-B|
musahip|n|ar|muṣāḥib|arkadaşlık eden|OSM|S-H-B|
havari|n|ar|ḥawārī|yardımcı; İsa'nın öğrencisi|EAT||
Mesih|prop|ar|masīḥ|yağla kutsanmış|EAT|M-S-H|he:māşīaḥ>ar:masīḥ>tr:Mesih
mesh|n|ar|masḥ|sıvazlama|EAT|M-S-H|
Cebrail|prop|ar|cibrīl|Tanrı'nın gücü|EAT||he:gavrīʾēl>ar:cibrīl>tr:Cebrail
Azrail|prop|ar|ʿazrāʾīl|Tanrı yardım etti|EAT||he:ʿazarʾēl>ar:ʿazrāʾīl>tr:Azrail
Mikail|prop|ar|mīkāʾīl|Tanrı gibi kim|EAT||he:mīkhāʾēl>ar:mīkāʾīl>tr:Mikail
İsrafil|prop|ar|isrāfīl|sur üfleyen melek|EAT||
huri|n|ar|ḥūr|kara gözlü|EAT||
gılman|n|ar|ġilmān|genç hizmetkârlar|OSM||
zebani|n|ar|zabāniya|cehennem bekçisi|EAT||
iblis|prop|ar|iblīs|umutsuz; şeytan|EAT||grc:diábolos>ar:iblīs>tr:iblis
ifrit|n|ar|ʿifrīt|güçlü cin|OSM||
cehennemlik|adj|tr|cehennem|cehenneme layık|OSM|C-N-N|
cennetlik|adj|tr|cennet|cennete layık|OSM|C-N-N|
firdevs|n|ar|firdaws|bahçe; cennet|EAT||fa:pardēs>grc:parádeisos>ar:firdaws>tr:firdevs
kevser|n|ar|kawṯar|çokluk; cennet ırmağı|EAT||
tuba|n|ar|ṭūbā|mutluluk; cennet ağacı|EAT||
sidre|n|ar|sidra|Arabistan kirazı; sınır ağacı|OSM||
arş|n|ar|ʿarş|taht; en yüksek gök|EAT||
kürsü|n|ar|kursī|iskemle; yüksek oturak|EAT||
levh|n|ar|lawḥ|tahta, levha|EAT||
sırat|n|ar|ṣirāṭ|yol; cehennem köprüsü|EAT||la:strata>grc:stráta>ar:ṣirāṭ>tr:sırat
mahşer|n|ar|maḥşar|toplanma yeri|EAT|H-Ş-R|
haşir|n|ar|ḥaşr|toplama; diriliş|OSM|H-Ş-R|
ahir|adj|ar|āḫir|son|EAT|A-H-R|
tehir|n|ar|taʾḫīr|erteleme|OSM|A-H-R|
müteahhir|adj|ar|mutaʾaḫḫir|sonradan gelen|OSM|A-H-R|
teehhür|n|ar|taʾaḫḫur|gecikme|OSM|A-H-R|
ebed|n|ar|abad|sonsuzluk|EAT||
ebedi|adj|ar|abadī|sonsuz|EAT||
ebediyet|n|ar|abadiyya|sonsuzluk|OSM||
ezel|n|ar|azal|başlangıcı olmayan|EAT||
ezeli|adj|ar|azalī|öncesiz|EAT||
sermedi|adj|ar|sarmadī|sürekli, ölümsüz|OSM||
mevta|n|ar|mawtā|ölüler|EAT|M-W-T|
mevt|n|ar|mawt|ölüm|EAT|M-W-T|
memat|n|ar|mamāt|ölüm|OSM|M-W-T|
meyyit|n|ar|mayyit|ölü|OSM|M-W-T|
vefat|n|ar|wafāt|ölüm|EAT|W-F-Y|
vafi|adj|ar|wāfī|yeterli; sözünü tutan|OSM|W-F-Y|
ifa|n|ar|īfāʾ|yerine getirme|OSM|W-F-Y|
istifa|n|ar|istiʿfāʾ|görevden çekilme|OSM19|W-F-Y|
irtihal|n|ar|irtiḥāl|göçme; ölüm|OSM|R-H-L|
rahle|n|ar|raḥl|yük; okuma sehpası|EAT|R-H-L|
merhale|n|ar|marḥala|konak yeri; aşama|OSM|R-H-L|
rihlet|n|ar|riḥla|yolculuk; ölüm|OSM|R-H-L|
kefen|n|ar|kafan|ölü örtüsü|EAT|K-F-N|
tekfin|n|ar|takfīn|kefenleme|OSM|K-F-N|
telkin|n|ar|talqīn|öğretme; mezarda okunan|EAT||
taziye|n|ar|taʿziya|baş sağlığı|OSM||
gömüt|n|tr|göm-|mezar|DD|*göm-|
gömü|n|tr|göm-|gömülmüş hazine|DLT|*göm-|
sin|n|tr|sin|mezar|DLT||
şefaat|n|ar|şafāʿa|aracılık|EAT|Ş-F-A|
şefi|n|ar|şafīʿ|aracı olan|OSM|Ş-F-A|
tövbe|n|ar|tawba|dönüş; pişmanlık|EAT|T-W-B|
tevvab|adj|ar|tawwāb|tövbeleri kabul eden|OSM|T-W-B|
tövbekâr|adj|fa|tawba-kār|tövbe eden|OSM|-kār|
af|n|ar|ʿafw|bağışlama|EAT|A-F-W|
muaf|adj|ar|muʿāf|bağışlanmış|OSM|A-F-W|
muafiyet|n|ar|muʿāfiyya|bağışıklık|OSM19|A-F-W|
# --- Tasavvuf: kavramlar ---------------------------------------------------------------------
zühd|n|ar|zuhd|dünyadan el çekme|EAT|Z-H-D|
zahit|n|ar|zāhid|dünyadan el çeken|EAT|Z-H-D|
halvet|n|ar|ḫalwa|yalnız kalma|EAT||
halveti|n|ar|ḫalwatī|Halvetiye tarikatından|OSM||
hali|adj|ar|ḫālī|boş|OSM||
cezbe|n|ar|caḏba|çekilme; coşku|EAT|C-Z-B|
cazibe|n|ar|cāḏiba|çeken güç|OSM|C-Z-B|
cazip|adj|ar|cāḏib|çekici|OSM19|C-Z-B|
meczup|adj|ar|macḏūb|çekilmiş; kendinden geçmiş|OSM|C-Z-B|
incizap|n|ar|incīḏāb|çekilme|OSM|C-Z-B|
fani|adj|ar|fānī|geçici|EAT|F-N-Y|
fenafillah|n|ar|fanāʾ fi'llāh|Allah'ta yok olma|OSM|F-N-Y|
celi|adj|ar|calī|açık, belirgin|OSM|C-L-W|
cila|n|ar|cilāʾ|parlatma|OSM|C-L-W|
mütecelli|adj|ar|mutacallī|görünen, beliren|OSM|C-L-W|
murakabe|n|ar|murāqaba|gözetleme; içe bakış|OSM|R-K-B|
mürakıp|n|ar|murāqib|denetleyen|OSM19|R-K-B|
rabıta|n|ar|rābiṭa|bağ|OSM|R-B-T|
irtibat|n|ar|irtibāṭ|bağlantı|OSM|R-B-T|
merbut|adj|ar|marbūṭ|bağlı|OSM|R-B-T|
murabıt|n|ar|murābiṭ|sınır boyunda bekleyen; derviş|OSM|R-B-T|
sema|n|ar|samāʿ|işitme; dönerek zikir|EAT|S-M-A|
semah|n|ar|samāʿ|Alevi ayin dansı|OSM|S-M-A|
istima|n|ar|istimāʿ|dinleme|OSM|S-M-A|
sami|n|ar|sāmiʿ|dinleyen|OSM|S-M-A|
semai|n|ar|samāʿī|işitmeye dayalı; bir şiir türü|OSM|S-M-A|
semazen|n|fa|samāʿ-zan|sema yapan|OSM|-zen|
neyzen|n|fa|nay-zan|ney çalan|OSM|-zen|
kudümzen|n|fa|qudūm-zan|kudüm çalan|OSM|-zen|
kudüm|n|ar|qudūm|geliş; çifte davul|OSM||
keşkül|n|fa|kaşkūl|derviş çanağı|OSM||
tennure|n|ar|tannūra|tandır biçimli etek|OSM||
teber|n|fa|tabar|balta|OSM||
nefir|n|ar|nafīr|boru; sığır boynuzu|OSM||
matbah|n|ar|maṭbaḫ|pişirme yeri|OSM|T-B-H|
zaviye|n|ar|zāwiya|köşe; küçük tekke|EAT|Z-W-Y|
münzevi|adj|ar|munzawī|köşeye çekilmiş|OSM|Z-W-Y|
inziva|n|ar|inziwāʾ|köşeye çekilme|OSM|Z-W-Y|
hankah|n|fa|ḫānaqāh|derviş evi|EAT||
asitane|n|fa|āsitāne|eşik; merkez tekke|OSM||
çilehane|n|fa|çilla-ḫāne|çile yeri|OSM|-hāne|
semahane|n|fa|samāʿ-ḫāne|sema yeri|OSM|-hāne|
meydancı|n|tr|meydan|tekkede meydanı düzenleyen|OSM||
postnişin|n|fa|pūst-nişīn|posta oturan|OSM|-nişīn|
şehnişin|n|fa|şāh-nişīn|şah oturağı; cumba|OSM|-nişīn|
hanenişin|adj|fa|ḫāne-nişīn|evde oturan|OSM|-nişīn|
çilekeş|adj|fa|çilla-kaş|çile çeken|OSM|-keş|
esrarkeş|n|fa|asrār-kaş|esrar içen|OSM19|-keş|
serkeş|adj|fa|sar-kaş|baş çeken; dik başlı|OSM|-keş|
cefakeş|adj|fa|cafā-kaş|cefa çeken|OSM|-keş|
afyonkeş|n|fa|afyūn-kaş|afyon içen|OSM|-keş|
putperest|n|fa|but-parast|puta tapan|EAT|-perest|
ateşperest|n|fa|ātaş-parast|ateşe tapan|OSM|-perest|
hayalperest|adj|fa|ḫayāl-parast|hayale tapan|OSM19|-perest|
menfaatperest|adj|fa|manfaʿat-parast|çıkara tapan|OSM19|-perest|
şekilperest|adj|fa|şakl-parast|biçime tapan|MOD|-perest|
ateşgede|n|fa|ātaş-kada|ateş evi|OSM|-gede|
meykede|n|fa|may-kada|şarap evi|OSM|-gede|
butkede|n|fa|but-kada|put evi|OSM|-gede|
puthane|n|fa|but-ḫāne|put evi|OSM|-hāne|
put|n|fa|but|heykel, tapınılan nesne|EAT||sa:buddha>fa:but>tr:put
sanem|n|ar|ṣanam|put|EAT||
dervişane|adj|fa|darvīşāne|derviş gibi|OSM|-ane|
tarikatçı|n|tr|tarikat|tarikata bağlı|MOD||
kalender|n|fa|qalandar|dünyayı önemsemeyen derviş|EAT||
kalenderi|n|fa|qalandarī|Kalenderiye dervişi|OSM||
abdal|n|ar|abdāl|bedeller; gezgin derviş|EAT|B-D-L|
tebdil|n|ar|tabdīl|değiştirme|OSM|B-D-L|
mübadele|n|ar|mubādala|karşılıklı değişim|OSM|B-D-L|
melamet|n|ar|malāma|kınanma|EAT|L-W-M|
melami|n|ar|malāmī|kınanmayı seçen derviş|OSM|L-W-M|
pir|n|fa|pīr|yaşlı; tarikat kurucusu|EAT||
bektaşi|n|fa|baktāşī|Hacı Bektaş yolundan|OSM||
mevlevi|n|ar|mawlawī|Mevlana yolundan|OSM|W-L-Y|
nakşibendi|n|fa|naqşbandī|nakış bağlayan; tarikat üyesi|OSM||
nakşi|n|fa|naqşī|Nakşibendi|OSM||
kadiri|n|ar|qādirī|Abdülkadir Geylani yolundan|OSM|K-D-R|
rifai|n|ar|rifāʿī|Ahmed Rifai yolundan|OSM||
bayrami|n|tr|Bayram|Hacı Bayram yolundan|OSM||
yesevi|n|tr|Yesi|Ahmed Yesevi yolundan|OSM||
çelebi|n|tr?|çalap|Tanrı'ya ait; efendi|EAT||
hazret|n|ar|ḥaḍra|huzur; saygı unvanı|EAT|H-D-R|
ihzar|n|ar|iḥḍār|hazır etme; mahkemeye getirme|OSM|H-D-R|
muhzır|n|ar|muḥḍir|mahkemeye getiren|OSM|H-D-R|
kutup|n|ar|quṭb|eksen; en büyük veli|EAT||
gavs|n|ar|ġawṯ|yardım; büyük veli|OSM||
ermiş|n|tr|er-|ulaşmış; veli|EAT|*er-|
ermek|v|tr|er-|ulaşmak|ORH|*er-|
erişmek|v|tr|eriş-|ulaşmak|DLT|*er-|
mistik|adj|fr|mystique|gizemli|CUM||grc:mystikós>fr:mystique>tr:mistik
mistisizm|n|fr|mysticisme|gizemcilik|CUM||
ruhban|n|ar|ruhbān|rahipler|OSM|R-H-B|
ruhbaniyet|n|ar|rahbāniyya|rahiplik|OSM|R-H-B|
# --- Ahlak ve erdemler -----------------------------------------------------------------------
hayâ|n|ar|ḥayāʾ|utanma|EAT|H-Y-Y|
iffet|n|ar|ʿiffa|namusluluk|EAT|A-F-F|
afif|adj|ar|ʿafīf|iffetli|OSM|A-F-F|
ar|n|ar|ʿār|utanç|EAT||
arsız|adj|tr|ar|utanmaz|OSM||
ırz|n|ar|ʿirḍ|namus|EAT|A-R-D|
vakar|n|ar|waqār|ağırbaşlılık|EAT|W-K-R|
vakur|adj|ar|waqūr|ağırbaşlı|OSM|W-K-R|
heybet|n|ar|hayba|korku veren görkem|EAT|H-Y-B|
mehabet|n|ar|mahāba|ululuk|OSM|H-Y-B|
haşmet|n|ar|ḥaşma|görkem|OSM|H-Ş-M|
muhteşem|adj|ar|muḥtaşam|görkemli|OSM|H-Ş-M|
halim|adj|ar|ḥalīm|yumuşak huylu|EAT|H-L-M|
hilim|n|ar|ḥilm|yumuşak huyluluk|OSM|H-L-M|
haşin|adj|ar|ḫaşin|sert, kaba|OSM|H-Ş-N|
huşunet|n|ar|ḫuşūna|sertlik|OSM|H-Ş-N|
metin|adj|ar|matīn|sağlam, dayanıklı|OSM|M-T-N|
metanet|n|ar|matāna|dayanıklılık|OSM|M-T-N|
cüret|n|ar|curʾa|yüreklilik|OSM||
asıl|n|ar|aṣl|kök, temel|EAT|A-S-L|
asil|adj|ar|aṣīl|köklü, soylu|OSM|A-S-L|
asalet|n|ar|aṣāla|soyluluk|OSM|A-S-L|
soylu|adj|tr|soy|asil|TDK||
alicenap|adj|ar|ʿālī-canāb|yüce yanlı; cömert|OSM|A-L-W|
civanmert|adj|fa|cavān-mard|genç er; yiğit|OSM||
namahrem|adj|fa|nā-maḥram|mahrem olmayan|OSM|nā-|
nahoş|adj|fa|nā-ḫoş|hoş olmayan|OSM|nā-|
naçar|adj|fa|nā-çār|çaresiz|EAT|nā-|
naçiz|adj|fa|nā-çīz|değersiz|OSM|nā-|
nankör|adj|fa|nān-kūr|ekmek körü|EAT||
kadirşinas|adj|fa|qadr-şinās|değer bilen|OSM|-şinās|
hakşinas|adj|fa|ḥaqq-şinās|hak bilen|OSM|-şinās|
vefadar|adj|fa|wafā-dār|vefalı|OSM|dār-|
minnettar|adj|fa|minnat-dār|minnet duyan|OSM|dār-|
kindar|adj|fa|kīn-dār|kin tutan|OSM|dār-|
sahi|adj|ar|saḫī|cömert|EAT|S-H-W|
sahavet|n|ar|saḫāwa|cömertlik|OSM|S-H-W|
cömertlik|n|tr|cömert|eli açıklık|EAT||
nekes|adj|fa|nākas|alçak; cimri|EAT||
tamah|n|ar|ṭamaʿ|açgözlülük|EAT||
açgözlü|adj|tr|aç|doymak bilmez|OSM||
tokgözlü|adj|tr|tok|gözü tok|OSM||
hırs|n|ar|ḥirṣ|aşırı istek|EAT|H-R-S|
haris|adj|ar|ḥarīṣ|hırslı|OSM|H-R-S|
kanaat|n|ar|qanāʿa|yetinme; inanç|EAT|K-N-A|
kani|adj|ar|qāniʿ|yetinen; inanmış|OSM|K-N-A|
ikna|n|ar|iqnāʿ|inandırma|OSM|K-N-A|
insaf|n|ar|inṣāf|yarıya bölme; hakkaniyet|EAT|N-S-F|
nısıf|n|ar|niṣf|yarı|OSM|N-S-F|
munsif|adj|ar|munṣif|insaflı|OSM|N-S-F|
şefkat|n|ar|şafaqa|acıyarak sevme|EAT|Ş-F-K|
müşfik|adj|ar|muşfiq|şefkatli|OSM|Ş-F-K|
şefik|adj|ar|şafīq|şefkatli|OSM|Ş-F-K|
lütuf|n|ar|luṭf|incelik; iyilik|EAT|L-T-F|
latif|adj|ar|laṭīf|ince, hoş|EAT|L-T-F|
latife|n|ar|laṭīfa|ince söz; şaka|OSM|L-T-F|
iltifat|n|ar|iltifāt|yönelme; güzel söz|OSM|L-T-F|
mültefit|adj|ar|multafit|ilgi gösteren|OSM|L-T-F|
nimet|n|ar|niʿma|iyilik, bolluk|EAT|N-A-M|
inam|n|ar|inʿām|bağış|OSM|N-A-M|
naim|n|ar|naʿīm|bolluk içinde yaşama|OSM|N-A-M|
münim|adj|ar|munʿim|nimet veren|OSM|N-A-M|
minnet|n|ar|minna|iyilik; şükran borcu|EAT|M-N-N|
memnun|adj|ar|mamnūn|minnet duyan; hoşnut|OSM|M-N-N|
imtinan|n|ar|imtinān|minnet duyma|OSM|M-N-N|
mennan|adj|ar|mannān|çok ihsan eden|OSM|M-N-N|
aziz|adj|ar|ʿazīz|değerli; ermiş|EAT|A-Z-Z|
azize|n|ar|ʿazīza|ermiş kadın|OSM|A-Z-Z|
muazzez|adj|ar|muʿazzaz|değerli tutulan|OSM|A-Z-Z|
taziz|n|ar|taʿzīz|yüceltme|OSM|A-Z-Z|
# --- Kötü huylar ------------------------------------------------------------------------------
riya|n|ar|riyāʾ|gösteriş|EAT|R-A-Y|
mürai|adj|ar|murāʾī|ikiyüzlü|OSM|R-A-Y|
mağrur|adj|ar|maġrūr|aldanmış; kibirli|EAT||
ukala|adj|ar|ʿuqalāʾ|akıllılar; bilgiç|OSM|A-K-L|
küstah|adj|fa|gustāḫ|saygısız|EAT||
yüzsüz|adj|tr|yüz|utanmaz|OSM||
hıyanet|n|ar|ḫiyāna|hainlik|EAT||
iftira|n|ar|iftirāʾ|uydurarak suçlama|EAT|F-R-Y|
müfteri|n|ar|muftarī|iftira eden|OSM|F-R-Y|
bühtan|n|ar|buhtān|kara çalma|EAT|B-H-T|
mebhut|adj|ar|mabhūt|şaşkına dönmüş|OSM|B-H-T|
gıybet|n|ar|ġība|arkadan konuşma|EAT|Ğ-Y-B|
gayb|n|ar|ġayb|görünmeyen|EAT|Ğ-Y-B|
gaip|adj|ar|ġāʾib|görünmez; kayıp|EAT|Ğ-Y-B|
kayıp|n|ar|ġāʾib|yitik|OSM|Ğ-Y-B|
gayri|adj|ar|ġayr|başka|EAT|Ğ-Y-R|
mugayir|adj|ar|muġāyir|aykırı|OSM|Ğ-Y-R|
tagayyür|n|ar|taġayyur|değişme|OSM|Ğ-Y-R|
tekzip|n|ar|takḏīb|yalanlama|OSM19|K-Z-B|
kâzip|adj|ar|kāḏib|yalancı|OSM|K-Z-B|
garez|n|ar|ġaraḍ|amaç; gizli düşmanlık|EAT||
hasut|adj|ar|ḥasūd|kıskanç|OSM||
çekememek|v|tr|çek-|kıskanmak|OSM|*çek-|
gaddar|adj|ar|ġaddār|sözünden dönen; acımasız|OSM|Ğ-D-R|
gadir|n|ar|ġadr|haksızlık|OSM|Ğ-D-R|
cebbar|adj|ar|cabbār|zorlayan; güçlü|EAT|C-B-R|
icbar|n|ar|icbār|zorlama|OSM|C-B-R|
cebren|adv|ar|cabran|zorla|OSM|C-B-R|
kahır|n|ar|qahr|ezme; derin üzüntü|EAT|K-H-R|
kahhar|adj|ar|qahhār|kahredici|EAT|K-H-R|
makhur|adj|ar|maqhūr|kahrolmuş|OSM|K-H-R|
settar|adj|ar|sattār|çok örten|EAT|S-T-R|
tesettür|n|ar|tasattur|örtünme|OSM|S-T-R|
mestur|adj|ar|mastūr|örtülü|OSM|S-T-R|
rezzak|adj|ar|razzāq|rızık veren|EAT|R-Z-K|
erzak|n|ar|arzāq|rızıklar; yiyecek|OSM|R-Z-K|
merzuk|adj|ar|marzūq|rızıklanmış|OSM|R-Z-K|
rezil|adj|ar|raḏīl|alçak|EAT|R-Z-L|
rezalet|n|ar|raḏāla|alçaklık|OSM|R-Z-L|
şer|n|ar|şarr|kötülük|EAT|Ş-R-R|
şerir|adj|ar|şarīr|kötü|OSM|Ş-R-R|
iyilik|n|tr|iyi|iyi olma|EAT||
kötülük|n|tr|kötü|kötü olma|EAT||
fuhuş|n|ar|fuḥş|edepsizlik|OSM|F-H-Ş|
fahişe|n|ar|fāḥişa|edepsiz kadın|OSM|F-H-Ş|
fahiş|adj|ar|fāḥiş|aşırı|OSM|F-H-Ş|
zina|n|ar|zinā|evlilik dışı ilişki|EAT|Z-N-Y|
zani|n|ar|zānī|zina eden|OSM|Z-N-Y|
riba|n|ar|ribā|faiz|EAT||
feyiz|n|ar|fayḍ|taşma; bereket|EAT|F-Y-D|
feyyaz|adj|ar|fayyāḍ|bol veren|OSM|F-Y-D|
mübah|adj|ar|mubāḥ|izin verilmiş|EAT||
müstehap|adj|ar|mustaḥabb|sevilen; sevap olan|OSM|H-B-B|
habib|n|ar|ḥabīb|sevgili|EAT|H-B-B|
mahbup|n|ar|maḥbūb|sevilen|EAT|H-B-B|
muhip|n|ar|muḥibb|seven|OSM|H-B-B|
mendup|adj|ar|mandūb|yapılması beğenilen|OSM||
vacip|adj|ar|wācib|gerekli|EAT|W-C-B|
vücup|n|ar|wucūb|gereklilik|OSM|W-C-B|
icap|n|ar|īcāb|gerektirme|OSM|W-C-B|
mucip|adj|ar|mūcib|gerektiren|OSM|W-C-B|
vecibe|n|ar|wacība|ödev|OSM19|W-C-B|
farize|n|ar|farīḍa|Allah'ın buyruğu|OSM|F-R-D|
faraza|adv|ar|faraḍan|diyelim ki|OSM|F-R-D|
faraziye|n|ar|faraḍiyya|varsayım|OSM19|F-R-D|
mefruz|adj|ar|mafrūḍ|varsayılan|OSM|F-R-D|
kerih|adj|ar|karīh|iğrenç|OSM|K-R-H|
kerahet|n|ar|karāha|iğrenme; mekruhluk|OSM|K-R-H|
ikrah|n|ar|ikrāh|zorlama; tiksinme|OSM|K-R-H|
vaz|n|ar|waḍʿ|koyma|OSM|W-D-A|
mevzu|n|ar|mawḍūʿ|konulmuş; konu|OSM|W-D-A|
vaziyet|n|ar|waḍʿiyya|konum, durum|OSM19|W-D-A|
mevzi|n|ar|mawḍiʿ|konulan yer|OSM|W-D-A|
sır|n|ar|sirr|giz|EAT|S-R-R|
esrar|n|ar|asrār|gizler|EAT|S-R-R|
sürur|n|ar|surūr|sevinç|OSM|S-R-R|
mesrur|adj|ar|masrūr|sevinçli|OSM|S-R-R|
hilekâr|adj|fa|ḥīla-kār|hile yapan|OSM|-kār|
riyakârlık|n|tr|riyakâr|ikiyüzlülük|OSM19|-kār|
sitemkâr|adj|fa|sitam-kār|sitem eden|OSM|-kār|
isyankâr|adj|fa|ʿiṣyān-kār|baş kaldıran|OSM|-kār|
itaatkâr|adj|fa|iṭāʿat-kār|boyun eğen|OSM|-kār|
kanaatkâr|adj|fa|qanāʿat-kār|yetinen|OSM|-kār|
hilebaz|adj|fa|ḥīla-bāz|hileci|OSM|-bāz|
sahtekârlık|n|tr|sahtekâr|dolandırıcılık|OSM19|-kār|
sitem|n|fa|sitam|zulüm; serzeniş|EAT||
mihnet|n|ar|miḥna|sıkıntı|EAT||
çile|n|fa|çilla|kırk gün; sıkıntı|EAT||
# --- Halk inanışları ---------------------------------------------------------------------------
nazarlık|n|tr|nazar|nazara karşı takılan|OSM|N-Z-R|
muska|n|ar|nusḫa|yazılı kopya; büyülü yazı|EAT|N-S-H|
nüsha|n|ar|nusḫa|kopya|OSM|N-S-H|
istinsah|n|ar|istinsāḫ|kopya etme|OSM|N-S-H|
tenasüh|n|ar|tanāsuḫ|ruh göçü|OSM|N-S-H|
efsun|n|fa|afsūn|büyü|EAT|afsūn|
füsun|n|fa|fusūn|büyü|OSM|afsūn|
efsunlu|adj|tr|efsun|büyülü|OSM|afsūn|
efsane|n|fa|afsāna|masal|EAT||
büyücü|n|tr|büyü|büyü yapan|OSM||
büyülü|adj|tr|büyü|büyülenmiş|OSM||
fal|n|ar|faʾl|uğurlu belirti|EAT||
falcı|n|tr|fal|fal bakan|OSM||
falname|n|fa|fāl-nāme|fal kitabı|OSM|-nāme|
yıldızname|n|fa|yıldız-nāme|yıldız falı kitabı|OSM|-nāme|
nasihatname|n|fa|naṣīḥat-nāme|öğüt kitabı|OSM|-nāme|
kehanet|n|ar|kahāna|gelecekten haber verme|OSM|K-H-N|
kâhin|n|ar|kāhin|gelecekten haber veren|EAT|K-H-N|
remil|n|ar|raml|kum; kum falı|OSM|R-M-L|
remmal|n|ar|rammāl|kum falcısı|OSM|R-M-L|
müneccim|n|ar|munaccim|yıldız bilgini|EAT||
uğur|n|tr|ugur|fırsat; talih|DLT|*uğur|
uğurlu|adj|tr|ugurlug|talihli|DLT|*uğur|
uğursuz|adj|tr|ugursuz|talihsiz|OSM|*uğur|
şom|adj|ar|şuʾm|uğursuz|EAT|Ş-A-M|
meşum|adj|ar|maşʾūm|uğursuz|OSM|Ş-A-M|
baht|n|fa|baḫt|talih|EAT|baḫt|
bahtiyar|adj|fa|baḫtiyār|talihli|EAT|baḫt|
bedbaht|adj|fa|bad-baḫt|talihsiz|EAT|baḫt|
felek|n|ar|falak|gök küresi; kader|EAT||
şans|n|fr|chance|düşüş; talih|OSM19||la:cadentia>fr:chance>tr:şans
kasem|n|ar|qasam|ant|OSM|K-S-M|
hortlak|n|tr|hortla-|mezardan çıkan ölü|OSM|*hortla-|
hortlamak|v|tr|hortla-|mezardan çıkmak|OSM|*hortla-|
öcü|n|tr|öcü|korkutucu hayali yaratık|OSM||
umacı|n|tr?|umacı|korkutucu hayali yaratık|OSM||
gulyabani|n|fa|ġūl-i biyābānī|çöl gulyabanisi|OSM||ar:ġūl>fa:ġūl-i biyābānī>tr:gulyabani
karakoncolos|n|el|kalikántzaros|kış cini|OSM||
alkarısı|n|tr|al karı|lohusa cini|OSM||
vampir|n|fr|vampire|kan emici hortlak|OSM19||sr:vampir>fr:vampire>tr:vampir
zombi|n|fr|zombie|dirilmiş ceset|MOD||
Şahmeran|prop|fa|şāh-i mārān|yılanların şahı|OSM|şāh|
anka|n|ar|ʿanqāʾ|uzun boyunlu; masal kuşu|EAT||
Zümrüdüanka|prop|fa|sīmurġ-i ʿanqā|masal kuşu|OSM||
Simurg|prop|fa|sīmurġ|otuz kuş; masal kuşu|OSM||
hüma|n|fa|humā|devlet kuşu|EAT||
ongun|n|mn|ongğon|totem; kutsal hayvan|DD||
şamanizm|n|fr|chamanisme|şamanlık|CUM||
totem|n|fr|totem|kabile simgesi|CUM||
totemizm|n|fr|totémisme|totem inancı|CUM||
tabu|n|fr|tabou|yasak, dokunulmaz|CUM||
fetiş|n|fr|fétiche|büyülü nesne|CUM|facere|la:facticius>pt:feitiço>fr:fétiche>tr:fetiş
animizm|n|fr|animisme|canlıcılık|CUM||
pagan|n|fr|païen|köylü; çok tanrılı|CUM|pagus|la:paganus>fr:païen>tr:pagan
paganizm|n|fr|paganisme|çok tanrıcılık|CUM|pagus|
mit|n|fr|mythe|söylence|CUM|mythos|grc:mŷthos>fr:mythe>tr:mit
mitoloji|n|fr|mythologie|söylence bilimi|OSM19|mythos|
mitos|n|el|mŷthos|söz, söylence|MOD|mythos|
mitolojik|adj|fr|mythologique|söylencesel|CUM|mythos|
# --- Hristiyanlık ------------------------------------------------------------------------------
Hristiyan|n|el|khristianós|Mesih'e bağlı|EAT||
Katolik|n|fr|catholique|evrensel|OSM19||grc:katholikós>la:catholicus>fr:catholique>tr:Katolik
Protestan|n|fr|protestant|karşı çıkan|OSM19||la:protestans>fr:protestant>tr:Protestan
nasrani|n|ar|naṣrānī|Nasıralı; Hristiyan|EAT|N-S-R|
nusret|n|ar|nuṣra|yardım, zafer|EAT|N-S-R|
ensar|n|ar|anṣār|yardımcılar|EAT|N-S-R|
mansur|adj|ar|manṣūr|yardım görmüş; zafer kazanmış|OSM|N-S-R|
haçlı|n|tr|haç|haç taşıyan|OSM19||
istavroz|n|el|stavrós|haç|OSM||
çarmıh|n|fa|çār-mīḫ|dört çivi|EAT||
vaftiz|n|el|báptisis|suya daldırma|OSM||
Noel|prop|fr|Noël|doğum|OSM19||la:natalis>fr:Noël>tr:Noel
paskalya|n|el|paskhaliá|Paskalya|OSM||he:pesaḥ>grc:páskha>el:paskhaliá>tr:paskalya
yortu|n|el|giortí|bayram|EAT||
katedral|n|fr|cathédrale|piskoposluk kilisesi|OSM19||grc:kathédra>la:cathedralis>fr:cathédrale>tr:katedral
bazilika|n|it|basilica|kral yapısı|CUM||grc:basilikḗ>la:basilica>it:basilica>tr:bazilika
şapel|n|fr|chapelle|küçük kilise|CUM||la:capella>fr:chapelle>tr:şapel
papa|n|it|papa|baba; Roma piskoposu|EAT|páppas|grc:páppas>la:papa>it:papa>tr:papa
papalık|n|tr|papa|papa makamı|OSM19|páppas|
kardinal|n|fr|cardinal|ana, temel|OSM19||la:cardinalis>fr:cardinal>tr:kardinal
başpiskopos|n|tr|baş|üst piskopos|OSM19|skopein|
metropolit|n|el|mētropolítēs|ana kent piskoposu|OSM|polis|
diyakoz|n|el|diákonos|hizmetçi; kilise görevlisi|OSM||
peder|n|fa|pidar|baba; papaz|OSM||
misyonerlik|n|tr|misyoner|din yayıcılığı|OSM19|mittere|
ortodoksluk|n|tr|ortodoks|Ortodoks mezhebi|OSM19|orthos|
ikon|n|fr|icône|kutsal resim; simge|MOD||grc:eikṓn>fr:icône>tr:ikon
Gregoryen|n|fr|grégorien|Aziz Gregor'a bağlı|OSM19||
Süryani|n|ar|suryānī|Suriyeli; Doğu Hristiyanı|EAT||
Kıpti|n|ar|qibṭī|Mısırlı Hristiyan|OSM||grc:Aigýptios>ar:qibṭī>tr:Kıpti
# --- Yahudilik ---------------------------------------------------------------------------------
Yahudi|n|ar|yahūdī|Yahuda soyundan|EAT||he:yəhūdī>ar:yahūdī>tr:Yahudi
Musevi|n|ar|mūsawī|Musa'ya bağlı|OSM||
İbrani|n|ar|ʿibrānī|öte yakalı; İbrani|OSM||he:ʿivrī>ar:ʿibrānī>tr:İbrani
haham|n|he|ḥākhām|bilge|OSM||
hahambaşı|n|tr|haham|hahamların başı|OSM||
Zebur|prop|ar|zabūr|yazılı kitap|EAT||
koşer|adj|en|kosher|uygun|NEW||he:kāşēr>en:kosher>tr:koşer
# --- Diğer dinler ve felsefe ---------------------------------------------------------------------
Mecusi|n|ar|macūsī|Zerdüşt rahibi|EAT||fa:maguş>ar:macūsī>tr:Mecusi
Zerdüşt|prop|fa|zartuşt|İranlı peygamber|OSM||
Buda|prop|fr|Bouddha|uyanmış|OSM19||sa:buddha>fr:Bouddha>tr:Buda
Budist|n|fr|bouddhiste|Buda'ya bağlı|CUM||
Budizm|n|fr|bouddhisme|Buda öğretisi|CUM||
Hindu|n|fr|hindou|Hint dinli|CUM||fa:hindū>fr:hindou>tr:Hindu
Brahman|n|fr|brahmane|Hint rahibi|CUM||sa:brāhmaṇa>fr:brahmane>tr:Brahman
nirvana|n|fr|nirvana|sönme|CUM||sa:nirvāṇa>fr:nirvana>tr:nirvana
karma|n|fr|karma|eylem|MOD||sa:karman>fr:karma>tr:karma
yoga|n|fr|yoga|birleşme, boyunduruk|MOD||sa:yoga>fr:yoga>tr:yoga
lama|n|fr|lama|Tibet rahibi|CUM||
ateist|n|fr|athée|tanrısız|CUM|theos|grc:átheos>fr:athée>tr:ateist
ateizm|n|fr|athéisme|tanrıtanımazlık|CUM|theos|
teoloji|n|fr|théologie|tanrı bilimi|OSM19|theos|grc:theología>fr:théologie>tr:teoloji
teizm|n|fr|théisme|tanrıcılık|CUM|theos|
panteizm|n|fr|panthéisme|tümtanrıcılık|CUM|theos|
monoteizm|n|fr|monothéisme|tektanrıcılık|CUM|theos|
politeizm|n|fr|polythéisme|çoktanrıcılık|CUM|theos|
deizm|n|fr|déisme|yaradancılık|CUM|deus|la:deus>fr:déisme>tr:deizm
deist|n|fr|déiste|yaradancı|CUM|deus|
agnostik|n|fr|agnostique|bilinemezci|MOD|gnōsis|grc:ágnōstos>fr:agnostique>tr:agnostik
agnostisizm|n|fr|agnosticisme|bilinemezcilik|MOD|gnōsis|
laik|adj|fr|laïque|halktan|CUM|laos|grc:laïkós>fr:laïque>tr:laik
laisizm|n|fr|laïcisme|laiklik|CUM|laos|
dogma|n|fr|dogme|kanı, öğreti|CUM|dokein|grc:dógma>fr:dogme>tr:dogma
dogmatik|adj|fr|dogmatique|inakçı|CUM|dokein|
paradoks|n|fr|paradoxe|kanıya aykırı|CUM|dokein|grc:parádoxos>fr:paradoxe>tr:paradoks
doktrin|n|fr|doctrine|öğreti|CUM|docere|la:doctrina>fr:doctrine>tr:doktrin
doküman|n|fr|document|öğretici belge|CUM|docere|la:documentum>fr:document>tr:doküman
sekülerizm|n|fr|sécularisme|dünyevilik|MOD||la:saecularis>fr:sécularisme>tr:sekülerizm
dünyevi|adj|ar|dunyawī|dünyaya ilişkin|OSM||
uhrevi|adj|ar|uḫrawī|ahirete ilişkin|OSM|A-H-R|
cismani|adj|ar|cismānī|bedene ilişkin|OSM||
kulluk|n|tr|kul|kul olma|DLT||
bende|n|fa|banda|kul, köle|EAT||
düzah|n|fa|dūzaḫ|cehennem|EAT||
behişt|n|fa|bihişt|cennet|EAT||
gönüllü|adj|tr|gönül|isteyerek yapan|OSM||
tütsülemek|v|tr|tütsü|tütsü yakmak|OSM|*tüt-|
Hızır|prop|ar|ḫaḍir|yeşil; ölümsüz veli|EAT|H-D-R|
hıdrellez|n|tr|Hızır-İlyas|Hızır ile İlyas günü|OSM|H-D-R|
Mehdi|prop|ar|mahdī|doğru yola iletilmiş|EAT|H-D-Y|
deccal|n|ar|daccāl|aldatıcı|EAT||
tufan|n|ar|ṭūfān|büyük sel|EAT||
kıssa|n|ar|qiṣṣa|anlatı|EAT||
ibret|n|ar|ʿibra|ders alınacak şey|EAT||
mütevazi|adj|ar|mutawāḍiʿ|alçakgönüllü|OSM|W-D-A|
ibadetli|adj|tr|ibadet|ibadete düşkün|OSM|A-B-D|
hacılık|n|tr|hacı|hacı olma|OSM|H-C-C|
imamlık|n|tr|imam|imam görevi|OSM|A-M-M|
müezzinlik|n|tr|müezzin|müezzin görevi|OSM|A-Z-N|
şeyhlik|n|tr|şeyh|şeyh makamı|OSM|Ş-Y-H|
dervişlik|n|tr|derviş|derviş olma|OSM||
hocalık|n|tr|hoca|hoca görevi|OSM||
evliyalık|n|tr|evliya|ermişlik|OSM|W-L-Y|
sofuluk|n|tr|sofu|aşırı dindarlık|OSM|S-W-F|
cennetmekân|adj|fa|cannat-makān|yeri cennet olan|OSM|C-N-N|
"""

FAMILIES = r"""
*ada-|tr|adamak, ayırmak|Eski Türkçe ata-/ada- "ad vermek, ayırmak"; adamak, adak (adanan şey) ve adanmak aynı kökten gelir.
*alka-|tr|övmek, dua etmek|Dîvânu Lugâti't-Türk'teki alka- "övmek, hayır dua etmek"; alkış (eski anlamı dua, övgü) ve alkışlamak aynı kökten türer.
*er-|tr|ulaşmak, olgunlaşmak|Orhun Yazıtları'ndaki er- "ulaşmak"; ermek, erişmek ve ermiş (Hakk'a ulaşmış, veli) aynı kökten gelir.
*göm-|tr|gömmek|Eski Türkçe köm- "gömmek"; gömü (gömülü hazine) ve Dil Devrimi türetmesi gömüt (mezar) aynı kökten türer.
*hortla-|tr|mezardan çıkmak|Anadolu Türkçesinde hort- yansıma kökünden hortlamak; hortlak (mezardan çıkan ölü) aynı kökten gelir.
*ilen-|tr|beddua etmek|Eski Anadolu Türkçesindeki ilen- "beddua etmek"; ilenmek ve ilenç (beddua) aynı kökten türer.
*karga-|tr|lanet etmek|Eski Türkçe karga- "lanetlemek"; kargımak ve kargış (beddua, ilenç) aynı kökten gelir; alkış-kargış ikilisi Dîvânu Lugâti't-Türk'te geçer.
*sap-|tr|yoldan ayrılmak|Eski Türkçe sap- "yoldan çıkmak"; sapmak, sapık, sapkın (dinden sapan) ve sapak aynı kökten türer.
*tap-|tr|hizmet etmek, tapınmak|Orhun Yazıtları'ndaki tap- "hizmet etmek"; tapmak, tapınmak, Dil Devrimi türetmeleri tapınak ve tapıncak aynı kökten gelir.
*uğur|tr|fırsat, talih|Dîvânu Lugâti't-Türk'teki ugur "fırsat, zaman, uğur"; uğurlu, uğursuz ve uğurlamak aynı kökten türer.
*yakar-|tr|yalvarmak|Eski Anadolu Türkçesindeki yakar- "yalvararak istemek"; yakarmak, yakarış ve yakarı (dua) aynı kökten gelir.
-gede|fa|ev, yer|Farsça kade "ev" ikinci öğesi; ateşgede (ateş tapınağı), meykede (meyhane) ve butkede (puthane) bu öğeyle kurulmuştur.
-hān|fa|okuyan|Farsça ḫʷāndan "okumak" fiilinden -ḫʷān; mevlithan, ayinhan ve gazelhan aynı öğeyle türetilmiştir.
-keş|fa|çeken|Farsça kaşīdan "çekmek" fiilinden -keş; çilekeş, cefakeş, esrarkeş, afyonkeş ve serkeş (baş çeken) aynı öğeyle kurulur.
-nişīn|fa|oturan|Farsça nişastan "oturmak" fiilinden -nişīn; postnişin (posta oturan şeyh), şehnişin (cumba) ve hanenişin aynı öğeyle yapılmıştır.
-perest|fa|tapan|Farsça parastīdan "tapmak" fiilinden -perest; putperest, ateşperest, hayalperest, menfaatperest ve şekilperest aynı öğeyle kurulur.
-zen|fa|vuran, çalan|Farsça zadan "vurmak" fiilinden -zen; neyzen, kudümzen ve semazen (sema vuran) aynı öğeyle türetilmiştir.
-şinās|fa|tanıyan, bilen|Farsça şināḫtan "tanımak" fiilinden -şinās; kadirşinas (değer bilen) ve hakşinas (hak bilen) aynı öğeyle kurulur.
A-C-R|ar|karşılık, ücret|Arapça ʾ-c-r kökü; ecir (sevap karşılığı), icar (kiralama), müstecir (kiracı) ve ücret aynı kökten gelir.
A-C-Z|ar|güçsüz olmak|Arapça ʿ-c-z kökü; aciz, acz, mucize (aciz bırakan), icaz, taciz ve darülaceze aynı kökten türer.
A-D-Y|ar|yerine getirmek|Arapça ʾ-d-y kökü; eda (yerine getirme) ve tediye (ödeme) aynı kökten gelir.
A-F-F|ar|iffetli olmak|Arapça ʿ-f-f kökü; iffet ve afif (iffetli) aynı kökten türer.
A-F-W|ar|bağışlamak|Arapça ʿ-f-w kökü; af, muaf (bağışlanmış) ve muafiyet aynı kökten gelir.
A-H-R|ar|son olmak, gecikmek|Arapça ʾ-ḫ-r kökü; ahir (son), ahiret, uhrevi, tehir (erteleme), müteahhir ve teehhür aynı kökten türer.
A-H-W|ar|kardeş|Arapça ʾ-ḫ-w kökü; ihvan (kardeşler), ahi (kardeşim; esnaf birliği üyesi), ahilik ve uhuvvet aynı kökten gelir.
A-L-H|ar|tanrı|Arapça ʾ-l-h kökü; Allah, ilah, ilahe, ilahi, ilahiyat, uluhiyet, vallahi ve billahi aynı kökten türer.
A-L-W|ar|yüce olmak|Arapça ʿ-l-w kökü; âli, ulvi, teali, alicenap ve Ali adından alevi aynı kökten gelir.
A-S-L|ar|kök, temel|Arapça ʾ-ṣ-l kökü; asıl, asil (köklü) ve asalet aynı kökten türer.
A-S-Y|ar|baş kaldırmak|Arapça ʿ-ṣ-y kökü; isyan ve asi aynı kökten gelir.
A-W-D|ar|dönmek, alışmak|Arapça ʿ-w-d kökü; iade, avdet (dönüş), mutat (alışılmış), itiyat ve adet aynı kökten türer.
A-Z-B|ar|azap çektirmek|Arapça ʿ-ḏ-b kökü; azap ve muazzep aynı kökten gelir.
A-Z-Z|ar|güçlü, değerli olmak|Arapça ʿ-z-z kökü; aziz, azize, izzet, muazzez ve taziz aynı kökten türer.
B-D-A|ar|yeni ortaya koymak|Arapça b-d-ʿ kökü; bidat (sonradan çıkan), ibda (yoktan yaratma) ve bedii aynı kökten gelir.
B-D-L|ar|değiştirmek|Arapça b-d-l kökü; bedel, abdal (bedeller; gezgin derviş), tebdil ve mübadele aynı kökten türer.
B-H-T|ar|şaşırtmak|Arapça b-h-t kökü; bühtan (kara çalma) ve mebhut (şaşkın) aynı kökten gelir.
B-L-Ğ|ar|ulaşmak, ulaştırmak|Arapça b-l-ġ kökü; tebliğ, baliğ, beliğ, belagat ve mübalağa aynı kökten türer.
B-T-L|ar|boş, geçersiz olmak|Arapça b-ṭ-l kökü; batıl, iptal ve battal (hükümsüz; kocaman) aynı kökten gelir.
C-B-R|ar|zorlamak|Arapça c-b-r kökü; cebir, cebbar, icbar, cebren ve mecbur aynı kökten türer.
C-L-W|ar|açığa çıkmak, parlamak|Arapça c-l-w kökü; tecelli, celi (açık), cila, cilve ve mütecelli aynı kökten gelir.
C-N-B|ar|yan, uzak|Arapça c-n-b kökü; cenup (güney), canip (taraf), ecnebi (yabancı), ictinap ve cenabet aynı kökten türer.
C-Z-B|ar|çekmek|Arapça c-ḏ-b kökü; cezbe, cazibe, cazip, meczup ve incizap aynı kökten gelir.
D-Y-N|ar|din; borç|Arapça d-y-n kökü; din, diyanet, mütedeyyin ve medyun (borçlu) aynı kökten türer.
F-H-Ş|ar|aşırı, edepsiz olmak|Arapça f-ḥ-ş kökü; fuhuş, fahişe ve fahiş (aşırı) aynı kökten gelir.
F-N-Y|ar|yok olmak|Arapça f-n-y kökü; fena (yok oluş), fani (geçici) ve fenafillah aynı kökten türer.
F-R-D|ar|buyurmak, varsaymak|Arapça f-r-ḍ kökü; farz, farize, faraza, faraziye ve mefruz aynı kökten gelir.
F-R-Y|ar|uydurmak|Arapça f-r-y kökü; iftira ve müfteri aynı kökten türer.
F-S-D|ar|bozulmak|Arapça f-s-d kökü; fesat, fasit, müfsit ve ifsat aynı kökten gelir.
F-S-K|ar|yoldan çıkmak|Arapça f-s-q kökü; fasık ve fısk aynı kökten türer.
F-T-N|ar|sınamak, ayartmak|Arapça f-t-n kökü; fitne, fettan ve meftun aynı kökten gelir.
F-Y-D|ar|taşmak|Arapça f-y-ḍ kökü; feyiz, feyyaz ve faiz (taşan, fazla) aynı kökten türer.
H-B-B|ar|sevmek|Arapça ḥ-b-b kökü; habib, mahbup, muhip, muhabbet ve müstehap aynı kökten gelir.
H-C-R|ar|göç etmek, ayrılmak|Arapça h-c-r kökü; hicret, muhacir, hicri ve hücre aynı kökten türer.
H-D-R|ar|hazır olmak; yeşil|Arapça ḥ-ḍ-r kökü; hazret (huzur), ihzar, muhzır, hazır, huzur ve ḫaḍir "yeşil" anlamıyla Hızır aynı kökten gelir.
H-D-S|ar|yeni olmak, olmak|Arapça ḥ-d-ṯ kökü; hadis (söz), hadise (olay), muhaddis, ihdas ve hudus aynı kökten türer.
H-L-F|ar|ardından gelmek|Arapça ḫ-l-f kökü; halife, hilafet, halef, muhalif ve ihtilaf aynı kökten gelir.
H-L-M|ar|yumuşak huylu olmak|Arapça ḥ-l-m kökü; halim ve hilim aynı kökten türer.
H-L-S|ar|arı, katışıksız olmak|Arapça ḫ-l-ṣ kökü; ihlas, halis, muhlis, halas, tahlis ve hülasa aynı kökten gelir.
H-M-D|ar|övmek|Arapça ḥ-m-d kökü; hamt, hamdele, tahmit ve Muhammed (övülmüş) aynı kökten gelir.
H-R-S|ar|aşırı istemek|Arapça ḥ-r-ṣ kökü; hırs ve haris aynı kökten türer.
H-Y-B|ar|korku ile saygı|Arapça h-y-b kökü; heybet ve mehabet aynı kökten gelir.
H-Ş-A|ar|boyun eğmek|Arapça ḫ-ş-ʿ kökü; huşu ve haşyet aynı kökten türer.
H-Ş-M|ar|görkem; utanma|Arapça ḥ-ş-m kökü; haşmet ve muhteşem aynı kökten gelir.
H-Ş-N|ar|sert olmak|Arapça ḫ-ş-n kökü; haşin ve huşunet aynı kökten türer.
H-Ş-R|ar|toplamak|Arapça ḥ-ş-r kökü; mahşer (toplanma yeri) ve haşir (diriliş) aynı kökten gelir.
K-A-D|ar|oturmak|Arapça q-ʿ-d kökü; kuud (oturma), kaide (temel, kural) ve zilkade aynı kökten türer.
K-B-L|ar|kabul etmek, karşılamak|Arapça q-b-l kökü; kabul, kıble, kabil, mukabil, mukabele, istikbal, makbul, ikbal ve tekabül aynı kökten gelir.
K-D-S|ar|kutsal olmak|Arapça q-d-s kökü; mukaddes, takdis, kutsi, kuddüs, kutsiyet ve Kudüs aynı kökten türer.
K-F-N|ar|örtmek|Arapça k-f-n kökü; kefen ve tekfin aynı kökten gelir.
K-H-N|ar|gelecekten haber vermek|Arapça k-h-n kökü; kâhin ve kehanet aynı kökten türer.
K-H-R|ar|ezmek, kahretmek|Arapça q-h-r kökü; kahır, kahhar ve makhur aynı kökten gelir.
K-N-A|ar|yetinmek, inanmak|Arapça q-n-ʿ kökü; kanaat, kani ve ikna aynı kökten türer.
K-R-A|ar|okumak|Arapça q-r-ʾ kökü; Kuran (okunan), kıraat, kari ve mukri aynı kökten gelir.
K-R-H|ar|hoşlanmamak|Arapça k-r-h kökü; mekruh, kerih, kerahet ve ikrah aynı kökten türer.
K-Z-B|ar|yalan söylemek|Arapça k-ḏ-b kökü; tekzip (yalanlama) ve kâzip (yalancı) aynı kökten gelir.
L-A-N|ar|lanet etmek|Arapça l-ʿ-n kökü; lanet ve melun aynı kökten türer.
L-H-D|ar|sapmak; mezar oyuğu|Arapça l-ḥ-d kökü; lahit (mezar oyuğu), mülhit (dinden sapan) ve ilhat aynı kökten gelir.
L-H-M|ar|içe doğurmak|Arapça l-h-m kökü; ilham ve mülhem aynı kökten türer.
L-T-F|ar|ince, nazik olmak|Arapça l-ṭ-f kökü; lütuf, latif, latife, iltifat ve mültefit aynı kökten gelir.
L-W-M|ar|kınamak|Arapça l-w-m kökü; melamet (kınanma) ve melami (kınanmayı seçen derviş) aynı kökten türer.
M-N-N|ar|iyilik etmek|Arapça m-n-n kökü; minnet, memnun, imtinan ve mennan aynı kökten gelir.
M-S-H|ar|sıvazlamak, yağ sürmek|Arapça m-s-ḥ kökü; mesh (abdestte sıvazlama) ve Mesih (yağla kutsanmış) aynı kökten türer.
M-S-K|ar|tutmak|Arapça m-s-k kökü; imsak (tutma) ve mümsik (eli sıkı) aynı kökten gelir.
M-T-N|ar|sağlam olmak|Arapça m-t-n kökü; metin (sağlam) ve metanet aynı kökten türer.
M-W-T|ar|ölmek|Arapça m-w-t kökü; mevt, mevta, memat ve meyyit aynı kökten gelir.
N-A-M|ar|nimet vermek|Arapça n-ʿ-m kökü; nimet, inam, naim ve münim aynı kökten türer.
N-B-A|ar|haber vermek|Arapça n-b-ʾ kökü; nebi, nübüvvet ve enbiya aynı kökten gelir.
N-C-S|ar|pis olmak|Arapça n-c-s kökü; necis ve necaset aynı kökten türer.
N-C-W|ar|kurtulmak; fısıldamak|Arapça n-c-w kökü; necat (kurtuluş) ve münacat (Tanrı'ya yakarış) aynı kökten gelir.
N-F-K|ar|harcamak; ikiyüzlülük|Arapça n-f-q kökü; nafaka, infak, nifak ve münafık aynı kökten türer.
N-F-L|ar|fazladan olan|Arapça n-f-l kökü; nafile (fazladan ibadet) ve enfal (ganimetler) aynı kökten gelir.
N-K-B|ar|delmek, seçmek|Arapça n-q-b kökü; nakip (başkan), nikap (yüz örtüsü) ve menkıbe aynı kökten türer.
N-S-F|ar|yarı; hakkaniyet|Arapça n-ṣ-f kökü; nısıf (yarı), insaf ve munsif aynı kökten gelir.
N-S-H|ar|kopya etmek|Arapça n-s-ḫ kökü; nüsha, muska (nüsha'dan), istinsah ve tenasüh aynı kökten türer.
N-S-R|ar|yardım etmek|Arapça n-ṣ-r kökü; nusret, ensar, mansur ve Nasıra adıyla nasrani aynı kökten gelir.
R-B-B|ar|rab, efendi|Arapça r-b-b kökü; rab, rabbani ve rububiyet aynı kökten türer.
R-B-T|ar|bağlamak|Arapça r-b-ṭ kökü; rabıta, irtibat, merbut ve murabıt aynı kökten gelir.
R-D-D|ar|geri çevirmek|Arapça r-d-d kökü; ret, reddetmek, merdut, mürtet, irtidat ve tereddüt aynı kökten türer.
R-D-Y|ar|hoşnut olmak|Arapça r-ḍ-y kökü; rıza, razı ve rıdvan aynı kökten gelir.
R-H-B|ar|korkmak; rahip olmak|Arapça r-h-b kökü; rahip, rahibe, ruhban ve ruhbaniyet aynı kökten türer.
R-H-L|ar|göçmek|Arapça r-ḥ-l kökü; rahle, irtihal, merhale ve rihlet aynı kökten gelir.
R-K-B|ar|gözetlemek|Arapça r-q-b kökü; murakabe, mürakıp, rakip ve rekabet aynı kökten türer.
R-M-L|ar|kum|Arapça r-m-l kökü; remil (kum falı) ve remmal aynı kökten gelir.
R-S-L|ar|göndermek|Arapça r-s-l kökü; resul, risalet, risale, irsal ve mürsel aynı kökten türer.
R-Z-K|ar|rızık vermek|Arapça r-z-q kökü; rızık, rezzak, erzak ve merzuk aynı kökten gelir.
R-Z-L|ar|alçak olmak|Arapça r-ḏ-l kökü; rezil ve rezalet aynı kökten türer.
R-Ş-D|ar|doğru yolu bulmak|Arapça r-ş-d kökü; mürşit, irşat, reşit ve rüşt aynı kökten gelir.
S-B-H|ar|yüceltmek|Arapça s-b-ḥ kökü; tespih, tesbihat, sübhan ve sübhanallah aynı kökten türer.
S-H-B|ar|arkadaşlık etmek|Arapça ṣ-ḥ-b kökü; sahabe, ashap, musahip, sahip ve sohbet aynı kökten gelir.
S-H-F|ar|sayfa|Arapça ṣ-ḥ-f kökü; mushaf, sahife, suhuf, sahaf ve sayfa aynı kökten türer.
S-H-W|ar|cömert olmak|Arapça s-ḫ-w kökü; sahi ve sahavet aynı kökten gelir.
S-L-F|ar|önce gelmek|Arapça s-l-f kökü; selef (öncekiler) ve selefi aynı kökten türer.
S-L-W|ar|namaz kılmak|Arapça ṣ-l-w kökü; salat, salavat, musalla ve musalli aynı kökten gelir.
S-M-A|ar|işitmek|Arapça s-m-ʿ kökü; sema, semah, istima, sami ve semai aynı kökten türer.
S-N-N|ar|yol, âdet|Arapça s-n-n kökü; sünnet, sünni ve mesnun aynı kökten gelir.
S-R-R|ar|giz; sevinç|Arapça s-r-r kökü; sır, esrar, sürur ve mesrur aynı kökten türer.
S-T-R|ar|örtmek|Arapça s-t-r kökü; settar, tesettür ve mestur aynı kökten gelir.
S-W-M|ar|oruç tutmak|Arapça ṣ-w-m kökü; savm (oruç) ve saim (oruçlu) aynı kökten türer.
T-H-R|ar|temiz olmak|Arapça ṭ-h-r kökü; taharet, tahir, tathir ve mutahhar aynı kökten gelir.
T-W-A|ar|boyun eğmek|Arapça ṭ-w-ʿ kökü; itaat, muti ve istitaat aynı kökten türer.
T-W-B|ar|dönmek, tövbe etmek|Arapça t-w-b kökü; tövbe ve tevvab aynı kökten gelir.
W-C-B|ar|gerekli olmak|Arapça w-c-b kökü; vacip, vücup, icap, mucip ve vecibe aynı kökten türer.
W-D-A|ar|koymak; alçalmak|Arapça w-ḍ-ʿ kökü; vaz, mevzu, mevzi, vaziyet, tevazu ve mütevazi aynı kökten gelir.
W-F-Y|ar|tam olmak, yerine getirmek|Arapça w-f-y kökü; vefa, vefat, vafi, ifa ve istifa aynı kökten türer.
W-K-F|ar|durdurmak|Arapça w-q-f kökü; vakıf, vakfe, vakfiye, evkaf, mevkuf ve tevkif aynı kökten gelir.
W-K-R|ar|ağırbaşlı olmak|Arapça w-q-r kökü; vakar ve vakur aynı kökten türer.
W-K-Y|ar|korumak, sakınmak|Arapça w-q-y kökü; takva ve müttaki aynı kökten gelir.
W-L-D|ar|doğmak|Arapça w-l-d kökü; velet, evlat, mevlit, mevlüt, veladet, tevellüt, milat ve miladi aynı kökten türer.
W-R-D|ar|gelmek, varmak|Arapça w-r-d kökü; vird, evrat, vürut ve varit aynı kökten gelir.
W-T-R|ar|tek olmak; ardışık gelmek|Arapça w-t-r kökü; vitir (tek rekâtlı namaz), tevatür ve mütevatir aynı kökten türer.
Z-H-B|ar|gitmek|Arapça ḏ-h-b kökü; mezhep (gidilen yol) ve zehap (sanı) aynı kökten gelir.
Z-H-D|ar|dünyadan el çekmek|Arapça z-h-d kökü; zühd ve zahit aynı kökten türer.
Z-M-M|ar|kınamak; koruma altına almak|Arapça ḏ-m-m kökü; zem, mezmum, zimmet ve zımmi aynı kökten gelir.
Z-N-Y|ar|zina etmek|Arapça z-n-y kökü; zina ve zani aynı kökten türer.
Z-W-Y|ar|köşeye çekilmek|Arapça z-w-y kökü; zaviye (köşe; küçük tekke), münzevi ve inziva aynı kökten gelir.
afsūn|fa|büyü|Farsça afsūn "büyü, sihir"; efsun, füsun ve efsunlu aynı kökten türer.
baḫt|fa|talih|Farsça baḫt "talih"; baht, bahtiyar (talihli) ve bedbaht (talihsiz) aynı kökten gelir.
deus|la|tanrı|Latince deus "tanrı"; deizm ve deist aynı kökten türer; Yunanca theós ile Hint-Avrupa akrabasıdır.
docere|la|öğretmek|Latince docere "öğretmek"; doktrin (öğreti), doküman (öğretici belge) ve doçent aynı kökten gelir.
dokein|el|sanmak, görünmek|Eski Yunanca dokeîn "sanmak"; dogma, dogmatik, paradoks ve ortodoks aynı kökten türer.
gnōsis|el|bilgi|Eski Yunanca gnôsis "bilgi"; agnostik ve agnostisizm aynı kökten gelir.
laos|el|halk|Eski Yunanca laós "halk"; laik (halktan olan, din adamı olmayan) ve laisizm aynı kökten türer.
mythos|el|söz, söylence|Eski Yunanca mŷthos "söz, öykü"; mit, mitos, mitoloji ve mitolojik aynı kökten gelir.
nā-|fa|olumsuzluk öneki|Farsça nā- "-sız, olmayan" öneki; namert, namahrem, nahoş, naçar ve naçiz bu önekle kurulmuştur.
pagus|la|köy, kır|Latince pagus "köy"; paganus "köylü; Hristiyan olmayan" sözünden pagan ve paganizm türer.
páppas|el|baba|Eski Yunanca páppas "baba"; papa, papalık ve papaz aynı kökten gelir.
theos|el|tanrı|Eski Yunanca theós "tanrı"; ateist, ateizm, teoloji, teizm, panteizm, monoteizm ve politeizm aynı kökten türer.
Ğ-D-R|ar|sözünden dönmek|Arapça ġ-d-r kökü; gaddar ve gadir (haksızlık) aynı kökten gelir.
Ğ-F-R|ar|örtmek, bağışlamak|Arapça ġ-f-r kökü; mağfiret, gufran, istiğfar, gaffar, gafur ve estağfurullah aynı kökten türer.
Ğ-S-L|ar|yıkamak|Arapça ġ-s-l kökü; gusül, gasil ve gassal aynı kökten gelir.
Ğ-Y-B|ar|gizli olmak|Arapça ġ-y-b kökü; gayb, gaip, gıybet ve kayıp aynı kökten türer.
Ğ-Y-R|ar|başka olmak, değişmek|Arapça ġ-y-r kökü; gayri, mugayir ve tagayyür aynı kökten gelir.
Ş-A-M|ar|uğursuz olmak|Arapça ş-ʾ-m kökü; şom ve meşum aynı kökten türer.
Ş-F-A|ar|aracı olmak|Arapça ş-f-ʿ kökü; şefaat ve şefi aynı kökten gelir.
Ş-F-K|ar|şefkat duymak|Arapça ş-f-q kökü; şefkat, müşfik ve şefik aynı kökten türer.
Ş-R-F|ar|yüce, soylu olmak|Arapça ş-r-f kökü; şeref, şerif, eşraf, müşerref, teşrif ve şerefe aynı kökten gelir.
Ş-R-R|ar|kötülük|Arapça ş-r-r kökü; şer ve şerir aynı kökten türer.
Ş-Y-A|ar|yayılmak; taraftar|Arapça ş-y-ʿ kökü; şia, şii ve şayi aynı kökten gelir.
Ş-Y-H|ar|yaşlı, önder|Arapça ş-y-ḫ kökü; şeyh, şeyhlik, şeyhülislam ve meşihat aynı kökten türer.
"""

COGNATES = r"""@namaz into_turkish
  fa نماز [namāz] ; namaz
  ur نماز [namāz] ; namaz
  az namaz ; namaz
  uz namoz ; namaz
  kk намаз [namaz] ; namaz
  ky намаз [namaz] ; namaz
  tk namaz ; namaz
  sq namaz ; namaz
  sr намаз [namaz] ; namaz
  bg намаз [namaz] ; namaz
  mk намаз [namaz] ; namaz
@ibadet shared_ancestor
  ar عبادة [ʿibāda] ; kulluk, tapınma
  fa عبادت [ebādat] ; ibadet
  ur عبادت [ibādat] ; ibadet
  az ibadət ; ibadet
  uz ibodat ; ibadet
  kk ғибадат [ğibadat] ; ibadet
  ky ибадат [ibadat] ; ibadet
  tk ybadat ; ibadet
  sq ibadet ; ibadet
  sr ибадет [ibadet] ; ibadet
@oruç into_turkish
  fa روزه [rūze] ; oruç
  ur روزہ [roza] ; oruç
  az oruc ; oruç
  uz roʻza ; oruç
  kk ораза [oraza] ; oruç
  ky орозо [orozo] ; oruç
  tk oraza ; oruç
@zekât shared_ancestor
  ar زكاة [zakāt] ; arınma; zekât
  fa زکات [zakāt] ; zekât
  ur زکوٰۃ [zakāt] ; zekât
  az zəkat ; zekât
  uz zakot ; zekât
  kk зекет [zeket] ; zekât
  ky зекет [zeket] ; zekât
  tk zekat ; zekât
  sq zeqat ; zekât
  sr зекат [zekat] ; zekât
@hac shared_ancestor
  ar حج [ḥacc] ; hac
  fa حج [hacc] ; hac
  ur حج [hajj] ; hac
  az həcc ; hac
  uz haj ; hac
  kk қажылық [qajılıq] ; hac
  ky ажылык [acılık] ; hac
  tk haj ; hac
  sq haxh ; hac
  sr хаџ [hadž] ; hac
  bg хадж [hadž] ; hac
  en hajj ; hac
@abdest into_turkish
  fa آبدست [ābdast] ; el suyu; abdest
  az dəstəmaz ; abdest ; ff:Azerbaycan Türkçesinde aynı kavram "dest-i namaz" (namaz eli) bileşiğiyle karşılanır
  kk дәрет [däret] ; abdest ; ff:Kazakça abdest için Arapça taharet'ten gelen däret sözünü kullanır
  ky даарат [daarat] ; abdest ; ff:Kırgızca taharet kökenli daarat sözünü kullanır
  sq abdes ; abdest
  sr абдест [abdest] ; abdest
  bg абдест [abdest] ; abdest
  mk абдест [abdest] ; abdest
@kıble shared_ancestor
  ar قبلة [qibla] ; yönelinen yön
  fa قبله [qeble] ; kıble
  ur قبلہ [qibla] ; kıble
  az qiblə ; kıble
  uz qibla ; kıble
  kk құбыла [qubıla] ; kıble
  ky кыбыла [kıbıla] ; kıble
  tk kybla ; kıble
  sq kible ; kıble
  sr кибла [kibla] ; kıble
  en qibla ; kıble
@ezan shared_ancestor
  ar أذان [aḏān] ; duyuru; ezan
  fa اذان [azān] ; ezan
  ur اذان [azān] ; ezan
  az azan ; ezan
  uz azon ; ezan
  kk азан [azan] ; ezan
  ky азан [azan] ; ezan
  tk azan ; ezan
  sq ezan ; ezan
  sr езан [ezan] ; ezan
  bg езан [ezan] ; ezan
  mk езан [ezan] ; ezan
@imam shared_ancestor
  ar إمام [imām] ; önder; imam
  fa امام [emām] ; imam
  ur امام [imām] ; imam
  az imam ; imam
  uz imom ; imam
  kk имам [imam] ; imam
  ky имам [imam] ; imam
  tk ymam ; imam
  sq imam ; imam
  sr имам [imam] ; imam
  bg имам [imam] ; imam
  el ιμάμης [imámis] ; imam
  en imam ; imam
  fr imam ; imam
  es imán ; imam ; ff:İspanyolca imán aynı zamanda Fransızca aimant'tan gelen "mıknatıs" sözcüğüyle eş seslidir
@müezzin shared_ancestor
  ar مؤذن [muʾaḏḏin] ; ezan okuyan
  fa مؤذن [moʾazzen] ; müezzin
  ur مؤذن [muʾazzin] ; müezzin
  az müəzzin ; müezzin
  uz muazzin ; müezzin
  sq myezin ; müezzin
  sr мујезин [mujezin] ; müezzin
  bg мюезин [myuezin] ; müezzin
  el μουεζίνης [mouezínis] ; müezzin
  en muezzin ; müezzin
  fr muezzin ; müezzin
  it muezzin ; müezzin
@hutbe shared_ancestor
  ar خطبة [ḫuṭba] ; söylev; hutbe
  fa خطبه [ḫotbe] ; hutbe
  ur خطبہ [khutba] ; hutbe
  az xütbə ; hutbe
  uz xutba ; hutbe
  kk құтпа [qutpa] ; hutbe
  ky кутпа [kutpa] ; hutbe
  sq hutbe ; hutbe
  sr хутба [hutba] ; hutbe
@fetva shared_ancestor
  ar فتوى [fatwā] ; dinî görüş
  fa فتوا [fatvā] ; fetva
  ur فتویٰ [fatwā] ; fetva
  az fətva ; fetva
  uz fatvo ; fetva
  kk пәтуа [pätwa] ; fetva; karar ; ff:Kazakçada pätwa "uzlaşı, karar" anlamına da genişlemiştir
  sq fetva ; fetva
  sr фетва [fetva] ; fetva
  en fatwa ; fetva
  fr fatwa ; fetva
  de Fatwa ; fetva
  es fetua ; fetva
@müftü shared_ancestor
  ar مفتي [muftī] ; fetva veren
  fa مفتی [moftī] ; müftü
  az müfti ; müftü
  uz mufti ; müftü
  kk мүфти [müfti] ; müftü
  sq myfti ; müftü
  sr муфтија [muftija] ; müftü
  bg мюфтия [myuftiya] ; müftü
  mk муфтија [muftija] ; müftü
  ro muftiu ; müftü
  en mufti ; müftü; sivil giysi ; ff:İngilizcede "in mufti" deyimi üniforma dışı sivil kıyafet anlamına gelir
  hu mufti ; müftü
@hadis shared_ancestor
  ar حديث [ḥadīṯ] ; söz; hadis
  fa حدیث [hadīs] ; hadis
  ur حدیث [hadīs] ; hadis
  az hədis ; hadis
  uz hadis ; hadis
  kk хадис [hadis] ; hadis
  ky хадис [hadis] ; hadis
  sq hadith ; hadis
  sr хадис [hadis] ; hadis
  en hadith ; hadis
@sünnet shared_ancestor
  ar سنة [sunna] ; yol, âdet
  fa سنت [sonnat] ; sünnet; gelenek
  ur سنت [sunnat] ; sünnet
  az sünnət ; sünnet
  uz sunnat ; sünnet
  kk сүндет [sündet] ; sünnet (erkek çocuk) ; ff:Kazakçada sündet öncelikle erkek çocuğun sünnet edilmesini anlatır
  ky сүннөт [sünnöt] ; sünnet
  tk sünnet ; sünnet
  sq synet ; erkek çocuk sünneti ; ff:Arnavutçada synet yalnızca sünnet töreni anlamındadır
  sr сунет [sunet] ; erkek çocuk sünneti ; ff:Boşnakça ve Sırpçada sunet yalnızca sünnet ameliyesini anlatır
  bg сюнет [syunet] ; erkek çocuk sünneti ; ff:Bulgarcada da yalnızca sünnet töreni anlamı yaşar
  mk сунет [sunet] ; sünnet töreni
  en sunnah ; sünnet
@farz shared_ancestor
  ar فرض [farḍ] ; buyruk; varsayım
  fa فرض [farz] ; varsayım; farz ; ff:Farsçada farz öncelikle "varsayım" demektir
  ur فرض [farz] ; farz; görev
  az fərz ; farz
  uz farz ; farz
  kk парыз [parız] ; farz; borç, görev
  ky парз [parz] ; farz; görev
  tk parz ; farz
  sq farz ; farz
  sr фарз [farz] ; farz
@haram shared_ancestor
  ar حرام [ḥarām] ; yasak
  fa حرام [harām] ; haram
  ur حرام [harām] ; haram
  az haram ; haram
  uz harom ; haram
  kk арам [aram] ; haram; pis, kirli ; ff:Kazakçada aram "haram" yanında "pis, kötü niyetli" anlamına da gelir
  ky арам [aram] ; haram; kirli
  tk haram ; haram
  sq haram ; haram
  sr харам [haram] ; haram
  bg харам [haram] ; haksız kazanç; yazık ; ff:Bulgarcada haram "haksız yere alınan şey; boşa giden" anlamına kaymıştır
  mk арам [aram] ; haram; boşa giden
  ro haram ; haksız kazanç; değersiz hayvan ; ff:Rumencede haram "çalıntı mal" ve "yaramaz, bakımsız hayvan" anlamlarına kaymıştır
  en haram ; haram
@helal shared_ancestor
  ar حلال [ḥalāl] ; izinli
  fa حلال [halāl] ; helal
  ur حلال [halāl] ; helal
  az halal ; helal
  uz halol ; helal
  kk адал [adal] ; dürüst, sadık ; ff:Kazakçada adal "dürüst, sadık, içten" anlamına kaymış, dinî "helal" anlamı ikincildir
  ky адал [adal] ; dürüst; helal ; ff:Kırgızcada adal "dürüst, temiz" anlamı önde gelir
  tk halal ; helal
  sq hallall ; helal
  sr халал [halal] ; helal
  bg халал [halal] ; helal olsun ; ff:Bulgarcada "халал да му е" (helal olsun) deyiminde yaşar
  mk алал [alal] ; helal
  en halal ; helal
  fr halal ; helal
  de halal ; helal
@sevap shared_ancestor
  ar ثواب [ṯawāb] ; karşılık, ödül
  fa ثواب [savāb] ; sevap
  ur ثواب [sawāb] ; sevap
  az savab ; sevap
  uz savob ; sevap
  kk сауап [sawap] ; sevap
  ky сооп [soop] ; sevap
  tk sogap ; sevap
  sq sevap ; sevap
  sr севап [sevap] ; sevap; iyilik
  bg севап [sevap] ; iyilik, sevap
  mk севап [sevap] ; sevap
@günah into_turkish
  fa گناه [gonāh] ; günah
  ur گناہ [gunāh] ; günah
  az günah ; günah
  uz gunoh ; günah
  kk күнә [künä] ; günah
  ky күнөө [künöö] ; günah
  tk günä ; günah
  sq gjynah ; günah; yazık ; ff:Arnavutçada gjynah "yazık, günah" ünlemi olarak da kullanılır
  bg гюнах [gyunah] ; günah
@tövbe shared_ancestor
  ar توبة [tawba] ; dönüş; tövbe
  fa توبه [towbe] ; tövbe
  ur توبہ [tauba] ; tövbe; aman! ; ff:Urducada "tauba tauba" şaşkınlık ve kınama ünlemi olarak da kullanılır
  az tövbə ; tövbe
  uz tavba ; tövbe
  kk тәубе [täwbe] ; tövbe; şükür ; ff:Kazakçada täwbe "şükür, hamd" anlamında da kullanılır
  ky тобо [tobo] ; tövbe; şükür
  tk toba ; tövbe
  sq tobe ; tövbe
  sr тоба [toba] ; tövbe
@cehennem shared_ancestor
  ar جهنم [cahannam] ; cehennem
  fa جهنم [jahannam] ; cehennem
  ur جہنم [jahannam] ; cehennem
  az cəhənnəm ; cehennem
  uz jahannam ; cehennem
  kk жаһаннам [jahannam] ; cehennem
  tk jähennem ; cehennem
  sq xhehenem ; cehennem
  sr џехенем [džehenem] ; cehennem
  bg джендем [džendem] ; cehennem; ücra yer ; ff:Bulgarcada džendem "çok uzak, ıssız yer" anlamında da kullanılır
  he גיהנום [gehinnom] ; cehennem ; ff:İbranice Ge Hinnom (Hinnom Vadisi) adından; Arapça cahannam da buradan gelir
  el γέεννα [géenna] ; cehennem
@şeytan shared_ancestor
  ar شيطان [şayṭān] ; şeytan
  fa شیطان [şeytān] ; şeytan; yaramaz ; ff:Farsçada şeytān çocuklar için "yaramaz, afacan" anlamında da kullanılır
  ur شیطان [şaitān] ; şeytan
  az şeytan ; şeytan
  uz shayton ; şeytan
  kk шайтан [şaytan] ; şeytan
  ky шайтан [şaytan] ; şeytan
  tk şeýtan ; şeytan
  sq shejtan ; şeytan
  sr шејтан [šejtan] ; şeytan
  bg шейтан [šeytan] ; şeytan; kurnaz kişi
  mk шејтан [šejtan] ; şeytan
  he שָׂטָן [satan] ; düşman; şeytan
  en Satan ; şeytan
  el Σατανάς [Satanás] ; şeytan
  ru сатана [satana] ; şeytan
  hu sátán ; şeytan
@melek shared_ancestor
  ar ملك [malak] ; melek
  fa ملک [malak] ; melek ; ff:Farsçada melek için daha çok firişte kullanılır
  az mələk ; melek
  sq melek ; melek
  sr мелек [melek] ; melek
  he מַלְאָךְ [malʾakh] ; elçi; melek
@peygamber into_turkish
  fa پیغمبر [peyğāmbar] ; haber getiren; peygamber
  ur پیغمبر [paighambar] ; peygamber
  az peyğəmbər ; peygamber
  uz paygʻambar ; peygamber
  kk пайғамбар [payğambar] ; peygamber
  ky пайгамбар [paygambar] ; peygamber
  tk pygamber ; peygamber
  sq pejgamber ; peygamber
  sr пејгамбер [pejgamber] ; peygamber
  mk пејгамбер [pejgamber] ; peygamber
@dua shared_ancestor
  ar دعاء [duʿāʾ] ; çağrı; dua
  fa دعا [doʿā] ; dua
  ur دعا [duā] ; dua
  az dua ; dua
  uz duo ; dua
  kk дұға [duğa] ; dua
  ky дуба [duba] ; dua
  tk doga ; dua
  sq dua ; dua
  sr дова [dova] ; dua
  mk дова [dova] ; dua
@tespih shared_ancestor
  ar تسبيح [tasbīḥ] ; Allah'ı yüceltme
  fa تسبیح [tasbīh] ; tespih
  ur تسبیح [tasbīh] ; tespih
  az təsbeh ; tespih
  uz tasbeh ; tespih
  kk тәспі [täspi] ; tespih
  ky теспе [tespe] ; tespih
  tk tesbi ; tespih
  sq tespih ; tespih
  sr тесбих [tesbih] ; tespih
@seccade shared_ancestor
  ar سجادة [saccāda] ; namaz halısı
  fa سجاده [saccāde] ; seccade
  az səccadə ; seccade
  sq sexhade ; seccade
  sr серџада [serdžada] ; seccade
@minare shared_ancestor
  ar منارة [manāra] ; ışık yeri; fener kulesi
  fa مناره [manāre] ; minare
  az minarə ; minare
  uz minora ; minare
  kk мұнара [munara] ; kule ; ff:Kazakçada munara her türlü kuleyi anlatır
  ky мунара [munara] ; kule
  tk minara ; minare
  sq minare ; minare
  sr минарет [minaret] ; minare
  bg минаре [minare] ; minare
  mk минаре [minare] ; minare
  el μιναρές [minarés] ; minare
  en minaret ; minare
  fr minaret ; minare
  it minareto ; minare
  de Minarett ; minare
  ru минарет [minaret] ; minare
  hu minaret ; minare
  ro minaret ; minare
@cami shared_ancestor
  ar جامع [cāmiʿ] ; toplayan; büyük mescit
  fa جامع [jāmeʿ] ; cuma camisi
  sq xhami ; cami
  sr џамија [džamija] ; cami
  bg джамия [džamiya] ; cami
  mk џамија [džamija] ; cami
  el τζαμί [tzamí] ; cami
  ro geamie ; cami
  hu dzsámi ; cami
@mescit shared_ancestor
  ar مسجد [mascid] ; secde yeri
  fa مسجد [masjed] ; cami
  ur مسجد [masjid] ; cami
  az məscid ; cami
  uz masjid ; cami
  kk мешіт [meşit] ; cami
  ky мечит [meçit] ; cami
  tk metjit ; cami
  sq mesxhid ; mescit
  es mezquita ; cami
  it moschea ; cami
  fr mosquée ; cami
  en mosque ; cami
@medrese shared_ancestor
  ar مدرسة [madrasa] ; okul ; ff:Arapçada madrasa her türlü okulu anlatır
  fa مدرسه [madrese] ; okul ; ff:Farsçada da madrese genel olarak "okul" demektir
  ur مدرسہ [madrasa] ; okul; medrese
  az mədrəsə ; medrese
  uz madrasa ; medrese
  kk медресе [medrese] ; medrese
  ky медресе [medrese] ; medrese
  tk medrese ; medrese
  sq medrese ; medrese
  sr медреса [medresa] ; medrese
  bg медресе [medrese] ; medrese
  mk медреса [medresa] ; medrese
  en madrasa ; medrese
  ru медресе [medrese] ; medrese
@türbe shared_ancestor
  ar تربة [turba] ; toprak; mezar ; ff:Arapçada turba öncelikle "toprak" demektir
  az türbə ; türbe
  sq tyrbe ; türbe
  sr турбе [turbe] ; türbe
  bg тюрбе [tyurbe] ; türbe
  mk турбе [turbe] ; türbe
  hu türbe ; türbe
@tekke shared_ancestor
  ar تكية [takiyya] ; tekke
  fa تکیه [tekye] ; dayanak; matem toplantı yeri ; ff:Farsçada tekye "dayanma" ve İran'da "taziye toplantı yeri" anlamındadır
  az təkkə ; tekke
  sq teqe ; tekke
  sr текија [tekija] ; tekke
  bg теке [teke] ; tekke
  mk теќе [teḱe] ; tekke
  el τεκές [tekés] ; tekke; uyuşturucu içilen yer ; ff:Yunancada tekés "esrar içilen gizli yer" anlamına kaymıştır
@derviş into_turkish
  fa درویش [darvīş] ; yoksul; derviş
  ur درویش [darvīş] ; derviş
  az dərviş ; derviş
  uz darvesh ; derviş
  kk дәруіш [däruiş] ; derviş
  ky дервиш [derviş] ; derviş
  tk derwüş ; derviş
  sq dervish ; derviş
  sr дервиш [derviš] ; derviş
  bg дервиш [derviš] ; derviş
  mk дервиш [derviš] ; derviş
  el δερβίσης [dervísis] ; derviş
  en dervish ; derviş
  fr derviche ; derviş
  it derviscio ; derviş
  de Derwisch ; derviş
  ru дервиш [derviš] ; derviş
  hu dervis ; derviş
  ro derviş ; derviş
@şeyh shared_ancestor
  ar شيخ [şayḫ] ; yaşlı; kabile reisi ; ff:Arapçada şayḫ öncelikle "yaşlı, ihtiyar; kabile başkanı" demektir
  fa شیخ [şeyḫ] ; şeyh
  ur شیخ [şaikh] ; şeyh; soy adı
  az şeyx ; şeyh
  uz shayx ; şeyh
  kk шейх [şeyh] ; şeyh
  tk şyh ; şeyh
  sq shejh ; şeyh
  sr шејх [šejh] ; şeyh
  bg шейх [šeyh] ; şeyh
  en sheikh ; şeyh; Arap emiri
  fr cheikh ; şeyh
  es jeque ; şeyh
  it sceicco ; şeyh
  de Scheich ; şeyh
  ru шейх [šeyh] ; şeyh
@mürit shared_ancestor
  ar مريد [murīd] ; isteyen; mürit
  fa مرید [morīd] ; mürit
  ur مرید [murīd] ; mürit
  az mürid ; mürit
  uz murid ; mürit
  kk мүрит [mürit] ; mürit
  sq myrid ; mürit
  sr мурид [murid] ; mürit
  ru мюрид [myurid] ; mürit
  en murid ; mürit
@mürşit shared_ancestor
  ar مرشد [murşid] ; yol gösteren; rehber ; ff:Arapçada murşid günlük dilde "tur rehberi" anlamına da gelir
  fa مرشد [morşed] ; mürşit
  ur مرشد [murşid] ; mürşit
  az mürşid ; mürşit
  uz murshid ; mürşit
  sq murshid ; mürşit
  sr муршид [muršid] ; mürşit
@tarikat shared_ancestor
  ar طريقة [ṭarīqa] ; yol; yöntem ; ff:Arapçada ṭarīqa öncelikle "yöntem, yol" demektir
  fa طریقت [tarīqat] ; tarikat
  ur طریقت [tarīqat] ; tarikat
  az təriqət ; tarikat
  uz tariqat ; tarikat
  sq tarikat ; tarikat
  sr тарикат [tarikat] ; tarikat
  bg тарикат [tarikat] ; kurnaz, açıkgöz kişi ; ff:Bulgarcada tarikat "uyanık, kurnaz adam" anlamına tümüyle kaymıştır
  mk тарикат [tarikat] ; tarikat; kurnaz kişi
@tasavvuf shared_ancestor
  ar تصوف [taṣawwuf] ; tasavvuf
  fa تصوف [tasavvof] ; tasavvuf
  ur تصوف [tasavvuf] ; tasavvuf
  az təsəvvüf ; tasavvuf
  uz tasavvuf ; tasavvuf
  sq tasavvuf ; tasavvuf
  sr тесавуф [tesavuf] ; tasavvuf
@sofu shared_ancestor
  ar صوفي [ṣūfī] ; yün giyen; sufi
  fa صوفی [sūfī] ; sufi
  ur صوفی [sūfī] ; sufi
  az sufi ; sufi
  uz soʻfi ; sufi; müezzin ; ff:Özbekçede soʻfi köy camilerinde "müezzin" anlamına da gelir
  kk сопы [sopı] ; sofu; yobaz ; ff:Kazakçada sopı "aşırı dindar, yobaz" çağrışımı taşır
  ky сопу [sopu] ; sofu; dindar
  tk sopy ; sofu
  sq sufi ; sufi
  sr суфија [sufija] ; sufi
  en Sufi ; sufi
  fr soufi ; sufi
  ru суфий [sufiy] ; sufi
@sema shared_ancestor
  ar سماع [samāʿ] ; işitme; dinleme ; ff:Arapçada samāʿ öncelikle "işitme, dinleme" demektir
  fa سماع [samāʿ] ; sema; zikir dansı
  ur سماع [samāʿ] ; dinî müzik dinleme; sema
  az səma ; sema
  uz samo ; sema
  en sema ; sema
@pir into_turkish
  fa پیر [pīr] ; yaşlı; şeyh ; ff:Farsçada pīr öncelikle "yaşlı, ihtiyar" demektir
  ur پیر [pīr] ; şeyh; Pazartesi ; ff:Urducada pīr aynı zamanda haftanın günü "Pazartesi" anlamına gelir
  az pir ; pir; ziyaret yeri ; ff:Azerbaycan Türkçesinde pir "ziyaret edilen kutsal yer, türbe" anlamına da gelir
  uz pir ; pir
  kk пір [pir] ; pir
  ky пир [pir] ; pir
  tk pir ; pir
  sq pir ; pir
@keramet shared_ancestor
  ar كرامة [karāma] ; onur, saygınlık ; ff:Arapçada karāma öncelikle "onur, haysiyet" demektir
  fa کرامت [karāmat] ; keramet; cömertlik
  ur کرامت [karāmat] ; keramet
  az kəramət ; keramet
  uz karomat ; keramet
  kk керемет [keremet] ; harika, olağanüstü ; ff:Kazakçada keremet "harika, muhteşem" anlamında sıfat olmuştur
  ky керемет [keremet] ; harika, mucizevi ; ff:Kırgızcada keremet "mucize; harika" anlamındadır
  tk keramat ; keramet
  sq qeramet ; keramet
  sr керамет [keramet] ; keramet
@mucize shared_ancestor
  ar معجزة [muʿciza] ; aciz bırakan şey
  fa معجزه [moʿjeze] ; mucize
  ur معجزہ [muʿjiza] ; mucize
  az möcüzə ; mucize
  uz moʻjiza ; mucize
  kk мұғжиза [muğjiza] ; mucize
  sq muxhize ; mucize
  sr муџиза [mudžiza] ; mucize
@evliya shared_ancestor
  ar أولياء [awliyāʾ] ; veliler; dostlar; vasiler ; ff:Arapçada çoğul olan awliyāʾ Türkçede tekil "ermiş" anlamına kaymıştır
  fa اولیا [owliyā] ; veliler; ebeveyn ; ff:Farsçada owliyā (owliyā-yi dāniş-āmūz) "öğrenci velileri, ebeveyn" anlamında da kullanılır
  az övliya ; evliya
  uz avliyo ; evliya
  kk әулие [äwlie] ; kutsal; ermiş; ziyaret yeri ; ff:Kazakçada äwlie "kutsal yer, türbe" anlamına da gelir
  ky олуя [oluya] ; evliya
  tk öwlüýä ; evliya
  sq evlia ; evliya
  sr евлија [evlija] ; evliya
  mk евлија [evlija] ; evliya
"""
