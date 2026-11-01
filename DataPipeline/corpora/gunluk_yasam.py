# -*- coding: utf-8 -*-
"""Korpus 1 — Günlük yaşam: ev, eşya, giyim, alışveriş, ulaşım, meslekler, zaman, beden, duygu, eğitim, sağlık."""

WORDS = r"""
yatak odası|n|tr|yatgak|yatak odası|OSM|*yat-|
yastık kılıfı|n|tr|yastuk|kılıf|OSM||
kılıf|n|ar|ġilāf|kın, örtü|EAT||
çarşaflık|n|fa|çādir-şab|çarşaflık kumaş|OSM||
battaniye|n|ar|baṭṭāniyya|iç örtü|OSM||
yün battaniye|n|tr|yuŋ|battaniye|OSM||
nevresim|n|fa|nev-resm|yeni biçim|OSM19||
halıfleks|n|tr|kalı-fleks|duvardan duvara halı|MOD||
paspas|n|fr|paillasson|hasır|CUM||fr:paillasson>tr:paspas
süpürge|n|tr|süpürge|süpürme aleti|DLT||
süpürmek|v|tr|süpür-|temizlemek|DLT||
faraş|n|ar|farrāş|yayan; yer süpürücü|OSM||
çöp|n|fa|çōb|çubuk; atık|EAT||
kova|n|tr|kova|su kabı|DLT||
leğen|n|fa|lagan|geniş kap|EAT||
sabunluk|n|ar|ṣābūn|sabun kabı|OSM||
fırça|n|it?|forcia|fırça|OSM19||la:furca>it:forcia>tr:fırça
sünger taşı|n|el|sfoungári|sünger taşı|OSM||
deterjan|n|fr|détergent|temizleyen|MOD||la:detergere>fr:détergent>tr:deterjan
çamaşır|n|fa|cāme-şūy|giysi yıkama|EAT||
çamaşır makinesi|n|fa|cāme-şūy|çamaşır makinesi|MOD||
buzdolabı|n|tr|buz tolabı|soğutucu|CUM||
ocaklık|n|tr|oçak|ocak yeri|OSM||
fırın tepsisi|n|el|foúrnos|tepsi|OSM||
tencere kapağı|n|ar|ṭancara|kapak|OSM||
kepçe|n|fa|kafçe|büyük kaşık|EAT||
kevgir|n|fa|kafgīr|köpük alan|EAT||
rende|n|fa|rande|rende|EAT||
havan|n|fa|hāvan|dövme kabı|EAT||
tokmak|n|tr|tokmak|vurma aleti|DLT||
oklava|n|tr|oklagu|hamur açma çubuğu|DLT||
elek|n|tr|elgek|eleme aracı|DLT||
elemek|v|tr|elge-|elekten geçirmek|DLT||
güğüm|n|el|koukoúmi|su kabı|OSM||la:cucuma>el:koukoúmi>tr:güğüm
maşrapa|n|ar|maşraba|içme kabı|EAT||
kupa|n|it|coppa|kadeh|OSM19||la:cuppa>it:coppa>tr:kupa
kadeh|n|ar|qadaḥ|kadeh|EAT||
şişe kapağı|n|fa|şīşe|kapak|OSM||
mantar|n|el|manitári|mantar|EAT||grc:amanítēs>el:manitári>tr:mantar
tıpa|n|el|týpa|tıkaç|OSM||
kavanoz|n|fa|kāvanūz|cam kap|OSM||
bidon|n|fr|bidon|teneke kap|CUM||fr:bidon>tr:bidon
teneke|n|it|tenecca|ince sac|OSM||it:tenecca>tr:teneke
sepet|n|fa|sapad|sepet|EAT||
torba|n|fa|tōbre|çuval|EAT||
çuval|n|fa|cuvāl|büyük torba|EAT||
heybe|n|ar|ḥaqība|at torbası|EAT||
valiz|n|fr|valise|bavul|CUM||it:valigia>fr:valise>tr:valiz
çanta|n|tr|çanta|torba|OSM||
cüzdan çantası|n|fa|cuz-dān|cüzdan|OSM||
anahtarlık|n|el|anoichtíri|anahtar halkası|CUM||
kilit dili|n|el|kleidí|kilit dili|OSM||
sürgü|n|tr|sürgü|kapı sürgüsü|OSM|*sür-|
menteşe|n|fa|band-i şah|kapı bağı|OSM||
tokmak kapı|n|tr|tokmak|kapı tokmağı|OSM||
zil|n|fa|zīl|çan|EAT||
çan|n|tr|çaŋ|çan|DLT||
kapı zili|n|fa|zīl|kapı zili|MOD||
cumba|n|ar|cumba|çıkma|OSM||
kafes|n|ar|qafaṣ|kafes|EAT||
panjur|n|it|pancione|kafesli kapak|OSM19||it:pancione>tr:panjur
pervaz|n|fa|parvāz|çerçeve|EAT||
eşik taşı|n|tr|éşik|eşik|OSM||
kiremit çatı|n|el|keramídi|çatı|OSM||
çatı|n|tr|çatı|dam|OSM|*çat-|
baca|n|fa|bāce|pencere; baca|EAT||
dam|n|tr|tam|dam, çatı|DLT||
kiler odası|n|el|kellári|kiler|OSM||
ambar|n|fa|anbār|depo|EAT||
mahzen|n|ar|maḫzan|depo|EAT||
sığınaklık|n|tr|sığınak|sığınak|MOD|*sığ-|
bodrum|n|el|ipódromos|yer altı|OSM||grc:hippódromos>el:ipódromos>tr:bodrum
asma kat|n|tr|asma|ara kat|MOD||
asmak|v|tr|as-|asmak|DLT||
askı|n|tr|askı|asma yeri|OSM||
çengel|n|fa|çangāl|kanca|EAT||
kanca|n|it|gancio|çengel|OSM||it:gancio>tr:kanca
çivi|n|tr|çıbı|çivi|DLT||
vida somunu|n|it|vite|somun|OSM19||
somun|n|el|psōmí|ekmek; cıvata somunu|EAT||grc:psōmíon>el:psōmí>tr:somun
cıvata|n|it|chiavarda|cıvata|OSM19||it:chiavarda>tr:cıvata
pense|n|fr|pince|kıskaç|CUM||fr:pince>tr:pense
tornavida ucu|n|it|tornavite|uç|CUM||
testere|n|fa|dast-arra|el bıçkısı|EAT||
keser|n|tr|keser|kesme aleti|DLT|*kes-|
törpü|n|tr|törpü|aşındırma aleti|OSM||
matkap|n|ar|miṯqab|delgi|OSM||
makas|n|ar|miqaṣṣ|kesme aleti|EAT||
cetvel|n|ar|cadwal|çizelge; çizgilik|OSM||
pergel|n|fa|pargār|daire çizen|EAT||
silgi|n|tr|silgi|silme aracı|DD||
silmek|v|tr|sil-|silmek|DLT||
kalemtıraş|n|ar|qalam-tırāş|kalem yontan|OSM||
zımba|n|fa|zanbūr?|delgeç|CUM||
dosya|n|fr|dossier|belge kabı|CUM||fr:dossier>tr:dosya
klasör|n|fr|classeur|sıralayıcı|CUM||fr:classeur>tr:klasör
zarf kâğıdı|n|ar|ẕarf|zarf|OSM||
pul|n|fa|pūl|para; posta pulu|EAT||grc:obolós>fa:pūl>tr:pul
damga|n|tr|tamga|işaret, mühür|ORH||
mühür|n|fa|muhr|mühür|EAT||
imza|n|ar|imḏāʾ|imza|OSM||
takvim yaprağı|n|ar|taqwīm|takvim|OSM||
saat kulesi|n|ar|sāʿa|saat kulesi|OSM||
çalar saat|n|ar|sāʿa|alarm saati|CUM||
kol saati|n|ar|sāʿa|kol saati|CUM||
gömlek yakası|n|tr|köŋlek|yaka|OSM||
pantolon askısı|n|fr|pantalon|askı|CUM||
etek ucu|n|tr|etek|etek|OSM||
elbise askısı|n|ar|albisa|askı|OSM||
kumaş topu|n|ar|qumāş|top|OSM||
yün kazak|n|tr|yuŋ|kazak|CUM||
hırka|n|ar|ḫirqa|yün giysi|EAT||
cüppe|n|ar|cubba|üst giysi|EAT||
kaftan kuşağı|n|fa|ḫaftān|kuşak|OSM||
şalvar|n|fa|şalvār|bol pantolon|EAT||
cepken|n|tr|cepken|kısa ceket|OSM||
yelek düğmesi|n|ar|yalak|düğme|OSM||
fermuar|n|fr|fermoir|kapatıcı|CUM||fr:fermoir>tr:fermuar
kemer tokası|n|fa|kemer|toka|OSM||
toka|n|it|tocca|kopça|OSM||it:tocca>tr:toka
kopça|n|sl|kopča|kopça|OSM||sr:kopča>tr:kopça
iğne oyası|n|tr|yigne|oya|OSM||
oya|n|el|oýa|dantel|OSM||
nakış|n|ar|naqş|işleme|EAT||
işleme|n|tr|işleme|nakış|OSM||
terlik|n|tr|terlik|ev ayakkabısı|OSM||
sandalet|n|fr|sandalette|hafif ayakkabı|CUM||grc:sándalon>fr:sandalette>tr:sandalet
bot|n|fr|botte|çizme|CUM||fr:botte>tr:bot
çarık|n|tr|çaruk|köylü ayakkabısı|DLT||
nalın|n|ar|naʿlayn|iki nal; takunya|EAT||
takunya|n|el|tsókara|tahta ayakkabı|OSM||
galoş|n|fr|galoche|lastik ayakkabı|CUM||fr:galoche>tr:galoş
pantolon paçası|n|fa|pāçe|paça|OSM|pā|
şapka siperi|n|sl|šapka|siper|CUM||
siper|n|fa|sipar|kalkan; korunak|EAT||
yağmurluk|n|tr|yagmur|yağmurluk|OSM||
şemsiye|n|ar|şamsiyya|güneşlik|OSM||
gözlük camı|n|tr|gözlük|cam|OSM|*kör-|
kolye|n|fr|collier|boyunluk|CUM||la:collum>fr:collier>tr:kolye
gerdanlık|n|fa|gardan|boyun süsü|EAT||
gerdan|n|fa|gardan|boyun|EAT||
broş|n|fr|broche|iğne|CUM||fr:broche>tr:broş
taç yaprağı|n|fa|tāc|taç|OSM||
nişan yüzüğü|n|fa|nişān|yüzük|OSM||
nişan|n|fa|nişān|işaret|EAT||
alışveriş listesi|n|tr|alış veriş|liste|MOD|*al-|
liste|n|fr|liste|çizelge|OSM19||it:lista>fr:liste>tr:liste
fiş fiyatı|n|fr|fiche|fiyat|MOD||
etiket|n|fr|étiquette|yafta|OSM19||fr:étiquette>tr:etiket
indirim kuponu|n|tr|indirim|kupon|MOD|*in-|
kupon|n|fr|coupon|kesilen parça|CUM||fr:coupon>tr:kupon
kasiyer|n|fr|caissier|kasa görevlisi|CUM||fr:caissier>tr:kasiyer
tezgâhtar|n|fa|dast-gāh-dār|tezgâh tutan|OSM|dār-|
müşteri|n|ar|muştarī|satın alan|EAT|Ş-R-K|
veresiye|n|tr|véresiye|sonra ödemeli|OSM|*ver-|
peşin|n|fa|pīşīn|önden|EAT||
taksit|n|ar|taqsīṭ|bölüştürme|OSM19||
kredi|n|fr|crédit|güven|OSM19||la:creditum>fr:crédit>tr:kredi
borçlu|adj|sog|pwrc|borcu olan|OSM||
alacak|n|tr|alacak|alınacak para|OSM|*al-|
kâr payı|n|fa|kār|temettü|MOD|-kār|
zam|n|ar|ḏamm|ekleme|OSM||
enflasyon|n|fr|inflation|şişme|MOD||la:inflatio>fr:inflation>tr:enflasyon
pahalılık|n|fa|bahā|fiyat yüksekliği|OSM||
ucuzluk|n|tr|uçuz|indirim|OSM||
kalite|n|fr|qualité|nitelik|CUM||la:qualitas>fr:qualité>tr:kalite
marka|n|it|marca|işaret|OSM19||ger:marka>it:marca>tr:marka
model|n|fr|modèle|örnek|CUM||it:modello>fr:modèle>tr:model
reklam|n|fr|réclame|çağrı|CUM||la:reclamare>fr:réclame>tr:reklam
vitrin camı|n|fr|vitrine|vitrin|CUM||
mağaza vitrini|n|ar|maḫāzin|vitrin|CUM||
dükkân sahibi|n|ar|dukkān|esnaf|OSM||
semt pazarı|n|ar|samt|pazar|OSM||
semt|n|ar|samt|yön, taraf|EAT||
sokak lambası|n|ar|zuqāq|lamba|CUM||
otobüs durağı|n|fr|autobus|durak|MOD|*dur-|
dolmuş|n|tr|dolmuş|paylaşımlı taksi|CUM|*dol-|
taksi|n|fr|taxi|ücret ölçer (taximètre kısaltması)|CUM|tangere|la:taxāre>fr:taxe>fr:taximètre>fr:taxi>tr:taksi
minibüs|n|fr|minibus|küçük otobüs|MOD||la:minimus+omnibus>fr:minibus>tr:minibüs
metro|n|fr|métro|ana kent demiryolu|MOD|polis|grc:mētrópolis>fr:métropolitain>fr:métro>tr:metro
tramvay hattı|n|en|tramway|hat|CUM||
feribot|n|en|ferry-boat|geçit teknesi|CUM||en:ferry-boat>tr:feribot
vapur iskelesi|n|fr|vapeur|iskele|OSM19||
bilet gişesi|n|fr|billet|gişe|CUM||
gişe|n|fr|guichet|küçük kapı|OSM19||fr:guichet>tr:gişe
peron saati|n|fr|perron|peron|CUM||
ray|n|en|rail|çubuk|OSM19||la:regula>fr:reille>en:rail>tr:ray
lokomotif|n|fr|locomotive|yerden hareket eden|OSM19||la:locus+motivus>fr:locomotive>tr:lokomotif
kondüktör düdüğü|n|fr|conducteur|düdük|CUM|ducere|
düdük|n|tr|tüdük|üfleme çalgısı|DLT||
direksiyon|n|fr|direction|yön verme|CUM||la:directio>fr:direction>tr:direksiyon
fren|n|fr|frein|gem|CUM||la:frenum>fr:frein>tr:fren
debriyaj|n|fr|débrayage|ayırma|CUM||fr:débrayage>tr:debriyaj
vites|n|fr|vitesse|hız|CUM||la:vivacitas>fr:vitesse>tr:vites
lastik|n|fr|élastique|esnek|CUM||grc:elastikós>fr:élastique>tr:lastik
tekerlek jantı|n|tr|tegirmek|jant|CUM||
jant|n|fr|jante|tekerlek çemberi|CUM||fr:jante>tr:jant
far|n|fr|phare|fener|CUM||grc:Pháros>fr:phare>tr:far
kaporta|n|it|coperta|örtü|CUM|caput|la:cooperta>it:coperta>tr:kaporta
bagaj|n|fr|bagage|yük|CUM||fr:bagage>tr:bagaj
plaka|n|it|placca|levha|CUM||fr:plaque>it:placca>tr:plaka
benzin|n|fr|benzine|benzin|CUM||ar:lubān cāwī>la:benzoe>fr:benzine>tr:benzin
mazot deposu|n|sl|mazut|depo|CUM||
kavşak|n|tr|kavşak|yol birleşimi|DD||
kavuşmak|v|tr|kavış-|buluşmak|DLT||
köprü ayağı|n|tr|köprüg|ayak|OSM||
viyadük|n|fr|viaduc|yol köprüsü|MOD||la:via+ducere>fr:viaduc>tr:viyadük
tünel|n|fr|tunnel|geçit|OSM19||fro:tonel>en:tunnel>fr:tunnel>tr:tünel
otoyol|n|tr|oto-yol|hızlı yol|MOD||
şerit|n|ar|şarīṭ|bant|OSM||
trafik ışığı|n|fr|trafic|ışık|MOD||
yaya|n|tr|yadag|yürüyen|DLT||
yaya geçidi|n|tr|yadag|geçit|MOD|*geç-|
kaldırım taşı|n|tr|kaldırım|taş|OSM||
sürücü belgesi|n|tr|sürücü|ehliyet|MOD|*sür-|
ehliyet|n|ar|ahliyya|yeterlik|OSM19||
yolculuk çantası|n|tr|yolçılık|çanta|OSM||
pilot|n|fr|pilote|dümenci|CUM||it:pilota>fr:pilote>tr:pilot
kaptan köşkü|n|it|capitano|köşk|OSM|caput|
tayfa|n|ar|ṭāʾifa|topluluk|EAT|T-W-F|
gemici|n|tr|kemi|denizci|DLT||
denizci|n|tr|teŋiz|denizci|OSM||
balıkçı|n|tr|balık|balık tutan|DLT||
çiftçi kadın|n|fa|cuft|çiftçi|OSM||
bağcı|n|tr|bag|bağ yetiştiren|OSM|*bağ-|
arıcı|n|tr|arı|arı yetiştiren|OSM||
değirmenci|n|tr|tegirmen|değirmen işleten|DLT||
fırıncı|n|el|foúrnos|ekmekçi|OSM||
aşçı|n|tr|aşçı|yemek pişiren|DLT|*aş|
garson kız|n|fr|garçon|garson|CUM||
hamalbaşı|n|ar|ḥammāl|hamal başı|OSM|H-M-L|
bekçi kulübesi|n|tr|bekçi|kulübe|OSM||
kulübe|n|fa|kulbe|küçük ev|EAT||
postacı|n|it|posta|posta dağıtan|OSM19||
itfaiye|n|ar|iṭfāʾiyya|söndürme|OSM19||
itfaiyeci|n|ar|iṭfāʾiyya|yangın söndüren|CUM||
polis memuru|n|fr|police|polis|OSM19|polis|
jandarma|n|fr|gendarme|silahlı adam|OSM19||fr:gens d'armes>fr:gendarme>tr:jandarma
zabıta|n|ar|ḏābiṭa|düzen tutan|OSM||
muhtar|n|ar|muḫtār|seçilmiş|OSM|H-Y-R|
muhtarlık|n|ar|muḫtār|muhtar dairesi|OSM19||
kâhya|n|fa|kad-ḫudā|ev sahibi|EAT||
kapıcı|n|tr|kapıg|kapı bekleyen|OSM|*kap-|
hizmetçi|n|ar|ḫidma|hizmet eden|OSM|H-D-M|
dadı|n|fa|dāda|süt anne|EAT||
sütanne|n|tr|süt ana|süt veren anne|OSM||
ebe|n|tr|ebe|doğum yaptıran|DLT||
hemşire|n|fa|hem-şīre|süt kardeş|EAT||
hastabakıcı|n|fa|ḫaste|hasta bakan|CUM||
cerrah|n|ar|carrāḥ|yara iyileştiren|EAT||
diş hekimi|n|tr|tış|dişçi|CUM|H-K-M|
dişçi|n|tr|tış|diş hekimi|OSM||
veteriner|n|fr|vétérinaire|yük hayvanı bakıcısı|CUM||la:veterinarius>fr:vétérinaire>tr:veteriner
eczacı kalfası|n|ar|aczāʾ|kalfa|OSM||
öğretmen odası|n|tr|öğretmen|oda|CUM|*ög-|
müdür yardımcısı|n|ar|mudīr|yardımcı|CUM|D-W-R|
hademe|n|ar|ḫadama|hizmetçiler|OSM||
bahçıvan makası|n|fa|bāġçevān|makas|OSM||
çöpçü|n|fa|çōb|çöp toplayan|CUM||
tamirci|n|ar|taʿmīr|onaran|CUM||
tamir|n|ar|taʿmīr|onarım|OSM|A-M-R|
onarım|n|tr|onarım|tamir|DD||
onarmak|v|tr|oŋar-|düzeltmek|DLT||
boyacı|n|tr|boduğ|boya yapan|OSM||
badana|n|ar|baṭāna|iç sıva|OSM||
sıva|n|tr|sıva|duvar kaplaması|OSM||
sıvamak|v|tr|sıba-|sıvamak|DLT||
duvarcı|n|fa|dīvār|duvar ören|OSM||
kalfa ustası|n|ar|ḫalīfa|usta|OSM||
çırak çocuğu|n|fa|çirāġ|çırak|OSM||
kunduracı|n|el|kothórnoi|ayakkabıcı|OSM||
saatçi|n|ar|sāʿa|saat onaran|OSM||
kuyumcu çarşısı|n|tr|kuyumçı|çarşı|OSM||
sarraf tezgâhı|n|ar|ṣarrāf|tezgâh|OSM||
bakkal dükkânı|n|ar|baqqāl|dükkân|OSM||
manav tezgâhı|n|tr|manav|tezgâh|OSM||
kasap bıçağı|n|ar|qaṣṣāb|bıçak|OSM||
pazarcı|n|fa|bāzār|pazarda satan|OSM||
seyyar|adj|ar|sayyār|gezici|OSM|S-Y-R|
işportacı|n|it|sporta|sepetle satan|OSM19||la:sporta>it:sporta>tr:işporta
işporta|n|it|sporta|sepet|OSM19||la:sporta>it:sporta>tr:işporta
sabahçı|n|ar|ṣabāḥ|sabah çalışan|CUM||
akşamcı|n|tr|akşam|akşam içen|OSM||
gece bekçisi|n|tr|kéçe|bekçi|OSM||
öğlen|adv|tr|öyle|öğle vakti|OSM||
ikindi|n|tr|ikindi|öğle sonrası|DLT||
şafak|n|ar|şafaq|tan kızıllığı|EAT||
tan|n|tr|taŋ|şafak|ORH||
alacakaranlık|n|tr|ala karaŋgu|alaca karanlık|OSM||
karanlık|n|tr|karaŋgu|karanlık|ORH||
aydınlık|n|tr|aydıŋ|ışıklı|DLT||
ay ışığı|n|tr|ay|ay ışığı|OSM|*ışı-|
mevsim|n|ar|mawsim|dönem|EAT|W-S-M|
ilkbahar|n|tr|ilk bahār|ilk bahar|OSM||
sonbahar|n|tr|soŋ bahār|son bahar|OSM||
yazlık|n|tr|yaz|yaz evi|OSM||
kışlık|n|tr|kış|kış için|DLT||
gün batımı|n|tr|kün|gün batımı|OSM|*bat-|
gün doğumu|n|tr|kün|gün doğumu|OSM|*doğ-|
haftalık|adj|fa|hafte|haftada bir|OSM||
aylık|n|tr|ay|aylık ücret|OSM||
yıllık|n|tr|yıl|yılda bir|DLT||
yüzyıl|n|tr|yüz yıl|asır|DD||
çağdaş|adj|mn|čaγ|aynı çağdan|DD||
dakik|adj|ar|daqīq|ince; tam vaktinde|OSM||
geç|adv|tr|kéç|geç|ORH|*geç-|
erkenci|adj|tr|érken|erken kalkan|OSM||
bedenen|adv|ar|badan|bedence|OSM||
beden|n|ar|badan|vücut|EAT||
omuz|n|tr|omuz|omuz|DLT||
sırt|n|tr|sırt|arka|DLT||
göğüs|n|tr|kögüz|göğüs|ORH||
kaburga kemiği|n|mn|qabirγa|kaburga|OSM||
kemik|n|tr|kemük|kemik|DLT||
kas|n|tr|kas|adale|DD||
adale|n|ar|ʿaḏala|kas|OSM||
damar|n|tr|tamır|damar|DLT||
kan|n|tr|kan|kan|ORH||
ter|n|tr|ter|ter|DLT||
nabız|n|ar|nabḏ|atış|EAT|N-B-D|
soluk|n|tr|soluk|nefes|DLT||
öksürük|n|tr|öksürük|öksürük|DLT||
öksürmek|v|tr|öksür-|öksürmek|DLT||
hapşırmak|v|tr|hapşır-|aksırmak|OSM||
ateşli|adj|fa|ātaş|yüksek sıcaklıklı|OSM||
üşütmek|v|tr|üşüt-|soğuk almak|OSM||
üşümek|v|tr|üşi-|soğuk duymak|DLT||
nezle|n|ar|nazla|akıntı|OSM||
grip|n|fr|grippe|yakalama|CUM||fr:grippe>tr:grip
aşı|n|tr|aşı|aşı|DLT||
iğne yapmak|v|tr|yigne|enjeksiyon|CUM||
şurup|n|ar|şarāb|içecek|OSM||
hap|n|ar|ḥabb|tane|OSM||
merhem|n|ar|marham|yara ilacı|EAT||
yara|n|tr|yara|yara|DLT||
yaralı|adj|tr|yaralıg|yaralanmış|DLT||
sargı|n|tr|sargı|yara bezi|OSM|*sar-|
sarmak|v|tr|sar-|dolamak|DLT|*sar-|
pansuman|n|fr|pansement|yara bakımı|CUM||fr:pansement>tr:pansuman
reçete|n|it|ricetta|alınmış|OSM19||la:recepta>it:ricetta>tr:reçete
muayene|n|ar|muʿāyana|gözle inceleme|OSM|A-Y-N|
tedavi|n|ar|tadāwī|ilaçla iyileştirme|OSM|D-W-Y|
şifalı|adj|ar|şifāʾ|iyileştirici|OSM||
sağlıklı|adj|tr|saglık|sıhhatli|OSM||
diyet|n|fr|diète|yaşam biçimi|CUM||grc:díaita>fr:diète>tr:diyet
perhiz|n|fa|parhīz|sakınma|EAT||
kilo|n|fr|kilo|bin|OSM19||grc:khílioi>fr:kilogramme>fr:kilo>tr:kilo
şişman|adj|tr|şişmek|şişmiş|OSM||
zayıf|adj|ar|ḏaʿīf|güçsüz|EAT||
ince yapılı|adj|tr|yinçge|narin|OSM||
narin|adj|fa|nāzanīn|nazlı|OSM||
yakışıklı|adj|tr|yakışıklı|göze hoş gelen|OSM||
sevimli bebek|n|tr|sebimlig|bebek|OSM|*sev-|
bebek|n|tr|bebek|küçük çocuk|DLT||
çocukluk|n|tr|çocuk|çocuk olma dönemi|OSM||
gençlik|n|tr|kenç|genç olma|DLT||
yaşlılık|n|tr|yaşlıg|ihtiyarlık|OSM|*yaş-|
ihtiyar|adj|ar|iḫtiyār|seçilmiş; yaşlı|EAT||
kocakarı|n|tr|koca karı|yaşlı kadın|OSM||
koca|n|tr|koca|büyük; eş|DLT||
karı|n|tr|karı|yaşlı; eş|DLT||
eş|n|tr|éş|arkadaş, eş|ORH||
nişanlı|adj|fa|nişān|nişanlanmış|OSM||
düğün|n|tr|tügün|düğün|DLT|*tüg-|
gelinlik|n|tr|kelin|gelin giysisi|OSM|*gel-|
güvey|n|tr|küdegü|damat|DLT||
kayınvalide|n|tr|kadın|kaynana|OSM||
kaynana|n|tr|kadın ana|kayınvalide|OSM||
kaynata|n|tr|kadın ata|kayınbaba|OSM||
baldız|n|tr|baldız|eşin kız kardeşi|DLT||
görümce|n|tr|görümce|kocanın kız kardeşi|OSM|*kör-|
elti|n|tr|elti|kocaların eşleri|DLT||
yenge|n|tr|yeŋge|ağabeyin eşi|DLT||
bacanak|n|tr|bacanak|eşlerin kocaları|OSM||
üvey|adj|tr|ögey|öz olmayan|DLT||
yeğen|n|tr|yegen|kardeş çocuğu|DLT||
ikiz|n|tr|ékiz|ikiz|DLT||
öksüz|adj|tr|ögsüz|annesiz|DLT||
yetim|adj|ar|yatīm|babasız|EAT||
komşuluk|n|tr|konşı|komşu ilişkisi|OSM|*kon-|
misafirlik|n|ar|musāfir|konuk olma|OSM|S-F-R|
ziyaret|n|ar|ziyāra|görmeye gitme|EAT||
ikram|n|ar|ikrām|ağırlama|EAT||
kahvaltılık|n|ar|qahwa|kahvaltı yiyeceği|MOD||
sofra bezi örtüsü|n|ar|sufra|örtü|OSM||
peçete|n|it|pezzetta|küçük bez|OSM19||it:pezzetta>tr:peçete
sürahi suyu|n|ar|ṣurāḥī|su|OSM||
ikramiye|n|ar|ikrām|ödül parası|OSM19||
hediyelik|n|ar|hadiyya|hediye olarak|OSM|H-D-Y|
armağan paketi|n|tr|armagan|paket|MOD||
paket|n|fr|paquet|bohça|OSM19||fr:paquet>tr:paket
bohça|n|tr|bogça|sarılı giysi|DLT||
"""
