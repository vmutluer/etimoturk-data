# -*- coding: utf-8 -*-
"""Korpus 7 — Hukuk ve diplomasi: yargı, sözleşme, ceza, devlet yönetimi ve uluslararası ilişkiler terimleri."""

WORDS = r"""
# --- Hukuk: Arapça kökenli yargı dili ------------------------------------------------
hukuk|n|ar|ḥuqūq|haklar|OSM|H-K-K|
hukukçu|n|ar|ḥuqūq|hukuk uzmanı|CUM|H-K-K|
hakkaniyet|n|ar|ḥaqqāniyya|hakka uygunluk|OSM19|H-K-K|
kanun|n|ar|qānūn|ölçü, kural|EAT|K-N-N|grc:kanṑn>ar:qānūn>tr:kanun
kanuni|adj|ar|qānūnī|yasaya uygun|OSM|K-N-N|
kanunname|n|ar|qānūn-nāme|yasa kitabı|OSM|-nāme|ar:qānūn>fa:qānūn-nāme>tr:kanunname
tüzük|n|tr|tüzük|düzenleme kuralları|DD|*düz-|
yönetmelik|n|tr|yönetmelik|yönetme kuralları|DD|*yön|
yön|n|tr|yön|taraf, doğrultu|EAT|*yön|
yönetmek|v|tr|yönet-|idare etmek|DD|*yön|
yönetim|n|tr|yönetim|idare|DD|*yön|
yönerge|n|tr|yönerge|talimat|DD|*yön|
dava|n|ar|daʿwā|çağrı; iddia|EAT|D-A-W|
davacı|n|ar|daʿwā|dava açan|OSM|D-A-W|
davalı|n|ar|daʿwā|dava edilen|OSM|D-A-W|
savcı|n|tr|savçı|söz ileten; iddia makamı|DD|*sav|
sav|n|tr|sab|söz; iddia|ORH|*sav|
savunmak|v|tr|sabun-|korumak için söz söylemek|DD|*sav|
savunma|n|tr|sabun-|müdafaa|DD|*sav|
yargıç|n|tr|yargıç|hüküm veren|DD|*yar-|
yargı|n|tr|yarġu|hüküm|DLT|*yar-|
yargılamak|v|tr|yarġula-|hüküm vermek|DD|*yar-|
yarlık|n|tr|yarlıg|buyruk|ORH|*yar-|
avukat|n|fr|avocat|yardıma çağrılan|OSM19|vocare|la:advocatus>fr:avocat>tr:avukat
vokal|adj|fr|vocal|sese ilişkin|CUM|vocare|
provokasyon|n|fr|provocation|kışkırtma|CUM|vocare|
vekâlet|n|ar|wakāla|yetki verme|OSM|W-K-L|
müvekkil|n|ar|muwakkil|vekil tutan|OSM|W-K-L|
tevekkül|n|ar|tawakkul|güvenip bırakma|EAT|W-K-L|
noter|n|fr|notaire|yazman|OSM19|nota|la:notarius>fr:notaire>tr:noter
nota|n|it|nota|işaret; yazı|OSM19|nota|
not|n|fr|note|işaret|OSM19|nota|
tapu|n|tr|tapu|hizmet; mülk belgesi|OSM||
senet|n|ar|sanad|dayanak|OSM|S-N-D|
istinat|n|ar|istinād|dayanma|OSM|S-N-D|
müstenit|adj|ar|mustanid|dayanan|OSM|S-N-D|
sözleşme|n|tr|söz|karşılıklı söz verme|DD||
mukavele|n|ar|muqāwala|karşılıklı söz|OSM|K-W-L|
akit|n|ar|ʿaqd|bağlama|OSM|A-K-D|
nikâh|n|ar|nikāḥ|evlenme bağı|EAT||
vasiyet|n|ar|waṣiyya|öğütle bırakma|EAT|W-S-Y|
vasi|n|ar|waṣī|koruyucu|OSM|W-S-Y|
tavsiye|n|ar|tawṣiya|öğütleme|OSM|W-S-Y|
vesayet|n|ar|waṣāya|koruyuculuk|OSM19|W-S-Y|
varis|n|ar|wāriṯ|mirasçı|OSM|W-R-S|
veraset|n|ar|wirāṯa|miras hakkı|OSM|W-R-S|
mirasçı|n|ar|mīrāṯ|miras alan|OSM19|W-R-S|
suç|n|tr|suç|kabahat|DLT||
suçlu|adj|tr|suçlug|kabahatli|DLT||
cinayet|n|ar|cināya|ağır suç|EAT|C-N-Y|
cani|n|ar|cānī|suç işleyen|OSM|C-N-Y|
katil|n|ar|qātil|öldüren|EAT|K-T-L|
maktul|n|ar|maqtūl|öldürülen|OSM|K-T-L|
katliam|n|ar|qatl-i ʿāmm|toplu öldürme|OSM19|K-T-L|
hırsız|n|tr|ḫırsız|hırsı olan|EAT||ar:ḥırṣ>tr:hırsız
dolandırmak|v|tr|tolan-|aldatarak kandırmak|OSM||
rüşvet|n|ar|rişwa|yem|EAT||
irtikap|n|ar|irtikāb|kötülük işleme|OSM||
zimmet|n|ar|ẕimma|borç; koruma yükümü|OSM|Z-M-M|
kefalet|n|ar|kafāla|üstlenme|OSM|K-F-L|
kefil|n|ar|kafīl|üstlenen|EAT|K-F-L|
teminat|n|ar|taʾmīnāt|güvenceler|OSM19|A-M-N|
emin|adj|ar|amīn|güvenilir|EAT|A-M-N|
emniyet|n|ar|amniyya|güvenlik|OSM|A-M-N|
emanet|n|ar|amāna|güvenilip bırakılan|EAT|A-M-N|
iman|n|ar|īmān|güvenle inanma|EAT|A-M-N|
mümin|n|ar|muʾmin|inanan|EAT|A-M-N|
amin|intj|ar|āmīn|öyle olsun|EAT|A-M-N|
rehin|n|ar|rahn|güvence malı|OSM||
ipotek|n|fr|hypothèque|altına koyma|OSM19||grc:hypothḕkē>fr:hypothèque>tr:ipotek
icra|n|ar|icrāʾ|yürütme|OSM|C-R-Y|
cari|adj|ar|cārī|akan, yürüyen|OSM|C-R-Y|
cereyan|n|ar|carayān|akış|OSM|C-R-Y|
mecra|n|ar|macrā|akış yolu|OSM|C-R-Y|
haciz|n|ar|ḥacz|el koyma|OSM19|H-C-Z|
mahcuz|adj|ar|maḥcūz|el konulmuş|OSM19|H-C-Z|
iflas|n|ar|iflās|parasız kalma|OSM|F-L-S|
müflis|adj|ar|muflis|parasız|OSM|F-L-S|
tazminat|n|ar|taḏmīnāt|ödence|OSM19||
zarar|n|ar|ḏarar|kayıp|EAT|D-R-R|
muzır|adj|ar|muḏirr|zarar veren|OSM|D-R-R|
zaruret|n|ar|ḏarūra|zorunluluk|OSM|D-R-R|
zaruri|adj|ar|ḏarūrī|zorunlu|OSM|D-R-R|
kusur|n|ar|quṣūr|eksiklik|OSM|Q-Ṣ-R|
kast|n|ar|qaṣd|niyet|OSM|K-S-D|
maksat|n|ar|maqṣad|hedef|EAT|K-S-D|
kasıt|n|ar|qaṣd|bile isteye|OSM19|K-S-D|
kasten|adv|ar|qaṣdan|bilerek|OSM|K-S-D|
iktisat|n|ar|iqtiṣād|ölçülü harcama|OSM19|K-S-D|
taksir|n|ar|taqṣīr|kısaltma; ihmal|OSM|Q-Ṣ-R|
tahliye|n|ar|taḫliya|boşaltma|OSM||
gözaltı|n|tr|göz altı|geçici tutma|TDK|*kör-|
hapis|n|ar|ḥabs|kapatma|EAT|H-B-S|
mahpus|n|ar|maḥbūs|kapatılmış|EAT|H-B-S|
hapishane|n|ar|ḥabs-ḫāne|kapatma evi|OSM|-hāne|ar:ḥabs>fa:ḥabs-ḫāne>tr:hapishane
zindan|n|fa|zindān|karanlık hapis|EAT||
cezaevi|n|ar|cazāʾ|ceza yeri|DD||
sanık|n|tr|sanık|sanılan|DD|*san-|
sanmak|v|tr|sa-|düşünmek, varsaymak|ORH|*san-|
sanı|n|tr|sanı|varsayım|DD|*san-|
tanık|n|tr|tanuk|gören, bilen|DLT|*tanı-|
şahit|n|ar|şāhid|gören|EAT|Ş-H-D|
delil|n|ar|dalīl|yol gösteren|EAT|D-L-L|
delalet|n|ar|dalāla|gösterme|OSM|D-L-L|
istidlal|n|ar|istidlāl|delil çıkarma|OSM|D-L-L|
kanıt|n|tr|kanıt|delil|DD|*kan-|
kanmak|v|tr|kan-|inanmak; doymak|DLT|*kan-|
kandırmak|v|tr|kantur-|inandırmak; aldatmak|DLT|*kan-|
itiraf|n|ar|iʿtirāf|kabul etme|OSM|A-R-F|
ikrar|n|ar|iqrār|kabul, onama|EAT|K-R-R|
karar|n|ar|qarār|yerleşme; hüküm|EAT|K-R-R|
mukarrer|adj|ar|muqarrar|kararlaştırılmış|OSM|K-R-R|
takrir|n|ar|taqrīr|yerleştirme; anlatım|OSM|K-R-R|
tekrar|n|ar|takrār|yineleme|EAT|K-R-R|
kararname|n|ar|qarār-nāme|karar yazısı|OSM19|K-R-R|ar:qarār>fa:qarār-nāme>tr:kararname
yemin|n|ar|yamīn|sağ el; ant|EAT|Y-M-N|
yemen|n|ar|yaman|sağ taraf; uğur|EAT|Y-M-N|
beraat|n|ar|barāʾa|arınma|OSM|B-R-A|
berat|n|ar|barāʾa|imtiyaz belgesi|OSM|B-R-A|
temyiz|n|ar|tamyīz|ayırt etme|OSM19|M-Y-Z|
mümeyyiz|n|ar|mumayyiz|ayırt eden|OSM19|M-Y-Z|
mümtaz|adj|ar|mumtāz|seçkin|OSM|M-Y-Z|
imtiyaz|n|ar|imtiyāz|ayrı tutulma|OSM|M-Y-Z|
istinaf|n|ar|istiʾnāf|yeniden başlama|OSM19||
infaz|n|ar|infāḏ|yerine getirme|OSM|N-F-Z|
nüfuz|n|ar|nufūḏ|içe işleme; etki|OSM|N-F-Z|
nafiz|adj|ar|nāfiḏ|işleyen|OSM|N-F-Z|
adalet|n|ar|ʿadāla|denklik|EAT|A-D-L|
adliye|n|ar|ʿadliyya|yargı örgütü|OSM19|A-D-L|
muadil|adj|ar|muʿādil|denk|OSM|A-D-L|
tadil|n|ar|taʿdīl|düzeltme|OSM|A-D-L|
zulüm|n|ar|ẕulm|haksızlık|EAT|Z-L-M|
zalim|adj|ar|ẕālim|haksızlık eden|EAT|Z-L-M|
mazlum|adj|ar|maẕlūm|haksızlığa uğrayan|EAT|Z-L-M|
zulmet|n|ar|ẕulma|karanlık|EAT|Z-L-M|
meşru|adj|ar|maşrūʿ|yasaya uygun|OSM|Ş-R-A|
şeriat|n|ar|şarīʿa|yol; din yasası|EAT|Ş-R-A|
teşri|n|ar|taşrīʿ|yasa koyma|OSM19|Ş-R-A|
şeri|adj|ar|şarʿī|şeriata uygun|EAT|Ş-R-A|
fetva|n|ar|fatwā|dinî hukuk görüşü|EAT|F-T-W|
müftü|n|ar|muftī|fetva veren|EAT|F-T-W|
fıkıh|n|ar|fiqh|derin anlama; İslam hukuku|EAT|F-K-H|
fakih|n|ar|faqīh|hukuk bilgini|EAT|F-K-H|
içtihat|n|ar|ictihād|çabalama; görüş|OSM|C-H-D|
hudut|n|ar|ḥudūd|sınırlar|EAT|H-D-D|
had|n|ar|ḥadd|sınır|EAT|H-D-D|
tahdit|n|ar|taḥdīd|sınırlama|OSM|H-D-D|
mahdut|adj|ar|maḥdūd|sınırlı|OSM|H-D-D|
# --- Diplomasi ve devlet ---------------------------------------------------------------
diplomasi|n|fr|diplomatie|belge işleri|OSM19|diploma|grc:díplōma>la:diploma>fr:diplomatie>tr:diplomasi
diplomat|n|fr|diplomate|belge görevlisi|OSM19|diploma|
diploma|n|fr|diplôme|katlanmış belge|OSM19|diploma|grc:díplōma>fr:diplôme>tr:diploma
diplomatik|adj|fr|diplomatique|diplomasiye ilişkin|CUM|diploma|
elçi|n|tr|élçi|il (barış) getiren|DLT|*el-|
elçilik|n|tr|élçilik|elçi kurumu|OSM|*el-|
büyükelçi|n|tr|büyük élçi|en üst elçi|CUM|*el-|
sefir|n|ar|safīr|yolcu; elçi|OSM|S-F-R|
sefaret|n|ar|safāra|elçilik|OSM|S-F-R|
seferberlik|n|ar|safar-ber-lik|sefere hazırlık|OSM19|S-F-R|
konsolos|n|it|console|danışman|OSM|consulere|la:consul>it:console>tr:konsolos
konsey|n|fr|conseil|danışma kurulu|CUM|consulere|la:consilium>fr:conseil>tr:konsey
konsültasyon|n|fr|consultation|danışma|MOD|consulere|
ataşe|n|fr|attaché|bağlanmış|CUM||
protokol|n|fr|protocole|ilk yapıştırılan yaprak|OSM19|kolla|grc:prōtókollon>fr:protocole>tr:protokol
kolaj|n|fr|collage|yapıştırma|MOD|kolla|
antlaşma|n|tr|ant|ant ile anlaşma|DD|*ant|
ant|n|tr|and|yemin|DLT|*ant|
andaç|n|tr|andaç|hatıra|DD|*ant|
muahede|n|ar|muʿāhada|karşılıklı söz|OSM|A-H-D|
ittifak|n|ar|ittifāq|uyuşma|OSM|W-F-K|
müttefik|n|ar|muttafiq|uyuşan|OSM|W-F-K|
tarafsız|adj|ar|ṭaraf|yan tutmayan|OSM19|T-R-F|
bitaraf|adj|ar|bī-ṭaraf|yansız|OSM19|T-R-F|
mütareke|n|ar|mutāraka|karşılıklı bırakma|OSM19|T-R-K|
terk|n|ar|tark|bırakma|EAT|T-R-K|
metruk|adj|ar|matrūk|bırakılmış|OSM|T-R-K|
ateşkes|n|fa|ātaş|ateşi kesme|CUM||
sulh|n|ar|ṣulḥ|barış|EAT|S-L-H|
ültimatom|n|fr|ultimatum|son söz|OSM19||la:ultimatum>fr:ultimatum>tr:ültimatom
delegasyon|n|fr|délégation|gönderilen kurul|CUM|legare|
delege|n|fr|délégué|gönderilen|CUM|legare|
lejyon|n|fr|légion|seçilmiş birlik|CUM|legere|
heyet|n|ar|hayʾa|biçim; kurul|OSM|H-Y-A|
hey'et|n|ar|hayʾa|gök bilimi|OSM|H-Y-A|
kurul|n|tr|kurul|toplanmış heyet|DD|*kur-|
kurmak|v|tr|kur-|oluşturmak|ORH|*kur-|
kurum|n|tr|kurum|kuruluş|DD|*kur-|
kuruluş|n|tr|kuruluş|örgüt|DD|*kur-|
kurultay|n|mn|quriltai|toplantı|CUM|*kur-|
komisyon|n|fr|commission|görevlendirme|OSM19|mittere|
kongre|n|fr|congrès|bir araya gelme|OSM19||la:congressus>fr:congrès>tr:kongre
konferans|n|fr|conférence|birlikte getirme|OSM19|ferre|
transfer|n|fr|transfert|öteye taşıma|MOD|ferre|
referans|n|fr|référence|geri götürme|MOD|ferre|
zirve|n|ar|ẕirwa|doruk|OSM||
vize|n|fr|visa|görülmüş|CUM|videre|
pasaport|n|fr|passeport|liman geçişi|OSM19|portus|
port|n|fr|port|liman|MOD|portus|
egemen|adj|tr|egemen|üstün, hâkim|DD|*ege|
egemenlik|n|tr|egemenlik|hükümranlık|DD|*ege|
ege|n|tr|ege|büyük, sahip|DLT|*ege|
hükümranlık|n|ar|ḥukm-rān|hüküm sürme|OSM|H-K-M|
istiklal|n|ar|istiqlāl|bağımsızlık|OSM19|K-L-L|
külli|adj|ar|kullī|tümel|OSM|K-L-L|
külliye|n|ar|kulliyya|bütünlük; yapı topluluğu|OSM|K-L-L|
küll|n|ar|kull|bütün|EAT|K-L-L|
cumhuriyet|n|ar|cumhūriyya|halk yönetimi|OSM19|C-M-H|
cumhur|n|ar|cumhūr|halk, çoğunluk|OSM|C-M-H|
cumhurbaşkanı|n|ar|cumhūr|cumhur başkanı|CUM|C-M-H|
demokrasi|n|fr|démocratie|halk egemenliği|OSM19|demos|
monarşi|n|fr|monarchie|tek yönetim|OSM19|arkhein|
anarşi|n|fr|anarchie|yönetimsizlik|OSM19|arkhein|
hiyerarşi|n|fr|hiérarchie|kutsal yönetim|CUM|arkhein|
oligarşi|n|fr|oligarchie|azınlık yönetimi|CUM|arkhein|
arşiv|n|fr|archives|yönetim evi|OSM19|arkhein|grc:arkheîon>la:archivum>fr:archives>tr:arşiv
patrik|n|el|patriárchis|baba yönetici|EAT|arkhein|
meclis|n|ar|maclis|oturma yeri|EAT|C-L-S|
celse|n|ar|calsa|oturum|OSM19|C-L-S|
parlamento|n|it|parlamento|konuşma yeri|OSM19|parabola|
parola|n|it|parola|söz|OSM19|parabola|
senato|n|it|senato|yaşlılar kurulu|OSM19||
anayasa|n|tr|ana yasa|temel yasa|DD||
yasama|n|tr|yasa|yasa yapma|DD||
yürütme|n|tr|yürüt-|uygulama erki|DD|*yürü-|
sadrazam|n|ar|ṣadr-i aʿẕam|en büyük göğüs (başvezir)|OSM|A-Ẕ-M|
vezir|n|ar|wazīr|yük taşıyan|EAT|W-Z-R|
vezaret|n|ar|wizāra|vezirlik|OSM|W-Z-R|
ferman|n|fa|farmān|buyruk|EAT||
tuğra|n|tr|tuğrağ|hükümdar imzası|DLT||
mühür|n|fa|muhr|damga|EAT||
imza|n|ar|imḏāʾ|geçirme; onay|OSM||
tasdik|n|ar|taṣdīq|doğrulama|OSM|S-D-K|
onay|n|tr|ona-|uygun bulma|DD|*ona-|
onamak|v|tr|ona-|uygun bulmak|DLT|*ona-|
onur|n|fr|honneur|saygınlık|CUM||la:honor>fr:honneur>tr:onur
veto|n|fr|veto|yasaklıyorum|CUM||la:veto>fr:veto>tr:veto
ambargo|n|es|embargo|engelleme|CUM||
yaptırım|n|tr|yaptırım|zorlayıcı önlem|DD|*yap-|
arabulucu|n|tr|ara bulucu|uzlaştırıcı|TDK|*bul-|
uzlaşmak|v|tr|uzlaş-|anlaşmak|DD|*uz|
uzlaşma|n|tr|uzlaşma|anlaşma|DD|*uz|
uz|adj|tr|uz|becerikli, iyi|DLT|*uz|
uzman|n|tr|uzman|işinin ustası|DD|*uz|
uzluk|n|tr|uzluk|ustalık|DLT|*uz|
bağımsız|adj|tr|bağımsız|başkasına bağlı olmayan|DD|*bağ-|
muhtar|n|ar|muḫtār|seçilmiş|OSM|Ḫ-Y-R|
ihtiyar|n|ar|iḫtiyār|seçme; yaşlı|EAT|Ḫ-Y-R|
hayır|n|ar|ḫayr|iyilik|EAT|Ḫ-Y-R|
hayırlı|adj|ar|ḫayr|iyilikli|EAT|Ḫ-Y-R|
vali|n|ar|wālī|yöneten|EAT|W-L-Y|
vilayet|n|ar|wilāya|yönetim bölgesi|OSM|W-L-Y|
veli|n|ar|walī|yakın; koruyucu|EAT|W-L-Y|
evliya|n|ar|awliyāʾ|veliler|EAT|W-L-Y|
mevla|n|ar|mawlā|efendi|EAT|W-L-Y|
kaymakam|n|ar|qāʾim-maqām|yerine duran|OSM|K-W-M|
belediye|n|ar|baladiyya|kente ilişkin|OSM19|B-L-D|
belde|n|ar|balda|kent|EAT|B-L-D|
kasaba|n|ar|qaṣaba|kale içi; küçük kent|EAT||
mahalle|n|ar|maḥalla|konaklama yeri|EAT|H-L-L|
mahal|n|ar|maḥall|yer|EAT|H-L-L|
helal|adj|ar|ḥalāl|çözülmüş; izinli|EAT|H-L-L|
tahlil|n|ar|taḥlīl|çözümleme|OSM|H-L-L|
hal|n|ar|ḥall|çözüm|OSM|H-L-L|
ilçe|n|tr|ilçe|il bölümü|DD|*el-|
il|n|tr|él|ülke; yönetim bölgesi|ORH|*el-|
bucak|n|tr|bucgak|köşe; yönetim birimi|DLT||
nahiye|n|ar|nāḥiya|yan; bucak|OSM||
kaza|n|ar|qaḏāʾ|yargı; ilçe; kader|EAT|K-D-Y|
kadı|n|ar|qāḏī|yargıç|EAT|K-D-Y|
eyalet|n|ar|iyāla|yönetim|OSM||
"""

FAMILIES = r"""
*yön|tr|taraf, doğrultu|Eski Anadolu Türkçesi yön "taraf"; yönetmek, yönetim, yönetmelik ve yönerge Dil Devrimi döneminde aynı kökten türetilmiştir.
*sav|tr|söz, iddia|Orhun Yazıtları'ndaki sab "söz"; sav (iddia), savcı ve savunma (müdafaa) aynı kökten gelir.
*yar-|tr|yarmak; hüküm vermek|Eski Türkçe yar- "yarmak, ayırmak"; yargı (yarġu), yargıç, yargılamak ve yarlık (buyruk) aynı kökten türer.
*san-|tr|saymak, düşünmek|Eski Türkçe sa-/san- "saymak, düşünmek"; sanmak, sanı ve sanık (sanılan) aynı köktendir.
*kan-|tr|inanmak, doymak|Eski Türkçe kan- "doymak, inanmak"; kanıt (Dil Devrimi), kanmak ve kandırmak aynı kökten gelir.
*el-|tr|il, ülke, barış|Orhun Yazıtları'ndaki él "ülke, devlet"; il, ilçe, elçi (il arası barış getiren) ve elçilik aynı kökten türer.
*ant|tr|yemin|Eski Türkçe and "yemin"; ant, antlaşma ve andaç (hatıra) aynı kökten gelir.
*kur-|tr|kurmak|Orhun Yazıtları'ndaki kur- "kurmak, dizmek"; kurul, kurum, kuruluş aynı kökten; Moğolca kurultay akraba köktendir.
*ege|tr|sahip, büyük|Eski Türkçe ege/ige "sahip"; egemen (Dil Devrimi) ve egemenlik aynı kökten türetilmiştir.
*ona-|tr|uygun bulmak|Eski Türkçe ona- "uygun bulmak"; onamak ve onay (Dil Devrimi) aynı kökten gelir.
*uz|tr|becerikli|Eski Türkçe uz "usta, becerikli"; uzluk, uzman (Dil Devrimi) ve uzlaşmak aynı kökten türer.
K-N-N|ar|kural|Arapça q-n-n kökü (Yunanca kanṑn'dan); kanun, kanuni ve kanunname aynı kökten gelir.
S-N-D|ar|dayanmak|Arapça s-n-d kökü; senet (dayanak), istinat (dayanma) ve müstenit aynı kökten türer.
W-S-Y|ar|öğütlemek|Arapça w-ṣ-y kökü; vasiyet, vasi, vesayet ve tavsiye aynı kökten gelir.
W-R-S|ar|miras bırakmak|Arapça w-r-ṯ kökü; miras, varis, veraset ve mirasçı aynı kökten türer.
C-N-Y|ar|suç işlemek|Arapça c-n-y kökü; cinayet ve cani aynı kökten gelir.
K-T-L|ar|öldürmek|Arapça q-t-l kökü; katil (öldüren), maktul (öldürülen) ve katliam aynı kökten türer.
K-F-L|ar|üstlenmek|Arapça k-f-l kökü; kefil ve kefalet aynı kökten gelir.
A-M-N|ar|güven|Arapça ʾ-m-n kökü; emin, emniyet, emanet, teminat, iman, mümin ve amin aynı kökten türer.
C-R-Y|ar|akmak|Arapça c-r-y kökü; cari (akan), cereyan (akış), icra (yürütme) ve mecra aynı kökten gelir.
H-C-Z|ar|alıkoymak|Arapça ḥ-c-z kökü; haciz ve mahcuz aynı kökten türer.
F-L-S|ar|parasız kalmak|Arapça f-l-s kökü (fils "küçük para"); iflas ve müflis aynı kökten gelir.
D-R-R|ar|zarar vermek|Arapça ḏ-r-r kökü; zarar, muzır, zaruret ve zaruri aynı kökten türer.
K-S-D|ar|niyet etmek|Arapça q-ṣ-d kökü; kast, kasıt, kasten, maksat ve iktisat (ölçülü harcama) aynı kökten gelir.
H-B-S|ar|kapatmak|Arapça ḥ-b-s kökü; hapis, mahpus ve hapishane aynı kökten türer.
D-L-L|ar|yol göstermek|Arapça d-l-l kökü; delil, delalet ve istidlal aynı kökten gelir.
K-R-R|ar|yerleşmek, yinelemek|Arapça q-r-r kökü; karar, ikrar, mukarrer, takrir, tekrar ve kararname aynı kökten türer.
Y-M-N|ar|sağ taraf, uğur|Arapça y-m-n kökü; yemin (sağ el ile ant), Yemen (sağdaki ülke) ve yemen (uğur) aynı kökten gelir.
B-R-A|ar|arınmak|Arapça b-r-ʾ kökü; beraat (arınma) ve berat (ayrıcalık belgesi) aynı kökten türer.
M-Y-Z|ar|ayırmak|Arapça m-y-z kökü; temyiz, mümeyyiz, mümtaz ve imtiyaz aynı kökten gelir.
N-F-Z|ar|içe işlemek|Arapça n-f-ḏ kökü; infaz (yerine getirme), nüfuz (etki) ve nafiz aynı kökten türer.
Z-L-M|ar|karanlık; haksızlık|Arapça ẕ-l-m kökü; zulüm, zalim, mazlum ve zulmet (karanlık) aynı kökten gelir.
Ş-R-A|ar|yol açmak, yasa koymak|Arapça ş-r-ʿ kökü; şeriat (yol), şeri, meşru (yasaya uygun) ve teşri aynı kökten türer.
F-T-W|ar|görüş bildirmek|Arapça f-t-w kökü; fetva ve müftü aynı kökten gelir.
F-K-H|ar|derin anlamak|Arapça f-q-h kökü; fıkıh (İslam hukuku) ve fakih aynı kökten türer.
H-D-D|ar|sınır|Arapça ḥ-d-d kökü; had, hudut, tahdit ve mahdut aynı kökten gelir.
T-R-K|ar|bırakmak|Arapça t-r-k kökü; terk, metruk ve mütareke (karşılıklı bırakma) aynı kökten türer.
H-Y-A|ar|biçim, kurul|Arapça h-y-ʾ kökü; heyet (kurul) ve hey'et (gök bilimi) aynı kökten gelir.
K-L-L|ar|bütün|Arapça k-l-l kökü; küll (bütün), külli, külliye ve istiklal aynı kökten türer.
C-M-H|ar|toplanmak|Arapça c-m-h kökü; cumhur (halk), cumhuriyet ve cumhurbaşkanı aynı kökten gelir.
C-L-S|ar|oturmak|Arapça c-l-s kökü; meclis (oturma yeri) ve celse (oturum) aynı kökten türer.
W-Z-R|ar|yük taşımak|Arapça w-z-r kökü; vezir (yükü taşıyan) ve vezaret aynı kökten gelir.
Ḫ-Y-R|ar|iyi; seçmek|Arapça ḫ-y-r kökü; hayır (iyilik), hayırlı, hayrat, ihtiyar (seçme; yaşlı) ve muhtar (seçilmiş) aynı kökten türer. Hayret ve hayran, ḥ-y-r kökünden gelen ayrı bir ailedir.
W-L-Y|ar|yakın olmak, yönetmek|Arapça w-l-y kökü; vali, vilayet, veli, evliya ve mevla aynı kökten gelir.
B-L-D|ar|kent|Arapça b-l-d kökü; belde ve belediye aynı kökten türer.
H-L-L|ar|çözmek; konmak|Arapça ḥ-l-l kökü; helal (çözülmüş, izinli), hal (çözüm), tahlil (çözümleme), mahal ve mahalle aynı kökten gelir.
K-D-Y|ar|hükmetmek|Arapça q-ḏ-y kökü; kadı (yargıç) ve kaza (yargı; ilçe; kader) aynı kökten türer.
vocare|la|çağırmak|Latince vocare "çağırmak"; avukat (yardıma çağrılan), vokal ve provokasyon aynı kökten gelir.
nota|la|işaret|Latince nota "işaret"; nota, not ve noter (yazman) aynı kökten türer.
diploma|el|katlanmış belge|Eski Yunanca díplōma "ikiye katlanmış"; diploma, diplomasi, diplomat ve diplomatik aynı kökten gelir.
consulere|la|danışmak|Latince consulere "danışmak"; konsolos, konsey ve konsültasyon aynı kökten türer.
kolla|el|tutkal|Eski Yunanca kólla "tutkal"; protokol (ilk yapıştırılan yaprak) ve kolaj aynı kökten gelir.
legare|la|göndermek, yasa|Latince legare "göndermek, vekil atamak"; delege ve delegasyon aynı kökten türer. Lejyon ise legere "toplamak" kökünden (legio) gelir.
ferre|la|taşımak|Latince ferre "taşımak"; konferans, transfer ve referans aynı kökten gelir.
portus|la|liman, geçit|Latince portus "liman"; port ve pasaport (liman geçişi) aynı kökten türer.
arkhein|el|yönetmek, ilk olmak|Eski Yunanca árkhein "başta olmak"; monarşi, anarşi, hiyerarşi, oligarşi, arşiv ve patrik aynı kökten gelir.
parabola|el|söz, benzetme|Eski Yunanca parabolḕ "yan yana koyma"; Latince parabola yoluyla parola, parlamento (konuşma yeri) aynı kökten türer.
"""
