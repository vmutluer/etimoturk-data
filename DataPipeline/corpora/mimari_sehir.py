# -*- coding: utf-8 -*-
"""Korpus 10 — Mimari ve şehir: yapı öğeleri, dinî ve sivil mimari, kent yönetimi ve mekân adları."""

WORDS = r"""
# --- Yapı ve mimari ---------------------------------------------------------------------
mimar|n|ar|miʿmār|yapı yapan|EAT|A-M-R|
mimari|n|ar|miʿmārī|yapı sanatı|OSM19|A-M-R|
imar|n|ar|iʿmār|bayındır kılma|OSM|A-M-R|
umran|n|ar|ʿumrān|bayındırlık|OSM|A-M-R|
mamur|adj|ar|maʿmūr|bayındır|EAT|A-M-R|
imaret|n|ar|ʿimāra|yapı; aş evi|EAT|A-M-R|
ömür|n|ar|ʿumr|yaşam süresi|EAT|A-M-R|
tamir|n|ar|taʿmīr|onarma|OSM|A-M-R|
bina|n|ar|binā|yapı|EAT|B-N-Y|
inşaat|n|ar|inşāʾāt|yapım işleri|OSM19|N-Ş-A|
inşa|n|ar|inşāʾ|kurma, yazma|EAT|N-Ş-A|
menşe|n|ar|manşaʾ|çıkış yeri|OSM|N-Ş-A|
neşet|n|ar|naşʾa|ortaya çıkma|OSM|N-Ş-A|
bünye|n|ar|bunya|yapı, kuruluş|OSM|B-N-Y|
mebni|adj|ar|mabnī|kurulmuş|OSM|B-N-Y|
sütun|n|fa|sutūn|direk|EAT||
kolon|n|fr|colonne|direk|CUM|columna|la:columna>fr:colonne>tr:kolon
kolonad|n|fr|colonnade|sütun dizisi|MOD|columna|
kubbe|n|ar|qubba|yuvarlak çatı|EAT|Q-B-B|
kebap|n|ar|kabāb|kızartılmış et|EAT||
kebapçı|n|ar|kabāb|kebap pişiren|OSM||
minare|n|ar|manāra|ışık yeri|EAT|N-W-R|
nur|n|ar|nūr|ışık|EAT|N-W-R|
münevver|adj|ar|munawwar|aydınlatılmış|OSM|N-W-R|
tenvir|n|ar|tanwīr|aydınlatma|OSM|N-W-R|
mihrap|n|ar|miḥrāb|savaş yeri; kıble nişi|EAT|H-R-B|
harp|n|ar|ḥarb|savaş|EAT|H-R-B|
muharebe|n|ar|muḥāraba|savaşma|OSM|H-R-B|
harbiye|n|ar|ḥarbiyya|savaş okulu|OSM19|H-R-B|
minber|n|ar|minbar|yükseltilmiş yer|EAT||
şadırvan|n|fa|şādurvān|çeşmeli havuz|OSM||
revak|n|ar|riwāq|sütunlu geçit|OSM||
eyvan|n|fa|eyvān|üç yanı kapalı mekân|EAT||
saray|n|fa|sarāy|büyük konut|EAT||
konak|n|tr|konak|konaklanan yer|DLT|*kon-|
yalı|n|el|yialí|kıyı; kıyı evi|OSM||
han|n|fa|ḫān|konaklama yeri|EAT||
kervansaray|n|fa|kārvān-sarāy|kervan konağı|EAT||
kervan|n|fa|kārvān|yolcu topluluğu|EAT||
medrese|n|ar|madrasa|ders yeri|EAT|D-R-S|
cami|n|ar|cāmiʿ|toplayan|EAT|C-M-A|
mescit|n|ar|mascid|secde yeri|EAT|S-C-D|
kümbet|n|fa|gunbed|kubbeli mezar|EAT||
çeşme|n|fa|çeşme|göz; kaynak|EAT||
sebil|n|ar|sabīl|yol; hayrat çeşmesi|EAT||
kuyu|n|tr|kudug|su çukuru|DLT||
sarnıç|n|ar|ṣihrīc|su deposu|EAT||
kanalizasyon|n|fr|canalisation|kanal döşeme|CUM|canalis|
kanal|n|fr|canal|su yolu|OSM19|canalis|la:canalis>fr:canal>tr:kanal
kaldırım|n|tr|kaldırım|yükseltilmiş yol|OSM|*kalk-|
bulvar|n|fr|boulevard|sur yolu|OSM19||nl:bolwerk>fr:boulevard>tr:bulvar
bedesten|n|fa|bezzāzistān|bezciler yeri|EAT|-istān|
arasta|n|fa|ārāste|bezenmiş çarşı|OSM||
menzil|n|ar|manzil|inilen yer|EAT|N-Z-L|
nüzul|n|ar|nuzūl|inme|OSM|N-Z-L|
tenzilat|n|ar|tanzīlāt|indirimler|OSM19|N-Z-L|
nazil|adj|ar|nāzil|inen|OSM|N-Z-L|
kale|n|ar|qalʿa|hisar|EAT||
sur|n|ar|sūr|kent duvarı|EAT||
burç|n|ar|burc|kule; yıldız kümesi|EAT||
hendek|n|ar|ḫandaq|çukur|EAT||fa:kandag>ar:ḫandaq>tr:hendek
hisar|n|ar|ḥiṣār|çevreleme; kale|EAT|H-S-R|
muhasara|n|ar|muḥāṣara|kuşatma|OSM|H-S-R|
hasır|n|ar|ḥaṣīr|örülmüş yaygı|EAT|H-S-R|
kule|n|ar|qulla|tepe|EAT||
eşik|n|tr|éşik|kapı altı|DLT||
cam|n|fa|cām|kadeh; cam|EAT||
çerçeve|n|fa|çār-çūbe|dört çubuk|OSM||
tuğla|n|el|toúvla|pişmiş kil|OSM|tegere|la:tegula>el:toúvla>tr:tuğla
dedektif|n|fr|détective|örtüyü kaldıran|CUM|tegere|la:detegere>en:detective>fr:détective>tr:dedektif
dedektör|n|fr|détecteur|bulucu|MOD|tegere|
kerpiç|n|tr|kerpiç|güneşte kurutulmuş kil|DLT||
harç|n|ar|ḫarc|çıkan; masraf; bağlayıcı|EAT|H-R-C|
harcamak|v|ar|ḫarc|para çıkarmak|EAT|H-R-C|
harçlık|n|ar|ḫarc|küçük harcama parası|OSM|H-R-C|
ihraç|n|ar|iḫrāc|dışa çıkarma|OSM19|H-R-C|
mahreç|n|ar|maḫrac|çıkış yeri|OSM|H-R-C|
hariç|adj|ar|ḫāric|dışta|OSM|H-R-C|
beton|n|fr|béton|çakıl harcı|CUM||la:bitumen>fr:béton>tr:beton
çimento|n|it|cimento|kırma taş|OSM19||la:caementum>it:cimento>tr:çimento
çelik|n|tr|çelik|sert demir|OSM||
kereste|n|fa|kiraste|yapı tahtası|OSM||
tahta|n|fa|taḫte|levha|EAT||
kiriş|n|tr|kiriş|yay teli; çatı direği|DLT||
çatı|n|tr|çatı|birleşen örtü|OSM|*çat-|
çatmak|v|tr|çat-|birleştirmek|DLT|*çat-|
çatışma|n|tr|çatış-|karşı karşıya gelme|TDK|*çat-|
dam|n|tr|tam|çatı; duvar|ORH||
saçak|n|tr|saçak|çatı çıkıntısı|OSM||
baca|n|fa|bāce|küçük pencere|EAT||
oluk|n|tr|oluk|su yolu|DLT||
basamak|n|tr|basamak|basılan yer|OSM|*bas-|
taban|n|tr|taban|alt yüz|DLT||
döşeme|n|tr|döşe-|yer kaplaması|OSM||
zemin|n|fa|zamīn|yer|EAT||
kat|n|tr|kat|katman|DLT|*kat-|
katmak|v|tr|kat-|eklemek|DLT|*kat-|
katman|n|tr|katman|tabaka|DD|*kat-|
katkı|n|tr|katkı|ekleme|DD|*kat-|
ahır|n|fa|āḫur|hayvan barınağı|EAT||
hangar|n|fr|hangar|üstü kapalı yer|CUM||
garaj|n|fr|garage|koruma yeri|CUM||
apartman|n|fr|appartement|ayrılmış bölüm|CUM||
daire|n|ar|dāʾira|dönen; çember; bölüm|OSM|D-W-R|
asansör|n|fr|ascenseur|yükselten|CUM||
teras|n|fr|terrasse|toprak set|CUM|terra|la:terra>fr:terrasse>tr:teras
terakota|n|it|terracotta|pişmiş toprak|MOD|terra|
teritoryal|adj|fr|territorial|toprağa ilişkin|MOD|terra|
hol|n|en|hall|giriş odası|CUM||
koridor|n|fr|corridor|koşulan yer|CUM|currere|it:corridore>fr:corridor>tr:koridor
antre|n|fr|entrée|giriş|CUM||
tuvalet|n|fr|toilette|küçük bez|CUM||
lavabo|n|fr|lavabo|yıkayacağım|CUM||la:lavabo>fr:lavabo>tr:lavabo
klozet|n|en|closet|kapalı yer|MOD||
hela|n|ar|ḫalāʾ|boşluk; ayakyolu|OSM||
avize|n|fa|āvīze|asılı|OSM||
şamdan|n|fa|şamʿ-dān|mum kabı|EAT||
mum|n|fa|mūm|balmumu|EAT||
kandil|n|ar|qindīl|yağ lambası|EAT||la:candela>ar:qindīl>tr:kandil
# --- Kent ve yönetim ---------------------------------------------------------------------
semt|n|ar|samt|yön; bölge|OSM||
anıt|n|tr|anıt|anma yapısı|DD|*an-|
heykel|n|ar|haykal|büyük yapı; yontu|OSM||
abide|n|ar|ābide|kalıcı yapı|OSM|A-B-D|
müze|n|fr|musée|ilham perileri evi|OSM19||grc:mouseîon>la:museum>fr:musée>tr:müze
tiyatro|n|it|teatro|seyir yeri|OSM19|theā|grc:théatron>la:theatrum>it:teatro>tr:tiyatro
teori|n|fr|théorie|seyretme; kuram|OSM19|theā|grc:theōría>fr:théorie>tr:teori
teorem|n|fr|théorème|görülen şey|CUM|theā|
teatral|adj|fr|théâtral|tiyatroya ilişkin|MOD|theā|
teorik|adj|fr|théorique|kurama ilişkin|CUM|theā|
sinema|n|fr|cinéma|hareket|CUM|kinein|grc:kínēma>fr:cinéma>tr:sinema
kinetik|adj|fr|cinétique|hareketli|MOD|kinein|
stadyum|n|fr|stade|koşu alanı|CUM||grc:stádion>la:stadium>fr:stade>tr:stadyum
hipodrom|n|fr|hippodrome|at koşusu yeri|OSM19|hippos|
hipopotam|n|fr|hippopotame|nehir atı|CUM|hippos|
otel|n|fr|hôtel|konuk evi|OSM19|hospes|la:hospitale>fr:hôtel>tr:otel
pansiyon|n|fr|pension|ödeme; konaklama|OSM19|pendere|
motel|n|en|motel|motorlu otel|MOD|hospes|
pazaryeri|n|fa|bāzār|pazar kurulan yer|TDK||
"""

FAMILIES = r"""
*çat-|tr|birleştirmek|Eski Türkçe çat- "birleştirmek, çarpıştırmak"; çatı (birleştirilen örtü), çatmak ve çatışma aynı kökten gelir.
*kat-|tr|eklemek|Eski Türkçe kat- "eklemek, karıştırmak"; kat (katman), katmak, katkı ve katman aynı kökten türer.
A-M-R|ar|yaşamak; bayındır kılmak|Arapça ʿ-m-r kökü; ömür (yaşam süresi), mimar, mimari, imar, umran, mamur, imaret ve tamir aynı kökten gelir.
B-N-Y|ar|kurmak|Arapça b-n-y kökü; bina, bünye (yapı) ve mebni aynı kökten türer.
N-Ş-A|ar|ortaya çıkmak, kurmak|Arapça n-ş-ʾ kökü; inşa, inşaat, menşe (çıkış yeri), neşet ve naşʾa (yetişme; ilk coşku) > neşe, neşeli aynı kökten gelir. Neşe için n-ş-ṭ (neşat) bağlantısı da önerilmiştir.
columna|la|sütun|Latince columna "sütun"; kolon ve kolonad aynı kökten türer.
Q-B-B|ar|kubbe yapmak; yuvarlak olmak|Arapça q-b-b kökü; qubba (kubbe) > kubbe ve kubbealtı aynı kökten gelir. Kebap bu kökten değildir: kabāb, Aramice/Akkadca "yakmak, kavurmak" anlamlı bir köke bağlanır.
N-W-R|ar|ışık|Arapça n-w-r kökü; nur, minare (ışık yeri), münevver ve tenvir aynı kökten türer.
H-R-B|ar|savaş|Arapça ḥ-r-b kökü; harp, muharebe, harbiye ve mihrap (savaş yeri; kıble nişi) aynı kökten gelir.
canalis|la|oluk|Latince canalis "oluk"; kanal ve kanalizasyon aynı kökten türer.
N-Z-L|ar|inmek|Arapça n-z-l kökü; menzil (inilen yer), nüzul, nazil ve tenzilat aynı kökten gelir.
H-S-R|ar|çevrelemek|Arapça ḥ-ṣ-r kökü; hisar, muhasara (kuşatma) ve hasır (örülmüş yaygı) aynı kökten türer.
tegere|la|örtmek|Latince tegere "örtmek"; tegula yoluyla tuğla, detegere yoluyla dedektif ve dedektör aynı kökten gelir.
H-R-C|ar|çıkmak|Arapça ḫ-r-c kökü; harç, harcamak, harçlık, ihraç, mahreç ve hariç aynı kökten türer.
terra|la|toprak|Latince terra "toprak"; teras, terakota ve teritoryal aynı kökten gelir.
theā|el|seyretmek|Eski Yunanca theâsthai "seyretmek"; tiyatro, teori (seyretme, kuram), teorem, teorik ve teatral aynı kökten türer.
kinein|el|hareket etmek|Eski Yunanca kineîn "hareket etmek"; sinema (hareket) ve kinetik aynı kökten gelir.
hippos|el|at|Eski Yunanca híppos "at"; hipodrom (at koşusu yeri) ve hipopotam (nehir atı) aynı kökten türer.
hospes|la|konuk|Latince hospes "konuk"; otel, hastane anlamındaki hôpital ve motel aynı kökten gelir.
pendere|la|asmak, ödemek|Latince pendere "asmak, tartmak, ödemek"; pansiyon (ödeme) aynı kökten türer.
"""
