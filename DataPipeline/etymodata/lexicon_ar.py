# -*- coding: utf-8 -*-
"""Arapça kökenli sözcükler (çoğu Osmanlı Türkçesi yoluyla).
Biçim: lemma|pos|origin|kaynak biçim|kaynak anlam|dönem|kök ailesi|zincir"""

LEXICON_AR = r"""
kitap|n|ar|kitāb|yazılı eser|EAT|K-T-B|
kâtip|n|ar|kātib|yazan, yazıcı|EAT|K-T-B|
mektup|n|ar|maktūb|yazılmış şey|EAT|K-T-B|
mektep|n|ar|maktab|yazı yazılan yer, okul|OSM|K-T-B|
kütüphane|n|ar|kutub-ḫāne|kitaplar evi|OSM|K-T-B|ar:kutub>fa:kutub-ḫāne>ota:kütübhāne>tr:kütüphane
kitabe|n|ar|kitāba|yazıt|OSM|K-T-B|
kitapçı|n|ar|kitāb|kitap satan|OSM|K-T-B|
mektuplaşmak|v|ar|maktūb|mektup yazışmak|TDK|K-T-B|
hekim|n|ar|ḥakīm|bilge, tabip|EAT|H-K-M|
hâkim|n|ar|ḥākim|hükmeden, yargıç|EAT|H-K-M|
hüküm|n|ar|ḥukm|yargı, karar|EAT|H-K-M|
mahkeme|n|ar|maḥkama|yargı yeri|EAT|H-K-M|
hikmet|n|ar|ḥikma|bilgelik|EAT|H-K-M|
muhakeme|n|ar|muḥākama|yargılama|OSM|H-K-M|
hükümet|n|ar|ḥukūma|yönetim|OSM19|H-K-M|
hakem|n|ar|ḥakam|yargıcı, arabulucu|OSM|H-K-M|
tahkim|n|ar|taḥkīm|sağlamlaştırma|OSM|H-K-M|
mahkûm|n|ar|maḥkūm|hükümlü|OSM|H-K-M|
hükümdar|n|ar|ḥukm-dār|hüküm tutan|EAT|dār-|ar:ḥukm>fa:ḥukm-dār>tr:hükümdar
hükmetmek|v|ar|ḥukm|hüküm vermek|EAT|H-K-M|
selam|n|ar|salām|esenlik, barış|EAT|S-L-M|
İslam|n|ar|islām|teslimiyet|EAT|S-L-M|
Müslüman|n|ar|muslim|teslim olan|EAT|S-L-M|ar:muslim>fa:muslimān>tr:Müslüman
teslim|n|ar|taslīm|bırakma, verme|EAT|S-L-M|
selamet|n|ar|salāma|esenlik|EAT|S-L-M|
salim|adj|ar|sālim|sağ, esen|OSM|S-L-M|
selim|adj|ar|salīm|kusursuz, sağlam|OSM|S-L-M|
teslimat|n|ar|taslīmāt|teslimler|OSM19|S-L-M|
selamlamak|v|ar|salām|selam vermek|OSM|S-L-M|
ilim|n|ar|ʿilm|bilgi|EAT|İ-L-M|
âlim|n|ar|ʿālim|bilen, bilgin|EAT|İ-L-M|
muallim|n|ar|muʿallim|öğreten|OSM|İ-L-M|
talim|n|ar|taʿlīm|öğretme, eğitim|OSM|İ-L-M|
malum|adj|ar|maʿlūm|bilinen|EAT|İ-L-M|
âlem|n|ar|ʿālam|dünya, evren|EAT|İ-L-M|
ilmî|adj|ar|ʿilmī|bilimsel|OSM19|İ-L-M|
alamet|n|ar|ʿalāma|işaret|EAT|İ-L-M|
talimat|n|ar|taʿlīmāt|yönergeler|OSM19|İ-L-M|
kelime|n|ar|kalima|söz|EAT|K-L-M|
kelam|n|ar|kalām|konuşma, söz|EAT|K-L-M|
mükâleme|n|ar|mukālama|karşılıklı konuşma|OSM|K-L-M|
akıl|n|ar|ʿaql|bağ, akıl|EAT|A-K-L|
âkil|adj|ar|ʿāqil|akıllı|OSM|A-K-L|
makul|adj|ar|maʿqūl|akla uygun|OSM|A-K-L|
akıllı|adj|ar|ʿaql|akıl sahibi|EAT|A-K-L|
akılcı|adj|ar|ʿaql|rasyonel|DD|A-K-L|
fikir|n|ar|fikr|düşünce|EAT|F-K-R|
tefekkür|n|ar|tafakkur|derin düşünme|EAT|F-K-R|
mütefekkir|n|ar|mutafakkir|düşünür|OSM19|F-K-R|
efkâr|n|ar|afkār|düşünceler; kaygı|OSM|F-K-R|
fikriyat|n|ar|fikriyyāt|düşünce dünyası|OSM19|F-K-R|
kader|n|ar|qadar|ölçülen pay, kısmet|EAT|K-D-R|
kadir|adj|ar|qādir|güçlü, muktedir|EAT|K-D-R|
kudret|n|ar|qudra|güç|EAT|K-D-R|
takdir|n|ar|taqdīr|değer biçme|EAT|K-D-R|
miktar|n|ar|miqdār|ölçü, nicelik|EAT|K-D-R|
mukadder|adj|ar|muqaddar|alın yazısı olan|OSM|K-D-R|
iktidar|n|ar|iqtidār|güç sahibi olma|OSM|K-D-R|
muktedir|adj|ar|muqtadir|gücü yeten|OSM|K-D-R|
hesap|n|ar|ḥisāb|sayma|EAT|H-S-B|
muhasebe|n|ar|muḥāsaba|hesaplaşma|OSM|H-S-B|
muhasebeci|n|ar|muḥāsaba|hesap tutan|OSM19|H-S-B|
hesaplamak|v|ar|ḥisāb|hesap yapmak|OSM|H-S-B|
şükür|n|ar|şukr|teşekkür, minnet|EAT|Ş-K-R|
teşekkür|n|ar|taşakkur|minnet bildirme|EAT|Ş-K-R|
şükran|n|ar|şukrān|minnettarlık|OSM|Ş-K-R|
müteşekkir|adj|ar|mutaşakkir|minnettar|OSM|Ş-K-R|
rahmet|n|ar|raḥma|acıma, bağış|EAT|R-H-M|
merhamet|n|ar|marḥama|acıma|EAT|R-H-M|
rahim|n|ar|raḥim|döl yatağı|EAT|R-H-M|
rahman|n|ar|raḥmān|çok merhametli|EAT|R-H-M|
merhum|adj|ar|marḥūm|rahmetli|OSM|R-H-M|
rahmetli|adj|ar|raḥma|ölmüş|OSM|R-H-M|
mekân|n|ar|makān|yer|EAT|K-W-N|
kâinat|n|ar|kāʾināt|var olanlar|EAT|K-W-N|
imkân|n|ar|imkān|olabilirlik|OSM|K-W-N|
mümkün|adj|ar|mumkin|olabilir|EAT|K-W-N|
kıyam|n|ar|qiyām|ayağa kalkma|EAT|K-W-M|
kıyamet|n|ar|qiyāma|yeniden dirilme|EAT|K-W-M|
makam|n|ar|maqām|durulan yer, mevki|EAT|K-W-M|
mukavemet|n|ar|muqāwama|direnme|OSM|K-W-M|
kavim|n|ar|qawm|topluluk|EAT|K-W-M|
istikamet|n|ar|istiqāma|doğrultu|OSM|K-W-M|
kıymet|n|ar|qīma|değer|EAT|K-W-M|
takvim|n|ar|taqwīm|düzeltme; takvim|OSM|K-W-M|
kaim|adj|ar|qāʾim|ayakta duran|OSM|K-W-M|
amel|n|ar|ʿamal|iş, eylem|EAT|A-M-L|
amele|n|ar|ʿamala|işçiler|OSM19|A-M-L|
muamele|n|ar|muʿāmala|işlem, davranış|EAT|A-M-L|
mamul|n|ar|maʿmūl|yapılmış ürün|OSM|A-M-L|
teamül|n|ar|taʿāmul|alışılmış uygulama|OSM19|A-M-L|
şahit|n|ar|şāhid|tanık|EAT|Ş-H-D|
şehit|n|ar|şahīd|tanık; inanç uğruna ölen|EAT|Ş-H-D|
şehadet|n|ar|şahāda|tanıklık|EAT|Ş-H-D|
müşahede|n|ar|muşāhada|gözlem|OSM|Ş-H-D|
şehitlik|n|ar|şahīd|şehit mezarlığı|OSM|Ş-H-D|
hüsün|n|ar|ḥusn|güzellik|EAT|H-S-N|
ihsan|n|ar|iḥsān|iyilik, bağış|EAT|H-S-N|
tahsin|n|ar|taḥsīn|beğenme|OSM|H-S-N|
muhsin|adj|ar|muḥsin|iyilik eden|OSM|H-S-N|
sefer|n|ar|safar|yolculuk|EAT|S-F-R|
misafir|n|ar|musāfir|yolcu, konuk|EAT|S-F-R|
sefir|n|ar|safīr|elçi|OSM|S-F-R|
sefaret|n|ar|sifāra|elçilik|OSM|S-F-R|
sofra|n|ar|sufra|yol azığı; yemek örtüsü|EAT|S-F-R|
seferberlik|n|fa|safar-bar|savaşa hazırlık|OSM19||
nazar|n|ar|naẕar|bakış|EAT|N-Z-R|
manzara|n|ar|manẕara|bakılan yer|OSM|N-Z-R|
nazır|n|ar|nāẕir|bakan, gözeten|EAT|N-Z-R|
nazariye|n|ar|naẕariyya|kuram|OSM19|N-Z-R|
münazara|n|ar|munāẕara|tartışma|OSM|N-Z-R|
intizar|n|ar|intiẕār|bekleme|OSM|N-Z-R|
nezaret|n|ar|niẕāra|gözetim|OSM|N-Z-R|
zikir|n|ar|ẕikr|anma|EAT|Z-K-R|
tezkere|n|ar|taẕkira|hatırlatma yazısı|OSM|Z-K-R|
müzakere|n|ar|muẕākara|görüşme|OSM|Z-K-R|
mezkûr|adj|ar|maẕkūr|anılan|OSM|Z-K-R|
hatıra|n|ar|ḫāṭira|anı|OSM|H-T-R|
haber|n|ar|ḫabar|bilgi, havadis|EAT|H-B-R|
muhabir|n|ar|muḫabir|haber veren|OSM19|H-B-R|
muhabere|n|ar|muḫābara|haberleşme|OSM|H-B-R|
ihbar|n|ar|iḫbār|haber verme|OSM|H-B-R|
istihbarat|n|ar|istiḫbārāt|haber alma|OSM19|H-B-R|
haberci|n|ar|ḫabar|haber getiren|EAT|H-B-R|
talep|n|ar|ṭalab|istek|EAT|T-L-B|
talebe|n|ar|ṭalaba|isteyenler, öğrenci|OSM|T-L-B|
talip|n|ar|ṭālib|isteyen|EAT|T-L-B|
matlup|n|ar|maṭlūb|istenen|OSM|T-L-B|
ders|n|ar|dars|öğrenim|EAT|D-R-S|
medrese|n|ar|madrasa|ders yeri|EAT|D-R-S|
müderris|n|ar|mudarris|ders veren|EAT|D-R-S|
tedris|n|ar|tadrīs|öğretim|OSM|D-R-S|
tedrisat|n|ar|tadrīsāt|öğretim işleri|OSM19|D-R-S|
dershane|n|ar|dars-ḫāne|ders evi|OSM19|-hāne|ar:dars>fa:dars-ḫāne>tr:dershane
arif|adj|ar|ʿārif|bilen, anlayışlı|EAT|A-R-F|
irfan|n|ar|ʿirfān|bilme, kültür|EAT|A-R-F|
marifet|n|ar|maʿrifa|ustalık, bilgi|EAT|A-R-F|
itiraf|n|ar|iʿtirāf|kabul etme|OSM|A-R-F|
örf|n|ar|ʿurf|gelenek|OSM|A-R-F|
tarif|n|ar|taʿrīf|tanımlama|EAT|A-R-F|
maruf|adj|ar|maʿrūf|bilinen, tanınmış|EAT|A-R-F|
arife|n|ar|ʿarafa|bayram öncesi gün|EAT|A-R-F|
hareket|n|ar|ḥaraka|kımıldama|EAT|H-R-K|
tahrik|n|ar|taḥrīk|harekete geçirme|OSM|H-R-K|
harekât|n|ar|ḥarakāt|askerî hareketler|OSM19|H-R-K|
müteharrik|adj|ar|mutaḥarrik|hareketli|OSM|H-R-K|
vuslat|n|ar|wuṣla|kavuşma|EAT|W-S-L|
vesile|n|ar|wasīla|aracı, sebep|EAT|W-S-L|
vasıl|adj|ar|wāṣil|ulaşan|OSM|W-S-L|
ittisal|n|ar|ittiṣāl|bitişme|OSM|W-S-L|
tabiat|n|ar|ṭabīʿa|yaratılış, doğa|EAT|T-B-A|
tabii|adj|ar|ṭabīʿī|doğal|OSM|T-B-A|
matbaa|n|ar|maṭbaʿa|basımevi|OSM|T-B-A|
matbuat|n|ar|maṭbūʿāt|basın|OSM19|T-B-A|
tabiiyet|n|ar|ṭabīʿiyya|uyrukluk|OSM19|T-B-A|
tıp|n|ar|ṭibb|hekimlik|EAT|T-B-B|
tabip|n|ar|ṭabīb|hekim|EAT|T-B-B|
tababet|n|ar|ṭabāba|hekimlik|OSM|T-B-B|
tıbbi|adj|ar|ṭibbī|tıpla ilgili|OSM19|T-B-B|
adalet|n|ar|ʿadāla|doğruluk, hak|EAT|A-D-L|
adil|adj|ar|ʿādil|doğru, hakkaniyetli|EAT|A-D-L|
adliye|n|ar|ʿadliyya|yargı kurumu|OSM19|A-D-L|
itidal|n|ar|iʿtidāl|ölçülülük|OSM|A-D-L|
muadil|adj|ar|muʿādil|denk|OSM|A-D-L|
tadil|n|ar|taʿdīl|değiştirme|OSM19|A-D-L|
hak|n|ar|ḥaqq|gerçek; hak|EAT|H-K-K|
hakikat|n|ar|ḥaqīqa|gerçeklik|EAT|H-K-K|
hukuk|n|ar|ḥuqūq|haklar|OSM|H-K-K|
hakiki|adj|ar|ḥaqīqī|gerçek|EAT|H-K-K|
tahkik|n|ar|taḥqīq|soruşturma|OSM|H-K-K|
muhakkak|adv|ar|muḥaqqaq|kesinlikle|OSM|H-K-K|
hakkaniyet|n|ar|ḥaqqāniyya|hakka uygunluk|OSM19|H-K-K|
aşk|n|ar|ʿişq|tutkulu sevgi|EAT|A-Ş-K|
âşık|n|ar|ʿāşiq|seven|EAT|A-Ş-K|
maşuk|n|ar|maʿşūq|sevilen|EAT|A-Ş-K|
resim|n|ar|rasm|çizim|EAT|R-S-M|
resmî|adj|ar|rasmī|kayıtlı, devlete ait|OSM|R-S-M|
merasim|n|ar|marāsim|törenler|OSM|R-S-M|
ressam|n|ar|rassām|resim yapan|OSM|R-S-M|
nizam|n|ar|niẕām|düzen|EAT|N-Z-M|
intizam|n|ar|intiẕām|düzenlilik|OSM|N-Z-M|
muntazam|adj|ar|muntaẕam|düzenli|OSM|N-Z-M|
nazım|n|ar|naẕm|şiir düzeni|EAT|N-Z-M|
manzum|adj|ar|manẕūm|dizilmiş, şiir biçiminde|OSM|N-Z-M|
tanzim|n|ar|tanẕīm|düzenleme|OSM|N-Z-M|
Tanzimat|n|ar|tanẕīmāt|düzenlemeler|OSM19|N-Z-M|
hayat|n|ar|ḥayāt|yaşam|EAT|H-Y-Y|
hayvan|n|ar|ḥayawān|canlı|EAT|H-Y-Y|
ihya|n|ar|iḥyāʾ|canlandırma|OSM|H-Y-Y|
hayati|adj|ar|ḥayātī|yaşamsal|OSM19|H-Y-Y|
mülk|n|ar|mulk|sahiplik, ülke|EAT|M-L-K|
melik|n|ar|malik|kral|EAT|M-L-K|
memleket|n|ar|mamlaka|ülke|EAT|M-L-K|
mülkiyet|n|ar|mulkiyya|sahiplik|OSM19|M-L-K|
malik|n|ar|mālik|sahip|EAT|M-L-K|
emlak|n|ar|amlāk|mülkler|OSM|M-L-K|
hür|adj|ar|ḥurr|özgür|EAT|H-R-R|
hürriyet|n|ar|ḥurriyya|özgürlük|OSM19|H-R-R|
tahrir|n|ar|taḥrīr|yazma|OSM|H-R-R|
muharrir|n|ar|muḥarrir|yazar|OSM19|H-R-R|
şirket|n|ar|şirka|ortaklık|OSM|Ş-R-K|
şerik|n|ar|şarīk|ortak|EAT|Ş-R-K|
iştirak|n|ar|iştirāk|katılma|OSM|Ş-R-K|
müşterek|adj|ar|muştarak|ortak|OSM|Ş-R-K|
şirk|n|ar|şirk|ortak koşma|EAT|Ş-R-K|
cami|n|ar|cāmiʿ|toplayan|EAT|C-M-A|
cuma|n|ar|cumʿa|toplanma günü|EAT|C-M-A|
cemaat|n|ar|camāʿa|topluluk|EAT|C-M-A|
cemiyet|n|ar|camʿiyya|dernek, toplum|OSM|C-M-A|
mecmua|n|ar|macmūʿa|derleme, dergi|OSM|C-M-A|
içtima|n|ar|ictimāʿ|toplanma|OSM|C-M-A|
cem|n|ar|camʿ|toplama|EAT|C-M-A|
cümle|n|ar|cumla|bütün; tümce|EAT|C-M-L|
cemal|n|ar|camāl|güzellik|EAT|C-M-L|
cemil|adj|ar|camīl|güzel|EAT|C-M-L|
kalp|n|ar|qalb|dönen şey, yürek|EAT|K-L-B|
kalıp|n|ar|qālib|döküm biçimi|EAT|K-L-B|
inkılap|n|ar|inqilāb|devrim|OSM19|K-L-B|
kavil|n|ar|qawl|söz|EAT|K-W-L|
makale|n|ar|maqāla|söylenen; yazı|OSM19|K-W-L|
mukavele|n|ar|muqāwala|sözleşme|OSM|K-W-L|
vücut|n|ar|wucūd|varlık, beden|EAT|W-C-D|
mevcut|adj|ar|mawcūd|var olan|EAT|W-C-D|
vecd|n|ar|wacd|kendinden geçme|EAT|W-C-D|
vicdan|n|ar|wicdān|iç duygu|OSM|W-C-D|
icat|n|ar|īcād|var etme, buluş|OSM|W-C-D|
nakil|n|ar|naql|taşıma|EAT|N-K-L|
nakliye|n|ar|naqliyya|taşımacılık|OSM19|N-K-L|
nakliyat|n|ar|naqliyyāt|taşıma işleri|OSM19|N-K-L|
menkul|adj|ar|manqūl|taşınabilir|OSM|N-K-L|
intikal|n|ar|intiqāl|geçiş|OSM|N-K-L|
vekil|n|ar|wakīl|yerine iş gören|EAT|W-K-L|
vekâlet|n|ar|wakāla|vekillik|OSM|W-K-L|
tevekkül|n|ar|tawakkul|güvenip bırakma|EAT|W-K-L|
müvekkil|n|ar|muwakkil|vekil tutan|OSM19|W-K-L|
şiir|n|ar|şiʿr|duyulan söz|EAT|Ş-A-R|
şair|n|ar|şāʿir|şiir yazan|EAT|Ş-A-R|
şuur|n|ar|şuʿūr|bilinç|OSM|Ş-A-R|
şöhret|n|ar|şuhra|ün|EAT|Ş-H-R|
meşhur|adj|ar|maşhūr|ünlü|EAT|Ş-H-R|
teşhir|n|ar|taşhīr|sergileme|OSM|Ş-H-R|
fiil|n|ar|fiʿl|eylem|EAT|F-A-L|
fail|n|ar|fāʿil|yapan|EAT|F-A-L|
faal|adj|ar|faʿʿāl|etkin|OSM|F-A-L|
faaliyet|n|ar|faʿʿāliyya|etkinlik|OSM19|F-A-L|
meful|n|ar|mafʿūl|nesne|OSM|F-A-L|
ibadet|n|ar|ʿibāda|kulluk|EAT|A-B-D|
mabet|n|ar|maʿbad|tapınak|OSM|A-B-D|
mabut|n|ar|maʿbūd|tapılan|OSM|A-B-D|
ubudiyet|n|ar|ʿubūdiyya|kulluk|OSM|A-B-D|
kesir|n|ar|kasr|kırık; kesirli sayı|OSM|K-S-R|
kusur|n|ar|quṣūr|eksiklik|EAT|K-S-R|
inkisar|n|ar|inkisār|kırılma, gücenme|OSM|K-S-R|
hafız|n|ar|ḥāfiẕ|ezberleyen|EAT|H-F-Z|
hıfz|n|ar|ḥifẕ|koruma, ezber|EAT|H-F-Z|
muhafaza|n|ar|muḥāfaẕa|koruma|OSM|H-F-Z|
muhafız|n|ar|muḥāfiẕ|koruyucu|OSM|H-F-Z|
mahfuz|adj|ar|maḥfūẕ|korunmuş|OSM|H-F-Z|
hafıza|n|ar|ḥāfiẕa|bellek|OSM|H-F-Z|
sanat|n|ar|ṣanʿa|yapma ustalığı|EAT|S-N-A|
sanayi|n|ar|ṣanāʾiʿ|zanaatlar|OSM19|S-N-A|
sınaî|adj|ar|ṣināʿī|endüstriyel|OSM19|S-N-A|
sanatkâr|n|ar|ṣanʿa-kār|sanat yapan|OSM|-kār|ar:ṣanʿa>fa:ṣanʿat-kār>tr:sanatkâr
zanaat|n|ar|ṣanʿa|el işi|OSM|S-N-A|
medeniyet|n|ar|madaniyya|şehirlilik, uygarlık|OSM19|M-D-N|
medenî|adj|ar|madanī|şehirli, uygar|OSM|M-D-N|
siyaset|n|ar|siyāsa|yönetme|EAT|S-Y-S|
siyasî|adj|ar|siyāsī|politik|OSM19|S-Y-S|
seyis|n|ar|sāʾis|at bakıcısı|EAT|S-Y-S|
devir|n|ar|dawr|dönüş, çağ|EAT|D-W-R|
devre|n|ar|dawra|dönem|OSM|D-W-R|
daire|n|ar|dāʾira|çember; büro|EAT|D-W-R|
idare|n|ar|idāra|yönetim|OSM|D-W-R|
müdür|n|ar|mudīr|yöneten|OSM19|D-W-R|
devran|n|ar|dawrān|dönüş, zaman|EAT|D-W-R|
idari|adj|ar|idārī|yönetimsel|OSM19|D-W-R|
taraf|n|ar|ṭaraf|yan|EAT|T-R-F|
etraf|n|ar|aṭrāf|yanlar, çevre|EAT|T-R-F|
bitaraf|adj|ar|bī-ṭaraf|yansız|OSM|T-R-F|
taraftar|n|ar|ṭaraf-dār|yan tutan|OSM|dār-|ar:ṭaraf>fa:ṭaraf-dār>tr:taraftar
vezin|n|ar|wazn|ölçü|EAT|W-Z-N|
mizan|n|ar|mīzān|terazi|EAT|W-Z-N|
vezne|n|ar|wazna|tartı; kasa|OSM19|W-Z-N|
hamal|n|ar|ḥammāl|yük taşıyan|EAT|H-M-L|
hamile|adj|ar|ḥāmila|yük taşıyan|OSM|H-M-L|
hamle|n|ar|ḥamla|atılım|EAT|H-M-L|
tahammül|n|ar|taḥammul|dayanma|OSM|H-M-L|
ihtimal|n|ar|iḥtimāl|olasılık|OSM|H-M-L|
harf|n|ar|ḥarf|kenar; harf|EAT|H-R-F|
tahrif|n|ar|taḥrīf|bozma|OSM|H-R-F|
harfiyen|adv|ar|ḥarfiyyan|harfi harfine|OSM|H-R-F|
ahit|n|ar|ʿahd|söz, antlaşma|EAT|A-H-D|
taahhüt|n|ar|taʿahhud|üstlenme|OSM19|A-H-D|
muahede|n|ar|muʿāhada|antlaşma|OSM|A-H-D|
fıtrat|n|ar|fiṭra|yaratılış|EAT|F-T-R|
iftar|n|ar|ifṭār|oruç açma|EAT|F-T-R|
fitre|n|ar|fiṭra|fitre sadakası|EAT|F-T-R|
secde|n|ar|sacda|yere kapanma|EAT|S-C-D|
mescit|n|ar|mascid|secde yeri|EAT|S-C-D|
seccade|n|ar|saccāda|namazlık|OSM|S-C-D|
sulh|n|ar|ṣulḥ|barış|EAT|S-L-H|
ıslah|n|ar|iṣlāḥ|düzeltme|OSM|S-L-H|
salih|adj|ar|ṣāliḥ|iyi, uygun|EAT|S-L-H|
maslahat|n|ar|maṣlaḥa|iş, çıkar|OSM|S-L-H|
dua|n|ar|duʿāʾ|çağrı, yakarış|EAT|D-A-W|
dava|n|ar|daʿwā|iddia; mahkeme işi|EAT|D-A-W|
davet|n|ar|daʿwa|çağrı|EAT|D-A-W|
iddia|n|ar|iddiʿāʾ|sav|OSM|D-A-W|
davetiye|n|ar|daʿwa|çağrı kartı|OSM19|D-A-W|
talih|n|ar|ṭāliʿ|doğan yıldız, şans|EAT|T-L-A|
mütalaa|n|ar|muṭālaʿa|inceleme|OSM|T-L-A|
hal|n|ar|ḥāl|durum|EAT|H-W-L|
ahval|n|ar|aḥwāl|durumlar|EAT|H-W-L|
havale|n|ar|ḥiwāla|aktarma|OSM|H-W-L|
tahvil|n|ar|taḥwīl|dönüştürme; borç senedi|OSM19|H-W-L|
halk|n|ar|ḫalq|yaratılanlar, insanlar|EAT|H-L-K|
hilkat|n|ar|ḫilqa|yaratılış|EAT|H-L-K|
ahlak|n|ar|aḫlāq|huylar|EAT|H-L-K|
mahlûk|n|ar|maḫlūq|yaratılmış|EAT|H-L-K|
sadık|adj|ar|ṣādiq|doğru, bağlı|EAT|S-D-K|
sadaka|n|ar|ṣadaqa|gönüllü bağış|EAT|S-D-K|
sadakat|n|ar|ṣadāqa|bağlılık|EAT|S-D-K|
tasdik|n|ar|taṣdīq|onaylama|OSM|S-D-K|
azim|n|ar|ʿazm|kararlılık|EAT|A-Z-M|
azamet|n|ar|ʿaẕama|büyüklük|EAT|A-Z-M|
muazzam|adj|ar|muʿaẕẕam|çok büyük|OSM|A-Z-M|
kemal|n|ar|kamāl|olgunluk|EAT|K-M-L|
kâmil|adj|ar|kāmil|olgun, tam|EAT|K-M-L|
tekâmül|n|ar|takāmul|olgunlaşma, evrim|OSM19|K-M-L|
mükemmel|adj|ar|mukammal|tamamlanmış, kusursuz|OSM|K-M-L|
ikmal|n|ar|ikmāl|tamamlama|OSM|K-M-L|
suret|n|ar|ṣūra|biçim, kopya|EAT|S-W-R|
tasvir|n|ar|taṣwīr|betimleme|EAT|S-W-R|
tasavvur|n|ar|taṣawwur|hayal etme|OSM|S-W-R|
nefes|n|ar|nafas|soluk|EAT|N-F-S|
nefis|n|ar|nafs|can, benlik|EAT|N-F-S|
nüfus|n|ar|nufūs|canlar, kişiler|OSM|N-F-S|
teneffüs|n|ar|tanaffus|soluk alma; ara|OSM19|N-F-S|
hediye|n|ar|hadiyya|armağan|EAT|H-D-Y|
hidayet|n|ar|hidāya|doğru yolu bulma|EAT|H-D-Y|
kâfir|n|ar|kāfir|örten, inkâr eden|EAT|K-F-R|
küfür|n|ar|kufr|inkâr; sövgü|EAT|K-F-R|
kefaret|n|ar|kaffāra|günah bedeli|EAT|K-F-R|
sabır|n|ar|ṣabr|dayanma|EAT|S-B-R|
sabretmek|v|ar|ṣabr|dayanmak|EAT|S-B-R|
sabırlı|adj|ar|ṣabr|dayanıklı|EAT|S-B-R|
zahir|adj|ar|ẕāhir|görünen|EAT|Z-H-R|
zuhur|n|ar|ẕuhūr|ortaya çıkma|OSM|Z-H-R|
tezahür|n|ar|taẕāhur|görünüş|OSM19|Z-H-R|
mazhar|adj|ar|maẕhar|erişen|OSM|Z-H-R|
hikâye|n|ar|ḥikāya|anlatı|EAT|H-K-Y|
hikâyeci|n|ar|ḥikāya|öykü yazarı|OSM|H-K-Y|
akit|n|ar|ʿaqd|sözleşme|OSM|A-K-D|
akide|n|ar|ʿaqīda|inanç|EAT|A-K-D|
itikat|n|ar|iʿtiqād|inanç|EAT|A-K-D|
cihat|n|ar|cihād|çaba, kutsal savaş|EAT|C-H-D|
içtihat|n|ar|ictihād|görüş çıkarma|OSM|C-H-D|
mücahit|n|ar|mucāhid|savaşçı|EAT|C-H-D|
zaman|n|ar|zamān|vakit|EAT||
vakit|n|ar|waqt|zaman|EAT||
saat|n|ar|sāʿa|an, saat|EAT||
dakika|n|ar|daqīqa|ince; dakika|OSM||
saniye|n|ar|ṯāniya|ikinci|OSM19||
sene|n|ar|sana|yıl|EAT||
asır|n|ar|ʿaṣr|çağ, yüzyıl|EAT||
hafta|n|fa|hafte|yedili|EAT||
dünya|n|ar|dunyā|en yakın; yeryüzü|EAT||
ahiret|n|ar|āḫira|öte dünya|EAT||
insan|n|ar|insān|insan|EAT||
beşer|n|ar|başar|insanlık|EAT||
millet|n|ar|milla|din topluluğu; ulus|EAT||
millî|adj|ar|millī|ulusal|OSM19||
vatan|n|ar|waṭan|yurt|EAT||
vatandaş|n|ar|waṭan|yurttaş|OSM19||
cumhuriyet|n|ar|cumhūriyya|halk yönetimi|OSM19|C-M-H|
cumhur|n|ar|cumhūr|halk topluluğu|OSM|C-M-H|
meclis|n|ar|maclis|oturma yeri|EAT|C-L-S|
kanun|n|ar|qānūn|yasa|EAT|K-N-N|grc:kanṑn>ar:qānūn>tr:kanun
nizamname|n|ar|niẕām-nāme|yönetmelik|OSM19|-nāme|ar:niẕām>fa:niẕām-nāme>tr:nizamname
memur|n|ar|maʾmūr|emredilen|OSM|E-M-R|
emir|n|ar|amr|buyruk|EAT|E-M-R|
emretmek|v|ar|amr|buyurmak|EAT||
vali|n|ar|wālī|yöneten|EAT|W-L-Y|
kaymakam|n|ar|qāʾim-maqām|yerine duran|OSM|K-W-M|
belediye|n|ar|baladiyya|şehir yönetimi|OSM19|B-L-D|
mahalle|n|ar|maḥalla|konak yeri|EAT|H-L-L|
şehir|n|fa|şahr|kent|EAT||
kasaba|n|ar|qaṣaba|kale içi|EAT||
cadde|n|ar|cādda|ana yol|OSM||
sokak|n|ar|zuqāq|dar yol|EAT||
meydan|n|ar|maydān|alan|EAT||
kale|n|ar|qalʿa|hisar|EAT||
hisar|n|ar|ḥiṣār|çevirme, kale|EAT|H-S-R|
saray|n|fa|sarāy|konak|EAT||
mezar|n|ar|mazār|ziyaret yeri|EAT||
kabir|n|ar|qabr|mezar|EAT||
türbe|n|ar|turba|toprak; anıt mezar|EAT||
minare|n|ar|manāra|ışık yeri|EAT|N-W-R|
mihrap|n|ar|miḥrāb|cami nişi|EAT|H-R-B|
minber|n|ar|minbar|kürsü|EAT||
imam|n|ar|imām|önder|EAT|A-M-M|
müezzin|n|ar|muʾaẕẕin|ezan okuyan|EAT|A-Z-N|
ezan|n|ar|aẕān|çağrı|EAT|A-Z-N|
namaz|n|fa|namāz|ibadet|EAT||
oruç|n|fa|rōza|oruç|EAT||
hac|n|ar|ḥacc|ziyaret|EAT|H-C-C|
hacı|n|ar|ḥāccī|hacca giden|EAT|H-C-C|
zekât|n|ar|zakāt|arınma; vergi|EAT||
kurban|n|ar|qurbān|yakınlaşma; adak|EAT|K-R-B|
bayram|n|tr|badram|şenlik|DLT||
din|n|ar|dīn|inanç|EAT||
iman|n|ar|īmān|inanç|EAT|A-M-N|
mümin|n|ar|muʾmin|inanan|EAT|A-M-N|
günah|n|fa|gunāh|suç|EAT||
sevap|n|ar|ṯawāb|ödül|EAT||
cennet|n|ar|canna|bahçe|EAT|C-N-N|
cehennem|n|ar|cahannam|cehennem|EAT||he:gē-hinnōm>ar:cahannam>tr:cehennem
melek|n|ar|malak|elçi|EAT||
şeytan|n|ar|şayṭān|kötü ruh|EAT||
ruh|n|ar|rūḥ|nefes, can|EAT|R-W-H|
nur|n|ar|nūr|ışık|EAT|N-W-R|
Allah|n|ar|allāh|Tanrı|EAT||
rab|n|ar|rabb|efendi, Tanrı|EAT||
hüda|n|ar|hudā|Tanrı|EAT||
kul|n|tr|kul|hizmetkâr|ORH||
ecel|n|ar|acal|ömür sonu|EAT||
kısmet|n|ar|qisma|pay|EAT||
nasip|n|ar|naṣīb|pay|EAT||
bereket|n|ar|baraka|bolluk|EAT|B-R-K|
rızık|n|ar|rizq|geçimlik|EAT||
şifa|n|ar|şifāʾ|iyileşme|EAT|Ş-F-Y|
afiyet|n|ar|ʿāfiya|sağlık|EAT||
sıhhat|n|ar|ṣiḥḥa|sağlık|EAT|S-H-H|
maraz|n|ar|maraḏ|hastalık|EAT||
illet|n|ar|ʿilla|hastalık, neden|EAT||
ameliyat|n|ar|ʿamaliyya|işlem|OSM19|A-M-L|
hastane|n|fa|ḫaste-ḫāne|hasta evi|OSM19|-hāne|
eczane|n|ar|aczāʾ-ḫāne|ilaç evi|OSM19|-hāne|ar:aczāʾ>fa:eczā-ḫāne>tr:eczane
ecza|n|ar|aczāʾ|parçalar; ilaçlar|OSM|C-Z-A|
deva|n|ar|dawāʾ|ilaç|EAT|D-W-Y|
zehir|n|fa|zahr|ağı|EAT||
şerbet|n|ar|şarba|içecek|EAT||
şarap|n|ar|şarāb|içecek|EAT||
kahve|n|ar|qahwa|kahve|OSM||ar:qahwa>ota:kahve>tr:kahve
şeker|n|fa|şakar|şeker|EAT||sa:śarkarā>fa:şakar>tr:şeker
helva|n|ar|ḥalwā|tatlı|EAT|H-L-W|
lokum|n|ar|luqma|lokma|OSM||ar:rāḥat al-ḥulqūm>ota:rahatü'l-hulkum>tr:lokum
lokma|n|ar|luqma|ağız dolusu|EAT||
baklava|n|tr|baklava|katmerli tatlı|OSM||
revani|n|fa|revānī|tatlı|OSM||
kadayıf|n|ar|qaṭāʾif|kadife; tatlı|EAT||
muhallebi|n|ar|muhallabiyya|sütlü tatlı|OSM||
sütlaç|n|tr|sütlü aş|sütlü tatlı|OSM|*aş|
hoşaf|n|fa|ḫoş-āb|hoş su|OSM|āb|
meyve|n|fa|mīve|yemiş|EAT||
sebze|n|fa|sabze|yeşillik|OSM||
zeytin|n|ar|zaytūn|zeytin|EAT||
zeytinyağı|n|ar|zaytūn|zeytin yağı|EAT||
limon|n|fa|līmū|limon|EAT||fa:līmū>ar:laymūn>tr:limon
portakal|n|pt|Portugal|Portekiz|OSM||pt:Portugal>it:portogallo>el:portokáli>ota:portakal>tr:portakal
nar|n|fa|anār|nar|EAT||
incir|n|fa|ancīr|incir|EAT||
hurma|n|fa|ḫurmā|hurma|EAT||
muz|n|ar|mawz|muz|OSM||
karpuz|n|fa|ḫarbuze|karpuz|EAT||
hıyar|n|fa|ḫiyār|salatalık|EAT||
patlıcan|n|ar|bāḏincān|patlıcan|EAT||sa:vātiṅgaṇa>fa:bādingān>ar:bāḏincān>tr:patlıcan
ıspanak|n|fa|ispanāḫ|ıspanak|EAT||
nohut|n|fa|nuḫūd|nohut|EAT||
mercimek|n|fa|marcumak|mercimek|EAT||
fasulye|n|el|fasóli|fasulye|OSM||la:phaseolus>el:fasóli>tr:fasulye
susam|n|ar|simsim|susam|EAT||
tarçın|n|fa|dārçīn|Çin ağacı|EAT||
karanfil|n|ar|qaranful|karanfil|EAT||
zencefil|n|ar|zancabīl|zencefil|EAT||
kimyon|n|el|kýminon|kimyon|EAT||
safran|n|ar|zaʿfarān|safran|EAT||
nane|n|ar|naʿnaʿ|nane|EAT||
maydanoz|n|el|makedonísi|maydanoz|OSM||
fıstık|n|ar|fustuq|fıstık|EAT||el:pistákion>ar:fustuq>tr:fıstık
cezve|n|ar|caḏwa|kor, köz|OSM||
fincan|n|fa|pingān|kâse|EAT||fa:pingān>ar:fincān>tr:fincan
ibrik|n|ar|ibrīq|su kabı|EAT||fa:āb-rīz>ar:ibrīq>tr:ibrik
sürahi|n|ar|ṣurāḥī|şişe|OSM||
tencere|n|ar|ṭancara|kap|EAT||
sahan|n|ar|ṣaḥn|tabak|EAT||
tas|n|ar|ṭās|çanak|EAT||
mutfak|n|ar|maṭbaḫ|pişirme yeri|EAT|T-B-H|
sofa odası|n|ar|ṣuffa|oturma yeri|OSM||
elbise|n|ar|albisa|giysiler|EAT||
kumaş|n|ar|qumāş|dokuma|EAT||
kadife|n|ar|qaṭīfa|kadife|EAT||
keten|n|ar|kattān|keten|EAT||
yelek|n|ar|yalak|yelek|OSM||
cep|n|ar|cayb|cep|EAT||
cüzdan|n|fa|cuz-dān|cüz tutan|OSM|C-Z-A|
kese|n|fa|kīse|torba|EAT||
sandık|n|ar|ṣandūq|kutu|EAT||
kutu|n|el|koutí|kutu|EAT||
raf|n|ar|raff|raf|OSM||
dolap|n|ar|dūlāb|çıkrık; dolap|EAT||
sedir|n|ar|ṣadr|göğüs; baş köşe|EAT||
minder|n|fa|mindar|minder|EAT||
perde|n|fa|parde|örtü|EAT||
halıcı|n|tr|kalı|halı satan|OSM||
kilimci|n|fa|gilīm|kilim dokuyan|OSM||
hamam|n|ar|ḥammām|yıkanma yeri|EAT|H-M-M|
sabun|n|ar|ṣābūn|sabun|EAT||la:sapo>ar:ṣābūn>tr:sabun
havlu|n|tr|havlu|havlu|OSM||
peşkir|n|fa|pīşgīr|önlük|EAT||
tarak|n|tr|targak|tarak|DLT||
ayna|n|fa|āyīne|ayna|EAT||
misk|n|ar|misk|misk|EAT||
amber|n|ar|ʿanbar|amber|EAT||
gül suyu|n|fa|gul|gül suyu|EAT||
sürme|n|tr|sürme|göz boyası|EAT||
kına|n|ar|ḥinnāʾ|kına|EAT||
asker ocağı|n|ar|ʿasker|askerî birlik|OSM||
ordugâh|n|tr|ordu-gāh|ordu yeri|OSM||
cephe|n|ar|cabha|alın; cephe|OSM19||
silah|n|ar|silāḥ|silah|EAT||
tüfek|n|fa|tufak|üfleme borusu|EAT||
tabanca|n|tr|tabanca|el silahı|OSM||
kurşun mermi|n|tr|korgaşun|mermi|OSM||
mermi|n|ar|marmī|atılan|OSM||
barut|n|ar|bārūd|barut|EAT||
zafer|n|ar|ẕafar|üstün gelme|EAT||
fetih|n|ar|fatḥ|açma|EAT||
fatih|n|ar|fātiḥ|açan|EAT||
gazi|n|ar|ġāzī|akıncı|EAT||
şehadet parmağı|n|ar|şahāda|işaret parmağı|OSM||
düşman|n|fa|duşman|düşman|EAT||
dost|n|fa|dōst|arkadaş|EAT||
arkadaş|n|tr|arka-daş|yol arkadaşı|OSM||
yâr|n|fa|yār|sevgili, dost|EAT||
rakip|n|ar|raqīb|gözleyen|OSM||
hasım|n|ar|ḫaṣm|düşman|EAT||
muhalif|n|ar|muḫālif|karşı olan|OSM||
muhalefet|n|ar|muḫālafa|karşıtlık|OSM19||
ittifak|n|ar|ittifāq|uyuşma|OSM|W-F-K|
anlaşma metni|n|ar|ʿahd|antlaşma|OSM||
muahede metni|n|ar|muʿāhada|antlaşma|OSM||
sulh anlaşması|n|ar|ṣulḥ|barış|OSM||
harp|n|ar|ḥarb|savaş|EAT|H-R-B|
muharebe|n|ar|muḥāraba|çarpışma|OSM|H-R-B|
cenk|n|fa|cang|savaş|EAT||
mücadele|n|ar|mucādala|çekişme|OSM||
gayret|n|ar|ġayra|çaba|EAT||
cesaret|n|ar|casāra|yüreklilik|EAT||
cesur|adj|ar|casūr|yürekli|OSM||
korkusuzluk|n|tr|korku|cesaret|OSM|*kork-|
şeref|n|ar|şaraf|onur|EAT||
namus|n|ar|nāmūs|yasa; onur|EAT||grc:nómos>ar:nāmūs>tr:namus
haysiyet|n|ar|ḥayṯiyya|onur|OSM19||
izzet|n|ar|ʿizza|yücelik|EAT||
şan|n|ar|şaʾn|ün|EAT||
itibar|n|ar|iʿtibār|saygınlık|OSM||
hürmet|n|ar|ḥurma|saygı|EAT|H-R-M|
edep|n|ar|adab|görgü|EAT|A-D-B|
edebiyat|n|ar|adabiyyāt|yazın|OSM19|A-D-B|
edip|n|ar|adīb|yazar|OSM|A-D-B|
nesir|n|ar|naṯr|düzyazı|EAT||
nazım biçimi|n|ar|naẕm|şiir|EAT||
beyit|n|ar|bayt|ev; iki dize|EAT|B-Y-T|
mısra|n|ar|miṣrāʿ|kapı kanadı; dize|EAT||
kafiye|n|ar|qāfiya|uyak|EAT||
redif|n|ar|radīf|arkadan gelen|EAT||
gazel|n|ar|ġazal|aşk şiiri|EAT||
kaside|n|ar|qaṣīda|övgü şiiri|EAT|K-S-D|
mesnevi|n|ar|maṯnawī|ikili|EAT||
divan|n|fa|dīvān|defter; şiir kitabı; kurul|EAT||
sohbet|n|ar|ṣuḥba|arkadaşlık; söyleşi|EAT||
muhabbet|n|ar|maḥabba|sevgi|EAT||
sevda|n|ar|sawdāʾ|kara safra; aşk|EAT||
merak|n|ar|marāq|kara sevda; ilgi|OSM||
keyif|n|ar|kayf|durum; hoşnutluk|EAT||
rahat|n|ar|rāḥa|dinlenme|EAT|R-W-H|
zevk|n|ar|ḏawq|tat alma|EAT||
lezzet|n|ar|laḏḏa|tat|EAT||
neşe|n|ar|naşʾa|coşku|OSM||
huzur|n|ar|ḥuḏūr|hazır bulunma; dinginlik|EAT||
sükûnet|n|ar|sukūn|dinginlik|EAT||
sükût|n|ar|sukūt|sessizlik|EAT||
sabah namazı|n|ar|ṣabāḥ|sabah ibadeti|EAT||
hüzün|n|ar|ḥuzn|keder|EAT||
keder|n|ar|kadar|üzüntü|EAT||
gam|n|ar|ġamm|tasa|EAT||
elem|n|ar|alam|acı|EAT||
dert|n|fa|dard|ağrı, acı|EAT||
tasa|n|fa|tāse|kaygı|EAT||
endişe|n|fa|andīşe|düşünce; kaygı|EAT||
hasret|n|ar|ḥasra|özlem|EAT||
hayal|n|ar|ḫayāl|görüntü, düş|EAT||
rüya|n|ar|ruʾyā|görme; düş|EAT||
düş|n|tr|tüş|rüya|DLT||
hayret|n|ar|ḥayra|şaşkınlık|EAT||
hiddet|n|ar|ḥidda|öfke|EAT||
gazap|n|ar|ġaḏab|öfke|EAT||
nefret|n|ar|nafra|tiksinti|OSM||
haset|n|ar|ḥasad|çekememe|EAT||
kibir|n|ar|kibr|büyüklenme|EAT|K-B-R|
gurur|n|ar|ġurūr|aldanma; kibir|EAT||
tevazu|n|ar|tawāḏuʿ|alçakgönüllülük|EAT||
sahip|n|ar|ṣāḥib|arkadaş; mal sahibi|EAT||
mal|n|ar|māl|varlık|EAT||
servet|n|ar|ṯarwa|zenginlik|OSM||
zengin|adj|fa|sangīn|taş gibi, ağır|EAT||
fakir|adj|ar|faqīr|yoksul|EAT||
fukara|n|ar|fuqarāʾ|yoksullar|EAT||
sefalet|n|ar|safāla|yoksulluk|OSM19||
miskin|adj|ar|miskīn|zavallı|EAT||
garip|adj|ar|ġarīb|yabancı, tuhaf|EAT||
acayip|adj|ar|ʿacāʾib|şaşılacak şeyler|EAT||
tuhaf|adj|ar|tuḥaf|nadide şeyler|OSM||
basit|adj|ar|basīṭ|yayılmış; sade|OSM||
sade|adj|fa|sāde|yalın|EAT||
mühim|adj|ar|muhimm|önemli|OSM||
ehemmiyet|n|ar|ahammiyya|önem|OSM19||
lazım|adj|ar|lāzim|gerekli|EAT||
lüzum|n|ar|luzūm|gereklilik|OSM||
ihtiyaç|n|ar|iḥtiyāc|gereksinim|OSM||
zaruri|adj|ar|ḏarūrī|zorunlu|OSM|D-R-R|
mecbur|adj|ar|macbūr|zorunlu|OSM||
mecburiyet|n|ar|macbūriyya|zorunluluk|OSM19||
kabul|n|ar|qabūl|benimseme|EAT||
ret|n|ar|radd|geri çevirme|OSM||
inkâr|n|ar|inkār|yadsıma|EAT||
tasdik belgesi|n|ar|taṣdīq|onay|OSM||
onay|n|tr|onay|tasdik|DD|*ona-|
izin|n|ar|iḏn|müsaade|EAT|A-Z-N|
müsaade|n|ar|musāʿada|yardım; izin|OSM||
ruhsat|n|ar|ruḫṣa|izin|OSM||
yardım|n|fa|yārī|dostluk, yardım|EAT||
imdat|n|ar|imdād|yardım|OSM|M-D-D|
hizmet|n|ar|ḫidma|görev|EAT||
hizmetkâr|n|ar|ḫidmat-kār|hizmet eden|OSM|-kār|ar:ḫidma>fa:ḫidmet-kār>tr:hizmetkâr
vazife|n|ar|waẕīfa|görev|OSM||
mesuliyet|n|ar|masʾūliyya|sorumluluk|OSM19||
mesul|adj|ar|masʾūl|sorumlu|OSM||
sual|n|ar|suʾāl|soru|EAT||
cevap|n|ar|cawāb|yanıt|EAT||
mesele|n|ar|masʾala|sorun|EAT||
sebep|n|ar|sabab|ip; neden|EAT||
netice|n|ar|natīca|sonuç|OSM||
şart|n|ar|şarṭ|koşul|EAT||
sıfat|n|ar|ṣifa|nitelik|EAT||
isim|n|ar|ism|ad|EAT||
zamir|n|ar|ḏamīr|iç; adıl|OSM||
zarf|n|ar|ẕarf|kap; belirteç|OSM||
edat|n|ar|adāt|araç|OSM||
cümle yapısı|n|ar|cumla|tümce|OSM||
lügat|n|ar|luġa|dil, sözlük|EAT||
sözlük|n|tr|sözlük|lügat|DD||
lisan|n|ar|lisān|dil|EAT||
lehçe|n|ar|lahca|ağız|OSM||
şive|n|fa|şīve|tarz|OSM||
tercüme|n|ar|tarcama|çeviri|EAT||
tercüman|n|ar|tarcumān|çevirmen|EAT||akk:targumannu>ar:tarcumān>tr:tercüman
mana|n|ar|maʿnā|anlam|EAT|A-N-Y|
mefhum|n|ar|mafhūm|kavram|OSM|F-H-M|
kavram|n|tr|kavram|mefhum|DD|*kavra-|
tabir|n|ar|taʿbīr|yorum; deyim|EAT||
ifade|n|ar|ifāda|anlatım|OSM||
beyan|n|ar|bayān|açıklama|EAT||
beyanname|n|ar|bayān-nāme|bildirge|OSM19|-nāme|ar:bayān>fa:bayān-nāme>tr:beyanname
izah|n|ar|īḏāḥ|açıklama|OSM||
şerh|n|ar|şarḥ|açıklama|EAT||
tefsir|n|ar|tafsīr|yorum|EAT||
hikmetli|adj|ar|ḥikma|bilgece|OSM|H-K-M|
felsefe|n|ar|falsafa|bilgelik sevgisi|OSM|sophos|grc:philosophía>ar:falsafa>tr:felsefe
mantık|n|ar|manṭiq|konuşma; akıl yürütme|EAT|N-T-K|
hendese|n|ar|handasa|geometri|OSM|H-N-D-S|fa:andāze>ar:handasa>tr:hendese
riyaziye|n|ar|riyāḏiyya|matematik|OSM19||
cebir|n|ar|cabr|zorlama; cebir|OSM||
kimya|n|ar|kīmiyāʾ|kimya|OSM||grc:khēmeía>ar:kīmiyāʾ>tr:kimya
simya|n|ar|kīmiyāʾ|simya|OSM||
coğrafya|n|ar|cuġrāfiyā|yer betimi|OSM|graphein|grc:geōgraphía>ar:cuġrāfiyā>tr:coğrafya
tarih|n|ar|tārīḫ|tarih|EAT||
hikâye anlatıcısı|n|ar|ḥikāya|meddah|OSM||
tıp fakültesi|n|ar|ṭibb|tıp okulu|OSM19|T-B-B|
eczacı|n|ar|aczāʾ|ilaç yapan|OSM19|C-Z-A|
mühendis|n|ar|muhandis|geometri bilen|OSM|H-N-D-S|
mimar|n|ar|miʿmār|yapı yapan|EAT|A-M-R|
imar|n|ar|iʿmār|yapılandırma|OSM|A-M-R|
inşaat|n|ar|inşāʾāt|yapılar|OSM19|N-Ş-A|
inşa|n|ar|inşāʾ|kurma|OSM|N-Ş-A|
bina|n|ar|binā|yapı|EAT|B-N-Y|
imaret|n|ar|ʿimāra|aşevi|EAT|A-M-R|
han|n|fa|ḫān|kervansaray|EAT||
kervan|n|fa|kārvān|kervan|EAT||
kervansaray|n|fa|kārvān-sarāy|kervan konağı|EAT||
tüccar|n|ar|tuccār|tacirler|EAT|T-C-R|
tacir|n|ar|tācir|ticaret yapan|EAT|T-C-R|
ticaret|n|ar|ticāra|alım satım|EAT|T-C-R|
esnaf|n|ar|aṣnāf|sınıflar|OSM||
sarraf|n|ar|ṣarrāf|para değiştiren|EAT||
kasap|n|ar|qaṣṣāb|et kesen|EAT||
bakkal|n|ar|baqqāl|sebzeci|EAT||
manav|n|tr|manav|meyveci|OSM||
terzi|n|fa|darzī|dikici|EAT||
berber|n|it|barbiere|sakal tıraşçısı|OSM||la:barba>it:barbiere>tr:berber
kuyumcu|n|tr|kuyumçı|altın işleyen|OSM||
demirci|n|tr|temirçi|demir işleyen|DLT||
marangoz|n|it|marangone|marangoz|OSM||ven:marangon>tr:marangoz
dülger|n|fa|durūdgar|ağaç işçisi|EAT||
nalbant|n|fa|naʿl-band|nal bağlayan|EAT||
attar|n|ar|ʿaṭṭār|koku satan|EAT||
hamamcı|n|ar|ḥammām|hamam işleten|OSM||
fiyat|n|ar|fīʾāt|değerler|OSM19||
bedel|n|ar|badal|karşılık|EAT||
ücret|n|ar|ucra|karşılık|EAT||
maaş|n|ar|maʿāş|geçimlik|OSM||
kâr|n|fa|kār|iş; kazanç|EAT|-kār|
zarar|n|ar|ḏarar|kayıp|EAT|D-R-R|
ziyan|n|fa|ziyān|kayıp|EAT||
sermaye|n|fa|ser-māye|ana para|OSM|ser|
hazine|n|ar|ḫazīna|saklanan yer|EAT||
hisse|n|ar|ḥiṣṣa|pay|OSM||
hissedar|n|ar|ḥiṣṣe-dār|pay tutan|OSM19|dār-|ar:ḥiṣṣa>fa:ḥiṣṣe-dār>tr:hissedar
faiz|n|ar|fāʾiḏ|artan|OSM||
kefil|n|ar|kafīl|güvence veren|EAT|K-F-L|
rehin|n|ar|rahn|güvence|EAT||
emanet|n|ar|amāna|güvenilen şey|EAT|A-M-N|
miras|n|ar|mīrāṯ|kalıt|EAT||
vasiyet|n|ar|waṣiyya|son dilek|EAT|W-S-Y|
nikâh|n|ar|nikāḥ|evlenme|EAT||
talak|n|ar|ṭalāq|boşanma|EAT||
mehir|n|ar|mahr|evlilik bedeli|EAT||
aile|n|ar|ʿāʾila|aile|OSM19||
akraba|n|ar|aqribāʾ|yakınlar|EAT|K-R-B|
evlat|n|ar|awlād|çocuklar|EAT||
veled|n|ar|walad|çocuk|EAT||
valide|n|ar|wālida|anne|EAT||
amca|n|ar|ʿamm|babanın kardeşi|EAT||
hala|n|ar|ḫāla|annenin kız kardeşi|EAT||
dayı|n|tr|tagay|annenin erkek kardeşi|DLT||
teyze|n|tr|teyze|annenin kız kardeşi|EAT||
damat|n|fa|dāmād|güvey|EAT||
enişte|n|fa|angişt|enişte|EAT||
kayın|n|tr|kadın|kayın|DLT||
cariye|n|ar|cāriya|hizmetçi kız|EAT||
hanım|n|tr|ḫānım|han eşi|EAT||
efendi|n|el|afthéntis|sahip, efendi|EAT||grc:authéntēs>el:afthéntis>tr:efendi
hoca|n|fa|ḫwāce|efendi, öğretmen|EAT||
molla|n|ar|mawlā|efendi|EAT||
şeyh|n|ar|şayḫ|yaşlı, önder|EAT||
derviş|n|fa|darvīş|yoksul; sufi|EAT||
tekke|n|ar|takya|dayanak; derviş ocağı|EAT||
tarikat|n|ar|ṭarīqa|yol|EAT||
sufi|n|ar|ṣūfī|yünlü giyen|EAT|S-W-F|
tasavvuf|n|ar|taṣawwuf|sufilik|EAT|S-W-F|
velî|n|ar|walī|dost, ermiş|EAT||
evliya|n|ar|awliyāʾ|ermişler|EAT|W-L-Y|
kerem|n|ar|karam|cömertlik|EAT||
cömert|adj|fa|cuvān-mard|yiğit adam|EAT||
cimri|adj|fa|cimrī|pinti|OSM||
hain|adj|ar|ḫāʾin|ihanet eden|EAT||
ihanet|n|ar|ḫiyāna|hainlik|OSM||
zalim|adj|ar|ẕālim|haksızlık eden|EAT|Z-L-M|
zulüm|n|ar|ẕulm|haksızlık|EAT|Z-L-M|
mazlum|adj|ar|maẕlūm|zulme uğrayan|EAT|Z-L-M|
mağdur|adj|ar|maġdūr|haksızlığa uğrayan|OSM||
masum|adj|ar|maʿṣūm|korunmuş, suçsuz|EAT||
günahkâr|n|fa|gunāh-kār|günah işleyen|EAT|-kār|
sahtekâr|n|fa|sāḫte-kār|düzmece yapan|OSM|-kār|
sahte|adj|fa|sāḫte|yapılmış, düzmece|OSM||
bestekâr|n|fa|beste-kār|beste yapan|OSM|-kār|
beste|n|fa|beste|bağlanmış; ezgi|OSM||
fedakâr|adj|ar|fidā-kār|kendini feda eden|OSM19|-kār|ar:fidāʾ>fa:fedā-kār>tr:fedakâr
feda|n|ar|fidāʾ|uğruna verme|EAT||
cefakâr|adj|ar|cafā-kār|cefa çeken|OSM|-kār|ar:cafāʾ>fa:cefā-kār>tr:cefakâr
cefa|n|ar|cafāʾ|eziyet|EAT||
vefa|n|ar|wafāʾ|sözünde durma|EAT||
vefakâr|adj|ar|wafā-kār|vefalı|OSM|-kār|ar:wafāʾ>fa:vefā-kār>tr:vefakâr
ziyankâr|adj|fa|ziyān-kār|zarar veren|OSM|-kār|
tamahkâr|adj|ar|ṭamaʿ-kār|açgözlü|OSM|-kār|ar:ṭamaʿ>fa:ṭamaʿ-kār>tr:tamahkâr
riyakâr|adj|ar|riyā-kār|ikiyüzlü|OSM|-kār|ar:riyāʾ>fa:riyā-kār>tr:riyakâr
defterdar|n|fa|daftar-dār|defter tutan|EAT|dār-|
defter|n|ar|daftar|yazı kâğıdı|EAT||grc:diphthéra>ar:daftar>tr:defter
dindar|adj|ar|dīn-dār|din tutan|OSM|dār-|ar:dīn>fa:dīn-dār>tr:dindar
bayraktar|n|tr|bayrak-dār|bayrak tutan|OSM|dār-|otk:batrak>fa:bayrak-dār>tr:bayraktar
sancaktar|n|tr|sancak-dār|sancak tutan|OSM|dār-|
emektar|adj|tr|emek-dār|emek vermiş|OSM|dār-|
mihmandar|n|fa|mihmān-dār|konuk ağırlayan|OSM|dār-|
kalemdar|n|ar|qalam-dār|kalem tutan|OSM|dār-|
kalem|n|ar|qalam|kamış kalem|EAT||grc:kálamos>ar:qalam>tr:kalem
kâğıt|n|fa|kāġaḏ|kâğıt|EAT||zh:gǔzhǐ>fa:kāġaḏ>tr:kâğıt
mürekkep|n|ar|murakkab|birleştirilmiş|EAT||
sayfa|n|ar|ṣaḥīfa|yazı yüzü|OSM||
satır|n|ar|saṭr|dize, sıra|EAT||
nokta|n|ar|nuqṭa|nokta|EAT||
hat|n|ar|ḫaṭṭ|çizgi; yazı sanatı|EAT||
hattat|n|ar|ḫaṭṭāṭ|güzel yazı yazan|EAT||
imla|n|ar|imlāʾ|yazdırma; yazım|OSM||
harita|n|ar|ḫarīṭa|kese; harita|OSM||el:khártēs>ar:ḫarīṭa>tr:harita
levha|n|ar|lawḥa|tahta, tabela|EAT||
tahta|n|fa|taḫte|tahta|EAT||
sandalye|n|ar|ṣandaliyya|sandal ağacından|OSM||
masa|n|la|mensa|masa|OSM||la:mensa>ro:masă>tr:masa
koltuk|n|tr|koltuk|kol altı; koltuk|DLT||
iskemle|n|el|skamní|iskemle|OSM||la:scamnum>el:skamní>tr:iskemle
lamba|n|el|lámpa|kandil|OSM19||grc:lampás>it:lampa>el:lámpa>tr:lamba
kandil|n|ar|qindīl|kandil|EAT||la:candela>ar:qindīl>tr:kandil
mum|n|fa|mūm|balmumu|EAT||
fener|n|el|fanári|fener|EAT|phainein|grc:phanós>el:fanári>tr:fener
fanus|n|ar|fānūs|fener|OSM|phainein|grc:phanós>ar:fānūs>tr:fanus
sofra bezi|n|ar|sufra|sofra örtüsü|OSM|S-F-R|
"""
