# -*- coding: utf-8 -*-
"""Batı dillerinden (Fransızca, İtalyanca, Yunanca, İngilizce, Latince, Almanca...) alıntılar.
Biçim: lemma|pos|origin|kaynak biçim|kaynak anlam|dönem|kök ailesi|zincir"""

LEXICON_EU = r"""
spektrum|n|fr|spectre|görünen şey|CUM|specere|la:spectrum>fr:spectre>tr:spektrum
perspektif|n|fr|perspective|içinden bakma|CUM|specere|la:perspicere>fr:perspective>tr:perspektif
prospektüs|n|fr|prospectus|ileriye bakış|CUM|specere|la:prospectus>fr:prospectus>tr:prospektüs
spekülasyon|n|fr|spéculation|gözlemleme|CUM|specere|la:speculatio>fr:spéculation>tr:spekülasyon
spesifik|adj|fr|spécifique|türe özgü|MOD|specere|la:species>fr:spécifique>tr:spesifik
spesiyal|adj|fr|spécial|özel|CUM|specere|la:specialis>fr:spécial>tr:spesiyal
spektakül|n|fr|spectacle|gösteri|MOD|specere|la:spectaculum>fr:spectacle>tr:spektakül
teleskop|n|fr|télescope|uzağı gören|OSM19|tēle|grc:tēle+skopeîn>it:telescopio>fr:télescope>tr:teleskop
traktör|n|fr|tracteur|çeken|CUM|trahere|la:tractor>fr:tracteur>tr:traktör
kontrat|n|fr|contrat|birlikte çekilen|OSM19|trahere|la:contractus>fr:contrat>tr:kontrat
portre|n|fr|portrait|çekip çıkarılan|OSM19|trahere|la:protrahere>fr:portrait>tr:portre
tren|n|fr|train|çekilen dizi|OSM19|trahere|la:trahere>fr:train>tr:tren
antrenman|n|fr|entraînement|çekip götürme|CUM|trahere|la:trahere>fr:entraînement>tr:antrenman
antrenör|n|fr|entraîneur|çalıştırıcı|CUM|trahere|la:trahere>fr:entraîneur>tr:antrenör
ekstre|n|fr|extrait|dışarı çekilen|CUM|trahere|la:extractum>fr:extrait>tr:ekstre
abstre|adj|fr|abstrait|çekip ayrılmış|CUM|trahere|la:abstractus>fr:abstrait>tr:abstre
soyut|adj|tr|soy-ut|soyulmuş|DD||
fotoğraf|n|fr|photographie|ışıkla yazma|OSM19|graphein|grc:phôs+gráphein>fr:photographie>tr:fotoğraf
telgraf|n|fr|télégraphe|uzağa yazma|OSM19|graphein|grc:tēle+gráphein>fr:télégraphe>tr:telgraf
paragraf|n|fr|paragraphe|yanına yazılan|OSM19|graphein|grc:parágraphos>fr:paragraphe>tr:paragraf
grafik|n|fr|graphique|çizimle ilgili|CUM|graphein|grc:graphikós>fr:graphique>tr:grafik
program|n|fr|programme|önceden yazılan|OSM19|graphein|grc:prógramma>fr:programme>tr:program
gramer|n|fr|grammaire|harf bilgisi|OSM19|graphein|grc:grammatikḕ>fr:grammaire>tr:gramer
biyografi|n|fr|biographie|yaşam yazısı|CUM|graphein|grc:bíos+gráphein>fr:biographie>tr:biyografi
otobiyografi|n|fr|autobiographie|kendi yaşam yazısı|CUM|graphein|grc:autós+bíos+gráphein>fr:autobiographie>tr:otobiyografi
analog|adj|fr|analogue|orantılı|MOD|logos|grc:análogos>fr:analogue>tr:analog
diyalog|n|fr|dialogue|karşılıklı söz|CUM|logos|grc:diálogos>fr:dialogue>tr:diyalog
monolog|n|fr|monologue|tek kişilik söz|CUM|logos|grc:monólogos>fr:monologue>tr:monolog
katalog|n|fr|catalogue|liste|CUM|logos|grc:katálogos>fr:catalogue>tr:katalog
biyoloji|n|fr|biologie|yaşam bilimi|OSM19|logos|grc:bíos+lógos>fr:biologie>tr:biyoloji
psikoloji|n|fr|psychologie|ruh bilimi|OSM19|logos|grc:psykhḕ+lógos>fr:psychologie>tr:psikoloji
teknoloji|n|fr|technologie|zanaat bilgisi|CUM|logos|grc:tékhnē+lógos>fr:technologie>tr:teknoloji
ekoloji|n|fr|écologie|ev bilimi|MOD|logos|grc:oîkos+lógos>fr:écologie>tr:ekoloji
sosyoloji|n|fr|sociologie|toplum bilimi|OSM19|logos|la:socius+grc:lógos>fr:sociologie>tr:sosyoloji
jeoloji|n|fr|géologie|yer bilimi|OSM19|logos|grc:gê+lógos>fr:géologie>tr:jeoloji
arkeoloji|n|fr|archéologie|eski şeyler bilimi|OSM19|logos|grc:arkhaîos+lógos>fr:archéologie>tr:arkeoloji
etimoloji|n|fr|étymologie|gerçek anlam bilgisi|OSM19|logos|grc:étymon+lógos>fr:étymologie>tr:etimoloji
teknik|n|fr|technique|zanaata ait|OSM19|tekhne|grc:tekhnikós>fr:technique>tr:teknik
teknisyen|n|fr|technicien|teknik uzman|CUM|tekhne|grc:tékhnē>fr:technicien>tr:teknisyen
teknokrat|n|fr|technocrate|teknik yönetici|MOD|tekhne|grc:tékhnē+krátos>fr:technocrate>tr:teknokrat
politika|n|it|politica|şehir işleri|OSM19|polis|grc:politikḕ>it:politica>tr:politika
polis|n|fr|police|şehir düzeni|OSM19|polis|grc:politeía>fr:police>tr:polis
metropol|n|fr|métropole|ana şehir|CUM|polis|grc:mētrópolis>fr:métropole>tr:metropol
polisiye|adj|fr|policier|polisle ilgili|CUM|polis|fr:policier>tr:polisiye
kozmopolit|adj|fr|cosmopolite|dünya vatandaşı|CUM|polis|grc:kosmopolítēs>fr:cosmopolite>tr:kozmopolit
kaptan|n|it|capitano|baş olan|EAT|caput|la:caput>it:capitano>tr:kaptan
kapital|n|fr|capital|baş para|OSM19|caput|la:capitalis>fr:capital>tr:kapital
kapitalizm|n|fr|capitalisme|sermayecilik|CUM|caput|la:caput>fr:capitalisme>tr:kapitalizm
kapitülasyon|n|fr|capitulation|başlıklara ayırma|OSM19|caput|la:capitulum>fr:capitulation>tr:kapitülasyon
kep|n|en|cap|başlık|CUM|caput|la:cappa>en:cap>tr:kep
şapka|n|sl|šapka|başlık|OSM19|caput|la:cappa>fr:chape>ru:šapka>tr:şapka
kapüşon|n|fr|capuchon|başlık|CUM|caput|la:cappa>fr:capuchon>tr:kapüşon
kaput|n|fr|capot|kaporta|CUM|caput|la:caput>fr:capot>tr:kaput
misyon|n|fr|mission|gönderme|CUM|mittere|la:missio>fr:mission>tr:misyon
misyoner|n|fr|missionnaire|gönderilen|OSM19|mittere|la:missio>fr:missionnaire>tr:misyoner
komisyon|n|fr|commission|görevlendirme|OSM19|mittere|la:commissio>fr:commission>tr:komisyon
komite|n|fr|comité|görevli kurul|OSM19|mittere|la:committere>en:committee>fr:comité>tr:komite
mesaj|n|fr|message|gönderilen söz|CUM|mittere|la:missaticum>fr:message>tr:mesaj
emisyon|n|fr|émission|dışa gönderme|CUM|mittere|la:emissio>fr:émission>tr:emisyon
transmisyon|n|fr|transmission|aktarma|CUM|mittere|la:transmissio>fr:transmission>tr:transmisyon
pozisyon|n|fr|position|konum|CUM|ponere|la:positio>fr:position>tr:pozisyon
pozitif|adj|fr|positif|konulmuş, olumlu|OSM19|ponere|la:positivus>fr:positif>tr:pozitif
kompozisyon|n|fr|composition|birlikte koyma|OSM19|ponere|la:compositio>fr:composition>tr:kompozisyon
depo|n|fr|dépôt|bırakılan|OSM19|ponere|la:depositum>fr:dépôt>tr:depo
depozito|n|it|deposito|bırakılan para|CUM|ponere|la:depositum>it:deposito>tr:depozito
opozisyon|n|fr|opposition|karşı koyma|CUM|ponere|la:oppositio>fr:opposition>tr:opozisyon
fabrika|n|it|fabbrica|yapım yeri|OSM19|facere|la:fabrica>it:fabbrica>tr:fabrika
fakülte|n|fr|faculté|yapabilme gücü|OSM19|facere|la:facultas>fr:faculté>tr:fakülte
efekt|n|en|effect|etki|CUM||
fason|n|fr|façon|yapış biçimi|CUM|facere|la:factio>fr:façon>tr:fason
ofis|n|fr|office|iş yapma|MOD|facere|la:officium>fr:office>tr:ofis
manifatura|n|it|manifattura|elle yapılmış|OSM19|facere|la:manu factura>it:manifattura>tr:manifatura
video|n|en|video|görüyorum|MOD|videre|la:videre>en:video>tr:video
vizyon|n|fr|vision|görme|CUM|videre|la:visio>fr:vision>tr:vizyon
televizyon|n|fr|télévision|uzağı görme|CUM|videre|grc:tēle+la:visio>fr:télévision>tr:televizyon
vize|n|fr|visa|görülmüş|CUM|videre|la:visa>fr:visa>tr:vize
revizyon|n|fr|révision|yeniden görme|CUM|videre|la:revisio>fr:révision>tr:revizyon
vitrin|n|fr|vitrine|camlı dolap|CUM||la:vitrum>fr:vitrine>tr:vitrin
kurs|n|fr|cours|akış, koşu|CUM|currere|la:cursus>fr:cours>tr:kurs
koridor|n|fr|corridor|koşulan yer|OSM19|currere|la:currere>it:corridore>fr:corridor>tr:koridor
kurye|n|fr|courrier|koşucu|CUM|currere|la:currere>fr:courrier>tr:kurye
konkur|n|fr|concours|birlikte koşma|CUM|currere|la:concursus>fr:concours>tr:konkur
kariyer|n|fr|carrière|araba yolu|MOD||la:carrus>fr:carrière>tr:kariyer
prodüktör|n|fr|producteur|öne götüren|CUM|ducere|la:producere>fr:producteur>tr:prodüktör
prodüksiyon|n|fr|production|üretim|CUM|ducere|la:productio>fr:production>tr:prodüksiyon
kondüktör|n|fr|conducteur|götüren|OSM19|ducere|la:conductor>fr:conducteur>tr:kondüktör
redüksiyon|n|fr|réduction|geri götürme|CUM|ducere|la:reductio>fr:réduction>tr:redüksiyon
dük|n|fr|duc|önder|OSM19|ducere|la:dux>fr:duc>tr:dük
düşes|n|fr|duchesse|dük eşi|OSM19|ducere|la:dux>fr:duchesse>tr:düşes
rapor|n|fr|rapport|geri taşıma|OSM19|portare|la:reportare>fr:rapport>tr:rapor
pasaport|n|fr|passeport|liman geçişi|OSM19|portare|la:portus>fr:passeport>tr:pasaport
portatif|adj|fr|portatif|taşınabilir|CUM|portare|la:portare>fr:portatif>tr:portatif
transport|n|fr|transport|öteye taşıma|CUM|portare|la:transportare>fr:transport>tr:transport
raportör|n|fr|rapporteur|rapor veren|CUM|portare|la:reportare>fr:rapporteur>tr:raportör
istasyon|n|fr|station|durma yeri|OSM19|stare|la:statio>fr:station>tr:istasyon
statü|n|fr|statut|durum|CUM|stare|la:status>fr:statut>tr:statü
istatistik|n|fr|statistique|devlet bilgisi|OSM19|stare|la:status>de:Statistik>fr:statistique>tr:istatistik
enstitü|n|fr|institut|kurulan|CUM|stare|la:institutum>fr:institut>tr:enstitü
sistem|n|fr|système|birlikte duran|CUM|stare|grc:sýstēma>fr:système>tr:sistem
asistan|n|fr|assistant|yanında duran|CUM|stare|la:assistere>fr:assistant>tr:asistan
stabil|adj|fr|stable|sabit|MOD|stare|la:stabilis>fr:stable>tr:stabil
stant|n|en|stand|durulan yer|MOD|stare|en:stand>tr:stant
telefon|n|fr|téléphone|uzak ses|OSM19|phone|grc:tēle+phōnḕ>fr:téléphone>tr:telefon
mikrofon|n|fr|microphone|küçük ses|CUM|phone|grc:mikrós+phōnḕ>fr:microphone>tr:mikrofon
fonetik|n|fr|phonétique|ses bilgisi|CUM|phone|grc:phōnētikós>fr:phonétique>tr:fonetik
senfoni|n|fr|symphonie|birlikte ses|OSM19|phone|grc:symphōnía>fr:symphonie>tr:senfoni
megafon|n|fr|mégaphone|büyük ses|CUM|phone|grc:mégas+phōnḕ>en:megaphone>fr:mégaphone>tr:megafon
gramofon|n|fr|gramophone|yazı sesi|CUM|phone|grc:grámma+phōnḕ>en:gramophone>fr:gramophone>tr:gramofon
bisiklet|n|fr|bicyclette|iki tekerlek|OSM19|kyklos|la:bi+grc:kýklos>fr:bicyclette>tr:bisiklet
siklon|n|fr|cyclone|dönen|CUM|kyklos|grc:kýklos>en:cyclone>fr:cyclone>tr:siklon
ansiklopedi|n|fr|encyclopédie|çember eğitim|OSM19|kyklos|grc:enkýklios paideía>fr:encyclopédie>tr:ansiklopedi
sirk|n|fr|cirque|çember alan|OSM19|kyklos|grc:kírkos>la:circus>fr:cirque>tr:sirk
sirkülasyon|n|fr|circulation|dolaşım|CUM|kyklos|la:circulatio>fr:circulation>tr:sirkülasyon
demokrasi|n|fr|démocratie|halk yönetimi|OSM19|kratos|grc:dēmokratía>fr:démocratie>tr:demokrasi
bürokrasi|n|fr|bureaucratie|masa yönetimi|CUM|kratos|fr:bureau+grc:krátos>fr:bureaucratie>tr:bürokrasi
aristokrasi|n|fr|aristocratie|en iyilerin yönetimi|OSM19|kratos|grc:aristokratía>fr:aristocratie>tr:aristokrasi
otokrasi|n|fr|autocratie|tek kişi yönetimi|CUM|kratos|grc:autokráteia>fr:autocratie>tr:otokrasi
demografi|n|fr|démographie|halk yazımı|MOD|demos|grc:dêmos+gráphein>fr:démographie>tr:demografi
epidemi|n|fr|épidémie|halk üstüne|CUM|demos|grc:epidēmía>fr:épidémie>tr:epidemi
pandemi|n|fr|pandémie|tüm halk|NEW|demos|grc:pándēmos>fr:pandémie>tr:pandemi
fantezi|n|fr|fantaisie|hayal gücü|CUM|phainein|grc:phantasía>fr:fantaisie>tr:fantezi
fenomen|n|fr|phénomène|görünen şey|CUM|phainein|grc:phainómenon>fr:phénomène>tr:fenomen
fantastik|adj|fr|fantastique|hayalî|CUM|phainein|grc:phantastikós>fr:fantastique>tr:fantastik
fantom|n|fr|fantôme|hayalet|CUM|phainein|grc:phántasma>fr:fantôme>tr:fantom
panayır|n|el|panḕgyris|tüm toplantı|EAT|pan|grc:panḕgyris>el:panigýri>tr:panayır
panorama|n|fr|panorama|tüm görünüm|CUM|pan|grc:pân+hórama>en:panorama>fr:panorama>tr:panorama
panteon|n|fr|panthéon|tüm tanrılar|CUM|pan|grc:pántheion>fr:panthéon>tr:panteon
pankreas|n|fr|pancréas|tüm et|CUM|pan|grc:pánkreas>fr:pancréas>tr:pankreas
metre|n|fr|mètre|ölçü|OSM19|metron|grc:métron>fr:mètre>tr:metre
termometre|n|fr|thermomètre|ısı ölçer|OSM19|metron|grc:thermós+métron>fr:thermomètre>tr:termometre
kilometre|n|fr|kilomètre|bin metre|OSM19|metron|grc:khílioi+métron>fr:kilomètre>tr:kilometre
geometri|n|fr|géométrie|yer ölçümü|OSM19|metron|grc:geōmetría>fr:géométrie>tr:geometri
simetri|n|fr|symétrie|birlikte ölçü|CUM|metron|grc:symmetría>fr:symétrie>tr:simetri
parametre|n|fr|paramètre|yan ölçü|MOD|metron|grc:pará+métron>fr:paramètre>tr:parametre
barometre|n|fr|baromètre|ağırlık ölçer|OSM19|metron|grc:báros+métron>fr:baromètre>tr:barometre
santimetre|n|fr|centimètre|yüzde bir metre|OSM19|metron|la:centum+grc:métron>fr:centimètre>tr:santimetre
metot|n|fr|méthode|yol izleme|OSM19|hodos|grc:méthodos>fr:méthode>tr:metot
periyot|n|fr|période|çevrim yolu|CUM|hodos|grc:períodos>fr:période>tr:periyot
katot|n|fr|cathode|aşağı yol|CUM|hodos|grc:káthodos>en:cathode>fr:cathode>tr:katot
anot|n|fr|anode|yukarı yol|CUM|hodos|grc:ánodos>en:anode>fr:anode>tr:anot
elektrot|n|fr|électrode|elektrik yolu|CUM|hodos|grc:ḕlektron+hodós>en:electrode>fr:électrode>tr:elektrot
otomobil|n|fr|automobile|kendi hareket eden|OSM19|movere|grc:autós+la:mobilis>fr:automobile>tr:otomobil
garaj|n|fr|garage|koruma yeri|CUM||fr:garage>tr:garaj
şoför|n|fr|chauffeur|ısıtıcı|CUM||fr:chauffeur>tr:şoför
kamyon|n|fr|camion|yük arabası|CUM||fr:camion>tr:kamyon
otobüs|n|fr|autobus|herkes için araç|CUM||la:omnibus>fr:autobus>tr:otobüs
gar|n|fr|gare|bekleme yeri|OSM19||fr:gare>tr:gar
bilet|n|fr|billet|kısa yazı|OSM19||la:bulla>fr:billet>tr:bilet
peron|n|fr|perron|taş basamak|CUM||la:petra>fr:perron>tr:peron
vagon|n|fr|wagon|araba|OSM19||en:wagon>fr:wagon>tr:vagon
bulvar|n|fr|boulevard|sur yolu|OSM19||nl:bolwerk>fr:boulevard>tr:bulvar
apartman|n|fr|appartement|ayrı bölüm|OSM19||it:appartamento>fr:appartement>tr:apartman
asansör|n|fr|ascenseur|yükselten|CUM||la:ascendere>fr:ascenseur>tr:asansör
balkon|n|fr|balcon|çıkma|OSM19||
salon|n|fr|salon|büyük oda|OSM19||it:salone>fr:salon>tr:salon
tuvalet|n|fr|toilette|küçük bez|OSM19||fr:toilette>tr:tuvalet
lavabo|n|fr|lavabo|yıkayacağım|CUM||la:lavabo>fr:lavabo>tr:lavabo
duş|n|fr|douche|su borusu|CUM||it:doccia>fr:douche>tr:duş
mobilya|n|it|mobilia|taşınabilir eşya|OSM19|movere|la:mobilis>it:mobilia>tr:mobilya
kanepe|n|fr|canapé|cibinlikli yatak|OSM19||grc:kōnōpeîon>fr:canapé>tr:kanepe
abajur|n|fr|abat-jour|ışık kesen|CUM||fr:abat-jour>tr:abajur
portmanto|n|fr|portemanteau|manto taşıyan|CUM||fr:portemanteau>tr:portmanto
şömine|n|fr|cheminée|baca|CUM||la:caminus>fr:cheminée>tr:şömine
parke|n|fr|parquet|küçük park|CUM||fr:parquet>tr:parke
jaluzi|n|fr|jalousie|kıskançlık; kafes perde|CUM||it:gelosia>fr:jalousie>tr:jaluzi
banyo|n|it|bagno|yıkanma|OSM19||la:balneum>it:bagno>tr:banyo
kuaför|n|fr|coiffeur|saç yapan|CUM||fr:coiffeur>tr:kuaför
makyaj|n|fr|maquillage|süsleme|CUM||fr:maquillage>tr:makyaj
ruj|n|fr|rouge|kırmızı|CUM||la:rubeus>fr:rouge>tr:ruj
parfüm|n|fr|parfum|tütsü|OSM19||la:per fumum>it:profumo>fr:parfum>tr:parfüm
krem|n|fr|crème|kaymak|CUM||la:chrisma>fr:crème>tr:krem
şampuan|n|fr|shampooing|ovmak|CUM||hi:chāmpo>en:shampoo>fr:shampooing>tr:şampuan
pudra|n|fr|poudre|toz|OSM19||la:pulvis>fr:poudre>tr:pudra
manikür|n|fr|manucure|el bakımı|CUM||la:manus+cura>fr:manucure>tr:manikür
losyon|n|fr|lotion|yıkama|CUM||la:lotio>fr:lotion>tr:losyon
jöle|n|fr|gelée|donmuş|CUM||la:gelata>fr:gelée>tr:jöle
kolonya|n|it|acqua di Colonia|Köln suyu|OSM19||la:Colonia>it:colonia>tr:kolonya
jilet|n|fr|Gillette|marka adı|CUM||en:Gillette>fr:Gillette>tr:jilet
pantolon|n|fr|pantalon|Pantalone kıyafeti|OSM19||it:Pantalone>fr:pantalon>tr:pantolon
ceket|n|fr|jaquette|köylü giysisi|OSM19||fr:jaquette>tr:ceket
bere|n|fr|béret|başlık|CUM||la:birrus>oc:berret>fr:béret>tr:bere
kravat|n|fr|cravate|Hırvat|OSM19||hr:Hrvat>fr:cravate>tr:kravat
eşarp|n|fr|écharpe|bağ|CUM||fr:écharpe>tr:eşarp
fular|n|fr|foulard|boyun bağı|CUM||fr:foulard>tr:fular
manto|n|fr|manteau|örtü|OSM19||la:mantellum>fr:manteau>tr:manto
palto|n|fr|paletot|üst giysi|OSM19||en:paltok>fr:paletot>tr:palto
kaban|n|fr|caban|yağmurluk|CUM||ar:qabāʾ>it:gabbano>fr:caban>tr:kaban
kazak|n|fr|casaque|Kazak giysisi|CUM||otk:kazak>fr:casaque>tr:kazak
jarse|n|fr|jersey|Jersey kumaşı|CUM||en:Jersey>fr:jersey>tr:jarse
kaşmir|n|fr|cachemire|Keşmir yünü|CUM||sa:Kaśmīra>fr:cachemire>tr:kaşmir
dantel|n|fr|dentelle|küçük diş|OSM19||la:dens>fr:dentelle>tr:dantel
tül|n|fr|tulle|Tulle kenti|OSM19||fr:Tulle>tr:tül
saten|n|fr|satin|Zaytun kenti|OSM19||ar:zaytūnī>fr:satin>tr:saten
naylon|n|en|nylon|marka adı|MOD||en:nylon>tr:naylon
plastik|n|fr|plastique|biçimlenebilir|CUM||grc:plastikós>fr:plastique>tr:plastik
beton|n|fr|béton|çakıl|CUM||la:bitumen>fr:béton>tr:beton
çimento|n|it|cimento|yapı harcı|OSM19||la:caementum>it:cimento>tr:çimento
tuğla|n|it|tegola|kiremit|EAT|tegere|la:tegula>it:tegola>tr:tuğla
kiremit|n|el|keramídi|kiremit|EAT||grc:kéramos>el:keramídi>tr:kiremit
mermer|n|el|mármaro|parlayan taş|EAT||grc:mármaros>el:mármaro>tr:mermer
granit|n|fr|granit|taneli|CUM||it:granito>fr:granit>tr:granit
asfalt|n|fr|asphalte|zift|CUM||grc:ásphaltos>fr:asphalte>tr:asfalt
kalorifer|n|fr|calorifère|ısı taşıyan|CUM||la:calor+ferre>fr:calorifère>tr:kalorifer
radyatör|n|fr|radiateur|ışın yayan|CUM|radius|la:radius>fr:radiateur>tr:radyatör
elektrik|n|fr|électrique|kehribar gücü|OSM19|ēlektron|grc:ḕlektron>fr:électrique>tr:elektrik
ampul|n|fr|ampoule|küçük şişe|CUM||la:ampulla>fr:ampoule>tr:ampul
priz|n|fr|prise|alma|CUM||fr:prise>tr:priz
fiş|n|fr|fiche|çivi|CUM||fr:fiche>tr:fiş
kablo|n|fr|câble|halat|CUM||la:capulum>fr:câble>tr:kablo
pil|n|fr|pile|yığın|CUM||la:pila>fr:pile>tr:pil
akü|n|fr|accumulateur|biriktirici|CUM||la:accumulare>fr:accumulateur>tr:akü
jeneratör|n|fr|générateur|üreten|CUM||la:generator>fr:générateur>tr:jeneratör
motor|n|fr|moteur|hareket ettiren|OSM19|movere|la:motor>fr:moteur>tr:motor
makine|n|it|macchina|aygıt|OSM19|mekhane|grc:mēkhanḕ>la:machina>it:macchina>tr:makine
atölye|n|fr|atelier|tahta parçası yeri|OSM19||fr:atelier>tr:atölye
büro|n|fr|bureau|yünlü örtü|OSM19||fr:bureau>tr:büro
sekreter|n|fr|secrétaire|sır tutan|OSM19||la:secretarius>fr:secrétaire>tr:sekreter
patron|n|fr|patron|koruyucu|OSM19||la:patronus>fr:patron>tr:patron
şef|n|fr|chef|baş|CUM||la:caput>fr:chef>tr:şef
garson|n|fr|garçon|oğlan|OSM19||fr:garçon>tr:garson
menü|n|fr|menu|küçük, ayrıntılı|CUM||la:minutus>fr:menu>tr:menü
restoran|n|fr|restaurant|güç veren|OSM19||la:restaurare>fr:restaurant>tr:restoran
lokanta|n|it|locanda|han|OSM19||la:locare>it:locanda>tr:lokanta
kafe|n|fr|café|kahve|CUM||ar:qahwa>tr:kahve>it:caffè>fr:café>tr:kafe
fırın|n|el|foúrnos|fırın|EAT||la:furnus>el:foúrnos>tr:fırın
pide|n|el|píta|yassı ekmek|OSM||el:píta>tr:pide
pizza|n|it|pizza|yassı ekmek|MOD||it:pizza>tr:pizza
makarna|n|it|maccheroni|makarna|OSM19||it:maccheroni>tr:makarna
pasta|n|it|pasta|hamur|OSM19|pasta|la:pasta>it:pasta>tr:pasta
salata|n|it|salata|tuzlanmış|OSM|sal|la:sal>it:salata>tr:salata
salatalık|n|it|salata|salata hıyarı|OSM||
domates|n|el|domátes|domates|OSM19||nah:tomatl>es:tomate>it:tomate>el:domátes>tr:domates
patates|n|el|patátes|patates|OSM19||tai:batata>es:patata>it:patata>el:patátes>tr:patates
lahana|n|el|láchano|yeşillik|EAT||grc:lákhanon>el:láchano>tr:lahana
pırasa|n|el|prásso|pırasa|EAT||grc:práson>el:prásso>tr:pırasa
marul|n|el|maroúli|marul|OSM||la:amarus>el:maroúli>tr:marul
biber|n|el|pipéri|biber|EAT||sa:pippalī>grc:péperi>el:pipéri>tr:biber
ananas|n|fr|ananas|ananas|CUM||tup:nanas>pt:ananás>fr:ananas>tr:ananas
sardalya|n|it|sardella|Sardinya balığı|OSM||la:sardina>it:sardella>tr:sardalya
levrek|n|el|lavráki|levrek|OSM||grc:lábrax>el:lavráki>tr:levrek
palamut|n|el|palamída|palamut|OSM||el:palamída>tr:palamut
istavrit|n|el|stavrídi|istavrit|OSM||el:stavrídi>tr:istavrit
uskumru|n|el|skoumbrí|uskumru|OSM||grc:skómbros>el:skoumbrí>tr:uskumru
hamsi|n|el|chapsí|hamsi|OSM||el:chapsí>tr:hamsi
midye|n|el|mýdi|midye|OSM||grc:mýs>el:mýdi>tr:midye
karides|n|el|garída|karides|OSM||grc:karís>el:garída>tr:karides
ahtapot|n|el|oktapódi|sekiz ayak|OSM||grc:oktṑpous>el:oktapódi>tr:ahtapot
kalamar|n|it|calamaro|mürekkep balığı|OSM||la:calamarius>it:calamaro>tr:kalamar
sandviç|n|en|sandwich|Sandwich kontu|CUM||en:sandwich>fr:sandwich>tr:sandviç
kek|n|en|cake|kek|CUM||en:cake>tr:kek
tost|n|en|toast|kızartılmış|MOD||la:tostus>en:toast>tr:tost
sosis|n|fr|saucisse|tuzlanmış|CUM||la:salsicia>fr:saucisse>tr:sosis
salam|n|it|salame|tuzlanmış|CUM|sal|la:sal>it:salame>tr:salam
bisküvi|n|fr|biscuit|iki kez pişmiş|OSM19|coquere|la:bis coctus>fr:biscuit>tr:bisküvi
çikolata|n|it|cioccolata|acı su|OSM19||nah:xocolātl>es:chocolate>it:cioccolata>tr:çikolata
şekerleme|n|fa|şakar|tatlı|OSM||
karamela|n|it|caramella|yanmış şeker|CUM||la:cannamellis>it:caramella>tr:karamela
likör|n|fr|liqueur|sıvı|OSM19||la:liquor>fr:liqueur>tr:likör
bira|n|it|birra|bira|OSM19||la:bibere>it:birra>tr:bira
viski|n|en|whisky|yaşam suyu|CUM||ga:uisce beatha>en:whisky>tr:viski
votka|n|sl|vodka|sucuk|CUM||ru:vodka>tr:votka
kokteyl|n|en|cocktail|horoz kuyruğu|MOD||en:cocktail>tr:kokteyl
futbol|n|en|football|ayak topu|CUM||en:football>tr:futbol
gol|n|en|goal|hedef|CUM||en:goal>tr:gol
tenis|n|en|tennis|tutun|CUM||fr:tenez>en:tennis>tr:tenis
basketbol|n|en|basketball|sepet topu|CUM||en:basketball>tr:basketbol
voleybol|n|en|volleyball|vole topu|CUM||en:volleyball>tr:voleybol
hentbol|n|en|handball|el topu|MOD||en:handball>tr:hentbol
golf|n|en|golf|golf|MOD||nl:kolf>en:golf>tr:golf
boks|n|en|boxing|yumruk|CUM||en:boxing>tr:boks
ofsayt|n|en|offside|dış taraf|CUM||en:offside>tr:ofsayt
penaltı|n|en|penalty|ceza|CUM||la:poenalis>en:penalty>tr:penaltı
korner|n|en|corner|köşe|CUM||la:cornu>en:corner>tr:korner
spor|n|fr|sport|eğlence|OSM19|portare|la:deportare>en:sport>fr:sport>tr:spor
şampiyon|n|fr|champion|alan savaşçısı|CUM||la:campus>fr:champion>tr:şampiyon
lig|n|fr|ligue|bağ|CUM||la:ligare>it:lega>fr:ligue>tr:lig
takım|n|tr|takım|grup|OSM|*tak-|
klip|n|en|clip|kesmek|MOD||en:clip>tr:klip
film|n|fr|film|zar|CUM||
kamera|n|fr|caméra|oda|CUM|camera|grc:kamára>la:camera>fr:caméra>tr:kamera
sinema|n|fr|cinéma|hareket|CUM|kinein|grc:kínēma>fr:cinéma>tr:sinema
tiyatro|n|it|teatro|seyir yeri|OSM19|theā|grc:théatron>it:teatro>tr:tiyatro
opera|n|it|opera|eser|OSM19||la:opera>it:opera>tr:opera
bale|n|fr|ballet|küçük dans|CUM||it:balletto>fr:ballet>tr:bale
konser|n|fr|concert|uyuşma|OSM19||it:concerto>fr:concert>tr:konser
orkestra|n|fr|orchestre|dans yeri|OSM19||grc:orkhḕstra>fr:orchestre>tr:orkestra
piyano|n|it|pianoforte|yumuşak-güçlü|OSM19||it:pianoforte>tr:piyano
gitar|n|fr|guitare|kitara|CUM||grc:kithára>ar:qīṯāra>es:guitarra>fr:guitare>tr:gitar
radyo|n|fr|radio|ışın|CUM|radius|la:radius>fr:radio>tr:radyo
internet|n|en|internet|ağlar arası|NEW||en:internet>tr:internet
web|n|en|web|ağ|NEW||en:web>tr:web
blog|n|en|blog|ağ günlüğü|NEW||en:weblog>tr:blog
çip|n|en|chip|yonga|MOD||en:chip>tr:çip
bit|n|en|bit|ikili rakam|MOD||en:binary digit>tr:bit
bayt|n|en|byte|sekiz bit|MOD||en:byte>tr:bayt
laptop|n|en|laptop|kucak üstü|NEW||en:laptop>tr:laptop
online|adj|en|online|çevrim içi|NEW||en:online>tr:online
hostes|n|en|hostess|ev sahibesi|MOD||la:hospes>fr:hôtesse>en:hostess>tr:hostes
spiker|n|en|speaker|konuşan|CUM||en:speaker>tr:spiker
menajer|n|en|manager|yöneten|MOD||la:manus>it:maneggiare>en:manager>tr:menajer
star|n|en|star|yıldız|MOD||en:star>tr:star
şov|n|en|show|göstermek|MOD||en:show>tr:şov
miting|n|en|meeting|toplantı|CUM||en:meeting>tr:miting
lider|n|en|leader|önder|CUM||en:leader>tr:lider
tişört|n|en|T-shirt|T gömlek|MOD||en:T-shirt>tr:tişört
blucin|n|en|blue jeans|mavi Cenova kumaşı|MOD||it:Genova>fr:Gênes>en:jeans>tr:blucin
stres|n|en|stress|sıkıntı|MOD||la:strictus>en:stress>tr:stres
şok|n|fr|choc|çarpma|CUM||fr:choc>tr:şok
trend|n|en|trend|eğilim|NEW||en:trend>tr:trend
market|n|en|market|pazar|MOD||la:mercatus>en:market>tr:market
süpermarket|n|en|supermarket|büyük pazar|MOD||en:supermarket>tr:süpermarket
bar|n|en|bar|çubuk; tezgâh|CUM||fr:barre>en:bar>tr:bar
ketçap|n|en|ketchup|balık sosu|MOD||zh:kê-tsiap>ml:kicap>en:ketchup>tr:ketçap
jip|n|en|jeep|GP aracı|MOD||en:jeep>tr:jip
tank|n|en|tank|su deposu|CUM||pt:tanque>en:tank>tr:tank
radar|n|en|radar|radyo algılama|MOD||en:radar>tr:radar
lazer|n|en|laser|ışık yükseltme|MOD||en:laser>tr:lazer
roket|n|fr|roquette|küçük iğ|CUM||it:rocchetta>fr:roquette>tr:roket
robot|n|fr|robot|angarya|CUM||cs:robota>cs:robot>fr:robot>tr:robot
kaset|n|fr|cassette|küçük kutu|MOD||it:cassetta>fr:cassette>tr:kaset
disk|n|fr|disque|yuvarlak levha|CUM||grc:dískos>la:discus>fr:disque>tr:disk
piknik|n|fr|pique-nique|kır yemeği|CUM||fr:pique-nique>tr:piknik
kampüs|n|en|campus|alan|MOD||la:campus>en:campus>tr:kampüs
kamp|n|fr|camp|alan|CUM||la:campus>fr:camp>tr:kamp
üniversite|n|fr|université|bütünlük|OSM19|unus|la:universitas>fr:université>tr:üniversite
lise|n|fr|lycée|Lykeion|OSM19||grc:Lýkeion>fr:lycée>tr:lise
profesör|n|fr|professeur|açıkça bildiren|OSM19||la:professor>fr:professeur>tr:profesör
doktor|n|fr|docteur|öğreten|OSM19||la:doctor>fr:docteur>tr:doktor
doçent|n|de|Dozent|öğreten|CUM||la:docens>de:Dozent>tr:doçent
diploma|n|it|diploma|ikiye katlanmış|OSM19||
sertifika|n|fr|certificat|kesinleştirilmiş|CUM||la:certificatum>fr:certificat>tr:sertifika
kültür|n|fr|culture|ekip biçme|CUM||la:cultura>fr:culture>tr:kültür
ekonomi|n|fr|économie|ev yönetimi|OSM19|oikos|grc:oikonomía>fr:économie>tr:ekonomi
banka|n|it|banca|tezgâh|OSM19||ger:bank>it:banca>tr:banka
borsa|n|it|borsa|kese|OSM19||la:bursa>it:borsa>tr:borsa
fatura|n|it|fattura|yapılmış|OSM19||la:factura>it:fattura>tr:fatura
firma|n|it|firma|imza|CUM||la:firmare>it:firma>tr:firma
kasa|n|it|cassa|kutu|OSM19||la:capsa>it:cassa>tr:kasa
sigorta|n|it|sicurtà|güvence|OSM19||la:securitas>it:sicurtà>tr:sigorta
poliçe|n|it|polizza|yazılı belge|OSM19||grc:apódeixis>it:polizza>tr:poliçe
ciro|n|it|giro|dönüş|CUM||la:gyrus>it:giro>tr:ciro
acente|n|it|agente|iş yapan|OSM19||la:agens>it:agente>tr:acente
avukat|n|fr|avocat|yardıma çağrılan|OSM19|vocare|la:advocatus>fr:avocat>tr:avukat
antika|n|it|antica|eski|OSM19||la:antiquus>it:antica>tr:antika
bavul|n|it|baule|sandık|OSM19||it:baule>tr:bavul
bezelye|n|it|pisello|bezelye|OSM19||la:pisum>it:pisello>tr:bezelye
fanila|n|it|flanella|yünlü kumaş|OSM19||en:flannel>it:flanella>tr:fanila
iskele|n|it|scala|merdiven|EAT|scala|la:scala>it:scala>tr:iskele
iskonto|n|it|sconto|indirim|OSM19||it:sconto>tr:iskonto
kaparo|n|it|caparra|ön ödeme|OSM19||it:caparra>tr:kaparo
karyola|n|it|carriola|tekerlekli yatak|OSM19||la:carrus>it:carriola>tr:karyola
korsan|n|it|corsaro|akıncı|OSM|currere|la:cursus>it:corsaro>tr:korsan
manivela|n|it|manovella|kol|OSM19||la:manus>it:manovella>tr:manivela
palyaço|n|it|pagliaccio|saman çuvalı|OSM19||la:palea>it:pagliaccio>tr:palyaço
piyango|n|it|bianco|beyaz|OSM19||it:bianco>tr:piyango
piyasa|n|it|piazza|meydan|OSM19||la:platea>it:piazza>tr:piyasa
posta|n|it|posta|konak yeri|OSM19||la:posita>it:posta>tr:posta
pusula|n|it|bussola|küçük kutu|OSM||la:buxis>it:bussola>tr:pusula
sigara|n|it|sigaro|sigara|OSM19||es:cigarro>it:sigaro>tr:sigara
tabela|n|it|tabella|küçük levha|OSM19||la:tabula>it:tabella>tr:tabela
tornavida|n|it|tornavite|vida çeviren|CUM||it:tornavite>tr:tornavida
vida|n|it|vite|asma; vida|OSM19||la:vitis>it:vite>tr:vida
vapur|n|fr|vapeur|buhar|OSM19||la:vapor>fr:vapeur>tr:vapur
kambiyo|n|it|cambio|değişim|OSM19||la:cambium>it:cambio>tr:kambiyo
kumanya|n|it|compagna|yol azığı|OSM||it:compagna>tr:kumanya
martı|n|it|marti|martı|OSM||it:marti>tr:martı
gazete|n|it|gazzetta|küçük para|OSM19||it:gazzetta>tr:gazete
mağaza|n|ar|maḫāzin|depolar|OSM|Ḫ-Z-N|ar:maḫāzin>it:magazzino>tr:mağaza
limonata|n|it|limonata|limonlu su|OSM19||it:limonata>tr:limonata
sofa takımı|n|ar|ṣuffa|oturma grubu|OSM||
anahtar|n|el|anoichtíri|açacak|EAT||grc:anoiktḕrion>el:anoichtíri>tr:anahtar
kilit|n|el|kleidí|anahtar|EAT||grc:kleidíon>el:kleidí>tr:kilit
kilise|n|el|ekklisía|toplantı|EAT||grc:ekklēsía>el:ekklisía>tr:kilise
manastır|n|el|monastíri|tek yaşanan yer|EAT||grc:monastḕrion>el:monastíri>tr:manastır
papaz|n|el|papás|baba|EAT||grc:pápas>el:papás>tr:papaz
keşiş|n|fa|kaşīş|rahip|EAT||arc:qaššīšā>fa:kaşīş>tr:keşiş
sınır taşı|n|tr|sınır|hudut taşı|OSM||
fidye|n|ar|fidya|kurtuluş bedeli|EAT||
temel|n|el|themélio|temel|EAT||grc:themélion>el:themélio>tr:temel
kiler|n|el|kellári|kiler|EAT||la:cellarium>el:kellári>tr:kiler
avlu|n|el|avlí|avlu|EAT||grc:aulḕ>el:avlí>tr:avlu
kümes|n|el|koumási|kümes|OSM||el:koumási>tr:kümes
sünger|n|el|sfoungári|sünger|OSM||grc:spóngos>el:sfoungári>tr:sünger
fener balığı|n|el|fanári|balık|OSM|phainein|
ızgara|n|el|schára|ızgara|OSM||grc:eskhára>el:schára>tr:ızgara
semaver|n|sl|samovar|kendi kaynatan|OSM19||ru:samovar>tr:semaver
mazot|n|sl|mazut|yağ artığı|CUM||ru:mazut>tr:mazot
kapuska|n|sl|kapusta|lahana|OSM||ru:kapusta>tr:kapuska
izbe|n|sl|izba|kulübe|OSM||ru:izba>tr:izbe
kral|n|sl|kralj|kral|EAT||ger:Karl>sl:kralj>tr:kral
kraliçe|n|sl|kraljica|kral eşi|EAT||sl:kraljica>tr:kraliçe
voyvoda|n|sl|vojevoda|ordu önderi|EAT||sl:vojevoda>tr:voyvoda
kuluçka|n|sl|kločka|tavuk|OSM||bg:kločka>tr:kuluçka
çete|n|sl|četa|birlik|OSM19||bg:četa>tr:çete
kosa|n|sl|kosa|tırpan|OSM||sl:kosa>tr:kosa
pulluk|n|sl|plug|saban|OSM19||bg:plug>tr:pulluk
koçan|n|sl|kočan|koçan|OSM||bg:kočan>tr:koçan
kokoreç|n|el|kokorétsi|bağırsak kızartması|OSM||
patika|n|sl|pateka|keçi yolu|OSM||bg:pateka>tr:patika
gocuk|n|sl|kožuh|kürk ceket|OSM||sl:kožuh>tr:gocuk
tundra|n|fr|toundra|tundra|CUM||ru:tundra>fr:toundra>tr:tundra
haç|n|hy|xačʿ|haç|EAT||hy:xačʿ>tr:haç
madımak|n|hy|madımak|ot|OSM||hy:madımak>tr:madımak
pezevenk|n|hy?|pozavag|aracı|OSM||hy:pozavag>tr:pezevenk
örnek|n|hy?|ōrinak|örnek|EAT||hy:ōrinak>tr:örnek
avanak|adj|hy?|havanag|saf|OSM||hy:havanag>tr:avanak
tel|n|hy?|t'el|tel|EAT||hy:t'el>tr:tel
hedik|n|hy|hadig|haşlanmış buğday|OSM||hy:hadig>tr:hedik
kaburga|n|mn|qabirγa|kaburga|DLT||mn:qabirγa>tr:kaburga
nöker|n|mn|nökür|yoldaş|DLT||mn:nökür>tr:nöker
maral|n|mn|maral|dişi geyik|OSM||mn:maral>tr:maral
şölen|n|mn|şölen|ziyafet|DLT||mn:şölen>tr:şölen
serin|adj|mn|serigün|serin|DLT||mn:serigün>tr:serin
ceren|n|mn|jegeren|ceylan|OSM||mn:jegeren>tr:ceren
cebe|n|mn|jebe|zırh|DLT||mn:jebe>tr:cebe
ceylan|n|mn|jegeren|ceylan|EAT||mn:jegeren>tr:ceylan
çağ|n|mn|čaγ|zaman|DLT||mn:čaγ>tr:çağ
çay|n|zh|chá|çay|OSM||zh:chá>fa:çāy>tr:çay
tofu|n|ja|tōfu|soya peyniri|NEW||zh:dòufu>ja:tōfu>tr:tofu
kimono|n|ja|kimono|giysi|CUM||ja:kimono>tr:kimono
cimnastik|n|fr|gymnastique|çıplak alıştırma|OSM19||grc:gymnastikós>fr:gymnastique>tr:cimnastik
jimnastik|n|fr|gymnastique|çıplak alıştırma|OSM19||grc:gymnastikós>fr:gymnastique>tr:jimnastik
şeker pancarı|n|fa|şakar|pancar|CUM||
pancar|n|hy|panjar|pancar|EAT||hy:panjar>tr:pancar
kuru fasulye|n|el|fasóli|fasulye yemeği|OSM||
turşucu|n|fa|turşī|turşu satan|OSM||
kayık yarışı|n|tr|kayguk|kayık yarışı|OSM||
kayak|n|tr|kayak|kar kayağı|DD||
"""
