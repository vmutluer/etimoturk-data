# -*- coding: utf-8 -*-
"""Korpus 16 — Bilim ve teknoloji: fizik, kimya, matematik, gök bilimi, mühendislik, elektrik, ölçü birimleri, bilişim ve Dil Devrimi bilim terimleri."""

WORDS = r"""
# --- Fizik, matematik ve genel bilim (Yunanca kökler, Fransızca yoluyla) -----------------
fizik|n|fr|physique|doğaya ilişkin|OSM19|physis|grc:physikḗ>la:physica>fr:physique>tr:fizik
fizikçi|n|fr|physique|fizik bilgini|CUM|physis|
fiziksel|adj|fr|physique|fiziğe ilişkin|TDK|physis|
fizyoterapi|n|fr|physiothérapie|doğal yolla sağaltım|MOD|physis|grc:physis>fr:physiothérapie>tr:fizyoterapi
fizyonomi|n|fr|physionomie|doğal görünüş|OSM19|physis|grc:physiognōmía>fr:physionomie>tr:fizyonomi
matematik|n|fr|mathématique|öğrenilen şeyler bilgisi|OSM19|mathēma|grc:mathēmatikḗ>la:mathematica>fr:mathématique>tr:matematik
matematikçi|n|fr|mathématique|matematik bilgini|CUM|mathēma|
matematiksel|adj|fr|mathématique|matematiğe ilişkin|TDK|mathēma|
aritmetik|n|fr|arithmétique|sayı bilgisi|OSM19|arithmos|grc:arithmētikḗ>la:arithmetica>fr:arithmétique>tr:aritmetik
logaritma|n|fr|logarithme|oran sayısı|OSM19|arithmos|grc:lógos+arithmós>fr:logarithme>tr:logaritma
algoritma|n|fr|algorithme|Hârizmî'nin yöntemi|MOD||ar:al-Ḫwārizmī>la:algorismus>fr:algorithme>tr:algoritma
analiz|n|fr|analyse|çözme, ayrıştırma|CUM|lyein|grc:análysis>fr:analyse>tr:analiz
analist|n|fr|analyste|çözümleyici|MOD|lyein|
analitik|adj|fr|analytique|çözümlemeli|CUM|lyein|grc:analytikós>fr:analytique>tr:analitik
kataliz|n|fr|catalyse|çözüp ayırma|MOD|lyein|grc:katálysis>fr:catalyse>tr:kataliz
katalizör|n|fr|catalyseur|tepkimeyi hızlandıran|MOD|lyein|
elektroliz|n|fr|électrolyse|elektrikle çözme|CUM|lyein|grc:ḗlektron+lýsis>fr:électrolyse>tr:elektroliz
diyaliz|n|fr|dialyse|ayrıştırarak çözme|MOD|lyein|grc:diálysis>fr:dialyse>tr:diyaliz
hidroliz|n|fr|hydrolyse|suyla çözünme|MOD|lyein|grc:hýdōr+lýsis>fr:hydrolyse>tr:hidroliz
sentez|n|fr|synthèse|birlikte koyma|CUM|tithenai|grc:sýnthesis>fr:synthèse>tr:sentez
sentetik|adj|fr|synthétique|bireşimle yapılmış|CUM|tithenai|grc:synthetikós>fr:synthétique>tr:sentetik
antitez|n|fr|antithèse|karşı koyma|CUM|tithenai|grc:antíthesis>fr:antithèse>tr:antitez
protez|n|fr|prothèse|yerine konan|MOD|tithenai|grc:prósthesis>fr:prothèse>tr:protez
fotosentez|n|fr|photosynthèse|ışıkla bireşim|MOD|tithenai|grc:phôs+sýnthesis>fr:photosynthèse>tr:fotosentez
santral|n|fr|central|merkezî|CUM|kentron|grc:kéntron>la:centrum>fr:central>tr:santral
santrifüj|n|fr|centrifuge|merkezden kaçan|MOD|kentron|la:centrum+fugere>fr:centrifuge>tr:santrifüj
konsantre|adj|fr|concentré|merkeze toplanmış|CUM|kentron|la:centrum>fr:concentré>tr:konsantre
konsantrasyon|n|fr|concentration|bir merkezde toplanma|CUM|kentron|la:centrum>fr:concentration>tr:konsantrasyon
eksantrik|adj|fr|excentrique|merkez dışı|CUM|kentron|grc:ékkentros>fr:excentrique>tr:eksantrik
kronoloji|n|fr|chronologie|zaman bilgisi|OSM19|khronos|grc:khrónos+lógos>fr:chronologie>tr:kronoloji
kronik|adj|fr|chronique|süregelen|CUM|khronos|grc:khronikós>fr:chronique>tr:kronik
kronometre|n|fr|chronomètre|zaman ölçer|CUM|khronos|grc:khrónos+métron>fr:chronomètre>tr:kronometre
senkron|adj|fr|synchrone|eş zamanlı|MOD|khronos|grc:sýnkhronos>fr:synchrone>tr:senkron
anakronizm|n|fr|anachronisme|zaman yanılgısı|MOD|khronos|grc:anakhronismós>fr:anachronisme>tr:anakronizm
topoloji|n|fr|topologie|yer bilgisi|MOD|topos|grc:tópos+lógos>fr:topologie>tr:topoloji
ütopya|n|fr|utopie|olmayan yer|CUM|topos|grc:ou+tópos>la:Utopia>fr:utopie>tr:ütopya
izotop|n|fr|isotope|aynı yerde|MOD|isos|grc:ísos+tópos>fr:isotope>tr:izotop
izomer|n|fr|isomère|eşit paylı|MOD|isos|grc:ísos+méros>fr:isomère>tr:izomer
izometrik|adj|fr|isométrique|eşit ölçülü|MOD|isos|grc:ísos+métron>fr:isométrique>tr:izometrik
somatik|adj|fr|somatique|bedene ilişkin|MOD|sōma|grc:sōmatikós>fr:somatique>tr:somatik
ribozom|n|fr|ribosome|riboz cisimciği|MOD|sōma|grc:sôma>fr:ribosome>tr:ribozom
plazma|n|fr|plasma|biçimlendirilmiş|MOD|plassein|grc:plásma>fr:plasma>tr:plazma
plaster|n|fr|plâtre|sıva; yakı|CUM|plassein|grc:émplastron>la:emplastrum>fr:plâtre>tr:plaster
homojen|adj|fr|homogène|aynı türden|CUM|homos|grc:homogenḗs>fr:homogène>tr:homojen
homolog|adj|fr|homologue|aynı sözlü, denk|MOD|homos|grc:homólogos>fr:homologue>tr:homolog
heterojen|adj|fr|hétérogène|başka türden|CUM|heteros|grc:heterogenḗs>fr:hétérogène>tr:heterojen
heterodoks|adj|fr|hétérodoxe|başka görüşlü|MOD|heteros|grc:heteródoxos>fr:hétérodoxe>tr:heterodoks
hiperbol|n|fr|hyperbole|aşırı atış|CUM|hyper|grc:hyperbolḗ>fr:hyperbole>tr:hiperbol
hipermetrop|adj|fr|hypermétrope|ölçü ötesi gören|MOD|hyper|grc:hypérmetros+ṓps>fr:hypermétrope>tr:hipermetrop
hiperaktif|adj|fr|hyperactif|aşırı etkin|MOD|hyper|grc:hypér+la:activus>fr:hyperactif>tr:hiperaktif
hipermarket|n|fr|hypermarché|büyük pazar|NEW|hyper|grc:hypér+la:mercatus>fr:hypermarché>tr:hipermarket
hipotenüs|n|fr|hypoténuse|altta gerilen|CUM|hypo|grc:hypoteínousa>la:hypotenusa>fr:hypoténuse>tr:hipotenüs
hipotermi|n|fr|hypothermie|düşük sıcaklık|MOD|hypo|grc:hypó+thermós>fr:hypothermie>tr:hipotermi
kripto|n|en|crypto|gizli|NEW|kryptos|grc:kryptós>en:crypto>tr:kripto
kriptoloji|n|fr|cryptologie|gizli yazı bilgisi|MOD|kryptos|grc:kryptós+lógos>fr:cryptologie>tr:kriptoloji
kriptografi|n|fr|cryptographie|gizli yazım|MOD|kryptos|grc:kryptós+gráphein>fr:cryptographie>tr:kriptografi
kripton|n|fr|krypton|gizli gaz|MOD|kryptos|grc:kryptón>fr:krypton>tr:kripton
manyetik|adj|fr|magnétique|mıknatısa ilişkin|CUM|Magnēsia|grc:Magnēsía>la:magneticus>fr:magnétique>tr:manyetik
manyetizma|n|fr|magnétisme|mıknatıslık|OSM19|Magnēsia|grc:magnḗtēs>fr:magnétisme>tr:manyetizma
manyeto|n|fr|magnéto|mıknatıslı üreteç|CUM|Magnēsia|grc:magnḗtēs>fr:magnéto>tr:manyeto
kimyager|n|ar|kīmiyā|kimya bilgini|OSM19|khēmeia|grc:khēmeía>ar:kīmiyāʾ>fa:kīmiyāger>tr:kimyager
kimyasal|adj|ar|kīmiyā|kimyaya ilişkin|TDK|khēmeia|
kimyacı|n|ar|kīmiyā|kimya ile uğraşan|CUM|khēmeia|
alşimi|n|fr|alchimie|dönüştürme sanatı|CUM|khēmeia|grc:khēmeía>ar:al-kīmiyāʾ>la:alchimia>fr:alchimie>tr:alşimi
biyokimya|n|fr|biochimie|yaşam kimyası|MOD|khēmeia|grc:bíos+khēmeía>fr:biochimie>tr:biyokimya
oksit|n|fr|oxyde|oksijen bileşiği|CUM|oxys|grc:oxýs>fr:oxyde>tr:oksit
oksitlenmek|v|fr|oxyde|oksijenle birleşmek|MOD|oxys|
oksidasyon|n|fr|oxydation|oksitlenme|CUM|oxys|grc:oxýs>fr:oxydation>tr:oksidasyon
dioksit|n|fr|dioxyde|iki oksijenli|MOD|oxys|grc:dís+oxýs>fr:dioxyde>tr:dioksit
antioksidan|n|fr|antioxydant|oksitlenmeyi önleyen|NEW|oxys|grc:antí+oxýs>fr:antioxydant>tr:antioksidan
peroksit|n|fr|peroxyde|fazla oksijenli|MOD|oxys|grc:perí+oxýs>fr:peroxyde>tr:peroksit
proton|n|fr|proton|ilk olan|CUM|prōtos|grc:prôton>en:proton>fr:proton>tr:proton
prototip|n|fr|prototype|ilk örnek|MOD|prōtos|grc:prōtótypon>fr:prototype>tr:prototip
protoplazma|n|fr|protoplasme|ilk biçimlenen|CUM|prōtos|grc:prôtos+plásma>de:Protoplasma>fr:protoplasme>tr:protoplazma
neon|n|fr|néon|yeni gaz|CUM|neos|grc:néon>en:neon>fr:néon>tr:neon
neolitik|adj|fr|néolithique|yeni taş|MOD|neos|grc:néos+líthos>fr:néolithique>tr:neolitik
nükleer|adj|fr|nucléaire|çekirdeğe ilişkin|MOD|nucleus|la:nucleus>fr:nucléaire>tr:nükleer
nükleus|n|fr|nucléus|çekirdek|MOD|nucleus|la:nucleus>fr:nucléus>tr:nükleus
nükleotit|n|fr|nucléotide|çekirdek asidi birimi|NEW|nucleus|la:nucleus>fr:nucléotide>tr:nükleotit
litografi|n|fr|lithographie|taş baskı|OSM19|lithos|grc:líthos+gráphein>fr:lithographie>tr:litografi
monolit|n|fr|monolithe|tek taş|MOD|lithos|grc:monólithos>fr:monolithe>tr:monolit
paleolitik|adj|fr|paléolithique|eski taş|MOD|lithos|grc:palaiós+líthos>fr:paléolithique>tr:paleolitik
aerodinamik|adj|fr|aérodynamique|hava devinimine ilişkin|MOD|aēr|grc:aḗr+dýnamis>fr:aérodynamique>tr:aerodinamik
aerosol|n|fr|aérosol|havada asılı|MOD|aēr|grc:aḗr+la:solutio>fr:aérosol>tr:aerosol
aerobik|adj|fr|aérobie|hava ile yaşayan|MOD|aēr|grc:aḗr+bíos>fr:aérobie>tr:aerobik
anaerobik|adj|fr|anaérobie|havasız yaşayan|MOD|aēr|grc:an+aḗr+bíos>fr:anaérobie>tr:anaerobik
iyonik|adj|fr|ionique|iyona ilişkin|MOD|ienai|grc:ión>fr:ionique>tr:iyonik
katyon|n|fr|cation|aşağı giden|MOD|ienai|grc:katá+ión>en:cation>fr:cation>tr:katyon
anyon|n|fr|anion|yukarı giden|MOD|ienai|grc:aná+ión>en:anion>fr:anion>tr:anyon
iyonlaşma|n|fr|ion|iyon durumuna geçme|MOD|ienai|
glikoz|n|fr|glucose|tatlı şeker|CUM|glykys|grc:glykýs>fr:glucose>tr:glikoz
glikojen|n|fr|glycogène|şeker doğuran|MOD|glykys|grc:glykýs+gennân>fr:glycogène>tr:glikojen
gliserin|n|fr|glycérine|tatlı yağ|OSM19|glykys|grc:glykerós>fr:glycérine>tr:gliserin
glisemi|n|fr|glycémie|kan şekeri|MOD|glykys|grc:glykýs+haîma>fr:glycémie>tr:glisemi
metal|n|fr|métal|maden|CUM|metallon|grc:métallon>la:metallum>fr:métal>tr:metal
metalurji|n|fr|métallurgie|maden işleme|CUM|metallon|grc:metallourgós>fr:métallurgie>tr:metalurji
metalik|adj|fr|métallique|madensel|CUM|metallon|grc:metallikós>fr:métallique>tr:metalik
mikron|n|fr|micron|küçük birim|CUM|mikros|grc:mikrón>fr:micron>tr:mikron
mikrodalga|n|en|microwave|küçük dalga|MOD|mikros|grc:mikrós+en:wave>en:microwave>tr:mikrodalga
mikroçip|n|en|microchip|küçük yonga|NEW|mikros|grc:mikrós+en:chip>en:microchip>tr:mikroçip
mikro|adj|fr|micro|küçük|MOD|mikros|grc:mikrós>fr:micro>tr:mikro
mikroskobik|adj|fr|microscopique|mikroskopla görülen|CUM|mikros|grc:mikrós+skopeîn>fr:microscopique>tr:mikroskobik
mikroorganizma|n|fr|micro-organisme|küçük canlı|MOD|mikros|grc:mikrós+órganon>fr:micro-organisme>tr:mikroorganizma
makro|adj|fr|macro|büyük|MOD|makros|grc:makrós>fr:macro>tr:makro
makroekonomi|n|fr|macroéconomie|büyük ölçekli ekonomi|MOD|makros|grc:makrós+oikonomía>fr:macroéconomie>tr:makroekonomi
makromolekül|n|fr|macromolécule|büyük molekül|MOD|makros|grc:makrós+la:molecula>fr:macromolécule>tr:makromolekül
polimer|n|fr|polymère|çok paylı|MOD|polys|grc:polymerḗs>fr:polymère>tr:polimer
poligon|n|fr|polygone|çok köşeli|CUM|polys|grc:polýgōnon>fr:polygone>tr:poligon
polinom|n|fr|polynôme|çok terimli|MOD|polys|grc:polýs+nómos>fr:polynôme>tr:polinom
politeknik|n|fr|polytechnique|çok sanatlı|OSM19|polys|grc:polýs+tékhnē>fr:polytechnique>tr:politeknik
polietilen|n|fr|polyéthylène|çok etilenli|MOD|polys|grc:polýs+fr:éthylène>fr:polyéthylène>tr:polietilen
monoton|adj|fr|monotone|tek sesli|CUM|monos|grc:monótonos>fr:monotone>tr:monoton
monopol|n|fr|monopole|tek satıcılık|CUM|monos|grc:monopṓlion>fr:monopole>tr:monopol
monokl|n|fr|monocle|tek gözlük|CUM|monos|grc:mónos+la:oculus>fr:monocle>tr:monokl
monografi|n|fr|monographie|tek konulu yazı|CUM|monos|grc:mónos+gráphein>fr:monographie>tr:monografi
monomer|n|fr|monomère|tek paylı|MOD|monos|grc:mónos+méros>fr:monomère>tr:monomer
otomatik|adj|fr|automatique|kendiliğinden işleyen|CUM|autos|grc:autómatos>fr:automatique>tr:otomatik
otonom|adj|fr|autonome|kendi yasalı|MOD|autos|grc:autónomos>fr:autonome>tr:otonom
otonomi|n|fr|autonomie|özerklik|CUM|autos|grc:autonomía>fr:autonomie>tr:otonomi
otomasyon|n|fr|automation|kendiliğinden işleme|MOD|autos|grc:autómatos>en:automation>fr:automation>tr:otomasyon
otopsi|n|fr|autopsie|kendi gözüyle görme|CUM|autos|grc:autopsía>fr:autopsie>tr:otopsi
otomat|n|fr|automate|kendiliğinden işleyen aygıt|CUM|autos|grc:autómaton>fr:automate>tr:otomat
dinamik|adj|fr|dynamique|güce ilişkin|CUM|dynamis|grc:dynamikós>fr:dynamique>tr:dinamik
dinamo|n|fr|dynamo|güç üreteci|OSM19|dynamis|grc:dýnamis>en:dynamo>fr:dynamo>tr:dinamo
dinamit|n|fr|dynamite|güçlü patlayıcı|OSM19|dynamis|grc:dýnamis>en:dynamite>fr:dynamite>tr:dinamit
dinamizm|n|fr|dynamisme|devingenlik|CUM|dynamis|grc:dýnamis>fr:dynamisme>tr:dinamizm
termodinamik|n|fr|thermodynamique|ısı devinimi bilimi|MOD|dynamis|grc:thermós+dýnamis>fr:thermodynamique>tr:termodinamik
statik|adj|fr|statique|duran|CUM|stasis|grc:statikós>fr:statique>tr:statik
termostat|n|fr|thermostat|ısı sabitleyici|MOD|stasis|grc:thermós+statós>fr:thermostat>tr:termostat
hidrostatik|adj|fr|hydrostatique|durgun suya ilişkin|MOD|stasis|grc:hýdōr+statikós>fr:hydrostatique>tr:hidrostatik
elektrostatik|adj|fr|électrostatique|durgun elektriğe ilişkin|MOD|stasis|grc:ḗlektron+statikós>fr:électrostatique>tr:elektrostatik
taksonomi|n|fr|taxonomie|düzenleme yasası|MOD|taxis|grc:táxis+nómos>fr:taxonomie>tr:taksonomi
sentaks|n|fr|syntaxe|birlikte dizme|MOD|taxis|grc:sýntaxis>fr:syntaxe>tr:sentaks
taktik|n|fr|tactique|düzenleme sanatı|CUM|taxis|grc:taktikḗ>fr:tactique>tr:taktik
taksimetre|n|fr|taximètre|ücret ölçer|CUM|tangere|la:taxāre>fr:taxe>fr:taximètre>tr:taksimetre
agronomi|n|fr|agronomie|tarla yasası|CUM|nomos|grc:agrós+nómos>fr:agronomie>tr:agronomi
metronom|n|fr|métronome|ölçü düzenleyici|CUM|nomos|grc:métron+nómos>fr:métronome>tr:metronom
sfer|n|fr|sphère|küre|MOD|sphaira|grc:sphaîra>la:sphaera>fr:sphère>tr:sfer
hemisfer|n|fr|hémisphère|yarım küre|MOD|sphaira|grc:hēmisphaírion>fr:hémisphère>tr:hemisfer
sferik|adj|fr|sphérique|küresel|MOD|sphaira|grc:sphairikós>fr:sphérique>tr:sferik
morfoloji|n|fr|morphologie|biçim bilgisi|CUM|morphē|grc:morphḗ+lógos>fr:morphologie>tr:morfoloji
amorf|adj|fr|amorphe|biçimsiz|MOD|morphē|grc:ámorphos>fr:amorphe>tr:amorf
metamorfoz|n|fr|métamorphose|biçim değiştirme|CUM|morphē|grc:metamórphōsis>fr:métamorphose>tr:metamorfoz
morfem|n|fr|morphème|biçim birimi|MOD|morphē|grc:morphḗ>fr:morphème>tr:morfem
polimorf|adj|fr|polymorphe|çok biçimli|MOD|morphē|grc:polýmorphos>fr:polymorphe>tr:polimorf
gnostik|adj|fr|gnostique|bilgiye ilişkin|MOD|gnōsis|grc:gnōstikós>fr:gnostique>tr:gnostik
agnostik|adj|fr|agnostique|bilinemezci|MOD|gnōsis|grc:ágnōstos>en:agnostic>fr:agnostique>tr:agnostik
prognoz|n|fr|prognose|önceden bilme|MOD|gnōsis|grc:prógnōsis>fr:prognose>tr:prognoz
diyagnostik|adj|fr|diagnostique|tanıya ilişkin|MOD|gnōsis|grc:diagnōstikós>fr:diagnostique>tr:diyagnostik
organik|adj|fr|organique|organa ilişkin|CUM|organon|grc:organikós>fr:organique>tr:organik
organize|adj|fr|organisé|düzenlenmiş|CUM|organon|grc:órganon>fr:organisé>tr:organize
organizasyon|n|fr|organisation|örgütleme|CUM|organon|grc:órganon>fr:organisation>tr:organizasyon
organel|n|fr|organelle|küçük organ|MOD|organon|grc:órganon>fr:organelle>tr:organel
baryum|n|fr|baryum|ağır element|CUM|baros|grc:barýs>en:barium>fr:baryum>tr:baryum
barometrik|adj|fr|barométrique|basınç ölçümüne ilişkin|MOD|baros|grc:báros+métron>fr:barométrique>tr:barometrik
kilogram|n|fr|kilogramme|bin gram|OSM19|khilioi|grc:khílioi+grámma>fr:kilogramme>tr:kilogram
kilovat|n|fr|kilowatt|bin vat|CUM|khilioi|grc:khílioi+en:watt>fr:kilowatt>tr:kilovat
kilobayt|n|en|kilobyte|bin bayt|MOD|khilioi|grc:khílioi+en:byte>en:kilobyte>tr:kilobayt
kilohertz|n|fr|kilohertz|bin hertz|MOD|khilioi|grc:khílioi+de:Hertz>fr:kilohertz>tr:kilohertz
megabayt|n|en|megabyte|milyon bayt|MOD|megas|grc:mégas+en:byte>en:megabyte>tr:megabayt
megapiksel|n|en|megapixel|milyon piksel|NEW|megas|grc:mégas+en:pixel>en:megapixel>tr:megapiksel
megahertz|n|fr|mégahertz|milyon hertz|MOD|megas|grc:mégas+de:Hertz>fr:mégahertz>tr:megahertz
megaloman|adj|fr|mégalomane|büyüklük delisi|CUM|megas|grc:megálos+manía>fr:mégalomane>tr:megaloman
nanoteknoloji|n|en|nanotechnology|cüce ölçek tekniği|NEW|nanos|grc:nânos+tékhnē>en:nanotechnology>tr:nanoteknoloji
nanometre|n|fr|nanomètre|milyarda bir metre|NEW|nanos|grc:nânos+métron>fr:nanomètre>tr:nanometre
gram|n|fr|gramme|küçük ağırlık|OSM19|gramma|grc:grámma>la:gramma>fr:gramme>tr:gram
miligram|n|fr|milligramme|binde bir gram|CUM|gramma|la:mille+grc:grámma>fr:milligramme>tr:miligram
diyagram|n|fr|diagramme|çizgi şekil|CUM|gramma|grc:diágramma>fr:diagramme>tr:diyagram
hologram|n|fr|hologramme|tam yazım|MOD|gramma|grc:hólos+grámma>en:hologram>fr:hologramme>tr:hologram
programlama|n|fr|programme|izlence yazma|MOD|gramma|
litre|n|fr|litre|sıvı ölçüsü|OSM19|litra|grc:lítra>fr:litre>tr:litre
mililitre|n|fr|millilitre|binde bir litre|CUM|litra|la:mille+grc:lítra>fr:millilitre>tr:mililitre
hektolitre|n|fr|hectolitre|yüz litre|CUM||grc:hekatón+lítra>fr:hectolitre>tr:hektolitre
galaktik|adj|fr|galactique|gökadaya ilişkin|MOD|gala|grc:galaktikós>fr:galactique>tr:galaktik
galaktoz|n|fr|galactose|süt şekeri|MOD|gala|grc:gála>fr:galactose>tr:galaktoz
elips|n|fr|ellipse|eksiklik|CUM|elleipsis|grc:élleipsis>la:ellipsis>fr:ellipse>tr:elips
eliptik|adj|fr|elliptique|elips biçimli|MOD|elleipsis|grc:elleiptikós>fr:elliptique>tr:eliptik
elipsoit|n|fr|ellipsoïde|elips görünümlü|MOD|elleipsis|grc:élleipsis+eîdos>fr:ellipsoïde>tr:elipsoit
torna|n|it|tornio|döndürme tezgâhı|OSM|tornos|grc:tórnos>la:tornus>it:tornio>tr:torna
turne|n|fr|tournée|dönüş gezisi|CUM|tornos|grc:tórnos>la:tornare>fr:tournée>tr:turne
tur|n|fr|tour|dönüş, dolaşma|CUM|tornos|grc:tórnos>la:tornus>fr:tour>tr:tur
turizm|n|fr|tourisme|gezginlik|CUM|tornos|grc:tórnos>fr:tourisme>tr:turizm
turist|n|fr|touriste|gezgin|CUM|tornos|grc:tórnos>fr:touriste>tr:turist
turnike|n|fr|tourniquet|döner geçit|CUM|tornos|grc:tórnos>fr:tourniquet>tr:turnike
turnuva|n|fr|tournoi|dönüşlü yarışma|CUM|tornos|grc:tórnos>fr:tournoi>tr:turnuva
kontur|n|fr|contour|çevre çizgisi|MOD|tornos|grc:tórnos>it:contorno>fr:contour>tr:kontur
siber|adj|en|cyber|dümenciye ilişkin|NEW|kybernan|grc:kybernḗtēs>en:cyber>tr:siber
sibernetik|n|fr|cybernétique|dümencilik bilimi|MOD|kybernan|grc:kybernētikḗ>en:cybernetics>fr:cybernétique>tr:sibernetik
ikon|n|fr|icône|tasvir|MOD|eikōn|grc:eikṓn>fr:icône>tr:ikon
ikonik|adj|en|iconic|simgesel|NEW|eikōn|grc:eikṓn>en:iconic>tr:ikonik
beril|n|fr|béryl|yeşil taş|MOD|bēryllos|grc:bḗryllos>la:beryllus>fr:béryl>tr:beril
berilyum|n|fr|béryllium|beril elementi|MOD|bēryllos|grc:bḗryllos>fr:béryllium>tr:berilyum
brilyant|n|fr|brillant|parlayan|CUM|bēryllos|grc:bḗryllos>it:brillare>fr:brillant>tr:brilyant
ksenon|n|fr|xénon|yabancı gaz|MOD|xenos|grc:xénon>en:xenon>fr:xénon>tr:ksenon
ksenofobi|n|fr|xénophobie|yabancı korkusu|MOD|xenos|grc:xénos+phóbos>fr:xénophobie>tr:ksenofobi
neft|n|fa|neft|yer yağı|EAT|naphtha|fa:naft>tr:neft
naftalin|n|fr|naphtaline|neft maddesi|OSM19|naphtha|fa:naft>grc:náphtha>fr:naphtaline>tr:naftalin
nafta|n|fr|naphte|yer yağı özü|MOD|naphtha|fa:naft>grc:náphtha>la:naphtha>fr:naphte>tr:nafta
kristalize|adj|fr|cristallisé|billurlaşmış|CUM|krystallos|grc:krýstallos>fr:cristallisé>tr:kristalize
kristalografi|n|fr|cristallographie|billur yazımı|MOD|krystallos|grc:krýstallos+gráphein>fr:cristallographie>tr:kristalografi
elastik|adj|fr|élastique|esnek|CUM|elastikos|grc:elastikós>fr:élastique>tr:elastik
elastikiyet|n|fr|élasticité|esneklik|CUM|elastikos|grc:elastikós>fr:élasticité>tr:elastikiyet
elastomer|n|fr|élastomère|esnek paylı|NEW|elastikos|grc:elastikós+méros>fr:élastomère>tr:elastomer
baz|n|fr|base|temel|CUM|basis|grc:básis>la:basis>fr:base>tr:baz
bazik|adj|fr|basique|baz özellikli|MOD|basis|grc:básis>fr:basique>tr:bazik
bazal|adj|fr|basal|temele ilişkin|MOD|basis|grc:básis>fr:basal>tr:bazal
şema|n|fr|schéma|görünüş, biçim|CUM|skhēma|grc:skhêma>la:schema>fr:schéma>tr:şema
şematik|adj|fr|schématique|şema biçiminde|MOD|skhēma|grc:skhêma>fr:schématique>tr:şematik
grafit|n|fr|graphite|yazı taşı|CUM|graphein|grc:gráphein>de:Graphit>fr:graphite>tr:grafit
kaligrafi|n|fr|calligraphie|güzel yazı|MOD|graphein|grc:kalligraphía>fr:calligraphie>tr:kaligrafi
metrik|adj|fr|métrique|ölçüye ilişkin|CUM|metron|grc:metrikós>fr:métrique>tr:metrik
metraj|n|fr|métrage|metre ölçüsü|CUM|metron|grc:métron>fr:métrage>tr:metraj
asimetri|n|fr|asymétrie|ölçüsüzlük|MOD|metron|grc:asymmetría>fr:asymétrie>tr:asimetri
trigonometri|n|fr|trigonométrie|üçgen ölçümü|OSM19|metron|grc:trígōnon+métron>fr:trigonométrie>tr:trigonometri
perimetre|n|fr|périmètre|çevre ölçüsü|MOD|metron|grc:perímetros>fr:périmètre>tr:perimetre
manometre|n|fr|manomètre|seyrek ölçer|CUM|metron|grc:manós+métron>fr:manomètre>tr:manometre
kaleydoskop|n|fr|kaléidoscope|güzel biçim görücü|CUM|skopein|grc:kalós+eîdos+skopeîn>en:kaleidoscope>fr:kaléidoscope>tr:kaleydoskop
endoskop|n|fr|endoscope|içe bakan|MOD|skopein|grc:éndon+skopeîn>fr:endoscope>tr:endoskop
spektroskop|n|fr|spectroscope|tayf görücü|MOD|skopein|la:spectrum+grc:skopeîn>fr:spectroscope>tr:spektroskop
horoskop|n|fr|horoscope|saat gözlemi|MOD|skopein|grc:hōroskópos>fr:horoscope>tr:horoskop
teleskopik|adj|fr|télescopique|iç içe geçen|MOD|skopein|grc:têle+skopeîn>fr:télescopique>tr:teleskopik
kinematik|n|fr|cinématique|devinim bilgisi|MOD|kinein|grc:kínēma>fr:cinématique>tr:kinematik
sinematograf|n|fr|cinématographe|devinim yazıcı|OSM19|kinein|grc:kínēma+gráphein>fr:cinématographe>tr:sinematograf
telekinezi|n|fr|télékinésie|uzaktan devindirme|MOD|kinein|grc:têle+kínēsis>fr:télékinésie>tr:telekinezi
motosiklet|n|fr|motocyclette|motorlu tekerlek|CUM|kyklos|la:motor+grc:kýklos>fr:motocyclette>tr:motosiklet
siklotron|n|fr|cyclotron|dairesel hızlandırıcı|MOD|kyklos|grc:kýklos>en:cyclotron>fr:cyclotron>tr:siklotron
sirküler|n|fr|circulaire|dolaşan yazı|CUM|kyklos|la:circulus>fr:circulaire>tr:sirküler
termosifon|n|fr|thermosiphon|ısı borusu|CUM|thermos|grc:thermós+síphōn>fr:thermosiphon>tr:termosifon
termoplastik|adj|fr|thermoplastique|ısıyla biçimlenen|NEW|thermos|grc:thermós+plastikós>fr:thermoplastique>tr:termoplastik
fotokopi|n|fr|photocopie|ışıkla kopya|MOD|phōs|grc:phôs+la:copia>fr:photocopie>tr:fotokopi
fotosel|n|fr|photocellule|ışık gözesi|MOD|phōs|grc:phôs+la:cellula>fr:photocellule>tr:fotosel
fotojenik|adj|fr|photogénique|ışık doğuran|MOD|phōs|grc:phôs+gennân>fr:photogénique>tr:fotojenik
teknolojik|adj|fr|technologique|teknolojiye ilişkin|MOD|tekhne|grc:tekhnología>fr:technologique>tr:teknolojik
tekno|adj|en|techno|teknolojik|NEW|tekhne|grc:tékhnē>en:techno>tr:tekno
mekanize|adj|fr|mécanisé|makineleştirilmiş|CUM|mekhane|grc:mēkhanḗ>fr:mécanisé>tr:mekanize
makinist|n|fr|machiniste|makine işleten|OSM19|mekhane|grc:mēkhanḗ>fr:machiniste>tr:makinist
periyodik|adj|fr|périodique|dönemsel|CUM|hodos|grc:periodikós>fr:périodique>tr:periyodik
metodoloji|n|fr|méthodologie|yöntem bilgisi|MOD|hodos|grc:méthodos+lógos>fr:méthodologie>tr:metodoloji
diyot|n|fr|diode|iki yollu|MOD|hodos|grc:dís+hodós>en:diode>fr:diode>tr:diyot
sinerji|n|fr|synergie|birlikte çalışma|NEW|ergon|grc:synergía>fr:synergie>tr:sinerji
erg|n|fr|erg|iş birimi|CUM|ergon|grc:érgon>fr:erg>tr:erg
fonograf|n|fr|phonographe|ses yazıcı|OSM19|phone|grc:phōnḗ+gráphein>fr:phonographe>tr:fonograf
fonem|n|fr|phonème|ses birimi|MOD|phone|grc:phṓnēma>fr:phonème>tr:fonem
fonoloji|n|fr|phonologie|ses bilgisi|MOD|phone|grc:phōnḗ+lógos>fr:phonologie>tr:fonoloji
hidrat|n|fr|hydrate|sulu bileşik|MOD|hydōr|grc:hýdōr>fr:hydrate>tr:hidrat
hidrofil|adj|fr|hydrophile|su seven|MOD|hydōr|grc:hýdōr+phílos>fr:hydrophile>tr:hidrofil
dehidrasyon|n|fr|déshydratation|su yitimi|MOD|hydōr|grc:hýdōr>fr:déshydratation>tr:dehidrasyon
klorür|n|fr|chlorure|klor bileşiği|CUM|khlōros|grc:khlōrós>fr:chlorure>tr:klorür
biyolojik|adj|fr|biologique|yaşam bilimine ilişkin|CUM|bios|grc:bíos+lógos>fr:biologique>tr:biyolojik
simbiyoz|n|fr|symbiose|birlikte yaşama|MOD|bios|grc:symbíōsis>fr:symbiose>tr:simbiyoz
biyoteknoloji|n|fr|biotechnologie|yaşam tekniği|NEW|bios|grc:bíos+tékhnē>fr:biotechnologie>tr:biyoteknoloji
atomik|adj|fr|atomique|atoma ilişkin|CUM|tomē|grc:átomos>fr:atomique>tr:atomik
parabol|n|fr|parabole|yanına atılan|CUM|parabola|grc:parabolḗ>la:parabola>fr:parabole>tr:parabol
parabolik|adj|fr|parabolique|parabol biçimli|MOD|parabola|grc:parabolḗ>fr:parabolique>tr:parabolik
# --- Latince kökler (Fransızca yoluyla) -----------------------------------------------------
numerik|adj|fr|numérique|sayısal|MOD|numerus|la:numerus>fr:numérique>tr:numerik
numaralamak|v|it|numero|sayı vermek|CUM|numerus|la:numerus>it:numero>tr:numaralamak
numaratör|n|fr|numéroteur|sayı basan|CUM|numerus|la:numerus>fr:numéroteur>tr:numaratör
kalker|n|fr|calcaire|kireç taşı|CUM|calx|la:calcarius>fr:calcaire>tr:kalker
kalsit|n|fr|calcite|kireç minerali|MOD|calx|la:calx>fr:calcite>tr:kalsit
vektör|n|fr|vecteur|taşıyan|MOD|vehere|la:vector>fr:vecteur>tr:vektör
vektörel|adj|fr|vectoriel|vektöre ilişkin|MOD|vehere|la:vector>fr:vectoriel>tr:vektörel
kapasite|n|fr|capacité|alma gücü|CUM|capere|la:capacitas>fr:capacité>tr:kapasite
kapasitör|n|fr|capaciteur|yük tutan|MOD|capere|la:capacitas>en:capacitor>fr:capaciteur>tr:kapasitör
konsept|n|fr|concept|kavranan|MOD|capere|la:conceptus>fr:concept>tr:konsept
persepsiyon|n|fr|perception|algılama|MOD|capere|la:perceptio>fr:perception>tr:persepsiyon
prensip|n|fr|principe|ilk tutulan, ilke|OSM19|capere|la:principium>fr:principe>tr:prensip
resepsiyon|n|fr|réception|kabul|CUM|capere|la:receptio>fr:réception>tr:resepsiyon
enstrüman|n|fr|instrument|araç|CUM|struere|la:instrumentum>fr:instrument>tr:enstrüman
konstrüksiyon|n|fr|construction|yapım|CUM|struere|la:constructio>fr:construction>tr:konstrüksiyon
endüstri|n|fr|industrie|çalışkanlık; sanayi|OSM19|struere|la:industria>fr:industrie>tr:endüstri
endüstriyel|adj|fr|industriel|sanayiye ilişkin|CUM|struere|la:industria>fr:industriel>tr:endüstriyel
enstrümantal|adj|fr|instrumental|çalgıya ilişkin|MOD|struere|la:instrumentum>fr:instrumental>tr:enstrümantal
osiloskop|n|fr|oscilloscope|salınım görücü|MOD|oscillare|la:oscillare+grc:skopeîn>fr:oscilloscope>tr:osiloskop
osilasyon|n|fr|oscillation|salınım|MOD|oscillare|la:oscillatio>fr:oscillation>tr:osilasyon
osilatör|n|fr|oscillateur|salınım üreteci|MOD|oscillare|la:oscillare>fr:oscillateur>tr:osilatör
fraksiyon|n|fr|fraction|kırılmış parça|CUM|frangere|la:fractio>fr:fraction>tr:fraksiyon
fraktal|n|fr|fractale|kırıklı biçim|NEW|frangere|la:fractus>fr:fractale>tr:fraktal
fragman|n|fr|fragment|parça|MOD|frangere|la:fragmentum>fr:fragment>tr:fragman
refraksiyon|n|fr|réfraction|kırılma|MOD|frangere|la:refractio>fr:réfraction>tr:refraksiyon
solüsyon|n|fr|solution|çözelti|CUM|solvere|la:solutio>fr:solution>tr:solüsyon
solvent|n|fr|solvant|çözücü|MOD|solvere|la:solvens>fr:solvant>tr:solvent
tanjant|n|fr|tangente|dokunan|CUM|tangere|la:tangens>fr:tangente>tr:tanjant
kontak|n|fr|contact|dokunma|CUM|tangere|la:contactus>fr:contact>tr:kontak
entegre|adj|fr|intégré|bütünleşmiş|MOD|tangere|la:integer>fr:intégré>tr:entegre
entegrasyon|n|fr|intégration|bütünleşme|MOD|tangere|la:integratio>fr:intégration>tr:entegrasyon
integral|n|fr|intégrale|bütünleyen|MOD|tangere|la:integer>fr:intégrale>tr:integral
sinyal|n|fr|signal|işaret|CUM|signum|la:signale>fr:signal>tr:sinyal
sinyalizasyon|n|fr|signalisation|işaretleme|MOD|signum|la:signum>fr:signalisation>tr:sinyalizasyon
dizayn|n|en|design|tasarım|MOD|signum|la:designare>it:disegno>en:design>tr:dizayn
desen|n|fr|dessin|çizim|CUM|signum|la:designare>fr:dessin>tr:desen
koordinasyon|n|fr|coordination|eşgüdüm|MOD|ordo|la:coordinatio>fr:coordination>tr:koordinasyon
koordine|adj|fr|coordonné|eşgüdümlü|MOD|ordo|la:ordinare>fr:coordonné>tr:koordine
ordinat|n|fr|ordonnée|düzenlenmiş|CUM|ordo|la:ordinata>fr:ordonnée>tr:ordinat
fonksiyon|n|fr|fonction|işleyiş|CUM|fungi|la:functio>fr:fonction>tr:fonksiyon
fonksiyonel|adj|fr|fonctionnel|işlevsel|MOD|fungi|la:functio>fr:fonctionnel>tr:fonksiyonel
vibrasyon|n|fr|vibration|titreşim|CUM|vibrare|la:vibratio>fr:vibration>tr:vibrasyon
vibratör|n|fr|vibrateur|titreştirici|MOD|vibrare|la:vibrare>fr:vibrateur>tr:vibratör
solar|adj|en|solar|güneşe ilişkin|NEW|sol|la:solaris>en:solar>tr:solar
solaryum|n|fr|solarium|güneşlenme yeri|MOD|sol|la:solarium>fr:solarium>tr:solaryum
akümülatör|n|fr|accumulateur|yığıcı|CUM|cumulus|la:accumulare>fr:accumulateur>tr:akümülatör
kümülatif|adj|fr|cumulatif|birikimli|MOD|cumulus|la:cumulare>fr:cumulatif>tr:kümülatif
pres|n|fr|presse|sıkma aygıtı|CUM|premere|la:pressare>fr:presse>tr:pres
kompresör|n|fr|compresseur|sıkıştırıcı|CUM|premere|la:compressus>fr:compresseur>tr:kompresör
kompres|n|fr|compresse|sıkıştırılmış bez|CUM|premere|la:compressus>fr:compresse>tr:kompres
ekspres|n|fr|express|sıkıştırılmış, hızlı|OSM19|premere|la:expressus>fr:express>tr:ekspres
depresyon|n|fr|dépression|bastırılma, çökme|CUM|premere|la:depressio>fr:dépression>tr:depresyon
vantilatör|n|fr|ventilateur|yelleyici|CUM|ventus|la:ventilare>fr:ventilateur>tr:vantilatör
ventilasyon|n|fr|ventilation|havalandırma|MOD|ventus|la:ventilatio>fr:ventilation>tr:ventilasyon
füzyon|n|fr|fusion|eritme, kaynaşma|MOD|fundere|la:fusio>fr:fusion>tr:füzyon
difüzyon|n|fr|diffusion|yayılma|MOD|fundere|la:diffusio>fr:diffusion>tr:difüzyon
sülfür|n|fr|sulfure|kükürt bileşiği|CUM|sulphur|la:sulphur>fr:sulfure>tr:sülfür
sülfat|n|fr|sulfate|sülfürik asit tuzu|CUM|sulphur|la:sulphur>fr:sulfate>tr:sülfat
sülfürik|adj|fr|sulfurique|kükürte ilişkin|CUM|sulphur|la:sulphur>fr:sulfurique>tr:sülfürik
karbonat|n|fr|carbonate|karbonik asit tuzu|OSM19|carbo|la:carbo>fr:carbonate>tr:karbonat
karbüratör|n|fr|carburateur|yakıt karıştırıcı|CUM|carbo|la:carbo>fr:carburateur>tr:karbüratör
karbonhidrat|n|fr|carbohydrate|karbon ve su bileşiği|MOD|carbo|la:carbo+grc:hýdōr>fr:carbohydrate>tr:karbonhidrat
karbonik|adj|fr|carbonique|karbona ilişkin|CUM|carbo|la:carbo>fr:carbonique>tr:karbonik
nitrik|adj|fr|nitrique|azota ilişkin|CUM|nitron|grc:nítron>fr:nitrique>tr:nitrik
nitrojen|n|fr|nitrogène|güherçile doğuran|CUM|nitron|grc:nítron+gennân>fr:nitrogène>tr:nitrojen
nitrogliserin|n|fr|nitroglycérine|nitratlı gliserin|CUM|nitron|grc:nítron+glykerós>fr:nitroglycérine>tr:nitrogliserin
alkol|n|fr|alcool|ince toz; damıtık öz|OSM19|K-H-L|ar:al-kuḥl>la:alcohol>fr:alcool>tr:alkol
alkolik|adj|fr|alcoolique|içkiye düşkün|CUM|K-H-L|ar:al-kuḥl>fr:alcoolique>tr:alkolik
alkolizm|n|fr|alcoolisme|içki bağımlılığı|CUM|K-H-L|ar:al-kuḥl>fr:alcoolisme>tr:alkolizm
alkali|n|fr|alcali|bitki külü|CUM|K-L-Y|ar:al-qily>la:alkali>fr:alcali>tr:alkali
alkalin|adj|fr|alcalin|alkali özellikli|MOD|K-L-Y|ar:al-qily>fr:alcalin>tr:alkalin
asit|n|fr|acide|ekşi|CUM|acere|la:acidus>fr:acide>tr:asit
asidik|adj|fr|acidique|asit özellikli|MOD|acere|la:acidus>fr:acidique>tr:asidik
aseton|n|fr|acétone|sirke özü|CUM|acere|la:acetum>fr:acétone>tr:aseton
asetat|n|fr|acétate|asetik asit tuzu|CUM|acere|la:acetum>fr:acétate>tr:asetat
asetik|adj|fr|acétique|sirkeye ilişkin|CUM|acere|la:acetum>fr:acétique>tr:asetik
silis|n|fr|silice|çakmak taşı özü|CUM|silex|la:silex>fr:silice>tr:silis
silisyum|n|fr|silicium|çakmak taşı elementi|CUM|silex|la:silex>fr:silicium>tr:silisyum
silikon|n|en|silicone|silisyum bileşiği|MOD|silex|la:silex>en:silicone>tr:silikon
silikat|n|fr|silicate|silisik asit tuzu|MOD|silex|la:silex>fr:silicate>tr:silikat
granül|n|fr|granule|tanecik|MOD|granum|la:granulum>fr:granule>tr:granül
granüle|adj|fr|granulé|tanecikli|MOD|granum|la:granulum>fr:granulé>tr:granüle
benzen|n|fr|benzène|benzoe özü|CUM|benzoe|ar:lubān cāwī>la:benzoe>fr:benzène>tr:benzen
benzol|n|de|Benzol|benzoe yağı|CUM|benzoe|ar:lubān cāwī>la:benzoe>de:Benzol>tr:benzol
kuantum|n|fr|quantum|ne kadarlık|MOD|quantus|la:quantum>de:Quantum>fr:quantum>tr:kuantum
kantite|n|fr|quantité|nicelik|CUM|quantus|la:quantitas>fr:quantité>tr:kantite
kantitatif|adj|fr|quantitatif|niceliksel|MOD|quantus|la:quantitas>fr:quantitatif>tr:kantitatif
nötr|adj|fr|neutre|ne o ne bu|CUM|neuter|la:neuter>fr:neutre>tr:nötr
nötron|n|fr|neutron|yüksüz parçacık|MOD|neuter|la:neuter>en:neutron>fr:neutron>tr:nötron
nötrino|n|it|neutrino|küçük yüksüz|MOD|neuter|la:neuter>it:neutrino>tr:nötrino
nötralize|adj|fr|neutralisé|etkisiz kılınmış|MOD|neuter|la:neutralis>fr:neutralisé>tr:nötralize
mol|n|fr|mole|kütle birimi|MOD|moles|la:moles>de:Mol>fr:mole>tr:mol
moleküler|adj|fr|moléculaire|moleküle ilişkin|MOD|moles|la:molecula>fr:moléculaire>tr:moleküler
molar|adj|fr|molaire|mole ilişkin|MOD|moles|la:moles>fr:molaire>tr:molar
reaktör|n|fr|réacteur|tepkime kabı|MOD|agere|la:reactus>fr:réacteur>tr:reaktör
reaksiyon|n|fr|réaction|tepkime|CUM|agere|la:reactio>fr:réaction>tr:reaksiyon
reaktif|adj|fr|réactif|tepkiyen|MOD|agere|la:reactus>fr:réactif>tr:reaktif
aktif|adj|fr|actif|etkin|CUM|agere|la:activus>fr:actif>tr:aktif
aktivite|n|fr|activité|etkinlik|CUM|agere|la:activitas>fr:activité>tr:aktivite
aksiyon|n|fr|action|eylem|CUM|agere|la:actio>fr:action>tr:aksiyon
türbin|n|fr|turbine|dönen|CUM|turbo|la:turbo>fr:turbine>tr:türbin
türbülans|n|fr|turbulence|çalkantı|MOD|turbo|la:turbulentia>fr:turbulence>tr:türbülans
turbo|n|en|turbo|türbinli|MOD|turbo|la:turbo>en:turbo>tr:turbo
şarj|n|fr|charge|yük|CUM|carrus|la:carricare>fr:charge>tr:şarj
şarjör|n|fr|chargeur|yükleyici|CUM|carrus|la:carricare>fr:chargeur>tr:şarjör
kargo|n|it|carico|yük|CUM|carrus|la:carricare>it:carico>tr:kargo
karoser|n|fr|carrosserie|araba gövdesi|CUM|carrus|la:carrus>fr:carrosserie>tr:karoser
alternatif|adj|fr|alternatif|değişimli|CUM|alter|la:alternare>fr:alternatif>tr:alternatif
alternatör|n|fr|alternateur|değişimli akım üreteci|MOD|alter|la:alternare>fr:alternateur>tr:alternatör
volt|n|fr|volt|Volta birimi|OSM19|Volta|it:Volta>fr:volt>tr:volt
voltaj|n|fr|voltage|gerilim|CUM|Volta|it:Volta>fr:voltage>tr:voltaj
voltmetre|n|fr|voltmètre|gerilim ölçer|CUM|Volta|it:Volta+grc:métron>fr:voltmètre>tr:voltmetre
fotovoltaik|adj|fr|photovoltaïque|ışıkla gerilim üreten|NEW|Volta|grc:phôs+it:Volta>fr:photovoltaïque>tr:fotovoltaik
amper|n|fr|ampère|Ampère birimi|OSM19|Ampère|fr:Ampère>tr:amper
ampermetre|n|fr|ampèremètre|akım ölçer|CUM|Ampère|fr:Ampère+grc:métron>fr:ampèremètre>tr:ampermetre
santim|n|fr|centime|yüzde bir|OSM19|centum|la:centum>fr:centime>tr:santim
santigrat|n|fr|centigrade|yüz dereceli|CUM|centum|la:centum+gradus>fr:centigrade>tr:santigrat
sent|n|en|cent|yüzde bir dolar|MOD|centum|la:centum>en:cent>tr:sent
milimetre|n|fr|millimètre|binde bir metre|OSM19|mille|la:mille+grc:métron>fr:millimètre>tr:milimetre
milenyum|n|en|millennium|bin yıl|NEW|mille|la:millennium>en:millennium>tr:milenyum
desimetre|n|fr|décimètre|onda bir metre|CUM|decem|la:decem+grc:métron>fr:décimètre>tr:desimetre
desibel|n|fr|décibel|onda bir bel|MOD|decem|la:decem+en:Bell>fr:décibel>tr:desibel
desilitre|n|fr|décilitre|onda bir litre|CUM|decem|la:decem+grc:lítra>fr:décilitre>tr:desilitre
desimal|adj|fr|décimal|onluk|CUM|decem|la:decimalis>fr:décimal>tr:desimal
tablet|n|fr|tablette|küçük levha|CUM|tabula|la:tabula>fr:tablette>tr:tablet
tabla|n|it|tavola|levha|OSM|tabula|la:tabula>it:tavola>tr:tabla
sensör|n|en|sensor|algılayıcı|MOD||
sansasyon|n|fr|sensation|duyum; heyecan|CUM|sentire|la:sensatio>fr:sensation>tr:sansasyon
sansasyonel|adj|fr|sensationnel|heyecan verici|MOD|sentire|la:sensatio>fr:sensationnel>tr:sansasyonel
modül|n|fr|module|küçük ölçü|MOD|modus|la:modulus>fr:module>tr:modül
modüler|adj|fr|modulaire|modüllerden oluşan|MOD|modus|la:modulus>fr:modulaire>tr:modüler
modern|adj|fr|moderne|şimdiki|OSM19|modus|la:modernus>fr:moderne>tr:modern
moda|n|it|moda|biçim, tarz|OSM19|modus|la:modus>it:moda>tr:moda
mod|n|fr|mode|biçim, kip|MOD|modus|la:modus>fr:mode>tr:mod
modülasyon|n|fr|modulation|ölçülü değişim|MOD|modus|la:modulatio>fr:modulation>tr:modülasyon
projeksiyon|n|fr|projection|öne atma|CUM|iacere|la:proiectio>fr:projection>tr:projeksiyon
projektör|n|fr|projecteur|ışık atan|CUM|iacere|la:proiectus>fr:projecteur>tr:projektör
objektif|n|fr|objectif|karşıya atılan; nesnel|CUM|iacere|la:obiectivus>fr:objectif>tr:objektif
obje|n|fr|objet|karşıya konan|CUM|iacere|la:obiectum>fr:objet>tr:obje
enjeksiyon|n|fr|injection|içe atma|CUM|iacere|la:iniectio>fr:injection>tr:enjeksiyon
kalitatif|adj|fr|qualitatif|nitel|MOD|qualis|la:qualitas>fr:qualitatif>tr:kalitatif
kalifiye|adj|fr|qualifié|nitelikli|CUM|qualis|la:qualificare>fr:qualifié>tr:kalifiye
norm|n|fr|norme|gönye; kural|MOD|norma|la:norma>fr:norme>tr:norm
normal|adj|fr|normal|kurala uygun|CUM|norma|la:normalis>fr:normal>tr:normal
anormal|adj|fr|anormal|kural dışı|CUM|norma|la:normalis>fr:anormal>tr:anormal
klasman|n|fr|classement|sınıflandırma|CUM|classis|la:classis>fr:classement>tr:klasman
klas|n|fr|classe|sınıf; seçkinlik|MOD|classis|la:classis>fr:classe>tr:klas
versiyon|n|fr|version|çevrilmiş|MOD|vertere|la:versio>fr:version>tr:versiyon
konvertör|n|fr|convertisseur|dönüştürücü|MOD|vertere|la:convertere>fr:convertisseur>tr:konvertör
konvertibl|adj|fr|convertible|dönüştürülebilir|MOD|vertere|la:convertere>fr:convertible>tr:konvertibl
adaptör|n|fr|adaptateur|uyarlayıcı|MOD|aptus|la:adaptare>fr:adaptateur>tr:adaptör
adaptasyon|n|fr|adaptation|uyarlama|CUM|aptus|la:adaptatio>fr:adaptation>tr:adaptasyon
adapte|adj|fr|adapté|uyarlanmış|CUM|aptus|la:adaptare>fr:adapté>tr:adapte
pedal|n|fr|pédale|ayaklık|CUM|pes|la:pes>it:pedale>fr:pédale>tr:pedal
pedikür|n|fr|pédicure|ayak bakımı|MOD|pes|la:pes+cura>fr:pédicure>tr:pedikür
empedans|n|fr|impédance|engelleme|MOD|pes|la:impedire>en:impedance>fr:impédance>tr:empedans
kontrol|n|fr|contrôle|karşı kayıt|OSM19|rotulus|la:contra+rotulus>fr:contrôle>tr:kontrol
rol|n|fr|rôle|tomar; oyun kişiliği|OSM19|rotulus|la:rotulus>fr:rôle>tr:rol
rulo|n|fr|rouleau|tomar|CUM|rotulus|la:rotulus>fr:rouleau>tr:rulo
rulman|n|fr|roulement|yuvarlanma|CUM|rotulus|la:rotulus>fr:roulement>tr:rulman
portal|n|en|portal|büyük kapı; giriş sitesi|NEW||la:porta>en:portal>tr:portal
akvaryum|n|fr|aquarium|su kabı|CUM|aqua|la:aquarium>fr:aquarium>tr:akvaryum
akvadük|n|fr|aqueduc|su yolu|MOD|aqua|la:aquaeductus>fr:aqueduc>tr:akvadük
akuakültür|n|fr|aquaculture|su ürünleri yetiştiriciliği|NEW|aqua|la:aqua+cultura>fr:aquaculture>tr:akuakültür
irrasyonel|adj|fr|irrationnel|akıl dışı; oransız|MOD|ratio|la:irrationalis>fr:irrationnel>tr:irrasyonel
rasyo|n|fr|ratio|oran|MOD|ratio|la:ratio>fr:ratio>tr:rasyo
üniversal|adj|fr|universel|evrensel|CUM|unus|la:universalis>fr:universel>tr:üniversal
üniform|adj|fr|uniforme|tek biçimli|MOD|unus|la:uniformis>fr:uniforme>tr:üniform
üniter|adj|fr|unitaire|birimli, tekil|MOD|unus|la:unitas>fr:unitaire>tr:üniter
moment|n|fr|moment|devindirici etki|CUM|movere|la:momentum>fr:moment>tr:moment
momentum|n|en|momentum|devinim niceliği|MOD|movere|la:momentum>en:momentum>tr:momentum
stabilize|adj|fr|stabilisé|kararlı kılınmış|MOD|stare|la:stabilis>fr:stabilisé>tr:stabilize
stabilizatör|n|fr|stabilisateur|kararlı kılan|MOD|stare|la:stabilis>fr:stabilisateur>tr:stabilizatör
spektral|adj|fr|spectral|tayfa ilişkin|MOD|specere|la:spectrum>fr:spectral>tr:spektral
transformatör|n|fr|transformateur|dönüştürücü|CUM|forma|la:transformare>fr:transformateur>tr:transformatör
trafo|n|de|Trafo|dönüştürücü|MOD|forma|la:transformare>de:Transformator>de:Trafo>tr:trafo
indüksiyon|n|fr|induction|içe götürme|CUM|ducere|la:inductio>fr:induction>tr:indüksiyon
endüksiyon|n|fr|induction|içe götürme|CUM|ducere|la:inductio>fr:induction>tr:endüksiyon
redüktör|n|fr|réducteur|geri götüren|MOD|ducere|la:reducere>fr:réducteur>tr:redüktör
dedüksiyon|n|fr|déduction|aşağı götürme, çıkarım|MOD|ducere|la:deductio>fr:déduction>tr:dedüksiyon
endüktans|n|fr|inductance|indükleme yeteneği|MOD|ducere|la:inducere>en:inductance>fr:inductance>tr:endüktans
kompozit|adj|fr|composite|birlikte konmuş|NEW|ponere|la:compositus>fr:composite>tr:kompozit
pozitron|n|fr|positron|artı yüklü elektron|MOD|ponere|la:positivus>en:positron>fr:positron>tr:pozitron
süperpozisyon|n|fr|superposition|üst üste koyma|MOD|ponere|la:superpositio>fr:superposition>tr:süperpozisyon
transkript|n|fr|transcript|aktarılmış yazı|MOD|scribere|la:transcriptum>fr:transcript>tr:transkript
faktör|n|fr|facteur|yapan; etken|CUM|facere|la:factor>fr:facteur>tr:faktör
faktöriyel|n|fr|factorielle|çarpanlar çarpımı|MOD|facere|la:factor>fr:factorielle>tr:faktöriyel
defekt|n|fr|défaut|eksiklik|MOD|facere|la:defectus>fr:défaut>tr:defekt
diferansiyel|n|fr|différentiel|ayrımsal|MOD|ferre|la:differentia>fr:différentiel>tr:diferansiyel
radyoaktif|adj|fr|radioactif|ışın saçan|CUM|radius|la:radius+activus>fr:radioactif>tr:radyoaktif
radyum|n|fr|radium|ışıyan element|CUM|radius|la:radius>fr:radium>tr:radyum
radyal|adj|fr|radial|ışınsal|MOD|radius|la:radialis>fr:radial>tr:radyal
radyan|n|fr|radian|yarıçap açısı|MOD|radius|la:radius>en:radian>fr:radian>tr:radyan
radyoloji|n|fr|radiologie|ışın bilgisi|CUM|radius|la:radius+grc:lógos>fr:radiologie>tr:radyoloji
# --- Elementler, mineraller ve malzemeler --------------------------------------------------
kauçuk|n|fr|caoutchouc|ağlayan ağaç|OSM19||fr:caoutchouc>tr:kauçuk
polyester|n|en|polyester|çok esterli|MOD||grc:polýs+de:Ester>en:polyester>tr:polyester
teflon|n|en|Teflon|tetrafloroetilen|MOD||
sodyum|n|fr|sodium|soda elementi|CUM||ar:suwwād>la:soda>fr:sodium>tr:sodyum
potasyum|n|fr|potassium|potas elementi|CUM||nl:potasch>fr:potassium>tr:potasyum
potas|n|fr|potasse|kap külü|OSM19||nl:potasch>fr:potasse>tr:potas
borat|n|fr|borate|borik asit tuzu|MOD||fa:būrah>fr:borate>tr:borat
argon|n|fr|argon|tembel gaz|MOD||grc:argón>en:argon>fr:argon>tr:argon
radon|n|fr|radon|radyum gazı|MOD||la:radius>de:Radon>fr:radon>tr:radon
arsenik|n|fr|arsenic|sarı zırnık|OSM19||fa:zarnīḫ>grc:arsenikón>la:arsenicum>fr:arsenic>tr:arsenik
zırnık|n|fa|zarnīḫ|altın renkli maden|EAT||
amonyak|n|fr|ammoniac|Ammon tuzu|OSM19||grc:ammōniakón>la:ammoniacum>fr:ammoniac>tr:amonyak
tunç|n|fa|tunc|bakır-kalay alaşımı|EAT||
helyum|n|fr|hélium|güneş elementi|CUM||grc:hḗlios>en:helium>fr:hélium>tr:helyum
iyodür|n|fr|iodure|iyot bileşiği|MOD||grc:iṓdēs>fr:iodure>tr:iyodür
nişadır|n|fa|nūşādur|amonyum klorür|EAT||
tutya|n|ar|tūtiyā|çinko oksit|EAT||sa:tuttha>ar:tūtiyā>tr:tutya
zaç|n|fa|zāc|sülfat; kara boya|OSM||
kezzap|n|fa|tīzāb|keskin su|OSM||
zift|n|ar|zift|katran|EAT||
alaşım|n|tr|alaş-|karışık maden|DD||
pas|n|fa|pas|demir çürüğü|OSM||
döküm|n|tr|döküm|eritip kalıba dökme|OSM|*dök-|
dökme|n|tr|dökme|dökülerek yapılmış|OSM|*dök-|
# --- Mühendislik, makine ve aygıtlar ---------------------------------------------------------
piston|n|fr|piston|itici|CUM||it:pistone>fr:piston>tr:piston
silindir|n|fr|cylindre|yuvarlanan|CUM||grc:kýlindros>la:cylindrus>fr:cylindre>tr:silindir
krank|n|en|crank|kıvrık mil|MOD||
şanzıman|n|fr|changement|değiştirme|MOD||la:cambiare>fr:changement>tr:şanzıman
makara|n|el?|makarás|çıkrık|OSM||
çark|n|fa|çarḫ|tekerlek|EAT||
dişli|n|tr|dişli|dişli çark|OSM||
vinç|n|en|winch|kaldırma aygıtı|CUM||
kriko|n|it|cricco|kaldırma aygıtı|CUM||
pompa|n|it|pompa|emme basma aygıtı|OSM19||
vana|n|fr|vanne|musluk|MOD||
valf|n|en|valve|kapakçık|MOD||la:valva>en:valve>tr:valf
supap|n|fr|soupape|emniyet kapağı|CUM||
boru|n|tr|boru|içi boş uzun nesne|DLT||
körük|n|tr|körük|hava basıcı|DLT||
perçin|n|fa|parçīn|çivi başı ezme|OSM||
lehim|n|ar|laḥm|yapıştırma|OSM||
freze|n|fr|fraise|çilek; yiv açıcı|MOD||
eğe|n|tr|egek|törpü|DLT||
zımpara|n|fa|sunbāde|aşındırıcı taş|OSM||
mengene|n|el|mángano|sıkıştırma aygıtı|OSM||grc:mánganon>el:mángano>tr:mengene
kerpeten|n|ar|kelbetān|iki köpek|EAT||
örs|n|tr|örs|demir dövme kütüğü|DLT||
levye|n|fr|levier|kaldıraç|CUM||la:levare>fr:levier>tr:levye
teker|n|tr|tegirmek|yuvarlanan|DLT|*tegir-|
aks|n|fr|axe|dingil|CUM||la:axis>fr:axe>tr:aks
kayış|n|tr|kayış|deri şerit|DLT||
kasnak|n|tr|kasnak|çember|OSM||
halat|n|ar|ḫalaṭ|kalın ip|OSM||
sim|n|fa|sīm|gümüş; tel|EAT||
izolatör|n|fr|isolateur|yalıtan|CUM||la:insula>it:isolare>fr:isolateur>tr:izolatör
yalıtım|n|tr|yalıt-|yalnız bırakma|DD||
yalıtkan|n|tr|yalıt-|elektriği geçirmeyen|DD||
iletken|n|tr|ilet-|ileten|DD|*il-|
iletim|n|tr|ilet-|iletme|DD|*il-|
ilinti|n|tr|il-|bağlantı|DD|*il-|
iletki|n|tr|ilet-|açı ölçer|DD|*il-|
kaldıraç|n|tr|kaldır-|kaldırma kolu|DD|*kalk-|
imalat|n|ar|iʿmālāt|yapımlar|OSM19|A-M-L|
kumpas|n|fr|compas|pergel; ölçü aleti|OSM||la:compassare>fr:compas>tr:kumpas
gönye|n|el|gōnía|köşe, açı|OSM||
şakul|n|ar|şāqūl|çekül|OSM||
kantar|n|ar|qinṭār|yüzlük ağırlık|EAT||la:centenarium>grc:kentēnárion>ar:qinṭār>tr:kantar
okka|n|ar|ūqiyya|onikide bir|EAT||la:uncia>grc:ounkía>ar:ūqiyya>tr:okka
dirhem|n|ar|dirham|gümüş sikke; ağırlık|EAT||grc:drakhmḗ>ar:dirham>tr:dirhem
miskal|n|ar|mithqāl|ağırlık ölçüsü|EAT|S-K-L|
kile|n|ar|kayl|ölçek|EAT||
batman|n|tr|batman|ağırlık ölçüsü|DLT||
çeki|n|tr|çeki|odun tartısı|OSM|*çek-|
mezura|n|it|misura|ölçü|CUM||la:mensura>it:misura>tr:mezura
diyapazon|n|fr|diapason|tüm sesler|CUM||grc:diapasôn>fr:diapason>tr:diyapazon
büyüteç|n|tr|büyüt-|büyüten|DD|*büyü-|
prizma|n|fr|prisme|kesilmiş|CUM||grc:prîsma>la:prisma>fr:prisme>tr:prizma
lens|n|en|lens|mercimek biçimli cam|MOD||la:lens>en:lens>tr:lens
mercek|n|fa|mercimek|mercimek biçimli cam|DD||
# --- Elektrik ve elektronik -------------------------------------------------------------------
elektrikçi|n|fr|électrique|elektrik işçisi|CUM|ēlektron|
elektromanyetik|adj|fr|électromagnétique|elektrik ve mıknatıs|MOD|ēlektron|grc:ḗlektron+Magnēsía>fr:électromagnétique>tr:elektromanyetik
elektrikli|adj|fr|électrique|elektrikle çalışan|CUM|ēlektron|
vat|n|en|watt|Watt birimi|CUM||
ohm|n|de|Ohm|Ohm birimi|CUM||
hertz|n|de|Hertz|Hertz birimi|MOD||
jul|n|en|joule|Joule birimi|MOD||
newton|n|en|newton|Newton birimi|MOD||
paskal|n|fr|pascal|Pascal birimi|MOD||
kelvin|n|en|kelvin|Kelvin birimi|MOD||
bobin|n|fr|bobine|makara|CUM||
röle|n|fr|relais|aktarıcı|MOD||
kondansatör|n|fr|condensateur|yoğunlaştırıcı|CUM||la:condensare>fr:condensateur>tr:kondansatör
transistör|n|en|transistor|aktarım direnci|MOD||
şalter|n|de|Schalter|açma kapama aygıtı|CUM||
batarya|n|it|batteria|vurma; pil takımı|OSM19||la:battuere>it:batteria>tr:batarya
flor|n|fr|fluor|akan|CUM||la:fluor>fr:fluor>tr:flor
soket|n|en|socket|yuva|MOD||
piksel|n|en|pixel|resim öğesi|MOD||
modem|n|en|modem|kipleyici çözücü|MOD||
disket|n|fr|disquette|küçük disk|MOD||grc:dískos>fr:disquette>tr:disket
toner|n|en|toner|ton veren|NEW||
kartuş|n|fr|cartouche|kâğıt külah|CUM||it:cartoccio>fr:cartouche>tr:kartuş
karton|n|fr|carton|kalın kâğıt|CUM||it:cartone>fr:carton>tr:karton
kartela|n|it|cartella|kâğıt kabı|CUM||
monitör|n|fr|moniteur|uyarıcı; ekran|MOD||la:monitor>fr:moniteur>tr:monitör
# --- Bilişim ve İnternet (İngilizce alıntılar) ------------------------------------------------
spam|n|en|spam|istenmeyen ileti|NEW||
link|n|en|link|bağlantı|NEW||
hacker|n|en|hacker|bilgisayar korsanı|NEW||
emoji|n|ja|emoji|resim yazı|NEW||
selfie|n|en|selfie|özçekim|NEW||
avatar|n|en|avatar|iniş, cisimlenme|NEW||sa:avatāra>en:avatar>tr:avatar
podcast|n|en|podcast|dijital ses yayını|NEW||
dron|n|en|drone|erkek arı; insansız araç|NEW||
android|n|en|android|insan görünümlü|NEW||grc:anḗr+eîdos>en:android>tr:android
webcam|n|en|webcam|ağ kamerası|NEW||
profil|n|fr|profil|yandan görünüş|CUM||it:profilo>fr:profil>tr:profil
forum|n|fr|forum|pazar yeri; tartışma alanı|CUM||la:forum>fr:forum>tr:forum
aplikasyon|n|fr|application|uygulama|MOD||la:applicatio>fr:application>tr:aplikasyon
lisans|n|fr|licence|izin|OSM19||la:licentia>fr:licence>tr:lisans
beta|n|el|bêta|Yunan alfabesinin ikinci harfi|MOD||
alfa|n|el|álpha|Yunan alfabesinin ilk harfi|MOD||
formatlamak|v|fr|format|biçimlendirmek|NEW|forma|
dijitalleşmek|v|fr|digital|sayısal ortama geçmek|NEW||
tıklamak|v|tr|tık|tık sesi çıkarmak|NEW||
bilişim|n|tr|bil-|bilgi işleme|DD|*bil-|
bilişsel|adj|tr|bil-|bilmeye ilişkin|TDK|*bil-|
bilgelik|n|tr|bilge|bilge olma|DLT|*bil-|
bilimsel|adj|tr|bilim|bilime ilişkin|DD|*bil-|
bilimkurgu|n|tr|bilim|bilim kurgusu|MOD|*bil-|
bildirim|n|tr|bildir-|bildirme|DD|*bil-|
sanal|adj|tr|san-|varsayılan, gerçek olmayan|DD|*san-|
simge|n|tr|sim|işaret|DD||
imleç|n|tr|im|gösterge|TDK|*im|
im|n|tr|im|işaret, parola|DLT|*im|
imlemek|v|tr|imle-|işaretlemek|DLT|*im|
kısayol|n|tr|kısa|kestirme|NEW||
masaüstü|n|tr|masa|masa yüzeyi|NEW||
dizüstü|n|tr|diz|dizde kullanılan|NEW||
arayüz|n|tr|ara|ara yüzey|NEW||
abone|n|fr|abonné|sınır belirleyen|OSM19||
önbellek|n|tr|ön|geçici bellek|NEW|*ön|
yedek|n|tr|yedek|yedeğe alınan|DLT||
kullanıcı|n|tr|kullan-|kullanan|DD||
oturum|n|tr|otur-|oturma süresi|DD||
istemci|n|tr|iste-|hizmet isteyen|NEW|*iste-|
istem|n|tr|iste-|isteme|DD|*iste-|
kablosuz|adj|tr|kablo|kablo gerektirmeyen|NEW||
yönlendirici|n|tr|yön|yön veren aygıt|NEW|*yön|
derleyici|n|tr|der-|toplayan; çevirici|TDK|*der-|
dernek|n|tr|der-|toplanma|DD|*der-|
yorumlayıcı|n|tr|yor-|yorumlayan|TDK|*yor-|
hata|n|ar|ḫaṭaʾ|yanlış|EAT||
güncel|adj|tr|gün|bugüne ilişkin|DD|*kün|
güncellemek|v|tr|gün|bugüne uyarlamak|NEW|*kün|
sekme|n|tr|sek-|sıçrama; sayfa ucu|DLT|*sek-|
sekmek|v|tr|sek-|sıçramak|DLT|*sek-|
tuşlamak|v|fr|touche|tuşa basmak|MOD||
bağıntı|n|tr|bağ|ilişki|DD|*bağ-|
sorgulamak|v|tr|sor-|sorguya çekmek|TDK|*sor-|
takip|n|ar|taʿqīb|peşinden gitme|OSM|A-K-B|
akıbet|n|ar|ʿāqiba|son|EAT|A-K-B|
algı|n|tr|al-|alınan duyum|DD|*al-|
algılamak|v|tr|al-|duyumla almak|DD|*al-|
algılayıcı|n|tr|al-|duyum alan aygıt|TDK|*al-|
yonga|n|tr|yon-|yontulmuş parça|DLT||
işletim|n|tr|işle-|işletme|DD|*iş|
işleç|n|tr|işle-|işlem yapan|TDK|*iş|
işlek|adj|tr|işle-|çok işleyen|OSM|*iş|
uygulama|n|tr|uygula-|uygulamak işi|DD|*uy-|
uygulamak|v|tr|uygula-|yürürlüğe koymak|DD|*uy-|
kurulum|n|tr|kur-|kurma|NEW|*kur-|
dizge|n|tr|diz-|sistem|DD|*diz-|
dizgi|n|tr|diz-|harf dizme|DD|*diz-|
dizilim|n|tr|diz-|dizilme biçimi|TDK|*diz-|
çevrim|n|tr|çevir-|döngü|DD|*çevir-|
çevrimiçi|adj|tr|çevir-|bağlantıda|NEW|*çevir-|
çevrimdışı|adj|tr|çevir-|bağlantısız|NEW|*çevir-|
sayman|n|tr|say-|hesap tutan|DD|*say-|
sayısallaştırmak|v|tr|say-|sayısal ortama aktarmak|NEW|*say-|
standart|n|fr|standard|ölçün|CUM||fro:estandart>en:standard>fr:standard>tr:standart
gigabayt|n|en|gigabyte|milyar bayt|NEW||grc:gígas+en:byte>en:gigabyte>tr:gigabayt
terabayt|n|en|terabyte|trilyon bayt|NEW||grc:téras+en:byte>en:terabyte>tr:terabayt
ton|n|fr|tonne|büyük fıçı; bin kilogram|OSM19||fr:tonne>tr:ton
tonaj|n|fr|tonnage|ton hesabı|CUM||fr:tonnage>tr:tonaj
eter|n|fr|éther|üst hava|OSM19||grc:aithḗr>la:aether>fr:éther>tr:eter
parafin|n|fr|paraffine|az ilgili|OSM19||la:parum+affinis>fr:paraffine>tr:parafin
kuark|n|en|quark|temel parçacık|NEW||
bozon|n|fr|boson|Bose parçacığı|NEW||en:boson>fr:boson>tr:bozon
# --- Arapça bilim mirası (sülasi kökler) -----------------------------------------------------
cebren|adv|ar|cabran|zorla|OSM|C-B-R|
cebrî|adj|ar|cabrī|zorlayıcı|OSM|C-B-R|
mecburi|adj|ar|macbūrī|zorunlu|OSM19|C-B-R|
icbar|n|ar|icbār|zorlama|OSM|C-B-R|
nükte|n|ar|nukta|ince söz|EAT|N-K-T|
nüktedan|adj|fa|nukta-dān|nükte bilen|OSM|N-K-T|
merkez|n|ar|markaz|dikilen yer; orta|EAT|R-K-Z|
merkezi|adj|ar|markazī|merkeze ilişkin|OSM19|R-K-Z|
temerküz|n|ar|tamarkuz|merkezde toplanma|OSM19|R-K-Z|
merkeziyet|n|ar|markaziyya|merkezcilik|OSM19|R-K-Z|
mütemerkiz|adj|ar|mutamarkiz|merkezlenmiş|OSM19|R-K-Z|
şekil|n|ar|şakl|biçim|EAT|Ş-K-L|
şekillenmek|v|ar|şakl|biçim almak|OSM|Ş-K-L|
teşkil|n|ar|taşkīl|biçim verme|OSM|Ş-K-L|
teşkilat|n|ar|taşkīlāt|kuruluşlar|OSM19|Ş-K-L|
müşkül|adj|ar|muşkil|karışık, güç|EAT|Ş-K-L|
müşkülat|n|ar|muşkilāt|güçlükler|OSM|Ş-K-L|
eşkâl|n|ar|aşkāl|biçimler|OSM|Ş-K-L|
vasıta|n|ar|wāsiṭa|aracı|EAT|W-S-T|
mütevassıt|adj|ar|mutawassiṭ|orta, aracı|OSM|W-S-T|
vesait|n|ar|wasāʾiṭ|araçlar|OSM19|W-S-T|
müteaddit|adj|ar|mutaʿaddid|sayılı, birçok|OSM|A-D-D|
taaddüt|n|ar|taʿaddud|çoğalma|OSM|A-D-D|
istidat|n|ar|istiʿdād|hazırlık; yetenek|EAT|A-D-D|
idadi|n|ar|iʿdādī|hazırlayıcı okul|OSM19|A-D-D|
zaviye|n|ar|zāwiya|köşe; açı|EAT|Z-W-Y|
münzevi|adj|ar|munzawī|köşeye çekilmiş|OSM|Z-W-Y|
inziva|n|ar|inziwāʾ|köşeye çekilme|OSM|Z-W-Y|
kürevi|adj|ar|kurawī|küresel|OSM19||
sıklet|n|ar|thiqla|ağırlık|OSM|S-K-L|
sakil|adj|ar|thaqīl|ağır; çirkin|EAT|S-K-L|
cisim|n|ar|cism|beden; nesne|EAT|C-S-M|
cismani|adj|ar|cismānī|bedene ilişkin|OSM|C-S-M|
tecessüm|n|ar|tacassum|cisimlenme|OSM|C-S-M|
mücessem|adj|ar|mucassam|cisimleşmiş|OSM|C-S-M|
cüsse|n|ar|cuththa|gövde|OSM|C-S-M|
mizaç|n|ar|mizāc|karışım; huy|EAT|M-Z-C|
imtizaç|n|ar|imtizāc|karışıp uyuşma|OSM|M-Z-C|
mezc|n|ar|mazc|karıştırma|OSM|M-Z-C|
memzuç|adj|ar|mamzūc|karışmış|OSM|M-Z-C|
terkip|n|ar|tarkīb|bileşim|EAT|R-K-B|
merkep|n|ar|markab|binek|EAT|R-K-B|
bahis|n|ar|baḥth|araştırma; konu|EAT|B-H-S|
mebhus|adj|ar|mabḥūth|söz edilen|OSM|B-H-S|
mübahase|n|ar|mubāḥatha|karşılıklı tartışma|OSM|B-H-S|
bahsetmek|v|ar|baḥth|söz etmek|OSM|B-H-S|
tecrübe|n|ar|tacriba|deneme|EAT|C-R-B|
mücerrep|adj|ar|mucarrab|denenmiş|OSM|C-R-B|
tecrübî|adj|ar|tacribī|deneysel|OSM19|C-R-B|
sabit|adj|ar|thābit|durağan|EAT|S-B-T|
sabite|n|ar|thābita|değişmez nicelik|OSM19|S-B-T|
tespit|n|ar|tathbīt|yerleştirme; belirleme|OSM|S-B-T|
müspet|adj|ar|muthbat|kanıtlanmış; olumlu|OSM|S-B-T|
sübut|n|ar|thubūt|kesinleşme|OSM|S-B-T|
fert|n|ar|fard|tek|EAT|F-R-D|
müfret|adj|ar|mufrad|tekil|OSM|F-R-D|
münferit|adj|ar|munfarid|tek başına|OSM|F-R-D|
infirat|n|ar|infirād|yalnız kalma|OSM|F-R-D|
katre|n|ar|qaṭra|damla|EAT|K-T-R|
taktir|n|ar|taqṭīr|damıtma|OSM|K-T-R|
mukattar|adj|ar|muqaṭṭar|damıtılmış|OSM|K-T-R|
kutur|n|ar|quṭr|çap|OSM|K-T-R|
katran|n|ar|qaṭrān|damlayan madde|EAT|K-T-R|
nebat|n|ar|nabāt|bitki|EAT|N-B-T|
nebati|adj|ar|nabātī|bitkisel|OSM|N-B-T|
nebatat|n|ar|nabātāt|bitkiler|OSM|N-B-T|
musattah|adj|ar|musaṭṭaḥ|düzleştirilmiş|OSM|S-T-H|
kaide|n|ar|qāʿida|temel; kural|EAT|K-A-D|
kavait|n|ar|qawāʿid|kurallar|OSM|K-A-D|
tasnif|n|ar|taṣnīf|sınıflandırma|OSM|S-N-F|
musannif|n|ar|muṣannif|sınıflandıran; yazar|OSM|S-N-F|
nevi|n|ar|nawʿ|tür|EAT|N-W-A|
enva|n|ar|anwāʿ|türler|OSM|N-W-A|
tenevvü|n|ar|tanawwuʿ|çeşitlenme|OSM|N-W-A|
fasıl|n|ar|faṣl|ayırma; bölüm|EAT|F-S-L|
fasıla|n|ar|fāṣila|ara|OSM|F-S-L|
tafsilat|n|ar|tafṣīlāt|ayrıntılar|OSM|F-S-L|
mufassal|adj|ar|mufaṣṣal|ayrıntılı|OSM|F-S-L|
munfasıl|adj|ar|munfaṣil|ayrılmış|OSM|F-S-L|
cihaz|n|ar|cihāz|donanım|EAT|C-H-Z|
teçhiz|n|ar|tachīz|donatma|OSM|C-H-Z|
teçhizat|n|ar|tachīzāt|donanımlar|OSM19|C-H-Z|
mücehhez|adj|ar|mucahhaz|donatılmış|OSM|C-H-Z|
müselles|n|ar|muthallath|üçgen|OSM|S-L-S|
sülüs|n|ar|thuluth|üçte bir|EAT|S-L-S|
salise|n|ar|thāliza|üçüncü; saniyenin altmışta biri|OSM|S-L-S|
mutlak|adj|ar|muṭlaq|salıverilmiş; kesin|EAT|T-L-K|
itlak|n|ar|iṭlāq|salıverme|OSM|T-L-K|
mücerret|adj|ar|mucarrad|soyut|OSM|C-R-D|
tecrit|n|ar|tacrīd|soyutlama; ayırma|OSM|C-R-D|
tecerrüt|n|ar|tacarrud|soyutlanma|OSM|C-R-D|
müsavi|adj|ar|musāwī|eşit|OSM|S-W-Y|
müsavat|n|ar|musāwāt|eşitlik|OSM19|S-W-Y|
seviye|n|ar|sawiyya|düzey|OSM19|S-W-Y|
tesviye|n|ar|taswiya|düzleme|OSM|S-W-Y|
mukaddime|n|ar|muqaddima|öne alınan; giriş|EAT|K-D-M|
takdim|n|ar|taqdīm|öne sürme; sunma|OSM|K-D-M|
kıdem|n|ar|qidam|öncelik|OSM|K-D-M|
kademe|n|ar|qadama|basamak|OSM|K-D-M|
kadim|adj|ar|qadīm|eski|EAT|K-D-M|
mevzu|n|ar|mawḍūʿ|konulmuş; konu|OSM|W-D-A|
vaziyet|n|ar|waḍʿiyya|durum|OSM19|W-D-A|
mevzuat|n|ar|mawḍūʿāt|konulmuş kurallar|OSM19|W-D-A|
tesadüf|n|ar|taṣāduf|rastlantı|OSM|S-D-F|
tesadüfi|adj|ar|taṣādufī|rastlantısal|OSM19|S-D-F|
müsadif|adj|ar|muṣādif|rastlayan|OSM|S-D-F|
itmam|n|ar|itmām|tamamlama|OSM|T-M-M|
mütemmim|adj|ar|mutammim|tamamlayan|OSM|T-M-M|
noksan|adj|ar|nuqṣān|eksik|EAT|N-K-S|
nakıs|adj|ar|nāqiṣ|eksik|EAT|N-K-S|
tenkis|n|ar|tanqīṣ|eksiltme|OSM|N-K-S|
ziyade|adj|ar|ziyāda|artış; fazla|EAT|Z-Y-D|
zait|adj|ar|zāʾid|artı; fazla|OSM|Z-Y-D|
mezat|n|ar|mazād|artırma|OSM|Z-Y-D|
tezyit|n|ar|tazyīd|artırma|OSM|Z-Y-D|
kemiyet|n|ar|kammiyya|nicelik|OSM||
keyfiyet|n|ar|kayfiyya|nitelik|OSM|K-Y-F|
keyfî|adj|ar|kayfī|isteğe bağlı|OSM19|K-Y-F|
felekiyat|n|ar|falakiyyāt|gök bilimi|OSM19|F-L-K|
necm|n|ar|nacm|yıldız|EAT|N-C-M|
tencim|n|ar|tancīm|yıldız bakımı|OSM|N-C-M|
kamerî|adj|ar|qamarī|aya ilişkin|OSM|K-M-R|
şemsî|adj|ar|şamsī|güneşe ilişkin|OSM|Ş-M-S|
unsur|n|ar|ʿunṣur|öğe; element|OSM|A-N-S-R|
anasır|n|ar|ʿanāṣir|öğeler|OSM|A-N-S-R|
mesaha|n|ar|misāḥa|yüzölçümü|OSM|M-S-H|
mesh|n|ar|masḥ|sıvazlama|EAT|M-S-H|
tarh|n|ar|ṭarḥ|atma; çıkarma|OSM|T-R-H|
matrah|n|ar|maṭraḥ|atılan yer; vergi tabanı|OSM19|T-R-H|
darp|n|ar|ḍarb|vurma; çarpma|EAT|D-R-B|
mazrup|n|ar|maḍrūb|çarpılan|OSM|D-R-B|
kayıt|n|ar|qayd|bağ; yazım|EAT|K-Y-D|
mukayyet|adj|ar|muqayyad|bağlı; kayıtlı|OSM|K-Y-D|
takyit|n|ar|taqyīd|sınırlama|OSM|K-Y-D|
ayar|n|ar|ʿiyār|ölçün|EAT|A-Y-R|
miyar|n|ar|miʿyār|ölçüt|OSM|A-Y-R|
muhasip|n|ar|muḥāsib|hesap tutan|OSM|H-S-B|
ihtisap|n|ar|iḥtisāb|çarşı denetimi|EAT|H-S-B|
kıyasen|adv|ar|qiyāsan|karşılaştırarak|OSM|K-Y-S|
deveran|n|ar|dawarān|dönüş; dolaşım|OSM|D-W-R|
müdevver|adj|ar|mudawwar|yuvarlak|OSM|D-W-R|
devriye|n|ar|dawriyya|dönerek dolaşma|OSM19|D-W-R|
dairevi|adj|ar|dāʾirawī|çember biçimli|OSM19|D-W-R|
medar|n|ar|madār|dönme yeri; yörünge|EAT|D-W-R|
muvazene|n|ar|muwāzana|denge|OSM|W-Z-N|
mevzun|adj|ar|mawzūn|tartılı; ölçülü|OSM|W-Z-N|
cemi|n|ar|camīʿ|tüm; çoğul|EAT|C-M-A|
nazarî|adj|ar|naẓarī|kuramsal|OSM19|N-Z-R|
nazariyat|n|ar|naẓariyyāt|kuramlar|OSM19|N-Z-R|
ilmiye|n|ar|ʿilmiyya|bilginler sınıfı|OSM|İ-L-M|
tekvin|n|ar|takwīn|var etme|OSM|K-W-N|
muharrik|adj|ar|muḥarrik|devindiren|OSM|H-R-K|
muhtemel|adj|ar|muḥtamal|olası|OSM|H-M-L|
takribi|adj|ar|taqrībī|yaklaşık|OSM19|K-R-B|
takriben|adv|ar|taqrīban|yaklaşık olarak|OSM|K-R-B|
maddi|adj|ar|māddī|maddeye ilişkin|OSM19|M-D-D|
maddiyat|n|ar|māddiyyāt|maddi şeyler|OSM19|M-D-D|
mahlul|n|ar|maḥlūl|çözülmüş; çözelti|OSM|H-L-L|
inhilal|n|ar|inḥilāl|çözülme|OSM|H-L-L|
nispi|adj|ar|nisbī|göreli|OSM19|N-S-B|
zerre|n|ar|ḏarra|toz tanesi|EAT||
menfi|adj|ar|manfī|olumsuz|OSM||
faraziye|n|ar|faraḍiyya|varsayım|OSM19||
farazi|adj|ar|faraḍī|varsayımsal|OSM19||
tahmin|n|ar|taḫmīn|kestirme|EAT||
kavis|n|ar|qaws|yay|EAT||
lif|n|ar|līf|tel, iplik|EAT||
tayf|n|ar|ṭayf|hayal; ışık yelpazesi|OSM||
an|n|ar|ān|kısa zaman|EAT||
cevvi|adj|ar|cawwī|havaya ilişkin|OSM19||
# --- Dil Devrimi ve Öz Türkçe bilim sözcükleri ------------------------------------------------
tümevarım|n|tr|tüm|tüme varma|DD|*tüm|
tümdengelim|n|tr|tüm|tümden gelme|DD|*tüm|
tümel|adj|tr|tüm|genel|DD|*tüm|
tümleç|n|tr|tüm|tamamlayan|DD|*tüm|
tümlev|n|tr|tüm|bütünleyen|DD|*tüm|
tümce|n|tr|tüm|cümle|DD|*tüm|
ölçüm|n|tr|ölç-|ölçme işi|DD|*ölç-|
ölçer|n|tr|ölç-|ölçen aygıt|DD|*ölç-|
ölçüt|n|tr|ölç-|kıstas|DD|*ölç-|
ölçümlemek|v|tr|ölç-|ölçerek değerlendirmek|TDK|*ölç-|
açıölçer|n|tr|açı|açı ölçen araç|DD|*ölç-|
yüzey|n|tr|yüz|dış yüz|DD|*yüz|
yüzeysel|adj|tr|yüz|derin olmayan|DD|*yüz|
uzam|n|tr|uza-|yer kaplama|DD|*uza-|
uzantı|n|tr|uza-|uzayan parça|DD|*uza-|
değişken|n|tr|değiş-|değişen nicelik|DD|*değ-|
değinmek|v|tr|değ-|dokunmak; söz etmek|DLT|*değ-|
değişinim|n|tr|değiş-|mutasyon|DD|*değ-|
teğet|n|tr|değ-|dokunan doğru|DD|*değ-|
eşitlik|n|tr|eş|eşit olma|DD|*eş|
eşlenik|adj|tr|eş|eş olarak bağlanmış|DD|*eş|
eşleşme|n|tr|eş|eş olma|DD|*eş|
eşdeğer|adj|tr|eş|aynı değerde|DD|*eş|
eşkenar|adj|tr|eş|kenarları eşit|DD|*eş|
birim|n|tr|bir|ölçü temeli|DD|*bir|
birleşik|adj|tr|bir|bir olmuş|DD|*bir|
birleşim|n|tr|bir|birleşme|DD|*bir|
bireşim|n|tr|bir|sentez|DD|*bir|
birey|n|tr|bir|fert|DD|*bir|
bireysel|adj|tr|bir|bireye ilişkin|DD|*bir|
birlik|n|tr|bir|bir olma|DLT|*bir|
bileşik|adj|tr|bir|birleşmiş|DD|*bir|
bileşim|n|tr|bir|birleşerek oluşma|DD|*bir|
bileşen|n|tr|bir|oluşturan öğe|DD|*bir|
bileşke|n|tr|bir|kuvvetlerin toplamı|DD|*bir|
yoğunluk|n|tr|yoğun|yoğun olma|DD|*yoğ-|
yoğunlaşmak|v|tr|yoğun|yoğun olmak|DD|*yoğ-|
titreşim|n|tr|titre-|titreme|DD|*titre-|
titremek|v|tr|titre-|ürpererek sallanmak|DLT|*titre-|
titrek|adj|tr|titre-|titreyen|OSM|*titre-|
boyut|n|tr|boy|uzunluk ölçüsü|DD|*boy|
enine|adv|tr|en|en yönünde|OSM|*en|
üstel|adj|tr|üst|üsse ilişkin|DD|*üst|
üs|n|ar|uss|temel, taban|DD||
türetmek|v|tr|türe-|türemesini sağlamak|DD|*tür|
türdeş|adj|tr|tür|aynı türden|DD|*tür|
küme|n|tr|küme|yığın|DLT|*küme|
kümelemek|v|tr|küme|küme yapmak|OSM|*küme|
eğilim|n|tr|eğ-|yönelme|DD|*eğ-|
yansıma|n|tr|yansı-|geri dönme|DD|*yansı-|
yansıtmak|v|tr|yansı-|geri döndürmek|DD|*yansı-|
yansı|n|tr|yansı-|yankı; akis|DLT|*yansı-|
saçılma|n|tr|saç-|dağılma|DD|*saç-|
saçmak|v|tr|saç-|dağıtmak|DLT|*saç-|
saçılım|n|tr|saç-|dağılım|TDK|*saç-|
soğutucu|n|tr|soğut-|soğutan aygıt|DD|*soğu-|
eriyik|n|tr|eri-|erimiş madde|DD|*eri-|
erime|n|tr|eri-|katıdan sıvıya geçme|OSM|*eri-|
patlamak|v|tr|patla-|birden parçalanmak|OSM|*patla-|
patlama|n|tr|patla-|patlamak işi|OSM|*patla-|
patlayıcı|n|tr|patla-|patlayan madde|DD|*patla-|
patlak|adj|tr|patla-|patlamış|OSM|*patla-|
karışım|n|tr|karış-|karışmış madde|DD|*kar-|
karmaşık|adj|tr|karma-|çetrefil|DD|*kar-|
karma|adj|tr|kar-|karışık|DD|*kar-|
karışmak|v|tr|karış-|bir araya girmek|DLT|*kar-|
ayrışım|n|tr|ayrış-|ayrılarak çözülme|DD|*ayır-|
ayrışmak|v|tr|ayrış-|bileşenlere ayrılmak|DD|*ayır-|
ayraç|n|tr|ayır-|parantez|DD|*ayır-|
ayrım|n|tr|ayır-|ayırma|DD|*ayır-|
ayrıt|n|tr|ayır-|kenar çizgisi|DD|*ayır-|
ayrıntı|n|tr|ayır-|detay|DD|*ayır-|
ayrı|adj|tr|adrı|ayrılmış|DLT|*ayır-|
ayırmak|v|tr|adır-|bölmek|DLT|*ayır-|
damıtmak|v|tr|tam-|buharlaştırıp yoğunlaştırmak|DD|*tam-|
damıtık|adj|tr|tam-|damıtılmış|DD|*tam-|
süzgeç|n|tr|süz-|süzme aracı|DLT|*süz-|
süzmek|v|tr|süz-|sıvıyı tortudan ayırmak|DLT|*süz-|
süzüntü|n|tr|süz-|süzülen sıvı|TDK|*süz-|
ilke|n|tr|ilk|temel düşünce|DD|*ilk|
ilkel|adj|tr|ilk|en eski|DD|*ilk|
ilksel|adj|tr|ilk|ilke ilişkin|DD|*ilk|
sonlu|adj|tr|son|sonu olan|DD|*son|
sonsuz|adj|tr|son|sonu olmayan|OSM|*son|
sonlandırmak|v|tr|son|sona erdirmek|TDK|*son|
nedensel|adj|tr|ne|nedene ilişkin|DD|*ne|
nicelik|n|tr|nice|kemiyet|DD|*ne|
nitelik|n|tr|nite|keyfiyet|DD|*ne|
nitel|adj|tr|nite|niteliğe ilişkin|DD|*ne|
nicel|adj|tr|nice|niceliğe ilişkin|DD|*ne|
odak|n|tr|od|ışınların toplandığı nokta|DD|*od|
odaklanmak|v|tr|od|odakta toplanmak|TDK|*od|
gözlemlemek|v|tr|köz|gözlem yapmak|TDK|*köz|
gözetim|n|tr|köz|gözetme|DD|*köz|
itki|n|tr|it-|itme gücü|DD|*it-|
itici|adj|tr|it-|iten|DD|*it-|
itiş|n|tr|it-|itme|OSM|*it-|
çarpım|n|tr|çarp-|çarpma sonucu|DD|*çarp-|
çarpan|n|tr|çarp-|çarpılan sayı|DD|*çarp-|
çarpı|n|tr|çarp-|çarpma işareti|DD|*çarp-|
çarpışma|n|tr|çarp-|çarpma|OSM|*çarp-|
artı|n|tr|art-|toplama işareti|DD|*art-|
artış|n|tr|art-|artma|DD|*art-|
eksi|n|tr|eksi-|çıkarma işareti|DD|*eksi-|
eksiltmek|v|tr|eksi-|azaltmak|DLT|*eksi-|
tartı|n|tr|tart-|ağırlık ölçme|DLT|*tart-|
tartım|n|tr|tart-|tartma|DD|*tart-|
deneysel|adj|tr|dene-|deneye dayanan|DD|*den-|
denek|n|tr|dene-|deneme nesnesi|DD|*den-|
ısıl|adj|tr|ısı|ısıya ilişkin|DD|*ısı-|
ısıtıcı|n|tr|ısıt-|ısıtan aygıt|DD|*ısı-|
ışıma|n|tr|ışı-|ışık saçma|DD|*ışı-|
ışınım|n|tr|ışı-|radyasyon|DD|*ışı-|
evrilmek|v|tr|evir-|dönüşmek|DD|*evir-|
dönence|n|tr|dön-|tropika|DD|*dön-|
dönel|adj|tr|dön-|dönmeyle oluşan|DD|*dön-|
kesişim|n|tr|kes-|kesişme|DD|*kes-|
kesinlik|n|tr|kes-|kesin olma|DD|*kes-|
bölü|n|tr|böl-|bölme işareti|DD|*böl-|
basım|n|tr|bas-|basma işi|DD|*bas-|
kırınım|n|tr|kır-|dalga kırılması|DD|*kır-|
kırılma|n|tr|kır-|kırılmak işi|OSM|*kır-|
çözücü|n|tr|çöz-|çözen madde|DD|*çöz-|
çözünürlük|n|tr|çöz-|çözünme oranı|TDK|*çöz-|
kaynaşma|n|tr|kayna-|birleşme|DD|*kayna-|
yanıcı|adj|tr|yan-|kolay yanan|DD|*yan-|
donatı|n|tr|dona-|donanım|DD|*don-|
donatmak|v|tr|dona-|gerekli araçları vermek|DLT|*don-|
olasılık|n|tr|ol-|olabilirlik|DD|*ol-|
özdek|n|tr|öz|madde|DD|*öz|
özgül|adj|tr|öz|kendine özgü|DD|*öz|
özdeş|adj|tr|öz|tıpatıp aynı|DD|*öz|
özçekim|n|tr|öz|kendini çekme|NEW|*öz|
varsayılan|adj|tr|var|öntanımlı|NEW|*var-|
çıkarım|n|tr|çık-|sonuç çıkarma|DD|*çık-|
koşut|adj|tr|koş-|paralel|DD|*koş-|
doğrusal|adj|tr|doğru|çizgisel|DD|*doğ-|
doğrultu|n|tr|doğru|yön|DD|*doğ-|
düzenek|n|tr|düz|mekanizma|DD|*düz-|
katsayı|n|tr|kat|çarpan|DD|*kat-|
akışkan|n|tr|ak-|akan madde|DD|*ak-|
akı|n|tr|ak-|akış miktarı|DD|*ak-|
tanımlamak|v|tr|tanı-|tanımını yapmak|DD|*tanı-|
sıvı|n|tr|sıv-|akışkan madde|DD||
katı|n|tr|katıg|sert madde|DLT||
yarıçap|n|tr|yarı|çapın yarısı|DD||
çap|n|hy|çʻapʻ|ölçü, boyut|OSM||
köşegen|n|tr|köşe|köşeleri birleştiren|DD||
ortalama|n|tr|orta|ortadaki değer|DD||
limit|n|fr|limite|sınır|MOD||la:limes>fr:limite>tr:limit
öğe|n|tr|öğe|eleman|DD||
parçacık|n|fa|pārçe|küçük parça|DD||
# --- Gök bilimi ---------------------------------------------------------------------------------
büyültmek|v|tr|büyült-|büyük kılmak|OSM|*büyü-|
soğutma|n|tr|soğut-|soğutma işi|TDK|*soğu-|
ensiz|adj|tr|en|dar|OSM|*en|
boyuna|adv|tr|boy|uzunlamasına|OSM|*boy|
eğilmek|v|tr|egil-|bükülmek|DLT|*eğ-|
"""

FAMILIES = r"""
physis|el|doğa|Eski Yunanca phýsis "doğa, oluş"; fizik, fizikçi, fiziksel, fizyoterapi, astrofizik ve fizyonomi aynı kökten gelir.
mathēma|el|öğrenilen şey|Eski Yunanca máthēma "öğrenilen bilgi"; matematik, matematikçi ve matematiksel aynı kökten türer.
arithmos|el|sayı|Eski Yunanca arithmós "sayı"; aritmetik ve logaritma (oran sayısı) aynı kökten gelir.
lyein|el|çözmek|Eski Yunanca lýein "çözmek, gevşetmek"; analiz, analist, analitik, kataliz, katalizör, elektroliz, diyaliz ve hidroliz aynı kökten türer.
tithenai|el|koymak|Eski Yunanca tithénai "koymak" ve thésis "koyma"; sentez, sentetik, antitez, protez ve fotosentez aynı kökten gelir.
kentron|el|iğne ucu, merkez|Eski Yunanca kéntron "sivri uç, pergel ucu, merkez"; santral, santrifüj, konsantre, konsantrasyon ve eksantrik aynı kökten türer.
khronos|el|zaman|Eski Yunanca khrónos "zaman"; kronoloji, kronik, kronometre, senkron ve anakronizm aynı kökten gelir.
topos|el|yer|Eski Yunanca tópos "yer"; topoloji, topografya ve ütopya (olmayan yer) aynı kökten türer.
isos|el|eşit|Eski Yunanca ísos "eşit"; izotop, izomer, izobar, izometrik ve izoterm aynı kökten gelir.
sōma|el|beden|Eski Yunanca sôma "beden"; somatik ve ribozom aynı kökten türer; kromozom da bu öğeyi taşır.
plassein|el|biçimlendirmek|Eski Yunanca plássein "yoğurmak, biçimlendirmek"; plazma, plaster ve plastik aynı kökten gelir.
homos|el|aynı|Eski Yunanca homós "aynı"; homojen ve homolog aynı kökten türer.
heteros|el|başka|Eski Yunanca héteros "öteki, başka"; heterojen ve heterodoks aynı kökten gelir.
hyper|el|üstünde, aşırı|Eski Yunanca hypér "üzerinde, ötesinde"; hiperbol, hipermetrop, hiperaktif ve hipermarket aynı ön ekle kurulmuştur.
hypo|el|altında|Eski Yunanca hypó "altında"; hipotenüs (altta gerilen), hipotermi ve hipotez aynı ön ekle kurulur.
kryptos|el|gizli|Eski Yunanca kryptós "gizli"; kripto, kriptoloji, kriptografi ve kripton (gizli gaz) aynı kökten gelir.
Magnēsia|el|Manisa yöresi|Eski Yunanca Magnēsía, mıknatıs taşının çıktığı yöre; manyetik, manyetizma, magnezyum, manganez, manyeto ve mıknatıs aynı addan türer.
khēmeia|el|madenleri dönüştürme sanatı|Eski Yunanca khēmeía, Arapça al-kīmiyāʾ yoluyla; kimya, kimyager, kimyasal, kimyacı, alşimi ve biyokimya aynı kökten gelir.
oxys|el|keskin, ekşi|Eski Yunanca oxýs "keskin, ekşi"; oksit, oksitlenmek, oksidasyon, dioksit, antioksidan ve peroksit aynı kökten türer.
prōtos|el|ilk|Eski Yunanca prôtos "ilk"; proton, prototip ve protoplazma aynı kökten gelir.
neos|el|yeni|Eski Yunanca néos "yeni"; neon (yeni gaz) ve neolitik (yeni taş çağı) aynı kökten türer.
nucleus|la|çekirdek|Latince nucleus "ceviz içi, çekirdek"; nükleer, nükleus ve nükleotit aynı kökten gelir.
lithos|el|taş|Eski Yunanca líthos "taş"; litografi, monolit, litosfer ve paleolitik aynı kökten türer.
aēr|el|hava|Eski Yunanca aḗr "hava"; aerodinamik, aerosol, aerobik ve anaerobik aynı kökten gelir.
ienai|el|gitmek|Eski Yunanca iénai "gitmek" ve ión "giden"; iyonik, katyon, anyon, iyonosfer ve iyonlaşma aynı kökten türer.
glykys|el|tatlı|Eski Yunanca glykýs "tatlı"; glikoz, glikojen, gliserin ve glisemi aynı kökten gelir.
metallon|el|maden ocağı|Eski Yunanca métallon "maden"; metal, metalurji ve metalik aynı kökten türer.
mikros|el|küçük|Eski Yunanca mikrós "küçük"; mikron, mikrodalga, mikroçip, mikro, mikroskobik ve mikroorganizma aynı kökten gelir.
makros|el|büyük, uzun|Eski Yunanca makrós "uzun, büyük"; makro, makroekonomi ve makromolekül aynı kökten türer.
polys|el|çok|Eski Yunanca polýs "çok"; polimer, poligon, polinom, politeknik ve polietilen aynı kökten gelir.
monos|el|tek|Eski Yunanca mónos "tek"; monoton, monopol, monokl, monografi ve monomer aynı kökten türer.
autos|el|kendi|Eski Yunanca autós "kendi"; otomatik, otonom, otonomi, otomasyon, otopsi ve otomat aynı kökten gelir.
dynamis|el|güç|Eski Yunanca dýnamis "güç"; dinamik, dinamo, dinamit, dinamizm ve termodinamik aynı kökten türer.
stasis|el|durma|Eski Yunanca stásis "durma" ve statós "duran"; statik, termostat, hidrostatik ve elektrostatik aynı kökten gelir.
taxis|el|düzenleme|Eski Yunanca táxis "dizme, düzen"; taksonomi, sentaks ve taktik aynı kökten türer. (Taksi ve taksimetre buraya değil, Latince taxāre "değer biçmek" < tangere köküne bağlanır.)
nomos|el|yasa, pay|Eski Yunanca nómos "yasa, kural"; agronomi ve metronom aynı kökten gelir; astronomi ve ekonomi de bu öğeyi taşır.
sphaira|el|top, küre|Eski Yunanca sphaîra "top"; sfer, atmosfer, hemisfer, stratosfer, biyosfer ve sferik aynı kökten türer.
morphē|el|biçim|Eski Yunanca morphḗ "biçim"; morfoloji, amorf, metamorfoz, morfem ve polimorf aynı kökten gelir.
gnōsis|el|bilgi|Eski Yunanca gnôsis "bilme"; gnostik, agnostik, prognoz ve diyagnostik aynı kökten türer.
organon|el|araç|Eski Yunanca órganon "iş aracı"; organik, organize, organizasyon ve organel aynı kökten gelir.
baros|el|ağırlık|Eski Yunanca báros "ağırlık" ve barýs "ağır"; baryum ve barometrik aynı kökten türer; barometre de bu öğeyi taşır.
khilioi|el|bin|Eski Yunanca khílioi "bin"; kilogram, kilovat, kilobayt ve kilohertz aynı ön öğeyle kurulur.
megas|el|büyük|Eski Yunanca mégas "büyük"; megabayt, megapiksel, megahertz ve megaloman aynı kökten gelir.
nanos|el|cüce|Eski Yunanca nânos "cüce"; nanoteknoloji ve nanometre aynı kökten türer.
gramma|el|yazılan şey; küçük ağırlık|Eski Yunanca grámma "harf, yazı; küçük ağırlık"; gram, miligram, diyagram, hologram ve programlama aynı kökten gelir.
litra|el|ağırlık birimi|Eski Yunanca lítra "tartı birimi"; litre ve mililitre aynı kökten türer.
gala|el|süt|Eski Yunanca gála "süt"; galaksi (Samanyolu), galaktik ve galaktoz (süt şekeri) aynı kökten gelir.
elleipsis|el|eksik kalma|Eski Yunanca élleipsis "eksiklik"; elips, eliptik ve elipsoit aynı kökten türer.
tornos|el|torna, döndürme|Eski Yunanca tórnos "pergel, torna"; torna, turne, tur, turizm, turist, turnike, turnuva ve kontur aynı kökten gelir.
kybernan|el|dümen tutmak|Eski Yunanca kybernân "dümen tutmak, yönetmek"; siber ve sibernetik aynı kökten türer.
eikōn|el|görüntü|Eski Yunanca eikṓn "görüntü, tasvir"; ikon, ikona ve ikonik aynı kökten gelir.
bēryllos|el|yeşil değerli taş|Eski Yunanca bḗryllos; Arapça yoluyla billur, Fransızca yoluyla beril, berilyum, İtalyanca yoluyla pırlanta ve brilyant aynı kökten türer.
xenos|el|yabancı|Eski Yunanca xénos "yabancı, konuk"; ksenon (yabancı gaz) ve ksenofobi aynı kökten gelir.
naphtha|fa|yer yağı|Farsça naft "petrol"; neft doğrudan, naftalin ve nafta Yunanca-Fransızca yoluyla aynı kökten türer.
krystallos|el|buz, billur|Eski Yunanca krýstallos "buz"; kristalize ve kristalografi aynı kökten gelir; kristal de bu köktendir.
elastikos|el|iten, esnek|Eski Yunanca elastikós "iten"; elastik, elastikiyet ve elastomer aynı kökten türer; lastik de buradan kısalmıştır.
basis|el|basma, temel|Eski Yunanca básis "adım, temel"; baz, bazik ve bazal aynı kökten gelir.
skhēma|el|görünüş, biçim|Eski Yunanca skhêma "biçim"; şema ve şematik aynı kökten türer.
numerus|la|sayı|Latince numerus "sayı"; numerik, numaralamak ve numaratör aynı kökten gelir; numara da buradandır.
calx|la|kireç taşı|Latince calx "kireç"; kalsiyum, kalker ve kalsit aynı kökten türer.
vehere|la|taşımak|Latince vehere "taşımak" ve vector "taşıyan"; vektör ve vektörel aynı kökten gelir.
capere|la|tutmak, almak|Latince capere "tutmak"; kapasite, kapasitör, konsept, persepsiyon, prensip ve resepsiyon aynı kökten türer.
struere|la|yığmak, kurmak|Latince struere "kurmak"; enstrüman, konstrüksiyon, endüstri, endüstriyel ve enstrümantal aynı kökten gelir.
oscillare|la|salınmak|Latince oscillare "sallanmak"; osiloskop, osilasyon ve osilatör aynı kökten türer.
frangere|la|kırmak|Latince frangere "kırmak"; fraksiyon, fraktal, fragman ve refraksiyon aynı kökten gelir.
solvere|la|çözmek|Latince solvere "çözmek"; solüsyon ve solvent aynı kökten türer.
tangere|la|dokunmak|Latince tangere "dokunmak"; tanjant, kontak, entegre, entegrasyon ve integral (dokunulmamış, bütün) aynı kökten gelir; sıklık fiili taxāre "değer biçmek" üzerinden taksi ve taksimetre de bu aileye bağlanır.
signum|la|işaret|Latince signum "işaret"; sinyal, sinyalizasyon, dizayn ve desen aynı kökten türer.
ordo|la|sıra, düzen|Latince ordo "sıra"; koordinat, koordinasyon, koordine ve ordinat aynı kökten gelir.
fungi|la|yerine getirmek|Latince fungi "görevini yapmak"; fonksiyon ve fonksiyonel aynı kökten türer.
vibrare|la|titremek|Latince vibrare "titremek"; vibrasyon ve vibratör aynı kökten gelir.
sol|la|güneş|Latince sol "güneş"; solar ve solaryum aynı kökten türer.
cumulus|la|yığın|Latince cumulus "yığın"; akümülatör ve kümülatif aynı kökten gelir; akü de kısaltmasıdır.
premere|la|basmak, sıkmak|Latince premere "basmak"; pres, kompresör, kompres, ekspres ve depresyon aynı kökten türer.
ventus|la|rüzgâr|Latince ventus "rüzgâr"; vantilatör ve ventilasyon aynı kökten gelir.
fundere|la|dökmek, eritmek|Latince fundere "dökmek"; füzyon ve difüzyon aynı kökten türer.
sulphur|la|kükürt|Latince sulphur "kükürt"; sülfür, sülfat ve sülfürik aynı kökten gelir.
carbo|la|kömür|Latince carbo "kömür"; karbonat, karbüratör, karbonhidrat ve karbonik aynı kökten türer; karbon da buradandır.
nitron|el|güherçile|Eski Yunanca nítron "soda, güherçile"; nitrat, nitrik, nitrojen ve nitrogliserin aynı kökten gelir.
K-H-L|ar|sürme, ince toz|Arapça k-ḥ-l kökü; al-kuḥl (ince sürme tozu) Latince yoluyla alkol, alkolik ve alkolizm sözcüklerine kaynaklık eder.
K-L-Y|ar|kavurmak; bitki külü|Arapça q-l-y kökü; al-qily (kül) Latince yoluyla alkali ve alkalin sözcüklerine kaynaklık eder.
acere|la|ekşi olmak|Latince acere "ekşi olmak", acidus ve acetum (sirke); asit, asidik, aseton, asetat ve asetik aynı kökten türer.
silex|la|çakmak taşı|Latince silex "çakmak taşı"; silis, silisyum, silikon ve silikat aynı kökten gelir.
granum|la|tane|Latince granum "tahıl tanesi"; granül ve granüle aynı kökten türer; granit de buradandır.
benzoe|ar|Cava günlüğü|Arapça lubān cāwī "Cava günlüğü", Latince benzoe yoluyla; benzen ve benzol aynı kökten gelir; benzin de bu öğeyi taşır.
quantus|la|ne kadar|Latince quantus "ne kadar"; kuantum, kantite ve kantitatif aynı kökten türer.
neuter|la|ne o ne bu|Latince neuter "ikisinden de olmayan"; nötr, nötron, nötrino ve nötralize aynı kökten gelir.
moles|la|kütle|Latince moles "kütle, yığın"; mol, moleküler ve molar aynı kökten türer; molekül de buradandır.
agere|la|yapmak, sürmek|Latince agere "yapmak"; reaktör, reaksiyon, reaktif, aktif, aktivite ve aksiyon aynı kökten gelir.
turbo|la|dönen şey|Latince turbo "topaç, girdap"; türbin, türbülans ve turbo aynı kökten türer.
carrus|la|araba|Latince carrus "yük arabası"; şarj (yükleme), şarjör, kargo ve karoser aynı kökten gelir.
alter|la|öteki|Latince alter "öteki"; alternatif ve alternatör (yön değiştiren) aynı kökten türer.
Volta|it|Alessandro Volta|İtalyan fizikçi Alessandro Volta'nın adından; volt, voltaj, voltmetre ve fotovoltaik aynı addan türer.
Ampère|fr|André-Marie Ampère|Fransız fizikçi Ampère'in adından; amper ve ampermetre aynı addan gelir.
centum|la|yüz|Latince centum "yüz"; santim, santigrat ve sent aynı kökten türer; santimetre de bu öğeyi taşır.
mille|la|bin|Latince mille "bin"; mil (bin adım), milimetre ve milenyum aynı kökten gelir; milyon da buradandır.
decem|la|on|Latince decem "on"; desimetre, desibel, desilitre ve desimal aynı kökten türer.
tabula|la|levha|Latince tabula "levha, tahta"; tablet ve tabla aynı kökten gelir; tablo da buradandır.
sentire|la|duymak|Latince sentire "duymak"; sensör, sansasyon ve sansasyonel aynı kökten türer.
modus|la|ölçü, biçim|Latince modus "ölçü, tarz"; modül, modüler, modern, moda, mod ve modülasyon aynı kökten gelir.
iacere|la|atmak|Latince iacere "atmak"; projeksiyon, projektör, objektif, obje ve enjeksiyon aynı kökten türer; proje de buradandır.
qualis|la|ne türden|Latince qualis "nasıl"; kalitatif ve kalifiye aynı kökten gelir; kalite de buradandır.
norma|la|gönye, kural|Latince norma "marangoz gönyesi"; norm, normal ve anormal aynı kökten türer.
classis|la|bölük, sınıf|Latince classis "sınıf"; klasman ve klas aynı kökten gelir; klasik ve klasör de buradandır.
vertere|la|döndürmek|Latince vertere "çevirmek"; versiyon, konvertör ve konvertibl aynı kökten türer.
aptus|la|uygun|Latince aptus "uygun"; adaptör, adaptasyon ve adapte aynı kökten gelir.
pes|la|ayak|Latince pes "ayak"; pedal, pedikür ve empedans (ayak bağı) aynı kökten türer.
rotulus|la|tomar, tekerlek|Latince rotulus "küçük tekerlek, tomar"; kontrol (karşı tomar), rol, rulo ve rulman aynı kökten gelir.
aqua|la|su|Latince aqua "su"; akvaryum, akvadük ve akuakültür aynı kökten türer.
C-B-R|ar|zorlamak; kırık kemiği kavuşturmak|Arapça c-b-r kökü; cebir (parçaları birleştirme), cebren, cebrî, mecburi ve icbar aynı kökten gelir.
N-K-T|ar|noktalamak|Arapça n-k-t kökü; nokta, nükte (ince söz) ve nüktedan aynı kökten türer.
R-K-Z|ar|dikmek, saplamak|Arapça r-k-z kökü; merkez (dikilen yer), merkezi, temerküz, merkeziyet ve mütemerkiz aynı kökten gelir.
Ş-K-L|ar|biçim vermek|Arapça ş-k-l kökü; şekil, şekillenmek, teşkil, teşkilat, müşkül, müşkülat ve eşkâl aynı kökten türer.
W-S-T|ar|orta|Arapça w-s-ṭ kökü; vasat, vasıta, vasati, mütevassıt, tavassut ve vesait aynı kökten gelir.
A-D-D|ar|saymak|Arapça ʿ-d-d kökü; adet, müteaddit, taaddüt, istidat ve idadi aynı kökten türer.
Z-W-Y|ar|köşe|Arapça z-w-y kökü; zaviye (köşe; açı), münzevi ve inziva aynı kökten gelir.
S-K-L|ar|ağır olmak|Arapça th-q-l kökü; sıklet, sakil ve miskal aynı kökten gelir.
C-S-M|ar|beden|Arapça c-s-m kökü; cisim, cismani, tecessüm, mücessem ve cüsse aynı kökten türer.
M-Z-C|ar|karıştırmak|Arapça m-z-c kökü; mizaç (karışım; huy), imtizaç, mezc ve memzuç aynı kökten türer.
R-K-B|ar|binmek; üst üste koymak|Arapça r-k-b kökü; terkip, merkep ve mürekkep aynı kökten gelir.
B-H-S|ar|araştırmak|Arapça b-ḥ-th kökü; bahis, mebhus, mübahase ve bahsetmek aynı kökten türer.
C-R-B|ar|denemek|Arapça c-r-b kökü; tecrübe, mücerrep ve tecrübî aynı kökten gelir.
S-B-T|ar|durmak, kesinleşmek|Arapça th-b-t kökü; sabit, sabite, tespit, müspet ve sübut aynı kökten türer.
F-R-D|ar|tek olmak|Arapça f-r-d kökü; fert, müfret, münferit ve infirat aynı kökten gelir.
K-T-R|ar|damlamak; çap|Arapça q-ṭ-r kökü; katre (damla), taktir (damıtma), mukattar, kutur (çap) ve katran aynı kökten gelir.
N-B-T|ar|bitmek, yetişmek|Arapça n-b-t kökü; nebat, nebati ve nebatat aynı kökten türer.
S-T-H|ar|yaymak, düzlemek|Arapça s-ṭ-ḥ kökü; satıh (yüzey), sathi ve musattah aynı kökten gelir.
K-A-D|ar|oturmak; temel|Arapça q-ʿ-d kökü; kaide (temel; kural) ve kavait aynı kökten türer.
S-N-F|ar|sınıflamak|Arapça ṣ-n-f kökü; sınıf, tasnif ve musannif aynı kökten gelir.
N-W-A|ar|tür|Arapça n-w-ʿ kökü; nevi, enva ve tenevvü aynı kökten türer.
F-S-L|ar|ayırmak|Arapça f-ṣ-l kökü; fasıl, fasıla, tafsilat, mufassal ve munfasıl aynı kökten gelir.
C-H-Z|ar|donatmak|Arapça c-h-z kökü; cihaz, teçhiz, teçhizat ve mücehhez aynı kökten türer.
S-L-S|ar|üç|Arapça th-l-th kökü; müselles (üçgen), sülüs (üçte bir) ve salise aynı kökten gelir.
T-L-K|ar|salıvermek|Arapça ṭ-l-q kökü; mutlak (salıverilmiş, kesin) ve itlak aynı kökten türer; talak da buradandır.
C-R-D|ar|soymak, soyutlamak|Arapça c-r-d kökü; mücerret, tecrit ve tecerrüt aynı kökten gelir.
S-W-Y|ar|eşit olmak|Arapça s-w-y kökü; müsavi, müsavat, seviye ve tesviye aynı kökten türer.
K-D-M|ar|önce gelmek|Arapça q-d-m kökü; mukaddime, takdim, kıdem, kademe ve kadim aynı kökten gelir.
W-D-A|ar|koymak|Arapça w-ḍ-ʿ kökü; mevzu (konulmuş; konu), vaziyet ve mevzuat aynı kökten türer.
S-D-F|ar|rastlamak|Arapça ṣ-d-f kökü; tesadüf, tesadüfi ve müsadif aynı kökten gelir.
T-M-M|ar|tamamlamak|Arapça t-m-m kökü; tam, tamam, itmam ve mütemmim aynı kökten türer.
N-K-S|ar|eksilmek|Arapça n-q-ṣ kökü; noksan, nakıs ve tenkis aynı kökten gelir.
Z-Y-D|ar|artmak|Arapça z-y-d kökü; ziyade, zait, mezat (artırma) ve tezyit aynı kökten türer.
K-Y-F|ar|nasıl; nitelik|Arapça k-y-f kökü; keyfiyet (nitelik), keyfî ve keyif aynı kökten gelir.
F-L-K|ar|gök katı|Arapça f-l-k kökü; felek, eflak ve felekiyat (gök bilimi) aynı kökten gelir.
N-C-M|ar|yıldız|Arapça n-c-m kökü; müneccim, necm, tencim ve nücum aynı kökten türer.
K-M-R|ar|ay|Arapça q-m-r kökü; kamer, kamerî ve kameriye aynı kökten türer.
Ş-M-S|ar|güneş|Arapça ş-m-s kökü; şems, şemsî ve şemsiye (güneşlik) aynı kökten gelir.
A-N-S-R|ar|öğe|Arapça ʿ-n-ṣ-r dörtlü kökü; unsur ve anasır aynı kökten türer.
M-S-H|ar|sıvazlamak; ölçmek|Arapça m-s-ḥ kökü; mesaha (yüzölçümü) ve mesh aynı kökten gelir.
T-R-H|ar|atmak|Arapça ṭ-r-ḥ kökü; tarh (çıkarma) ve matrah aynı kökten türer.
D-R-B|ar|vurmak|Arapça ḍ-r-b kökü; darp (çarpma), mazrup, darbe ve darbuka aynı kökten gelir.
K-Y-D|ar|bağlamak|Arapça q-y-d kökü; kayıt, mukayyet ve takyit aynı kökten türer.
A-Y-R|ar|ölçün|Arapça ʿ-y-r kökü; ayar ve miyar (ölçüt) aynı kökten gelir.
A-K-B|ar|izlemek; son|Arapça ʿ-q-b kökü; takip ve akıbet aynı kökten türer.
*dök-|tr|dökmek|Eski Türkçe tök- "dökmek"; döküm, dökme ve dökmek aynı kökten türer.
*il-|tr|bağlamak, iliştirmek|Eski Türkçe il- "takmak, iliştirmek"; iletken, iletim, ilinti, iletki ve iletişim aynı kökten gelir.
*büyü-|tr|büyümek|Eski Türkçe bedü- "büyümek"; büyüteç ve büyültmek aynı kökten türer.
*im|tr|işaret|Dîvânu Lugâti't-Türk'teki im "parola, işaret"; im, imlemek ve imleç aynı kökten gelir.
*der-|tr|toplamak|Eski Türkçe tér- "toplamak"; derleyici, dernek, dergi ve derlemek aynı kökten türer.
*sek-|tr|sıçramak|Eski Türkçe sek- "sıçramak"; sekmek ve sekme (sayfa ucu) aynı kökten gelir.
*iş|tr|iş, çalışma|Orhun Yazıtları'ndaki iş "iş"; işletim, işleç, işlek, işlem ve işlev aynı kökten türer.
*çevir-|tr|döndürmek|Eski Türkçe çevür- "döndürmek"; çevrim, çevrimiçi ve çevrimdışı aynı kökten gelir.
*tüm|tr|bütün|Eski Türkçe tüm "bütün, tam"; tümevarım, tümdengelim, tümel, tümleç, tümlev ve tümce aynı kökten türer.
*ölç-|tr|ölçmek|Eski Türkçe ölçe- "ölçmek"; ölçüm, ölçer, ölçüt, ölçümlemek ve açıölçer aynı kökten gelir.
*yüz|tr|yüz, dış yüzey|Eski Türkçe yüz "çehre, yüzey"; yüzey ve yüzeysel aynı kökten türer.
*uza-|tr|uzamak|Eski Türkçe uza- "uzamak"; uzam, uzantı ve uzanmak aynı kökten gelir.
*değ-|tr|dokunmak|Eski Türkçe teg- "değmek"; değişken, değinmek, değişinim ve teğet aynı kökten gelir.
*eş|tr|eş, denk|Eski Türkçe éş "arkadaş, denk"; eşitlik, eşlenik, eşleşme, eşdeğer ve eşkenar aynı kökten türer.
*bir|tr|bir|Eski Türkçe bir "bir"; birim, birleşik, birleşim, bireşim, birey, bireysel, birlik, bileşik, bileşim, bileşen ve bileşke aynı kökten gelir.
*yoğ-|tr|kalınlaşmak|Eski Türkçe yogun "kalın, yoğun"; yoğunluk ve yoğunlaşmak aynı kökten türer.
*titre-|tr|titremek|Eski Türkçe titre- "titremek"; titreşim, titremek ve titrek aynı kökten gelir.
*boy|tr|uzunluk|Eski Türkçe bod "boy, gövde"; boyut ve boylam aynı kökten türer.
*en|tr|genişlik|Eski Türkçe én "genişlik"; enlem ve enine aynı kökten gelir.
*üst|tr|üst|Eski Türkçe üst "üst"; üstel ve üs (kuvvet) aynı kökten türer.
*tür|tr|tür, çeşit|Eski Türkçe tür "çeşit"; türetmek ve türdeş aynı kökten gelir; türev de buradandır.
*küme|tr|yığın|Eski Türkçe küme "yığın"; küme ve kümelemek aynı kökten türer.
*eğ-|tr|eğmek|Eski Türkçe eg- "eğmek"; eğim, eğik ve eğilim aynı kökten gelir.
*yansı-|tr|yankılanmak|Eski Türkçe yaŋsı- "yankılanmak"; yansıma, yansıtmak ve yansı aynı kökten türer.
*saç-|tr|dağıtmak|Eski Türkçe saç- "dağıtmak"; saçılma, saçmak ve saçılım aynı kökten gelir.
*soğu-|tr|soğumak|Eski Türkçe sogı- "soğumak"; soğutucu ve soğutma aynı kökten türer.
*eri-|tr|erimek|Eski Türkçe erü- "erimek"; eriyik ve erime aynı kökten gelir.
*patla-|tr|patlamak|Yansıma kökenli pat sesinden; patlamak, patlama, patlayıcı ve patlak aynı kökten türer.
*kar-|tr|karıştırmak|Eski Türkçe kar- "karıştırmak"; karışım, karmaşık, karma ve karışmak aynı kökten gelir.
*ayır-|tr|ayırmak|Eski Türkçe adır- "ayırmak"; ayrışım, ayrışmak, ayraç, ayrım, ayrıt, ayrıntı, ayrı ve ayırmak aynı kökten türer.
*tam-|tr|damlamak|Eski Türkçe tam- "damlamak"; damıtmak ve damıtık aynı kökten gelir; damla da buradandır.
*süz-|tr|süzmek|Eski Türkçe süz- "süzmek"; süzgeç, süzmek ve süzüntü aynı kökten türer.
*ilk|tr|ilk, önce|Eski Türkçe ilk "önce"; ilke, ilkel ve ilksel aynı kökten gelir.
*son|tr|son|Eski Türkçe soŋ "son"; sonlu, sonsuz ve sonlandırmak aynı kökten türer.
*ne|tr|ne (soru)|Eski Türkçe ne soru sözcüğünden; nedensel, nicelik, nitelik, nitel ve nicel aynı kökten gelir.
*od|tr|ateş|Eski Türkçe ōt "ateş"; odak (ateşin toplandığı nokta) ve odaklanmak aynı kökten türer.
*köz|tr|göz|Eski Türkçe köz "göz"; gözlemevi, gözlemlemek ve gözetim aynı kökten gelir.
*it-|tr|itmek|Eski Türkçe it- "itmek"; itki, itici ve itiş aynı kökten türer.
*çarp-|tr|çarpmak|Eski Türkçe çarp- "vurmak"; çarpım, çarpan, çarpı ve çarpışma aynı kökten gelir.
*art-|tr|artmak|Eski Türkçe art- "artmak"; artı ve artış aynı kökten türer.
*eksi-|tr|eksilmek|Eski Türkçe egsü- "eksilmek"; eksi ve eksiltmek aynı kökten gelir.
*tart-|tr|tartmak|Eski Türkçe tart- "çekmek, tartmak"; tartı ve tartım aynı kökten türer.
"""

COGNATES = r"""@fizik shared_ancestor
  en physics ; fizik
  fr physique ; fizik ; ff:Fransızcada physique ayrıca "bedensel; dış görünüş" anlamındadır
  de Physik ; fizik
  it fisica ; fizik
  es física ; fizik
  ru физика [fizika] ; fizik
  el φυσική [fysikí] ; fizik ; ff:Yunancada fysikí sıfat olarak "doğal" anlamını da korur
  ro fizică ; fizik
  hu fizika ; fizik
  pl fizyka ; fizik
  bg физика [fizika] ; fizik
  sr физика [fizika] ; fizik
  az fizika ; fizik
  uz fizika ; fizik
  kk физика [fizika] ; fizik
  fa فیزیک [fizik] ; fizik
  ar فيزياء [fīzyāʾ] ; fizik
  ur فزکس [fiziks] ; fizik
@matematik shared_ancestor
  en mathematics ; matematik
  fr mathématiques ; matematik
  de Mathematik ; matematik
  it matematica ; matematik
  es matemáticas ; matematik
  ru математика [matematika] ; matematik
  el μαθηματικά [mathimatiká] ; matematik ; ff:Eski Yunanca máthēma "öğrenilen şey" anlamından; Yunancada bu bağ hâlâ sezilir
  ro matematică ; matematik
  hu matematika ; matematik
  pl matematyka ; matematik
  bg математика [matematika] ; matematik
  sr математика [matematika] ; matematik
  uz matematika ; matematik
  kk математика [matematika] ; matematik
  ky математика [matematika] ; matematik
@aritmetik shared_ancestor
  en arithmetic ; aritmetik
  fr arithmétique ; aritmetik
  de Arithmetik ; aritmetik
  it aritmetica ; aritmetik
  es aritmética ; aritmetik
  ru арифметика [arifmetika] ; aritmetik
  el αριθμητική [arithmitikí] ; aritmetik
  ro aritmetică ; aritmetik
  hu aritmetika ; aritmetik
  pl arytmetyka ; aritmetik
  bg аритметика [aritmetika] ; aritmetik
  az arifmetika ; aritmetik
  uz arifmetika ; aritmetik
  kk арифметика [arifmetika] ; aritmetik
@analiz shared_ancestor
  en analysis ; çözümleme
  fr analyse ; çözümleme
  de Analyse ; çözümleme
  it analisi ; çözümleme
  es análisis ; çözümleme
  ru анализ [analiz] ; çözümleme; tahlil
  el ανάλυση [análysi] ; çözümleme ; ff:Yunancada análysi ayrıca "çözünürlük" (ekran) anlamında kullanılır
  ro analiză ; çözümleme
  hu analízis ; çözümleme
  pl analiza ; çözümleme
  bg анализ [analiz] ; çözümleme
  sr анализа [analiza] ; çözümleme
  az analiz ; çözümleme
  uz analiz ; çözümleme
  kk анализ [analiz] ; çözümleme
  fa آنالیز [ānāliz] ; çözümleme
@sentez shared_ancestor
  en synthesis ; bireşim
  fr synthèse ; bireşim
  de Synthese ; bireşim
  it sintesi ; bireşim ; ff:İtalyancada sintesi "özet" anlamında da yaygındır
  es síntesis ; bireşim
  ru синтез [sintez] ; bireşim
  el σύνθεση [sýnthesi] ; bireşim ; ff:Yunancada sýnthesi ayrıca "bileşim, beste" demektir
  ro sinteză ; bireşim
  hu szintézis ; bireşim
  pl synteza ; bireşim
  bg синтез [sintez] ; bireşim
  az sintez ; bireşim
  uz sintez ; bireşim
  kk синтез [sintez] ; bireşim
@santral shared_ancestor
  en central ; merkezî ; ff:İngilizcede yalnız sıfattır; Türkçede "telefon santrali" gibi ad olmuştur
  fr centrale ; santral; merkez
  de Zentrale ; merkez; santral
  it centrale ; santral; merkezî
  es central ; santral; merkezî
  ro centrală ; santral
  pl centrala ; santral
  bg централа [tsentrala] ; santral
  sr централа [centrala] ; santral
  az santral ; santral
@kronoloji shared_ancestor
  en chronology ; kronoloji
  fr chronologie ; kronoloji
  de Chronologie ; kronoloji
  it cronologia ; kronoloji
  es cronología ; kronoloji
  ru хронология [khronologiya] ; kronoloji
  el χρονολογία [chronología] ; kronoloji; tarih (yıl) ; ff:Yunancada chronología ayrıca "tarih atma, yıl" anlamına gelir
  ro cronologie ; kronoloji
  hu kronológia ; kronoloji
  pl chronologia ; kronoloji
  bg хронология [khronologiya] ; kronoloji
  az xronologiya ; kronoloji
  uz xronologiya ; kronoloji
  kk хронология [khronologiya] ; kronoloji
@manyetik shared_ancestor
  en magnetic ; manyetik
  fr magnétique ; manyetik
  de magnetisch ; manyetik
  it magnetico ; manyetik
  es magnético ; manyetik
  ru магнитный [magnitnyy] ; manyetik
  el μαγνητικός [magnitikós] ; manyetik
  ro magnetic ; manyetik
  hu mágneses ; manyetik
  pl magnetyczny ; manyetik
  az maqnit ; mıknatıs ; ff:Azerbaycan Türkçesinde Rusça yoluyla maqnit "mıknatıs" adıdır
  uz magnit ; mıknatıs ; ff:Özbekçede magnit "mıknatıs" adıdır
  kk магнит [magnit] ; mıknatıs
@oksit shared_ancestor
  en oxide ; oksit
  fr oxyde ; oksit
  de Oxid ; oksit
  it ossido ; oksit
  es óxido ; oksit ; ff:İspanyolcada óxido günlük dilde "pas" demektir
  ru оксид [oksid] ; oksit
  el οξείδιο [oxeídio] ; oksit
  ro oxid ; oksit
  hu oxid ; oksit
  bg оксид [oksid] ; oksit
  az oksid ; oksit
  uz oksid ; oksit
  kk оксид [oksid] ; oksit
@proton shared_ancestor
  en proton ; proton
  fr proton ; proton
  de Proton ; proton
  it protone ; proton
  es protón ; proton
  ru протон [proton] ; proton
  el πρωτόνιο [protónio] ; proton
  ro proton ; proton
  hu proton ; proton
  pl proton ; proton
  bg протон [proton] ; proton
  sr протон [proton] ; proton
  az proton ; proton
  uz proton ; proton
  kk протон [proton] ; proton
  fa پروتون [proton] ; proton
  ar بروتون [brūtūn] ; proton
@nükleer shared_ancestor
  en nuclear ; nükleer
  fr nucléaire ; nükleer
  de nuklear ; nükleer
  it nucleare ; nükleer
  es nuclear ; nükleer
  ro nuclear ; nükleer
  hu nukleáris ; nükleer
  pl nuklearny ; nükleer
  bg нуклеарен [nuklearen] ; nükleer
  sr нуклеаран [nuklearan] ; nükleer
@iyon shared_ancestor
  en ion ; iyon
  fr ion ; iyon
  de Ion ; iyon
  it ione ; iyon
  es ion ; iyon
  ru ион [ion] ; iyon
  el ιόν [ión] ; iyon ; ff:Yunancada ión "giden" ortacından; aynı sözcük "menekşe" anlamındaki íon ile karıştırılır
  ro ion ; iyon
  hu ion ; iyon
  pl jon ; iyon
  bg йон [yon] ; iyon
  az ion ; iyon
  uz ion ; iyon
  kk ион [ion] ; iyon
@metal shared_ancestor
  en metal ; metal
  fr métal ; metal
  de Metall ; metal
  it metallo ; metal
  es metal ; metal
  ru металл [metall] ; metal
  el μέταλλο [métallo] ; metal
  ro metal ; metal
  hu metál ; metal müziği ; ff:Macarcada metál yalnız müzik türüdür; maden için fém kullanılır
  pl metal ; metal
  bg метал [metal] ; metal
  sr метал [metal] ; metal
  az metal ; metal
  uz metall ; metal
  kk металл [metall] ; metal
@polimer shared_ancestor
  en polymer ; polimer
  fr polymère ; polimer
  de Polymer ; polimer
  it polimero ; polimer
  es polímero ; polimer
  ru полимер [polimer] ; polimer
  el πολυμερές [polymerés] ; polimer
  ro polimer ; polimer
  hu polimer ; polimer
  pl polimer ; polimer
  bg полимер [polimer] ; polimer
  az polimer ; polimer
  uz polimer ; polimer
  kk полимер [polimer] ; polimer
@otomatik shared_ancestor
  en automatic ; otomatik
  fr automatique ; otomatik
  de automatisch ; otomatik
  it automatico ; otomatik
  es automático ; otomatik
  ru автоматический [avtomaticheskiy] ; otomatik
  el αυτόματος [aftómatos] ; kendiliğinden; otomatik
  ro automat ; otomatik
  hu automatikus ; otomatik
  pl automatyczny ; otomatik
  bg автоматичен [avtomatichen] ; otomatik
  sr аутоматски [automatski] ; otomatik
  az avtomatik ; otomatik
  uz avtomatik ; otomatik
  kk автоматты [avtomatty] ; otomatik
  fa اتوماتیک [otomātik] ; otomatik
  ar أوتوماتيكي [ʾūtūmātīkī] ; otomatik
  ur آٹومیٹک [āṭomeṭik] ; otomatik
@dinamik shared_ancestor
  en dynamic ; dinamik
  fr dynamique ; dinamik
  de dynamisch ; dinamik
  it dinamico ; dinamik
  es dinámico ; dinamik
  ru динамический [dinamicheskiy] ; dinamik
  el δυναμικός [dynamikós] ; dinamik; güçlü ; ff:Yunancada dynamikós "güçlü, kuvvetli" anlamını korur
  ro dinamic ; dinamik
  hu dinamikus ; dinamik
  pl dynamiczny ; dinamik
  bg динамичен [dinamichen] ; dinamik
  az dinamik ; dinamik
  uz dinamik ; dinamik
  kk динамикалық [dinamikalyq] ; dinamik
@statik shared_ancestor
  en static ; statik
  fr statique ; statik
  de statisch ; statik
  it statico ; statik
  es estático ; statik
  ru статический [staticheskiy] ; statik
  el στατικός [statikós] ; statik
  ro static ; statik
  hu statikus ; statik
  pl statyczny ; statik
  bg статичен [statichen] ; statik
  az statik ; statik
  uz statik ; statik
@atmosfer shared_ancestor
  en atmosphere ; atmosfer
  fr atmosphère ; atmosfer
  de Atmosphäre ; atmosfer
  it atmosfera ; atmosfer
  es atmósfera ; atmosfer
  ru атмосфера [atmosfera] ; atmosfer
  el ατμόσφαιρα [atmósfaira] ; atmosfer ; ff:Yunancada atmós "buhar" ve sfaíra "küre" öğeleri hâlâ saydamdır
  ro atmosferă ; atmosfer
  hu atmoszféra ; atmosfer
  pl atmosfera ; atmosfer
  bg атмосфера [atmosfera] ; atmosfer
  sr атмосфера [atmosfera] ; atmosfer
  az atmosfer ; atmosfer
  uz atmosfera ; atmosfer
  kk атмосфера [atmosfera] ; atmosfer
  fa اتمسفر [atmosfer] ; atmosfer
@morfoloji shared_ancestor
  en morphology ; morfoloji
  fr morphologie ; morfoloji
  de Morphologie ; morfoloji
  it morfologia ; morfoloji
  es morfología ; morfoloji
  ru морфология [morfologiya] ; morfoloji
  el μορφολογία [morfología] ; morfoloji
  ro morfologie ; morfoloji
  hu morfológia ; morfoloji
  pl morfologia ; morfoloji
  bg морфология [morfologiya] ; morfoloji
  az morfologiya ; morfoloji
  uz morfologiya ; morfoloji
  kk морфология [morfologiya] ; morfoloji
@organik shared_ancestor
  en organic ; organik
  fr organique ; organik
  de organisch ; organik
  it organico ; organik ; ff:İtalyancada organico ayrıca "kadro, personel" anlamındadır
  es orgánico ; organik
  ru органический [organicheskiy] ; organik
  el οργανικός [organikós] ; organik
  ro organic ; organik
  hu organikus ; organik
  pl organiczny ; organik
  bg органичен [organichen] ; organik
  uz organik ; organik
  kk органикалық [organikalyq] ; organik
@kilogram shared_ancestor
  en kilogram ; kilogram
  fr kilogramme ; kilogram
  de Kilogramm ; kilogram
  it chilogrammo ; kilogram
  es kilogramo ; kilogram
  ru килограмм [kilogramm] ; kilogram
  el χιλιόγραμμο [chiliógrammo] ; kilogram ; ff:Yunancada khílioi "bin" öğesi kendi yazımıyla korunur; günlük dilde kiló
  ro kilogram ; kilogram
  hu kilogramm ; kilogram
  pl kilogram ; kilogram
  bg килограм [kilogram] ; kilogram
  sr килограм [kilogram] ; kilogram
  az kiloqram ; kilogram
  uz kilogramm ; kilogram
  kk килограмм [kilogramm] ; kilogram
  ky килограмм [kilogramm] ; kilogram
  fa کیلوگرم [kilogeram] ; kilogram
  ar كيلوغرام [kīlūġrām] ; kilogram
  ur کلوگرام [kilogrām] ; kilogram
@gram shared_ancestor
  en gram ; gram
  fr gramme ; gram
  de Gramm ; gram
  it grammo ; gram
  es gramo ; gram
  ru грамм [gramm] ; gram
  el γραμμάριο [grammário] ; gram ; ff:Yunancada grámma "harf" ile ayrım için grammário biçimi kullanılır
  ro gram ; gram
  hu gramm ; gram
  pl gram ; gram
  bg грам [gram] ; gram
  sr грам [gram] ; gram
  az qram ; gram
  uz gramm ; gram
  kk грамм [gramm] ; gram
  fa گرم [geram] ; gram ; ff:Farsçada garm "sıcak" ile yazımı aynıdır; bağlamdan ayrılır
  ar غرام [ġrām] ; gram ; ff:Arapçada ġarām "aşk, tutku" sözcüğüyle yazımı çakışır
  ur گرام [grām] ; gram
@litre shared_ancestor
  en litre ; litre
  fr litre ; litre
  de Liter ; litre
  it litro ; litre
  es litro ; litre
  ru литр [litr] ; litre
  el λίτρο [lítro] ; litre
  ro litru ; litre
  hu liter ; litre
  pl litr ; litre
  bg литър [litar] ; litre
  sr литар [litar] ; litre
  az litr ; litre
  uz litr ; litre
  kk литр [litr] ; litre
  fa لیتر [litr] ; litre
  ar لتر [litr] ; litre
  ur لیٹر [līṭar] ; litre
@hektar shared_ancestor
  en hectare ; hektar
  fr hectare ; hektar
  de Hektar ; hektar
  it ettaro ; hektar
  es hectárea ; hektar
  ru гектар [gektar] ; hektar
  el εκτάριο [ektário] ; hektar
  ro hectar ; hektar
  hu hektár ; hektar
  pl hektar ; hektar
  bg хектар [khektar] ; hektar
  sr хектар [hektar] ; hektar
  az hektar ; hektar
  uz gektar ; hektar
  kk гектар [gektar] ; hektar
  fa هکتار [hektār] ; hektar
  ar هكتار [hiktār] ; hektar
  ur ہیکٹر [hekṭar] ; hektar
@galaksi shared_ancestor
  en galaxy ; gökada
  fr galaxie ; gökada
  de Galaxie ; gökada
  it galassia ; gökada
  es galaxia ; gökada
  ru галактика [galaktika] ; gökada
  el γαλαξίας [galaxías] ; gökada; Samanyolu ; ff:Yunancada gála "süt" ile bağ saydamdır: "sütlü yol"
  ro galaxie ; gökada
  hu galaxis ; gökada
  pl galaktyka ; gökada
  bg галактика [galaktika] ; gökada
  sr галаксија [galaksija] ; gökada
  az qalaktika ; gökada
  uz galaktika ; gökada
  kk галактика [galaktika] ; gökada
@meteor shared_ancestor
  en meteor ; göktaşı
  fr météore ; göktaşı
  de Meteor ; göktaşı
  it meteora ; göktaşı
  es meteoro ; göktaşı
  ru метеор [meteor] ; göktaşı
  el μετέωρο [metéoro] ; göktaşı; havada asılı ; ff:Yunancada metéoro sıfat olarak "havada asılı" anlamını korur
  ro meteor ; göktaşı
  hu meteor ; göktaşı
  pl meteor ; göktaşı
  bg метеор [meteor] ; göktaşı
  az meteor ; göktaşı
  uz meteor ; göktaşı
  kk метеор [meteor] ; göktaşı
@zenit shared_ancestor
  en zenith ; başucu
  fr zénith ; başucu
  de Zenit ; başucu
  it zenit ; başucu
  es cenit ; başucu
  ru зенит [zenit] ; başucu
  el ζενίθ [zeníth] ; başucu
  ro zenit ; başucu
  hu zenit ; başucu
  pl zenit ; başucu
  bg зенит [zenit] ; başucu
  az zenit ; başucu
  ar سمت الرأس [samt ar-raʾs] ; başın yönü ; ff:Arapça samt "yön" tamlamasının Latince yanlış çeviri yazısı zenit biçimini doğurmuştur
@elips shared_ancestor
  en ellipse ; elips
  fr ellipse ; elips
  de Ellipse ; elips
  it ellisse ; elips
  es elipse ; elips
  ru эллипс [ellips] ; elips
  el έλλειψη [élleipsi] ; eksiklik; elips ; ff:Yunancada élleipsi önce "eksiklik, yokluk" demektir; geometri anlamı ikincildir
  ro elipsă ; elips
  hu ellipszis ; elips
  pl elipsa ; elips
  bg елипса [elipsa] ; elips
  az ellips ; elips
  uz ellips ; elips
  kk эллипс [ellips] ; elips
@turizm shared_ancestor
  en tourism ; turizm
  fr tourisme ; turizm
  de Tourismus ; turizm
  it turismo ; turizm
  es turismo ; turizm
  ru туризм [turizm] ; turizm
  el τουρισμός [tourismós] ; turizm
  ro turism ; turizm
  hu turizmus ; turizm
  pl turystyka ; turizm
  bg туризъм [turizam] ; turizm
  sr туризам [turizam] ; turizm
  az turizm ; turizm
  uz turizm ; turizm
  kk туризм [turizm] ; turizm
  fa توریسم [turism] ; turizm
@turist shared_ancestor
  en tourist ; turist
  fr touriste ; turist
  de Tourist ; turist
  it turista ; turist
  es turista ; turist
  ru турист [turist] ; turist
  el τουρίστας [tourístas] ; turist
  ro turist ; turist
  hu turista ; turist
  pl turysta ; turist
  bg турист [turist] ; turist
  sr туриста [turista] ; turist
  az turist ; turist
  uz turist ; turist
  kk турист [turist] ; turist
  fa توریست [turist] ; turist
  ur ٹورسٹ [ṭūrisṭ] ; turist
@sibernetik shared_ancestor
  en cybernetics ; sibernetik
  fr cybernétique ; sibernetik
  de Kybernetik ; sibernetik
  it cibernetica ; sibernetik
  es cibernética ; sibernetik
  ru кибернетика [kibernetika] ; sibernetik
  el κυβερνητική [kyvernitikí] ; sibernetik; hükûmete ilişkin ; ff:Yunancada kyvérnisi "hükûmet" ile aynı köktendir; kyvernitikí "hükûmet sıfatı" olarak da okunur
  ro cibernetică ; sibernetik
  hu kibernetika ; sibernetik
  pl cybernetyka ; sibernetik
  bg кибернетика [kibernetika] ; sibernetik
  az kibernetika ; sibernetik
  uz kibernetika ; sibernetik
  kk кибернетика [kibernetika] ; sibernetik
@elastik shared_ancestor
  en elastic ; esnek
  fr élastique ; esnek; lastik ; ff:Fransızcada élastique ad olarak "lastik bant" demektir; Türkçe lastik buradan kısalmıştır
  de elastisch ; esnek
  it elastico ; esnek; lastik
  es elástico ; esnek
  ru эластичный [elastichnyy] ; esnek
  el ελαστικός [elastikós] ; esnek; lastik ; ff:Yunancada elastikó ad olarak "araba lastiği" demektir
  ro elastic ; esnek
  hu elasztikus ; esnek
  pl elastyczny ; esnek
  bg еластичен [elastichen] ; esnek
  az elastik ; esnek
  uz elastik ; esnek
@baz shared_ancestor
  en base ; temel; baz
  fr base ; temel; baz
  de Base ; baz (kimya) ; ff:Almancada Base kimya terimidir; "temel" için Basis kullanılır
  it base ; temel; baz
  es base ; temel; baz
  ru база [baza] ; üs; depo; veri tabanı ; ff:Rusçada baza "askerî üs, depo" demektir; kimyasal baz için osnovaniye kullanılır
  el βάση [vási] ; temel; baz
  ro bază ; temel; baz
  hu bázis ; temel; üs
  pl baza ; üs; veri tabanı ; ff:Lehçede baza "üs, veri tabanı" anlamındadır; kimyasal baz için zasada kullanılır
  bg база [baza] ; üs; temel
  sr база [baza] ; üs; temel
  az baza ; üs; temel ; ff:Azerbaycan Türkçesinde baza Rusça anlamıyla "üs, depo" demektir
  uz baza ; üs; temel
@şema shared_ancestor
  en scheme ; plan; düzen; dolap ; ff:İngilizcede scheme "plan, düzen; entrika" anlamına kaymıştır
  fr schéma ; şema
  de Schema ; şema
  it schema ; şema
  es esquema ; şema
  ru схема [skhema] ; şema; devre
  el σχήμα [schíma] ; biçim; şekil ; ff:Yunancada schíma "biçim, şekil" demektir; çizim anlamı yoktur
  ro schemă ; şema
  hu séma ; şema
  pl schemat ; şema
  bg схема [skhema] ; şema
  sr шема [šema] ; şema
  az sxem ; şema
  uz sxema ; şema
  kk схема [skhema] ; şema
@kuantum shared_ancestor
  en quantum ; kuantum
  fr quantum ; kuantum
  de Quantum ; miktar; kuantum ; ff:Almancada Quantum günlük dilde "miktar" demektir; fizik terimi Quant'tır
  it quanto ; kuantum
  es cuanto ; kuantum
  ru квант [kvant] ; kuantum
  el κβάντο [kvánto] ; kuantum
  ro cuantă ; kuantum
  hu kvantum ; kuantum
  pl kwant ; kuantum
  bg квант [kvant] ; kuantum
  az kvant ; kuantum
  uz kvant ; kuantum
  kk квант [kvant] ; kuantum
@vektör shared_ancestor
  en vector ; vektör
  fr vecteur ; vektör
  de Vektor ; vektör
  it vettore ; vektör; taşıyıcı ; ff:İtalyancada vettore ayrıca "taşıyıcı, nakliyeci" demektir
  es vector ; vektör
  ru вектор [vektor] ; vektör
  ro vector ; vektör
  hu vektor ; vektör
  pl wektor ; vektör
  bg вектор [vektor] ; vektör
  sr вектор [vektor] ; vektör
  az vektor ; vektör
  uz vektor ; vektör
  kk вектор [vektor] ; vektör
@kapasite shared_ancestor
  en capacity ; kapasite
  fr capacité ; kapasite
  de Kapazität ; kapasite
  it capacità ; kapasite; yetenek
  es capacidad ; kapasite; yetenek
  ro capacitate ; kapasite
  hu kapacitás ; kapasite
  bg капацитет [kapatsitet] ; kapasite
  sr капацитет [kapacitet] ; kapasite
  sq kapacitet ; kapasite
@endüstri shared_ancestor
  en industry ; sanayi
  fr industrie ; sanayi
  de Industrie ; sanayi
  it industria ; sanayi
  es industria ; sanayi
  ru индустрия [industriya] ; sanayi
  ro industrie ; sanayi
  bg индустрия [industriya] ; sanayi
  sr индустрија [industrija] ; sanayi
  sq industri ; sanayi
@sinyal shared_ancestor
  en signal ; sinyal
  fr signal ; sinyal
  de Signal ; sinyal
  it segnale ; sinyal
  es señal ; sinyal; işaret
  ru сигнал [signal] ; sinyal
  el σινιάλο [sinyálo] ; işaret; sinyal ; ff:Yunancaya İtalyanca segnale yoluyla girmiştir
  ro semnal ; sinyal
  hu szignál ; sinyal
  pl sygnał ; sinyal
  bg сигнал [signal] ; sinyal
  sr сигнал [signal] ; sinyal
  az siqnal ; sinyal
  uz signal ; sinyal
  kk сигнал [signal] ; sinyal
  fa سیگنال [signāl] ; sinyal
  ur سگنل [signal] ; sinyal
@koordinat shared_ancestor
  en coordinate ; koordinat
  fr coordonnée ; koordinat
  de Koordinate ; koordinat
  it coordinata ; koordinat
  es coordenada ; koordinat
  ru координата [koordinata] ; koordinat
  ro coordonată ; koordinat
  hu koordináta ; koordinat
  bg координата [koordinata] ; koordinat
  az koordinat ; koordinat
  uz koordinata ; koordinat
  kk координата [koordinata] ; koordinat
@fonksiyon shared_ancestor
  en function ; işlev; fonksiyon
  fr fonction ; işlev; fonksiyon
  de Funktion ; işlev; fonksiyon
  it funzione ; işlev; fonksiyon
  es función ; işlev; fonksiyon
  ru функция [funktsiya] ; işlev; fonksiyon
  ro funcție ; işlev; fonksiyon
  hu funkció ; işlev; fonksiyon
  pl funkcja ; işlev; fonksiyon
  bg функция [funktsiya] ; işlev; fonksiyon
  sr функција [funkcija] ; işlev; fonksiyon
  az funksiya ; işlev; fonksiyon
  uz funksiya ; işlev; fonksiyon
  kk функция [funktsiya] ; işlev; fonksiyon
  ky функция [funktsiya] ; işlev; fonksiyon
@akümülatör shared_ancestor
  en accumulator ; akümülatör
  fr accumulateur ; akümülatör
  de Akkumulator ; akümülatör
  it accumulatore ; akümülatör
  es acumulador ; akümülatör
  ru аккумулятор [akkumulyator] ; akümülatör
  ro acumulator ; akümülatör
  hu akkumulátor ; akümülatör
  pl akumulator ; akümülatör
  bg акумулатор [akumulator] ; akümülatör
  sr акумулатор [akumulator] ; akümülatör
  az akkumulyator ; akümülatör
  uz akkumulyator ; akümülatör
  kk аккумулятор [akkumulyator] ; akümülatör
@füzyon shared_ancestor
  en fusion ; kaynaşma; füzyon
  fr fusion ; erime; kaynaşma
  de Fusion ; birleşme; füzyon
  it fusione ; erime; birleşme
  es fusión ; erime; birleşme
  ro fuziune ; füzyon
  hu fúzió ; füzyon
  pl fuzja ; birleşme; füzyon
@sülfat shared_ancestor
  en sulfate ; sülfat
  fr sulfate ; sülfat
  de Sulfat ; sülfat
  it solfato ; sülfat
  es sulfato ; sülfat
  ru сульфат [sul'fat] ; sülfat
  ro sulfat ; sülfat
  hu szulfát ; sülfat
  bg сулфат [sulfat] ; sülfat
  az sulfat ; sülfat
  uz sulfat ; sülfat
  kk сульфат [sul'fat] ; sülfat
@karbonat shared_ancestor
  en carbonate ; karbonat
  fr carbonate ; karbonat
  de Karbonat ; karbonat
  it carbonato ; karbonat
  es carbonato ; karbonat
  ru карбонат [karbonat] ; karbonat
  ro carbonat ; karbonat
  hu karbonát ; karbonat
  bg карбонат [karbonat] ; karbonat
  az karbonat ; karbonat
  uz karbonat ; karbonat
  kk карбонат [karbonat] ; karbonat
  ar كربونات [karbūnāt] ; karbonat
  fa کربنات [karbonāt] ; karbonat
@nitrat shared_ancestor
  en nitrate ; nitrat
  fr nitrate ; nitrat
  de Nitrat ; nitrat
  it nitrato ; nitrat
  es nitrato ; nitrat
  ru нитрат [nitrat] ; nitrat
  ro nitrat ; nitrat
  hu nitrát ; nitrat
  bg нитрат [nitrat] ; nitrat
  az nitrat ; nitrat
  uz nitrat ; nitrat
  kk нитрат [nitrat] ; nitrat
  fa نیترات [nitrāt] ; nitrat
  ar نترات [nitrāt] ; nitrat
@alkol shared_ancestor
  en alcohol ; alkol
  fr alcool ; alkol
  de Alkohol ; alkol
  it alcol ; alkol
  es alcohol ; alkol
  ru алкоголь [alkogol'] ; alkol
  el αλκοόλ [alkoól] ; alkol
  ro alcool ; alkol
  hu alkohol ; alkol
  pl alkohol ; alkol
  bg алкохол [alkokhol] ; alkol
  sr алкохол [alkohol] ; alkol
  az alkoqol ; alkol
  uz alkogol ; alkol
  kk алкоголь [alkogol'] ; alkol
  fa الکل [alkol] ; alkol
  ar كحول [kuḥūl] ; alkol ; ff:Arapça al-kuḥl "sürme tozu" Batı'da alkol anlamını almış; modern Arapça kuḥūl geri alıntıdır
  ur الکحل [alkoḥal] ; alkol
@asit shared_ancestor
  en acid ; asit
  fr acide ; asit; ekşi ; ff:Fransızcada acide sıfat olarak "ekşi" anlamını korur
  it acido ; asit; ekşi
  es ácido ; asit; ekşi
  ro acid ; asit
  sq acid ; asit
@silikon shared_ancestor
  en silicone ; silikon
  fr silicone ; silikon
  de Silikon ; silikon
  it silicone ; silikon
  es silicona ; silikon
  ru силикон [silikon] ; silikon
  el σιλικόνη [silikóni] ; silikon
  ro silicon ; silikon
  hu szilikon ; silikon
  pl silikon ; silikon
  bg силикон [silikon] ; silikon
  sr силикон [silikon] ; silikon
  az silikon ; silikon
  uz silikon ; silikon
  kk силикон [silikon] ; silikon
  fa سیلیکون [silikon] ; silikon
  ar سيليكون [sīlīkūn] ; silikon
  ur سلیکون [silīkon] ; silikon
@nötron shared_ancestor
  en neutron ; nötron
  fr neutron ; nötron
  de Neutron ; nötron
  it neutrone ; nötron
  es neutrón ; nötron
  ru нейтрон [neytron] ; nötron
  el νετρόνιο [netrónio] ; nötron
  ro neutron ; nötron
  hu neutron ; nötron
  pl neutron ; nötron
  bg неутрон [neutron] ; nötron
  sr неутрон [neutron] ; nötron
  az neytron ; nötron
  uz neytron ; nötron
  kk нейтрон [neytron] ; nötron
  fa نوترون [notron] ; nötron
  ar نيوترون [nyūtrūn] ; nötron
@reaktör shared_ancestor
  en reactor ; reaktör
  fr réacteur ; reaktör; jet motoru ; ff:Fransızcada réacteur ayrıca "jet motoru" demektir
  de Reaktor ; reaktör
  it reattore ; reaktör; jet motoru
  es reactor ; reaktör
  ru реактор [reaktor] ; reaktör
  ro reactor ; reaktör
  hu reaktor ; reaktör
  pl reaktor ; reaktör
  bg реактор [reaktor] ; reaktör
  sr реактор [reaktor] ; reaktör
  az reaktor ; reaktör
  uz reaktor ; reaktör
  kk реактор [reaktor] ; reaktör
  fa رآکتور [reʾāktor] ; reaktör
  ur ری ایکٹر [rī-ekṭar] ; reaktör
@türbin shared_ancestor
  en turbine ; türbin
  fr turbine ; türbin
  de Turbine ; türbin
  it turbina ; türbin
  es turbina ; türbin
  ru турбина [turbina] ; türbin
  el τουρμπίνα [tourbína] ; türbin
  ro turbină ; türbin
  hu turbina ; türbin
  pl turbina ; türbin
  bg турбина [turbina] ; türbin
  sr турбина [turbina] ; türbin
  az turbin ; türbin
  uz turbina ; türbin
  kk турбина [turbina] ; türbin
  fa توربین [turbin] ; türbin
  ar توربين [tūrbīn] ; türbin
  ur ٹربائن [ṭarbāʾin] ; türbin
@volt shared_ancestor
  en volt ; volt
  fr volt ; volt
  de Volt ; volt
  it volt ; volt
  es voltio ; volt
  ru вольт [vol't] ; volt
  el βολτ [volt] ; volt
  ro volt ; volt
  hu volt ; volt
  pl wolt ; volt
  bg волт [volt] ; volt
  sr волт [volt] ; volt
  az volt ; volt
  uz volt ; volt
  kk вольт [vol't] ; volt
  fa ولت [volt] ; volt
  ar فولت [fūlt] ; volt
  ur وولٹ [volṭ] ; volt
@amper shared_ancestor
  en ampere ; amper
  fr ampère ; amper
  de Ampere ; amper
  it ampere ; amper
  es amperio ; amper
  ru ампер [amper] ; amper
  el αμπέρ [ampér] ; amper
  ro amper ; amper
  hu amper ; amper
  pl amper ; amper
  bg ампер [amper] ; amper
  az amper ; amper
  uz amper ; amper
  kk ампер [amper] ; amper
  fa آمپر [āmper] ; amper
  ar أمبير [ʾambīr] ; amper
@tablet shared_ancestor
  en tablet ; tablet; hap
  fr tablette ; tablet; raf; çikolata kalıbı ; ff:Fransızcada tablette ayrıca "raf, çikolata kalıbı" demektir
  de Tablette ; hap ; ff:Almancada Tablette yalnız "hap" demektir; tablet bilgisayar için Tablet kullanılır
  it tavoletta ; küçük levha; tablet
  es tableta ; tablet; hap
  ru таблетка [tabletka] ; hap ; ff:Rusçada tabletka "hap" demektir; tablet bilgisayar için planşet kullanılır
  ro tabletă ; tablet; hap
  hu tabletta ; hap ; ff:Macarcada tabletta "hap" demektir
  pl tabletka ; hap ; ff:Lehçede tabletka "hap" anlamındadır
  bg таблетка [tabletka] ; hap ; ff:Bulgarcada tabletka "hap" demektir
  az tablet ; tablet
  fa تبلت [tablet] ; tablet
@sensör shared_ancestor
  en sensor ; algılayıcı
  fr senseur ; algılayıcı ; ff:Fransızcada daha çok capteur kullanılır; senseur İngilizce etkisiyle yaygınlaşmıştır
  de Sensor ; algılayıcı
  it sensore ; algılayıcı
  es sensor ; algılayıcı
  ru сенсор [sensor] ; algılayıcı; dokunmatik ; ff:Rusçada sensornyy "dokunmatik" (ekran) anlamında yaygındır
  ro senzor ; algılayıcı
  hu szenzor ; algılayıcı
  pl sensor ; algılayıcı
  bg сензор [senzor] ; algılayıcı
  sr сензор [senzor] ; algılayıcı
  az sensor ; algılayıcı
  uz sensor ; algılayıcı
  kk сенсор [sensor] ; algılayıcı
  fa سنسور [sensor] ; algılayıcı
  ur سینسر [sensar] ; algılayıcı
@modül shared_ancestor
  en module ; modül
  fr module ; modül
  de Modul ; modül
  it modulo ; modül; form ; ff:İtalyancada modulo ayrıca "başvuru formu" demektir
  es módulo ; modül
  ru модуль [modul'] ; modül
  ro modul ; modül
  hu modul ; modül
  pl moduł ; modül
  bg модул [modul] ; modül
  sr модул [modul] ; modül
  az modul ; modül
  uz modul ; modül
  kk модуль [modul'] ; modül
@norm shared_ancestor
  en norm ; norm
  fr norme ; norm; standart
  de Norm ; norm; standart
  it norma ; kural; norm
  es norma ; kural; norm
  ru норма [norma] ; norm; ölçü
  el νόρμα [nórma] ; norm
  ro normă ; norm
  hu norma ; norm
  pl norma ; norm
  bg норма [norma] ; norm
  sr норма [norma] ; norm
  az norma ; norm
  uz norma ; norm
  kk норма [norma] ; norm
@kontrol shared_ancestor
  en control ; denetim; kontrol
  fr contrôle ; denetim; kontrol
  de Kontrolle ; denetim; kontrol
  it controllo ; denetim; kontrol
  es control ; denetim; kontrol
  ru контроль [kontrol'] ; denetim; kontrol
  el κοντρόλ [kontról] ; kontrol
  ro control ; denetim; kontrol
  hu kontroll ; denetim; kontrol
  pl kontrola ; denetim; kontrol
  bg контрол [kontrol] ; denetim; kontrol
  sr контрола [kontrola] ; denetim; kontrol
  sq kontroll ; denetim; kontrol
  az kontrol ; denetim; kontrol
  uz kontrol ; denetim; kontrol
  kk контроль [kontrol'] ; denetim; kontrol
  fa کنترل [kontrol] ; denetim; kontrol
  ur کنٹرول [kanṭrol] ; denetim; kontrol
@pedal shared_ancestor
  en pedal ; pedal
  fr pédale ; pedal
  de Pedal ; pedal
  it pedale ; pedal
  es pedal ; pedal
  ru педаль [pedal'] ; pedal
  el πεντάλ [pentál] ; pedal
  ro pedală ; pedal
  hu pedál ; pedal
  pl pedał ; pedal ; ff:Lehçede pedał argoda "eşcinsel" için aşağılayıcı bir sözcüktür; dikkat ister
  bg педал [pedal] ; pedal
  sr педала [pedala] ; pedal
  az pedal ; pedal
  uz pedal ; pedal
  kk педаль [pedal'] ; pedal
  fa پدال [pedāl] ; pedal
  ur پیڈل [peḍal] ; pedal
@kalsiyum shared_ancestor
  en calcium ; kalsiyum
  fr calcium ; kalsiyum
  de Kalzium ; kalsiyum
  it calcio ; kalsiyum; futbol; tekme ; ff:İtalyancada calcio aynı zamanda "futbol" ve "tekme" demektir
  es calcio ; kalsiyum
  ru кальций [kal'tsiy] ; kalsiyum
  ro calciu ; kalsiyum
  hu kalcium ; kalsiyum
  bg калций [kaltsiy] ; kalsiyum
  sr калцијум [kalcijum] ; kalsiyum
  az kalsium ; kalsiyum
  uz kalsiy ; kalsiyum
  kk кальций [kal'tsiy] ; kalsiyum
  fa کلسیم [kalsiyom] ; kalsiyum
  ar كالسيوم [kālsiyūm] ; kalsiyum
  ur کیلشیم [kailşiyam] ; kalsiyum
@magnezyum shared_ancestor
  en magnesium ; magnezyum
  fr magnésium ; magnezyum
  de Magnesium ; magnezyum
  it magnesio ; magnezyum
  es magnesio ; magnezyum
  ru магний [magniy] ; magnezyum
  el μαγνήσιο [magnísio] ; magnezyum ; ff:Yunancada Magnisía yer adıyla (Manisa) bağ saydamdır
  ro magneziu ; magnezyum
  hu magnézium ; magnezyum
  pl magnez ; magnezyum
  bg магнезий [magneziy] ; magnezyum
  az maqnezium ; magnezyum
  uz magniy ; magnezyum
  kk магний [magniy] ; magnezyum
  fa منیزیم [menizyom] ; magnezyum
  ar مغنيسيوم [maġnīsiyūm] ; magnezyum
@torna shared_ancestor
  it tornio ; torna tezgâhı
  es torno ; torna; vinç
  fr tour ; torna; dönüş ; ff:Fransızcada tour "dönüş, tur, kule" anlamlarıyla çok anlamlıdır
  el τόρνος [tórnos] ; torna
  ru токарный [tokarnyy] ; tornaya ilişkin ; ff:Rusçada tokar' "tornacı" Eski Yunanca tórnos ile akraba değildir; yalnız anlamca denktir
@kristal shared_ancestor
  en crystal ; kristal
  fr cristal ; kristal
  de Kristall ; kristal
  it cristallo ; kristal
  es cristal ; kristal; cam ; ff:İspanyolcada cristal günlük dilde "cam" demektir
  ru кристалл [kristall] ; kristal
  el κρύσταλλο [krýstallo] ; kristal; buz ; ff:Eski Yunanca krýstallos "buz" demekti; bu anlam şiir dilinde sürer
  ro cristal ; kristal
  hu kristály ; kristal
  pl kryształ ; kristal
  bg кристал [kristal] ; kristal
  sr кристал [kristal] ; kristal
  az kristal ; kristal
  uz kristall ; kristal
  kk кристалл [kristall] ; kristal
  fa کریستال [keristāl] ; kristal
  ar كريستال [kristāl] ; kristal
@piksel shared_ancestor
  en pixel ; piksel
  fr pixel ; piksel
  de Pixel ; piksel
  it pixel ; piksel
  es píxel ; piksel
  ru пиксель [piksel'] ; piksel
  el πίξελ [píxel] ; piksel
  ro pixel ; piksel
  hu pixel ; piksel
  pl piksel ; piksel
  bg пиксел [piksel] ; piksel
  az piksel ; piksel
  uz piksel ; piksel
  kk пиксель [piksel'] ; piksel
  fa پیکسل [piksel] ; piksel
  ar بكسل [biksil] ; piksel
@modem shared_ancestor
  en modem ; modem
  fr modem ; modem
  de Modem ; modem
  it modem ; modem
  es módem ; modem
  ru модем [modem] ; modem
  el μόντεμ [móntem] ; modem
  ro modem ; modem
  hu modem ; modem
  pl modem ; modem
  bg модем [modem] ; modem
  az modem ; modem
  uz modem ; modem
  fa مودم [modem] ; modem
  ar مودم [mūdim] ; modem
@robot shared_ancestor
  en robot ; robot
  fr robot ; robot
  de Roboter ; robot
  it robot ; robot
  es robot ; robot
  ru робот [robot] ; robot
  el ρομπότ [robót] ; robot
  ro robot ; robot
  hu robot ; robot; angarya ; ff:Macarcada robot ayrıca "angarya, zorunlu iş" demektir; Çekçe robota "angarya" kökü de budur
  pl robot ; robot ; ff:Lehçede robota "iş" sözcüğüyle aynı Slav köküne dayanır
  bg робот [robot] ; robot
  sr робот [robot] ; robot
  az robot ; robot
  uz robot ; robot
  kk робот [robot] ; robot
  fa روبات [robāt] ; robot
  ar روبوت [rūbūt] ; robot
  ur روبوٹ [roboṭ] ; robot
@avatar shared_ancestor
  en avatar ; avatar
  fr avatar ; avatar; değişim ; ff:Fransızcada avatar "başkalaşım, serüven" anlamına da kaymıştır
  de Avatar ; avatar
  it avatar ; avatar
  es avatar ; avatar; iniş çıkış
  ru аватар [avatar] ; avatar
  el άβαταρ [ávatar] ; avatar
  ro avatar ; avatar
  hu avatár ; avatar
  pl awatar ; avatar
  ur اوتار [avtār] ; tanrının yeryüzüne inmiş biçimi ; ff:Urduca-Hintçe avtār Sanskritçe avatāra "iniş" kaynağıdır; dinî anlam önde gelir
@cebir into_turkish
  ar جبر [cabr] ; cebir; zorlama; kırık kavuşturma ; ff:Arapçada cabr "zorlama, kırığı kavuşturma" demektir; el-cebr adını Hârizmî'nin kitabı vermiştir
@cebir shared_ancestor
  en algebra ; cebir
  fr algèbre ; cebir
  de Algebra ; cebir
  it algebra ; cebir
  es álgebra ; cebir
  ru алгебра [algebra] ; cebir
  el άλγεβρα [álgevra] ; cebir
  ro algebră ; cebir
  hu algebra ; cebir
  pl algebra ; cebir
  bg алгебра [algebra] ; cebir
  sr алгебра [algebra] ; cebir
  az cəbr ; cebir
  uz algebra ; cebir ; ff:Özbekçe Rusça yoluyla Batı biçimini almıştır; Arapça biçim yalnız eski metinlerdedir
  kk алгебра [algebra] ; cebir
  fa جبر [cabr] ; cebir; zorlama
  ur الجبرا [alcabrā] ; cebir
@kimya into_turkish
  ar كيمياء [kīmiyāʾ] ; kimya
@kimya shared_ancestor
  en chemistry ; kimya
  fr chimie ; kimya
  de Chemie ; kimya
  it chimica ; kimya
  es química ; kimya
  ru химия [khimiya] ; kimya
  el χημεία [chimeía] ; kimya
  ro chimie ; kimya
  hu kémia ; kimya
  pl chemia ; kimya
  bg химия [khimiya] ; kimya
  sr хемија [hemija] ; kimya
  az kimya ; kimya
  uz kimyo ; kimya
  kk химия [khimiya] ; kimya
  ky химия [khimiya] ; kimya
  fa شیمی [şimi] ; kimya ; ff:Farsça Fransızca chimie biçimini almıştır; kīmiyā eski metinlerde "simya" demektir
  ur کیمیا [kīmiyā] ; kimya
@merkez into_turkish
  ar مركز [markaz] ; merkez
@merkez shared_ancestor
  fa مرکز [markaz] ; merkez
  ur مرکز [markaz] ; merkez
  az mərkəz ; merkez
  uz markaz ; merkez
  tk merkez ; merkez
@küre into_turkish
  ar كرة [kura] ; top; küre ; ff:Arapçada kura günlük dilde "top, futbol topu" demektir
@küre shared_ancestor
  fa کره [kore] ; küre
  ur کرہ [kura] ; küre
  az kürə ; küre
@zaviye into_turkish
  ar زاوية [zāwiya] ; köşe; açı; tekke ; ff:Arapçada zāwiya "köşe" ve "tekke" anlamlarını korur
@zaviye shared_ancestor
  fa زاویه [zāviye] ; açı; köşe
  ur زاویہ [zāviya] ; açı; bakış açısı
  az zaviyə ; köşe; açı
@cisim into_turkish
  ar جسم [cism] ; beden; cisim
@cisim shared_ancestor
  fa جسم [cesm] ; beden; cisim
  ur جسم [cism] ; beden ; ff:Urducada cism yalnız "beden, vücut" anlamındadır
  az cisim ; cisim
  uz jism ; cisim; beden
  tk jisim ; cisim
@hesap into_turkish
  ar حساب [ḥisāb] ; hesap
@hesap shared_ancestor
  fa حساب [hesāb] ; hesap
  ur حساب [ḥisāb] ; hesap
  az hesab ; hesap
  uz hisob ; hesap
  kk есеп [esep] ; hesap
  ky эсеп [esep] ; hesap
  tk hasap ; hesap
  sq hesap ; hesap
@mesafe into_turkish
  ar مسافة [masāfa] ; mesafe
@mesafe shared_ancestor
  fa مسافت [masāfat] ; mesafe
  ur مسافت [masāfat] ; mesafe; yolculuk ; ff:Urducada masāfat "yolculuk" anlamına da gelir
  az məsafə ; mesafe
  uz masofa ; mesafe
@satıh into_turkish
  ar سطح [saṭḥ] ; yüzey
@satıh shared_ancestor
  fa سطح [saṭḥ] ; yüzey; düzey
  ur سطح [satah] ; yüzey; düzey
  az səth ; yüzey
  uz sath ; yüzey
@sabit into_turkish
  ar ثابت [thābit] ; sabit; kanıtlanmış
@sabit shared_ancestor
  fa ثابت [sābet] ; sabit
  ur ثابت [sābit] ; kanıtlanmış ; ff:Urducada sābit önce "kanıtlanmış, ispatlı" demektir
  az sabit ; sabit
  uz sobit ; sabit
@nebat into_turkish
  ar نبات [nabāt] ; bitki
@nebat shared_ancestor
  fa نبات [nabāt] ; bitki; kristal şeker ; ff:Farsçada nabāt ayrıca "kristal şeker (nöbet şekeri)" demektir
  ur نبات [nabāt] ; bitki
  uz nabotot ; bitkiler
@felek into_turkish
  ar فلك [falak] ; gök katı; yörünge
@felek shared_ancestor
  fa فلک [falak] ; gök; felek
  ur فلک [falak] ; gök
  az fələk ; felek
  uz falak ; gök; felek
@kamer into_turkish
  ar قمر [qamar] ; ay
@kamer shared_ancestor
  fa قمر [qamar] ; ay; uydu ; ff:Farsçada qamar bugün daha çok "uydu" anlamında kullanılır
  ur قمر [qamar] ; ay
  az qəmər ; ay
@sema into_turkish
  ar سماء [samāʾ] ; gök
@sema shared_ancestor
  fa سما [samā] ; gök
  ur سما [samā] ; gök
  az səma ; gök
  uz samo ; gök
  he שמים [shamayim] ; gökler ; ff:İbranice şamayim aynı Sami kökten gelir; biçim çoğuldur
@şems into_turkish
  ar شمس [şams] ; güneş
@şems shared_ancestor
  fa شمس [şams] ; güneş
  ur شمس [şams] ; güneş
  az şəms ; güneş
  he שמש [şemeş] ; güneş ; ff:İbranice şemeş aynı Sami köktendir
@necm into_turkish
  ar نجم [nacm] ; yıldız
@necm shared_ancestor
  fa نجم [nacm] ; yıldız
  ur نجم [nacm] ; yıldız
  az nəcm ; yıldız
@unsur into_turkish
  ar عنصر [ʿunṣur] ; öğe; element
@unsur shared_ancestor
  fa عنصر [ʿonṣor] ; öğe; element
  ur عنصر [ʿunṣur] ; öğe; element
  az ünsür ; öğe
  uz unsur ; öğe
@cihaz into_turkish
  ar جهاز [cihāz] ; aygıt; donanım
@cihaz shared_ancestor
  fa جهاز [cahāz] ; çeyiz; donanım ; ff:Farsçada cahāz ayrıca "çeyiz" demektir
  ur جہاز [cahāz] ; gemi; uçak ; ff:Urducada cahāz "gemi, uçak" anlamına kaymıştır
  az cihaz ; aygıt
  uz jihoz ; donanım; mobilya ; ff:Özbekçede jihoz "ev eşyası, donanım" demektir
@tecrübe into_turkish
  ar تجربة [tacriba] ; deneme; deney
@tecrübe shared_ancestor
  fa تجربه [tacrobe] ; deneyim
  ur تجربہ [tajriba] ; deneyim; deney
  az təcrübə ; deneyim
  uz tajriba ; deneyim; deney
  kk тәжірибе [täjiribe] ; deneyim; uygulama
  ky тажрыйба [tacrıyba] ; deneyim
@hata into_turkish
  ar خطأ [ḫaṭaʾ] ; yanlış
@hata shared_ancestor
  fa خطا [ḫaṭā] ; yanlış
  ur خطا [ḫatā] ; yanlış; suç
  az xəta ; yanlış
  uz xato ; yanlış
  kk қате [qate] ; yanlış
  ky ката [kata] ; yanlış
  tk hata ; yanlış
@kayıt into_turkish
  ar قيد [qayd] ; bağ; zincir; kayıt ; ff:Arapçada qayd önce "bağ, zincir" demektir
@kayıt shared_ancestor
  fa قید [qeyd] ; bağ; kısıt ; ff:Farsçada qeyd "kısıt, koşul" anlamındadır
  ur قید [qaid] ; hapis ; ff:Urducada qaid "hapis, tutukluluk" demektir
  az qeyd ; kayıt; not
  uz qayd ; kayıt; not
@ayar into_turkish
  ar عيار [ʿiyār] ; ölçün; ayar
@ayar shared_ancestor
  fa عیار [ʿayār] ; ayar; saflık derecesi
  ur عیار [ʿayār] ; kurnaz ; ff:Urducada ʿayār "kurnaz, düzenbaz" anlamına kaymıştır
  az əyar ; ayar
@şekil into_turkish
  ar شكل [şakl] ; biçim
@şekil shared_ancestor
  fa شکل [şekl] ; biçim; şekil
  ur شکل [şakl] ; yüz; çehre ; ff:Urducada şakl "yüz, çehre" demektir
  az şəkil ; resim; fotoğraf ; ff:Azerbaycan Türkçesinde şəkil "resim, fotoğraf" anlamına kaymıştır
  uz shakl ; biçim
@vasıta into_turkish
  ar واسطة [wāsiṭa] ; aracı; araç
@vasıta shared_ancestor
  fa واسطه [vāseṭe] ; aracı
  ur واسطہ [vāsta] ; ilişki; sebep ; ff:Urducada vāsta "ilişki; uğruna" anlamında edat gibi kullanılır
  az vasitə ; araç
  uz vosita ; araç
@mizaç into_turkish
  ar مزاج [mizāc] ; karışım; ruh hâli ; ff:Arapçada mizāc "keyif, ruh hâli" anlamı öndedir
@mizaç shared_ancestor
  fa مزاج [mezāc] ; huy; mizaç
  ur مزاج [mizāj] ; huy; ruh hâli
  az mizac ; mizaç
@kaide into_turkish
  ar قاعدة [qāʿida] ; temel; kural; üs ; ff:Arapçada qāʿida "askerî üs" anlamını da taşır; El-Kaide adı buradandır
@kaide shared_ancestor
  fa قاعده [qāʿede] ; kural
  ur قاعدہ [qāʿida] ; kural; alfabe kitabı
  az qayda ; kural
  uz qoida ; kural
@nevi into_turkish
  ar نوع [nawʿ] ; tür
@nevi shared_ancestor
  fa نوع [nowʿ] ; tür
  ur نوع [nauʿ] ; tür
  az növ ; tür
@tasnif into_turkish
  ar تصنيف [taṣnīf] ; sınıflandırma; eser yazma
@tasnif shared_ancestor
  fa تصنیف [taṣnīf] ; şarkı sözü; beste ; ff:Farsçada taṣnīf "beste, şarkı" anlamına kaymıştır
  ur تصنیف [taṣnīf] ; eser yazma ; ff:Urducada taṣnīf "kitap yazma, telif" demektir
  az təsnif ; sınıflandırma
@mukaddime into_turkish
  ar مقدمة [muqaddima] ; giriş; ön söz
@mukaddime shared_ancestor
  fa مقدمه [moqaddame] ; giriş; ön söz
  ur مقدمہ [muqaddama] ; dava; ön söz ; ff:Urducada muqaddama "mahkeme davası" anlamı öndedir
  az müqəddimə ; giriş
  uz muqaddima ; giriş
@billur into_turkish
  ar بلور [ballūr] ; billur; kristal
@billur shared_ancestor
  fa بلور [bolūr] ; billur; kristal
  ur بلور [bilaur] ; billur
  az büllur ; billur
  uz billur ; billur
  el βήρυλλος [výryllos] ; beril taşı ; ff:Yunanca výryllos yalnız "beril" minerali için kullanılır
  en beryl ; beril
  fr béryl ; beril
  de Beryll ; beril
@neft into_turkish
  fa نفت [naft] ; petrol
@neft shared_ancestor
  az neft ; petrol
  uz neft ; petrol
  ru нефть [neft'] ; petrol
  el νάφθα [náftha] ; nafta
  en naphtha ; nafta
  de Naphtha ; nafta
  ar نفط [nafṭ] ; petrol
  hy նավթ [navt'] ; petrol
  ka ნავთი [navti] ; gaz yağı; petrol
@terazi into_turkish
  fa ترازو [tarāzū] ; terazi
@terazi shared_ancestor
  az tərəzi ; terazi
  uz tarozi ; terazi
  kk таразы [tarazy] ; terazi
  ky тараза [taraza] ; terazi
  tk terezi ; terazi
  ur ترازو [tarāzū] ; terazi
@terazi from_turkish
  bg теразия [teraziya] ; terazi
  sr теразије [terazije] ; terazi
  mk теразија [terazija] ; terazi
  sq terezi ; terazi
  ro terezie ; terazi
@kantar into_turkish
  ar قنطار [qinṭār] ; yüz okkalık ağırlık; kantar
@kantar shared_ancestor
  fa قنطار [qenṭār] ; kantar
  el καντάρι [kantári] ; kantar ; ff:Yunancada kantári hem "kantar" hem eski "yüz okkalık ağırlık" demektir
@kantar from_turkish
  bg кантар [kantar] ; kantar
  sr кантар [kantar] ; kantar
  mk кантар [kantar] ; kantar
  sq kandar ; kantar
  ro cântar ; kantar; tartı
@okka into_turkish
  ar أوقية [ūqiyya] ; okka; ons
@okka from_turkish
  bg ока [oka] ; okka
  sr ока [oka] ; okka
  mk ока [oka] ; okka
  el οκά [oká] ; okka
  ro oca ; okka
  sq okë ; okka
@dirhem into_turkish
  ar درهم [dirham] ; dirhem; para birimi
@dirhem shared_ancestor
  fa درهم [derham] ; dirhem
  ur درہم [dirham] ; dirhem
  az dirhəm ; dirhem
  el δράμι [drámi] ; dirhem ; ff:Yunanca drámi aynı Eski Yunanca drakhmḗ'den doğrudan gelir
  bg драм [dram] ; dirhem
  sr драм [dram] ; dirhem
  ro dram ; dirhem; azıcık ; ff:Rumencede dram "bir parça, azıcık" anlamına kaymıştır
@arşın shared_ancestor
  az arşın ; arşın
  kk аршын [arşyn] ; arşın
  uz arshin ; arşın
  tk arşyn ; arşın
@arşın from_turkish
  ru аршин [arshin] ; arşın
  uk аршин [arshyn] ; arşın
  bg аршин [arshin] ; arşın
  sr аршин [aršin] ; arşın
  mk аршин [arşin] ; arşın
  ro arșin ; arşın
  sq arshin ; arşın
@batman shared_ancestor
  az batman ; batman
  kk батпан [batpan] ; batman
  ky батман [batman] ; batman
  uz botmon ; batman
  tk batman ; batman
@batman from_turkish
  ru батман [batman] ; eski ağırlık ölçüsü
@çark into_turkish
  fa چرخ [çarḫ] ; tekerlek; çark
@çark shared_ancestor
  az çarx ; çark
  uz charx ; çark
  ur چرخ [carḫ] ; çark; tekerlek
  tk çarh ; çark
@çark from_turkish
  bg чарк [chark] ; çark
  mk чарк [çark] ; çark
  sq çark ; çark
@tunç from_turkish
  bg тунч [tunch] ; tunç
  sr туч [tuč] ; tunç
  mk тунч [tunç] ; tunç
  sq tunxh ; tunç
  ro tuci ; dökme demir ; ff:Rumencede tuci "dökme demir" anlamına kaymıştır
@tunç shared_ancestor
  az tunc ; tunç
@kehribar into_turkish
  fa کهربا [kahrubā] ; kehribar ; ff:Farsça kāh-rubā "saman kapan": kehribarın sürtününce saman çekmesine gönderme
@kehribar shared_ancestor
  az kəhrəba ; kehribar
  ur کہربا [kahrubā] ; kehribar
  ar كهرباء [kahrabāʾ] ; elektrik ; ff:Arapçada kahrabāʾ bugün "elektrik" demektir; kehribar taşı için de kullanılır
@kehribar from_turkish
  bg кехлибар [kekhlibar] ; kehribar
  sr ћилибар [ćilibar] ; kehribar
  mk ќилибар [kjilibar] ; kehribar
  sq qelibar ; kehribar
  ro chihlimbar ; kehribar
  el κεχριμπάρι [kechrimbári] ; kehribar
@katran into_turkish
  ar قطران [qaṭrān] ; katran
@katran shared_ancestor
  fa قطران [qaṭrān] ; katran
  az qatran ; katran
  uz qatron ; katran
@katran from_turkish
  bg катран [katran] ; katran
  sr катран [katran] ; katran
  mk катран [katran] ; katran
  sq katran ; katran
  ro catran ; katran
  el κατράμι [katrámi] ; katran
  hu kátrány ; katran
@kireç from_turkish
  bg киреч [kirech] ; kireç
  sr креч [kreč] ; kireç
  mk креч [kreç] ; kireç
@nişadır into_turkish
  fa نوشادر [nūşādur] ; nişadır
@nişadır shared_ancestor
  ar نشادر [nuşādir] ; nişadır
@nişadır from_turkish
  bg нишадър [nishadar] ; nişadır
  sr нишадор [nišador] ; nişadır
  mk нишадор [nişador] ; nişadır
  el νισαντίρι [nisantíri] ; nişadır
  ru нашатырь [nashatyr'] ; nişadır
@elmas into_turkish
  fa الماس [almās] ; elmas
@elmas shared_ancestor
  ar ألماس [almās] ; elmas
  ur الماس [almās] ; elmas
  az almaz ; elmas
  uz olmos ; elmas
  kk алмас [almas] ; elmas
  ky алмаз [almaz] ; elmas
  el αδάμας [adámas] ; elmas; yenilmez ; ff:Eski Yunanca adámas "yenilmez" sıfatıdır; diamánti buradan türer
@elmas from_turkish
  ru алмаз [almaz] ; elmas
  bg елмаз [elmaz] ; elmas
  mk елмаз [elmaz] ; elmas
  sq elmaz ; elmas
@zümrüt into_turkish
  fa زمرد [zomorrod] ; zümrüt
@zümrüt shared_ancestor
  ar زمرد [zumurrud] ; zümrüt
  ur زمرد [zumurrud] ; zümrüt
  az zümrüd ; zümrüt
  uz zumrad ; zümrüt
  el σμαράγδι [smarágdi] ; zümrüt
  en emerald ; zümrüt
  fr émeraude ; zümrüt
@zümrüt from_turkish
  ru изумруд [izumrud] ; zümrüt
@firuze into_turkish
  fa فیروزه [fīrūze] ; firuze
@firuze shared_ancestor
  ar فيروز [fayrūz] ; firuze
  ur فیروزہ [fīroza] ; firuze
  az firuzə ; firuze
  uz feruza ; firuze
  ru бирюза [biryuza] ; firuze
  en turquoise ; firuze ; ff:Batı dillerinde "Türk taşı" adıyla anılır; Farsça kökle akraba değildir, yalnız anlamdaştır
  fr turquoise ; firuze ; ff:Fransızca turquoise "Türk (taşı)" demektir
@inci shared_ancestor
  az inci ; inci
  kk інжу [injü] ; inci
  tk hünji ; inci
@inci from_turkish
  ru жемчуг [zhemchug] ; inci ; ff:Eski Türkçe yinçü biçiminden; Rusça j- ile başlar
  hu gyöngy ; inci; boncuk ; ff:Macarca gyöngy Eski Türkçe yinçü'den alınmıştır
@kükürt into_turkish
  fa گوگرد [gūgerd] ; kükürt
@kükürt shared_ancestor
  az kükürd ; kükürt
  kk күкірт [kükirt] ; kükürt
  ky күкүрт [kükürt] ; kükürt
  tk kükürt ; kükürt
  uz oltingugurt ; kükürt ; ff:Özbekçe oltingugurt "altın kükürt" bileşiğidir
@cıva into_turkish
  fa جیوه [jīve] ; cıva
@cıva shared_ancestor
  az civə ; cıva
  uz simob ; cıva ; ff:Özbekçe simob Farsça sīmāb "gümüş su" sözcüğüdür; cıva ile anlamdaş, biçimce ayrıdır
@kalay shared_ancestor
  az qalay ; kalay
  kk қалайы [qalayy] ; kalay
  ky калай [kalay] ; kalay
  uz qalay ; kalay
  tk galaýy ; kalay
@kalay from_turkish
  bg калай [kalay] ; kalay
  sr калај [kalaj] ; kalay
  mk калај [kalaj] ; kalay
  sq kallaj ; kalay
  el καλάι [kalái] ; kalay
@makara into_turkish
  el μακαράς [makarás] ; makara
@makara from_turkish
  bg макара [makara] ; makara
  sr макара [makara] ; makara
  mk макара [makara] ; makara
  sq makara ; makara
  ro macara ; vinç ; ff:Rumencede macara "vinç" anlamına kaymıştır
@makara shared_ancestor
  az makara ; makara
@ölçmek shared_ancestor
  az ölçmək ; ölçmek
  kk өлшеу [ölşeu] ; ölçmek
  uz oʻlchamoq ; ölçmek
  ky өлчөө [ölçöö] ; ölçmek
  tk ölçemek ; ölçmek
@sayı shared_ancestor
  az say ; sayı
  kk сан [san] ; sayı
  uz son ; sayı
  ky сан [san] ; sayı
  tk san ; sayı
@yıldız shared_ancestor
  az ulduz ; yıldız
  kk жұлдыз [juldyz] ; yıldız
  uz yulduz ; yıldız
  ky жылдыз [cıldız] ; yıldız
  tk ýyldyz ; yıldız
@bilim shared_ancestor
  az bilim ; bilim ; ff:Azerbaycan Türkçesinde bilim seyrektir; yaygın sözcük elm'dir
  kk білім [bilim] ; bilgi; eğitim ; ff:Kazakçada bilim "eğitim, bilgi" demektir; bilim için ğılım kullanılır
  uz bilim ; bilgi ; ff:Özbekçede bilim "bilgi" demektir; bilim için fan kullanılır
  ky билим ; bilgi; eğitim ; ff:Kırgızcada bilim "eğitim" anlamındadır
  tk bilim ; bilgi ; ff:Türkmencede bilim "bilgi" demektir; bilim için ylym kullanılır
@katı shared_ancestor
  az qatı ; katı; koyu
  kk қатты [qatty] ; sert; çok ; ff:Kazakçada qatty "sert" yanında "çok, şiddetle" zarfıdır
  uz qattiq ; sert; katı
  ky катуу [katuu] ; sert; şiddetli
  tk gaty ; sert; çok
@süzmek shared_ancestor
  az süzmək ; süzmek
  kk сүзу [süzu] ; süzmek
  uz suzmoq ; süzmek; yüzmek ; ff:Özbekçede suzmoq hem "süzmek" hem "yüzmek" demektir
  ky сүзүү [süzüü] ; süzmek; boynuzlamak ; ff:Kırgızcada süzüü ayrıca "boynuzla vurmak" anlamındadır
  tk süzmek ; süzmek
@ayırmak shared_ancestor
  az ayırmaq ; ayırmak
  kk айыру [ayyru] ; ayırmak
  uz ajratmoq ; ayırmak
  ky айыруу [ayıruu] ; ayırmak
  tk aýyrmak ; ayırmak
@saçmak shared_ancestor
  az saçmaq ; saçmak
  kk шашу [şaşu] ; saçmak; düğünde şeker saçma ; ff:Kazakçada şaşu ayrıca düğünde şeker saçma törenidir
  uz sochmoq ; saçmak
  ky чачуу [çaçuu] ; saçmak
  tk saçmak ; saçmak
@soğumak shared_ancestor
  az soyumaq ; soğumak
  kk суу [suu] ; soğumak ; ff:Kazakçada suu "su" sözcüğüyle yazımı çakışır
  uz sovimoq ; soğumak
  ky суу [suu] ; soğumak
  tk sowamak ; soğumak
@titremek shared_ancestor
  az titrəmək ; titremek
  uz titramoq ; titremek
  ky титирөө [titiröö] ; titremek
  tk titremek ; titremek
@tartmak shared_ancestor
  az dartmaq ; çekmek ; ff:Azerbaycan Türkçesinde dartmaq "çekmek" demektir; tartmak için çəkmək kullanılır
  kk тарту [tartu] ; çekmek; tartmak ; ff:Kazakçada tartu önce "çekmek" demektir
  uz tortmoq ; çekmek; tartmak
  ky тартуу [tartuu] ; çekmek; tartmak
  tk dartmak ; çekmek
@damla shared_ancestor
  az damla ; damla
  kk тамшы [tamşy] ; damla
  uz tomchi ; damla
  ky тамчы [tamçı] ; damla
  tk damja ; damla
@alaca shared_ancestor
  az alaca ; alaca
  kk ала [ala] ; alaca
  uz ola ; alaca
  ky ала [ala] ; alaca
  tk ala ; alaca
@körük shared_ancestor
  az körük ; körük
  kk көрік [körik] ; körük
  ky көөрүк [köörük] ; körük
  tk körük ; körük
@kayış shared_ancestor
  az qayış ; kayış
  kk қайыс [qayys] ; kayış
  uz qayish ; kayış
  ky кайыш [kayış] ; kayış
  tk gaýyş ; kayış
@artmak shared_ancestor
  az artmaq ; artmak
  kk арту [artu] ; artmak
  uz ortmoq ; artmak
  ky артуу [artuu] ; artmak
  tk artmak ; artmak
@itmek shared_ancestor
  az itələmək ; itmek
  kk итеру [iteru] ; itmek
  uz itarmoq ; itmek
  ky итерүү [iterüü] ; itmek
  tk itmek ; itmek
@ısı shared_ancestor
  az isti ; sıcak ; ff:Azerbaycan Türkçesinde isti "sıcak" sıfatıdır
  kk ыстық [ystyq] ; sıcak ; ff:Kazakçada ystyq "sıcak" sıfatıdır; ısı için jılu kullanılır
  uz issiq ; sıcak ; ff:Özbekçede issiq "sıcak" sıfatıdır
  ky ысык [ısık] ; sıcak ; ff:Kırgızcada ısık "sıcak" demektir; Issık Göl adı da buradandır
  tk yssy ; sıcak ; ff:Türkmencede yssy "sıcak" sıfatıdır
@boy shared_ancestor
  az boy ; boy; uzunluk
  kk бой [boy] ; boy; gövde ; ff:Kazakçada boy ayrıca "gövde, beden" ve "kendi" (öz boyı) anlamlarındadır
  uz boʻy ; boy
  ky бой [boy] ; boy; gövde
  tk boý ; boy
@gök shared_ancestor
  az göy ; gök; mavi ; ff:Azerbaycan Türkçesinde göy ayrıca "mavi" ve "yeşillik" anlamındadır
  kk көк [kök] ; gök; mavi ; ff:Kazakçada kök hem "gök" hem "mavi, yeşil" demektir
  uz koʻk ; gök; mavi
  ky көк [kök] ; gök; mavi
  tk gök ; gök; mavi
"""
