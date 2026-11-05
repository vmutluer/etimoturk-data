# -*- coding: utf-8 -*-
"""Korpus 9 — Gastronomi ve mutfak kültürü: yemekler, tatlılar, içecekler, sebze-meyve, mutfak araçları, esnaf."""

WORDS = r"""
# --- Mutfak ve sofra -----------------------------------------------------------------
aşçı|n|tr|aşçı|yemek pişiren|DLT|*aş|
aş|n|tr|aş|yemek|ORH|*aş|
aşevi|n|tr|aş evi|yemek dağıtılan yer|CUM|*aş|
aşure|n|ar|ʿāşūrāʾ|onuncu gün tatlısı|EAT||
mutfak|n|ar|maṭbaḫ|pişirme yeri|EAT|T-B-H|
tabhane|n|ar|ṭabḫ-ḫāne|aş evi|OSM|T-B-H|
ziyafet|n|ar|ḏiyāfa|konuk ağırlama|EAT|D-Y-F|
misafir|n|ar|musāfir|yolcu; konuk|EAT|S-F-R|
köfte|n|fa|kūfte|dövülmüş|OSM||
döner|n|tr|döner|dönerek pişen|MOD|*dön-|
lahmacun|n|ar|laḥm bi-ʿacīn|hamurlu et|MOD||
pilav|n|fa|pilāv|pişmiş pirinç|EAT||
bulgur|n|tr|bulgur|kırılmış buğday|EAT||
börek|n|tr|bügrek|kıvrılmış hamur|EAT||
gözleme|n|tr|gözleme|sacda pişen hamur|OSM|*kör-|
yufka|n|tr|yubka|ince hamur|DLT||
baklava|n|tr?|baklava|katmerli tatlı|OSM||
kadayıf|n|ar|qaṭāʾif|ince tel hamur|OSM||
helva|n|ar|ḥalwā|tatlı|EAT|H-L-W|
helvacı|n|ar|ḥalwā|helva satan|OSM|H-L-W|
halavet|n|ar|ḥalāwa|tatlılık|OSM|H-L-W|
lokum|n|ar|rāḥatu'l-ḥulqūm|boğazın rahatı|OSM19||
muhallebi|n|ar|muhallabiyya|sütlü tatlı|OSM||
sütlaç|n|tr|sütlü aş|sütlü pirinç tatlısı|OSM|*aş|
zerde|n|fa|zarde|sarı tatlı|EAT||
hoşaf|n|fa|ḫoş-āb|hoş su|OSM|āb|
komposto|n|it|composta|bir arada konmuş|OSM19|ponere|
reçel|n|fa|rīçāl|meyve tatlısı|OSM||
pekmez|n|tr|pekmez|üzüm şırası kaynatması|DLT||
pestil|n|el|pastíli|yassı tatlı|OSM||
turşu|n|fa|turşī|ekşi|EAT||
salamura|n|el|salamoúra|tuzlu su|OSM19||la:salmuria>it:salamoia>el:salamoúra>tr:salamura
salça|n|it|salsa|tuzlu sos|OSM19|sal|la:salsa>it:salsa>tr:salça
sos|n|fr|sauce|tuzlu|CUM|sal|la:salsa>fr:sauce>tr:sos
salata|n|it|salata|tuzlanmış|OSM19|sal|
salam|n|it|salame|tuzlanmış et|OSM19|sal|
mayonez|n|fr|mayonnaise|Mahón sosu|CUM||
ketçap|n|en|ketchup|balık sosu|MOD||zh:kê-tsiap>en:ketchup>tr:ketçap
hardal|n|ar|ḫardal|hardal|EAT||
sirke|n|fa|sirke|ekşi sıvı|EAT||
tereyağı|n|tr|tere yağı|taze yağ|OSM||
yağ|n|tr|yag|yağ|ORH||
tuz|n|tr|tuz|tuz|DLT||
baharat|n|ar|bahārāt|kokulu bitkiler|OSM||
tarçın|n|fa|dārçīn|Çin ağacı|EAT||
kekik|n|tr|kekik|kokulu ot|OSM||
nane|n|ar|naʿnaʿ|nane|EAT||
fesleğen|n|el|vasilikón|kral otu|OSM||
roka|n|it|ruca|roka|OSM19||
ıspanak|n|fa|ispanāḫ|ıspanak|EAT||
kabak|n|tr|kabak|kabak|DLT||
hıyar|n|fa|ḫiyār|salatalık|EAT||
sarımsak|n|tr|sarmusak|sarımsak|DLT||
soğan|n|tr|sogun|soğan|DLT||
havuç|n|fa|havīc|sebze|OSM||
turp|n|fa|turb|turp|EAT||
enginar|n|el|ankinára|enginar|OSM||
bamya|n|ar|bāmiya|bamya|OSM||
bezelye|n|it|pisello|küçük bakla|OSM19||
nohut|n|fa|noḫūd|nohut|EAT||
mercimek|n|fa|mercümek|mercimek|EAT||
un|n|tr|un|öğütülmüş tahıl|DLT||
hamur|n|ar|ḫamīr|mayalanmış|EAT|H-M-R|
mahmur|adj|ar|maḫmūr|sersem|OSM|H-M-R|
humar|n|ar|ḫumār|içki sersemliği|OSM|H-M-R|
maya|n|fa|māye|öz; kabartan|EAT||
simit|n|ar|samīd|has un|EAT||
poğaça|n|it|focaccia|ocak ekmeği|OSM||la:focacia>it:focaccia>tr:poğaça
çörek|n|tr|çörek|yuvarlak hamur işi|DLT||
bisküvi|n|fr|biscuit|iki kez pişmiş|OSM19|coquere|la:bis coctus>fr:biscuit>tr:bisküvi
pasta|n|it|pasta|hamur|OSM19|pasta|
pastane|n|it|pasta|pasta evi|CUM|pasta|it:pasta>fa:-ḫāne>tr:pastane
pastacı|n|it|pasta|pasta yapan|CUM|pasta|
pastel|n|fr|pastel|hamur boya|MOD|pasta|
kek|n|en|cake|kek|CUM||
akide|n|ar|ʿaqīda|bağlanmış şeker|OSM|A-K-D|
bonbon|n|fr|bonbon|iyi iyi|CUM||
çikolata|n|it|cioccolata|acı su|OSM19||nah:xocolātl>es:chocolate>it:cioccolata>tr:çikolata
kakao|n|es|cacao|kakao|OSM19||nah:cacahuatl>es:cacao>tr:kakao
vanilya|n|it|vaniglia|küçük kılıf|OSM19||es:vainilla>it:vaniglia>tr:vanilya
karamel|n|fr|caramel|yanık şeker|CUM||
dondurma|n|tr|dondurma|dondurulmuş tatlı|OSM19|*don-|
donmak|v|tr|toŋ-|buz tutmak|DLT|*don-|
limonata|n|it|limonata|limonlu içecek|OSM19||
gazoz|n|fr|gazeuse|gazlı|CUM||
soda|n|it|soda|sodyum karbonat|OSM19||
kefir|n|sl|kefir|Kafkas süt içeceği|CUM||
boza|n|fa|būze|darı içeceği|EAT||
şalgam|n|fa|şalġam|şalgam|EAT||
rakı|n|ar|ʿaraq|ter; damıtık içki|OSM||
bira|n|it|birra|bira|OSM19||
likör|n|fr|liqueur|sıvı|OSM19||
konyak|n|fr|cognac|Cognac kasabası|OSM19||
viski|n|en|whisky|yaşam suyu|CUM||
meyhane|n|fa|mey-ḫāne|şarap evi|EAT|-hāne|
lokanta|n|it|locanda|konaklama yeri|OSM19||
restoran|n|fr|restaurant|güç veren|CUM||
kafe|n|fr|café|kahve evi|MOD||ar:qahwa>tr:kahve>it:caffè>fr:café>tr:kafe
kahvehane|n|ar|qahwa|kahve evi|OSM|-hāne|
kasap|n|ar|qaṣṣāb|kesen|EAT||
bakkal|n|ar|baqqāl|sebzeci|EAT||
şarküteri|n|fr|charcuterie|pişmiş et|MOD||
garson|n|fr|garçon|oğlan|OSM19||
menü|n|fr|menu|küçük liste|CUM||la:minutus>fr:menu>tr:menü
çanak|n|tr|çanak|kap|DLT||
kâse|n|fa|kāse|çanak|EAT||
fincan|n|ar|fincān|küçük kap|EAT||fa:pingān>ar:fincān>tr:fincan
sürahi|n|ar|ṣurāḥī|saf kap|EAT||
ibrik|n|ar|ibrīq|su kabı|EAT||fa:ābrīz>ar:ibrīq>tr:ibrik
tava|n|fa|tābe|kızartma kabı|EAT||
kazan|n|tr|kazgan|büyük kap|DLT||
güveç|n|tr|güveç|toprak kap|OSM||
saç|n|tr|saç|demir levha|DLT||
mangal|n|ar|manqal|taşınan ocak|OSM|N-K-L|
şiş|n|tr|şiş|sivri çubuk|DLT||
meze|n|fa|maze|tat|OSM||
leblebi|n|fa|leblebī|kavrulmuş nohut|OSM||
fıstık|n|ar|fustuq|fıstık|EAT||grc:pistákion>fa:piste>ar:fustuq>tr:fıstık
incir|n|fa|encīr|incir|EAT||
üzüm|n|tr|üzüm|üzüm|DLT||
hurma|n|fa|ḫurmā|hurma|EAT||
nar|n|fa|nār|nar|EAT||
elma|n|tr|alma|elma|DLT||
erik|n|tr|erük|erik|DLT||
şeftali|n|fa|şaftālū|şeftali|EAT||
muz|n|ar|mawz|muz|OSM||
mandalina|n|it|mandarino|mandalina|OSM19||
limon|n|ar|laymūn|limon|EAT||fa:līmū>ar:laymūn>tr:limon
greyfurt|n|en|grapefruit|salkım meyve|MOD||
ananas|n|pt|ananás|ananas|OSM19||tup:nanas>pt:ananás>tr:ananas
çilek|n|tr|çilek|çilek|OSM||
böğürtlen|n|tr|böğürtlen|böğürtlen|OSM||
kavun|n|tr|kagun|kavun|DLT||
dut|n|fa|tūt|dut|EAT||
ayva|n|tr|avya|ayva|DLT||
kuruyemiş|n|tr|kuru yemiş|kurutulmuş meyve|TDK|*ye-|
yemiş|n|tr|yémiş|meyve|ORH|*ye-|
"""

FAMILIES = r"""
*aş|tr|yemek|Orhun Yazıtları'ndaki aş "yemek"; aşçı, aşevi ve sütlaç (sütlü aş) aynı kökten gelir.
*don-|tr|buz tutmak|Eski Türkçe toŋ- "donmak"; donmak ve dondurma aynı kökten türer.
T-B-H|ar|pişirmek|Arapça ṭ-b-ḫ kökü; mutfak (maṭbaḫ: pişirme yeri) ve tabhane aynı kökten gelir.
D-Y-F|ar|konuk olmak|Arapça ḏ-y-f kökü; ziyafet (konuk ağırlama) ile dayf (konuk) aynı kökten gelir; Türkçede bu kökten yalnızca ziyafet yaşamaktadır.
H-L-W|ar|tatlı|Arapça ḥ-l-w kökü; helva, helvacı ve halavet (tatlılık) aynı kökten gelir.
sal|la|tuz|Latince sal "tuz"; salça, sos, salata (tuzlanmış), salam ve salamura aynı kökten türer.
H-M-R|ar|mayalanmak|Arapça ḫ-m-r kökü; hamur (mayalanmış), mahmur ve humar (içki sersemliği) aynı kökten gelir.
coquere|la|pişirmek|Latince coquere "pişirmek"; bisküvi (iki kez pişmiş) aynı kökten gelir.
pasta|it|hamur|Geç Latince pasta "hamur"; pasta, pastane, pastacı ve pastel (hamur boya) aynı kökten türer.
"""
