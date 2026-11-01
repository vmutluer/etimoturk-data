# -*- coding: utf-8 -*-
"""Korpus 2 — Toplum, hukuk, ekonomi, din, eğitim, bilim, teknik ve sanat sözcükleri."""

WORDS = r"""
anayasa|n|tr|ana yasa|temel yasa|DD||
yasama organı|n|tr|yasama|meclis|DD||
yürütme kurulu|n|tr|yürütme|kurul|DD|*yürü-|
başbakan|n|tr|baş bakan|hükümet başkanı|DD|*bak-|
milletvekili|n|ar|milla|mebus|CUM||
mebus|n|ar|mabʿūṯ|gönderilmiş|OSM19||
senato|n|it|senato|yaşlılar kurulu|OSM19||la:senatus>it:senato>tr:senato
parlamento|n|it|parlamento|konuşma yeri|OSM19|parabola|fr:parlement>it:parlamento>tr:parlamento
oy pusulası|n|tr|oy|pusula|DD||
sandık başı|n|ar|ṣandūq|seçim sandığı|CUM||
aday|n|ar|ʿadad?|namzet|DD||
namzet|n|fa|nāmzad|adı anılan|OSM||
kampanya|n|fr|campagne|sefer|CUM||la:campania>fr:campagne>tr:kampanya
propaganda|n|it|propaganda|yayılması gereken|CUM||la:propaganda>it:propaganda>tr:propaganda
parti|n|fr|parti|bölüm, taraf|OSM19||la:partitus>fr:parti>tr:parti
fırka|n|ar|firqa|bölük, parti|OSM19||
cumhurbaşkanı|n|ar|cumhūr|devlet başkanı|CUM|C-M-H|
reis|n|ar|raʾīs|baş|EAT||
reisicumhur|n|ar|raʾīs-i cumhūr|cumhurbaşkanı|CUM||
sefir heyeti|n|ar|safīr|heyet|OSM|S-F-R|
heyet|n|ar|hayʾa|biçim; kurul|EAT|H-Y-A|
elçi|n|tr|élçi|ülke temsilcisi|ORH|*el-|
elçilik|n|tr|élçi|sefaret|OSM|*el-|
konsolos|n|it|console|danışman|OSM19|consulere|la:consul>it:console>tr:konsolos
diplomat|n|fr|diplomate|belge taşıyan|OSM19|diploma|grc:díplōma>fr:diplomate>tr:diplomat
protokol|n|fr|protocole|ilk yapıştırılan yaprak|OSM19|kolla|grc:prōtókollon>fr:protocole>tr:protokol
antlaşma|n|tr|ant|ahit|DD|*ant|
ant|n|tr|and|yemin|ORH|*ant|
yemin|n|ar|yamīn|sağ el; yemin|EAT|Y-M-N|
tüzük|n|tr|tüzük|nizamname|DD|*düz-|
yönerge|n|tr|yönerge|talimat|DD|*yön|
genelge|n|tr|genelge|tamim|DD||
tamim|n|ar|taʿmīm|genelleştirme|OSM19||
belge|n|tr|belge|vesika|DD||
vesika|n|ar|waṯīqa|güvenilir yazı|OSM||
sözleşme|n|tr|sözleşme|mukavele|DD||
kira|n|ar|kirāʾ|kiralama|EAT||
kiracı|n|ar|kirāʾ|kira ödeyen|OSM||
tapu|n|tr|tapu|hizmet; mülk belgesi|OSM||
noter|n|fr|notaire|yazman|OSM19|nota|la:notarius>fr:notaire>tr:noter
dava dilekçesi|n|ar|daʿwā|dilekçe|CUM|D-A-W|
dilekçe|n|tr|tilek|arzuhal|DD||
arzuhal|n|ar|ʿarḏ-i ḥāl|hâl arzı|OSM||
savcı|n|tr|savcı|iddia makamı|DD|*sav|
sav|n|tr|sab|söz, haber|ORH|*sav|
yargıtay|n|tr|yargı|temyiz mahkemesi|DD||
temyiz|n|ar|tamyīz|ayırt etme|OSM19|M-Y-Z|
sanık|n|tr|sanık|itham edilen|DD|*san-|
sanmak|v|tr|sa-n-|zannetmek|DLT|*san-|
tanıklık|n|tr|tanuk|şahitlik|OSM|*tanı-|
delil|n|ar|dalīl|kılavuz; kanıt|EAT|D-L-L|
kanıt|n|tr|kanıt|delil|DD|*kan-|
ispat|n|ar|iṯbāt|sağlamlaştırma|OSM||
hüküm giymek|v|ar|ḥukm|mahkûm olmak|OSM|H-K-M|
hapis|n|ar|ḥabs|alıkoyma|EAT|H-B-S|
zindan|n|fa|zindān|hapishane|EAT||
tutukevi|n|tr|tutuk|hapishane|DD|*tut-|
infaz|n|ar|infāḏ|yerine getirme|OSM|N-F-Z|
af kararı|n|ar|ʿafw|af|OSM||
suçsuz|adj|tr|suç|masum|OSM||
kabahat|n|ar|qabāḥa|çirkinlik; kusur|EAT||
cinayet|n|ar|cināya|suç|EAT|C-N-Y|
katil|n|ar|qātil|öldüren|EAT|K-T-L|
hırsız|n|fa|ḫırs?|çalan|EAT||
hırsızlık|n|fa|ḫırs|çalma|OSM||
dolandırıcı|n|tr|dolandırıcı|hileyle alan|OSM|*dol-|
hile|n|ar|ḥīla|oyun|EAT||
rüşvet|n|ar|rişwa|rüşvet|EAT||
yolsuzluk|n|tr|yolsuzluk|suistimal|DD||
adli tıp|n|ar|ʿadlī|adli tıp|CUM|A-D-L|
vergi dairesi|n|tr|bérgü|maliye|CUM|*ver-|
maliye|n|ar|māliyya|mal işleri|OSM19||
bütçe açığı|n|fr|budget|açık|MOD||
gelir vergisi|n|tr|gelir|vergi|DD|*gel-|
gider kalemi|n|tr|gider|kalem|DD|*git-|
hazine bonosu|n|ar|ḫazīna|bono|MOD||
bono|n|it|buono|iyi; senet|OSM19||la:bonus>it:buono>tr:bono
senet|n|ar|sanad|dayanak|EAT|S-N-D|
tahvil piyasası|n|ar|taḥwīl|piyasa|MOD|H-W-L|
hisse senedi|n|ar|ḥiṣṣa|pay belgesi|OSM19||
sermaye piyasası|n|fa|ser-māye|piyasa|MOD|ser|
yatırımcı|n|tr|yatırım|yatırım yapan|MOD|*yat-|
tasarruf|n|ar|taṣarruf|kullanma; biriktirme|OSM|S-R-F|
birikim|n|tr|birikim|tasarruf|DD||
birikmek|v|tr|birik-|toplanmak|DLT||
döviz|n|fr|devise|parola; yabancı para|CUM||la:divisa>fr:devise>tr:döviz
kur|n|fr|cours|akış; değer|CUM|currere|la:cursus>fr:cours>tr:kur
ihracat|n|ar|iḫrācāt|çıkarmalar|OSM19||
ithalat|n|ar|idḫālāt|sokmalar|OSM19||
gümrük vergisi|n|el|kommérkion|vergi|OSM||
tarife|n|fr|tarif|bildirme|OSM19||ar:taʿrīf>it:tariffa>fr:tarif>tr:tarife
tekel|n|tr|tek el|monopol|DD||
rekabet|n|ar|raqāba|gözetme; yarış|OSM19||
yarış|n|tr|yarış|müsabaka|DLT||
pazarlamak|v|fa|bāzār|satışa sunmak|MOD||
üretici|n|tr|üretici|üreten|DD|*ür-|
tüketici|n|tr|tüketici|tüketen|DD||
tüketmek|v|tr|tüket-|bitirmek|DLT||
girişimci|n|tr|girişim|müteşebbis|DD|*gir-|
müteşebbis|n|ar|muteşebbis|teşebbüs eden|OSM19||
işveren|n|tr|iş veren|patron|DD|*ver-|
sendika|n|fr|syndicat|birlikte yargılayan|CUM||grc:sýndikos>fr:syndicat>tr:sendika
grev|n|fr|grève|kumsal|CUM||fr:grève>tr:grev
emekli|adj|tr|emgek|çalışmayı bırakmış|DD||
emeklilik|n|tr|emgek|emekli olma|DD||
sigortalı|adj|it|sicurtà|sigortası olan|CUM||
poliçe bedeli|n|it|polizza|bedel|CUM||
banka hesabı|n|it|banca|hesap|CUM|H-S-B|
çek|n|en|cheque|denetim|OSM19||fa:çek>en:cheque>fr:chèque>tr:çek
kredi kartı|n|fr|crédit|kart|MOD||
kart|n|fr|carte|kâğıt|OSM19||grc:khártēs>la:charta>fr:carte>tr:kart
cami avlusu|n|ar|cāmiʿ|avlu|OSM|C-M-A|
mihrap nişi|n|ar|miḥrāb|niş|OSM||
kubbe|n|ar|qubba|kubbe|EAT|K-B-B|
kemer|n|fa|kamar|kavis|EAT||
sütun|n|fa|ustūn|direk|EAT||
direk|n|tr|tirek|dayak|DLT||
şerefe|n|ar|şurfa|balkon|EAT||
vaaz|n|ar|waʿẕ|öğüt|EAT||
vaiz|n|ar|wāʿiẕ|öğüt veren|EAT||
hutbe|n|ar|ḫuṭba|konuşma|EAT|H-T-B|
ilahi|n|ar|ilāhī|Tanrı'ya ait|EAT||
ayet|n|ar|āya|işaret|EAT||
sure|n|ar|sūra|bölüm|EAT||
hadis|n|ar|ḥadīṯ|söz|EAT||
sünnet|n|ar|sunna|yol, gelenek|EAT||
farz|n|ar|farḏ|zorunlu|EAT||
helal|adj|ar|ḥalāl|izinli|EAT|H-L-L|
haram|adj|ar|ḥarām|yasak|EAT|H-R-M|
mekruh|adj|ar|makrūh|hoş görülmeyen|EAT||
abdesthane|n|fa|āb-dest-ḫāne|tuvalet|OSM|-hāne|
seccade kilimi|n|ar|saccāda|kilim|OSM|S-C-D|
tespih|n|ar|tasbīḥ|anma|EAT||
Ramazan|n|ar|ramaḏān|kavurucu ay|EAT||
sahur|n|ar|saḥūr|seher yemeği|EAT||
seher|n|ar|saḥar|şafak öncesi|EAT||
kandil gecesi|n|ar|qindīl|gece|OSM||
mevlit|n|ar|mawlid|doğum|EAT||
hatim|n|ar|ḫatm|bitirme|EAT||
Kur'an|n|ar|qurʾān|okuma|EAT||
İncil|n|ar|incīl|müjde|EAT||grc:euangélion>ar:incīl>tr:İncil
Tevrat|n|ar|tawrā|öğreti|EAT||he:tōrā>ar:tawrā>tr:Tevrat
havra|n|ar|ḥāra|mahalle; sinagog|OSM||
sinagog|n|fr|synagogue|toplanma|CUM||grc:synagōgḕ>fr:synagogue>tr:sinagog
patrik|n|el|patriárchis|aile başı|EAT|arkhein|grc:patriárkhēs>el:patriárchis>tr:patrik
piskopos|n|el|epískopos|gözetmen|EAT||grc:epískopos>tr:piskopos
rahip|n|ar|rāhib|korkan; keşiş|EAT||
rahibe|n|ar|rāhiba|kadın keşiş|EAT||
ikona|n|el|eikóna|görüntü|OSM||grc:eikṑn>el:eikóna>tr:ikona
ayin|n|fa|āyīn|tören|EAT||
tören|n|tr|törün|merasim|DD||
cenaze|n|ar|canāza|tabut|EAT||
tabut|n|ar|tābūt|sandık|EAT||
mezarlık|n|ar|mazār|kabristan|OSM||
kabristan|n|fa|qabr-istān|mezarlık|EAT|-istān|
ders programı|n|ar|dars|program|CUM|D-R-S|
ders kitabı|n|ar|dars|kitap|CUM|D-R-S|
ödev defteri|n|tr|ödev|defter|CUM||
sınıf öğretmeni|n|ar|ṣinf|öğretmen|CUM|*ög-|
anaokulu|n|tr|ana okul|kreş|DD|*oku-|
kreş|n|fr|crèche|yemlik|CUM||fr:crèche>tr:kreş
ilkokul|n|tr|ilk okul|ilköğretim|DD|*oku-|
ortaokul|n|tr|orta okul|orta öğretim|DD|*oku-|
yatılı okul|n|tr|yatılı|yatılı okul|CUM|*yat-|
burs|n|fr|bourse|kese|CUM||la:bursa>fr:bourse>tr:burs
karne|n|fr|carnet|küçük defter|OSM19||fr:carnet>tr:karne
not|n|fr|note|işaret|OSM19|nota|la:nota>fr:note>tr:not
sınav kâğıdı|n|tr|sınav|kâğıt|DD||
yazılı|n|tr|yazılı|yazılı sınav|CUM|*yaz-|
sözlü|n|tr|sözlü|sözlü sınav|CUM||
bitirme tezi|n|tr|bitirme|tez|MOD|*bit-|
tez|n|fr|thèse|koyma|OSM19||grc:thésis>fr:thèse>tr:tez
makale yazarı|n|ar|maqāla|yazar|CUM|K-W-L|
dergi|n|tr|dergi|mecmua|DD||
derlemek|v|tr|térle-|toplamak|DLT||
derleme|n|tr|derleme|antoloji|DD||
yayın|n|tr|yayın|neşriyat|DD||
yayınevi|n|tr|yayın evi|neşriyat evi|DD||
basımevi|n|tr|basım|matbaa|DD|*bas-|
kütüphaneci|n|ar|kutub-ḫāne|kütüphane görevlisi|CUM|K-T-B|
raf etiketi|n|ar|raff|etiket|MOD||
ansiklopedi cildi|n|fr|encyclopédie|cilt|CUM|kyklos|
cilt|n|ar|cild|deri; kitap kapağı|EAT||
sayfa numarası|n|ar|ṣaḥīfa|numara|CUM||
dizin|n|tr|dizin|indeks|DD|*diz-|
indeks|n|fr|index|işaret parmağı|CUM||la:index>fr:index>tr:indeks
sözlükçü|n|tr|sözlük|lügatçi|DD||
bilimci|n|tr|bilim|bilim insanı|DD|*bil-|
araştırma|n|tr|araştırma|tetkik|DD||
araştırmak|v|tr|araştır-|incelemek|DLT||
inceleme|n|tr|inceleme|tetkik|DD||
incelemek|v|tr|yinçgele-|tetkik etmek|OSM||
gözlemci|n|tr|gözlem|gözleyen|DD|*kör-|
kuram|n|tr|kuram|teori|DD|*kur-|
teori|n|fr|théorie|bakış|OSM19|theā|grc:theōría>fr:théorie>tr:teori
kuramsal|adj|tr|kuram|teorik|DD||
varsayımsal|adj|tr|varsayım|hipotetik|DD|*var-|
hipotez|n|fr|hypothèse|altına koyma|CUM||grc:hypóthesis>fr:hypothèse>tr:hipotez
kanun|n|ar|qānūn|yasa; kural|EAT|K-N-N|
formül|n|fr|formule|küçük biçim|OSM19||la:formula>fr:formule>tr:formül
denklem|n|tr|denklem|eşitlik|DD||
denk|adj|tr|teŋ|eşit|ORH||
eşit|adj|tr|éş|denk|DD||
oran|n|tr|oran|nispet|DD||
orantı|n|tr|orantı|nispet|DD||
yüzde|n|tr|yüz|yüzde oran|OSM||
kesirli sayı|n|ar|kasr|sayı|CUM|K-S-R|
ondalık|adj|tr|on|ondalık|DD||
toplama|n|tr|toplama|cem|DD||
çıkarma|n|tr|çıkarma|tarh|DD|*çık-|
çarpma|n|tr|çarpma|zarp|DD||
çarpmak|v|tr|çarp-|vurmak|DLT||
bölme işlemi|n|tr|bölme|taksim|DD|*böl-|
üçgen|n|tr|üç gen|üç kenarlı|DD||
kare|n|fr|carré|dörtgen|OSM19||la:quadratus>fr:carré>tr:kare
dikdörtgen|n|tr|dik dörtgen|dikdörtgen|DD|*dik-|
daire alanı|n|ar|dāʾira|alan|DD|D-W-R|
çember|n|fa|çanbar|halka|EAT||
açı|n|tr|açı|zaviye|DD|*aç-|
açıortay|n|tr|açı ortay|açıortay|DD|*aç-|
doğru parçası|n|tr|togru|doğru|DD|*doğ-|
nokta|n|ar|nuqṭa|nokta|EAT||
eğri|adj|tr|egri|eğri|DLT||
eğmek|v|tr|eg-|bükmek|DLT||
hacim|n|ar|ḥacm|büyüklük|OSM||
kütle|n|ar|kutla|yığın|OSM||
ağırlık|n|tr|agırlık|sıklet|DLT||
hız|n|tr|hız|sürat|DD||
sürat|n|ar|surʿa|hız|EAT||
ivme|n|tr|ivme|akselerasyon|DD||
ivmek|v|tr|iv-|acele etmek|DLT||
kuvvet|n|ar|quwwa|güç|EAT||
basınç ölçer|n|tr|basınç|manometre|DD|*bas-|
ısı|n|tr|ısıg|sıcaklık|DLT|*ısı-|
sıcaklık derecesi|n|tr|ısıglık|derece|CUM||
derece|n|ar|daraca|basamak|EAT||
mıknatıs|n|ar|maġnāṭīs|mıknatıs|EAT||grc:magnḕtis>ar:maġnāṭīs>tr:mıknatıs
elektrik akımı|n|fr|électrique|akım|CUM||
akım|n|tr|akım|cereyan|DD||
cereyan|n|ar|carayān|akış|OSM|C-R-Y|
gerilim|n|tr|gerilim|voltaj|DD||
germek|v|tr|ker-|germek|DLT||
direnç|n|tr|direnç|rezistans|DD||
direnmek|v|tr|tiren-|karşı koymak|OSM||
devre kesici|n|ar|dawra|kesici|MOD|D-W-R|
sigorta kutusu|n|it|sicurtà|kutu|MOD||
anten|n|fr|antenne|serene direği|CUM||la:antenna>fr:antenne>tr:anten
dalga|n|tr|talga|dalga|DLT||
dalga boyu|n|tr|talga|dalga boyu|DD||
frekans|n|fr|fréquence|sıklık|CUM||la:frequentia>fr:fréquence>tr:frekans
sıklık|n|tr|sık|frekans|DD||
yayın bandı|n|tr|yayın|bant|MOD||
bant|n|fr|bande|şerit|CUM||fr:bande>tr:bant
hoparlör|n|fr|haut-parleur|yüksek konuşan|CUM||fr:haut-parleur>tr:hoparlör
kulaklık|n|tr|kulkak|kulaklık|CUM||
ekran|n|fr|écran|perde|CUM||fr:écran>tr:ekran
klavye|n|fr|clavier|tuş takımı|MOD||la:clavis>fr:clavier>tr:klavye
fare|n|tr|fare|sıçan; bilgisayar faresi|DLT||
yazıcı|n|tr|yazıcı|printer|MOD|*yaz-|
tarayıcı|n|tr|tarayıcı|scanner|MOD||
taramak|v|tr|tara-|taramak|DLT||
bellek|n|tr|bellek|hafıza|DD|*belle-|
bellemek|v|tr|belle-|öğrenmek|DLT|*belle-|
işlemci|n|tr|işlemci|işlemci|MOD||
yazılımcı|n|tr|yazılım|programcı|MOD|*yaz-|
programcı|n|fr|programme|yazılımcı|MOD|graphein|
kod|n|fr|code|yasa kitabı|CUM||la:codex>fr:code>tr:kod
şifre|n|fr|chiffre|rakam|OSM19||ar:ṣifr>la:cifra>fr:chiffre>tr:şifre
parola|n|it|parola|söz|OSM19|parabola|grc:parabolḕ>la:parabola>it:parola>tr:parola
ağ|n|tr|ag|ağ|DLT||
sunucu|n|tr|sunucu|server|MOD||
veri tabanı|n|tr|veri|database|MOD|*ver-|
dosya yolu|n|fr|dossier|yol|MOD||
e-posta|n|it|posta|elektronik posta|NEW||
ileti|n|tr|ileti|mesaj|DD|*ulaş-|
iletmek|v|tr|ilet-|ulaştırmak|DLT|*ulaş-|
iletişim|n|tr|iletişim|komünikasyon|DD|*ulaş-|
yapay zekâ|n|tr|yapay|zekâ|NEW|*yap-|
zekâ|n|ar|ḏakāʾ|keskin anlayış|EAT||
zeki|adj|ar|ḏakī|akıllı|EAT||
uzman|n|tr|uzman|mütehassıs|DD|*uz|
uzmanlık|n|tr|uzman|ihtisas|DD||
tasarım|n|tr|tasarım|dizayn|DD||
tasarlamak|v|tr|tasarla-|planlamak|OSM||
mimarlık|n|ar|miʿmār|mimarlık|OSM||
heykel|n|ar|haykal|büyük yapı; heykel|OSM||
heykeltıraş|n|ar|haykal-tırāş|heykel yontan|OSM19||
yontu|n|tr|yontu|heykel|DD||
yontmak|v|tr|yon-|biçimlendirmek|DLT||
resim sergisi|n|ar|rasm|sergi|CUM|R-S-M|
sergi|n|tr|sergi|teşhir|DD||
sermek|v|tr|ser-|yaymak|DLT||
tablo|n|fr|tableau|levha|OSM19||la:tabula>fr:tableau>tr:tablo
tuval|n|fr|toile|bez|CUM||la:tela>fr:toile>tr:tuval
palet|n|fr|palette|küçük kürek|CUM||fr:palette>tr:palet
fresk|n|fr|fresque|taze|CUM||it:fresco>fr:fresque>tr:fresk
minyatür|n|fr|miniature|kırmızıyla boyanmış|OSM19||la:miniare>it:miniatura>fr:miniature>tr:minyatür
tezhip|n|ar|taḏhīb|altınlama|EAT||
ebru|n|fa|abrī|bulut gibi|OSM||
çini|n|fa|çīnī|Çin işi|EAT||
seramik|n|fr|céramique|çömlek|CUM||grc:keramikós>fr:céramique>tr:seramik
porselen|n|fr|porcelaine|deniz kabuğu|OSM19||it:porcellana>fr:porcelaine>tr:porselen
vazo|n|it|vaso|kap|OSM19||la:vas>it:vaso>tr:vazo
şiir kitabı|n|ar|şiʿr|kitap|OSM|Ş-A-R|
roman|n|fr|roman|Roma dilinde|OSM19|roma|la:romanice>fr:roman>tr:roman
öykücü|n|tr|öykü|hikâyeci|DD||
oyun yazarı|n|tr|oyun|dramaturg|DD||
sahne|n|ar|ṣaḥn|avlu; sahne|OSM19||
perde arası|n|fa|parde|ara|CUM||
kostüm|n|fr|costume|alışkanlık|CUM||it:costume>fr:costume>tr:kostüm
dekor|n|fr|décor|süs|CUM||la:decorare>fr:décor>tr:dekor
senaryo|n|it|scenario|sahne düzeni|CUM||la:scaena>it:scenario>tr:senaryo
yönetmen|n|tr|yönetmen|rejisör|DD||
rejisör|n|fr|régisseur|yöneten|CUM||la:regere>fr:régisseur>tr:rejisör
oyuncu kadrosu|n|tr|oyunçı|kadro|CUM||
kadro|n|fr|cadre|çerçeve|CUM||it:quadro>fr:cadre>tr:kadro
beste yarışması|n|fa|beste|yarışma|CUM||
nota|n|it|nota|işaret|OSM19|nota|la:nota>it:nota>tr:nota
melodi|n|fr|mélodie|şarkı|CUM|ōidē|grc:melōdía>fr:mélodie>tr:melodi
ritim|n|fr|rythme|akış|CUM||grc:rhythmós>fr:rythme>tr:ritim
usul|n|ar|uṣūl|kökler; yöntem; ritim|EAT||
makam dizisi|n|ar|maqām|dizi|OSM|K-W-M|
koro|n|it|coro|dans alanı|OSM19||grc:khorós>la:chorus>it:coro>tr:koro
solist|n|fr|soliste|tek başına|CUM||it:solista>fr:soliste>tr:solist
flüt|n|fr|flûte|flüt|OSM19||fro:flaüte>fr:flûte>tr:flüt
klarnet|n|fr|clarinette|küçük boru|OSM19|clarus|it:clarinetto>fr:clarinette>tr:klarnet
trompet|n|fr|trompette|küçük boru|OSM19||fr:trompette>tr:trompet
bağlama|n|tr|bagla-|telli çalgı|OSM|*bağ-|
kaval|n|tr|kaval|çoban düdüğü|DLT||
tulum|n|tr|tulum|deri kap; çalgı|DLT||
darbuka|n|ar|darbūka|vurmalı çalgı|OSM||
zil takımı|n|fa|zīl|zil|OSM||
"""
