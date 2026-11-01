# -*- coding: utf-8 -*-
"""Korpus 21 — Coğrafya, yer şekilleri, iklim ve gökyüzü: dağ-ova-kıyı sözcükleri, hava olayları, gök cisimleri,
yönler, uzaklık ve ölçü birimleri, yer adı ögeleri; Öz Türkçe kökler, Arapça üçlü kökler ve Batı kökenli yer bilimi terimleri."""

WORDS = r"""
# --- Yer şekilleri: Öz Türkçe ------------------------------------------------------------
doruk|n|tr|doruk|en yüksek nokta|OSM||
yar|n|tr|yar|uçurum, dik kıyı|DLT|*yar-|
yarık|n|tr|yarık|yarılmış yer|DLT|*yar-|
yalıyar|n|tr|yalı+yar|dik deniz kıyısı|DD|*yar-|
falez|n|fr|falaise|dik kıyı|CUM||
çukur|n|tr|çukur|oyuk yer|DLT||
çukurluk|n|tr|çukur|çukur alan|TDK||
bozkır|n|tr|boz+kır|ağaçsız düzlük|OSM|*kır|
step|n|fr|steppe|ağaçsız düzlük|CUM||ru:step'>fr:steppe>tr:step
kırsal|adj|tr|kır|kıra ilişkin|DD|*kır|
kırlık|n|tr|kır|kır alanı|TDK|*kır|
kıraç|adj|tr|kır|verimsiz, kuru toprak|OSM|*kır|
funda|n|el|phoúnta|süpürge çalısı|OSM||
fundalık|n|el|phoúnta|funda kaplı yer|OSM19||
dikenlik|n|tr|tiken|dikenli yer|OSM||
kayalık|n|tr|kaya|kaya kaplı yer|OSM|*kaya|
kayaç|n|tr|kaya|yer kabuğunu oluşturan taş kütlesi|DD|*kaya|
balçık|n|tr|balçık|yapışkan çamur|DLT||
çamur|n|tr|çamur|ıslak toprak|EAT||
çamurlu|adj|tr|çamur|çamur kaplı|OSM||
tın|n|tr|tın|verimli toprak|TDK||
tınlı|adj|tr|tın|verimli topraklı|TDK||
humus|n|fr|humus|toprak|CUM||la:humus>fr:humus>tr:humus
in|n|tr|in|hayvan yuvası; mağara|DLT||
kovuk|n|tr|kovuk|oyuk, boşluk|DLT||
kanyon|n|fr|canyon|derin vadi|MOD||es:cañón>fr:canyon>tr:kanyon
plato|n|fr|plateau|yüksek düzlük|CUM||
baraj|n|fr|barrage|set|CUM||
nehir|n|ar|nahr|ırmak|EAT||
fay|n|fr|faille|kırık|MOD||
krater|n|fr|cratère|karıştırma kabı; yanardağ ağzı|CUM||grc:kratḗr>fr:cratère>tr:krater
dağlık|adj|tr|taġ|dağı çok|OSM|*tağ|
dağcı|n|tr|taġ|dağa tırmanan|TDK|*tağ|
dağcılık|n|tr|taġ|dağa tırmanma sporu|TDK|*tağ|
dağlı|n|tr|taġ|dağ köylüsü|EAT|*tağ|
sıradağ|n|tr|sıra+taġ|dağ dizisi|DD|*tağ|
tepelik|n|tr|töpü|tepeli alan|OSM|*töpü|
tepecik|n|tr|töpü|küçük tepe|OSM|*töpü|
tümsek|n|tr|tümsek|küçük kabarıklık|OSM||
ovalık|n|tr|ova|ova alanı|TDK||
yaylacı|n|tr|yaylaġ|yaylaya çıkan|OSM|*yay|
yaylacılık|n|tr|yaylaġ|yaylaya çıkma geleneği|TDK|*yay|
oyuk|n|tr|oyuk|oyulmuş yer|DLT|*oy-|
oyuntu|n|tr|oy-|oyulmuş iz|TDK|*oy-|
obruk|n|tr|obruk|çökme çukuru|OSM||
düden|n|tr|düden|suyun yer altına battığı delik|TDK||
dolin|n|fr|doline|çökme çukuru|MOD||sl:dolina>fr:doline>tr:dolin
karst|n|de|Karst|kireçtaşı arazisi|MOD||sl:Kras>de:Karst>tr:karst
traverten|n|fr|travertin|Tivoli taşı|MOD||la:tiburtinus>it:travertino>fr:travertin>tr:traverten
sarkıt|n|tr|sark-|tavandan sarkan kireç oluşumu|DD||
dikit|n|tr|dik-|tabandan yükselen kireç oluşumu|DD|*dik-|
çatlak|n|tr|çatla-|yarılmış yer|OSM||
çatak|n|tr|çat-|iki derenin birleştiği yer|OSM|*çat-|
çatal|n|tr|çat-|iki kola ayrılan|DLT|*çat-|
koyak|n|tr|koy|vadi|DD||
derecik|n|fa|darre|küçük dere|OSM||
belen|n|tr|belen|dağ geçidi, bel|EAT||
derbent|n|fa|darband|geçit kapısı|OSM||
bent|n|fa|band|bağ; su seti|EAT||
set|n|ar|sadd|engel, su bendi|EAT|S-D-D|
sedde|n|ar|sadda|set, engel|OSM|S-D-D|
kuytu|adj|tr|kuytu|rüzgârsız, gizli yer|OSM||
delta|n|fr|delta|ırmak ağzı çatalı|CUM||grc:délta>fr:delta>tr:delta
göze|n|tr|köz|pınar|DLT||
kaynarca|n|tr|kayna-|sıcak su kaynağı|OSM|*kayna-|
kaplıca|n|tr|kaplu+ılıca|sıcak su hamamı|EAT||
ılıca|n|tr|ılı-|sıcak su kaynağı|DLT|*ılı-|
ılıman|adj|tr|ılı-|ne sıcak ne soğuk|DD|*ılı-|
ılımak|v|tr|ılı-|ılık duruma gelmek|DLT|*ılı-|
çermik|n|hy|ǰermuk|kaplıca|OSM||
memba|n|ar|manbaʿ|kaynak|OSM||
havza|n|ar|ḥawḍa|su toplama alanı|OSM19||
birikinti|n|tr|birik-|birikmiş su|OSM||
sulak|adj|tr|sub|suyu bol|DLT|*sub|
suyolu|n|tr|sub|su kanalı|OSM|*sub|
subasar|n|tr|sub|taşkın ovası|DD|*sub|
sulu|adj|tr|sub|suyu çok|DLT|*sub|
susuz|adj|tr|sub|suyu olmayan|DLT|*sub|
ark|n|tr|arık|su yolu, kanal|DLT|*arık|
arık|n|tr|arık|su kanalı|DLT|*arık|
akak|n|tr|ak-|akarsu yatağı|DD|*ak-|
akaç|n|tr|ak-|suyu akıtan oluk|DD|*ak-|
savak|n|tr|sav-|su bendi kapağı|OSM||
çavlan|n|tr|çavla-|büyük çağlayan|DD||
girdap|n|fa|gerdāb|dönen su|EAT||
anafor|n|el|anaphorá|ters akıntı|OSM||
burgaç|n|tr|bur-|girdap|DD||
dalgakıran|n|tr|dalga+kır-|dalgaları kıran set|CUM||
köpük|n|tr|köpük|köpük|DLT||
met|n|ar|madd|denizin kabarması|OSM|M-D-D|
dip|n|tr|tüp|en alt|DLT||
derinlik|n|tr|teriŋ|derin olma|OSM|*teriŋ|
derinleşmek|v|tr|teriŋ|derin duruma gelmek|TDK|*teriŋ|
sığlık|n|tr|sığ|sığ yer|OSM||
turba|n|fr|tourbe|çürümüş bitki tortusu|CUM||
çayırlık|n|tr|çayır|çayır alanı|OSM||
çimenlik|n|fa|çaman|çimen kaplı yer|OSM||
söğütlük|n|tr|sögüt|söğüt ağaçlığı|OSM||
ormanlık|n|tr|orman|orman kaplı|OSM||
koruluk|n|tr|korıġ|küçük orman|OSM|*koru-|
yeşillik|n|tr|yaşıl|yeşil alan|OSM||
resif|n|fr|récif|kayalık sığlık|MOD||ar:raṣīf>es:arrecife>fr:récif>tr:resif
lagün|n|fr|lagune|deniz kulağı|MOD||la:lacuna>it:laguna>fr:lagune>tr:lagün
kumul|n|tr|kum|kum tepesi|DD|*kum|
kumluk|n|tr|kum|kum kaplı alan|OSM|*kum|
kumlu|adj|tr|kum|kumu çok|DLT|*kum|
çakıllı|adj|tr|çakıl|çakıl kaplı|OSM||
çakıllık|n|tr|çakıl|çakıl alanı|OSM||
adacık|n|tr|ada|küçük ada|OSM|*ada|
takımada|n|tr|takım+ada|ada topluluğu|DD|*ada|
atol|n|fr|atoll|mercan adası|MOD||
denizaşırı|adj|tr|teŋiz|deniz ötesinde|DD|*teŋiz|
denizel|adj|tr|teŋiz|denize ilişkin|DD|*teŋiz|
kıtasal|adj|ar|qiṭʿa|kıtaya ilişkin|DD|K-T-A|
anakara|n|tr|ana+kara|kıta|DD||
karasal|adj|tr|kara|karaya ilişkin|DD||
moren|n|fr|moraine|buzul taş yığını|MOD||
buzdağı|n|tr|buz|yüzen buz kütlesi|DD|*buz|
aysberg|n|en|iceberg|buz dağı|MOD||
kartopu|n|tr|kar|yuvarlanmış kar|OSM|*kar|
karlı|adj|tr|kar|kar kaplı|DLT|*kar|
karlık|n|tr|kar|kar kuyusu|OSM|*kar|
çığ|n|tr|çığ|kayan kar kütlesi|OSM||
tipi|n|tr|tipi|kar fırtınası|OSM||
boran|n|tr|boraġan|fırtına|EAT||
don|n|tr|toŋ|buz tutma, ayaz|DLT|*don-|
ayaz|n|tr|ayas|açık ve soğuk hava|DLT||
kutup|n|ar|quṭb|eksen ucu; önder|EAT||
kutupsal|adj|ar|quṭb|kutba ilişkin|DD||
tayga|n|sl|tayga|kuzey iğne yapraklı ormanı|MOD||
savan|n|fr|savane|tropikal otlak|MOD||es:sabana>fr:savane>tr:savan
pampa|n|es|pampa|Güney Amerika bozkırı|MOD||
fiyort|n|fr|fjord|buzul koyu|MOD||
# --- Yanardağ, deprem, yer bilimi ---------------------------------------------------------
magma|n|fr|magma|erimiş kaya|MOD||grc:mágma>fr:magma>tr:magma
kaldera|n|es|caldera|kazan; çökmüş yanardağ ağzı|MOD||la:caldaria>es:caldera>tr:kaldera
püskürmek|v|tr|püskür-|fışkırmak|OSM||
püskürük|adj|tr|püskür-|yanardağdan çıkmış|DD||
tüf|n|fr|tuf|yanardağ külü taşı|MOD||la:tofus>it:tufo>fr:tuf>tr:tüf
bazalt|n|fr|basalte|koyu volkanik kaya|MOD||la:basaltes>fr:basalte>tr:bazalt
andezit|n|fr|andésite|And Dağları taşı|MOD||
obsidyen|n|fr|obsidienne|volkan camı|MOD||la:obsidianus>fr:obsidienne>tr:obsidyen
volkanik|adj|fr|volcanique|yanardağa ilişkin|CUM|vulcanus|
vulkanoloji|n|fr|volcanologie|yanardağ bilimi|MOD|vulcanus|
sarsıntı|n|tr|sars-|sarsılma|OSM|*sars-|
sarsmak|v|tr|sars-|sallamak|EAT|*sars-|
sarsılmak|v|tr|sars-|sallanmak|EAT|*sars-|
artçı|n|tr|art|sonradan gelen sarsıntı|DD||
tsunami|n|ja|tsunami|liman dalgası|NEW||
heyelan|n|ar|hayalān|toprak kayması|OSM19||
göçük|n|tr|köç-|çökmüş yer|OSM|*köç-|
çökme|n|tr|çök-|çökme işi|OSM|*çök-|
çöküntü|n|tr|çök-|çökmüş alan|DD|*çök-|
çökel|n|tr|çök-|dibe çöken madde|DD|*çök-|
çökelti|n|tr|çök-|tortu|DD|*çök-|
kayma|n|tr|kay-|kayma işi|OSM|*kay-|
kaygan|adj|tr|kay-|kolay kayan|OSM|*kay-|
erozyon|n|fr|érosion|aşınma|MOD||la:erosio>fr:érosion>tr:erozyon
aşınma|n|tr|aşın-|yıpranma|TDK|*aşın-|
aşınmak|v|tr|aşın-|yıpranmak|OSM|*aşın-|
aşındırmak|v|tr|aşın-|yıpratmak|OSM|*aşın-|
tortu|n|tr|tort|dibe çöken|DLT|*tort|
tortul|adj|tr|tort|tortudan oluşmuş|DD|*tort|
alüvyon|n|fr|alluvion|akarsu birikintisi|MOD||la:alluvio>fr:alluvion>tr:alüvyon
lös|n|de|Löss|rüzgâr tortusu|MOD||
kumtaşı|n|tr|kum+taş|kumdan oluşmuş taş|DD|*taş|
kireçtaşı|n|tr|kireç+taş|kalker|DD|*taş|
çakmaktaşı|n|tr|çakmak+taş|kıvılcım taşı|OSM|*taş|
taşlı|adj|tr|taş|taşı çok|DLT|*taş|
taşlaşmak|v|tr|taş|taş kesilmek|OSM|*taş|
taşıl|n|tr|taş|fosil|DD|*taş|
kireç|n|fa|kīreç|kireç|EAT||
kireçli|adj|fa|kīreç|kireç içeren|OSM||
alçı|n|tr|alçu|kalsiyum sülfat|EAT||
alçıtaşı|n|tr|alçu+taş|jips|DD|*taş|
jips|n|fr|gypse|alçıtaşı|MOD||grc:gýpsos>la:gypsum>fr:gypse>tr:jips
kuvars|n|fr|quartz|silis minerali|MOD||de:Quarz>fr:quartz>tr:kuvars
mika|n|fr|mica|yaprak yapılı mineral|MOD||la:mica>fr:mica>tr:mika
feldspat|n|de|Feldspat|tarla taşı|MOD||
şist|n|fr|schiste|yapraklı kaya|MOD||grc:skhistós>fr:schiste>tr:şist
gnays|n|de|Gneis|başkalaşım kayası|MOD||
killi|adj|fa|gil|kil içeren|OSM||
marn|n|fr|marne|kireçli kil|MOD||
linyit|n|fr|lignite|odun kömürü|MOD||la:lignum>fr:lignite>tr:linyit
antrasit|n|fr|anthracite|parlak kömür|MOD||grc:ánthrax>fr:anthracite>tr:antrasit
tabakalı|adj|ar|ṭabaqa|katmanlı|OSM||
katmanlı|adj|tr|kat|katmanı olan|DD|*kat-|
fosilleşmek|v|fr|fossile|taşıl olmak|MOD||
paleontoloji|n|fr|paléontologie|eski varlıklar bilimi|MOD||
petrografi|n|fr|pétrographie|kaya betimleme|MOD|petra|
mineraloji|n|fr|minéralogie|mineral bilimi|CUM||
jeodezi|n|fr|géodésie|yer bölme|MOD|gē|
jeolog|n|fr|géologue|yer bilimci|CUM|gē|
jeolojik|adj|fr|géologique|yer bilimine ilişkin|CUM|gē|
jeokimya|n|fr|géochimie|yer kimyası|MOD|gē|
jeomorfoloji|n|fr|géomorphologie|yer şekilleri bilimi|MOD|gē|
jeotermal|adj|fr|géothermal|yer ısısı|MOD|gē|
sismik|adj|fr|sismique|sarsıntıya ilişkin|MOD|seismos|
sismograf|n|fr|sismographe|sarsıntı yazıcı|MOD|seismos|
sismoloji|n|fr|sismologie|deprem bilimi|MOD|seismos|
sismolog|n|fr|sismologue|deprem bilimci|MOD|seismos|
episantr|n|fr|épicentre|üst merkez|MOD||
magnitüd|n|fr|magnitude|büyüklük|MOD||
tektonik|adj|fr|tectonique|yapıya ilişkin|MOD||grc:tektonikós>fr:tectonique>tr:tektonik
hidrografi|n|fr|hydrographie|su betimleme|MOD|hydōr|
hidroloji|n|fr|hydrologie|su bilimi|MOD|hydōr|
hidrolojik|adj|fr|hydrologique|su bilimine ilişkin|MOD|hydōr|
oşinografi|n|fr|océanographie|okyanus betimleme|MOD|graphein|
kartografya|n|fr|cartographie|harita çizimi|MOD|graphein|
kartograf|n|fr|cartographe|harita çizen|MOD|graphein|
topografya|n|fr|topographie|yer betimleme|CUM|topos|grc:topographía>fr:topographie>tr:topografya
topoğraf|n|fr|topographe|arazi ölçen|CUM|topos|
ekosistem|n|fr|écosystème|çevre dizgesi|MOD|oikos|
ekolojik|adj|fr|écologique|çevre bilimine ilişkin|MOD|oikos|
biyom|n|fr|biome|yaşam birliği|MOD|bios|
habitat|n|fr|habitat|yaşama yeri|MOD||la:habitare>fr:habitat>tr:habitat
çevresel|adj|tr|çevre|çevreye ilişkin|MOD|*evir-|
çevrebilim|n|tr|çevre+bil-|ekoloji|MOD|*evir-|
artezyen|n|fr|artésien|Artois bölgesine ilişkin|MOD||
sondaj|n|fr|sondage|yoklama, delme|MOD||
# --- Madenler, taşlar, cevherler ----------------------------------------------------------
cevher|n|ar|jawhar|öz; değerli taş|EAT|C-W-H|fa:gawhar>ar:jawhar>tr:cevher
cevheri|adj|ar|jawharī|öze ilişkin|OSM|C-W-H|
cevahir|n|ar|jawāhir|cevherler|OSM|C-W-H|
mücevher|n|ar|mujawhar|cevherli|OSM|C-W-H|
mücevherat|n|ar|mujawharāt|mücevherler|OSM|C-W-H|
madenci|n|ar|maʿdin|maden işçisi|OSM19|A-D-N|
madencilik|n|ar|maʿdin|maden işletme|CUM|A-D-N|
madeni|adj|ar|maʿdinī|madenden yapılmış|OSM|A-D-N|
boksit|n|fr|bauxite|Les Baux taşı|MOD||
uranyum|n|fr|uranium|Uranüs elementi|MOD||
alüminyum|n|fr|aluminium|şap madeni|MOD||la:alumen>fr:aluminium>tr:alüminyum
nikel|n|fr|nickel|cin bakırı|MOD||de:Kupfernickel>fr:nickel>tr:nikel
kobalt|n|fr|cobalt|cin madeni|MOD||
manganez|n|fr|manganèse|manganez|MOD||it:manganese>fr:manganèse>tr:manganez
tungsten|n|en|tungsten|ağır taş|MOD||
volfram|n|de|Wolfram|kurt köpüğü|MOD||
platin|n|fr|platine|gümüşçük|OSM19||es:platina>fr:platine>tr:platin
kükürt|n|fa|gūgird|kükürt|EAT||
fosfat|n|fr|phosphate|fosfor tuzu|MOD||
nitrat|n|fr|nitrate|azot tuzu|MOD||
bor|n|fr|bore|bor elementi|MOD||ar:būraq>la:borax>fr:bore>tr:bor
boraks|n|fr|borax|boraks tuzu|MOD||fa:būrah>ar:būraq>la:borax>fr:borax>tr:boraks
titanyum|n|fr|titane|Titan elementi|MOD||
magnezyum|n|fr|magnésium|Magnesia elementi|MOD||
kalsiyum|n|fr|calcium|kireç elementi|MOD||la:calx>fr:calcium>tr:kalsiyum
tuzla|n|tr|tuz|tuz çıkarılan yer|DLT||
zümrüt|n|ar|zumurrud|yeşil değerli taş|EAT||grc:smáragdos>ar:zumurrud>tr:zümrüt
yakut|n|ar|yāqūt|kırmızı değerli taş|EAT||grc:hyákinthos>ar:yāqūt>tr:yakut
elmas|n|ar|almās|en sert taş|EAT||grc:adámas>ar:almās>tr:elmas
pırlanta|n|it|brillante|parlayan|OSM||
akik|n|ar|ʿaqīq|damarlı süs taşı|EAT||
safir|n|fr|saphir|mavi değerli taş|OSM19||grc:sáppheiros>la:sapphirus>fr:saphir>tr:safir
firuze|n|fa|fīrūze|mavi-yeşil taş|EAT||
lal|n|fa|laʿl|kırmızı taş|EAT||
opal|n|fr|opale|renk oyunlu taş|MOD||sa:upala>la:opalus>fr:opale>tr:opal
oniks|n|fr|onyx|tırnak; damarlı taş|MOD||grc:ónyx>fr:onyx>tr:oniks
yeşim|n|tr?|yaşım|yeşil süs taşı|OSM||
billur|n|ar|billawr|kristal|EAT||grc:bḗryllos>ar:billawr>tr:billur
# --- Hava olayları ve iklim ---------------------------------------------------------------
sağanak|n|tr|sağanak|ani kuvvetli yağış|OSM||
çisenti|n|tr|çise-|ince yağmur|OSM|*çise-|
çise|n|tr|çise|ince yağmur|OSM|*çise-|
çiselemek|v|tr|çise-|ince ince yağmak|OSM|*çise-|
serpinti|n|tr|serp-|serpilen yağmur|OSM||
sulusepken|n|tr|sulu+sep-|karla karışık yağmur|OSM||
çiy|n|tr|çıġ|sabah nemi|EAT||
şebnem|n|fa|şabnam|gece nemi, çiy|EAT||
jale|n|fa|jāle|çiy|OSM||
sis|n|tr|sis|yoğun pus|EAT||
sisli|adj|tr|sis|sis kaplı|OSM||
pus|n|tr|bus|hafif sis|DLT||
puslu|adj|tr|bus|pus kaplı|OSM||
dumanlı|adj|tr|tuman|duman kaplı|EAT||
bulutlu|adj|tr|bulıt|bulut kaplı|DLT|*bulıt|
bulutsuz|adj|tr|bulıt|bulutu olmayan|OSM|*bulıt|
bulutlanmak|v|tr|bulıt|bulutla kaplanmak|OSM|*bulıt|
bulutsu|n|tr|bulıt|nebula|DD|*bulıt|
nebula|n|fr|nébuleuse|sisli|MOD||la:nebula>fr:nébuleuse>tr:nebula
şimşek|n|tr|şimşek|bulut parıltısı|EAT||
gürlemek|v|tr|gür|gümbürdemek|EAT|*gür-|
gürüldemek|v|tr|gür|gök gürlemek|OSM|*gür-|
gümbürtü|n|tr|gümbür|güçlü ses|OSM||
gümbürdemek|v|tr|gümbür|güçlü ses çıkarmak|OSM||
uğultu|n|tr|uğul|rüzgâr sesi|OSM||
uğuldamak|v|tr|uğul|uğultu çıkarmak|OSM||
bora|n|el|bóra|sert fırtına|OSM||la:boreas>it:bora>el:bóra>tr:bora
keşişleme|n|fa|kaşīş|rahip; Keşiş Dağı'ndan esen güneydoğu rüzgârı|OSM||
gündoğusu|n|tr|kün|doğu rüzgârı|OSM|*kün|
günbatısı|n|tr|kün|batı rüzgârı|OSM|*kün|
esinti|n|tr|es-|hafif rüzgâr|OSM|*es-|
estirmek|v|tr|es-|rüzgâr çıkarmak|OSM|*es-|
rüzgârlı|adj|fa|rūzgār|rüzgârı olan|OSM||
yelli|adj|tr|yel|rüzgârlı|DLT|*yel|
rüzgârgülü|n|fa|rūzgār|yön gülü|CUM||
bad|n|fa|bād|rüzgâr|EAT||
saba|n|ar|ṣabā|tan yeli|EAT||
nesim|n|ar|nasīm|hafif rüzgâr|EAT||
sam|n|ar|sāmm|zehirli|OSM||
samyeli|n|ar|sāmm|çöl sıcak rüzgârı|OSM||
alize|n|fr|alizé|düzenli tropikal rüzgâr|MOD||
muson|n|fr|mousson|mevsim rüzgârı|MOD||ar:mawsim>pt:monção>fr:mousson>tr:muson
fön|n|de|Föhn|sıcak dağ rüzgârı|MOD||la:favonius>de:Föhn>tr:fön
sirokko|n|it|scirocco|doğu rüzgârı|OSM19||ar:şarqī>it:scirocco>tr:sirokko
mistral|n|fr|mistral|usta rüzgârı|MOD||la:magistralis>oc:mistral>fr:mistral>tr:mistral
tornado|n|en|tornado|hortum|MOD||es:tronada>en:tornado>tr:tornado
antisiklon|n|fr|anticyclone|yüksek basınç alanı|MOD||
izobar|n|fr|isobare|eş basınç çizgisi|MOD|isos|
izoterm|n|fr|isotherme|eş sıcaklık çizgisi|MOD|isos|
higrometre|n|fr|hygromètre|nem ölçer|MOD|metron|
anemometre|n|fr|anémomètre|rüzgâr ölçer|MOD|metron|
altimetre|n|fr|altimètre|yükseklik ölçer|MOD|metron|
yağmurölçer|n|tr|yaġmur|yağış ölçen|DD|*yağ-|
yağış|n|tr|yaġ-|yağan|DD|*yağ-|
yağışlı|adj|tr|yaġ-|yağışı olan|TDK|*yağ-|
yağmak|v|tr|yaġ-|gökten düşmek|ORH|*yağ-|
yağdırmak|v|tr|yaġ-|yağmasına yol açmak|DLT|*yağ-|
yağmurlu|adj|tr|yaġmur|yağmuru olan|DLT|*yağ-|
rutubetli|adj|ar|ruṭūba|nemli|OSM||
nemlenmek|v|fa|nam|nem kazanmak|OSM||
buğu|n|tr|buġ|su buharı|DLT||
buğulanmak|v|tr|buġ|buğu kaplamak|OSM||
buhar|n|ar|buḫār|su buğusu|EAT||
buharlaşmak|v|ar|buḫār|buhara dönüşmek|TDK||
çorak|adj|tr|çorak|verimsiz, tuzlu|DLT||
kuraklaşmak|v|tr|kurı-|kurak duruma gelmek|TDK|*kuru-|
çölleşme|n|tr|çöl|çöle dönüşme|TDK|*çöl|
çölleşmek|v|tr|çöl|çöle dönüşmek|TDK|*çöl|
taşkın|n|tr|taş-|su baskını|OSM|*taş-|
taşmak|v|tr|taş-|kabından dışarı akmak|DLT|*taş-|
seylap|n|fa|saylāb|sel baskını|OSM|S-Y-L|
seyelan|n|ar|sayalān|akma|OSM|S-Y-L|
seyyal|adj|ar|sayyāl|akıcı|OSM|S-Y-L|
tufan|n|ar|ṭūfān|büyük sel|EAT|T-W-F|
feyezan|n|ar|fayaḍān|taşma|OSM|F-Y-Ḍ|
feyiz|n|ar|fayḍ|bolluk, taşma|EAT|F-Y-Ḍ|
dondurucu|adj|tr|toŋ-|çok soğuk|TDK|*don-|
donuk|adj|tr|toŋ-|donmuş; mat|OSM|*don-|
buzlu|adj|tr|buz|buz kaplı|DLT|*buz|
buzlanmak|v|tr|buz|buz tutmak|OSM|*buz|
buzul|n|tr|buz|buz kütlesi|DD|*buz|
buzkıran|n|tr|buz|buz kıran gemi|CUM|*buz|
buzluk|n|tr|buz|buz kabı|OSM|*buz|
serinlik|n|tr|serin|serin olma|OSM|*serin|
serinlemek|v|tr|serin|serin duruma gelmek|OSM|*serin|
serinletmek|v|tr|serin|serin duruma getirmek|OSM|*serin|
mutedil|adj|ar|muʿtadil|ılımlı|OSM|A-D-L|
hararet|n|ar|ḥarāra|sıcaklık|EAT|H-R-R|
suhunet|n|ar|suḫūna|sıcaklık|OSM||
bürudet|n|ar|burūda|soğukluk|OSM||
kavurucu|adj|tr|kavur-|yakıcı|TDK||
bunaltıcı|adj|tr|bun|sıkıntı veren|TDK||
bunaltı|n|tr|bun|sıkıntı|TDK||
boğucu|adj|tr|boġ-|nefes aldırmayan|OSM|*boğ-|
zemheri|n|ar|zamharīr|şiddetli soğuk|EAT||
erbain|n|ar|arbaʿīn|kırk|OSM||
hamsin|n|ar|ḫamsīn|elli|OSM||
cemre|n|ar|jamra|kor|OSM||
hazan|n|fa|ḫazān|sonbahar|EAT||
ilkyaz|n|tr|ilk+yaz|ilkbahar|TDK||
mevsimsel|adj|ar|mawsim|mevsime ilişkin|TDK||
kışın|adv|tr|kış|kış mevsiminde|DLT|*kış|
güzün|adv|tr|küz|sonbaharda|DLT|*küz|
güzlük|n|tr|küz|güzün ekilen|OSM|*küz|
hıdrellez|n|ar|Ḫiḍr+Ilyās|Hızır ve İlyas günü|OSM||
ekinoks|n|fr|équinoxe|gün-gece eşitliği|MOD|aequus|
ılım|n|tr|ılı-|ekinoks|DD|*ılı-|
gündönümü|n|tr|kün|güneşin dönüm günü|DD|*kün|
kırkikindi|n|tr|kırk+ikindi|mayıs ikindi yağmurları|OSM||
almanak|n|fr|almanach|yıllık|OSM19||ar:al-manāḫ>fr:almanach>tr:almanak
iklimlendirme|n|ar|iqlīm|hava koşullandırma|MOD|klima|
klima|n|fr|climatiseur|iklimleyici|MOD|klima|
klimatoloji|n|fr|climatologie|iklim bilimi|MOD|klima|
klimatolog|n|fr|climatologue|iklim bilimci|MOD|klima|
meteoroloji|n|fr|météorologie|hava bilimi|CUM|meteōros|
meteorolog|n|fr|météorologue|hava bilimci|MOD|meteōros|
meteorolojik|adj|fr|météorologique|hava bilimine ilişkin|MOD|meteōros|
meteor|n|fr|météore|havada yükselen|CUM|meteōros|
meteorit|n|fr|météorite|göktaşı|MOD|meteōros|
göktaşı|n|tr|kök+taş|gökten düşen taş|DD|*kök|
atmosfer|n|fr|atmosphère|buhar küresi|CUM|sphaira|
litosfer|n|fr|lithosphère|taş küre|MOD|sphaira|
hidrosfer|n|fr|hydrosphère|su küre|MOD|sphaira|
biyosfer|n|fr|biosphère|yaşam küresi|MOD|sphaira|
stratosfer|n|fr|stratosphère|katman küre|MOD|sphaira|
troposfer|n|fr|troposphère|dönüş küresi|MOD|sphaira|
iyonosfer|n|fr|ionosphère|iyon küresi|MOD|sphaira|
ozon|n|fr|ozone|kokan|MOD||grc:ózein>fr:ozone>tr:ozon
küre|n|ar|kura|top, yuvarlak|OSM||
küresel|adj|ar|kura|küreye ilişkin; dünya çapında|MOD||
yarıküre|n|tr|yarı+küre|yarım küre|DD||
güneşli|adj|tr|kün|güneşi olan|OSM|*kün|
güneşlenmek|v|tr|kün|güneşte durmak|TDK|*kün|
güneşlik|n|tr|kün|güneşten koruyan|OSM|*kün|
güneşlenme|n|tr|kün|güneşte durma|TDK|*kün|
gölgeli|adj|tr|kölige|gölgesi olan|DLT|*kölige|
gölgelik|n|tr|kölige|gölge yeri|OSM|*kölige|
gölgelemek|v|tr|kölige|gölge yapmak|OSM|*kölige|
gölgelenmek|v|tr|kölige|gölgede durmak|OSM|*kölige|
tente|n|it|tenda|gölgelik bezi|OSM19||
sayfiye|n|ar|ṣayfiyya|yazlık|OSM||
yazlıkçı|n|tr|yaz|yazlığa gelen|MOD||
mehtap|n|fa|māhtāb|ay ışığı|EAT|māh|
mehtaplı|adj|fa|māhtāb|ay ışıklı|OSM|māh|
ziya|n|ar|ḍiyāʾ|ışık|EAT|D-W-A|
ziyadar|adj|fa|ḍiyā+dār|ışıklı|OSM|D-W-A|
şule|n|ar|şuʿla|alev, ışık|EAT|Ş-A-L|
meşale|n|ar|maşʿal|alev taşıyıcı|EAT|Ş-A-L|
iştial|n|ar|iştiʿāl|tutuşma|OSM|Ş-A-L|
şerare|n|ar|şarāra|kıvılcım|OSM||
kıvılcım|n|tr|kıvılcım|ateş parçası|EAT||
ışıltı|n|tr|yaşu-|parıltı|OSM|*ışı-|
ışıldamak|v|tr|yaşu-|parlamak|OSM|*ışı-|
parıltı|n|tr|parıl|parlama|OSM|*parla-|
parıldamak|v|tr|parıl|parlamak|OSM|*parla-|
pırıltı|n|tr|pırıl|hafif parlama|OSM|*parla-|
loş|adj|tr?|loş|yarı karanlık|OSM||
loşluk|n|tr?|loş|yarı karanlık olma|OSM||
zulmetli|adj|ar|ẓulma|karanlık|OSM|Z-L-M|
alaca|adj|tr|ala|karışık renkli|DLT||
alacalı|adj|tr|ala|alaca renkli|OSM||
karartı|n|tr|kara|karanlıkta görünen şey|OSM||
ağarmak|v|tr|ak|beyazlaşmak; tan atmak|DLT||
kararmak|v|tr|kara|karanlık olmak|DLT||
aydınlanma|n|tr|ay|ışıklanma|TDK|*ay|
# --- Günün vakitleri --------------------------------------------------------------------
yatsı|n|tr|yatsıġ|yatma vakti|DLT|*yat-|
öğleüstü|n|tr|öđ|öğle vakti|OSM||
akşamüstü|n|tr|akşam|akşama doğru|OSM||
sabahleyin|adv|ar|ṣabāḥ|sabah vakti|EAT||
akşamleyin|adv|tr|akşam|akşam vakti|OSM||
geceleyin|adv|tr|kiçe|gece vakti|EAT||
fecir|n|ar|fajr|tan ağarması|EAT||
gurup|n|ar|ġurūb|batış|EAT|Ğ-R-B|
zeval|n|ar|zawāl|öğle; yok olma|EAT|Z-W-L|
zail|adj|ar|zāʾil|yok olan|OSM|Z-W-L|
izale|n|ar|izāla|giderme|OSM|Z-W-L|
tulu|n|ar|ṭulūʿ|doğuş|EAT|T-L-A|
matla|n|ar|maṭlaʿ|doğuş yeri; ilk beyit|OSM|T-L-A|
# --- Gökyüzü ve gök cisimleri -------------------------------------------------------------
gökyüzü|n|tr|kök+yüz|gök|OSM|*kök|
gökbilim|n|tr|kök+bil-|astronomi|DD|*kök|
gökbilimci|n|tr|kök+bil-|astronom|DD|*kök|
gökada|n|tr|kök+ada|galaksi|DD|*kök|
gökcismi|n|tr|kök+cisim|gök nesnesi|DD|*kök|
gökkuşağı|n|tr|kök+kuşak|alkım|OSM|*kök|
gökkubbe|n|tr|kök+kubbe|gök çatısı|OSM|*kök|
gökçe|adj|tr|kökçe|mavimsi; güzel|DLT|*kök|
göksel|adj|tr|kök|göğe ilişkin|DD|*kök|
gökdelen|n|tr|kök+del-|çok katlı yapı|CUM|*kök|
galaksi|n|fr|galaxie|süt yolu|CUM||grc:galaxías>fr:galaxie>tr:galaksi
Samanyolu|prop|tr|saman+yol|gökada|OSM||
Kehkeşan|prop|fa|kahkaşān|saman çeken|OSM||
yıldızlı|adj|tr|yultuz|yıldızı olan|DLT|*yultuz|
takımyıldız|n|tr|takım+yultuz|yıldız kümesi|DD|*yultuz|
yıldızname|n|tr|yultuz+nāme|yıldız falı kitabı|OSM|*yultuz|
seyyare|n|ar|sayyāra|gezen; gezegen|OSM|S-Y-R|
hilal|n|ar|hilāl|yeni ay|EAT||
dolunay|n|tr|dolun+ay|ayın dolgun hâli|OSM|*ay|
ayça|n|tr|ay|yeni ay|DLT|*ay|
aydede|n|tr|ay+dede|ay|OSM|*ay|
ayla|n|tr|ay|hale|DD|*ay|
bedir|n|ar|badr|dolunay|EAT||
tutulma|n|tr|tut-|gök cisminin örtülmesi|TDK|*tut-|
husuf|n|ar|ḫusūf|ay tutulması|OSM||
küsuf|n|ar|kusūf|güneş tutulması|OSM||
Merkür|prop|fr|Mercure|Roma tanrısı; gezegen|CUM||la:Mercurius>fr:Mercure>tr:Merkür
Utarit|prop|ar|ʿUṭārid|Merkür|OSM||
Venüs|prop|fr|Vénus|Roma tanrıçası; gezegen|CUM||la:Venus>fr:Vénus>tr:Venüs
Zühre|prop|ar|Zuhara|Venüs|EAT||
Mars|prop|fr|Mars|savaş tanrısı; gezegen|CUM||la:Mars>fr:Mars>tr:Mars
Merih|prop|ar|Mirrīḫ|Mars|EAT||
Jüpiter|prop|fr|Jupiter|baş tanrı; gezegen|CUM||la:Iuppiter>fr:Jupiter>tr:Jüpiter
Müşteri|prop|ar|Muştarī|Jüpiter|EAT||
Satürn|prop|fr|Saturne|ekin tanrısı; gezegen|CUM||la:Saturnus>fr:Saturne>tr:Satürn
Zühal|prop|ar|Zuḥal|Satürn|EAT||
Uranüs|prop|fr|Uranus|gök tanrısı; gezegen|CUM||grc:Ouranós>la:Uranus>fr:Uranus>tr:Uranüs
Neptün|prop|fr|Neptune|deniz tanrısı; gezegen|CUM||la:Neptunus>fr:Neptune>tr:Neptün
Plüton|prop|fr|Pluton|yer altı tanrısı; cüce gezegen|MOD||grc:Ploútōn>la:Pluto>fr:Pluton>tr:Plüton
Ülker|prop|tr|Ülker|Süreyya yıldız kümesi|DLT||
Süreyya|prop|ar|Ṯurayyā|Ülker|EAT||
Demirkazık|prop|tr|temir+kazık|Kutup Yıldızı|OSM||
feza|n|ar|faḍāʾ|boşluk, uzay|EAT||
sema|n|ar|samāʾ|gök|EAT|S-M-W|
semavi|adj|ar|samāwī|göksel|EAT|S-M-W|
semavat|n|ar|samāwāt|gökler|OSM|S-M-W|
arş|n|ar|ʿarş|taht; en yüksek gök|EAT||
felek|n|ar|falak|gök küresi; talih|EAT|F-L-K|
eflak|n|ar|aflāk|gökler|OSM|F-L-K|
çarkıfelek|n|fa|çarḫ-i falak|gök çarkı|OSM|F-L-K|
yörünge|n|tr|yörü-|dolanım yolu|DD|*yürü-|
mahrek|n|ar|maḥrak|yörünge|OSM|H-R-K|
peyk|n|fa|payk|haberci; uydu|OSM||
rasat|n|ar|raṣad|gözetleme|OSM|R-S-D|
rasathane|n|fa|raṣad+ḫāne|gözlemevi|OSM|R-S-D|
rasıt|n|ar|rāṣid|gözlemci|OSM|R-S-D|
gözlemevi|n|tr|köz|rasathane|DD||
usturlap|n|ar|asṭurlāb|yıldız ölçer|EAT||grc:astrolábos>ar:asṭurlāb>tr:usturlap
nücum|n|ar|nujūm|yıldızlar|EAT|N-C-M|
necim|n|ar|najm|yıldız|OSM|N-C-M|
müneccim|n|ar|munajjim|yıldız falcısı|EAT|N-C-M|
müneccimbaşı|n|ar|munajjim|saray baş astroloğu|OSM|N-C-M|
kamer|n|ar|qamar|ay|EAT|K-M-R|
kameri|adj|ar|qamarī|aya ilişkin|OSM|K-M-R|
kameriye|n|ar|qamariyya|ay seyredilen çardak|OSM|K-M-R|
şems|n|ar|şams|güneş|EAT|Ş-M-S|
şemsi|adj|ar|şamsī|güneşe ilişkin|OSM|Ş-M-S|
astrolog|n|fr|astrologue|yıldız yorumcusu|CUM|astēr|
astrofizik|n|fr|astrophysique|yıldız fiziği|MOD|astēr|
kozmonot|n|sl|kosmonavt|evren gezgini|MOD|kosmos|
uzaylı|n|tr|uzay|uzaydan gelen|MOD||
Koç|prop|tr|koç|burç|OSM||
Boğa|prop|tr|buka|burç|OSM||
İkizler|prop|tr|ikiz|burç|OSM||
Yengeç|prop|tr|yengeç|burç|OSM||
Aslan|prop|tr|arslan|burç|OSM||
Başak|prop|tr|başak|burç|OSM||
Terazi|prop|fa|tarāzū|burç|OSM||
Akrep|prop|ar|ʿaqrab|burç|OSM||
Yay|prop|tr|ya|burç|OSM||
Oğlak|prop|tr|oġlak|burç|OSM||
Kova|prop|tr|kova|burç|OSM||
Balık|prop|tr|balık|burç|OSM||
terazi|n|fa|tarāzū|tartı|EAT||
# --- Yönler ve uzam ---------------------------------------------------------------------
kuzey|n|tr|kuz|gölgeli yan; şimal|DD|*kuz|
güney|n|tr|kün|güneşli yan; cenup|DD|*kün|
kuzeyli|n|tr|kuz|kuzeyden olan|TDK|*kuz|
güneyli|n|tr|kün|güneyden olan|TDK|*kün|
kuzeybatı|n|tr|kuz|kuzey ile batı arası|DD|*kuz|
kuzeydoğu|n|tr|kuz|kuzey ile doğu arası|DD|*kuz|
güneybatı|n|tr|kün|güney ile batı arası|DD|*kün|
güneydoğu|n|tr|kün|güney ile doğu arası|DD|*kün|
doğulu|n|tr|toġ-|doğudan olan|TDK|*doğ-|
batılı|n|tr|bat-|batıdan olan|TDK|*bat-|
batılılaşmak|v|tr|bat-|Batı'yı örnek almak|TDK|*bat-|
batılılaşma|n|tr|bat-|Batı'yı örnek alma|TDK|*bat-|
şark|n|ar|şarq|doğu|EAT|Ş-R-Q|
maşrık|n|ar|maşriq|güneşin doğduğu yer|EAT|Ş-R-Q|
şarklı|n|ar|şarq|doğulu|OSM|Ş-R-Q|
şarkiyat|n|ar|şarqiyyāt|doğu bilimleri|OSM19|Ş-R-Q|
şarkiyatçı|n|ar|şarqiyyāt|doğu bilimci|CUM|Ş-R-Q|
oryantal|adj|fr|oriental|doğulu|CUM||la:oriens>fr:oriental>tr:oryantal
oryantalist|n|fr|orientaliste|doğu bilimci|CUM||
oryantalizm|n|fr|orientalisme|doğu bilimi|CUM||
garp|n|ar|ġarb|batı|EAT|Ğ-R-B|
mağrip|n|ar|maġrib|güneşin battığı yer|EAT|Ğ-R-B|
garplı|n|ar|ġarb|batılı|OSM19|Ğ-R-B|
gurbet|n|ar|ġurba|yabancı yer|EAT|Ğ-R-B|
gurbetçi|n|ar|ġurba|gurbette çalışan|MOD|Ğ-R-B|
garabet|n|ar|ġarāba|tuhaflık|OSM|Ğ-R-B|
garipsemek|v|ar|ġarīb|yadırgamak|OSM|Ğ-R-B|
şimal|n|ar|şimāl|kuzey; sol|EAT|Ş-M-L|
şimali|adj|ar|şimālī|kuzeye ilişkin|OSM|Ş-M-L|
şümul|n|ar|şumūl|kapsam|OSM|Ş-M-L|
şamil|adj|ar|şāmil|kapsayan|OSM|Ş-M-L|
şümullü|adj|ar|şumūl|kapsamlı|OSM|Ş-M-L|
müştemilat|n|ar|muştamilāt|eklentiler|OSM|Ş-M-L|
cihanşümul|adj|fa|jahān+şumūl|evrensel|OSM|Ş-M-L|
âlemşümul|adj|ar|ʿālam+şumūl|evrensel|OSM|Ş-M-L|
cenup|n|ar|janūb|güney|EAT|C-N-B|
cenubi|adj|ar|janūbī|güneye ilişkin|OSM|C-N-B|
canip|n|ar|jānib|yan, taraf|EAT|C-N-B|
ecnebi|n|ar|ajnabī|yabancı|EAT|C-N-B|
içtinap|n|ar|ijtināb|kaçınma|OSM|C-N-B|
cünüp|adj|ar|junub|yıkanması gereken|EAT|C-N-B|
cenabet|n|ar|janāba|cünüplük|EAT|C-N-B|
cihet|n|ar|jiha|yön|EAT|W-C-H|
vecih|n|ar|wajh|yüz; yön|EAT|W-C-H|
veçhe|n|ar|wijha|yön, görünüş|OSM|W-C-H|
tevcih|n|ar|tawjīh|yöneltme|OSM|W-C-H|
teveccüh|n|ar|tawajjuh|yönelme; ilgi|OSM|W-C-H|
müteveccih|adj|ar|mutawajjih|yönelmiş|OSM|W-C-H|
tarafgir|adj|fa|ṭaraf+gīr|taraf tutan|OSM|T-R-F|
civar|n|ar|jiwār|komşuluk, yöre|EAT|C-W-R|
mücavir|adj|ar|mujāwir|komşu|OSM|C-W-R|
muhit|n|ar|muḥīṭ|kuşatan; çevre|OSM|H-W-T|
ihata|n|ar|iḥāṭa|kuşatma|OSM|H-W-T|
havali|n|ar|ḥawālī|çevre, dolay|EAT|H-W-L|
mıntıka|n|ar|minṭaqa|kuşak, bölge|OSM|N-T-K|
bölgesel|adj|tr|böl-|bölgeye ilişkin|TDK|*böl-|
mevki|n|ar|mawqiʿ|yer, konum|EAT||
kenar|n|fa|kanār|uç, kıyı|EAT||
köşe|n|fa|gūşe|iki kenarın birleştiği yer|EAT|gūşe|
köşeli|adj|fa|gūşe|köşesi olan|OSM|gūşe|
köşebaşı|n|fa|gūşe|sokak köşesi|OSM|gūşe|
uç|n|tr|uç|son nokta; sınır|ORH||
sivri|adj|tr|sivri|ucu ince|EAT||
dik|adj|tr|tik|düşey|DLT||
sarp|adj|tr|sarp|dik ve geçilmez|DLT||
engebe|n|tr|engebe|inişli çıkışlı yer|TDK||
engebeli|adj|tr|engebe|inişli çıkışlı|TDK||
yokuş|n|tr|yokuş|yukarı giden yol|DLT||
düzlem|n|tr|tüz|düz yüzey|DD|*düz-|
eğim|n|tr|eg-|eğiklik|DD|*eg-|
eğimli|adj|tr|eg-|eğik|TDK|*eg-|
eğik|adj|tr|eg-|eğilmiş|OSM|*eg-|
meyil|n|ar|mayl|eğim; eğilim|EAT|M-Y-L|
meyilli|adj|ar|mayl|eğimli|OSM|M-Y-L|
mail|adj|ar|māʾil|eğik|OSM|M-Y-L|
temayül|n|ar|tamāyul|eğilim|OSM|M-Y-L|
irtifa|n|ar|irtifāʿ|yükseklik|OSM||
rakım|n|ar|raqm|işaret; yükselti|OSM19|R-K-M|
merkum|adj|ar|marqūm|adı geçen|OSM|R-K-M|
kot|n|fr|cote|yükseklik değeri|MOD||
yükseklik|n|tr|yük-|yüksek olma|OSM|*yük-|
yükselti|n|tr|yük-|rakım|DD|*yük-|
mesafe|n|ar|masāfa|uzaklık|EAT||
yakınlık|n|tr|yak-|yakın olma|DLT|*yak-|
yakınlaşmak|v|tr|yak-|yakın duruma gelmek|OSM|*yak-|
uzaklaşmak|v|tr|uza-|uzak duruma gelmek|EAT||
uzaklaştırmak|v|tr|uza-|uzak duruma getirmek|OSM||
ırak|adj|tr|yırak|uzak|ORH|*yırak|
ıraksamak|v|tr|yırak|uzak görmek|DD|*yırak|
mil|n|en|mile|bin adım|OSM19||la:milia>en:mile>tr:mil
fersah|n|ar|farsaḫ|fersah (uzunluk ölçüsü)|EAT||
kulaç|n|tr|kulaç|iki kol açımı|DLT||
arşın|n|fa?|araş|dirsek boyu|EAT||
karış|n|tr|karış|el açımı|DLT||
dönüm|n|tr|tön-|bir çift öküzün günlük sürdüğü alan|OSM|*dön-|
hektar|n|fr|hectare|yüz ar|CUM||
koordinat|n|fr|coordonnée|birlikte düzenlenmiş|MOD||
enlem|n|tr|en|paralel|DD||
boylam|n|tr|boy|meridyen|DD||
paralel|n|fr|parallèle|yan yana|CUM||grc:parállēlos>fr:parallèle>tr:paralel
meridyen|n|fr|méridien|öğle çizgisi|CUM||la:meridianus>fr:méridien>tr:meridyen
ekvator|n|fr|équateur|eşitleyici|CUM|aequus|la:aequator>fr:équateur>tr:ekvator
ekvatoral|adj|fr|équatorial|ekvatora ilişkin|MOD|aequus|
tropik|n|fr|tropique|dönence|CUM|tropos|grc:tropikós>fr:tropique>tr:tropik
tropikal|adj|fr|tropical|dönenceye ilişkin|CUM|tropos|
subtropikal|adj|fr|subtropical|dönence altı|MOD|tropos|
zenit|n|fr|zénith|başucu|CUM|S-M-T|ar:samt>es:cenit>fr:zénith>tr:zenit
azimut|n|fr|azimut|yönler|MOD|S-M-T|ar:as-sumūt>es:acimut>fr:azimut>tr:azimut
kıblenüma|n|fa|qibla+numā|kıble gösteren|OSM||
navigasyon|n|fr|navigation|gemi sürme|MOD||la:navigatio>fr:navigation>tr:navigasyon
sekstant|n|fr|sextant|altıda bir|MOD||la:sextans>fr:sextant>tr:sekstant
haritacı|n|ar|ḫarīṭa|harita yapan|CUM||
haritacılık|n|ar|ḫarīṭa|harita yapımı|CUM||
ufuk|n|ar|ufuq|gök ile yerin birleşir göründüğü çizgi|EAT||
yerbilim|n|tr|yer|jeoloji|DD|*yer|
yerbilimci|n|tr|yer|jeolog|DD|*yer|
yeryüzü|n|tr|yer+yüz|dünya yüzeyi|EAT|*yer|
yerküre|n|tr|yer+küre|dünya|DD|*yer|
yerkabuğu|n|tr|yer+kabuk|litosfer|DD|*yer|
yeraltı|n|tr|yer+alt|yerin altı|OSM|*yer|
yerüstü|n|tr|yer+üst|yerin üstü|OSM|*yer|
yerçekimi|n|tr|yer+çek-|kütle çekimi|DD|*yer|
yerel|adj|tr|yer|yöresel|DD|*yer|
yerli|n|tr|yer|o yerden olan|DLT|*yer|
yerleşim|n|tr|yer|yerleşme yeri|DD|*yer|
yerleşke|n|tr|yer|kampüs|NEW|*yer|
yerleşmek|v|tr|yerleş-|bir yere konmak|DLT|*yer|
yerleşik|adj|tr|yerleş-|yerleşmiş|DD|*yer|
dünyevi|adj|ar|dunyawī|dünyaya ilişkin|OSM|D-N-W|
dünyalık|n|ar|dunyā|mal, para|OSM|D-N-W|
vasat|n|ar|wasaṭ|orta|EAT|W-S-T|
vasati|adj|ar|wasaṭī|ortalama|OSM|W-S-T|
mutavassıt|adj|ar|mutawassiṭ|aracı; orta|OSM|W-S-T|
tavassut|n|ar|tawassuṭ|aracılık|OSM|W-S-T|
ulvi|adj|ar|ʿulwī|yüce|EAT|A-L-W|
âli|adj|ar|ʿālī|yüksek|EAT|A-L-W|
teali|n|ar|taʿālī|yükselme|OSM|A-L-W|
süfli|adj|ar|suflī|aşağı, bayağı|OSM|S-F-L|
sefil|adj|ar|safīl|düşkün|EAT|S-F-L|
esfel|adj|ar|asfal|en aşağı|OSM|S-F-L|
şahika|n|ar|şāhiqa|doruk|OSM||
hacer|n|ar|ḥajar|taş|EAT|Ḥ-C-R|
hacir|n|ar|ḥajr|kısıtlama|OSM|Ḥ-C-R|
mahcur|adj|ar|maḥjūr|kısıtlanmış|OSM|Ḥ-C-R|
türab|n|ar|turāb|toprak|EAT|T-R-B|
cebel|n|ar|jabal|dağ|EAT|C-B-L|
cibilliyet|n|ar|jibilliyya|yaratılış|OSM|C-B-L|
cezire|n|ar|jazīra|ada|EAT|C-Z-R|
Cezayir|prop|ar|al-Jazāʾir|adalar|OSM|C-Z-R|
heva|n|ar|hawāʾ|hava; boşluk|EAT|H-W-A|
havai|adj|ar|hawāʾī|havaya ilişkin; uçarı|OSM|H-W-A|
havadar|adj|fa|hawā+dār|havası bol|OSM|H-W-A|
havalanmak|v|ar|hawāʾ|havaya kalkmak|OSM|H-W-A|
havalı|adj|ar|hawāʾ|havası olan; gösterişli|OSM|H-W-A|
havasız|adj|ar|hawāʾ|havası olmayan|OSM|H-W-A|
havacı|n|ar|hawāʾ|hava taşıtı kullanan|CUM|H-W-A|
havacılık|n|ar|hawāʾ|hava ulaşımı|CUM|H-W-A|
havaalanı|n|ar|hawāʾ|uçak alanı|CUM|H-W-A|
havalimanı|n|ar|hawāʾ|hava limanı|MOD|H-W-A|
havayolu|n|ar|hawāʾ|uçak şirketi|CUM|H-W-A|
rayiha|n|ar|rāʾiḥa|koku|OSM|R-W-H|
# --- Yer adı ögeleri ve yerleşim ----------------------------------------------------------
burgaz|n|el|pýrgos|kule|EAT||
viran|adj|fa|vīrān|yıkık|EAT|vīrān|
virane|n|fa|vīrāne|yıkıntı|OSM|vīrān|
harabe|n|ar|ḫarāba|yıkıntı|EAT||
harap|adj|ar|ḫarāb|yıkık|EAT||
enkaz|n|ar|anqāḍ|yıkıntı|OSM||
yıkıntı|n|tr|yık-|yıkılmış yer|OSM||
ören|n|tr|ören|yıkıntı, eski yerleşim|EAT||
höyük|n|tr|öyük|yığma tepe|OSM||
tümülüs|n|fr|tumulus|yığma mezar tepesi|MOD||la:tumulus>fr:tumulus>tr:tümülüs
nekropol|n|fr|nécropole|ölüler kenti|MOD|polis|
akropol|n|fr|acropole|yüksek kent|MOD|polis|
antik|adj|fr|antique|eski|CUM||la:antiquus>fr:antique>tr:antik
bulak|n|tr|bulak|pınar|DLT||
kom|n|hy?|gom|ağıl|OSM||
mezra|n|ar|mazraʿa|ekilen yer; küçük köy|OSM|Z-R-A|
abat|adj|fa|ābād|bayındır|EAT||
balkan|n|tr|balkan|sarp ormanlık dağ|OSM||
yurtluk|n|tr|yurt|yurt olarak verilen yer|OSM||
konalga|n|tr|kon-|konak yeri|DLT|*kon-|
göçebe|n|tr|köç|yer değiştiren|OSM|*köç-|
göçer|adj|tr|köç-|göç eden|DLT|*köç-|
konargöçer|n|tr|kon-+köç-|yarı göçebe|TDK|*köç-|
yörük|n|tr|yörü-|göçebe Türkmen|EAT|*yürü-|
uğrak|n|tr|uğra-|uğranılan yer|OSM||
yolak|n|tr|yol|keçi yolu|OSM||
sapa|adj|tr|sap-|yol dışında|OSM||
ıssız|adj|tr|idi+sız|sahipsiz, tenha|EAT||
balbal|n|tr|balbal|mezar taşı heykeli|ORH||
tamga|n|tr|tamġa|damga, boy işareti|ORH||
gölcük|n|tr|köl|küçük göl|OSM||
# --- Ek: yer, ölçü, gök ve iklim sözcükleri ----------------------------------------------
kadran|n|fr|cadran|güneş saati levhası; gösterge yüzü|CUM||la:quadrans>fr:cadran>tr:kadran
sönük|adj|tr|sön-|ışığı azalmış|OSM||
tenha|adj|fa|tanhā|yalnız; ıssız|EAT||
meskûn|adj|ar|maskūn|oturulan, yerleşilmiş|OSM|S-K-N|
bayındır|adj|tr|bayındır|gelişmiş, mamur|DLT||
bayındırlık|n|tr|bayındır|imar işleri|TDK||
kümülüs|n|fr|cumulus|yığın bulutu|MOD||la:cumulus>fr:cumulus>tr:kümülüs
evrenbilim|n|tr|evren+bil-|kozmoloji|DD|*evir-|
kuasar|n|en|quasar|yıldızımsı radyo kaynağı|MOD||
pulsar|n|en|pulsar|atarca|MOD||
süpernova|n|fr|supernova|yeni yıldız patlaması|MOD||la:nova>fr:supernova>tr:süpernova
imsak|n|ar|imsāk|tutma; oruç başlangıcı|EAT||
palanka|n|it|palanca|kazık; ahşap tabya|OSM||
varoş|n|hu|város|şehir; kenar mahalle|OSM||
ayazma|n|el|hagíasma|kutsal kaynak|OSM||
seki|n|tr|seki|yüksek düz yer; taraça|DLT||
taraça|n|it|terrazza|düz dam; sekili arazi|OSM19|terra|
engin|adj|tr|engin|uçsuz bucaksız; açık deniz|OSM||
enginlik|n|tr|engin|uçsuz bucaksızlık|TDK||
çoraklaşmak|v|tr|çorak|çorak duruma gelmek|TDK||
selinti|n|ar|sayl|sel sularının bıraktığı birikinti|OSM|S-Y-L|
buzlanma|n|tr|buz|buz tutma|TDK|*buz|
donma|n|tr|toŋ-|donma olayı|TDK|*don-|
endaze|n|fa|andāze|ölçü; 65 santimetrelik ölçü|EAT||
yarda|n|en|yard|üç ayaklık uzunluk|OSM19||
inç|n|en|inch|parmak; 2,54 santimetre|MOD||la:uncia>en:inch>tr:inç
püskürme|n|tr|püskür-|yanardağ patlaması|TDK||
gayzer|n|fr|geyser|fışkıran sıcak su kaynağı|MOD||
haliç|n|ar|ḫalīj|körfez; ırmak ağzı|EAT||
mendirek|n|el|mandráki|küçük liman; dalgakıran|OSM||
mevsimsiz|adj|ar|mawsim|mevsimi dışında|OSM||
baharlık|adj|fa|bahār|bahara uygun|OSM||
yılbaşı|n|tr|yıl+baş|yılın ilk günü|OSM||
yıldönümü|n|tr|yıl+dön-|yıllık dönüm günü|TDK|*dön-|
dolay|n|tr|dolay|çevre, yakın yer|OSM||
satıh|n|ar|saṭḥ|yüzey|OSM|S-T-H|
sathi|adj|ar|saṭḥī|yüzeysel|OSM|S-T-H|
cihannüma|n|fa|jahān+numā|dünyayı gösteren; çatı köşkü|OSM||
mürtefi|adj|ar|murtafiʿ|yüksek|OSM|R-F-A|
refi|adj|ar|rafīʿ|yüce|OSM|R-F-A|
çemenzar|n|fa|çamanzār|çimenlik|OSM|-zār|
lalezar|n|fa|lālezār|lale bahçesi|OSM|-zār|
gülzar|n|fa|gulzār|gül bahçesi|EAT|-zār|
rezervuar|n|fr|réservoir|su deposu|MOD||
peyzaj|n|fr|paysage|kır görünümü|MOD||
kadastro|n|fr|cadastre|arazi kütüğü|CUM||
kroki|n|fr|croquis|taslak çizim|CUM||
dürbün|n|fa|dūrbīn|uzağı gören|OSM||
glasyoloji|n|fr|glaciologie|buzul bilimi|MOD||
speleoloji|n|fr|spéléologie|mağara bilimi|MOD||
stratigrafi|n|fr|stratigraphie|katman betimleme|MOD|graphein|
toponimi|n|fr|toponymie|yer adı bilimi|MOD|topos|
biyoçeşitlilik|n|fr|biodiversité|yaşam çeşitliliği|NEW|bios|
endemik|adj|fr|endémique|yöreye özgü|MOD||
arazi|n|ar|arāḍī|topraklar|EAT||
yönelmek|v|tr|yön|bir yöne dönmek|DD|*yön|
yönelim|n|tr|yön|yönelme|DD|*yön|
terfi|n|ar|tarfīʿ|yükseltme|OSM|R-F-A|
miladi|adj|ar|mīlādī|doğuma ilişkin; güneş takvimi|OSM||
hicri|adj|ar|hijrī|hicrete ilişkin; ay takvimi|OSM||
bük|n|tr|bük|akarsu kıyısındaki çalılık|EAT||
yalçın|adj|tr|yalçın|dik ve çıplak kaya|OSM||
kesek|n|tr|kesek|toprak topağı|DLT|*kes-|
tozlu|adj|tr|toz|toz kaplı|DLT||
sarplık|n|tr|sarp|dik ve geçilmez olma|TDK||
sivrilmek|v|tr|sivri|ucu incelmek; öne çıkmak|OSM||
uçsuz|adj|tr|uç|ucu olmayan|OSM||
bucaksız|adj|tr|bucak|sınırsız|OSM||
tepeleme|adv|tr|töpü|ağzına kadar dolu|OSM|*töpü|
dağlamak|v|tr|taġ-|kızgın demirle yakmak|DLT||
yıldızyeli|n|tr|yultuz+yel|kuzey rüzgârı|OSM|*yel|
lodoslu|adj|el|nótos|lodosu esen|OSM||
poyrazlı|adj|el|boréas|poyrazı esen|OSM||
meltemli|adj|it|maltempo|meltemi esen|OSM||
akıntılı|adj|tr|ak-|akıntısı olan|OSM|*ak-|
gelgitli|adj|tr|gel-+git-|gelgiti olan|TDK||
dalgalı|adj|tr|dalga|dalgası olan|OSM||
köpüklü|adj|tr|köpük|köpüğü olan|OSM||
sisleşmek|v|tr|sis|sise dönüşmek|TDK||
ayazlamak|v|tr|ayas|soğukta kalmak|OSM||
serinkanlı|adj|tr|serin+kan|soğukkanlı|TDK|*serin|
# --- Ek II: doğa olayları, ölçüler, coğrafi adlar ----------------------------------------
bağlık|n|fa|bāġ|bağ alanı|OSM||
otluk|n|tr|ot|otlu yer; ot deposu|DLT||
ıssızlık|n|tr|idi+sız|tenha olma|OSM||
tenhalık|n|fa|tanhā|ıssızlık|OSM||
yabanlık|n|fa|yābān|yaban yeri|OSM||
ağaçsız|adj|tr|yıġaç|ağacı olmayan|OSM||
yağmursuz|adj|tr|yaġmur|yağmuru olmayan|OSM|*yağ-|
rüzgârsız|adj|fa|rūzgār|rüzgârı olmayan|OSM||
güneşsiz|adj|tr|kün|güneşi olmayan|OSM|*kün|
gölgesiz|adj|tr|kölige|gölgesi olmayan|OSM|*kölige|
yıldızsız|adj|tr|yultuz|yıldızı olmayan|OSM|*yultuz|
nemsiz|adj|fa|nam|nemi olmayan|TDK||
susuzluk|n|tr|sub|su yokluğu|DLT|*sub|
kabarmak|v|tr|kabar-|şişmek; deniz yükselmek|DLT||
kabarma|n|tr|kabar-|deniz yükselmesi|TDK||
kabarık|adj|tr|kabar-|şişkin|OSM||
çekilme|n|tr|çek-|denizin alçalması|TDK|*çek-|
fışkırmak|v|tr|fışkır-|güçle dışarı çıkmak|OSM||
fışkırma|n|tr|fışkır-|güçle dışarı çıkma|TDK||
çatlamak|v|tr|çatla-|yarılmak|EAT||
çökmek|v|tr|çök-|aşağı inmek, göçmek|DLT|*çök-|
çökelme|n|tr|çök-|dibe çökme|DD|*çök-|
tutulmak|v|tr|tutul-|örtülmek; yakalanmak|DLT|*tut-|
dolanmak|v|tr|tola-|çevresinde dönmek|DLT||
çözülmek|v|tr|çöz-|erimek, gevşemek|DLT|*çöz-|
çözülme|n|tr|çöz-|buzun erimesi|TDK|*çöz-|
dumanlanmak|v|tr|tuman|dumanla kaplanmak|OSM||
bulanmak|v|tr|bulġa-|berraklığını yitirmek|DLT||
bulanık|adj|tr|bulġa-|berrak olmayan|DLT||
duru|adj|tr|turuġ|berrak|DLT||
berrak|adj|ar|barrāq|parlak, duru|OSM||
coşkun|adj|tr|çoş-|taşkın, azgın|OSM||
çağlamak|v|tr|çağla-|gürültüyle akmak|OSM||
şırıldamak|v|tr|şırıl|hafif sesle akmak|OSM||
şırıltı|n|tr|şırıl|hafif su sesi|OSM||
çağıltı|n|tr|çağla-|akarsu sesi|OSM||
tozlanmak|v|tr|toz|tozla kaplanmak|OSM||
bahri|adj|ar|baḥrī|denize ilişkin|OSM|B-H-R|
ufki|adj|ar|ufuqī|yatay|OSM||
şakuli|adj|ar|şāqūlī|düşey|OSM||
amudi|adj|ar|ʿamūdī|dikey|OSM||
düşey|adj|tr|tüş-|şakuli|DD|*düş-|
yüzölçümü|n|tr|yüz+ölç-|alan|DD||
kadem|n|ar|qadam|ayak; ayak ölçüsü|EAT||
karye|n|ar|qarya|köy|EAT||
diyar|n|ar|diyār|ülke, yurt|EAT|D-W-R|
mihver|n|ar|miḥwar|eksen|OSM||
eksen|n|el|áxōn|mil, dingil|DD||
istiva|n|ar|istiwāʾ|düz olma; ekvator çizgisi|OSM||
afitap|n|fa|āftāb|güneş|OSM||
ahter|n|fa|aḫtar|yıldız|OSM||
sipihr|n|fa|sipihr|gök|OSM||
gerdun|n|fa|gardūn|dönen gök; felek|OSM||
voli|n|el|bolí|ağ atma yeri|OSM||
kıstak|n|tr|kıs-|berzah|DD||
berzah|n|ar|barzaḫ|iki deniz arası kara; ara âlem|EAT||
akanyıldız|n|tr|ak-+yultuz|göktaşı|DD|*yultuz|
Büyükayı|prop|tr|bedük+adıġ|takımyıldız|OSM||
Küçükayı|prop|tr|kiçig+adıġ|takımyıldız|OSM||
Kervankıran|prop|fa|kārvān+kır-|sabah yıldızı|OSM||
günbatımı|n|tr|kün|güneşin batışı|TDK|*kün|
gündoğumu|n|tr|kün|güneşin doğuşu|TDK|*kün|
fırtınalı|adj|it|fortuna|fırtınası olan|OSM|fortuna|
sonda|n|fr|sonde|yoklama aleti|CUM||
coğrafyacı|n|ar|juġrāfiyā|coğrafya bilgini|CUM|gē|
coğrafi|adj|ar|juġrāfī|coğrafyaya ilişkin|OSM19|gē|
iklimbilim|n|ar|iqlīm|klimatoloji|DD|klima|
denizbilim|n|tr|teŋiz+bil-|oşinografi|DD|*teŋiz|
madenbilim|n|ar|maʿdin|mineraloji|DD|A-D-N|
taşbilim|n|tr|taş+bil-|petrografi|DD|*taş|
yeryuvarı|n|tr|yer+yuvar|yerküre|DD|*yer|
yerölçüm|n|tr|yer+ölç-|jeodezi|DD|*yer|
Rumeli|prop|el|Rōmanía|Rumların ülkesi; Balkanlar|OSM||
Trakya|prop|el|Thrákē|Trakya|OSM||
Marmara|prop|el|mármaron|mermer|EAT||
Boğaziçi|prop|tr|boġaz+iç|İstanbul Boğazı|OSM|*boğ-|
Kıbrıs|prop|el|Kýpros|bakır adası|EAT||
Kafkas|prop|el|Kaúkasos|Kafkas Dağları|OSM||
Hazar|prop|tr|Hazar|Hazar kavmi; Hazar Denizi|OSM||
Tuna|prop|hu|Duna|Tuna Irmağı|EAT||la:Danubius>hu:Duna>tr:Tuna
Fırat|prop|ar|Furāt|Fırat Irmağı|EAT||akk:Purattu>ar:Furāt>tr:Fırat
Dicle|prop|ar|Dijla|Dicle Irmağı|EAT||akk:Idiglat>ar:Dijla>tr:Dicle
Kızılırmak|prop|tr|kızıl+ırmak|Kızılırmak|OSM||
Meriç|prop|sl|Marica|Meriç Irmağı|OSM||
uzunluk|n|tr|uzun|uzun olma|DLT||
genişlik|n|tr|keŋ|geniş olma|DLT||
uruk|n|tr|uruġ|soy, boy; tohum|DLT||
kayağantaş|n|tr|kayağan+taş|şist|DD|*taş|
ılıklık|n|tr|ılı-|ılık olma|OSM|*ılı-|
yaşlık|n|tr|yaş|ıslaklık|DLT||
nemlilik|n|fa|nam|nemli olma|TDK||
bulutluluk|n|tr|bulıt|bulutlu olma|TDK|*bulıt|
yağışsız|adj|tr|yaġ-|yağışı olmayan|TDK|*yağ-|
sulanma|n|tr|sub|su verilme|TDK|*sub|
sulanmak|v|tr|sub|su verilmek; sulu olmak|DLT|*sub|
kurutma|n|tr|kurı-|kurutma işi|OSM|*kuru-|
kuruma|n|tr|kurı-|kuru duruma gelme|OSM|*kuru-|
kuruluk|n|tr|kurı-|kuru olma|OSM|*kuru-|
kuraklaşma|n|tr|kurı-|kurak duruma gelme|TDK|*kuru-|
yükselme|n|tr|yük-|yükselme olayı|OSM|*yük-|
alçalma|n|tr|alçak|alçak duruma gelme|TDK||
dalgalanma|n|tr|dalga|dalga oluşması|TDK||
dalgalanmak|v|tr|dalga|dalga oluşmak|OSM||
dinginlik|n|tr|tin-|durgunluk|DD||
durgunluk|n|tr|tur-|durgun olma|OSM|*dur-|
sızıntı|n|tr|sız-|sızan su|OSM||
sızma|n|tr|sız-|sızma olayı|TDK||
yarılma|n|tr|yar-|yarılma olayı|TDK|*yar-|
yarılmak|v|tr|yar-|ikiye ayrılmak|DLT|*yar-|
ufalanmak|v|tr|ufa-|küçük parçalara ayrılmak|OSM||
ufalanma|n|tr|ufa-|parçalanma|TDK||
parçalanma|n|fa|pārçe|parçalara ayrılma|TDK||
aşınım|n|tr|aşın-|erozyon|DD|*aşın-|
yığın|n|tr|yıġ-|üst üste birikmiş küme|DLT||
yığılma|n|tr|yıġ-|yığın oluşması|TDK||
taşınma|n|tr|taşı-|bir yerden başka yere gitme|OSM|*taşı-|
sürüklenme|n|tr|sürü-|akıntıyla taşınma|TDK|*sür-|
sürüklenmek|v|tr|sürü-|akıntıyla taşınmak|OSM|*sür-|
sürükleme|n|tr|sürü-|sürükleme işi|TDK|*sür-|
çatlaklı|adj|tr|çatla-|çatlağı olan|TDK||
tümsekli|adj|tr|tümsek|tümseği olan|TDK||
engebesiz|adj|tr|engebe|düz|TDK||
kıvrım|n|tr|kıvır-|bükülmüş yer; kat|DD||
kıvrımlı|adj|tr|kıvır-|kıvrımı olan|TDK||
kıvrılmak|v|tr|kıvır-|bükülmek|OSM||
büklüm|n|tr|bük-|kıvrım|OSM||
buzullaşma|n|tr|buz|buzul oluşması|TDK|*buz|
ağaçlanmak|v|tr|yıġaç|ağaçla kaplanmak|OSM||
ağaçlandırma|n|tr|yıġaç|ağaç dikme|TDK||
yeşillenmek|v|tr|yaşıl|yeşil olmak|OSM||
yeşermek|v|tr|yaşar-|yeşil duruma gelmek|DLT||
gürleme|n|tr|gür|gürleme sesi|OSM|*gür-|
uğultulu|adj|tr|uğul|uğultusu olan|TDK||
ışıksız|adj|tr|yaşu-|ışığı olmayan|OSM|*ışı-|
göllenmek|v|tr|köl|göl gibi birikmek|OSM||
nemlenme|n|fa|nam|nem kazanma|TDK||
buharlaşma|n|ar|buḫār|buhara dönüşme|TDK||
buğulanma|n|tr|buġ|buğu kaplama|TDK||
yoğunlaşma|n|tr|yoġun|buharın suya dönüşmesi|DD||
"""

FAMILIES = r"""
*kuz|tr|gölgeli yan, kuzey|Eski Türkçe kuz "güneş görmeyen dağ yanı"; kuzey (Dil Devrimi), kuzeyli, kuzeybatı ve kuzeydoğu aynı kökten türer.
*kök|tr|gök, mavi|Eski Türkçe kök "gök; mavi"; gökyüzü, gökbilim, gökada, göktaşı, gökkuşağı, gökçe ve gökdelen aynı kökten gelir.
*yultuz|tr|yıldız|Eski Türkçe yultuz "yıldız"; yıldızlı, takımyıldız ve yıldızname aynı kökten türer.
*ay|tr|ay|Eski Türkçe ay "gök cismi; otuz gün"; ayça, aydede, ayla (hale), dolunay ve aydın (ay ışığı) aynı kökten gelir.
*taş|tr|taş|Eski Türkçe taş; taşlık, taşlı, taşlaşmak, taşıl (fosil), kumtaşı, kireçtaşı ve çakmaktaşı aynı kökten türer.
*kum|tr|kum|Eski Türkçe kum "ince taş"; kumul, kumluk ve kumlu aynı kökten gelir.
*kaya|tr|kaya|Eski Türkçe kaya "büyük taş"; kayalık ve kayaç (Dil Devrimi) aynı kökten türer.
*tağ|tr|dağ|Orhun Yazıtları'ndaki tağ "dağ"; dağlık, dağcı, dağcılık, dağlı ve sıradağ aynı kökten gelir.
*töpü|tr|tepe|Eski Türkçe töpü "tepe, baş üstü"; tepelik ve tepecik aynı kökten türer.
*kır|tr|yüksek yer, bozkır|Eski Türkçe kır "yüksek yer, sırt"; bozkır, kırsal, kırlık ve kıraç aynı kökten gelir.
*çöl|tr|çöl|Eski Türkçe çöl "kurak alan"; çölleşmek ve çölleşme aynı kökten türer.
*yer|tr|yer, yeryüzü|Orhun Yazıtları'ndaki yer; yerel, yerli, yerleşmek, yerleşim, yerleşke, yeryüzü, yerküre, yeraltı ve yerbilim aynı kökten gelir.
*sub|tr|su|Eski Türkçe sub "su"; sulak, sulu, susuz, suyolu ve subasar aynı kökten türer.
*ada|tr|ada|Eski Türkçe ada; adacık ve takımada aynı kökten gelir.
*teŋiz|tr|deniz|Orhun Yazıtları'ndaki teŋiz "deniz"; denizel ve denizaşırı aynı kökten türer.
*buz|tr|buz|Eski Türkçe buz; buzlu, buzlanmak, buzul, buzdağı, buzkıran ve buzluk aynı kökten gelir.
*kar|tr|kar|Eski Türkçe kar; karlı, kartopu ve karlık (kar kuyusu) aynı kökten türer.
*bulıt|tr|bulut|Eski Türkçe bulıt "bulut"; bulutlu, bulutsuz, bulutlanmak ve bulutsu (nebula) aynı kökten gelir.
*yağ-|tr|yağmak|Orhun Yazıtları'ndaki yağ- "gökten düşmek"; yağmak, yağdırmak, yağış, yağışlı, yağmurlu ve yağmurölçer aynı kökten türer.
*es-|tr|esmek|Eski Türkçe es- "rüzgâr esmek"; esinti ve estirmek aynı kökten gelir.
*gür-|tr|gürlemek|Ses yansımalı gür kökü; gürlemek ve gürüldemek aynı kökten türer.
*ılı-|tr|ılımak|Eski Türkçe ılı- "ılık olmak"; ılıca, ılıman, ılımak ve ılım (ekinoks) aynı kökten gelir.
*serin|tr|serin|Eski Türkçe serin; serinlik, serinlemek ve serinletmek aynı kökten türer.
*sars-|tr|sarsmak|Eski Anadolu Türkçesi sars- "sallamak"; sarsıntı, sarsmak ve sarsılmak aynı kökten gelir.
*aşın-|tr|aşınmak|Türkçe aşın- "yıpranmak"; aşınma, aşınmak ve aşındırmak aynı kökten türer.
*çök-|tr|çökmek|Eski Türkçe çök- "aşağı inmek"; çökme, çöküntü, çökel ve çökelti aynı kökten gelir.
*kay-|tr|kaymak|Eski Türkçe kay- "kaymak"; kayma ve kaygan aynı kökten türer.
*tort|tr|tortu|Eski Türkçe tort "dibe çöken"; tortu ve tortul aynı kökten gelir.
*oy-|tr|oymak|Eski Türkçe oy- "oymak"; oyuk ve oyuntu aynı kökten türer.
*eg-|tr|eğmek|Eski Türkçe eg- "eğmek"; eğim, eğimli ve eğik aynı kökten gelir.
*köç-|tr|göçmek|Eski Türkçe köç- "göçmek"; göçük, göçebe, göçer ve konargöçer aynı kökten türer.
*küz|tr|güz|Eski Türkçe küz "sonbahar"; güzün ve güzlük aynı kökten gelir.
*yırak|tr|uzak|Orhun Yazıtları'ndaki yırak "uzak"; ırak ve ıraksamak aynı kökten türer.
*yak-|tr|yaklaşmak|Eski Türkçe yak- "yaklaşmak"; yakınlık ve yakınlaşmak aynı kökten gelir.
*teriŋ|tr|derin|Orhun Yazıtları'ndaki teriŋ "derin"; derinlik ve derinleşmek aynı kökten türer.
*kölige|tr|gölge|Eski Türkçe kölige "gölge"; gölgeli, gölgelik, gölgelemek ve gölgelenmek aynı kökten gelir.
*çise-|tr|ince yağmak|Ses yansımalı çise kökü; çise, çisenti ve çiselemek aynı kökten türer.
*taş-|tr|taşmak|Eski Türkçe taş- "kabından aşmak"; taşmak ve taşkın aynı kökten gelir.
*arık|tr|su kanalı|Eski Türkçe arık "su yolu"; arık ve ark aynı kökten türer.
*parla-|tr|parlamak|Ses yansımalı parıl/pırıl kökü; parıltı, parıldamak ve pırıltı aynı kökten gelir.
Ş-R-Q|ar|doğmak, doğu|Arapça ş-r-q kökü "güneşin doğması"; şark, maşrık, şarklı, şarkiyat ve şarkiyatçı aynı kökten gelir; İtalyanca scirocco rüzgâr adı da bu kökten türer.
Ğ-R-B|ar|batmak, uzaklaşmak|Arapça ġ-r-b kökü "güneşin batması; uzak olmak"; garp, mağrip, gurup, gurbet, gurbetçi, garabet ve garipsemek aynı kökten gelir.
Ş-M-L|ar|kuzey; kapsamak|Arapça ş-m-l kökü; şimal (kuzey, sol), şümul, şamil, müştemilat, cihanşümul ve âlemşümul aynı kökten türer.
C-N-B|ar|yan, güney|Arapça c-n-b kökü "yan, kenar"; cenup, cenubi, canip, ecnebi (yabancı), içtinap ve cünüp aynı kökten gelir.
W-C-H|ar|yüz, yön|Arapça w-c-h kökü "yüz"; cihet, vecih, veçhe, tevcih, teveccüh ve müteveccih aynı kökten türer.
S-M-W|ar|yüksek olmak, gök|Arapça s-m-w kökü "yükselmek"; sema, semavi ve semavat aynı kökten gelir.
C-B-L|ar|dağ; yaratılış|Arapça c-b-l kökü; cebel (dağ) ve cibilliyet (yaratılış) aynı kökten gelir.
H-W-A|ar|hava, boşluk|Arapça h-w-ʾ kökü; heva, havai, havadar, havalanmak, havalı, havacı, havacılık, havaalanı ve havayolu aynı kökten türer.
C-W-H|ar|cevher, öz|Farsça gawhar'dan Arapçalaşan c-w-h-r kökü; cevher, cevheri, cevahir, mücevher ve mücevherat aynı kökten gelir.
S-Y-L|ar|akmak, sel|Arapça s-y-l kökü; sel, seylap, seyelan ve seyyal aynı kökten türer.
C-Z-R|ar|kesmek, ada|Arapça c-z-r kökü; cezir (çekilme), cezire (ada) ve Cezayir (adalar) aynı kökten türer.
Ş-A-L|ar|alevlenmek|Arapça ş-ʿ-l kökü; şule, meşale ve iştial aynı kökten gelir.
S-F-L|ar|aşağı olmak|Arapça s-f-l kökü; süfli, sefil, esfel ve sefalet aynı kökten türer.
Z-W-L|ar|yok olmak, kaymak|Arapça z-w-l kökü; zeval, zail ve izale aynı kökten gelir.
R-K-M|ar|işaretlemek|Arapça r-q-m kökü; rakım, rakam ve merkum aynı kökten türer.
A-L-W|ar|yüksek olmak|Arapça ʿ-l-w kökü; ulvi, âli ve teali aynı kökten gelir.
Ḥ-C-R|ar|taş; kısıtlamak|Arapça ḥ-c-r kökü; hacer (taş), hücre (küçük oda), hacir (kısıtlama) ve mahcur aynı kökten türer. Hicret ve muhacir, h-c-r "göç etmek" kökünden gelen ayrı bir ailedir.
S-M-T|ar|yön|Arapça s-m-t kökü "yol, yön"; semt, zenit (samt ar-raʾs) ve azimut (as-sumūt) aynı kökten gelir.
R-S-D|ar|gözetlemek|Arapça r-ṣ-d kökü; rasat, rasathane ve rasıt aynı kökten türer.
D-N-W|ar|yakın olmak, dünya|Arapça d-n-w kökü "yakın olmak"; dünya, dünyevi ve dünyalık aynı kökten türer.
C-W-R|ar|komşuluk|Arapça c-w-r kökü; civar ve mücavir aynı kökten gelir.
H-W-T|ar|kuşatmak|Arapça ḥ-w-ṭ kökü; muhit ve ihata aynı kökten türer.
M-Y-L|ar|eğilmek|Arapça m-y-l kökü; meyil, meyilli, mail ve temayül aynı kökten gelir.
S-D-D|ar|kapatmak, set|Arapça s-d-d kökü; set ve sedde aynı kökten türer.
D-W-A|ar|ışık|Arapça ḍ-w-ʾ kökü; ziya ve ziyadar aynı kökten gelir.
gūşe|fa|köşe|Farsça gūşe "köşe, kulak ucu"; köşe, köşeli ve köşebaşı aynı kökten türer.
māh|fa|ay|Farsça māh "ay"; mehtap (ay ışığı) ve mehtaplı aynı kökten gelir.
vīrān|fa|yıkık|Farsça vīrān "yıkık"; viran ve virane aynı kökten türer.
seismos|el|sarsıntı|Eski Yunanca seismós "sarsıntı"; sismik, sismograf, sismoloji ve sismolog aynı kökten gelir.
klima|el|eğim, iklim|Eski Yunanca klíma "eğim, iklim kuşağı"; iklim (Arapça yoluyla), klima, klimatoloji ve klimatolog aynı kökten türer.
meteōros|el|havada yükselen|Eski Yunanca metéōros "havada asılı"; meteor, meteorit, meteoroloji ve meteorolog aynı kökten gelir.
tropos|el|dönüş|Eski Yunanca trópos "dönüş"; tropik, tropikal ve subtropikal aynı kökten türer.
aequus|la|eşit|Latince aequus "eşit"; ekvator, ekvatoral ve ekinoks aynı kökten gelir.
vulcanus|la|ateş tanrısı|Latince Vulcanus; volkan, volkanik ve vulkanoloji aynı kökten türer.
R-F-A|ar|yükselmek|Arapça r-f-ʿ kökü; irtifa (yükseklik), mürtefi (yüksek), refi (yüce) ve terfi (yükseltme) aynı kökten türer.
-zār|fa|yer, bahçe|Farsça -zār "yer, bahçe" eki; çemenzar, lalezar ve gülzar bu ekle kurulur.
"""

COGNATES = r"""@yayla shared_ancestor
  az yaylaq ; yayla
  kk жайлау [jaylaw] ; yaz otlağı
  ky жайлоо [jayloo] ; yaz otlağı
  uz yaylov ; yaz otlağı
  tk ýaýla ; yayla
  ru яйла [yayla] ; Kırım dağlarındaki yüksek otlak ; ff:Rusçada yalnızca Kırım'daki yüksek platolar için kullanılan bir terimdir
  bg яйла [yayla] ; dağ otlağı
@bayır from_turkish
  az bayır ; bayır
  bg баир [bair] ; tepe, yokuş
  mk баир [bair] ; tepe
@çay shared_ancestor
  az çay ; ırmak ; ff:Azericede çay hem "ırmak" hem "çay içeceği" demektir
  tk çaý ; dere ; ff:Türkmencede çaý hem "dere" hem "çay içeceği"
  kk шай [şay] ; çay içeceği ; ff:Kazakçada шай yalnızca içecek anlamındadır; akarsu için өзен kullanılır
@bulak shared_ancestor
  az bulaq ; pınar
  kk бұлақ [bulaq] ; pınar
  ky булак [bulak] ; pınar
  uz buloq ; pınar
  tk bulak ; pınar
  mn булаг [bulag] ; pınar
@balkan from_turkish
  bg Балкан [Balkan] ; Balkan Dağları; yarımada
  sr Балкан [Balkan] ; Balkan yarımadası
  ro Balcani ; Balkanlar
  en Balkan ; Balkan ; ff:Batı dillerinde yalnızca yarımadanın adıdır; Türkçede "sarp ormanlık dağ" ortak adı da yaşar
  de Balkan ; Balkan
  tk Balkan ; Türkmenistan'daki Balkan Dağları ; ff:Türkmencede Hazar kıyısındaki dağ silsilesinin adıdır
  ru балка [balka] ; kuru dere, sel yatağı ; ff:Rusça balka "dere yatağı" Türkçe balkan ile ilişkilendirilir; anlam dağdan vadiye kaymıştır
@kışla from_turkish
  ro câșlă ; koyun ağılı, kışlak ; ff:Romencede askerî anlam yoktur; yalnızca koyun kışlağı
  bg къшла [kışla] ; koyun ağılı
  az qışla ; kışla
  kk қыстау [qıstaw] ; kışlak
  ky кыштоо [kıştoo] ; kışlak
  uz qishloq ; köy ; ff:Özbekçede qishloq "köy" demektir; kış konağı anlamı yerleşim adına dönüşmüştür
  tk gyşlag ; kışlak
@yurt from_turkish
  ru юрта [yurta] ; keçe çadır ; ff:Rusçada yalnızca göçebe çadırı demektir; Türkçedeki "vatan" anlamı yoktur
  uk юрта [yurta] ; keçe çadır
  en yurt ; keçe çadır ; ff:İngilizcede yurt "yuvarlak göçebe çadırı"dır
  fr yourte ; keçe çadır
  de Jurte ; keçe çadır
  pl jurta ; keçe çadır
  hu jurta ; keçe çadır
  az yurd ; vatan
  kk жұрт [jurt] ; halk, memleket ; ff:Kazakçada jurt öncelikle "halk, el" demektir
  ky журт [jurt] ; halk, ülke
  uz yurt ; ülke, vatan
  tk ýurt ; ülke
@step into_turkish
  ru степь [step'] ; bozkır
  en steppe ; bozkır
  fr steppe ; bozkır
  de Steppe ; bozkır
  pl step ; bozkır
  hu sztyeppe ; bozkır
  bg степ [step] ; bozkır
  ro stepă ; bozkır
@tayga into_turkish
  ru тайга [tayga] ; kuzey iğne yapraklı ormanı
  en taiga ; tayga
  fr taïga ; tayga
  de Taiga ; tayga
  kk тайга [tayga] ; tayga
  mn тайга [taiga] ; tayga
@yar shared_ancestor
  az yar ; uçurum
  kk жар [jar] ; uçurum, dik kıyı
  ky жар [jar] ; uçurum
  tk ýar ; uçurum
  ru яр [yar] ; dik kıyı, uçurum ; ff:Rusçaya Türk dillerinden geçmiştir; Krasnoyarsk adı "kızıl yar" demektir
  uk яр [yar] ; derin vadi, dere yatağı
  pl jar ; dar vadi, kanyon
@balçık shared_ancestor
  az palçıq ; çamur
  kk балшық [balşıq] ; çamur
  ky балчык [balçık] ; çamur
  uz balchiq ; çamur
  tk palçyk ; çamur
@tuzla from_turkish
  sr Тузла [Tuzla] ; Bosna'daki Tuzla kenti ; ff:Sırpçada yalnızca tuz ocağı kentinin adıdır
  bg тузла [tuzla] ; tuz gölü
  ro Tuzla ; Köstence yakınındaki yerleşim
  ru тузлук [tuzluk] ; salamura ; ff:Rusça tuzluk "tuzlu su, salamura" demektir; Türkçede tuzluk "tuz kabı"dır
@kum shared_ancestor
  az qum ; kum
  kk құм [qum] ; kum ; ff:Kızılkum ve Karakum çöl adları aynı sözcüğü taşır
  ky кум [kum] ; kum
  uz qum ; kum
  tk gum ; kum
@kaya shared_ancestor
  az qaya ; kaya
  kk қия [qiya] ; dik yamaç ; ff:Kazakçada qiya "dik yamaç, yokuş" anlamına kaymıştır
  ky кыя [kıya] ; yamaç ; ff:Kırgızcada kıya "dağ yamacı" demektir
  uz qoya ; kaya
  tk gaýa ; kaya
@yel shared_ancestor
  az yel ; rüzgâr
  kk жел [jel] ; rüzgâr
  ky жел [jel] ; rüzgâr
  uz yel ; rüzgâr
  tk ýel ; rüzgâr
@bulut shared_ancestor
  az bulud ; bulut
  kk бұлт [bult] ; bulut
  ky булут [bulut] ; bulut
  uz bulut ; bulut
  tk bulut ; bulut
@kar shared_ancestor
  az qar ; kar
  kk қар [qar] ; kar
  ky кар [kar] ; kar
  uz qor ; kar
  tk gar ; kar
@buz shared_ancestor
  az buz ; buz
  kk мұз [muz] ; buz ; ff:Kazakça ve Kırgızcada b- > m- değişimiyle muz biçimindedir
  ky муз [muz] ; buz
  uz muz ; buz
  tk buz ; buz
@yağmur shared_ancestor
  az yağmur ; yağmur
  kk жаңбыр [jañbır] ; yağmur
  ky жамгыр [jamgır] ; yağmur
  uz yomgʻir ; yağmur
  tk ýagyş ; yağmur ; ff:Türkmencede ýagyş genel "yağış" sözcüğü yağmur anlamında kullanılır
@yıldız shared_ancestor
  az ulduz ; yıldız
  kk жұлдыз [juldız] ; yıldız
  ky жылдыз [jıldız] ; yıldız
  uz yulduz ; yıldız
  tk ýyldyz ; yıldız
@güneş shared_ancestor
  az günəş ; güneş
  kk күн [kün] ; güneş; gün ; ff:Kazakçada kün hem "güneş" hem "gün" demektir
  ky күн [kün] ; güneş; gün
  tk gün ; güneş; gün
  uz quyosh ; güneş ; ff:Özbekçe quyosh ayrı bir sözcüktür; kun "gün" demektir
@ayaz shared_ancestor
  az ayaz ; ayaz
  kk аяз [ayaz] ; ayaz, şiddetli soğuk ; ff:Kazakçada Аяз Ата "Ayaz Dede" Noel Baba karşılığıdır
  ky аяз [ayaz] ; ayaz
  uz ayoz ; ayaz
  tk aýaz ; ayaz
@boran shared_ancestor
  kk боран [boran] ; kar fırtınası, tipi
  ky бороон [boroon] ; fırtına
  uz boʻron ; fırtına
  mn бороо [boroo] ; yağmur ; ff:Moğolcada boroo "yağmur" demektir; Türkçede fırtına anlamı öne çıkar
  ru буран [buran] ; kar fırtınası ; ff:Rusçaya Türk dillerinden geçmiştir; Buran uzay mekiğinin adı da budur
@çöl shared_ancestor
  az çöl ; çöl; kır ; ff:Azericede çöl "kır, açık arazi" anlamında da kullanılır
  kk шөл [şöl] ; çöl
  ky чөл [çöl] ; çöl
  uz choʻl ; çöl
  tk çöl ; çöl
@kır shared_ancestor
  kk қыр [qır] ; sırt, yüksek bozkır ; ff:Kazakçada qır "dağ sırtı, yüksek yer" anlamını korur
  ky кыр [kır] ; sırt, dağ beli
  uz qir ; tepe, yükselti
  tk gyr ; sırt
@tepe shared_ancestor
  az təpə ; tepe
  kk төбе [töbe] ; tepe; başın üstü ; ff:Kazakçada töbe "başın tepesi" anlamı da canlıdır
  ky төбө [töbö] ; tepe
  uz tepa ; tepe
  tk depe ; tepe
  bg тепе [tepe] ; tepe ; ff:Bulgarcada ağızlarda ve yer adlarında (Айтепе) yaşar
@bataklık shared_ancestor
  az bataqlıq ; bataklık
  kk батпақ [batpaq] ; bataklık
  ky баткак [batkak] ; bataklık
  uz botqoq ; bataklık
@orman shared_ancestor
  az orman ; orman
  kk орман [orman] ; orman
  uz oʻrmon ; orman
  bg орман [orman] ; orman ; ff:Bulgarcada halk dilinde ve yer adlarında (Орманлия) kullanılır
@göl shared_ancestor
  az göl ; göl
  kk көл [köl] ; göl
  ky көл [köl] ; göl ; ff:Issık-Göl adı "ılık göl" demektir
  uz koʻl ; göl
  tk köl ; göl
@dere into_turkish
  fa دره [darre] ; vadi, dere ; ff:Farsçada darre "vadi" demektir; Türkçede "küçük akarsu" anlamı öne çıkmıştır
  az dərə ; dere, vadi
  uz dara ; dağ geçidi, vadi
  tk dere ; dere
  ur درہ [dara] ; dağ geçidi ; ff:Urducada dara "dağ geçidi" demektir (Hayber Geçidi: Darra-i Hayber)
@ada shared_ancestor
  az ada ; ada
  tk ada ; ada
  kk арал [aral] ; ada ; ff:Kazakçada ada için aral kullanılır; Aral Gölü adı buradan gelir
  ky арал [aral] ; ada
  uz orol ; ada
@toprak shared_ancestor
  az torpaq ; toprak
  kk топырақ [topıraq] ; toprak
  ky топурак [topurak] ; toprak
  uz tuproq ; toprak
  tk toprak ; toprak
@yer shared_ancestor
  az yer ; yer
  kk жер [jer] ; yer, toprak
  ky жер [jer] ; yer
  uz yer ; yer
  tk ýer ; yer
@tan shared_ancestor
  az dan ; tan
  kk таң [tañ] ; tan
  ky таң [tañ] ; tan
  uz tong ; tan
  tk daň ; tan
@bahar shared_ancestor
  az bahar ; bahar
  uz bahor ; bahar
  tk bahar ; bahar
  fa بهار [bahār] ; ilkbahar
  ur بہار [bahār] ; ilkbahar
@güz shared_ancestor
  kk күз [küz] ; sonbahar
  ky күз [küz] ; sonbahar
  uz kuz ; sonbahar
  tk güýz ; sonbahar
  az payız ; sonbahar ; ff:Azericede güz yerine Farsça kökenli payız kullanılır
@sel shared_ancestor
  az sel ; sel
  uz sel ; sel
  tk sil ; sel
  kk сел [sel] ; sel
  ky сел [sel] ; sel
  fa سیل [seyl] ; sel
  ar سيل [sayl] ; sel
  ur سیل [sail] ; sel
@tufan shared_ancestor
  az tufan ; tufan, fırtına
  uz toʻfon ; tufan
  fa طوفان [tūfān] ; fırtına, tufan
  ar طوفان [ṭūfān] ; tufan
  ur طوفان [tūfān] ; fırtına ; ff:Urducada tūfān günlük dilde her tür fırtına için kullanılır
  kk топан [topan] ; tufan
  ky топон [topon] ; tufan
  sq tufan ; fırtına, tufan
  en typhoon ; tayfun ; ff:İngilizce typhoon Çince kökenlidir; Arapça ṭūfān ile biçim benzerliği rastlantısal sayılır
@bora shared_ancestor
  el μπόρα [bóra] ; sağanak, fırtına
  it bora ; Adriyatik'in kuzeydoğu rüzgârı
  sr бура [bura] ; kuzeydoğu rüzgârı
  bg буря [burya] ; fırtına ; ff:Bulgarca burya Slavca kökenlidir; Yunanca-Latince bóra ile ses benzerliği yanıltıcıdır
  ro bură ; çisenti, ince yağmur ; ff:Romencede bură "çisenti" anlamına kaymıştır
  hu bóra ; Adriyatik rüzgârı
@muson shared_ancestor
  ar موسم [mawsim] ; mevsim ; ff:Arapça mawsim "mevsim" sözcüğü Portekizce yoluyla Avrupa dillerinde "muson" adına dönüşmüştür
  pt monção ; muson
  en monsoon ; muson
  fr mousson ; muson
  de Monsun ; muson
  es monzón ; muson
  it monsone ; muson
  ur موسم [mausam] ; hava durumu; mevsim ; ff:Urducada mausam günlük dilde "hava durumu" demektir
  fa موسم [mowsem] ; mevsim
@mevsim shared_ancestor
  az mövsüm ; mevsim
  uz mavsum ; mevsim
  fa موسم [mowsem] ; mevsim
  ar موسم [mawsim] ; mevsim; hac zamanı
  ur موسم [mausam] ; hava durumu; mevsim
  en monsoon ; muson ; ff:İngilizce monsoon aynı Arapça sözcüğün Portekizce üzerinden dönüşmüş biçimidir
@hava shared_ancestor
  az hava ; hava
  uz havo ; hava
  tk howa ; hava
  fa هوا [havā] ; hava; heves
  ar هواء [hawāʾ] ; hava
  ur ہوا [havā] ; hava; rüzgâr
  sq hava ; hava ; ff:Arnavutçada daha çok "hava durumu, iklim" anlamında kullanılır
@iklim shared_ancestor
  az iqlim ; iklim
  uz iqlim ; iklim
  fa اقلیم [eqlīm] ; iklim; bölge
  ar إقليم [iqlīm] ; bölge, il ; ff:Arapçada iqlīm bugün yönetim bölgesi demektir; hava anlamı için manāḫ kullanılır
  ur اقلیم [iqlīm] ; ülke, bölge
  en climate ; iklim
  fr climat ; iklim
  el κλίμα [klíma] ; iklim
@rüzgâr into_turkish
  fa روزگار [rūzgār] ; zaman, devir; dünya ; ff:Farsçada rūzgār "zaman, devran" demektir; "yel" anlamı yalnızca Türkçede gelişmiştir
  az ruzigar ; zaman, devran ; ff:Azericede rüzgâr anlamı için külək kullanılır
  ur روزگار [rozgār] ; geçim, iş ; ff:Urducada rozgār "iş, geçim" anlamına kaymıştır
@felek shared_ancestor
  az fələk ; felek
  uz falak ; gök; talih
  fa فلک [falak] ; gök küresi; talih
  ar فلك [falak] ; yörünge; gök küresi ; ff:Arapçada ʿilm al-falak "astronomi" demektir
  ur فلک [falak] ; gök
@kamer shared_ancestor
  az qəmər ; ay
  fa قمر [qamar] ; ay; uydu ; ff:Farsça ve Arapçada qamar bugün "yapay uydu" anlamında da kullanılır
  ar قمر [qamar] ; ay
  ur قمر [qamar] ; ay
@şems shared_ancestor
  az şəms ; güneş
  fa شمس [şams] ; güneş
  ar شمس [şams] ; güneş
  ur شمس [şams] ; güneş
  he שמש [shemesh] ; güneş ; ff:İbranice shemesh Arapça şams ile ortak Sami köktendir
@ufuk shared_ancestor
  az üfüq ; ufuk
  uz ufq ; ufuk
  fa افق [ofoq] ; ufuk
  ar أفق [ufuq] ; ufuk
  ur افق [ufaq] ; ufuk
@kutup shared_ancestor
  az qütb ; kutup
  uz qutb ; kutup
  fa قطب [qoṭb] ; kutup; önder
  ar قطب [quṭb] ; kutup; eksen
  ur قطب [qutb] ; kutup; Kutup Yıldızı
@cenup shared_ancestor
  az cənub ; güney
  uz janub ; güney
  fa جنوب [jonūb] ; güney
  ar جنوب [janūb] ; güney
  ur جنوب [janūb] ; güney
@şimal shared_ancestor
  az şimal ; kuzey
  uz shimol ; kuzey
  fa شمال [şomāl] ; kuzey
  ar شمال [şimāl] ; kuzey; sol ; ff:Arapçada şimāl aynı zamanda "sol taraf" demektir
  ur شمال [şimāl] ; kuzey
@şark shared_ancestor
  az şərq ; doğu
  uz sharq ; doğu
  fa شرق [şarq] ; doğu
  ar شرق [şarq] ; doğu
  ur مشرق [maşriq] ; doğu ; ff:Urducada doğu için maşriq biçimi yaygındır
  it scirocco ; sıcak güneydoğu rüzgârı ; ff:İtalyanca scirocco Arapça şarqī "doğulu" sıfatından gelir
@garp shared_ancestor
  az qərb ; batı
  uz gʻarb ; batı
  fa غرب [ġarb] ; batı
  ar غرب [ġarb] ; batı
  ur مغرب [maġrib] ; batı ; ff:Urducada batı için maġrib biçimi yaygındır
@mağrip shared_ancestor
  az Məğrib ; Kuzeybatı Afrika
  fa مغرب [maġreb] ; batı; akşam namazı
  ar المغرب [al-maġrib] ; Fas; batı ; ff:Arapçada al-Maġrib bugün Fas ülkesinin adıdır
  ur مغرب [maġrib] ; batı; akşam namazı
  es Magreb ; Kuzeybatı Afrika
  fr Maghreb ; Kuzeybatı Afrika
  en Maghreb ; Kuzeybatı Afrika
@gurbet shared_ancestor
  az qürbət ; gurbet
  uz gʻurbat ; yoksulluk ; ff:Özbekçede gʻurbat "yoksulluk, düşkünlük" anlamına kaymıştır
  fa غربت [ġorbat] ; gurbet; yabancılık
  ar غربة [ġurba] ; gurbet, yabancılık
  ur غربت [ġurbat] ; yoksulluk ; ff:Urducada ġurbat "yoksulluk" demektir
@cevher shared_ancestor
  az cövhər ; cevher
  uz javhar ; öz ; ff:Özbekçede javhar daha çok "öz, töz" anlamındadır
  fa گوهر [gowhar] ; inci; öz
  ar جوهر [jawhar] ; öz; mücevher
  ur جوہر [jauhar] ; öz; cevher
@elmas shared_ancestor
  az almaz ; elmas
  kk алмас [almas] ; elmas
  ky алмаз [almaz] ; elmas
  uz olmos ; elmas
  tk almaz ; elmas
  ru алмаз [almaz] ; ham elmas ; ff:Rusçaya Türk dillerinden geçmiştir; işlenmiş elmas için бриллиант kullanılır
  uk алмаз [almaz] ; elmas
  fa الماس [almās] ; elmas
  ar ألماس [almās] ; elmas
  el αδάμας [adámas] ; elmas; yenilmez ; ff:Eski Yunanca adámas "boyun eğmez" demektir; İngilizce diamond da buradan gelir
@zümrüt shared_ancestor
  az zümrüd ; zümrüt
  uz zumrad ; zümrüt
  fa زمرد [zomorrod] ; zümrüt
  ar زمرد [zumurrud] ; zümrüt
  ur زمرد [zumurrud] ; zümrüt
  ru изумруд [izumrud] ; zümrüt ; ff:Rusçaya Farsça-Türkçe yoluyla geçmiştir
  el σμαράγδι [smarágdi] ; zümrüt
  en emerald ; zümrüt
  fr émeraude ; zümrüt
  hu smaragd ; zümrüt
  pl szmaragd ; zümrüt
@yakut shared_ancestor
  az yaqut ; yakut
  uz yoqut ; yakut
  fa یاقوت [yāqūt] ; yakut
  ar ياقوت [yāqūt] ; yakut
  ur یاقوت [yāqūt] ; yakut
  ru яхонт [yakhont] ; yakut, safir (eski) ; ff:Eski Rusçada yakhont hem kırmızı hem mavi değerli taşları karşılardı
  el υάκινθος [yákinthos] ; sümbül ; ff:Yunancada sözcük önce "sümbül" çiçeğidir; taş anlamı Arapçada gelişmiştir
  en hyacinth ; sümbül ; ff:İngilizce hyacinth çiçek adıdır; taş adı değildir
@firuze shared_ancestor
  az firuzə ; firuze
  uz feruza ; firuze
  fa فیروزه [fīrūze] ; firuze
  ar فيروز [fayrūz] ; firuze
  ur فیروزہ [fīroza] ; firuze
  ru бирюза [biryuza] ; firuze ; ff:Rusçaya Farsçadan geçmiştir
  en turquoise ; firuze ; ff:İngilizce turquoise "Türk taşı" demektir; taş Avrupa'ya Türkiye üzerinden ulaşmıştır
@lal shared_ancestor
  fa لعل [laʿl] ; kırmızı taş, lal
  ar لعل [laʿl] ; lal taşı
  ur لعل [laʿl] ; lal; yakut
  az lal ; dilsiz ; ff:Azericede lal "dilsiz" demektir; Farsça lāl "dilsiz" ile laʿl "taş" ayrı sözcüklerdir
@sedef shared_ancestor
  az sədəf ; sedef
  uz sadaf ; sedef
  fa صدف [ṣadaf] ; sedef; istiridye
  ar صدف [ṣadaf] ; sedef; deniz kabuğu
  ur صدف [ṣadaf] ; sedef
  bg седеф [sedef] ; sedef
  sr седеф [sedef] ; sedef
  mk седеф [sedef] ; sedef
  sq sedef ; sedef
  ro sidef ; sedef
@akik shared_ancestor
  az əqiq ; akik
  uz aqiq ; akik
  fa عقیق [ʿaqīq] ; akik
  ar عقيق [ʿaqīq] ; akik
  ur عقیق [ʿaqīq] ; akik
@billur shared_ancestor
  az büllur ; billur
  uz billur ; billur
  fa بلور [bolūr] ; kristal
  ar بلور [billawr] ; kristal
  ur بلور [bilaur] ; kristal
  el βήρυλλος [vírillos] ; beril taşı ; ff:Yunanca bḗryllos "beril" adıdır; gözlük anlamındaki Almanca Brille de buradan gelir
  en beryl ; beril ; ff:İngilizce beryl yalnızca beril mineralidir
@kükürt shared_ancestor
  az kükürd ; kükürt
  kk күкірт [kükirt] ; kükürt
  ky күкүрт [kükürt] ; kükürt
  uz oltingugurt ; kükürt ; ff:Özbekçe oltingugurt "altın kükürt" bileşiğidir
  tk kükürt ; kükürt
  fa گوگرد [gūgerd] ; kükürt
@kireç from_turkish
  sr креч [kreč] ; kireç
  mk креч [kreč] ; kireç
  bg киреч [kireç] ; kireç
  sq kireç ; kireç ; ff:Arnavutçada ölçünlü sözcük gëlqere olup kireç ağızlarda yaşar
@çayır from_turkish
  bg чаир [çair] ; çayır
  sr чаир [čair] ; çayır
  mk чаир [čair] ; çayır
  sq çair ; çayır
  ru чаир [chair] ; Kırım dağ bahçesi ; ff:Rusçada Kırım Tatarlarına özgü meyve bahçeleri için kullanılan bir terimdir
@çukur shared_ancestor
  az çuxur ; çukur
  kk шұңқыр [şuñqır] ; çukur
  ky чуңкур [çuñkur] ; çukur
  uz chuqur ; derin ; ff:Özbekçede chuqur "derin" demektir; çukur için chuqurlik kullanılır
  tk çukur ; çukur
@kanyon shared_ancestor
  es cañón ; kanyon; top ; ff:İspanyolca cañón hem "boru, top" hem "derin vadi" demektir
  en canyon ; kanyon
  fr canyon ; kanyon
  ru каньон [kan'on] ; kanyon
  bg каньон [kanyon] ; kanyon
@plato shared_ancestor
  fr plateau ; yüksek düzlük; tepsi ; ff:Fransızcada plateau aynı zamanda "tepsi, platform" demektir
  en plateau ; plato
  ru плато [plato] ; plato
  bg плато [plato] ; plato
  ro platou ; plato
  sr плато [plato] ; plato
@delta shared_ancestor
  el δέλτα [délta] ; delta harfi; ırmak deltası
  en delta ; delta
  fr delta ; delta
  ru дельта [del'ta] ; delta
  bg делта [delta] ; delta
  ar دلتا [daltā] ; delta
  hu delta ; delta
@krater shared_ancestor
  el κρατήρας [kratíras] ; krater; şarap karıştırma kabı ; ff:Eski Yunanca kratḗr büyük şarap kabıdır; biçim benzerliğinden yanardağ ağzına aktarılmıştır
  en crater ; krater
  fr cratère ; krater
  de Krater ; krater
  ru кратер [krater] ; krater
  it cratere ; krater
  hu kráter ; krater
@magma shared_ancestor
  en magma ; magma
  fr magma ; magma
  el μάγμα [mágma] ; hamur; magma ; ff:Yunanca mágma "yoğrulmuş hamur" demektir
  ru магма [magma] ; magma
  de Magma ; magma
@tsunami shared_ancestor
  en tsunami ; tsunami
  fr tsunami ; tsunami
  ru цунами [tsunami] ; tsunami
  de Tsunami ; tsunami
  ar تسونامي [tsūnāmī] ; tsunami
@tornado shared_ancestor
  es tornado ; hortum
  en tornado ; hortum
  fr tornade ; hortum
  ru торнадо [tornado] ; hortum
  de Tornado ; hortum
@karst shared_ancestor
  de Karst ; karst
  en karst ; karst
  fr karst ; karst
  ru карст [karst] ; karst
  sr крас [kras] ; Kras platosu; karst ; ff:Sırpça kras kireçtaşı bölgesinin yerel adıdır
  it carso ; karst
  hu karszt ; karst
@dolin shared_ancestor
  fr doline ; çökme çukuru
  en doline ; çökme çukuru
  de Doline ; çökme çukuru
  sr долина [dolina] ; vadi ; ff:Sırpçada dolina genel olarak "vadi" demektir; terim anlamı dardır
  ru долина [dolina] ; vadi ; ff:Rusçada dolina "vadi" demektir
  bg долина [dolina] ; vadi
  pl dolina ; vadi
  uk долина [dolyna] ; vadi
@lagün shared_ancestor
  fr lagune ; lagün
  it laguna ; lagün; Venedik lagünü
  en lagoon ; lagün
  es laguna ; küçük göl ; ff:İspanyolcada laguna "gölcük" demektir
  pt lagoa ; göl ; ff:Portekizcede lagoa "göl" anlamındadır
  ru лагуна [laguna] ; lagün
  de Lagune ; lagün
@resif shared_ancestor
  ar رصيف [raṣīf] ; kaldırım; rıhtım ; ff:Arapça raṣīf "kaldırım, rıhtım" demektir; İspanyolca arrecife yoluyla "kayalık" anlamını almıştır
  es arrecife ; resif
  fr récif ; resif
  en reef ; resif
  de Riff ; resif
  ru риф [rif] ; resif
  pt recife ; resif; Recife kenti
@atol shared_ancestor
  fr atoll ; mercan adası
  en atoll ; mercan adası
  de Atoll ; mercan adası
  ru атолл [atoll] ; mercan adası
@moren shared_ancestor
  fr moraine ; moren
  en moraine ; moren
  de Moräne ; moren
  ru морена [morena] ; moren
  it morena ; moren
@aysberg shared_ancestor
  en iceberg ; buz dağı
  de Eisberg ; buz dağı
  fr iceberg ; buz dağı
  ru айсберг [aysberg] ; buz dağı
  es iceberg ; buz dağı
@savan shared_ancestor
  fr savane ; savan
  es sabana ; savan; çarşaf ; ff:İspanyolcada sábana "çarşaf" ile sabana "savan" ayrı sözcüklerdir
  en savanna ; savan
  pt savana ; savan
  ru саванна [savanna] ; savan
  de Savanne ; savan
@pampa shared_ancestor
  es pampa ; pampa
  en pampas ; pampa
  fr pampa ; pampa
  ru пампа [pampa] ; pampa
  pt pampa ; pampa
@fiyort shared_ancestor
  en fjord ; fiyort
  fr fjord ; fiyort
  de Fjord ; fiyort
  ru фьорд [f'ord] ; fiyort
  es fiordo ; fiyort
  it fiordo ; fiyort
  pl fiord ; fiyort
@humus shared_ancestor
  en humus ; humus ; ff:İngilizce hummus (nohut ezmesi) Arapça ḥummuṣ'tan gelir ve bu sözcükle ilgisizdir
  fr humus ; humus
  de Humus ; humus
  ru гумус [gumus] ; humus
  es humus ; humus
@turba shared_ancestor
  fr tourbe ; turba
  it torba ; turba
  de Torf ; turba
  ru торф [torf] ; turba
  pl torf ; turba
  en turf ; çim, çimen ; ff:İngilizce turf aynı Germen kökten gelir ama "çim örtüsü" demektir
@linyit shared_ancestor
  fr lignite ; linyit
  en lignite ; linyit
  ru лигнит [lignit] ; linyit
  es lignito ; linyit
  it lignite ; linyit
@antrasit shared_ancestor
  en anthracite ; antrasit
  fr anthracite ; antrasit
  ru антрацит [antratsit] ; antrasit
  de Anthrazit ; antrasit
  el ανθρακίτης [anthrakítis] ; antrasit
  it antracite ; antrasit
@bazalt shared_ancestor
  fr basalte ; bazalt
  en basalt ; bazalt
  de Basalt ; bazalt
  ru базальт [bazal't] ; bazalt
  it basalto ; bazalt
  es basalto ; bazalt
  el βασάλτης [vasáltis] ; bazalt
@kuvars shared_ancestor
  de Quarz ; kuvars
  fr quartz ; kuvars
  en quartz ; kuvars
  ru кварц [kvarts] ; kuvars
  it quarzo ; kuvars
  pl kwarc ; kuvars
  hu kvarc ; kuvars
@mika shared_ancestor
  fr mica ; mika
  en mica ; mika
  es mica ; mika
  it mica ; kırıntı; hiç ; ff:İtalyancada mica "kırıntı" ve olumsuzluk pekiştiricisi "hiç" anlamındadır; mineral için de kullanılır
  de Glimmer ; mika ; ff:Almancada mika için Latince kökenli sözcük yerine Glimmer kullanılır
@obsidyen shared_ancestor
  fr obsidienne ; obsidyen
  en obsidian ; obsidyen
  es obsidiana ; obsidyen
  de Obsidian ; obsidyen
  ru обсидиан [obsidian] ; obsidyen
@jips shared_ancestor
  fr gypse ; jips
  en gypsum ; jips
  el γύψος [gýpsos] ; alçı
  de Gips ; alçı
  ru гипс [gips] ; alçı
  it gesso ; alçı; tebeşir ; ff:İtalyanca gesso "tebeşir" anlamında da kullanılır
  es yeso ; alçı
  pl gips ; alçı
  hu gipsz ; alçı
  ar جبس [jibs] ; alçı
  fa گچ [gaç] ; alçı
@boksit shared_ancestor
  fr bauxite ; boksit
  en bauxite ; boksit
  de Bauxit ; boksit
  ru боксит [boksit] ; boksit
  it bauxite ; boksit
@uranyum shared_ancestor
  fr uranium ; uranyum
  en uranium ; uranyum
  de Uran ; uranyum
  ru уран [uran] ; uranyum; Uranüs ; ff:Rusçada uran hem elementi hem gezegeni karşılar
  it uranio ; uranyum
  es uranio ; uranyum
  ar يورانيوم [yūrānyūm] ; uranyum
  el ουράνιο [ouránio] ; uranyum
@alüminyum shared_ancestor
  fr aluminium ; alüminyum
  en aluminium ; alüminyum
  de Aluminium ; alüminyum
  ru алюминий [alyuminiy] ; alüminyum
  it alluminio ; alüminyum
  es aluminio ; alüminyum
  ar ألومنيوم [alūmnyūm] ; alüminyum
  el αλουμίνιο [aloumínio] ; alüminyum
  hu alumínium ; alüminyum
  pl aluminium ; alüminyum
@nikel shared_ancestor
  fr nickel ; nikel
  en nickel ; nikel; beş sent ; ff:Amerikan İngilizcesinde nickel "beş sentlik madenî para"dır
  de Nickel ; nikel
  ru никель [nikel'] ; nikel
  it nichel ; nikel
  es níquel ; nikel
  pl nikiel ; nikel
  hu nikkel ; nikel
  el νικέλιο [nikélio] ; nikel
@kobalt shared_ancestor
  de Kobalt ; kobalt ; ff:Almanca Kobold "maden cini" sözcüğünden; madenciler cevheri cinlerin bozduğunu sanırdı
  en cobalt ; kobalt
  fr cobalt ; kobalt
  ru кобальт [kobal't] ; kobalt
  it cobalto ; kobalt
  es cobalto ; kobalt
  pl kobalt ; kobalt
@manganez shared_ancestor
  it manganese ; manganez
  fr manganèse ; manganez
  en manganese ; manganez
  de Mangan ; manganez
  ru марганец [marganets] ; manganez
  es manganeso ; manganez
  el μαγγάνιο [mangánio] ; manganez
@platin shared_ancestor
  es platina ; gümüşçük ; ff:İspanyolca platina "küçük gümüş" demektir; element adı buradan türemiştir
  fr platine ; platin
  en platinum ; platin
  de Platin ; platin
  ru платина [platina] ; platin
  it platino ; platin
  pl platyna ; platin
  hu platina ; platin
  ar بلاتين [blātīn] ; platin
  el πλατίνα [platína] ; platin
@tungsten shared_ancestor
  en tungsten ; tungsten
  de Wolfram ; tungsten ; ff:Almanca ve Türkçe volfram "kurt köpüğü" adını kullanır; kimyasal simge W buradan gelir
  ru вольфрам [vol'fram] ; tungsten
  fr tungstène ; tungsten
  es wolframio ; tungsten
  it tungsteno ; tungsten
  pl wolfram ; tungsten
@fosfat shared_ancestor
  fr phosphate ; fosfat
  en phosphate ; fosfat
  de Phosphat ; fosfat
  ru фосфат [fosfat] ; fosfat
  it fosfato ; fosfat
  es fosfato ; fosfat
  ar فوسفات [fūsfāt] ; fosfat
@nitrat shared_ancestor
  fr nitrate ; nitrat
  en nitrate ; nitrat
  de Nitrat ; nitrat
  ru нитрат [nitrat] ; nitrat
  es nitrato ; nitrat
  it nitrato ; nitrat
@boraks shared_ancestor
  ar بورق [bawraq] ; boraks
  fa بوره [būre] ; boraks
  en borax ; boraks
  fr borax ; boraks
  de Borax ; boraks
  ru бура [bura] ; boraks ; ff:Rusça bura "boraks" ile буря "fırtına" karıştırılmamalıdır
  it borace ; boraks
  es bórax ; boraks
@meteor shared_ancestor
  el μετέωρο [metéoro] ; göktaşı; havada asılı ; ff:Yunanca metéōros "havada yükselen" demektir; Meteora manastırlarının adı da budur
  en meteor ; meteor
  fr météore ; meteor
  de Meteor ; meteor
  ru метеор [meteor] ; meteor
  it meteora ; meteor
  es meteoro ; meteor
  hu meteor ; meteor
  pl meteor ; meteor
  bg метеор [meteor] ; meteor
@meteoroloji shared_ancestor
  en meteorology ; meteoroloji
  fr météorologie ; meteoroloji
  el μετεωρολογία [meteorología] ; meteoroloji
  ru метеорология [meteorologiya] ; meteoroloji
  de Meteorologie ; meteoroloji
  es meteorología ; meteoroloji
@galaksi shared_ancestor
  el γαλαξίας [galaxías] ; Samanyolu; galaksi ; ff:Yunanca gála "süt" kökünden; Türkçe Samanyolu ise saman imgesine dayanır
  en galaxy ; galaksi
  fr galaxie ; galaksi
  ru галактика [galaktika] ; galaksi
  de Galaxie ; galaksi
  it galassia ; galaksi
  es galaxia ; galaksi
  bg галактика [galaktika] ; galaksi
  hu galaxis ; galaksi
@nebula shared_ancestor
  en nebula ; bulutsu
  fr nébuleuse ; bulutsu
  de Nebel ; sis ; ff:Almanca Nebel aynı Hint-Avrupa kökten gelir ama "sis" demektir
  it nebbia ; sis ; ff:İtalyanca nebbia "sis" anlamındadır; bulutsu için nebulosa kullanılır
  es nebulosa ; bulutsu
@atmosfer shared_ancestor
  en atmosphere ; atmosfer
  fr atmosphère ; atmosfer
  de Atmosphäre ; atmosfer
  ru атмосфера [atmosfera] ; atmosfer
  el ατμόσφαιρα [atmósfaira] ; atmosfer ; ff:Yunanca atmós "buhar" ve sphaîra "küre" ögelerinden kurulmuştur
  it atmosfera ; atmosfer
  es atmósfera ; atmosfer
  hu atmoszféra ; atmosfer
  pl atmosfera ; atmosfer
  bg атмосфера [atmosfera] ; atmosfer
@ozon shared_ancestor
  en ozone ; ozon
  fr ozone ; ozon
  de Ozon ; ozon
  ru озон [ozon] ; ozon
  el όζον [ózon] ; ozon ; ff:Yunanca ózein "kokmak" fiilinden; gazın keskin kokusuna göre adlandırılmıştır
  it ozono ; ozon
@ekvator shared_ancestor
  en equator ; ekvator
  fr équateur ; ekvator
  de Äquator ; ekvator
  ru экватор [ekvator] ; ekvator
  it equatore ; ekvator
  es ecuador ; ekvator; Ekvador ülkesi ; ff:İspanyolcada Ecuador hem ekvator çizgisi hem ülke adıdır
  pt equador ; ekvator
  bg екватор [ekvator] ; ekvator
@meridyen shared_ancestor
  fr méridien ; meridyen
  en meridian ; meridyen
  de Meridian ; meridyen
  ru меридиан [meridian] ; meridyen
  it meridiano ; meridyen; öğleye ilişkin ; ff:Latince meridies "öğle" kökünden; güneşin öğlede geçtiği çizgi anlamındadır
  es meridiano ; meridyen
@tropik shared_ancestor
  en tropic ; dönence
  fr tropique ; dönence
  el τροπικός [tropikós] ; dönence; dönüşe ilişkin ; ff:Yunanca tropḗ "dönüş" kökünden; güneşin geri döndüğü enlem demektir
  de Tropen ; tropikal bölge
  ru тропик [tropik] ; dönence
  es trópico ; dönence
  it tropico ; dönence
  pt trópico ; dönence
@alize shared_ancestor
  fr alizé ; alize
  es alisio ; alize
  pt alísio ; alize
  en trade wind ; alize ; ff:İngilizcede alize için "ticaret rüzgârı" karşılığı kullanılır
@fön shared_ancestor
  de Föhn ; sıcak dağ rüzgârı; saç kurutma makinesi ; ff:Almancada Föhn (marka adından) saç kurutma makinesi anlamına da gelir
  en foehn ; fön rüzgârı
  fr foehn ; fön rüzgârı
  it favonio ; ılık batı rüzgârı ; ff:İtalyanca favonio doğrudan Latince favonius'tan gelir
  ru фён [fyon] ; fön rüzgârı
@sirokko shared_ancestor
  it scirocco ; sıcak güneydoğu rüzgârı
  ar شرقي [şarqī] ; doğulu; doğu rüzgârı ; ff:Arapça şarqī "doğuya ait" sıfatı İtalyancada rüzgâr adına dönüşmüştür
  en sirocco ; sirokko
  fr sirocco ; sirokko
  es siroco ; sirokko
  de Schirokko ; sirokko
  el σιρόκος [sirókos] ; sirokko
  ru сирокко [sirokko] ; sirokko
@mistral shared_ancestor
  fr mistral ; mistral
  en mistral ; mistral
  it maestrale ; kuzeybatı rüzgârı ; ff:İtalyanca maestrale "usta rüzgâr" anlamını korur
  es mistral ; mistral
  de Mistral ; mistral
  ru мистраль [mistral'] ; mistral
@ekinoks shared_ancestor
  fr équinoxe ; ekinoks
  en equinox ; ekinoks
  it equinozio ; ekinoks
  es equinoccio ; ekinoks
  pt equinócio ; ekinoks
  de Äquinoktium ; ekinoks
@almanak shared_ancestor
  ar المناخ [al-manāḫ] ; iklim ; ff:Arapça manāḫ bugün "iklim" demektir; Orta Çağ'da takvim cetvelleri için kullanılmıştır
  fr almanach ; almanak
  en almanac ; almanak
  de Almanach ; almanak
  ru альманах [al'manakh] ; edebiyat derlemesi ; ff:Rusçada al'manakh "yıllık edebiyat seçkisi" demektir
  it almanacco ; almanak
  es almanaque ; almanak; takvim
  hu almanach ; almanak
  pl almanach ; almanak
@usturlap shared_ancestor
  ar أسطرلاب [asṭurlāb] ; usturlap
  el αστρολάβος [astrolávos] ; yıldız tutan ; ff:Yunanca astrolábos "yıldız yakalayan" demektir
  fa اسطرلاب [osṭorlāb] ; usturlap
  en astrolabe ; usturlap
  fr astrolabe ; usturlap
  es astrolabio ; usturlap
  ur اسطرلاب [asturlāb] ; usturlap
  ru астролябия [astrolyabiya] ; usturlap
@zenit shared_ancestor
  ar سمت [samt] ; yön; başucu ; ff:Arapça samt ar-raʾs "baş yönü" Latince yazıcıların hatasıyla zenit biçimine dönüşmüştür
  es cenit ; zenit
  fr zénith ; zenit
  en zenith ; zenit
  de Zenit ; zenit
  it zenit ; zenit
  ru зенит [zenit] ; zenit; Zenit kulübü ; ff:Rusçada Zenit St. Petersburg futbol kulübünün de adıdır
  pt zénite ; zenit
  pl zenit ; zenit
  hu zenit ; zenit
@azimut shared_ancestor
  ar السموت [as-sumūt] ; yönler
  fr azimut ; azimut
  en azimuth ; azimut
  es acimut ; azimut
  de Azimut ; azimut
  ru азимут [azimut] ; azimut
  it azimut ; azimut
  pl azymut ; azimut
@koordinat shared_ancestor
  fr coordonnée ; koordinat
  en coordinate ; koordinat
  de Koordinate ; koordinat
  ru координата [koordinata] ; koordinat
  it coordinata ; koordinat
  es coordenada ; koordinat
  bg координата [koordinata] ; koordinat
@navigasyon shared_ancestor
  fr navigation ; seyrüsefer
  en navigation ; seyrüsefer
  de Navigation ; seyrüsefer
  ru навигация [navigatsiya] ; seyrüsefer
  it navigazione ; seyrüsefer
  es navegación ; seyrüsefer
  pt navegação ; seyrüsefer
  pl nawigacja ; seyrüsefer
  hu navigáció ; seyrüsefer
@sekstant shared_ancestor
  fr sextant ; sekstant
  en sextant ; sekstant
  de Sextant ; sekstant
  ru секстант [sekstant] ; sekstant
  it sestante ; sekstant
  es sextante ; sekstant
  pl sekstant ; sekstant
@hektar shared_ancestor
  fr hectare ; hektar
  en hectare ; hektar
  de Hektar ; hektar
  ru гектар [gektar] ; hektar
  it ettaro ; hektar
  es hectárea ; hektar
  pt hectare ; hektar
  pl hektar ; hektar
  hu hektár ; hektar
  bg хектар [hektar] ; hektar
  ro hectar ; hektar
  sq hektar ; hektar
  ar هكتار [hiktār] ; hektar
  fa هکتار [hektār] ; hektar
@mil shared_ancestor
  en mile ; mil
  fr mille ; mil; bin ; ff:Fransızca mille hem "bin" sayısı hem "mil" ölçüsüdür
  de Meile ; mil
  ru миля [milya] ; mil
  it miglio ; mil
  es milla ; mil
  pt milha ; mil
  pl mila ; mil
  ar ميل [mīl] ; mil
  fa میل [mīl] ; mil; arzu ; ff:Farsça mīl "mil" ile meyl "arzu" ayrı kökenlidir
  ur میل [mīl] ; mil
@fersah shared_ancestor
  fa فرسنگ [farsang] ; fersah
  ar فرسخ [farsaḫ] ; fersah
  az fərsəx ; fersah
  uz farsax ; fersah
  ur فرسنگ [farsang] ; fersah
  el παρασάγγης [parasángis] ; fersah ; ff:Eski Yunanca parasángēs Ksenophon'un Anabasis'inde Pers yol ölçüsü olarak geçer
  en parasang ; fersah
@kulaç shared_ancestor
  az qulac ; kulaç
  kk құлаш [qulaş] ; kulaç
  ky кулач [kulaç] ; kulaç
  uz quloch ; kulaç
  tk gulaç ; kulaç
@arşın from_turkish
  ru аршин [arşin] ; arşın (71 cm) ; ff:Rusçada arşın Türk dillerinden alınmış ve 1918'e dek resmî uzunluk ölçüsü olmuştur
  uk аршин [arşyn] ; arşın
  bg аршин [arşin] ; arşın
  sr аршин [aršin] ; arşın
  ro arșin ; arşın
  pl arszyn ; arşın
  az arşın ; arşın
  kk аршын [arşın] ; arşın
  ky аршын [arşın] ; arşın
  uz arshin ; arşın
  tk arşyn ; arşın
@karış shared_ancestor
  az qarış ; karış
  kk қарыс [qarıs] ; karış
  ky карыш [karış] ; karış
  uz qarich ; karış
  tk garyş ; karış
@dönüm from_turkish
  bg дюнюм [dyunyum] ; dönüm
  sr дунум [dunum] ; dönüm
  mk дунум [dunum] ; dönüm
  sq dynym ; dönüm
  ar دونم [dūnam] ; dönüm (1000 m²) ; ff:Arapçada dönüm Osmanlı mirası olarak Filistin, Ürdün ve Irak'ta hâlâ resmî ölçüdür
  he דונם [dunam] ; dönüm ; ff:İbranicede dunam İsrail'de yasal arazi ölçüsüdür; Osmanlı tapu düzeninden kalmıştır
  el στρέμμα [strémma] ; dönüm ; ff:Yunanca strémma Türkçe sözcüğün çevirisi değil, ayrı bir sözcüktür; alan büyüklüğü aynıdır
@merkez shared_ancestor
  az mərkəz ; merkez
  uz markaz ; merkez
  fa مرکز [markaz] ; merkez
  ar مركز [markaz] ; merkez; karakol ; ff:Arapçada markaz "polis karakolu" anlamında da kullanılır
  ur مرکز [markaz] ; merkez
@mesafe shared_ancestor
  az məsafə ; mesafe
  uz masofa ; mesafe
  fa مسافت [masāfat] ; mesafe
  ar مسافة [masāfa] ; mesafe
  ur مسافت [masāfat] ; mesafe
@cihet shared_ancestor
  az cəhət ; yön; bakım
  uz jihat ; yön; bakım
  fa جهت [jahat] ; yön; sebep ; ff:Farsçada jahat daha çok "sebep, için" anlamında kullanılır
  ar جهة [jiha] ; yön; taraf
  ur جہت [jihat] ; yön; boyut
@köşe from_turkish
  bg кьоше [kyoşe] ; köşe
  sr ћоше [ćoše] ; köşe
  mk ќоше [kjoše] ; köşe
  sq qoshe ; köşe
@köşe into_turkish
  fa گوشه [gūşe] ; köşe; kenar; kulak memesi
  ur گوشہ [goşa] ; köşe; kuytu
  az guşə ; köşe
@kenar shared_ancestor
  az kənar ; kenar
  fa کنار [kanār] ; kenar; yan; sahil
  ur کنار [kinār] ; kenar; sahil
  bg кенар [kenar] ; kenarlı ince bez ; ff:Bulgarcada kenar Türkçe yoluyla "kenar dokumalı bez" anlamına kaymıştır
@nem shared_ancestor
  az nəm ; nem
  uz nam ; nem
  fa نم [nam] ; nem
  ur نم [nam] ; nem
@hararet shared_ancestor
  az hərarət ; hararet; ateş
  uz harorat ; sıcaklık
  fa حرارت [ḥarārat] ; sıcaklık
  ar حرارة [ḥarāra] ; sıcaklık
  ur حرارت [ḥarārat] ; sıcaklık
@şebnem shared_ancestor
  az şəbnəm ; çiy
  uz shabnam ; çiy
  fa شبنم [şabnam] ; çiy
  ur شبنم [şabnam] ; çiy; kadın adı
@hazan shared_ancestor
  az xəzan ; sonbahar
  uz xazon ; sonbahar
  fa خزان [ḫazān] ; sonbahar
  ur خزاں [ḫizāñ] ; sonbahar
@cemre shared_ancestor
  az cəmrə ; cemre
  fa جمره [jamre] ; kor; Mina'daki taşlama sütunu ; ff:Farsça ve Arapçada jamra hac sırasında taşlanan sütunları da adlandırır
  ar جمرة [jamra] ; kor, köz ; ff:Arapçada jamra "kor" demektir; ilkbahar sıcaklığı anlamı Türkçeye özgüdür
  ur جمرہ [jamra] ; kor
@girdap shared_ancestor
  az girdab ; girdap
  uz girdob ; girdap
  fa گرداب [gerdāb] ; girdap
  ur گرداب [girdāb] ; girdap
@nesim shared_ancestor
  az nəsim ; nesim
  uz nasim ; esinti
  fa نسیم [nasīm] ; esinti
  ar نسيم [nasīm] ; esinti
  ur نسیم [nasīm] ; esinti; kadın adı
@saba shared_ancestor
  az səba ; saba
  fa صبا [ṣabā] ; tan yeli
  ar صبا [ṣabā] ; doğu yeli
  ur صبا [ṣabā] ; tan yeli
@samyeli shared_ancestor
  ar سموم [samūm] ; zehirli sıcak rüzgâr
  fa سموم [samūm] ; samyeli
  en simoom ; samyeli
  fr simoun ; samyeli
  es simún ; samyeli
@feza shared_ancestor
  az fəza ; uzay
  uz fazo ; uzay
  fa فضا [fażā] ; uzay; ortam
  ar فضاء [faḍāʾ] ; uzay; boşluk
  ur فضا [fazā] ; atmosfer; uzay
@sema shared_ancestor
  az səma ; gök
  uz samo ; gök
  fa سما [samā] ; gök
  ar سماء [samāʾ] ; gök
  he שמים [shamayim] ; gökler ; ff:İbranice shamayim Arapça samāʾ ile ortak Sami köktendir
@arş shared_ancestor
  az ərş ; arş
  fa عرش [ʿarş] ; taht; gök
  ar عرش [ʿarş] ; taht ; ff:Arapçada ʿarş öncelikle "taht" demektir
  ur عرش [ʿarş] ; arş
@nücum shared_ancestor
  az nücum ; yıldızlar
  fa نجوم [nojūm] ; yıldızlar; astroloji
  ar نجوم [nujūm] ; yıldızlar
  ur نجوم [nujūm] ; yıldızlar; astroloji
@müneccim shared_ancestor
  az münəccim ; müneccim
  uz munajjim ; astrolog
  fa منجم [monajjem] ; astrolog
  ar منجّم [munajjim] ; astrolog
  ur منجم [munajjim] ; astrolog
@hilal shared_ancestor
  az hilal ; hilal
  uz hilol ; hilal
  fa هلال [helāl] ; hilal
  ar هلال [hilāl] ; hilal
  ur ہلال [hilāl] ; hilal
@bedir shared_ancestor
  fa بدر [badr] ; dolunay
  ar بدر [badr] ; dolunay; Bedir savaşı yeri
  ur بدر [badr] ; dolunay
@husuf shared_ancestor
  fa خسوف [ḫosūf] ; ay tutulması
  ar خسوف [ḫusūf] ; ay tutulması
  ur خسوف [ḫusūf] ; ay tutulması
@küsuf shared_ancestor
  fa کسوف [kosūf] ; güneş tutulması
  ar كسوف [kusūf] ; güneş tutulması
  ur کسوف [kusūf] ; güneş tutulması
@mehtap shared_ancestor
  az mehtab ; mehtap
  fa مهتاب [mahtāb] ; ay ışığı
  ur مہتاب [mahtāb] ; ay ışığı; ay
@Zühre shared_ancestor
  az Zöhrə ; Venüs
  fa زهره [Zohre] ; Venüs
  ar الزهرة [az-Zuhara] ; Venüs
  ur زہرہ [Zuhra] ; Venüs
@Merih shared_ancestor
  az Mərrix ; Mars
  fa مریخ [Merrīḫ] ; Mars
  ar المريخ [al-Mirrīḫ] ; Mars
  ur مریخ [Mirrīḫ] ; Mars
@Müşteri shared_ancestor
  fa مشتری [Moştarī] ; Jüpiter; müşteri ; ff:Farsça ve Arapçada aynı sözcük hem gezegen hem "alıcı" anlamındadır
  ar المشتري [al-Muştarī] ; Jüpiter
  ur مشتری [Muştarī] ; Jüpiter
@Zühal shared_ancestor
  az Zühəl ; Satürn
  fa زحل [Zoḥal] ; Satürn
  ar زحل [Zuḥal] ; Satürn
  ur زحل [Zuḥal] ; Satürn
@Utarit shared_ancestor
  fa عطارد [ʿOṭāred] ; Merkür
  ar عطارد [ʿUṭārid] ; Merkür
  ur عطارد [ʿUtārid] ; Merkür
@Ülker shared_ancestor
  az Ülkər ; Ülker
  kk Үркер [Ürker] ; Ülker
  ky Үркөр [Ürkör] ; Ülker
  uz Hulkar ; Ülker
  tk Ülker ; Ülker
@Süreyya shared_ancestor
  az Sürəyya ; Ülker
  fa ثریا [Sorayyā] ; Ülker; avize ; ff:Farsçada sorayyā "avize" anlamında da kullanılır
  ar الثريا [aṯ-Ṯurayyā] ; Ülker
  ur ثریا [Surayyā] ; Ülker
@Kehkeşan shared_ancestor
  az Kəhkəşan ; Samanyolu
  fa کهکشان [kahkeşān] ; Samanyolu; galaksi
  ur کہکشاں [kahkaşāñ] ; Samanyolu; galaksi
@Merkür shared_ancestor
  en Mercury ; Merkür
  fr Mercure ; Merkür
  de Merkur ; Merkür
  ru Меркурий [Merkuriy] ; Merkür
  it Mercurio ; Merkür
  es Mercurio ; Merkür
@Venüs shared_ancestor
  en Venus ; Venüs
  fr Vénus ; Venüs
  de Venus ; Venüs
  ru Венера [Venera] ; Venüs
  it Venere ; Venüs
  es Venus ; Venüs
@Mars shared_ancestor
  en Mars ; Mars
  fr Mars ; Mars; mart ayı ; ff:Fransızca mars aynı zamanda "mart ayı"dır
  de Mars ; Mars
  ru Марс [Mars] ; Mars
  it Marte ; Mars
  es Marte ; Mars
@Jüpiter shared_ancestor
  en Jupiter ; Jüpiter
  fr Jupiter ; Jüpiter
  de Jupiter ; Jüpiter
  ru Юпитер [Yupiter] ; Jüpiter
  it Giove ; Jüpiter ; ff:İtalyanca Giove Latince Iovis biçiminden gelir
  es Júpiter ; Jüpiter
@Satürn shared_ancestor
  en Saturn ; Satürn
  fr Saturne ; Satürn
  de Saturn ; Satürn
  ru Сатурн [Saturn] ; Satürn
  it Saturno ; Satürn
  es Saturno ; Satürn
@Uranüs shared_ancestor
  en Uranus ; Uranüs
  fr Uranus ; Uranüs
  de Uranus ; Uranüs
  ru Уран [Uran] ; Uranüs; uranyum
  it Urano ; Uranüs
  el Ουρανός [Ouranós] ; gök; Uranüs ; ff:Yunanca ouranós günlük dilde "gök" demektir
@Neptün shared_ancestor
  en Neptune ; Neptün
  fr Neptune ; Neptün
  de Neptun ; Neptün
  ru Нептун [Neptun] ; Neptün
  it Nettuno ; Neptün
  es Neptuno ; Neptün
@Plüton shared_ancestor
  en Pluto ; Plüton
  fr Pluton ; Plüton
  de Pluto ; Plüton
  ru Плутон [Pluton] ; Plüton
  it Plutone ; Plüton
  el Πλούτων [Ploúton] ; yer altı tanrısı; Plüton
@rasat shared_ancestor
  az rəsəd ; rasat
  uz rasad ; gözlem
  fa رصد [raṣad] ; gözlem
  ar رصد [raṣad] ; gözlem; bütçe ayırma ; ff:Arapçada raṣada bugün "ödenek ayırmak" anlamında da kullanılır
  ur رصد [raṣad] ; gözlem
@rasathane shared_ancestor
  az rəsədxana ; rasathane
  uz rasadxona ; rasathane
  fa رصدخانه [raṣadḫāne] ; rasathane
@Akrep shared_ancestor
  az Əqrəb ; Akrep burcu
  fa عقرب [ʿaqrab] ; akrep; Akrep burcu
  ar العقرب [al-ʿaqrab] ; Akrep burcu
  ur عقرب [ʿaqrab] ; akrep; Akrep burcu
@terazi shared_ancestor
  az tərəzi ; terazi
  uz tarozi ; terazi
  fa ترازو [tarāzū] ; terazi
  ur ترازو [tarāzū] ; terazi
  kk таразы [tarazı] ; terazi
  ky тараза [taraza] ; terazi
  tk terezi ; terazi
@fecir shared_ancestor
  az fəcr ; fecir
  fa فجر [fajr] ; tan; sabah namazı
  ar فجر [fajr] ; tan; sabah namazı
  ur فجر [fajr] ; sabah namazı
@gurup shared_ancestor
  az qürub ; gurup
  fa غروب [ġorūb] ; gün batımı
  ar غروب [ġurūb] ; gün batımı
  ur غروب [ġurūb] ; gün batımı
@tulu shared_ancestor
  fa طلوع [ṭolūʿ] ; doğuş
  ar طلوع [ṭulūʿ] ; doğuş; çıkış
  ur طلوع [tulūʿ] ; doğuş
@zeval shared_ancestor
  az zaval ; zeval
  fa زوال [zavāl] ; yok oluş; öğle sonrası
  ar زوال [zawāl] ; yok oluş; güneşin öğleyi geçmesi
  ur زوال [zavāl] ; çöküş; öğle vakti
@ırak shared_ancestor
  az iraq ; uzak ; ff:Azerice iraq "uzak" ile İraq ülke adı yalnızca sesçe benzer
  kk жырақ [jıraq] ; uzak
  ky ыраак [ıraak] ; uzak
  uz yiroq ; uzak
  tk ýyrak ; uzak
@dik shared_ancestor
  az dik ; dik
  kk тік [tik] ; dik
  ky тик [tik] ; dik
  uz tik ; dik
  tk dik ; dik
@uç shared_ancestor
  az uc ; uç
  kk ұш [uş] ; uç
  ky уч [uç] ; uç
  uz uch ; uç
  tk uç ; uç
@harabe shared_ancestor
  az xarabalıq ; harabe
  uz xaroba ; harabe
  fa خرابه [ḫarābe] ; harabe
  ar خرابة [ḫarāba] ; harabe
  ur خرابہ [ḫarāba] ; harabe
@antik shared_ancestor
  en antique ; antika ; ff:İngilizce antique "antika eşya" demektir; "eski çağ" için ancient kullanılır
  fr antique ; antik
  de antik ; antik
  ru античный [antichnıy] ; antik
  it antico ; eski
  es antiguo ; eski
@tamga shared_ancestor
  kk таңба [tañba] ; damga, boy işareti
  ky тамга [tamga] ; damga
  mn тамга [tamga] ; mühür
  ru тамга [tamga] ; tamga; damga ; ff:Rusçaya Altın Orda döneminde geçmiş; tamojnya (gümrük) sözcüğü de buradan türemiştir
@balbal shared_ancestor
  kk балбал [balbal] ; taş heykel
  ky балбал [balbal] ; taş heykel
  ru балбал [balbal] ; Türk mezar heykeli
@yörük from_turkish
  bg юруци [yurutsi] ; Yörükler
  mk Јуруци [Juruci] ; Yörükler
  el Γιουρούκοι [Giouroúki] ; Yörükler
@derbent shared_ancestor
  az Dərbənd ; Derbent kenti
  ru Дербент [Derbent] ; Dağıstan'daki Derbent kenti ; ff:Rusçada yalnızca kent adıdır; "geçit" anlamı yoktur
  fa دربند [darband] ; dağ geçidi; kapalı yer
@abat shared_ancestor
  az abad ; bayındır
  uz obod ; bayındır
  fa آباد [ābād] ; bayındır; şehir eki
  ur آباد [ābād] ; yerleşik; şehir eki ; ff:Urducada İslamabad, Haydarabad gibi kent adlarının ekidir
@viran shared_ancestor
  az viran ; viran
  uz vayron ; viran
  fa ویران [vīrān] ; yıkık
  ur ویران [vīrān] ; yıkık, ıssız
@mezra shared_ancestor
  fa مزرعه [mazraʿe] ; tarla, çiftlik ; ff:Farsçada mazraʿe "çiftlik" demektir; Türkçede küçük köy anlamı gelişmiştir
  ar مزرعة [mazraʿa] ; çiftlik
  ur مزرعہ [mazraʿa] ; çiftlik
  az məzrə ; mezra
@ağıl shared_ancestor
  az ağıl ; ağıl
  tk agyl ; ağıl
  uz ogʻil ; ahır ; ff:Özbekçede ogʻil "ahır" anlamındadır
  kk ауыл [awıl] ; köy ; ff:Kazakça awıl "köy" aynı sözcüğün gelişmiş biçimidir
  ky айыл [ayıl] ; köy
  ru аул [aul] ; Kafkas ve Orta Asya köyü ; ff:Rusçaya Türk dillerinden geçmiş; dağ köyü anlamındadır
@ılıca from_turkish
  sr Илиџа [Ilidža] ; Saraybosna'daki kaplıca semti ; ff:Sırpça-Boşnakçada yalnızca yer adı olarak yaşar
  bg Илиджа [Ilidja] ; kaplıca yer adı
@çermik into_turkish
  hy ջերմուկ [jermuk] ; kaplıca; Jermuk kenti
@burgaz into_turkish
  el πύργος [pýrgos] ; kule
  bg Бургас [Burgas] ; Burgas kenti ; ff:Bulgarca kent adı aynı Yunanca sözcükten gelir
@taşkın shared_ancestor
  az daşqın ; taşkın
  kk тасқын [tasqın] ; taşkın
  ky ташкын [taşkın] ; taşkın
  uz toshqin ; taşkın
@çiy shared_ancestor
  kk шық [şıq] ; çiy
  ky чык [çık] ; çiy
  tk çyg ; çiy
@şimşek shared_ancestor
  az şimşək ; şimşek
@köpük shared_ancestor
  az köpük ; köpük
  kk көбік [köbik] ; köpük
  ky көбүк [köbük] ; köpük
  uz koʻpik ; köpük
  tk köpük ; köpük
@tuzla shared_ancestor
  az duzlaq ; tuzla
  kk тұздық [tuzdıq] ; salamura ; ff:Kazakça tuzdıq "salamura, sos" demektir
"""
