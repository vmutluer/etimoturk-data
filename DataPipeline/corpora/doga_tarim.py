# -*- coding: utf-8 -*-
"""Korpus 11 — Doğa ve tarım: ekip biçme, hayvancılık, coğrafya, hava, madenler ve yer bilimleri."""

WORDS = r"""
# --- Tarım: Öz Türkçe ------------------------------------------------------------------
tarım|n|tr|tarı-|ekip biçme|DD|*tarı-|
tarla|n|tr|tarıġlaġ|ekilen yer|DLT|*tarı-|
darı|n|tr|tarıġ|ekin; mısır tanesi|ORH|*tarı-|
tarhana|n|fa|tarḫāne|kurutulmuş yoğurtlu çorba|OSM||
çiftlik|n|fa|cuft|çift öküzlük yer|OSM|cuft|
çift|n|fa|cuft|iki; öküz çifti|EAT|cuft|
çiftçi|n|fa|cuft|çift süren|OSM|cuft|
ekin|n|tr|ekin|ekilen|DLT|*ek-|
ekim|n|tr|ekim|ekme işi; ay adı|DD|*ek-|
ekenek|n|tr|ekenek|ekilen tarla|DD|*ek-|
orman|n|tr|orman|sık ağaçlık|EAT||
koru|n|tr|korıġ|korunan ağaçlık|DLT|*koru-|
korumak|v|tr|korı-|esirgemek|DLT|*koru-|
koruma|n|tr|korı-|esirgeme|TDK|*koru-|
korunak|n|tr|korunak|sığınak|DD|*koru-|
çayır|n|tr|çayır|otlak|EAT||
mera|n|ar|marʿā|otlak|OSM|R-A-Y|
riayet|n|ar|riʿāya|gözetme|OSM|R-A-Y|
raiyet|n|ar|raʿiyya|güdülen; halk|EAT|R-A-Y|
reaya|n|ar|raʿāyā|yönetilen halk|OSM|R-A-Y|
yayla|n|tr|yaylaġ|yaz konağı|DLT|*yay|
yay|n|tr|yay|yaz; ilkbahar|ORH|*yay|
kışlak|n|tr|kışlaġ|kış konağı|DLT|*kış|
kış|n|tr|kış|soğuk mevsim|ORH|*kış|
kışla|n|tr|kışlaġ|asker barınağı|OSM|*kış|
sera|n|fr|serre|kapatan|CUM||la:serare>fr:serre>tr:sera
saban|n|tr|saban|toprak yarma aracı|DLT||
tırmık|n|tr|tırmık|toprak tarağı|OSM|*tırma-|
tırmalamak|v|tr|tırmala-|tırnakla çizmek|OSM|*tırma-|
tırmanmak|v|tr|tırman-|tırnaklarla yukarı çıkmak|OSM|*tırma-|
orak|n|tr|orġak|ekin biçme aracı|DLT|*or-|
ormak|v|tr|or-|biçmek|DLT|*or-|
tırpan|n|el|drepánē|biçme aracı|OSM||
kazma|n|tr|kazma|toprak kazma aracı|OSM|*kaz-|
kazmak|v|tr|kaz-|toprağı oymak|DLT|*kaz-|
kazı|n|tr|kazı|kazma işi|DD|*kaz-|
harman|n|fa|ḫarman|dövülen ekin|EAT||
değirmen|n|tr|tegirmen|öğütme yapısı|DLT|*tegir-|
değirmi|adj|tr|tegirmi|yuvarlak|DLT|*tegir-|
sap|n|tr|sap|bitki gövdesi|DLT||
saman|n|tr|saman|kuru sap|DLT||
ot|n|tr|ot|yeşil bitki|ORH||
otlak|n|tr|otlaġ|hayvan otlatılan yer|DLT||
çimen|n|fa|çemen|yeşillik|EAT||
yonca|n|tr|yorınça|yem bitkisi|DLT||
arpa|n|tr|arpa|tahıl|DLT||
buğday|n|tr|buġday|tahıl|DLT||
çavdar|n|fa|cawdār|çavdar|OSM||
mısır|n|ar|miṣr|Mısır ülkesi; mısır bitkisi|OSM||
çeltik|n|fa|çaltūk|kabuklu pirinç|OSM||
susam|n|ar|simsim|yağlı tohum|EAT||
keten|n|ar|kattān|lifli bitki|EAT||
kenevir|n|el|kannábouri|lifli bitki|EAT||
tütün|n|tr|tütün|duman; tütün bitkisi|OSM|*tüt-|
ipek|n|tr|yipek|ipek|DLT||
yün|n|tr|yuŋ|koyun kılı|DLT||
deri|n|tr|teri|hayvan kabuğu|DLT||
post|n|fa|pōst|tüylü deri|EAT||
kuzu|n|tr|kuzı|koyun yavrusu|DLT||
keçi|n|tr|keçi|keçi|DLT||
oğlak|n|tr|oġlak|keçi yavrusu|DLT|*oğul|
oğul|n|tr|oġul|erkek çocuk|ORH|*oğul|
oğlan|n|tr|oġlan|çocuklar; erkek çocuk|DLT|*oğul|
inek|n|tr|ingek|dişi sığır|DLT||
öküz|n|tr|öküz|erkek sığır|DLT||
boğa|n|tr|buka|damızlık erkek sığır|DLT||
kısrak|n|tr|kısrak|dişi at|DLT||
aygır|n|tr|adġır|erkek at|DLT||
tay|n|tr|tay|at yavrusu|DLT||
eşek|n|tr|eşgek|eşek|DLT||
katır|n|tr|katır|at ile eşek melezi|DLT||
deve|n|tr|tebe|deve|ORH||
tavuk|n|tr|takıġu|kümes hayvanı|DLT||
horoz|n|fa|ḫurūs|erkek tavuk|EAT||
hindi|n|ar|hindī|Hint'e ilişkin; hindi kuşu|OSM||
ördek|n|tr|ördek|su kuşu|DLT||
kaz|n|tr|kaz|su kuşu|DLT||
güvercin|n|tr|kögürçgün|güvercin|DLT||
arı|n|tr|arı|bal yapan böcek|DLT||
bal|n|tr|bal|arı ürünü|DLT||
kurt|n|tr|kurt|yırtıcı hayvan; böcek|ORH||
ayı|n|tr|adıġ|ayı|DLT||
tilki|n|tr|tilkü|tilki|DLT||
tavşan|n|tr|tabışġan|tavşan|DLT||
geyik|n|tr|keyik|yabani hayvan|DLT||
karaca|n|tr|karaca|küçük geyik|OSM||
yaban|n|fa|yābān|çöl, ıssız yer|EAT||
çöl|n|tr|çöl|kurak alan|EAT||
tepe|n|tr|töpü|yükselti|DLT||
vadi|n|ar|wādī|akarsu yatağı|EAT||
yamaç|n|tr|yamaç|dağ yanı|OSM||
bayır|n|tr|bayır|yokuş|OSM||
dere|n|fa|darra|küçük akarsu|EAT||
ırmak|n|tr|ırmak|büyük akarsu|DLT||
göl|n|tr|köl|durgun su|ORH||
gölet|n|tr|gölet|küçük göl|DD||
bataklık|n|tr|batak|çamurlu alan|OSM|*bat-|
kaynak|n|tr|kaynak|su çıkışı; köken|OSM|*kayna-|
kaynamak|v|tr|kayna-|fokurdamak|DLT|*kayna-|
kaynaşmak|v|tr|kaynaş-|birbirine karışmak|OSM|*kayna-|
pınar|n|tr|bıŋar|kaynak|DLT||
çağlayan|n|tr|çağla-|şelale|TDK||
şelale|n|ar|şallāla|çağlayan|OSM19||
kaya|n|tr|kaya|büyük taş|DLT||
kum|n|tr|kum|ince taş|DLT||
çakıl|n|tr|çakıl|küçük yuvarlak taş|OSM||
kil|n|fa|gil|balçık|EAT||
maden|n|ar|maʿdin|yer altı kaynağı|EAT|A-D-N|
altın|n|tr|altun|değerli maden|ORH||
gümüş|n|tr|kümüş|değerli maden|ORH||
bakır|n|tr|bakır|kızıl maden|DLT||
demir|n|tr|temir|sert maden|ORH||
kurşun|n|tr|korġaşın|yumuşak maden|DLT||
kalay|n|tr|kalay|beyaz maden|OSM||
çinko|n|it|zinco|çinko|OSM19||
cıva|n|fa|jīve|akışkan maden|EAT||
kömür|n|tr|kömür|yanıcı kara madde|DLT||
petrol|n|fr|pétrole|taş yağı|OSM19|petra|la:petra oleum>fr:pétrole>tr:petrol
petrokimya|n|fr|pétrochimie|petrol kimyası|MOD|petra|
gaz|n|fr|gaz|kaos|OSM19||
hava|n|ar|hawāʾ|boşluk; yel|EAT||
yel|n|tr|yel|rüzgâr|DLT|*yel|
yelken|n|tr|yelken|yel tutan bez|DLT|*yel|
yelpaze|n|fa|yel-bāze|yel oyuncağı|OSM|*yel|
bulut|n|tr|bulıt|bulut|DLT||
kar|n|tr|kar|kar|DLT||
dolu|n|tr|tolı|buz taneleri|DLT||
kırağı|n|tr|kıraġu|ince don|DLT||
duman|n|tr|tuman|sis; duman|DLT||
yıldırım|n|tr|yıldırım|gök çakması|DLT|*yal-|
yalaz|n|tr|yalaz|alev|DLT|*yal-|
yalım|n|tr|yalın|alev|DLT|*yal-|
gök|n|tr|kök|gökyüzü; mavi|ORH||
güneş|n|tr|künäş|gün ışığı|DLT|*kün|
gündüz|n|tr|küntüz|günün aydınlık bölümü|ORH|*kün|
gezegen|n|tr|gezegen|gezen yıldız|DD|*gez-|
gezmek|v|tr|kez-|dolaşmak|DLT|*gez-|
gezi|n|tr|gezi|gezme|DD|*gez-|
gezgin|n|tr|gezgin|gezen kişi|DD|*gez-|
uydu|n|tr|uydu|uyan gök cismi|DD|*uy-|
uymak|v|tr|ud-|izlemek|ORH|*uy-|
uyum|n|tr|uyum|uygunluk|DD|*uy-|
evren|n|tr|evren|dönen; kâinat|DD|*evir-|
evrim|n|tr|evrim|dönüşüm|DD|*evir-|
evirmek|v|tr|evir-|döndürmek|DLT|*evir-|
iklim|n|ar|iqlīm|eğim; bölge|EAT||grc:klíma>ar:iqlīm>tr:iklim
mevsim|n|ar|mawsim|belirli zaman|EAT|W-S-M|
mevsimlik|adj|ar|mawsim|mevsime bağlı|CUM|W-S-M|
hasat|n|ar|ḥaṣād|biçme|OSM|H-S-D|
hasıl|n|ar|ḥāṣil|elde edilen|EAT|H-S-L|
mahsul|n|ar|maḥṣūl|elde edilen ürün|EAT|H-S-L|
tahsil|n|ar|taḥṣīl|elde etme; öğrenim|OSM|H-S-L|
tahsildar|n|fa|taḥṣīl-dār|vergi toplayan|OSM|H-S-L|ar:taḥṣīl>fa:taḥṣīl-dār>tr:tahsildar
hasılat|n|ar|ḥāṣilāt|gelirler|OSM19|H-S-L|
ürün|n|tr|ürün|üretilen|DD|*ür-|
bereket|n|ar|baraka|bolluk|EAT|B-R-K|
mübarek|adj|ar|mubārak|kutlu|EAT|B-R-K|
tebrik|n|ar|tabrīk|kutlama|OSM|B-R-K|
kuraklık|n|tr|kurak|susuzluk|TDK|*kuru-|
kurak|adj|tr|kurġak|susuz|DLT|*kuru-|
kurumak|v|tr|kurı-|suyunu kaybetmek|DLT|*kuru-|
kıtlık|n|tr|kıt|yokluk|OSM||
sel|n|ar|sayl|taşkın|EAT||
afet|n|ar|āfa|büyük yıkım|EAT||
deprem|n|tr|deprem|yer sarsıntısı|DD|*tepre-|
depremek|v|tr|tepre-|sarsılmak|DLT|*tepre-|
zelzele|n|ar|zalzala|sarsıntı|EAT||
volkan|n|fr|volcan|ateş tanrısı Vulcanus|OSM19||la:Vulcanus>it:vulcano>fr:volcan>tr:volkan
yanardağ|n|tr|yanar dağ|volkan|DD|*yan-|
lav|n|fr|lave|akan|CUM||
ziraat|n|ar|zirāʿa|ekip biçme|OSM|Z-R-A|
zürra|n|ar|zurrāʿ|çiftçiler|OSM|Z-R-A|
mezru|adj|ar|mazrūʿ|ekilmiş|OSM|Z-R-A|
coğrafya|n|ar|coġrāfiyā|yer yazımı|OSM|gē|grc:geōgraphía>ar:coġrāfiyā>tr:coğrafya
jeoloji|n|fr|géologie|yer bilgisi|OSM19|gē|
geometri|n|fr|géométrie|yer ölçümü|OSM19|gē|grc:geōmetría>fr:géométrie>tr:geometri
jeofizik|n|fr|géophysique|yer fiziği|MOD|gē|
jeopolitik|n|fr|géopolitique|yer siyaseti|MOD|gē|
kozmos|n|fr|cosmos|düzen; evren|CUM|kosmos|
kozmik|adj|fr|cosmique|evrensel|MOD|kosmos|
kozmetik|n|fr|cosmétique|süsleyen|CUM|kosmos|
kozmopolit|adj|fr|cosmopolite|dünya yurttaşı|CUM|kosmos|
kozmoloji|n|fr|cosmologie|evren bilgisi|MOD|kosmos|
astronomi|n|fr|astronomie|yıldız yasası|OSM19|astēr|grc:astronomía>fr:astronomie>tr:astronomi
astroloji|n|fr|astrologie|yıldız bilgisi|OSM19|astēr|
astronot|n|fr|astronaute|yıldız gemicisi|MOD|astēr|
asteroit|n|fr|astéroïde|yıldızımsı|MOD|astēr|
hidrojen|n|fr|hydrogène|su doğuran|OSM19|hydōr|
hidrolik|adj|fr|hydraulique|su borusu|CUM|hydōr|
hidroelektrik|n|fr|hydroélectrique|su gücü|MOD|hydōr|
hidrofor|n|fr|hydrophore|su taşıyan|MOD|hydōr|
klor|n|fr|chlore|yeşil sarı|OSM19|khlōros|
klorofil|n|fr|chlorophylle|yeşil yaprak|CUM|khlōros|
kloroform|n|fr|chloroforme|klorlu|OSM19|khlōros|
oksijen|n|fr|oxygène|ekşi doğuran|OSM19|genus|
azot|n|fr|azote|yaşamsız|OSM19||
karbon|n|fr|carbone|kömür|OSM19||la:carbo>fr:carbone>tr:karbon
mineral|n|fr|minéral|madene ilişkin|CUM||
kristal|n|fr|cristal|buz|OSM19||grc:krýstallos>la:crystallum>fr:cristal>tr:kristal
fosil|n|fr|fossile|kazılmış|CUM||la:fossilis>fr:fossile>tr:fosil
ekoloji|n|fr|écologie|yuva bilgisi|MOD|oikos|
ekonomi|n|fr|économie|ev yönetimi|OSM19|oikos|grc:oikonomía>fr:économie>tr:ekonomi
ekümenik|adj|fr|œcuménique|yerleşik dünyaya ilişkin|MOD|oikos|
flora|n|fr|flore|çiçek tanrıçası|MOD|flos|
floresan|adj|fr|fluorescent|akışkan ışıltılı|MOD||
fauna|n|fr|faune|kır tanrısı Faunus|MOD||
botanik|n|fr|botanique|bitkilere ilişkin|OSM19||grc:botanikḕ>fr:botanique>tr:botanik
zooloji|n|fr|zoologie|hayvan bilgisi|OSM19|zōon|
zodyak|n|fr|zodiaque|hayvan çemberi|CUM|zōon|
hayvanat|n|ar|ḥaywānāt|hayvanlar|OSM|H-Y-Y|
"""

FAMILIES = r"""
*tarı-|tr|ekmek, ekip biçmek|Eski Türkçe tarı- "ekmek"; darı (tarıġ: ekin), tarla (tarıġlaġ: ekilen yer) ve Dil Devrimi türetmesi tarım aynı kökten gelir.
cuft|fa|çift, öküz çifti|Farsça cuft "çift"; çift, çiftçi (çift süren) ve çiftlik aynı kökten türer.
*koru-|tr|esirgemek|Eski Türkçe korı- "korumak"; koru (korunan ağaçlık), korumak, koruma ve korunak aynı kökten gelir.
R-A-Y|ar|gütmek, gözetmek|Arapça r-ʿ-y kökü; mera (otlak), riayet (gözetme), raiyet ve reaya (güdülen halk) aynı kökten türer. Riya, mürai ve rüya, r-ʾ-y "görmek" kökünden gelen ayrı bir ailedir.
*yay|tr|yaz, ilkbahar|Eski Türkçe yay "yaz"; yayla (yaz konağı) aynı kökten gelir; Türk dünyasında yaz anlamı sürer.
*kış|tr|soğuk mevsim|Eski Türkçe kış; kışlak (kış konağı) ve kışla (asker barınağı) aynı kökten türer.
*tırma-|tr|tırnakla çizmek|Eski Türkçe tırŋak "tırnak" ile akraba tırma- gövdesi; tırmık, tırmalamak ve tırmanmak aynı kökten gelir.
*or-|tr|biçmek|Eski Türkçe or- "biçmek"; orak (biçme aracı) ve ormak aynı kökten türer.
*kaz-|tr|kazmak|Eski Türkçe kaz- "kazmak"; kazma, kazı ve kazmak aynı kökten gelir.
*tegir-|tr|döndürmek|Eski Türkçe tegir- "döndürmek"; değirmen (döndürülen) ve değirmi (yuvarlak) aynı kökten türer.
*oğul|tr|çocuk|Orhun Yazıtları'ndaki oġul "çocuk, oğul"; oğlan (çoğul biçimi) ve oğlak (keçi yavrusu) aynı kökten gelir.
*kayna-|tr|fokurdamak|Eski Türkçe kayna- "kaynamak"; kaynak (su çıkışı; köken), kaynamak ve kaynaşmak aynı kökten türer.
petra|el|taş|Eski Yunanca pétra "kaya"; Latince yoluyla petrol (taş yağı) ve petrokimya aynı kökten gelir.
*yel|tr|rüzgâr|Eski Türkçe yel "rüzgâr"; yelken (yel tutan) ve Farsça bileşik yelpaze aynı kökten türer.
*yal-|tr|alevlenmek|Eski Türkçe yal- "alevlenmek"; yalaz, yalım (alev) ve yıldırım aynı kökten gelir.
*kün|tr|gün, güneş|Orhun Yazıtları'ndaki kün "gün, güneş"; güneş ve gündüz aynı kökten türer.
*gez-|tr|dolaşmak|Eski Türkçe kez- "dolaşmak"; gezmek, gezi, gezgin ve gezegen (gezen yıldız) aynı kökten gelir.
*uy-|tr|izlemek|Eski Türkçe ud- "izlemek"; uymak, uyum ve uydu (gezegeni izleyen) aynı kökten türer.
*evir-|tr|döndürmek|Eski Türkçe evir- "çevirmek"; evren (dönen gök), evrim (dönüşüm) ve evirmek aynı kökten gelir.
W-S-M|ar|işaretlemek|Arapça w-s-m kökü; mevsim (belirlenmiş zaman) ve mevsimlik aynı kökten türer.
H-S-D|ar|biçmek|Arapça ḥ-ṣ-d kökü; hasat (biçme) aynı kökten gelir.
H-S-L|ar|elde etmek|Arapça ḥ-ṣ-l kökü; hasıl, mahsul (ürün), tahsil (elde etme; öğrenim), tahsildar ve hasılat aynı kökten türer.
B-R-K|ar|kutlu olmak|Arapça b-r-k kökü; bereket, mübarek ve tebrik aynı kökten gelir.
*kuru-|tr|kurumak|Eski Türkçe kurı- "kurumak"; kurak, kurumak ve kuraklık aynı kökten türer.
*tepre-|tr|sarsılmak|Eski Türkçe tepre- "kımıldamak"; depremek ve Dil Devrimi türetmesi deprem aynı kökten gelir.
Z-R-A|ar|ekmek|Arapça z-r-ʿ kökü; ziraat, zürra (çiftçiler) ve mezru (ekilmiş) aynı kökten türer.
gē|el|yer|Eski Yunanca gê "yer"; coğrafya (Arapça yoluyla), jeoloji, geometri, jeofizik ve jeopolitik aynı kökten gelir.
kosmos|el|düzen, evren|Eski Yunanca kósmos "düzen, süs, evren"; kozmos, kozmik, kozmetik (süsleyen), kozmopolit ve kozmoloji aynı kökten türer.
astēr|el|yıldız|Eski Yunanca astḕr "yıldız"; astronomi, astroloji, astronot ve asteroit aynı kökten gelir.
hydōr|el|su|Eski Yunanca hýdōr "su"; hidrojen, hidrolik, hidroelektrik ve hidrofor aynı kökten türer.
khlōros|el|yeşil sarı|Eski Yunanca khlōrós "yeşil"; klor, klorofil ve kloroform aynı kökten gelir.
oikos|el|ev|Eski Yunanca oîkos "ev"; ekonomi (ev yönetimi), ekoloji (yuva bilgisi) ve ekümenik aynı kökten türer.
flos|la|çiçek|Latince flos "çiçek"; flora aynı kökten gelir.
zōon|el|canlı|Eski Yunanca zôion "canlı, hayvan"; zooloji ve zodyak (hayvan çemberi) aynı kökten türer.
"""
