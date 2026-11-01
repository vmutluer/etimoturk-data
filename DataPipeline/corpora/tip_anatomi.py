# -*- coding: utf-8 -*-
"""Korpus 6 — Tıp ve anatomi: beden bölümleri (Öz Türkçe), hastalık ve sağaltım terimleri (Arapça),
modern tıp sözcükleri (Fransızca yoluyla Yunanca/Latince kökler)."""

WORDS = r"""
# --- Beden: Öz Türkçe anatomi adları -------------------------------------------------
kafatası|n|tr|kafa tası|baş kemiği|TDK||
omur|n|tr|omurtka|bel kemiği halkası|DLT|*omur|
omurga|n|tr|omurga|sırt kemiği dizisi|DD|*omur|
omurilik|n|tr|omurilik|omurga içindeki sinir|DD|*omur|
diz|n|tr|tiz|bacak eklemi|ORH||
dirsek|n|tr|tirsgek|kol eklemi|DLT||
bilek|n|tr|bilek|el ile kol arası|DLT||
tırnak|n|tr|tırŋak|parmak ucu boynuzsu yapı|DLT||
kirpik|n|tr|kirpik|göz kapağı kılı|DLT||
kaş|n|tr|kaş|göz üstü kıllı yay|DLT||
dudak|n|tr|dudak|ağız kenarı|EAT||
damak|n|tr|tamgak|ağız tavanı|DLT||
gırtlak|n|tr|kırtlak|ses yolu|EAT||
bağırsak|n|tr|bagırsuk|sindirim borusu|DLT|*bağır|
bağır|n|tr|bagır|karaciğer; göğüs|ORH|*bağır|
bağırmak|v|tr|bagır-|yüksek sesle seslenmek|DLT|*bağır|
böbrek|n|tr|bögrek|idrar süzen organ|DLT|*böl-|
dalak|n|tr|talak|karın içi organ|DLT||
karaciğer|n|tr|kara cigar|kan süzen büyük organ|OSM||
akciğer|n|tr|ak cigar|solunum organı|OSM||
ciğer|n|fa|cigar|iç organ|EAT||
kemik|n|tr|kemük|iskelet parçası|CC||
kıkırdak|n|tr|kıkırdak|esnek doku|TDK||
eklem|n|tr|eklem|kemiklerin birleştiği yer|DD|*ek-|
sinir|n|tr|siŋir|kiriş; sinir|DLT||
damar|n|tr|tamar|kan yolu|DLT||
kan|n|tr|kan|damar sıvısı|ORH||
ter|n|tr|ter|deri sıvısı|DLT||
tükürük|n|tr|tükrük|ağız sıvısı|DLT||
nabız|n|ar|nabḏ|atış|OSM|N-B-D|
nabzetmek|v|ar|nabḏ|atmak (damar)|OSM19|N-B-D|
beyin|n|tr|beŋi|baş içi organ|DLT||
yürek|n|tr|yürek|kalp; cesaret|ORH||
göğüs|n|tr|kögüz|döş|DLT||
bel|n|tr|bél|gövde ortası|DLT||
kalça|n|tr|kalça|but üstü|OSM||
topuk|n|tr|topık|ayak arkası|DLT|*top-|
avuç|n|tr|adut|el içi|DLT||
yumruk|n|tr|yudruk|sıkılmış el|DLT||
kol|n|tr|kol|üst uzuv|ORH||
bacak|n|tr|bacak|alt uzuv|EAT||
boyun|n|tr|boyın|baş ile gövde arası|ORH||
ense|n|fa|ense|boyun arkası|EAT||
alın|n|tr|alın|yüzün üst kısmı|DLT||
yanak|n|tr|yaŋak|yüz yanı|DLT||
çene|n|fa|çāne|alt yüz kemiği|EAT||
şakak|n|tr?|şakak|göz ile kulak arası|OSM||
gaga|n|tr|kaka|kuş ağzı|OSM||
# --- Sağlık ve hastalık: Arapça / Farsça ----------------------------------------------
tıp|n|ar|ṭibb|sağaltma bilgisi|EAT|T-B-B|
tabip|n|ar|ṭabīb|sağaltan|EAT|T-B-B|
tababet|n|ar|ṭabāba|hekimlik|OSM|T-B-B|
şifa|n|ar|şifāʾ|iyileşme|EAT|Ş-F-Y|
şifahane|n|ar|şifāʾ-ḫāne|hastane|OSM|Ş-F-Y|ar:şifāʾ>fa:şifā-ḫāne>tr:şifahane
hastane|n|fa|ḫaste-ḫāne|hastalar evi|OSM19|-hāne|
eczane|n|ar|aczāʾ-ḫāne|ilaçlar evi|OSM19|-hāne|ar:aczāʾ>fa:aczā-ḫāne>tr:eczane
ecza|n|ar|aczāʾ|parçalar; ilaç maddeleri|OSM|C-Z-A|
cüz|n|ar|cuzʾ|parça|EAT|C-Z-A|
cüzdan|n|fa|cuz-dān|parça kabı|OSM|C-Z-A|ar:cuzʾ>fa:cuz-dān>tr:cüzdan
hap|n|ar|ḥabb|tane|OSM||
merhem|n|ar|marham|yara ilacı|EAT||
macun|n|ar|maʿcūn|yoğrulmuş|EAT||
tedavi|n|ar|tadāwī|sağaltım|OSM|D-W-Y|
deva|n|ar|dawāʾ|ilaç|EAT|D-W-Y|
muayene|n|ar|muʿāyana|gözle inceleme|OSM19|A-Y-N|
ayna|n|fa|āyīne|yansıtan yüzey|EAT||
ayan|adj|ar|ʿayān|açık, belli|EAT|A-Y-N|
teşhis|n|ar|taşḫīṣ|tanılama|OSM19|Ş-H-S|
şahıs|n|ar|şaḫṣ|kişi|EAT|Ş-H-S|
şahsiyet|n|ar|şaḫṣiyya|kişilik|OSM19|Ş-H-S|
ameliyat|n|ar|ʿamaliyyāt|işlemler|OSM19|A-M-L|
veba|n|ar|wabāʾ|salgın hastalık|EAT||
humma|n|ar|ḥummā|ateşli hastalık|EAT|H-M-M|
hamam|n|ar|ḥammām|ısıtılan yıkanma yeri|EAT|H-M-M|
sıtma|n|tr|ısıtma|ateş yapan hastalık|EAT||
verem|n|ar|waram|şişlik|EAT|W-R-M|
tümör|n|fr|tumeur|şişlik|MOD||la:tumor>fr:tumeur>tr:tümör
nezle|n|ar|nazla|inme (burundan)|OSM||
felç|n|ar|falc|yarım inme|OSM||
sara|n|ar|ṣarʿ|düşme hastalığı|EAT||
kanser|n|fr|cancer|yengeç; ur|CUM||la:cancer>fr:cancer>tr:kanser
romatizma|n|fr|rhumatisme|akıntı hastalığı|OSM19||grc:rheûma>la:rheumatismus>fr:rhumatisme>tr:romatizma
zatürre|n|ar|ẕātu'r-riʾa|akciğer hastalığı|OSM||
iltihap|n|ar|iltihāb|alevlenme|OSM|L-H-B|
alev|n|fa|alāv|yalım|EAT||
öksürük|n|tr|öksürük|solunum tepkisi|DLT||
öksürmek|v|tr|öksür-|öksürmek|DLT||
hapşırmak|v|tr|hapşur-|aksırmak|OSM||
aksırmak|v|tr|asur-|hapşırmak|DLT||
ağrı|n|tr|agrı|sızı|DLT|*ağır|
sancı|n|tr|sançıg|batma ağrısı|DLT||
sızı|n|tr|sızı|hafif ağrı|OSM||
yara|n|tr|yara|doku zedelenmesi|DLT||
bere|n|tr|bere|çürük|OSM||
çürük|adj|tr|çürük|bozulmuş|DLT||
kırık|n|tr|kırık|kırılmış yer|DLT|*kır-|
çıkık|n|tr|çıkık|yerinden çıkmış eklem|OSM|*çık-|
burkulma|n|tr|burk-|eklem zorlanması|TDK||
morluk|n|hy|mor|ezik izi|TDK||
kabuk|n|tr|kabuk|dış örtü|DLT|*kap-|
kaşıntı|n|tr|kaşı-|kaşınma duygusu|TDK||
kaşınmak|v|tr|kaşı-|deriyi tırmalamak|DLT||
sağlık|n|tr|sag|esenlik|DLT|*sağ|
sağ|adj|tr|sag|canlı; sağlam|ORH|*sağ|
sağlam|adj|tr|saglam|dayanıklı|EAT|*sağ|
sağalmak|v|tr|sagal-|iyileşmek|DLT|*sağ|
iyileşmek|v|tr|edgü|sağlığa kavuşmak|TDK||
hasta|adj|fa|ḫaste|yaralı; hasta|EAT||
rahatsız|adj|ar|rāḥa|huzursuz|OSM19|R-W-H|
rahat|n|ar|rāḥa|dinginlik|EAT|R-W-H|
istirahat|n|ar|istirāḥa|dinlenme|OSM|R-W-H|
ruh|n|ar|rūḥ|can, soluk|EAT|R-W-H|
ruhsal|adj|ar|rūḥ|ruha ilişkin|TDK|R-W-H|
ruhani|adj|ar|rūḥānī|manevi|OSM|R-W-H|
reyhan|n|ar|rayḥān|fesleğen|EAT|R-W-H|
afiyet|n|ar|ʿāfiya|sağlık|EAT||
sıhhat|n|ar|ṣiḥḥa|sağlık|EAT|S-H-H|
sahih|adj|ar|ṣaḥīḥ|doğru, sağlam|EAT|S-H-H|
tashih|n|ar|taṣḥīḥ|düzeltme|OSM|S-H-H|
sıhhi|adj|ar|ṣiḥḥī|sağlığa ilişkin|OSM19|S-H-H|
hemşire|n|fa|hem-şīre|süt kardeşi|OSM19||
ebe|n|tr|ebe|doğum yardımcısı|DLT||
eczacı|n|ar|aczāʾ|ilaç yapan|OSM19|C-Z-A|
# --- Modern tıp: Fransızca yoluyla Yunanca / Latince -------------------------------
anatomi|n|fr|anatomie|kesip ayırma|OSM19|tomē|grc:anatomḕ>la:anatomia>fr:anatomie>tr:anatomi
atom|n|fr|atome|bölünmez|OSM19|tomē|grc:átomos>fr:atome>tr:atom
tomografi|n|fr|tomographie|kesit yazımı|MOD|tomē|
refleks|n|fr|réflexe|geri bükülen; kendiliğinden yanıt|CUM|flectere|la:reflexus>fr:réflexe>tr:refleks
refleksif|adj|fr|réflexif|refleks niteliğinde|MOD|flectere|la:reflexus>fr:réflexif>tr:refleksif
fleksiyon|n|fr|flexion|bükülme|MOD|flectere|la:flexio>fr:flexion>tr:fleksiyon
fleksibl|adj|fr|flexible|bükülebilir, esnek|MOD|flectere|la:flexibilis>fr:flexible>tr:fleksibl
fizyoloji|n|fr|physiologie|doğa bilgisi|OSM19|logos|grc:physiología>fr:physiologie>tr:fizyoloji
patoloji|n|fr|pathologie|hastalık bilgisi|CUM|pathos|
patolojik|adj|fr|pathologique|hastalıklı|MOD|pathos|
psikopat|n|fr|psychopathe|ruh hastası|MOD|pathos|
sempati|n|fr|sympathie|birlikte duyma|CUM|pathos|grc:sympátheia>fr:sympathie>tr:sempati
antipati|n|fr|antipathie|karşı duygu|CUM|pathos|
empati|n|fr|empathie|içten duyma|MOD|pathos|
apati|n|fr|apathie|duygusuzluk|MOD|pathos|
anestezi|n|fr|anesthésie|duyumsuzluk|CUM|aisthēsis|grc:anaisthēsía>fr:anesthésie>tr:anestezi
estetik|n|fr|esthétique|duyuma ilişkin|CUM|aisthēsis|grc:aisthētikós>fr:esthétique>tr:estetik
estet|n|fr|esthète|güzellik düşkünü|MOD|aisthēsis|
antibiyotik|n|fr|antibiotique|yaşama karşı|MOD|bios|
biyoloji|n|fr|biologie|yaşam bilgisi|CUM|bios|grc:bíos>fr:biologie>tr:biyoloji
biyografi|n|fr|biographie|yaşam yazısı|CUM|bios|
biyopsi|n|fr|biopsie|canlı dokuya bakma|MOD|bios|
mikrobiyoloji|n|fr|microbiologie|küçük canlılar bilgisi|MOD|bios|
mikrop|n|fr|microbe|küçük canlı|OSM19|bios|
mikroskop|n|fr|microscope|küçüğü gören|OSM19|skopein|
amfibi|adj|fr|amphibie|iki yaşamlı|MOD|bios|
aşı|n|tr|aşı|aşılama maddesi|OSM||
virüs|n|fr|virus|zehir|CUM||la:virus>fr:virus>tr:virüs
bakteri|n|fr|bactérie|çubuk|CUM||grc:baktḕrion>fr:bactérie>tr:bakteri
enfeksiyon|n|fr|infection|bulaşma|CUM||la:infectio>fr:infection>tr:enfeksiyon
klinik|n|fr|clinique|yatağa ilişkin|CUM||grc:klinikḕ>fr:clinique>tr:klinik
poliklinik|n|fr|polyclinique|çok bölümlü klinik|CUM||
röntgen|n|de|Röntgen|fizikçi W. C. Röntgen'in adı|CUM||
ultrason|n|fr|ultrason|ses ötesi|MOD|sonus|
sonar|n|en|sonar|ses yoluyla yön bulma|MOD|sonus|
sone|n|fr|sonnet|küçük ezgi|OSM19|sonus|
sendrom|n|fr|syndrome|birlikte koşma|MOD||grc:syndromḕ>fr:syndrome>tr:sendrom
alerji|n|fr|allergie|başka etkinlik|MOD|ergon|grc:állos+érgon>fr:allergie>tr:alerji
enerji|n|fr|énergie|iş gücü|OSM19|ergon|grc:enérgeia>fr:énergie>tr:enerji
ergonomi|n|fr|ergonomie|iş düzeni|MOD|ergon|
cerrahi|n|ar|carrāḥī|elle sağaltım|OSM19|C-R-H|
astım|n|fr|asthme|soluk darlığı|CUM||grc:ásthma>fr:asthme>tr:astım
diyabet|n|fr|diabète|akıp geçen|CUM||grc:diabḕtēs>fr:diabète>tr:diyabet
kolesterol|n|fr|cholestérol|safra katısı|MOD||
vitamin|n|fr|vitamine|yaşam amini|CUM||la:vita>fr:vitamine>tr:vitamin
protein|n|fr|protéine|birinci sırada|CUM||grc:prôtos>fr:protéine>tr:protein
hormon|n|fr|hormone|harekete geçiren|CUM||grc:hormôn>fr:hormone>tr:hormon
enzim|n|fr|enzyme|mayada|MOD||
hücre|n|ar|ḥucra|oda|EAT|Ḥ-C-R|
doku|n|tr|doku|dokunmuş yapı|DD|*doku-|
dokumak|v|tr|tokı-|iplikleri örmek|DLT|*doku-|
dokuma|n|tr|tokı-|dokunmuş kumaş|OSM|*doku-|
dokunmak|v|tr|tokın-|değmek|DLT|*doku-|
organ|n|fr|organe|araç|OSM19|ergon|grc:órganon>la:organum>fr:organe>tr:organ
organizma|n|fr|organisme|canlı yapı|CUM|ergon|
kromozom|n|fr|chromosome|renkli cisim|MOD|khrōma|
krom|n|fr|chrome|renk|OSM19|khrōma|
kromatik|adj|fr|chromatique|renkli|MOD|khrōma|
gen|n|fr|gène|doğuran|MOD|genus|
genetik|n|fr|génétique|soya ilişkin|MOD|genus|
embriyo|n|fr|embryon|içte büyüyen|MOD||grc:émbryon>fr:embryon>tr:embriyo
plasenta|n|fr|placenta|yassı çörek|MOD||
rahim|n|ar|raḥim|döl yatağı|EAT|R-H-M|
hamile|adj|ar|ḥāmila|yük taşıyan|OSM|H-M-L|
gebe|adj|tr|kebe|hamile|DLT||
sezaryen|n|fr|césarienne|Sezar'a ilişkin|MOD||
dermatoloji|n|fr|dermatologie|deri bilgisi|MOD|derma|
dermatolog|n|fr|dermatologue|deri hekimi|MOD|derma|
epidermis|n|fr|épiderme|üst deri|MOD|derma|
kardiyoloji|n|fr|cardiologie|yürek bilgisi|MOD|kardia|
kardiyolog|n|fr|cardiologue|yürek hekimi|MOD|kardia|
kardiyak|adj|fr|cardiaque|yüreğe ilişkin|MOD|kardia|
elektrokardiyogram|n|fr|électrocardiogramme|yürek akım yazımı|MOD|kardia|
nöroloji|n|fr|neurologie|sinir bilgisi|MOD|neuron|
nöron|n|fr|neurone|sinir hücresi|MOD|neuron|
nevroz|n|fr|névrose|sinir bozukluğu|CUM|neuron|
nevralji|n|fr|névralgie|sinir ağrısı|CUM|neuron|
psikoloji|n|fr|psychologie|ruh bilgisi|OSM19|psykhe|grc:psykhḕ>fr:psychologie>tr:psikoloji
psikiyatri|n|fr|psychiatrie|ruh hekimliği|CUM|psykhe|
psikolog|n|fr|psychologue|ruh bilimci|CUM|psykhe|
psişik|adj|fr|psychique|ruhsal|MOD|psykhe|
hematoloji|n|fr|hématologie|kan bilgisi|MOD|haima|
anemi|n|fr|anémie|kansızlık|CUM|haima|
lösemi|n|fr|leucémie|ak kan|MOD|haima|
hemoglobin|n|fr|hémoglobine|kan yuvarı|MOD|haima|
hemoroid|n|fr|hémorroïde|kan akıntısı|MOD|haima|
gastrit|n|fr|gastrite|mide yangısı|MOD|gaster|
gastronomi|n|fr|gastronomie|mide yasası|MOD|gaster|
gastroenteroloji|n|fr|gastro-entérologie|mide bağırsak bilgisi|MOD|gaster|
osteoporoz|n|fr|ostéoporose|kemik gözenekliliği|MOD|osteon|
osteopati|n|fr|ostéopathie|kemik hastalığı|MOD|osteon|
ortopedi|n|fr|orthopédie|çocuğu düzeltme|CUM|orthos|
ortodonti|n|fr|orthodontie|diş düzeltme|MOD|orthos|
ortodoks|adj|fr|orthodoxe|doğru inançlı|OSM19|orthos|grc:orthódoxos>fr:orthodoxe>tr:ortodoks
ortografi|n|fr|orthographe|doğru yazım|CUM|orthos|
dental|adj|fr|dental|dişe ilişkin|MOD||la:dens>fr:dental>tr:dental
oftalmoloji|n|fr|ophtalmologie|göz bilgisi|MOD||
optik|n|fr|optique|görmeye ilişkin|OSM19||grc:optikós>fr:optique>tr:optik
pediatri|n|fr|pédiatrie|çocuk hekimliği|MOD|pais|
pedagoji|n|fr|pédagogie|çocuk yetiştirme|CUM|pais|
pedagog|n|fr|pédagogue|çocuk eğitmeni|CUM|pais|
ansiklopedi|n|fr|encyclopédie|çember eğitim|OSM19|pais|
onkoloji|n|fr|oncologie|ur bilgisi|MOD||
üroloji|n|fr|urologie|idrar bilgisi|MOD||
jinekoloji|n|fr|gynécologie|kadın bilgisi|MOD||
morfin|n|fr|morphine|uyku tanrısı Morpheus'tan|OSM19||
afyon|n|ar|afyūn|haşhaş özü|EAT||grc:ópion>ar:afyūn>tr:afyon
haşhaş|n|ar|ḫaşḫāş|afyon bitkisi|EAT||
kına|n|ar|ḥinnāʾ|boya bitkisi|EAT||
kinin|n|fr|quinine|kınakına özü|OSM19||
iyot|n|fr|iode|menekşe rengi|OSM19||grc:iṑdēs>fr:iode>tr:iyot
aspirin|n|de|Aspirin|ticari ad|CUM||
penisilin|n|en|penicillin|fırça küfü|MOD||la:penicillum>en:penicillin>tr:penisilin
ambulans|n|fr|ambulance|gezici hastane|CUM||la:ambulare>fr:ambulance>tr:ambulans
reçete|n|it|ricetta|alınan şey|OSM19||la:recepta>it:ricetta>tr:reçete
termometre|n|fr|thermomètre|ısı ölçer|OSM19|metron|
termal|adj|fr|thermal|ısıya ilişkin|MOD|thermos|
termos|n|fr|thermos|sıcak|CUM|thermos|
termik|adj|fr|thermique|ısıl|MOD|thermos|
hijyen|n|fr|hygiène|sağlık bilgisi|CUM||grc:hygieinḕ>fr:hygiène>tr:hijyen
diyet|n|fr|diète|yaşam düzeni|CUM||grc:díaita>fr:diète>tr:diyet
rejim|n|fr|régime|yönetim; perhiz|OSM19||la:regimen>fr:régime>tr:rejim
perhiz|n|fa|parhīz|sakınma|EAT||
"""

FAMILIES = r"""
*omur|tr|bel kemiği|Eski Türkçe omurtka "bel kemiği"; omurga (Dil Devrimi türetmesi) ve omurilik aynı kökten gelir.
*bağır|tr|karaciğer; göğüs|Eski Türkçe bagır "karaciğer, göğüs"; bağırsak (bagırsuk) ve yüksek sesle seslenmek anlamındaki bağırmak aynı köktendir.
*sağ|tr|canlı, sağlam|Eski Türkçe sag "sağ, canlı"; sağlık, sağlam ve sağalmak (iyileşmek) aynı kökten türer.
*doku-|tr|dokumak|Eski Türkçe tokı- "dokumak, vurmak"; doku (Dil Devrimi), dokuma ve dokunmak aynı kökten gelir.
N-B-D|ar|atmak (damar)|Arapça n-b-ḏ kökü; nabız (atış) ve nabzetmek aynı kökten gelir.
Ş-F-Y|ar|iyileştirmek|Arapça ş-f-y kökü; şifa (iyileşme) ve şifahane (hastane) aynı kökten türer.
C-Z-A|ar|parça|Arapça c-z-ʾ kökü; cüz (parça), ecza (ilaç maddeleri), eczane, eczacı ve cüzdan aynı kökten gelir.
D-W-Y|ar|ilaç|Arapça d-w-y kökü; deva (ilaç) ve tedavi (sağaltım) aynı kökten türer.
A-Y-N|ar|göz; kaynak|Arapça ʿ-y-n kökü; ayan (gözle görülür), muayene (gözle inceleme) ve ayn (göz, kaynak) aynı kökten gelir.
Ş-H-S|ar|kişi|Arapça ş-ḫ-ṣ kökü; şahıs, şahsiyet ve teşhis (kişiliğini belirleme, tanılama) aynı kökten türer.
H-M-M|ar|ısıtmak|Arapça ḥ-m-m kökü; hamam (ısıtılan yer) ve humma (ateşli hastalık) aynı kökten gelir.
W-R-M|ar|şişmek|Arapça w-r-m kökü; verem (şişlik) sözcüğü Türkçede akciğer hastalığına ad olmuştur.
L-H-B|ar|alevlenmek|Arapça l-h-b kökü; iltihap (alevlenme, yangı) ve lehib (alev) aynı kökten gelir.
R-W-H|ar|soluk, dinginlik|Arapça r-w-ḥ kökü; ruh (soluk, can), rahat, istirahat, rahatsız, ruhani ve reyhan aynı kökten türer.
S-H-H|ar|sağlam olmak|Arapça ṣ-ḥ-ḥ kökü; sıhhat (sağlık), sahih (sağlam), sıhhi ve tashih (düzeltme) aynı kökten gelir.
tomē|el|kesme|Eski Yunanca témnein "kesmek"; anatomi (kesip ayırma), atom (kesilemeyen) ve tomografi aynı kökten gelir.
pathos|el|duygu, acı|Eski Yunanca páthos "acı, duygu"; patoloji, psikopat, sempati, antipati, empati ve apati aynı kökten türer.
aisthēsis|el|duyum|Eski Yunanca aísthēsis "duyum"; estetik (duyuma ilişkin) ile anestezi (duyumsuzluk) aynı kökten gelir.
bios|el|yaşam|Eski Yunanca bíos "yaşam"; biyoloji, biyografi, antibiyotik, biyopsi, mikrop ve amfibi aynı kökten türer.
sonus|la|ses|Latince sonus "ses"; sone, sonar ve ultrason aynı kökten gelir.
ergon|el|iş|Eski Yunanca érgon "iş"; enerji, organ (iş aracı), organizma, alerji ve ergonomi aynı kökten türer.
khrōma|el|renk|Eski Yunanca khrôma "renk"; krom, kromozom (renklenen cisim) ve kromatik aynı kökten gelir.
derma|el|deri|Eski Yunanca dérma "deri"; dermatoloji, dermatolog ve epidermis aynı kökten türer.
kardia|el|yürek|Eski Yunanca kardía "yürek"; kardiyoloji, kardiyak ve elektrokardiyogram aynı kökten gelir; Latince cor ile Hint-Avrupa akrabasıdır.
neuron|el|sinir|Eski Yunanca neûron "kiriş, sinir"; nöroloji, nöron, nevroz ve nevralji aynı kökten türer.
psykhe|el|ruh, soluk|Eski Yunanca psykhḕ "soluk, ruh"; psikoloji, psikiyatri, psikolog ve psişik aynı kökten gelir.
haima|el|kan|Eski Yunanca haîma "kan"; hematoloji, anemi, lösemi, hemoglobin ve hemoroid aynı kökten türer.
gaster|el|mide|Eski Yunanca gastḕr "karın, mide"; gastrit, gastronomi ve gastroenteroloji aynı kökten gelir.
osteon|el|kemik|Eski Yunanca ostéon "kemik"; osteoporoz ve osteopati aynı kökten türer; Latince os ile akrabadır.
orthos|el|doğru, dik|Eski Yunanca orthós "doğru"; ortopedi, ortodonti, ortodoks ve ortografi aynı kökten gelir.
pais|el|çocuk|Eski Yunanca paîs "çocuk"; pedagoji, pedagog, pediatri ve ansiklopedi (çember eğitim) aynı kökten türer.
thermos|el|sıcak|Eski Yunanca thermós "sıcak"; termos, termal, termik ve termometre aynı kökten gelir.
flectere|la|bükmek|Latince flectere "bükmek, çevirmek" fiili (geçmiş ortacı flexus); refleks (geri bükülen, kendiliğinden yanıt), fleksiyon (bükülme), fleksibl (esnek) ve refleksif aynı kökten türer.
"""
