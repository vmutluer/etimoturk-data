# -*- coding: utf-8 -*-
"""Korpus 14 — Ek söz varlığı: akrabalık, sayılar, renkler, günlük eşya, giyim, meslek, zaman, duygu,
eğitim, teknoloji, spor, müzik, din ve soyut kavramlar. Yinelenen madde başları üretimde atlanır."""

WORDS = r"""
# --- Akrabalık ve kişiler --------------------------------------------------------------
ana|n|tr|ana|anne|DLT||
ata|n|tr|ata|baba; dede|DLT||
dede|n|tr|dede|büyükbaba|EAT||
nine|n|tr|nine|büyükanne|OSM||
torun|n|hy|thoṛn|çocuğun çocuğu|EAT||
amca|n|tr|amca|babanın erkek kardeşi|OSM||ar:ʿamm>tr:amca
dayı|n|tr|tagay|annenin erkek kardeşi|DLT||
hala|n|ar|ḫāla|babanın kız kardeşi|EAT||
teyze|n|tr|teyze|annenin kız kardeşi|OSM||
yenge|n|tr|yeŋge|ağabeyin eşi|DLT||
enişte|n|fa|angişte|kız kardeşin kocası|OSM||
görümce|n|tr|görümce|kocanın kız kardeşi|OSM|*kör-|
baldız|n|tr|baldız|karının kız kardeşi|DLT||
kayın|n|tr|kadın|eşin erkek kardeşi|DLT||
güvey|n|tr|küdegü|damat|DLT||
damat|n|fa|dāmād|güvey|EAT||
dul|n|tr|tul|eşi ölmüş|DLT||
yetim|n|ar|yatīm|babasız|EAT||
öksüz|n|tr|ögsüz|annesiz|DLT|*ög-|
bebek|n|tr|bebek|yeni doğan|EAT||
emzik|n|tr|emzik|emme aracı|OSM|*em-|
emmek|v|tr|em-|süt içmek|DLT|*em-|
emzirmek|v|tr|emüz-|süt vermek|DLT|*em-|
# --- Sayılar ------------------------------------------------------------------------------
bir|num|tr|bir|1|ORH||
iki|num|tr|éki|2|ORH||
üç|num|tr|üç|3|ORH||
dört|num|tr|tört|4|ORH||
beş|num|tr|béş|5|ORH||
altı|num|tr|altı|6|ORH||
yedi|num|tr|yéti|7|ORH||
sekiz|num|tr|sekiz|8|ORH||
dokuz|num|tr|tokuz|9|ORH||
on|num|tr|on|10|ORH||
yirmi|num|tr|yégirmi|20|ORH||
otuz|num|tr|otuz|30|ORH||
kırk|num|tr|kırk|40|ORH||
elli|num|tr|élig|50|ORH||
altmış|num|tr|altmış|60|ORH||
yetmiş|num|tr|yétmiş|70|ORH||
seksen|num|tr|sekiz on|80|DLT||
doksan|num|tr|tokuz on|90|DLT||
yüz|num|tr|yüz|100|ORH||
bin|num|tr|bıŋ|1000|ORH||
tümen|num|tr|tümen|on bin|ORH||
milyon|num|fr|million|büyük bin|OSM19||it:milione>fr:million>tr:milyon
milyar|num|fr|milliard|bin milyon|CUM||
sıfır|num|ar|ṣifr|boş|EAT||ar:ṣifr>tr:sıfır
yarım|adj|tr|yarım|ikide bir|DLT|*yar-|
çeyrek|n|fa|çahār-yek|dörtte bir|OSM||
# --- Renkler --------------------------------------------------------------------------------
kara|adj|tr|kara|siyah|ORH||
kızıl|adj|tr|kızıl|kırmızı|ORH||
boz|adj|tr|boz|gri|DLT||
al|adj|tr|al|kırmızı|ORH||
yağız|adj|tr|yagız|koyu kahverengi|ORH||
kır|adj|tr|kır|ağarmış|DLT||
siyah|adj|fa|siyāh|kara|EAT||
beyaz|adj|ar|bayāḏ|aklık|EAT||
mor|adj|hy|mor|eflatun|EAT||
pembe|adj|fa|pambe|pamuk rengi|OSM||
lacivert|adj|fa|lāciverd|koyu mavi|EAT||fa:lāciverd>tr:lacivert
turuncu|adj|fa|turunc|turunç rengi|OSM||
eflatun|adj|ar|aflāṭūn|Platon'un adı; açık mor|OSM||grc:Plátōn>ar:aflāṭūn>tr:eflatun
bej|adj|fr|beige|doğal yün rengi|CUM||
gri|adj|fr|gris|kül rengi|CUM||
bordo|adj|fr|bordeaux|Bordeaux şarabı rengi|CUM||
turkuaz|adj|fr|turquoise|Türk taşı|CUM||fr:turquoise>tr:turkuaz
haki|adj|fa|ḫākī|toprak rengi|OSM19|-ī (nisbet)|fa:ḫāk>fa:ḫākī>ur:khākī>en:khaki>tr:haki
# --- Giyim ve eşya ------------------------------------------------------------------------
gömlek|n|tr|köŋlek|üst giysi|DLT||
pantolon|n|fr|pantalon|Pantalone tiplemesi|OSM19||it:Pantalone>fr:pantalon>tr:pantolon
etek|n|tr|etek|alt giysi|DLT||
ceket|n|fr|jaquette|kısa üstlük|OSM19||
palto|n|fr|paletot|üstlük|OSM19||
manto|n|fr|manteau|örtü|OSM19||la:mantellum>fr:manteau>tr:manto
kaban|n|fr|caban|kukuletalı üstlük|CUM||ar:qabāʾ>it:gabbano>fr:caban>tr:kaban
yelek|n|tr|yelek|kolsuz giysi|OSM||
kuşak|n|tr|kurşag|bel bağı|DLT|*kur-|
şalvar|n|fa|şalvār|bol pantolon|EAT||
fes|n|ar|fās|Fas kenti|OSM||
kalpak|n|tr|kalpak|börk|EAT||
börk|n|tr|börk|başlık|DLT||
sarık|n|tr|sarık|baş sargısı|EAT|*sar-|
sarmak|v|tr|sar-|dolamak|DLT|*sar-|
sargı|n|tr|sargı|sarılan bez|OSM|*sar-|
sarma|n|tr|sarma|sarılmış yemek|OSM|*sar-|
eldiven|n|tr|eldiven|el giysisi|OSM||
pabuç|n|fa|pā-pūş|ayak örtüsü|EAT|pā|
terlik|n|tr|terlik|ev ayakkabısı|OSM||
çizme|n|tr|çizme|uzun ayakkabı|OSM|*çiz-|
çizmek|v|tr|çiz-|çizgi yapmak|DLT|*çiz-|
çizgi|n|tr|çizgi|çizilen iz|OSM|*çiz-|
çizim|n|tr|çizim|çizme işi|DD|*çiz-|
düğme|n|tr|tügme|bağlama parçası|DLT|*tüg-|
düğüm|n|tr|tügün|bağ|DLT|*tüg-|
düğün|n|tr|tügün|evlenme töreni|DLT|*tüg-|
iğne|n|tr|yigne|dikiş aracı|DLT||
iplik|n|tr|yiplik|ince ip|DLT||
ip|n|tr|yip|bağ|DLT||
makas|n|ar|miqaṣṣ|kesme aracı|EAT||
dikiş|n|tr|tikiş|dikme işi|DLT|*dik-|
terzi|n|fa|derzī|dikici|EAT||
kumaş|n|ar|qumāş|dokuma|EAT||
atlas|n|ar|aṭlas|parlak kumaş|EAT||
kadife|n|ar|qaṭīfa|havlı kumaş|EAT||
keçe|n|tr|kidiz|dövme yün|DLT||
yastık|n|tr|yastuk|baş altlığı|DLT||
yorgan|n|tr|yogurkan|örtü|DLT||
çarşaf|n|fa|çādir-şab|gece örtüsü|OSM||
peşkir|n|fa|pīş-gīr|önlük; havlu|EAT||
havlu|n|tr|havlu|kurulama bezi|OSM||
sabun|n|ar|ṣābūn|temizlik maddesi|EAT||la:sapo>ar:ṣābūn>tr:sabun
tarak|n|tr|targak|saç düzenleyici|DLT||
dolap|n|ar|dūlāb|dönen; kapaklı eşya|EAT||fa:dōlāb>ar:dūlāb>tr:dolap
sandık|n|ar|ṣundūq|kapaklı kutu|EAT||
raf|n|ar|raff|yükseltilmiş yer|OSM||
sedir|n|ar|ṣadr|göğüs; baş köşe|EAT||
minder|n|tr|minder|oturma yastığı|OSM||
sehpa|n|fa|se-pā|üç ayak|OSM|pā|
sandalye|n|ar|ṣandalī|sandal ağacından|OSM||
koltuk|n|tr|koltuk|kol altı; oturak|DLT||
masa|n|it|mesa|yemek tahtası|OSM19||la:mensa>it:mesa>tr:masa
# --- Meslekler ------------------------------------------------------------------------------
demirci|n|tr|temirçi|demir işleyen|DLT||
kuyumcu|n|tr|kuyumcı|değerli maden işleyen|OSM||
kalaycı|n|tr|kalaycı|kalay yapan|OSM||
nalbant|n|fa|naʿl-band|nal bağlayan|OSM||ar:naʿl>fa:naʿl-band>tr:nalbant
marangoz|n|el|marangós|ağaç işçisi|OSM||it:marangone>el:marangós>tr:marangoz
duvarcı|n|fa|dīvār|duvar ören|OSM||
boyacı|n|tr|boyacı|boya yapan|OSM||
hamal|n|ar|ḥammāl|yük taşıyan|EAT|H-M-L|
çoban|n|fa|şubān|sürü güden|EAT||
avcı|n|tr|avçı|av yapan|DLT||
sucu|n|tr|suvçı|su satan|OSM||
bekçi|n|tr|bekçi|koruyan|OSM||
hizmetçi|n|ar|ḫidma|hizmet eden|OSM|H-D-M|
kâhya|n|fa|ked-ḫudā|ev sahibi; yönetici|OSM||
tüccar|n|ar|tuccār|ticaret yapanlar|EAT|T-C-R|
ticaret|n|ar|ticāra|alım satım|EAT|T-C-R|
tacir|n|ar|tācir|ticaret yapan|EAT|T-C-R|
esnaf|n|ar|aṣnāf|sınıflar|OSM||
zanaat|n|ar|ṣanʿa|el işi|EAT|S-N-A|
berber|n|it|barbiere|sakal tıraşçısı|OSM||la:barba>it:barbiere>tr:berber
şoför|n|fr|chauffeur|ısıtan|CUM||
pilot|n|fr|pilote|dümenci|CUM||
mühendis|n|ar|muhandis|geometri bilen|OSM19|H-N-D-S|
hendese|n|ar|handasa|geometri|OSM|H-N-D-S|
memur|n|ar|maʾmūr|emredilmiş|OSM|E-M-R|
amir|n|ar|āmir|emreden|OSM|E-M-R|
emir|n|ar|amr|buyruk|EAT|E-M-R|
# --- Zaman ----------------------------------------------------------------------------------
yarın|n|tr|yarın|gelecek gün|DLT||
bugün|n|tr|bu kün|içinde bulunulan gün|ORH|*kün|
öğle|n|tr|öyle|gün ortası|DLT||
ikindi|n|tr|ikindi|ikinci namaz vakti|EAT||
şafak|n|ar|şafaq|tan|EAT||
tan|n|tr|taŋ|gün ağarması|ORH||
güz|n|tr|küz|sonbahar|ORH||
mayıs|n|la|Maius|Maia ayı|OSM19||la:Maius>tr:mayıs
mart|n|la|Martius|Mars ayı|OSM19||la:Martius>tr:mart
nisan|n|ar|nīsān|nisan|EAT||akk:nisannu>ar:nīsān>tr:nisan
haziran|n|ar|ḥazīrān|haziran|EAT||
temmuz|n|ar|tammūz|temmuz|EAT||akk:Dumuzi>ar:tammūz>tr:temmuz
ağustos|n|la|Augustus|Augustus ayı|OSM||la:Augustus>el:ávgoustos>tr:ağustos
eylül|n|ar|aylūl|eylül|EAT||
kasım|n|ar|qāsim|bölen|EAT||
aralık|n|tr|aralık|ara; ay adı|DD||
ocak|n|tr|oçak|ateş yeri; ay adı|DLT||
şubat|n|ar|şubāṭ|şubat|EAT||
pazartesi|n|fa|bāzār|pazar ertesi|OSM||
salı|n|ar|ṯalāṯā|üçüncü gün|EAT||
çarşamba|n|fa|çahār-şanbe|dördüncü gün|EAT||
perşembe|n|fa|penc-şanbe|beşinci gün|EAT||
cuma|n|ar|cumʿa|toplanma günü|EAT|C-M-A|
cumartesi|n|ar|cumʿa|cuma ertesi|OSM|C-M-A|
# --- Duygu ve nitelik --------------------------------------------------------------------------
sevinç|n|tr|sevinç|mutluluk|DLT|*sev-|
üzüntü|n|tr|üzüntü|keder|TDK|*üz-|
öfke|n|tr|öpke|akciğer; kızgınlık|DLT||
kıskançlık|n|tr|kıskanç|haset|TDK||
utanç|n|tr|utanç|mahcubiyet|TDK|*ut-|
utanmak|v|tr|ut-|mahcup olmak|DLT|*ut-|
umut|n|tr|umut|ümit|TDK|*um-|
ummak|v|tr|um-|beklemek|DLT|*um-|
özlem|n|tr|özlem|hasret|DD|*öz|
hasret|n|ar|ḥasra|özlem|EAT||
keder|n|ar|kadar|bulanıklık; üzüntü|EAT||
gurur|n|ar|ġurūr|aldanma; kibir|EAT||
kibir|n|ar|kibr|büyüklenme|EAT|K-B-R|
büyük|adj|tr|bedük|iri|ORH||
küçük|adj|tr|kiçig|ufak|ORH||
uzun|adj|tr|uzun|boylu|ORH||
kısa|adj|tr|kısga|boysuz|DLT||
geniş|adj|tr|kéŋ|enli|ORH||
dar|adj|tr|tar|ensiz|DLT||
yüksek|adj|tr|yüksek|yukarıda|DLT|*yük-|
alçak|adj|tr|alçak|aşağıda; aşağılık|DLT||
derin|adj|tr|teriŋ|dibi uzak|ORH||
sıcak|adj|tr|ısıg|ısılı|DLT|*ısı-|
ısı|n|tr|ısıg|sıcaklık|DLT|*ısı-|
ısınmak|v|tr|ısın-|sıcaklık kazanmak|DLT|*ısı-|
soğuk|adj|tr|soguk|ısısız|DLT||
ılık|adj|tr|yılıg|az sıcak|DLT||
sert|adj|fa|sard|katı|OSM||
yumuşak|adj|tr|yumşak|sert olmayan|DLT||
hafif|adj|ar|ḫafīf|ağır olmayan|EAT||
temiz|adj|ar|tamīz|ayırt edilmiş|EAT|M-Y-Z|
kirli|adj|tr|kir|pis|OSM||
eski|adj|tr|eski|yeni olmayan|DLT||
genç|adj|tr|kenç|yaşı az|DLT||
yaşlı|adj|tr|yaşlıg|ihtiyar|DLT|*yaş-|
zengin|adj|fa|sangīn|taş gibi ağır; varlıklı|EAT||
fakir|adj|ar|faqīr|yoksul|EAT||
yoksul|adj|tr|yoksul|fakir|DD||
# --- Eğitim, teknoloji ve bilim ------------------------------------------------------------------
öğrenci|n|tr|öğrenci|öğrenen|DD|*ög-|
öğretim|n|tr|öğretim|öğretme|DD|*ög-|
ödev|n|tr|ödev|görev|DD|*öde-|
ödemek|v|tr|öte-|borcu vermek|DLT|*öde-|
ödül|n|tr|ödül|mükâfat|DD|*öde-|
sınav|n|tr|sına-|imtihan|DD|*sına-|
sınamak|v|tr|sına-|denemek|DLT|*sına-|
imtihan|n|ar|imtiḥān|deneme|OSM||
üniversite|n|fr|université|bütünlük|CUM|unus|la:universitas>fr:université>tr:üniversite
üniforma|n|fr|uniforme|tek biçim|OSM19|unus|
ünite|n|fr|unité|birim|MOD|unus|
fakülte|n|fr|faculté|yeti|CUM|facere|
akademi|n|fr|académie|Platon'un bahçesi|OSM19||grc:Akadḕmeia>fr:académie>tr:akademi
lise|n|fr|lycée|Aristoteles'in okulu|OSM19||grc:Lýkeion>fr:lycée>tr:lise
profesör|n|fr|professeur|açıkça söyleyen|OSM19||
doçent|n|de|Dozent|öğreten|CUM||la:docens>de:Dozent>tr:doçent
teknoloji|n|fr|technologie|sanat bilgisi|CUM|tekhne|
teknik|n|fr|technique|sanata ilişkin|OSM19|tekhne|
teknisyen|n|fr|technicien|teknik görevli|CUM|tekhne|
makine|n|it|macchina|aygıt|OSM19|mekhane|grc:mēkhanḕ>la:machina>it:macchina>tr:makine
mekanik|n|fr|mécanique|makineye ilişkin|OSM19|mekhane|
mekanizma|n|it|meccanismo|işleyiş|CUM||
motor|n|fr|moteur|hareket ettiren|CUM|movere|la:motor>fr:moteur>tr:motor
mobil|adj|fr|mobile|hareketli|MOD|movere|
mobilya|n|it|mobilia|taşınabilir eşya|OSM19|movere|
otomobil|n|fr|automobile|kendi hareket eden|CUM|movere|
elektrik|n|fr|électrique|kehribara ilişkin|OSM19|ēlektron|grc:ḕlektron>la:electricus>fr:électrique>tr:elektrik
elektron|n|fr|électron|kehribar|CUM|ēlektron|
elektronik|n|fr|électronique|elektrona ilişkin|MOD|ēlektron|
telefon|n|fr|téléphone|uzak ses|OSM19|tēle|
telgraf|n|fr|télégraphe|uzak yazı|OSM19|tēle|
televizyon|n|fr|télévision|uzak görüş|CUM|tēle|
teleskop|n|fr|télescope|uzağı gören|OSM19|tēle|
radyo|n|fr|radio|ışın|CUM|radius|la:radius>fr:radio>tr:radyo
radyasyon|n|fr|radiation|ışınım|MOD|radius|
radyatör|n|fr|radiateur|ısı yayan|CUM|radius|
fotoğraf|n|fr|photographie|ışık yazısı|OSM19|phōs|grc:phôs>fr:photographie>tr:fotoğraf
foton|n|fr|photon|ışık parçacığı|MOD|phōs|
fosfor|n|fr|phosphore|ışık taşıyan|OSM19|phōs|
yazılım|n|tr|yazılım|program|MOD|*yaz-|
donanım|n|tr|donanım|aygıt bütünü|MOD||
internet|n|en|internet|ağlar arası|NEW||
dijital|adj|fr|digital|parmağa ilişkin|NEW||la:digitus>en:digital>fr:digital>tr:dijital
sayısal|adj|tr|sayısal|dijital|MOD|*say-|
yapay|adj|tr|yapay|doğal olmayan|DD|*yap-|
zekâ|n|ar|ẕakāʾ|keskin anlayış|OSM||
veri|n|tr|veri|bilgi birimi|DD|*ver-|
# --- Spor ve oyun ---------------------------------------------------------------------------------
spor|n|fr|sport|eğlence|CUM|portare|la:deportare>fro:desport>en:sport>fr:sport>tr:spor
futbol|n|en|football|ayak topu|CUM||
basketbol|n|en|basketball|sepet topu|CUM||
voleybol|n|en|volleyball|uçuş topu|CUM||
tenis|n|fr|tennis|tutun|CUM||fro:tenez>en:tennis>fr:tennis>tr:tenis
güreş|n|tr|küreş|boğuşma|DLT|*küreş-|
güreşmek|v|tr|küreş-|boğuşmak|DLT|*küreş-|
pehlivan|n|fa|pahlavān|Pehlevi yiğidi|EAT||
cirit|n|ar|carīd|hurma dalı; mızrak|EAT||
okçuluk|n|tr|ok|ok atma sporu|TDK||
ok|n|tr|ok|yay ile atılan|ORH||
at|n|tr|at|binek hayvanı|ORH||
atlet|n|fr|athlète|yarışan|CUM||grc:athlētḕs>fr:athlète>tr:atlet
antrenör|n|fr|entraîneur|çalıştıran|CUM||
şampiyon|n|fr|champion|alan savaşçısı|CUM||la:campus>fr:champion>tr:şampiyon
takım|n|tr|takım|bir arada bulunan grup|OSM|*tak-|
takmak|v|tr|tak-|iliştirmek|DLT|*tak-|
takı|n|tr|takı|süs eşyası|OSM|*tak-|
olimpiyat|n|fr|olympiade|Olympia oyunları|CUM||
satranç|n|fa|şatranc|dört kol|EAT||sa:caturaṅga>fa:şatranc>tr:satranç
tavla|n|it|tavola|tahta|OSM||la:tabula>it:tavola>tr:tavla
zar|n|ar|zahr|çiçek; oyun küpü|EAT||
dama|n|fr|dame|hanım|OSM19||
iskambil|n|it|scambio|değiş tokuş|OSM19||
# --- Müzik -------------------------------------------------------------------------------------------
müzik|n|fr|musique|Musa'lara ilişkin|OSM19|mousa|grc:mousikḕ>fr:musique>tr:müzik
mozaik|n|fr|mosaïque|Musa'lara ilişkin|OSM19|mousa|grc:mouseîon>la:musaicum>fr:mosaïque>tr:mozaik
musiki|n|ar|mūsīqī|müzik|EAT|mousa|grc:mousikḕ>ar:mūsīqī>tr:musiki
şarkıcı|n|fa|şarqī|şarkı söyleyen|OSM19||
türkü|n|tr|türkī|Türk'e özgü ezgi|OSM||
ezgi|n|tr|ezgi|melodi|DD||
melodi|n|fr|mélodie|ezgili şarkı|OSM19|ōidē|
parodi|n|fr|parodie|yan şarkı|MOD|ōidē|
rapsodi|n|fr|rhapsodie|dikilmiş şarkı|MOD|ōidē|
prozodi|n|fr|prosodie|şarkıya eklenen|MOD|ōidē|
orkestra|n|fr|orchestre|dans alanı|OSM19||grc:orkhḕstra>fr:orchestre>tr:orkestra
koro|n|it|coro|dans topluluğu|OSM19||grc:khorós>la:chorus>it:coro>tr:koro
piyano|n|it|piano|yumuşak|OSM19||
keman|n|fa|kamān|yay|EAT||
kemençe|n|fa|kamānçe|küçük yaylı|OSM||
ud|n|ar|ʿūd|ağaç; çalgı|EAT||
tambur|n|ar|ṭanbūr|telli çalgı|EAT||
saz|n|fa|sāz|çalgı|EAT||
bağlama|n|tr|bağla-|bağlı telli çalgı|OSM|*bağ-|
davul|n|ar|ṭabl|vurmalı çalgı|EAT||
zurna|n|fa|sūrnāy|düğün kavalı|EAT||
kaval|n|tr?|kaval|üflemeli çalgı|OSM||
ney|n|fa|nāy|kamış|EAT||
def|n|ar|daff|vurmalı çalgı|EAT||
gitar|n|fr|guitare|telli çalgı|CUM||grc:kithára>ar:qīṯāra>es:guitarra>fr:guitare>tr:gitar
flüt|n|fr|flûte|üflemeli çalgı|OSM19||
klarnet|n|fr|clarinette|berrak sesli|OSM19|clarus|
klasik|adj|fr|classique|birinci sınıf|CUM||la:classicus>fr:classique>tr:klasik
ritim|n|fr|rythme|akış|CUM||grc:rhythmós>fr:rythme>tr:ritim
armoni|n|fr|harmonie|uyum|OSM19||grc:harmonía>fr:harmonie>tr:armoni
konser|n|fr|concert|birlikte çalma|OSM19||
# --- Din ve gelenek ------------------------------------------------------------------------------------
Tanrı|n|tr|teŋri|gök; Tanrı|ORH||
Allah|n|ar|allāh|Tanrı|EAT||
yaradan|n|tr|yarat-|yaratıcı|EAT|*yar-|
yaratmak|v|tr|yarat-|var etmek|DLT|*yar-|
yaratık|n|tr|yaratık|yaratılmış|DD|*yar-|
dua|n|ar|duʿāʾ|çağrı; yakarış|EAT|D-A-W|
namaz|n|fa|namāz|eğilme|EAT||
oruç|n|fa|rōze|gün; oruç|EAT||
bayram|n|fa|baḏrām|şenlik|DLT||
kurban|n|ar|qurbān|yakınlaşma|EAT|K-R-B|
akraba|n|ar|aqribāʾ|yakınlar|OSM|K-R-B|
hac|n|ar|ḥacc|ziyaret|EAT|H-C-C|
hacı|n|ar|ḥāccī|hacca giden|EAT|H-C-C|
kıble|n|ar|qibla|yön|EAT||
ezan|n|ar|aḏān|duyuru|EAT|A-Z-N|
izin|n|ar|iḏn|müsaade|EAT|A-Z-N|
müezzin|n|ar|muʾaḏḏin|ezan okuyan|EAT|A-Z-N|
imam|n|ar|imām|önder|EAT|A-M-M|
ümmet|n|ar|umma|topluluk|EAT|A-M-M|
umumi|adj|ar|ʿumūmī|genel|OSM|A-M-M|
hutbe|n|ar|ḫuṭba|konuşma|EAT|H-T-B|
hitap|n|ar|ḫiṭāb|seslenme|OSM|H-T-B|
hatip|n|ar|ḫaṭīb|konuşmacı|EAT|H-T-B|
muhatap|n|ar|muḫāṭab|kendine seslenilen|OSM|H-T-B|
vaaz|n|ar|waʿẕ|öğüt|EAT||
melek|n|ar|malak|elçi|EAT||
şeytan|n|ar|şayṭān|uzak olan|EAT||he:śāṭān>ar:şayṭān>tr:şeytan
cennet|n|ar|canna|bahçe|EAT|C-N-N|
cin|n|ar|cinn|gizli varlık|EAT|C-N-N|
cinnet|n|ar|cinna|delilik|OSM|C-N-N|
mecnun|adj|ar|macnūn|cinli; deli|EAT|C-N-N|
cehennem|n|ar|cahannam|ateş çukuru|EAT||he:gē-hinnōm>ar:cahannam>tr:cehennem
uçmak|n|tr|uçmak|cennet|DLT||sog:uştmax>tr:uçmak
günah|n|fa|gunāh|suç|EAT||
sevap|n|ar|ṯawāb|karşılık|EAT||
haram|adj|ar|ḥarām|yasak|EAT|H-R-M|
harem|n|ar|ḥaram|yasak yer|EAT|H-R-M|
hürmet|n|ar|ḥurma|saygı|EAT|H-R-M|
mahrem|adj|ar|maḥram|yakın; gizli|EAT|H-R-M|
ihram|n|ar|iḥrām|hac giysisi|EAT|H-R-M|
muhterem|adj|ar|muḥtaram|saygıdeğer|OSM|H-R-M|
kutsal|adj|tr|kut|mübarek|DD|*kut|
kut|n|tr|kut|talih; kutluluk|ORH|*kut|
kutlu|adj|tr|kutlug|mübarek|ORH|*kut|
kutlamak|v|tr|kutla-|tebrik etmek|DD|*kut|
şaman|n|sl|şaman|Sibirya din adamı|CUM||evn:šamān>ru:шаман>tr:şaman
kam|n|tr|kam|şaman|DLT||
yuğ|n|tr|yog|cenaze töreni|ORH||
# --- Ortak sözcük başlıkları için ek maddeler --------------------------------------------------
aman|intj|ar|amān|güvenlik; yakarış ünlemi|EAT|A-M-N|
ataman|n|sl|ataman|Kazak reisi|OSM19||tr:ata>ru:атаман>tr:ataman
bedava|adj|fa|bād-i havā|hava parası; karşılıksız|OSM||
bre|intj|el|moré|be, hey|EAT||
haydut|n|hu|hajdú|sığır çobanı; başıbozuk asker|OSM||
kabadayı|n|tr|kaba dayı|yiğit; zorba|OSM||
kurgan|n|tr|kurgan|höyük; kale|DLT|*koru-|
nal|n|ar|naʿl|at ayakkabısı|EAT||
tabur|n|tr|tabur|asker birliği; çember|OSM||
tulumba|n|it|tromba|pompa; tatlı|OSM||
yas|n|tr|yas|ölüm acısı; zarar|ORH||
çakı|n|tr|çakı|katlanır bıçak|OSM|*çak-|
çakmak|v|tr|çak-|vurmak; tutuşturmak|DLT|*çak-|
çakmak|n|tr|çakmak|ateş yakma aracı|OSM|*çak-|
çardak|n|fa|çār-ṭāq|dört kemer|EAT||
"""

FAMILIES = r"""
*em-|tr|süt emmek|Eski Türkçe em- "emmek"; emmek, emzirmek ve emzik aynı kökten gelir.
*sar-|tr|dolamak|Eski Türkçe sar- "dolamak"; sarmak, sarık, sargı ve sarma (yemek) aynı kökten türer.
*çiz-|tr|çizgi yapmak|Eski Türkçe çiz- "çizmek"; çizmek, çizgi, çizim ve çizme (uzun ayakkabı) aynı kökten gelir.
*tüg-|tr|bağlamak, düğümlemek|Eski Türkçe tüg- "bağlamak"; düğüm, düğme ve düğün (bağlanma töreni) aynı kökten türer.
T-C-R|ar|alıp satmak|Arapça t-c-r kökü; ticaret, tacir ve tüccar aynı kökten gelir.
H-N-D-S|ar|geometri|Arapça h-n-d-s dörtlü kökü (Farsça andāze'den); hendese (geometri) ve mühendis aynı kökten türer.
E-M-R|ar|buyurmak|Arapça ʾ-m-r kökü; emir (buyruk), amir (buyuran) ve memur (buyrulan) aynı kökten gelir.
*ut-|tr|utanmak|Eski Türkçe ut- "utanmak"; utanmak ve utanç aynı kökten türer.
*um-|tr|beklemek, ummak|Eski Türkçe um- "ummak"; ummak ve umut aynı kökten gelir.
K-B-R|ar|büyük olmak|Arapça k-b-r kökü; kibir (büyüklenme), kebir, ekber ve tekbir aynı kökten türer.
*ısı-|tr|ısınmak|Eski Türkçe ısıg "sıcak"; ısı, ısınmak ve sıcak (ısıcak) aynı kökten gelir.
*öde-|tr|ödemek|Eski Türkçe öte- "ödemek"; ödemek, ödev (ödenmesi gereken) ve ödül aynı kökten türer.
*sına-|tr|denemek|Eski Türkçe sına- "denemek"; sınamak ve sınav aynı kökten gelir.
unus|la|bir|Latince unus "bir"; üniversite, üniforma ve ünite aynı kökten türer.
mekhane|el|araç, düzenek|Eski Yunanca mēkhanḕ "araç"; makine, mekanik ve mekanizma aynı kökten gelir.
movere|la|hareket ettirmek|Latince movere "hareket ettirmek"; motor, mobil, mobilya ve otomobil aynı kökten türer.
ēlektron|el|kehribar|Eski Yunanca ḕlektron "kehribar"; elektrik, elektron ve elektronik aynı kökten gelir.
tēle|el|uzak|Eski Yunanca têle "uzak"; telefon, telgraf, televizyon ve teleskop aynı kökten türer.
radius|la|ışın, çubuk|Latince radius "ışın"; radyo, radyasyon ve radyatör aynı kökten gelir.
phōs|el|ışık|Eski Yunanca phôs "ışık"; fotoğraf, foton ve fosfor aynı kökten türer.
*küreş-|tr|boğuşmak|Eski Türkçe küreş- "güreşmek"; güreş ve güreşmek aynı kökten gelir.
*tak-|tr|iliştirmek|Eski Türkçe tak- "takmak"; takmak, takı ve takım aynı kökten türer.
mousa|el|ilham perisi|Eski Yunanca Moûsa "ilham perisi"; müzik, musiki, müze ve mozaik aynı kökten gelir.
ōidē|el|şarkı|Eski Yunanca ōidḕ "şarkı"; melodi, komedi, trajedi, parodi, rapsodi ve prozodi aynı kökten türer.
clarus|la|parlak, berrak|Latince clarus "berrak"; klarnet aynı kökten gelir.
K-R-B|ar|yakın olmak|Arapça q-r-b kökü; kurban (yakınlaşma) ve akraba (yakınlar) aynı kökten türer.
H-C-C|ar|ziyaret etmek|Arapça ḥ-c-c kökü; hac ve hacı aynı kökten gelir.
A-Z-N|ar|duyurmak, izin vermek|Arapça ʾ-ḏ-n kökü; ezan (duyuru), müezzin ve izin aynı kökten türer.
A-M-M|ar|öne geçmek; genel|Arapça ʾ-m-m kökü; imam (önder), ümmet ve umumi aynı kökten gelir.
H-T-B|ar|konuşmak|Arapça ḫ-ṭ-b kökü; hutbe, hitap, hatip ve muhatap aynı kökten türer.
C-N-N|ar|örtmek, gizlemek|Arapça c-n-n kökü; cennet (örtülü bahçe), cin (gizli varlık), cinnet ve mecnun aynı kökten gelir.
H-R-M|ar|yasaklamak|Arapça ḥ-r-m kökü; haram, harem, mahrem, hürmet, ihram ve muhterem aynı kökten türer.
*çak-|tr|vurmak, tutuşturmak|Eski Türkçe çak- "vurmak, çakmak"; çakmak (eylem ve araç), çakı ve çakıl aynı kökten gelir.
*kut|tr|talih, kutluluk|Orhun Yazıtları'ndaki kut "talih"; kutlu, kutsal ve kutlamak aynı kökten gelir.
"""
