# -*- coding: utf-8 -*-
"""Korpus 17 — Hayvanlar ve bitkiler: memeliler, kuşlar, balıklar, böcekler, sürüngenler, at ve hayvancılık
terimleri, hayvan vücut bölümleri ve sesleri; ağaçlar, meyveler, sebzeler, tahıllar, baharatlar, çiçekler ve bitki bölümleri."""

WORDS = r"""
# --- Memeliler: Öz Türkçe ----------------------------------------------------------------
porsuk|n|tr|borsuk|porsuk|DLT||
gelincik|n|tr|gelin|küçük gelin; gelincik hayvanı ve çiçeği|OSM||
sansar|n|tr?|sansar|sansar|OSM||
kakım|n|tr|kakım|ermin|OSM||
kunduz|n|tr|kunduz|kunduz|DLT||
susamuru|n|tr|su samuru|su samuru|TDK||
sıçan|n|tr|sıçgan|sıçan|DLT||
köstebek|n|tr|köstebek|köstebek|OSM||
kirpi|n|tr|kirpi|kirpi|DLT||
oklukirpi|n|tr|oklu kirpi|oklu kirpi|OSM||
yarasa|n|tr|yarasa|yarasa|EAT||
vaşak|n|fa|vaşaq|vaşak|OSM||
pars|n|tr|bars|pars, kaplan|DLT||
sırtlan|n|tr|sırtlan|sırtlan|OSM||
kokarca|n|tr|kok-|kokan hayvan|OSM||
alageyik|n|tr|ala keyik|benekli geyik|OSM|*ala|
aladoğan|n|tr|ala toğan|benekli doğan|OSM|*ala|
alakarga|n|tr|ala karga|renkli karga|OSM|*ala|
sığın|n|tr|sıgun|iri geyik|DLT||
bozayı|n|tr|boz adıġ|boz renkli ayı|OSM|*boz|
bozkurt|n|tr|boz kurt|boz renkli kurt|OSM|*boz|
tavşancıl|n|tr|tabışġan|tavşan avlayan kartal|OSM||
keler|n|tr|keler|kertenkele|DLT||
manda|n|unk?|manda|su sığırı|OSM||
malak|n|tr|malak|manda yavrusu|OSM||
tekboynuz|n|tr|tek müŋüz|tek boynuzlu masal atı|TDK|*boynuz|
# --- Memeliler: alıntılar ----------------------------------------------------------------
sincap|n|fa|sincāb|sincap|EAT||
samur|n|fa|samūr|samur|EAT||
vizon|n|fr|vison|vizon|MOD||
çakal|n|fa|şaġāl|çakal|EAT||sa:śṛgāla>fa:şaġāl>tr:çakal
rakun|n|en|raccoon|rakun|MOD||unk:aroughcun>en:raccoon>tr:rakun
hamster|n|en|hamster|hamster|MOD||
kobay|n|fr|cobaye|kobay|CUM||
ren|n|fr|renne|ren geyiği|MOD||ger:hreinn>fr:renne>tr:ren
muflon|n|fr|mouflon|yaban koyunu|MOD||it:muflone>fr:mouflon>tr:muflon
yak|n|en|yak|Tibet öküzü|MOD||unk:gyag>en:yak>tr:yak
bizon|n|fr|bison|yaban sığırı|CUM||ger:wisund>la:bison>fr:bison>tr:bizon
antilop|n|fr|antilope|antilop|CUM||grc:anthólops>la:antalopus>fr:antilope>tr:antilop
gazal|n|ar|ġazāl|ceylan|EAT||
ahu|n|fa|āhū|ceylan|EAT||
zürafa|n|ar|zarāfa|zürafa|OSM||
fil|n|ar|fīl|fil|EAT||fa:pīl>ar:fīl>tr:fil
mamut|n|fr|mammouth|mamut|MOD||ru:mamont>fr:mammouth>tr:mamut
gergedan|n|fa|kargadan|gergedan|OSM||sa:khaḍgadanta>fa:kargadan>tr:gergedan
zebra|n|fr|zèbre|zebra|CUM||pt:zebra>fr:zèbre>tr:zebra
maymun|n|ar|maymūn|uğurlu, kutlu; maymun|EAT||
şempanze|n|fr|chimpanzé|şempanze|MOD||unk:kivili-chimpenze>fr:chimpanzé>tr:şempanze
goril|n|fr|gorille|goril|MOD||grc:górillai>en:gorilla>fr:gorille>tr:goril
orangutan|n|fr|orang-outan|orman insanı|MOD||ml:orang hutan>nl:orang-oetan>fr:orang-outan>tr:orangutan
babun|n|fr|babouin|babun|MOD||
lemur|n|fr|lémur|gece ruhu|MOD||la:lemures>fr:lémur>tr:lemur
kanguru|n|en|kangaroo|kanguru|OSM19||unk:gangurru>en:kangaroo>tr:kanguru
koala|n|en|koala|koala|MOD||unk:gula>en:koala>tr:koala
panda|n|fr|panda|panda|MOD||
lama|n|es|llama|lama|MOD||unk:llama>es:llama>tr:lama
alpaka|n|es|alpaca|alpaka|MOD||unk:allpaqa>es:alpaca>tr:alpaka
leopar|n|fr|léopard|aslan-pars|CUM||grc:leópardos>la:leopardus>fr:léopard>tr:leopar
jaguar|n|fr|jaguar|jaguar|MOD||tup:yaguara>pt:jaguar>fr:jaguar>tr:jaguar
puma|n|es|puma|puma|MOD||unk:puma>es:puma>tr:puma
çita|n|en|cheetah|benekli|MOD||sa:citraka>hi:cītā>en:cheetah>tr:çita
hecin|n|ar|hajīn|melez; yarış devesi|OSM||
camız|n|ar|jāmūs|manda|OSM||fa:gāvmēş>ar:jāmūs>tr:camız
mors|n|fr|morse|mors|MOD||ru:morž>fr:morse>tr:mors
yabandomuzu|n|fa|yābān|ıssız kır (domuzu)|OSM|yābān|
yabankedisi|n|fa|yābān|yaban kedisi|OSM|yābān|
yabankeçisi|n|fa|yābān|yaban keçisi|OSM|yābān|
yabanmersini|n|fa|yābān|yaban mersini|TDK|yābān|
mahluk|n|ar|maḫlūq|yaratılmış|EAT|H-L-K|
mahlukat|n|ar|maḫlūqāt|yaratılmışlar|OSM|H-L-K|
hayvani|adj|ar|ḥayawānī|hayvana ilişkin|OSM|H-Y-Y|
# --- At ve koşum takımı ---------------------------------------------------------------
beygir|n|fa|bārgīr|yük tutan|EAT||
küheylan|n|ar|kuḥaylān|soylu Arap atı|OSM||
midilli|n|el|Mytilḗnē|Midilli adası (atı)|OSM19||
kulun|n|tr|kulun|at yavrusu|DLT||
sıpa|n|tr|sıpa|eşek yavrusu|OSM||
iğdiş|n|tr|igdiş|enenmiş hayvan|EAT||
doru|n|tr|torug|kızıl kahverengi at|DLT||
kula|n|tr|kula|sarımsı kahverengi at|DLT||
rahvan|n|fa|rahvār|yol gider; yorga yürüyüş|OSM||
tırıs|n|tr|tırıs|atın kısa adımlı koşusu|OSM||
dörtnal|n|tr|dört nal|dört nalla koşu|OSM||
eşkin|n|tr|eşgin|atın rahat koşusu|DLT||
yele|n|tr|yal|at boynu kılı|DLT||
toynak|n|tr|tuynak|tırnak|DLT||
eyer|n|tr|eder|at oturağı|DLT|*eyer|
eyerlemek|v|tr|eder|eyer vurmak|OSM|*eyer|
semer|n|el|samári|yük hayvanı eyeri|EAT||grc:ságma>el:samári>tr:semer
palan|n|fa|pālān|semer|EAT||
yular|n|tr|yular|başlık ipi|DLT||
dizgin|n|tr|tizgin|at yönetme kayışı|DLT||
gem|n|tr|gem|at ağızlığı|EAT||
kantarma|n|tr|kantarma|sert gem|OSM||
üzengi|n|tr|üzeŋgü|ayak basamağı|DLT||
kolan|n|tr|kolan|eyer kuşağı|DLT||
hamut|n|sl|ḫomut|boyunduruk yastığı|OSM||
koşum|n|tr|koş-|koşma takımı|OSM|*koş-|
boyunduruk|n|tr|boyunduruk|boyun bağı|DLT||
çul|n|ar|jull|hayvan örtüsü|EAT||
kamçı|n|tr|kamçı|kamçı|DLT|*kamçı|
kamçılamak|v|tr|kamçı|kamçı vurmak|OSM|*kamçı|
kırbaç|n|tr|kırbaç|kamçı|OSM||
mahmuz|n|ar|mihmāz|dürtme aracı|EAT||
kaşağı|n|tr|kaşagu|at tarağı|DLT||
tımar|n|fa|tīmār|bakım|EAT||
jokey|n|en|jockey|yarış binicisi|MOD||
# --- Büyükbaş, küçükbaş ve kümes ---------------------------------------------------------
dana|n|tr|tana|genç sığır|EAT||
düve|n|tr|düve|doğurmamış dişi sığır|OSM||
tosun|n|tr|tosun|genç boğa|OSM||
buzağı|n|tr|buzagu|sığır yavrusu|DLT|*buzağı|
buzağılamak|v|tr|buzagu|buzağı doğurmak|OSM|*buzağı|
koç|n|tr|koç|erkek koyun|DLT|*koç|
koçbaşı|n|tr|koç başı|kale dövme aracı|OSM|*koç|
toklu|n|tr|toklı|bir yaşında kuzu|DLT||
şişek|n|tr|şişek|iki yaşında koyun|OSM||
çebiç|n|tr|çebiç|bir yaşında keçi|OSM||
kuzulamak|v|tr|kuzı|kuzu doğurmak|OSM|*kuzu|
kuzukulağı|n|tr|kuzı|ekşi yapraklı ot|OSM|*kuzu|
kuzugöbeği|n|tr|kuzı|bir mantar türü|OSM|*kuzu|
keçiboynuzu|n|tr|keçi|harnup|OSM|*keçi|
keçiyolu|n|tr|keçi|dar patika|OSM|*keçi|
keçisakalı|n|tr|keçi|bir ot türü|OSM|*keçi|
civciv|n|tr|civ|yavru tavuk sesi|OSM|*cıv|
piliç|n|el?|poulí|kuş, yavru kuş|OSM||
folluk|n|tr?|fol|tavuk yumurtlama yeri|OSM||
tünek|n|tr|tüne-|kuşun konduğu yer|OSM|*tüne-|
tünemek|v|tr|tüne-|gece konmak|DLT|*tüne-|
tavus|n|fa|ṭāvūs|tavus kuşu|EAT||grc:taṓs>ar:ṭāwūs>fa:ṭāvūs>tr:tavus
sülün|n|tr|sülün|sülün|OSM||
suna|n|tr|suna|dişi ördek|OSM||
angıt|n|tr|angıt|kızıl ördek|OSM||
yumurtlamak|v|tr|yumurtga|yumurta bırakmak|OSM|*yumurta|
yumurtalık|n|tr|yumurtga|yumurta üreten organ|DD|*yumurta|
yavru|n|tr|yavru|hayvan çocuğu|EAT|*yavru|
yavrulamak|v|tr|yavru|yavru doğurmak|OSM|*yavru|
yavrucak|n|tr|yavru|küçük yavru|OSM|*yavru|
enik|n|tr|enük|köpek yavrusu|DLT||
döl|n|tr|töl|yavru, soy|DLT|*döl|
döllemek|v|tr|töl|döl vermek|DD|*döl|
dölüt|n|tr|töl|cenin|DD|*döl|
damızlık|n|tr|damız|üretim için ayrılan|OSM||
sağmal|adj|tr|sag-|sağılan|OSM|*sağ-|
sağmak|v|tr|sag-|süt almak|DLT|*sağ-|
sağım|n|tr|sag-|sağma işi|OSM|*sağ-|
besi|n|tr|besle-|semirtme|OSM|*besle-|
besili|adj|tr|besle-|semiz|OSM|*besle-|
mandıra|n|el|mándra|ağıl; süt işliği|OSM||
yemlik|n|tr|yem|yem konan kap|OSM|*yem|
yemlemek|v|tr|yem|yem vermek|OSM|*yem|
silaj|n|fr|silage|silolanmış yem|MOD||es:silo>fr:silage>tr:silaj
küspe|n|fa|kusba|yağı alınmış posa|OSM||
otlamak|v|tr|otla-|ot yemek|DLT|*ot|
otlatmak|v|tr|otlat-|otlamasını sağlamak|DLT|*ot|
otçul|adj|tr|ot|ot yiyen|DD|*ot|
gütmek|v|tr|küd-|sürüyü yönetmek|DLT|*güt-|
güdüm|n|tr|küd-|yönetme|DD|*güt-|
güdümlü|adj|tr|küd-|yönetilen|DD|*güt-|
sığırtmaç|n|tr|sıgır|sığır güden|EAT|*sığır|
sığırcık|n|tr|sıgır|kara renkli kuş|OSM|*sığır|
sığırdili|n|tr|sıgır|tüylü yapraklı ot|OSM|*sığır|
sığırkuyruğu|n|tr|sıgır|sarı çiçekli ot|OSM|*sığır|
kırkmak|v|tr|kırk-|yün kesmek|DLT|*kırk-|
kırkım|n|tr|kırk-|yün kesme mevsimi|OSM|*kırk-|
yapağı|n|tr|yapagu|ilkbahar yünü|DLT||
tiftik|n|tr?|tift-|didilmiş yün|OSM||
moher|n|en|mohair|tiftik yünü|MOD||ar:muḫayyar>it:mocaiarro>en:mohair>tr:moher
meşin|n|fa|mīşīn|koyun derisi|OSM||
sahtiyan|n|fa|saḫtiyān|keçi derisi|OSM||
kösele|n|fa|gūsāla|dana (derisi)|OSM||
tazı|n|fa|tāzī|Arap (köpeği)|EAT||
kangal|n|tr|Kangal|Kangal ilçesi (köpeği)|MOD||
çiftleşmek|v|fa|cuft|çift olmak|OSM|cuft|
kızışmak|v|tr|kız-|çiftleşme isteği duymak|OSM||
geviş|n|tr|kev-|çiğnenmiş yem|DLT||
yalamak|v|tr|yalga-|dille sürmek|DLT||
yuvalanmak|v|tr|yuva|yuva yapmak|OSM||
baytar|n|ar|bayṭār|hayvan hekimi|EAT||
# --- Kuşlar --------------------------------------------------------------------------------
serçe|n|tr|serçe|serçe|EAT||
kırlangıç|n|tr|karlıgaç|kırlangıç|DLT||
leylek|n|fa|laklak|leylek|EAT||
akbaba|n|tr|ak baba|akbaba|OSM||
baykuş|n|tr|bay kuş|baykuş|EAT|*kuş|
kuzgun|n|tr|kuzgun|kuzgun|DLT||
karga|n|tr|karga|karga|DLT||
saksağan|n|tr|sagızgan|saksağan|DLT||
kumru|n|ar|qumrī|kumru|EAT||
üveyik|n|tr|üveyik|yaban güvercini|OSM||
bıldırcın|n|tr|budursın|bıldırcın|DLT||
keklik|n|tr|keklik|keklik|DLT||
çil|n|tr|çil|benek; çil kuşu|OSM||
çulluk|n|tr|çulluk|çulluk|OSM||
turaç|n|ar|durrāj|turaç|OSM||
kuğu|n|tr|kugu|kuğu|DLT||
pelikan|n|fr|pélican|pelikan|OSM19||grc:pelekán>la:pelicanus>fr:pélican>tr:pelikan
flamingo|n|en|flamingo|alev renkli|MOD||pt:flamengo>en:flamingo>tr:flamingo
karabatak|n|tr|kara batak|karabatak|OSM|*kara|
balıkçıl|n|tr|balıkçıl|balık yiyen kuş|OSM|*balık|
balaban|n|tr|balaban|iri; bir balıkçıl türü|DLT||
yalıçapkını|n|tr|yalı çapkını|yalıçapkını|OSM||
ağaçkakan|n|tr|ağaç kakan|ağaçkakan|OSM|*ağaç|
çalıkuşu|n|tr|çalı kuşu|çalıkuşu|OSM|*çalı|
ispinoz|n|el|spínos|ispinoz|OSM||
kanarya|n|it|canaria|Kanarya Adaları (kuşu)|OSM||la:Canaria>it:canaria>tr:kanarya
papağan|n|ar|babbaġāʾ|papağan|EAT||
saka|n|ar|saqqāʾ|sucu|OSM||
florya|n|el|flóros|florya|OSM||
karatavuk|n|tr|kara tavuk|karatavuk|OSM|*kara|
ardıçkuşu|n|tr|ardıç kuşu|ardıçkuşu|OSM|*kuş|
toygar|n|tr|toygar|tarla kuşu|OSM||
baştankara|n|tr|baştan kara|baştankara|OSM|*baş|
çobanaldatan|n|tr|çoban aldatan|çobanaldatan|OSM||
sakarmeke|n|tr|sakar meke|su tavuğu|OSM||
bağırtlak|n|tr|bağırtlak|bağırtlak|OSM||
puhu|n|tr|puhu|büyük baykuş|OSM||
kukumav|n|el|koukouvágia|küçük baykuş|OSM||
guguk|n|tr|guguk|guguk kuşu|OSM||
kerkenez|n|el|kirkinézi|kerkenez|OSM||
delice|n|tr|deli|delice doğan|OSM||
çakır|n|tr|çakır|çakır doğan|DLT||
sungur|n|tr|sunkur|akdoğan|DLT||
laçin|n|tr|laçın|şahin|DLT||
tuğrul|n|tr|tugrıl|yırtıcı kuş|DLT||
atmaca|n|tr|atmaca|atmaca|EAT|*at-|
doğancı|n|tr|toğan|doğan yetiştiren|OSM||
devekuşu|n|tr|deve kuşu|devekuşu|OSM|*deve|
penguen|n|fr|pingouin|penguen|CUM||
ibibik|n|tr|ibibik|çavuş kuşu|OSM||
hüthüt|n|ar|hudhud|çavuş kuşu|OSM||
ebabil|n|ar|abābīl|sürüler; dağ kırlangıcı|OSM||
kuyrukkakan|n|tr|kuyruk kakan|kuyrukkakan|OSM|*kuyruk|
sinekkuşu|n|tr|sinek kuşu|sinekkuşu|MOD|*sinek|
sinekkapan|n|tr|sinek kapan|sinekkapan kuşu|OSM|*sinek|
sarıasma|n|tr|sarı asma|sarıasma kuşu|OSM|*sarı|
ötleğen|n|tr|öt-|öten kuş|OSM|*öt-|
anka|n|ar|ʿanqāʾ|uzun boyunlu; masal kuşu|EAT||
hüma|n|fa|humā|devlet kuşu|EAT||
simurg|n|fa|sīmurġ|otuz kuş|OSM||
kuşbaşı|n|tr|kuş başı|küçük doğranmış et|OSM|*kuş|
kuşburnu|n|tr|kuş burnu|yaban gülü meyvesi|OSM|*kuş|
kuşkonmaz|n|tr|kuş konmaz|kuşkonmaz|OSM|*kuş|
kuşbakışı|n|tr|kuş bakışı|yukarıdan görünüş|OSM|*kuş|
kuşçu|n|tr|kuş|kuş yetiştiren|OSM|*kuş|
kuşdili|n|tr|kuş dili|bir ot türü|OSM|*kuş|
kuşüzümü|n|tr|kuş üzümü|küçük kuru üzüm|OSM|*üzüm|
ötmek|v|tr|öt-|ses çıkarmak|DLT|*öt-|
ötücü|adj|tr|öt-|öten|TDK|*öt-|
ötüş|n|tr|öt-|ötme biçimi|OSM|*öt-|
şakımak|v|tr|şakı-|güzel ötmek|OSM||
cıvıldamak|v|tr|cıvıl|cıvıl cıvıl ötmek|OSM|*cıv|
cıvıltı|n|tr|cıvıl|kuş sesi|OSM|*cıv|
gaklamak|v|tr|gak|karga sesi çıkarmak|OSM||
gıdaklamak|v|tr|gıdak|tavuk sesi çıkarmak|OSM||
vaklamak|v|tr|vak|ördek sesi çıkarmak|OSM||
tüy|n|tr|tü|kıl, tüy|DLT|*tüy|
tüylü|adj|tr|tü|tüyü olan|DLT|*tüy|
tüysüz|adj|tr|tü|tüyü olmayan|OSM|*tüy|
tüylenmek|v|tr|tü|tüy çıkarmak|OSM|*tüy|
kuştüyü|n|tr|kuş tüyü|kuş tüyü|OSM|*tüy|
kanat|n|tr|kanat|kanat|DLT|*kanat|
kanatlı|adj|tr|kanat|kanadı olan|DLT|*kanat|
kanatlanmak|v|tr|kanat|kanat açıp uçmak|OSM|*kanat|
kanatsız|adj|tr|kanat|kanadı olmayan|OSM|*kanat|
sarıkanat|n|tr|sarı kanat|orta boy lüfer|OSM|*sarı|
ibik|n|tr|ibik|horoz tepeliği|OSM||
kursak|n|tr|kursak|kuş midesi|DLT||
ördekbaşı|n|tr|ördek başı|yeşil renk tonu|OSM||
kazayağı|n|tr|kaz ayağı|kazayağı otu|OSM||
tavukgöğsü|n|tr|tavuk göğsü|sütlü tatlı|OSM||
horozibiği|n|tr|horoz ibiği|horozibiği çiçeği|OSM||
# --- Balıklar ve deniz canlıları ------------------------------------------------------------
balina|n|it|balena|balina|OSM19||grc:phállaina>la:ballaena>it:balena>tr:balina
köpekbalığı|n|tr|köpek balığı|köpekbalığı|OSM|*balık|
kılıçbalığı|n|tr|kılıç balığı|kılıçbalığı|OSM|*balık|
yılanbalığı|n|tr|yılan balığı|yılanbalığı|OSM|*yılan|
yılancık|n|tr|yılan|deri hastalığı|OSM|*yılan|
ayıbalığı|n|tr|ayı balığı|fok|OSM|*balık|
mürekkepbalığı|n|tr|mürekkep balığı|mürekkepbalığı|OSM|*balık|
balıkçılık|n|tr|balık|balık avlama işi|TDK|*balık|
balıkhane|n|tr|balık hane|balık hali|OSM|-hāne|
denizaslanı|n|tr|deniz aslanı|denizaslanı|TDK|*deniz|
denizanası|n|tr|deniz anası|denizanası|OSM|*deniz|
denizyıldızı|n|tr|deniz yıldızı|denizyıldızı|TDK|*deniz|
denizkestanesi|n|tr|deniz kestanesi|denizkestanesi|TDK|*deniz|
denizatı|n|tr|deniz atı|denizatı|TDK|*deniz|
deniztarağı|n|tr|deniz tarağı|deniztarağı|TDK|*deniz|
istiridye|n|el|ostrídia|istiridye|OSM||
salyangoz|n|el|saliángos|salyangoz|OSM||
sümüklüböcek|n|tr|sümüklü böcek|sümüklüböcek|OSM|*böcek|
kerevit|n|el|karavída|tatlı su istakozu|OSM||
havyar|n|fa|ḫāviyār|mersin balığı yumurtası|OSM||
mersin|n|el|myrsínē|mersin ağacı|EAT||
somon|n|fr|saumon|somon|CUM||la:salmo>fr:saumon>tr:somon
sudak|n|sl|sudak|sudak balığı|MOD||
zargana|n|el|zargána|zargana|OSM||
kolyoz|n|el|koliós|kolyoz|OSM||
lapina|n|el|lapína|lapina|OSM||
hani|n|el|khános|hani balığı|OSM||
sinarit|n|el|synagrída|sinarit|OSM||
fangri|n|el|fagrí|mercan türü|OSM||
lagos|n|el|lagós|tavşan; lagos balığı|OSM||
orfoz|n|el|orfós|orfoz|OSM||
iskorpit|n|el|skorpína|akrep balığı|OSM||
tirsi|n|el|thríssa|tirsi|OSM||
vatoz|n|el|vátos|vatoz|OSM||
izmarit|n|el|smarída|izmarit|OSM||
sargoz|n|el|sargós|sargoz|OSM||
mırmır|n|el|mourmoúra|mırmır|OSM||
sarpa|n|el|sálpa|sarpa|OSM||
yüzgeç|n|tr|yüz-|yüzme organı|DD|*yüz-|
yüzmek|v|tr|yüz-|suda ilerlemek|DLT|*yüz-|
yüzücü|n|tr|yüz-|yüzen kişi|TDK|*yüz-|
solungaç|n|tr|solu-|su soluma organı|DD|*solu-|
solumak|v|tr|solu-|nefes almak|DLT|*solu-|
solunum|n|tr|solu-|nefes alıp verme|DD|*solu-|
kılçık|n|tr|kıl|balık kemiği|OSM|*kıl|
kıl|n|tr|kıl|ince tüy|DLT|*kıl|
kıllanmak|v|tr|kıl|kıl çıkarmak|OSM|*kıl|
kabuklu|adj|tr|kabuk|kabuğu olan|OSM||
yumuşakça|n|tr|yumuşak|yumuşak gövdeli hayvan|DD||
eklembacaklı|n|tr|eklem bacaklı|eklemli bacaklı hayvan|DD||
omurgalı|adj|tr|omurga|omurgası olan|DD|*omur|
omurgasız|adj|tr|omurga|omurgası olmayan|DD|*omur|
plankton|n|fr|plancton|gezinen|MOD||grc:planktón>fr:plancton>tr:plankton
# --- Böcekler ve küçük canlılar --------------------------------------------------------------
böcek|n|tr|böcek|böcek|EAT|*böcek|
böcü|n|tr|böcü|böcek; korkunç yaratık|OSM|*böcek|
böcekçil|adj|tr|böcek|böcek yiyen|DD|*böcek|
sivrisinek|n|tr|sivri sinek|sivrisinek|OSM|*sinek|
karasinek|n|tr|kara sinek|karasinek|OSM|*kara|
sineklik|n|tr|sinek|sinek önleyici tel|OSM|*sinek|
tatarcık|n|tr|tatar|küçük ısırıcı sinek|OSM||
tırtıl|n|tr|tırtıl|kelebek kurdu|OSM||
kurtçuk|n|tr|kurt|küçük kurt|OSM|*kurt|
kurtlanmak|v|tr|kurt|kurt üremek|OSM|*kurt|
kurtbağrı|n|tr|kurt bağrı|kurtbağrı çalısı|OSM|*kurt|
larva|n|fr|larve|hayalet; maske|MOD||la:larva>fr:larve>tr:larva
koza|n|fa|ġūze|pamuk kozası; ipek kozası|OSM||
krizalit|n|fr|chrysalide|altın renkli|MOD||grc:khrysallís>la:chrysallis>fr:chrysalide>tr:krizalit
eşekarısı|n|tr|eşek arısı|eşekarısı|OSM|*arı|
yabanarısı|n|tr|yaban arısı|yabanarısı|OSM|*arı|
balarısı|n|tr|bal arısı|balarısı|OSM|*arı|
arıcılık|n|tr|arı|arı yetiştirme|TDK|*arı|
balmumu|n|tr|bal mumu|balmumu|OSM|*bal|
ballıbaba|n|tr|ballı baba|ballıbaba otu|OSM|*bal|
balkabağı|n|tr|bal kabağı|bal kabağı|OSM|*bal|
petek|n|tr|petek|bal gözenekleri|OSM||
kovan|n|tr|kovan|arı evi|EAT||
termit|n|fr|termite|ağaç kurdu|MOD||la:termes>fr:termite>tr:termit
çekirge|n|tr|çekürge|çekirge|DLT||
cırcırböceği|n|tr|cırcır böceği|cırcırböceği|OSM|*böcek|
ağustosböceği|n|tr|ağustos böceği|ağustosböceği|OSM|*böcek|
hamamböceği|n|tr|hamam böceği|hamamböceği|OSM|*böcek|
uğurböceği|n|tr|uğur böceği|uğurböceği|OSM|*böcek|
ipekböceği|n|tr|ipek böceği|ipekböceği|OSM|*böcek|
ateşböceği|n|tr|ateş böceği|ateşböceği|OSM|*böcek|
kınkanatlı|n|tr|kın kanatlı|kın kanatlı böcek|DD|*kanat|
kene|n|tr|kene|kene|DLT||
pire|n|tr|bürge|pire|DLT||
tahtakurusu|n|tr|tahta kurusu|tahtakurusu|OSM|*kurt|
güve|n|tr|küye|güve|DLT||
solucan|n|tr|solucan|solucan|OSM||
sülük|n|tr|sülük|sülük|DLT||
peygamberdevesi|n|tr|peygamber devesi|peygamberdevesi|OSM|*deve|
yusufçuk|n|tr|Yusuf|kız böceği|OSM||
kırkayak|n|tr|kırk ayak|kırkayak|OSM||
çıyan|n|tr|çıyan|çıyan|OSM||
danaburnu|n|tr|dana burnu|danaburnu|OSM||
haşere|n|ar|ḥaşara|böcek|OSM|H-Ş-R|
haşerat|n|ar|ḥaşarāt|böcekler|OSM|H-Ş-R|
insektisit|n|fr|insecticide|böcek öldürücü|MOD||
pestisit|n|fr|pesticide|zararlı öldürücü|MOD||
vızıldamak|v|tr|vız|vız sesi çıkarmak|OSM|*vız|
vızıltı|n|tr|vız|vız sesi|OSM|*vız|
sokmak|v|tr|sok-|iğne batırmak|DLT|*sok-|
sokulmak|v|tr|sok-|yaklaşmak|DLT|*sok-|
sokulgan|adj|tr|sok-|yakınlık kuran|TDK|*sok-|
ısırgan|n|tr|ısır-|ısıran ot|OSM|*ısır-|
ısırık|n|tr|ısır-|ısırma izi|OSM|*ısır-|
kemirmek|v|tr|kemir-|dişle aşındırmak|OSM|*kemir-|
kemirgen|n|tr|kemir-|kemiren hayvan|DD|*kemir-|
# --- Sürüngenler ve iki yaşamlılar ----------------------------------------------------------
kurbağa|n|tr|kurbaka|kurbağa|DLT|*kurbağa|
kurbağalama|n|tr|kurbaka|kurbağa yüzüşü|MOD|*kurbağa|
kaplumbağa|n|tr|kaplu baga|kabuklu kurbağa|EAT||
tosbağa|n|tr|tos baga|kaplumbağa|OSM||
kertenkele|n|tr|keler|kertenkele|OSM||
kobra|n|fr|cobra|yılan|MOD||pt:cobra>fr:cobra>tr:kobra
engerek|n|tr|engerek|zehirli yılan|OSM||
boa|n|fr|boa|boa yılanı|MOD||la:boa>fr:boa>tr:boa
piton|n|fr|python|Python ejderi|MOD||grc:Pýthōn>la:python>fr:python>tr:piton
anakonda|n|en|anaconda|anakonda|MOD||ta:ānai-kondra>en:anaconda>tr:anakonda
timsah|n|ar|timsāḥ|timsah|EAT||egy:msḥ>cop:emsah>ar:timsāḥ>tr:timsah
bukalemun|n|ar|abū qalamūn|renk değiştiren|OSM||grc:khamailéōn>ar:abū qalamūn>tr:bukalemun
semender|n|fa|samandar|semender|OSM||grc:salamándra>fa:samandar>tr:semender
iguana|n|es|iguana|iguana|MOD||unk:iwana>es:iguana>tr:iguana
dinozor|n|fr|dinosaure|korkunç kertenkele|MOD||
ejder|n|fa|ajdar|ejderha|EAT||
sürüngen|n|tr|sürün-|sürünen hayvan|DD|*sür-|
sürünmek|v|tr|sürün-|yerde ilerlemek|DLT|*sür-|
sürek|n|tr|sür-|sürek avı|OSM|*sür-|
tıslamak|v|tr|tıs|tıs sesi çıkarmak|OSM||
# --- Hayvan vücut bölümleri -------------------------------------------------------------------
boynuz|n|tr|müŋüz|boynuz|DLT|*boynuz|
boynuzlamak|v|tr|müŋüz|boynuzla vurmak|OSM|*boynuz|
boynuzlu|adj|tr|müŋüz|boynuzu olan|OSM|*boynuz|
kuyruk|n|tr|kudruk|kuyruk|DLT|*kuyruk|
kuyruklu|adj|tr|kudruk|kuyruğu olan|OSM|*kuyruk|
kuyruksuz|adj|tr|kudruk|kuyruğu olmayan|OSM|*kuyruk|
atkuyruğu|n|tr|at kuyruğu|saç biçimi; eğrelti türü|OSM|*kuyruk|
tilkikuyruğu|n|tr|tilki kuyruğu|bir ot türü|OSM|*kuyruk|
pençe|n|fa|panca|beş; el|EAT|panca|
pençelemek|v|fa|panca|pençeyle tutmak|OSM|panca|
pençeleşmek|v|fa|panca|boğuşmak|OSM|panca|
aslanpençesi|n|fa|panca|bir ot türü|OSM|panca|
meme|n|tr|meme|süt bezi|EAT||
memeli|n|tr|meme|memesi olan hayvan|DD||
pati|n|tr|pati|hayvan ayağı|MOD||
iskelet|n|fr|squelette|kurumuş|OSM19||grc:skeletós>fr:squelette>tr:iskelet
köpekdişi|n|tr|köpek dişi|sivri diş|OSM||
kedidili|n|tr|kedi dili|ince bisküvi|OSM||
# --- Hayvan sesleri ---------------------------------------------------------------------------
havlamak|v|tr|hav|köpek sesi çıkarmak|OSM||
miyavlamak|v|tr|miyav|kedi sesi çıkarmak|OSM||
mırlamak|v|tr|mır|kedi hırıltısı çıkarmak|OSM||
böğürmek|v|tr|bögür-|sığır sesi çıkarmak|DLT|*böğür-|
böğürtü|n|tr|bögür-|böğürme sesi|OSM|*böğür-|
melemek|v|tr|mele-|koyun sesi çıkarmak|OSM||
kişnemek|v|tr|kişne-|at sesi çıkarmak|DLT||
anırmak|v|tr|aŋır-|eşek sesi çıkarmak|OSM||
ulumak|v|tr|ulı-|kurt sesi çıkarmak|DLT||
hırlamak|v|tr|hır|hır sesi çıkarmak|OSM||
kükremek|v|tr|kükre-|aslan sesi çıkarmak|DLT||
cıyaklamak|v|tr|cıyak|cıyak sesi çıkarmak|OSM||
zırlamak|v|tr|zır|sürekli ötmek|OSM||
# --- Avcılık, yırtıcılık ve sınıflar ------------------------------------------------------
yırtıcı|adj|tr|yırt-|parçalayan|OSM|*yırt-|
yırtmak|v|tr|yırt-|parçalamak|DLT|*yırt-|
yırtık|adj|tr|yırt-|yırtılmış|DLT|*yırt-|
etçil|adj|tr|et|et yiyen|DD||
hepçil|adj|tr|hep|her şeyi yiyen|DD||
evcil|adj|tr|ev|eve alışmış|DD||
ehli|adj|ar|ahlī|aileye ait; evcil|EAT|A-H-L|
ehlileştirmek|v|ar|ahlī|evcilleştirmek|OSM|A-H-L|
ehlileşmek|v|ar|ahlī|evcilleşmek|OSM|A-H-L|
vahşi|adj|ar|waḥşī|yabani|EAT|W-H-Ş|
vahşet|n|ar|waḥşa|yabanilik, ıssızlık|EAT|W-H-Ş|
tuzak|n|tr|tuzak|kapan|DLT||
kapan|n|tr|kap-|tuzak|OSM|*kap-|
ökse|n|el|iksós|ökse otu zamkı|OSM||
kement|n|fa|kamand|ilmikli ip|EAT||
zıpkın|n|tr|zıpkın|balık mızrağı|OSM||
serpme|n|tr|serp-|atma ağı|OSM||
avlak|n|tr|av|av yeri|OSM|*av|
avlanmak|v|tr|av|av yapmak|OSM|*av|
# --- Ağaçlar ve çalılar -----------------------------------------------------------------------
ardıç|n|tr|artuç|ardıç|DLT||
köknar|n|el|koukounariá|fıstık çamı kozalağı|OSM||
ladin|n|ar?|lādan|reçineli ağaç; reçine|OSM||
söğüt|n|tr|sögüt|söğüt|DLT||
salkımsöğüt|n|tr|salkım söğüt|salkım söğüt|OSM|*salkım|
salkım|n|tr|salkım|üzüm salkımı|DLT|*salkım|
salkımsaçak|adj|tr|salkım saçak|dağınık sarkık|OSM|*salkım|
ıhlamur|n|el|flamoúri|ıhlamur|OSM||
gürgen|n|tr?|gürgen|gürgen|OSM||
dişbudak|n|tr|diş budak|dişbudak|OSM|*budak|
budak|n|tr|butak|dal|DLT|*budak|
budanmak|v|tr|buta-|dalı kesilmek|OSM|*budak|
karaağaç|n|tr|kara ağaç|karaağaç|OSM|*kara|
kızılağaç|n|tr|kızıl ağaç|kızılağaç|OSM|*kızıl|
akçaağaç|n|tr|akça ağaç|akçaağaç|OSM|*ağaç|
ağaçlandırmak|v|tr|ıgaç|ağaç dikmek|DD|*ağaç|
sığla|n|tr|sığla|günlük ağacı|OSM||
ılgın|n|tr|yılgun|ılgın|DLT||
çitlembik|n|tr|çitlembik|menengiç|OSM||
ahlat|n|tr|ahlat|yaban armudu|OSM||
katırtırnağı|n|tr|katır tırnağı|katırtırnağı çalısı|OSM||
okaliptüs|n|fr|eucalyptus|iyi örtülü|MOD||grc:eukályptos>fr:eucalyptus>tr:okaliptüs
akasya|n|fr|acacia|akasya|OSM19||grc:akakía>la:acacia>fr:acacia>tr:akasya
manolya|n|fr|magnolia|Magnol çiçeği|CUM||
sakız|n|tr|sakız|sakız|DLT||
sakızkabağı|n|tr|sakız kabağı|sakız kabağı|OSM||
mazı|n|fa|māzū|mazı|OSM||
şimşir|n|fa|şimşād|şimşir|EAT||
zakkum|n|ar|zaqqūm|cehennem ağacı|EAT||
hünnap|n|ar|ʿunnāb|hünnap|OSM||
harnup|n|ar|ḫarrūb|keçiboynuzu|EAT||
defne|n|el|dáfnē|defne|EAT||
çamfıstığı|n|tr|çam fıstığı|çam fıstığı|OSM|*çam|
çamsakızı|n|tr|çam sakızı|reçine|OSM|*çam|
karaçam|n|tr|kara çam|karaçam|OSM|*çam|
sarıçam|n|tr|sarı çam|sarıçam|OSM|*çam|
kızılçam|n|tr|kızıl çam|kızılçam|OSM|*kızıl|
kozalak|n|tr|kozalak|çam meyvesi|OSM||
selvi|n|fa|sarv|servi|EAT||
palmiye|n|fr|palmier|hurma ağacı|OSM19||la:palma>fr:palmier>tr:palmiye
bambu|n|fr|bambou|bambu|MOD||ml:bambu>pt:bambu>fr:bambou>tr:bambu
kaktüs|n|fr|cactus|kaktüs|MOD||grc:káktos>la:cactus>fr:cactus>tr:kaktüs
kamış|n|tr|kamış|kamış|DLT|*kamış|
şekerkamışı|n|tr|şeker kamışı|şeker kamışı|OSM|*kamış|
kocayemiş|n|tr|koca yemiş|kocayemiş|OSM||
üvez|n|tr|üvez|üvez ağacı|OSM||
kütük|n|tr|kötük|ağaç gövdesi|DLT||
hevenk|n|fa|āvang|asılı meyve dizisi|OSM||
asma|n|tr|as-|asılan bitki|OSM||
bağbozumu|n|tr|bağ bozumu|üzüm hasadı|OSM||
bağcılık|n|fa|bāġ|bağ yetiştiriciliği|TDK||
koruk|n|tr|koruk|ham üzüm|OSM||
çağla|n|fa|çaġāla|ham badem|OSM||
# --- Meyveler ---------------------------------------------------------------------------------
ahududu|n|fa|āhū|ceylan (dutu)|OSM||
alıç|n|fa|ālūça|küçük erik|OSM||
kızılcık|n|tr|kızıl|kızıl meyve|OSM|*kızıl|
iğde|n|tr|yigde|iğde|DLT||
muşmula|n|el|moúsmoulo|muşmula|OSM||
frenküzümü|n|tr|Frenk üzümü|Frenk üzümü|OSM|*üzüm|
bektaşiüzümü|n|tr|Bektaşi üzümü|Bektaşi üzümü|OSM|*üzüm|
itüzümü|n|tr|it üzümü|itüzümü otu|OSM|*üzüm|
karadut|n|tr|kara dut|karadut|OSM|*kara|
kivi|n|en|kiwi|kivi kuşu; kivi|MOD||unk:kiwi>en:kiwi>tr:kivi
avokado|n|en|avocado|avokado|MOD||
mango|n|en|mango|mango|MOD||ta:māṅkāy>pt:manga>en:mango>tr:mango
papaya|n|es|papaya|papaya|MOD||
nektarin|n|en|nectarine|nektar gibi|MOD||grc:néktar>en:nectarine>tr:nektarin
kaju|n|pt|caju|kaju|NEW||tup:acajú>pt:caju>tr:kaju
kumkuat|n|en|kumquat|altın portakal|NEW||zh:gām-gwāt>en:kumquat>tr:kumkuat
hindistancevizi|n|tr|Hindistan cevizi|Hindistan cevizi|OSM||
yerfıstığı|n|tr|yer fıstığı|yer fıstığı|OSM|*fıstık|
şamfıstığı|n|tr|Şam fıstığı|Şam fıstığı|OSM|*fıstık|
antepfıstığı|n|tr|Antep fıstığı|Antep fıstığı|MOD|*fıstık|
yerelması|n|tr|yer elması|yer elması|OSM||
narenciye|n|ar|nāranciyya|turunçgiller|OSM19||fa:nārang>ar:nāranj>tr:narenciye
turunçgil|n|fa|turunc|turunç ailesi|TDK||
meyvelenmek|v|fa|mēva|meyve vermek|OSM||
# --- Sebzeler ve baklagiller ------------------------------------------------------------------
bakla|n|ar|bāqillāʾ|bakla|EAT||
baklagil|n|ar|bāqillāʾ|bakla ailesi|TDK||
bakliyat|n|ar|baqliyyāt|kuru sebzeler|OSM19||
börülce|n|unk|börülce|börülce|OSM||
soya|n|en|soy|soya|MOD||zh:jiàngyóu>ja:shōyu>nl:soja>en:soy>tr:soya
brokoli|n|it|broccoli|filizler|MOD||
karnabahar|n|ar|qarnabīṭ|karnabahar|OSM||
kereviz|n|fa|karafs|kereviz|EAT||
semizotu|n|tr|semiz otu|semiz ot|OSM|*ot|
tere|n|fa|tara|yeşillik|EAT||
dereotu|n|fa|tara|tere otu|OSM|*ot|
şerbetçiotu|n|tr|şerbetçi otu|şerbetçi otu|OSM|*ot|
kinoa|n|es|quinua|kinoa|NEW||unk:kinwa>es:quinua>tr:kinoa
şekerpancarı|n|tr|şeker pancarı|şeker pancarı|CUM||
trüf|n|fr|truffe|trüf|MOD||la:tuber>fr:truffe>tr:trüf
kornişon|n|fr|cornichon|küçük boynuz|MOD||la:cornu>fr:cornichon>tr:kornişon
hindiba|n|ar|hindibāʾ|hindiba|OSM||
radika|n|el|radíki|radika|OSM||la:radix>el:radíki>tr:radika
labada|n|el|lápatho|labada|OSM||
kenger|n|fa|kangar|kenger|OSM||
acur|n|ar|ʿajjūr|acur|OSM||
arpacık|n|tr|arpa|küçük soğan; göz arpacığı|OSM||
ebegümeci|n|tr|ebe gömeci|ebegümeci|OSM||
fiğ|n|el?|víkos|yem bitkisi|OSM||
burçak|n|tr|burçak|burçak|DLT||
koyungözü|n|tr|koyun gözü|papatya türü|OSM||
öküzgözü|n|tr|öküz gözü|iri papatya|OSM||
farekulağı|n|tr|fare kulağı|bir ot türü|OSM||
# --- Tahıllar ve taneler ----------------------------------------------------------------------
yulaf|n|ar?|ʿalaf|yem, ot|OSM||
karabuğday|n|tr|kara buğday|karabuğday|OSM|*kara|
sorgum|n|fr|sorgho|sorgum|MOD||it:sorgo>fr:sorgho>tr:sorgum
başak|n|tr|başak|başak|DLT|*baş|
başaklanmak|v|tr|başak|başak bağlamak|OSM|*baş|
kepek|n|tr|kepek|kepek|DLT||
nişasta|n|fa|nişāsta|nişasta|OSM||
çiğit|n|tr|çigit|pamuk çekirdeği|DLT||
çenek|n|tr|çeŋek|tohum yaprağı|TDK||
hububat|n|ar|ḥubūbāt|taneler|OSM|H-B-B|
habbe|n|ar|ḥabba|tane|EAT|H-B-B|
zahire|n|ar|ḏaḫīra|stok, azık|EAT||
tahıl|n|ar?|daḫl|gelir, ürün|OSM||
zerzevat|n|fa|sabzavāt|yeşillikler|OSM||
jüt|n|en|jute|jüt|MOD||
kınakına|n|es|quinaquina|kınakına|OSM19||unk:kinakina>es:quinaquina>tr:kınakına
# --- Baharat ve otlar -------------------------------------------------------------------------
karabiber|n|tr|kara biber|karabiber|OSM|*biber|
biberiye|n|tr|biber|biber gibi kokulu ot|OSM|*biber|
biberlik|n|tr|biber|biber kabı|OSM|*biber|
kişniş|n|fa|kişnīz|kişniş|OSM||
zerdeçal|n|fa|zard-çūb|sarı değnek|OSM||
sumak|n|ar|summāq|sumak|EAT||
çörekotu|n|tr|çörek otu|çörek otu|OSM|*ot|
anason|n|el|ánison|anason|EAT||
rezene|n|fa|rāziyāne|rezene|OSM||
kakule|n|ar|qāqulla|kakule|OSM||
yenibahar|n|tr|yeni bahar|yeni baharat|OSM||
muskat|n|fr|muscade|misk kokulu|OSM19||la:muscus>fr:muscade>tr:muskat
mahlep|n|ar|maḥlab|mahlep|OSM||
adaçayı|n|tr|ada çayı|ada çayı|OSM||
lavanta|n|it|lavanda|yıkama otu|OSM19||la:lavare>it:lavanda>tr:lavanta
melisa|n|fr|mélisse|arı (otu)|MOD||grc:mélissa>la:melissa>fr:mélisse>tr:melisa
papatya|n|el|papadía|papaz karısı; papatya|OSM||
devedikeni|n|tr|deve dikeni|devedikeni|OSM|*deve|
devetüyü|n|tr|deve tüyü|açık kahverengi|OSM|*deve|
deveboynu|n|tr|deve boynu|eğri boru|OSM|*deve|
hatmi|n|ar|ḫaṭmī|hatmi|OSM||
tarhun|n|fa|tarḫūn|tarhun|OSM||
zamk|n|ar|ṣamġ|ağaç yapışkanı|EAT||
# --- Çiçekler --------------------------------------------------------------------------------
leylak|n|fa|līlak|leylak|OSM||
orkide|n|fr|orchidée|orkide|CUM||grc:órkhis>la:orchis>fr:orchidée>tr:orkide
kardelen|n|tr|kar delen|kardelen|OSM||
krizantem|n|fr|chrysanthème|altın çiçek|CUM||grc:khrysánthemon>la:chrysanthemum>fr:chrysanthème>tr:krizantem
kasımpatı|n|tr|kasım patı|kasımpatı|OSM||
şebboy|n|fa|şab-bū|gece kokusu|OSM||
hanımeli|n|tr|hanım eli|hanımeli|OSM||
sarmaşık|n|tr|sarmaş-|sarılarak büyüyen bitki|OSM|*sar-|
begonya|n|fr|bégonia|Bégon çiçeği|MOD||
kamelya|n|fr|camélia|Kamel çiçeği|OSM19||
gardenya|n|fr|gardénia|Garden çiçeği|MOD||
dalya|n|fr|dahlia|Dahl çiçeği|MOD||
mimoza|n|fr|mimosa|taklitçi|CUM||la:mimus>fr:mimosa>tr:mimoza
ortanca|n|fr|hortensia|Hortense çiçeği|OSM19||
nilüfer|n|fa|nīlūfar|nilüfer|EAT||sa:nīlotpala>fa:nīlūfar>tr:nilüfer
lotus|n|fr|lotus|lotus|MOD||grc:lōtós>la:lotus>fr:lotus>tr:lotus
glayöl|n|fr|glaïeul|küçük kılıç|MOD||la:gladiolus>fr:glaïeul>tr:glayöl
ıtır|n|ar|ʿiṭr|güzel koku|OSM|A-T-R|
ıtriyat|n|ar|ʿiṭriyyāt|güzel kokular|OSM19|A-T-R|
petunya|n|fr|pétunia|tütün çiçeği|MOD||tup:petun>fr:pétunia>tr:petunya
hercai|adj|fa|harcāyī|her yerde olan|OSM||
çiğdem|n|tr|çigdem|çiğdem|OSM||
mine|n|fa|mīnā|sır, cam|EAT||
aslanağzı|n|tr|aslan ağzı|aslanağzı|OSM||
hüsnüyusuf|n|ar|ḥusn-i Yūsuf|Yusuf'un güzelliği|OSM||
ayçiçeği|n|tr|ay çiçeği|ayçiçeği|OSM|*çiçek|
günebakan|n|tr|güne bakan|ayçiçeği|OSM|*bak-|
şakayık|n|ar|şaqāʾiq|gelincik türleri|OSM||
erguvan|n|fa|arġavān|erguvan|EAT||
süsen|n|fa|sūsan|süsen|EAT||
zerrin|n|fa|zarrīn|altın renkli|OSM||
çiçeklenmek|v|tr|çeçek|çiçek açmak|OSM|*çiçek|
çiçekçi|n|tr|çeçek|çiçek satan|OSM|*çiçek|
çiçeklik|n|tr|çeçek|çiçek yeri|OSM|*çiçek|
gonca|n|fa|ġunça|tomurcuk|EAT||
tomurcuk|n|tr|tomur-|çiçek düğmesi|OSM|*tomur-|
tomurcuklanmak|v|tr|tomur-|tomurcuk vermek|OSM|*tomur-|
polen|n|fr|pollen|ince un|MOD||la:pollen>fr:pollen>tr:polen
tozlaşma|n|tr|toz|çiçek tozu aktarımı|DD||
nektar|n|fr|nectar|tanrı içkisi|MOD||grc:néktar>la:nectar>fr:nectar>tr:nektar
diken|n|tr|tiken|diken|DLT|*dik-|
dikenli|adj|tr|tiken|dikeni olan|OSM|*dik-|
# --- Bitki bölümleri ve süreçleri -------------------------------------------------------------
filiz|n|el?|phyllís|yaprakçık; taze sürgün|OSM||
filizlenmek|v|el?|phyllís|filiz vermek|OSM||
fide|n|el?|phyteía|dikim|OSM||
çimlenmek|v|tr|çim|filizlenmek|OSM|*çim|
çim|n|tr|çim|ince ot|OSM|*çim|
çimlendirmek|v|tr|çim|çimlenmesini sağlamak|TDK|*çim|
yaprakçık|n|tr|yapurgak|küçük yaprak|TDK|*yaprak|
yapraklanmak|v|tr|yapurgak|yaprak açmak|OSM|*yaprak|
yapraklı|adj|tr|yapurgak|yaprağı olan|OSM|*yaprak|
dallanmak|v|tr|tal|dal vermek|OSM||
köklenmek|v|tr|kök|kök salmak|OSM||
solmak|v|tr|sol-|canlılığını yitirmek|DLT|*sol-|
solgun|adj|tr|sol-|solmuş|OSM|*sol-|
soldurmak|v|tr|sol-|solmasına yol açmak|OSM|*sol-|
yumru|n|tr|yumru|şişkin kök|OSM||
reçine|n|fr|résine|reçine|CUM||grc:rhētínē>la:resina>fr:résine>tr:reçine
özsu|n|tr|öz su|bitki suyu|DD||
elyaf|n|ar|alyāf|lifler|OSM19|L-Y-F|
kıymık|n|tr|kıymık|ağaç parçası|OSM||
talaş|n|fa|tarāş|yontma|EAT||
liken|n|fr|lichen|liken|MOD||grc:leikhḗn>la:lichen>fr:lichen>tr:liken
eğrelti|n|tr|eğrelti|eğrelti otu|OSM||
küf|n|tr|küf|küf|EAT||
alg|n|fr|algue|su yosunu|MOD||la:alga>fr:algue>tr:alg
herbaryum|n|la|herbarium|ot deposu|MOD|herba|
herbisit|n|fr|herbicide|ot öldürücü|MOD|herba|
# --- Ek: yetiştiricilik, ırklar, davranışlar, bitki bilimi ------------------------------------
yelkovan|n|tr|yel kovan|yelkovan kuşu; saat ibresi|OSM|*yel|
kızkuşu|n|tr|kız kuşu|kızkuşu|OSM|*kuş|
pisi|n|tr|pisi|yavru kedi; pisi balığı|OSM||
trakonya|n|el|drákaina|dişi ejder; trakonya balığı|OSM||
melanur|n|el|melanoúri|kara kuyruk; melanur balığı|OSM||
menengiç|n|tr?|menengiç|yabani fıstık|OSM||
abanoz|n|ar|abanūs|abanoz|EAT||egy:hbny>grc:ébenos>ar:abanūs>tr:abanoz
pelesenk|n|ar|balasān|pelesenk ağacı|OSM||grc:bálsamon>ar:balasān>tr:pelesenk
sandal|n|ar|ṣandal|sandal ağacı; kayık|EAT||sa:candana>ar:ṣandal>tr:sandal
begonvil|n|fr|bougainvillée|Bougainville çiçeği|MOD||
yarpuz|n|tr|yarpuz|yabani nane|DLT||
mercanköşk|n|ar|marzanjūş|mercanköşk|OSM||fa:marzangōş>ar:marzanjūş>tr:mercanköşk
isot|n|tr|ısı ot|acı biber|MOD|*ot|
otlu|adj|tr|ot|otu olan|OSM|*ot|
irmik|n|tr?|irmik|iri un|OSM||
gelengi|n|tr|gelengi|tarla sincabı|OSM||
fino|n|it|fino|ince; süs köpeği|OSM19||
buldok|n|en|bulldog|boğa köpeği|MOD||
kaniş|n|fr|caniche|ördek köpeği|MOD||
hayvancılık|n|ar|ḥayawān|hayvan yetiştiriciliği|TDK|H-Y-Y|
arılık|n|tr|arı|arı kovanları yeri|OSM|*arı|
tavukçuluk|n|tr|takıġu|tavuk yetiştiriciliği|TDK||
ipekçilik|n|tr|yipek|ipek üretimi|TDK||
koyunculuk|n|tr|koñ|koyun yetiştiriciliği|TDK||
atçılık|n|tr|at|at yetiştiriciliği|TDK||
kırma|n|tr|kır-|melez; kırılmış|OSM|*kır-|
safkan|adj|ar|ṣāf|saf kanlı|OSM19||
propolis|n|fr|propolis|şehrin önü|NEW||grc:própolis>fr:propolis>tr:propolis
duyarga|n|tr|duy-|böcek anteni|DD||
sırım|n|tr|sırım|deri şerit|DLT||
fildişi|n|ar|fīl|fil dişi|OSM||
angora|n|fr|angora|Ankara (keçisi, kedisi)|OSM19||la:Ancyra>fr:angora>tr:angora
merinos|n|fr|mérinos|ince yünlü koyun|OSM19||es:merino>fr:mérinos>tr:merinos
karakul|n|tr|kara köl|Karakul koyunu|MOD|*kara|
kıvırcık|adj|tr|kıvır-|kıvrımlı; kıvırcık salata|OSM||
samanlık|n|tr|saman|saman deposu|OSM||
yalak|n|tr|yalak|hayvan su kabı|OSM||
ercik|n|tr|er|çiçeğin erkek organı|DD||
dişicik|n|tr|tişi|çiçeğin dişi organı|DD||
dişi|n|tr|tişi|dişi|DLT||
meyvecilik|n|fa|mēva|meyve yetiştiriciliği|TDK||
sebzecilik|n|fa|sabza|sebze yetiştiriciliği|TDK||
çiçekçilik|n|tr|çeçek|çiçek yetiştirme ve satma|TDK|*çiçek|
seracılık|n|fr|serre|sera yetiştiriciliği|MOD||
ormancılık|n|tr|orman|orman işletmeciliği|TDK||
fidanlık|n|el?|phytón|fidan yetiştirilen yer|OSM||
kompost|n|fr|compost|karışık; çürütülmüş gübre|NEW||la:compositus>fr:compost>tr:kompost
uçuşmak|v|tr|uç-|birlikte uçmak|OSM|*uç-|
ötüşmek|v|tr|öt-|birlikte ötmek|OSM|*öt-|
çöreklenmek|v|tr|çörek|halka olup yatmak|OSM||
gevelemek|v|tr|kev-|ağızda evirip çevirmek|OSM||
çifte|n|fa|cuft|hayvan tekmesi; çift namlulu tüfek|OSM|cuft|
evcilleşmek|v|tr|ev|evcil olmak|TDK||
evcilleştirmek|v|tr|ev|evcil duruma getirmek|TDK||
yabanileşmek|v|fa|yābān|yabani olmak|TDK|yābān|
üreme|n|tr|üre-|çoğalma|DD|*ür-|
sürüngenler|n|tr|sürün-|sürüngen sınıfı|DD|*sür-|
kuşbilim|n|tr|kuş|kuşları inceleyen bilim|DD|*kuş|
yırtıcılık|n|tr|yırt-|yırtıcı olma|TDK|*yırt-|
otobur|adj|tr|ot|ot yiyen|DD|*ot|
etobur|adj|tr|et|et yiyen|DD||
lor|n|fa|lōr|peynir suyu kesiği|OSM||
sütlük|n|tr|süt|süt kabı; süt veren|OSM||
kuzucuk|n|tr|kuzı|küçük kuzu; sevgi sözü|OSM|*kuzu|
yavruağzı|n|tr|yavru ağzı|açık pembe turuncu|OSM|*yavru|
kuşpalazı|n|tr|kuş palazı|difteri|OSM|*kuş|
ökseotu|n|el|iksós|ökse otu|OSM||
kuşyemi|n|tr|kuş yemi|kuş yemi|OSM|*yem|
zehirli|adj|fa|zahr|zehir içeren|OSM||
panzehir|n|fa|pād-zahr|zehir karşıtı|EAT||
timsahgözü|n|ar|timsāḥ|timsah gözü (çeşit)|OSM||
kedicik|n|tr|kedi|küçük kedi|OSM||
köpekçik|n|tr|köpek|küçük köpek|OSM||
kurtboğan|n|tr|kurt boğan|zehirli bitki|OSM|*kurt|
balözü|n|tr|bal özü|nektar|TDK|*bal|
arıkovanı|n|tr|arı kovanı|arı kovanı|OSM|*arı|
yemleme|n|tr|yem|yem verme|TDK|*yem|
kemirme|n|tr|kemir-|kemirme işi|TDK|*kemir-|
tüyleme|n|tr|tü|tüy yolma|TDK|*tüy|
boynuzsuz|adj|tr|müŋüz|boynuzu olmayan|OSM|*boynuz|
kılsız|adj|tr|kıl|kılı olmayan|OSM|*kıl|
yumurtacı|n|tr|yumurtga|yumurta satan|OSM|*yumurta|
kanatçık|n|tr|kanat|küçük kanat|TDK|*kanat|
budaklı|adj|tr|butak|budağı olan|OSM|*budak|
kamışçık|n|tr|kamış|küçük kamış|OSM|*kamış|
# --- Ek II: hastalıklar, mide bölümleri, yabani otlar, eski Türkçe av kuşları ----------------
kuduz|n|tr|kutuz|köpek hastalığı|DLT||
uyuz|n|tr|uduz|deri hastalığı|DLT||
sakağı|n|tr|sakağı|at hastalığı|OSM||
kırkbayır|n|tr|kırk bayır|geviş getirenlerin üçüncü midesi|OSM||
şirden|n|fa|şīrdān|süt kabı; dördüncü mide|OSM||
börkenek|n|tr|börk|başlık; ikinci mide|OSM||
toynaklı|adj|tr|tuynak|toynağı olan|TDK||
kiş|n|tr|kiş|samur|DLT||
turumtay|n|tr|turumtay|küçük doğan|DLT||
sorgun|n|tr|sorgun|bir söğüt türü|OSM||
ağaçkavunu|n|tr|ağaç kavunu|ağaç kavunu|OSM|*ağaç|
pelin|n|sl|pelin|pelin otu|OSM||
yavşan|n|tr|yavşan|pelin türü|DLT||
zahter|n|ar|zaʿtar|yabani kekik|OSM||
aspir|n|ar|ʿuṣfur|yalancı safran|OSM||
kafur|n|ar|kāfūr|kâfur|EAT||sa:karpūra>ar:kāfūr>tr:kafur
terebentin|n|fr|térébenthine|terebentin|OSM19||grc:terebínthinos>la:terebinthina>fr:térébenthine>tr:terebentin
sarısabır|n|tr|sarı sabır|aloe|OSM|*sarı|
kantaron|n|el|kentaúrion|kantaron otu|OSM||grc:kentaúreion>el:kentaúrion>tr:kantaron
kökboya|n|tr|kök boya|kök boyası bitkisi|OSM||
ayrık|n|tr|adır-|ayrık otu|OSM||
sütleğen|n|tr|süt|sütlü ot|OSM||
sinirotu|n|tr|sinir otu|sinirotu|OSM|*ot|
civanperçemi|n|fa|cavān|genç (perçemi)|OSM||
oğulotu|n|tr|oġul otu|melisa|OSM|*oğul|
karabaş|n|tr|kara baş|karabaş otu; köpek adı|OSM|*kara|
kuşkirazı|n|tr|kuş kirazı|kuş kirazı|OSM|*kuş|
yabangülü|n|fa|yābān|yaban gülü|OSM|yābān|
yabanhavucu|n|fa|yābān|yaban havucu|OSM|yābān|
kuzuotu|n|tr|kuzı|bir ot türü|OSM|*kuzu|
ördekgagası|n|tr|ördek gagası|yumurtlayan memeli|TDK||
ayıkulağı|n|tr|ayı kulağı|bir dağ bitkisi|OSM||
tırnaklı|adj|tr|tırŋak|tırnağı olan|OSM||
gevişgetiren|n|tr|keviş|geviş getiren hayvan|TDK||
bürküt|n|tr|bürküt|kaya kartalı|DLT||
# --- Ek III: bileşik hayvan ve bitki adları --------------------------------------------------
sakarca|n|tr|sakar|alnı beyaz kaz|OSM||
yeşilbaş|n|tr|yeşil baş|yaban ördeği|OSM|*baş|
tahtalı|n|tr|tahta|tahtalı güvercin|OSM||
sumru|n|tr|sumru|deniz kırlangıcı|OSM||
yağmurkuşu|n|tr|yağmur kuşu|yağmurkuşu|OSM|*kuş|
ishakkuşu|n|tr|İshak kuşu|küçük baykuş|OSM|*kuş|
kızılgerdan|n|tr|kızıl gerdan|kızılgerdan kuşu|OSM|*kızıl|
kamışçın|n|tr|kamış|kamış bülbülü|OSM|*kamış|
çıvgın|n|tr|çıvgın|çıvgın kuşu|OSM||
arıkuşu|n|tr|arı kuşu|arıkuşu|OSM|*arı|
çakırkanat|n|tr|çakır kanat|bir ördek türü|OSM|*kanat|
kılkuyruk|n|tr|kıl kuyruk|bir ördek türü|OSM|*kuyruk|
dikkuyruk|n|tr|dik kuyruk|bir ördek türü|OSM|*kuyruk|
karıncayiyen|n|tr|karınca yiyen|karıncayiyen|TDK||
denizkulağı|n|tr|deniz kulağı|deniz kulağı|TDK|*deniz|
denizhıyarı|n|tr|deniz hıyarı|deniz hıyarı|TDK|*deniz|
denizgergedanı|n|tr|deniz gergedanı|deniz gergedanı|TDK|*deniz|
denizkızı|n|tr|deniz kızı|deniz kızı|OSM|*deniz|
mayısböceği|n|tr|mayıs böceği|mayısböceği|OSM|*böcek|
gübreböceği|n|tr|gübre böceği|gübreböceği|OSM|*böcek|
geyikböceği|n|tr|geyik böceği|geyikböceği|OSM|*böcek|
yaprakbiti|n|tr|yaprak biti|yaprakbiti|TDK|*yaprak|
karayemiş|n|tr|kara yemiş|karayemiş|OSM|*kara|
karamuk|n|tr|karamuk|karamuk otu|OSM||
karaçalı|n|tr|kara çalı|karaçalı|OSM|*çalı|
akdiken|n|tr|ak tiken|akdiken|OSM|*dik-|
karadiken|n|tr|kara tiken|karadiken|OSM|*kara|
ateşdikeni|n|tr|ateş dikeni|ateşdikeni|OSM|*dik-|
danaayağı|n|tr|dana ayağı|danaayağı bitkisi|OSM||
eşekhıyarı|n|tr|eşek hıyarı|eşekhıyarı|OSM||
kediotu|n|tr|kedi otu|kediotu|OSM|*ot|
köpeküzümü|n|tr|köpek üzümü|köpeküzümü|OSM|*üzüm|
kuzgunkılıcı|n|tr|kuzgun kılıcı|kuzgunkılıcı|OSM||
tavşankulağı|n|tr|tavşan kulağı|siklamen|OSM||
turnagagası|n|tr|turna gagası|turnagagası|OSM||
yılanyastığı|n|tr|yılan yastığı|yılanyastığı|OSM|*yılan|
atkestanesi|n|tr|at kestanesi|atkestanesi|OSM|*ağaç|
kırkkilit|n|tr|kırk kilit|atkuyruğu bitkisi|OSM||
boruçiçeği|n|tr|boru çiçeği|boruçiçeği|OSM|*çiçek|
yıldızçiçeği|n|tr|yıldız çiçeği|dalya|OSM|*çiçek|
kadifeçiçeği|n|tr|kadife çiçeği|kadifeçiçeği|OSM|*çiçek|
çuhaçiçeği|n|tr|çuha çiçeği|çuhaçiçeği|OSM|*çiçek|
kınaçiçeği|n|tr|kına çiçeği|kınaçiçeği|OSM|*çiçek|
küpeçiçeği|n|tr|küpe çiçeği|küpeçiçeği|OSM|*çiçek|
akşamsefası|n|tr|akşam sefası|akşamsefası|OSM||
gündüzsefası|n|tr|gündüz sefası|gündüzsefası|OSM||
lifli|adj|ar|līf|lifi olan|OSM|L-Y-F|
# --- Ek IV: yeniden eklenen temel maddeler ------------------------------------------------------
akrep|n|ar|ʿaqrab|akrep|EAT||
çekirdek|n|tr|çekirdek|çekirdek|EAT||
sedef|n|ar|ṣadaf|deniz kabuğu|EAT||
ağıl|n|tr|agıl|koyun barınağı|DLT||
taşlık|n|tr|taş|kuş katısı|OSM||
yabanıl|adj|fa|yābān|kıra ait, evcil olmayan|DD|yābān|
kuşluk|n|tr|kuşluk|sabahın ilerleyen saati|DLT|*kuş|
çalı|n|tr|çalı|çalı|OSM|*çalı|
çalılık|n|tr|çalı|çalı alanı|OSM|*çalı|
ağaçlık|n|tr|ıgaç|ağaçlı yer|OSM|*ağaç|
çamlık|n|tr|çam|çam ormanı|OSM|*çam|
kamışlık|n|tr|kamış|kamış alanı|OSM|*kamış|
sazlık|n|tr|saz|sazlı alan|OSM||
meşelik|n|tr|meşe|meşe ormanı|OSM||
kavaklık|n|tr|kavak|kavak korusu|OSM||
zeytinlik|n|tr|zeytin|zeytin bahçesi|OSM||
fındıklık|n|tr|fındık|fındık bahçesi|OSM||
kışlamak|v|tr|kışla-|kışı geçirmek|DLT|*kış|
yaylamak|v|tr|yayla-|yazı yaylada geçirmek|DLT|*yay|
yaylak|n|tr|yaylaġ|yaz otlağı|DLT|*yay|
"""

FAMILIES = r"""
*kuş|tr|kuş|Orhun Yazıtları'nda da geçen kuş sözü; baykuş, kuşluk, kuşbaşı, yağmurkuşu, ishakkuşu, kuşburnu, kuşkonmaz, kuşbakışı, kuşçu, kızkuşu ve ardıçkuşu aynı kökten gelir.
*sağ-|tr|süt sağmak|Eski Türkçe sag- "sağmak"; sağmak, sağım ve sağmal (sağılan hayvan) aynı kökten türer.
*yavru|tr|hayvan çocuğu|Türkçe yavru "hayvan çocuğu"; yavrulamak, yavrucak ve yavruağzı (renk) aynı kökten gelir.
*boynuz|tr|boynuz|Eski Türkçe müŋüz, sonra boynuz; boynuzlamak, boynuzlu, boynuzsuz ve tekboynuz aynı kökten türer.
*kuyruk|tr|kuyruk|Eski Türkçe kudruk "kuyruk"; kuyruklu, kuyruksuz, kuyrukkakan (kuş), atkuyruğu ve tilkikuyruğu (bitki) aynı kökten gelir.
*tüy|tr|tüy, kıl|Eski Türkçe tü "kıl, tüy"; tüylü, tüysüz, tüylenmek, tüyleme ve kuştüyü aynı kökten türer.
*kanat|tr|kanat|Dîvânu Lugâti't-Türk'te kanat; kanatlı, kanatsız, kanatlanmak, kanatçık ve kınkanatlı aynı kökten gelir.
*yaprak|tr|yaprak|Eski Türkçe yapurgak "yaprak"; yaprakçık, yapraklı ve yapraklanmak aynı kökten türer.
*yılan|tr|yılan|Eski Türkçe yılan; yılanbalığı, yılanyastığı (bitki) ve yılancık (deri hastalığı) aynı kökten gelir.
*böcek|tr|böcek|Türkçe böcek; böcü, böcekçil, ipekböceği, ateşböceği, uğurböceği, hamamböceği, cırcırböceği, ağustosböceği, mayısböceği, geyikböceği ve sümüklüböcek aynı kökten türer.
*ısır-|tr|dişle kavramak|Eski Türkçe ısır- "ısırmak"; ısırgan (ısıran ot) ve ısırık aynı kökten gelir.
*sok-|tr|batırmak|Eski Türkçe sok- "sokmak, batırmak"; sokmak (iğne batırmak), sokulmak ve sokulgan aynı kökten türer.
*kemir-|tr|dişle aşındırmak|Türkçe kemir-; kemirmek, kemirgen (kemiren hayvan) ve kemirme aynı kökten gelir.
*yırt-|tr|parçalamak|Eski Türkçe yırt- "yırtmak"; yırtmak, yırtık, yırtıcı ve yırtıcılık aynı kökten türer.
*öt-|tr|kuş sesi çıkarmak|Eski Türkçe öt- "ötmek"; ötmek, ötücü, ötüş, ötüşmek ve ötleğen (kuş) aynı kökten gelir.
*tüne-|tr|gece konmak|Eski Türkçe tün "gece" ile ilgili tüne-; tünemek ve tünek (kuşun gece konduğu yer) aynı kökten türer.
*kırk-|tr|yün kesmek|Eski Türkçe kırk- "kırkmak"; kırkmak ve kırkım (yün kesme mevsimi) aynı kökten gelir.
*güt-|tr|sürü yönetmek|Eski Türkçe küd- "gütmek, gözetmek"; gütmek, güdüm ve güdümlü aynı kökten türer.
*ot|tr|yeşil bitki|Orhun Yazıtları'ndaki ot "bitki"; otlamak, otlatmak, otçul, otobur, otlu, isot, semizotu, çörekotu, dereotu, sinirotu ve şerbetçiotu aynı kökten gelir.
*yem|tr|hayvan yiyeceği|Eski Türkçe yem "yiyecek"; yemlik, yemlemek, yemleme ve kuşyemi aynı kökten türer.
*av|tr|av|Eski Türkçe av; avlak (av yeri) ve avlanmak aynı kökten gelir.
*bal|tr|bal|Dîvânu Lugâti't-Türk'te bal; balmumu, balözü, ballıbaba ve balkabağı aynı kökten türer.
*arı|tr|bal yapan böcek|Eski Türkçe arı; balarısı, eşekarısı, yabanarısı, arıkovanı, arılık ve arıcılık aynı kökten gelir.
*deniz|tr|deniz|Eski Türkçe teŋiz "deniz"; denizanası, denizyıldızı, denizkestanesi, denizaslanı, denizatı, deniztarağı, denizkulağı, denizhıyarı ve denizkızı aynı kökten türer.
*balık|tr|balık|Orhun Yazıtları'ndaki balık; balıkçıl, balıkçılık, köpekbalığı, kılıçbalığı, ayıbalığı ve mürekkepbalığı aynı kökten gelir.
*kara|tr|siyah|Eski Türkçe kara "siyah"; karabatak, karatavuk, karasinek, karaağaç, karabuğday, karadut, karayemiş, karadiken, karabaş ve karakul aynı kökten türer.
*kızıl|tr|kırmızı|Eski Türkçe kızıl "kırmızı"; kızılcık, kızılağaç ve kızılçam aynı kökten gelir.
yābān|fa|ıssız kır|Farsça yābān "çöl, kır"; yabanıl, yabandomuzu, yabankedisi, yabankeçisi, yabanmersini, yabangülü, yabanhavucu ve yabanileşmek aynı kökten türer.
*keçi|tr|keçi|Dîvânu Lugâti't-Türk'te keçi; keçiboynuzu, keçiyolu ve keçisakalı aynı kökten gelir.
*koç|tr|erkek koyun|Eski Türkçe koç; koç ve koçbaşı (kale dövme aracı) aynı kökten türer.
*buzağı|tr|sığır yavrusu|Eski Türkçe buzagu; buzağı ve buzağılamak aynı kökten gelir.
*kuzu|tr|koyun yavrusu|Eski Türkçe kuzı; kuzulamak, kuzucuk, kuzukulağı, kuzugöbeği ve kuzuotu aynı kökten türer.
*deve|tr|deve|Orhun Yazıtları'ndaki tebe "deve"; devekuşu, devedikeni, devetüyü, deveboynu ve peygamberdevesi aynı kökten gelir.
*ağaç|tr|ağaç|Eski Türkçe ıgaç "ağaç"; ağaçkakan, ağaçlık, ağaçlandırmak, akçaağaç, atkestanesi ve ağaçkavunu aynı kökten türer.
*çalı|tr|çalı|Türkçe çalı; çalılık, çalıkuşu ve karaçalı aynı kökten gelir.
*budak|tr|dal|Eski Türkçe butak "dal"; budanmak, budaklı ve dişbudak aynı kökten türer.
*tomur-|tr|şişip çıkmak|Türkçe tomur- "kabarmak"; tomurcuk ve tomurcuklanmak aynı kökten gelir.
*çim|tr|ince ot|Türkçe çim; çimlenmek ve çimlendirmek aynı kökten türer.
*kamış|tr|kamış|Dîvânu Lugâti't-Türk'te kamış; kamışlık, kamışçık, kamışçın (kuş) ve şekerkamışı aynı kökten gelir.
*baş|tr|baş|Orhun Yazıtları'ndaki baş; başak (başçık), başaklanmak ve baştankara (kuş) aynı kökten türer.
*yumurta|tr|yumurta|Eski Türkçe yumurtga; yumurtlamak, yumurtalık ve yumurtacı aynı kökten gelir.
*kıl|tr|ince tüy|Eski Türkçe kıl; kılçık, kıllanmak ve kılsız aynı kökten türer.
*eyer|tr|at oturağı|Eski Türkçe eder "eyer"; eyer ve eyerlemek aynı kökten gelir.
*kamçı|tr|kamçı|Dîvânu Lugâti't-Türk'te kamçı; kamçı ve kamçılamak aynı kökten türer; Rusça kamça ve Bulgarca kamşik de bu sözden alınmıştır.
*besle-|tr|yedirip büyütmek|Türkçe besle-; besi (semirtme) ve besili aynı kökten gelir.
W-H-Ş|ar|yabanıl olmak|Arapça w-ḥ-ş kökü; vahşi (yabani) ve vahşet (yabanilik, ıssızlık) aynı kökten gelir.
A-H-L|ar|aile, yakınlık|Arapça a-h-l kökü; ehli (aileye ait; evcil), ehlileştirmek ve ehlileşmek aynı kökten türer.
H-Ş-R|ar|toplanmak, kaynaşmak|Arapça ḥ-ş-r kökü; haşere (böcek) ve haşerat (böcekler) aynı kökten gelir.
H-B-B|ar|tane|Arapça ḥ-b-b "tane" kökü; habbe (tane) ve hububat (taneler, tahıllar) aynı kökten türer.
L-Y-F|ar|lif|Arapça l-y-f kökü; lifli ve çoğul biçim elyaf aynı kökten gelir.
A-T-R|ar|güzel koku|Arapça ʿ-ṭ-r kökü; ıtır (hem koku hem bitki) ve ıtriyat aynı kökten türer.
herba|la|ot|Latince herba "ot"; herbaryum (bitki koleksiyonu) ve herbisit (ot öldürücü) aynı kökten gelir.
*yüz-|tr|suda ilerlemek|Eski Türkçe yüz- "yüzmek"; yüzmek, yüzücü ve yüzgeç (balığın yüzme organı) aynı kökten türer.
*solu-|tr|nefes almak|Eski Türkçe solu-; solumak, solunum ve solungaç (balığın soluma organı) aynı kökten gelir.
*sığır|tr|sığır|Eski Türkçe sıgır; sığırtmaç (güden), sığırcık (kuş), sığırdili ve sığırkuyruğu (bitkiler) aynı kökten türer.
*kurt|tr|kurt; böcek kurdu|Orhun Yazıtları'ndaki kurt hem yırtıcı hayvanı hem böcek kurdunu karşılar; kurtçuk, kurtlanmak, kurtbağrı, kurtboğan ve tahtakurusu aynı kökten gelir.
*ala|tr|benekli, karışık renkli|Eski Türkçe ala "alacalı"; alageyik, aladoğan ve alakarga aynı kökten türer.
*çiçek|tr|çiçek|Eski Türkçe çeçek; çiçeklenmek, çiçekçi, çiçeklik, çiçekçilik, ayçiçeği, kadifeçiçeği, küpeçiçeği ve yıldızçiçeği aynı kökten gelir.
*kurbağa|tr|kurbağa|Dîvânu Lugâti't-Türk'te kurbaka; kurbağa ve kurbağalama (yüzme biçimi) aynı kökten türer.
*cıv|tr|kuş sesi yansıması|Yansıma cıv/civ sesi; civciv, cıvıldamak ve cıvıltı aynı kökten gelir.
*vız|tr|böcek sesi yansıması|Yansıma vız sesi; vızıldamak ve vızıltı aynı kökten türer.
*böğür-|tr|sığır sesi çıkarmak|Eski Türkçe bögür-; böğürmek ve böğürtü aynı kökten gelir.
panca|fa|beş; el, pençe|Farsça panc "beş" ve panca "el"; pençe, pençelemek, pençeleşmek ve aslanpençesi aynı kökten türer.
*sinek|tr|sinek|Eski Türkçe siŋek; sivrisinek, sineklik, sinekkuşu ve sinekkapan aynı kökten gelir.
*salkım|tr|üzüm salkımı|Eski Türkçe salkım; salkımsöğüt ve salkımsaçak aynı kökten türer.
*çam|tr|çam|Türkçe çam; çamlık, çamfıstığı, çamsakızı, karaçam ve sarıçam aynı kökten gelir.
*üzüm|tr|üzüm|Eski Türkçe üzüm; kuşüzümü, frenküzümü, bektaşiüzümü ve itüzümü aynı kökten türer.
*fıstık|ar|fıstık|Arapça fustuq, Yunanca pistákion'dan; yerfıstığı, şamfıstığı ve antepfıstığı aynı kökten gelir.
*biber|el|biber|Yunanca pipéri "biber"; karabiber, biberiye ve biberlik aynı kökten türer.
*döl|tr|yavru, soy|Eski Türkçe töl "döl"; döllemek ve dölüt (cenin) aynı kökten gelir.
*sol-|tr|canlılığını yitirmek|Eski Türkçe sol- "solmak"; solmak, solgun ve soldurmak aynı kökten türer.
*sarı|tr|sarı|Eski Türkçe sarıg "sarı"; sarıasma (kuş), sarıkanat (balık) ve sarısabır (bitki) aynı kökten gelir.
*boz|tr|gri, boz|Eski Türkçe boz; bozayı ve bozkurt aynı kökten türer.
"""

COGNATES = r"""
@porsuk shared_ancestor
  az porsuq ; porsuk
  kk борсық [borsıq] ; porsuk
  uz boʻrsiq ; porsuk
  ky борсук [borsuk] ; porsuk
  tk torsuk ; porsuk
  ru барсук [barsuk] ; porsuk ; ff:Rusça barsuk Türk dillerinden alınmıştır; Slav kökenli değildir
  uk борсук [borsuk] ; porsuk
@kunduz shared_ancestor
  az qunduz ; kunduz
  kk құндыз [qundız] ; kunduz
  uz qunduz ; kunduz
  ky кундуз [kunduz] ; kunduz
  tk gunduz ; kunduz
@sıçan shared_ancestor
  az siçan ; sıçan
  kk тышқан [tışqan] ; fare, sıçan ; ff:Kazakçada tışqan hem fare hem sıçan için kullanılır
  uz sichqon ; sıçan
  ky чычкан [çıçkan] ; fare, sıçan
  tk syçan ; sıçan
@kirpi shared_ancestor
  az kirpi ; kirpi
  kk кірпі [kirpi] ; kirpi
  uz kirpi ; kirpi
  ky кирпи [kirpi] ; kirpi
  tk kirpi ; kirpi
@köstebek shared_ancestor
  az köstəbək ; köstebek
  kk көртышқан [körtışqan] ; köstebek ; ff:Kazakçada "kör sıçan" bileşiği kullanılır; köstebek sözü yoktur
  tk körsyçan ; köstebek ; ff:Türkmencede "kör sıçan" bileşiği kullanılır
@yarasa shared_ancestor
  az yarasa ; yarasa
  kk жарқанат [jarqanat] ; yarasa ; ff:Kazakça "yarık kanat" bileşiği; Türkçe yarasa ile aynı söz değildir
  tk ýarganat ; yarasa ; ff:Türkmence "yarık kanat" bileşiğidir
@pars shared_ancestor
  kk барыс [barıs] ; kar leoparı ; ff:Kazakçada barıs özellikle kar leoparını adlandırır; Kazakistan'ın simgesidir
  ky барс [bars] ; leopar
  mn барс [bars] ; leopar, kaplan
  ru барс [bars] ; kar leoparı ; ff:Rusçaya Türk dillerinden geçmiştir
@çakal into_turkish
  fa شغال [şaġāl] ; çakal
  az çaqqal ; çakal
  ru шакал [şakal] ; çakal
  bg чакал [çakal] ; çakal
  sr шакал [šakal] ; çakal
  el τσακάλι [tsakáli] ; çakal
  ro șacal ; çakal
  hu sakál ; çakal
  en jackal ; çakal
  fr chacal ; çakal
  ur گیدڑ [gīdaṛ] ; çakal ; ff:Urduca başka bir kök kullanır; Farsça şaġāl ile ilgisi yoktur
@gergedan into_turkish
  fa کرگدن [kargadan] ; gergedan
  ar كركدن [karkaddan] ; gergedan
  az kərgədan ; gergedan
  uz karkidon ; gergedan
@fil into_turkish
  ar فيل [fīl] ; fil
  fa فیل [fīl] ; fil
  az fil ; fil
  uz fil ; fil
  kk піл [pil] ; fil
  ky пил [pil] ; fil
  tk pil ; fil
  ur فیل [fīl] ; fil (edebî) ; ff:Urducada günlük sözcük hāthī'dir; fīl daha çok satrançta kullanılır
@maymun shared_ancestor
  ar ميمون [maymūn] ; uğurlu, kutlu ; ff:Arapçada asıl anlam "uğurlu"dur; hayvan adı olarak kullanımı örtmece kaynaklıdır
  fa میمون [meymūn] ; maymun
  az meymun ; maymun
  uz maymun ; maymun
  kk маймыл [maymıl] ; maymun
  ky маймыл [maymıl] ; maymun
  tk maýmyn ; maymun
  bg маймуна [maymuna] ; maymun
  sr мајмун [majmun] ; maymun
  mk мајмун [majmun] ; maymun
  sq majmun ; maymun
  ro maimuță ; maymun
  el μαϊμού [maïmoú] ; maymun
@zürafa shared_ancestor
  ar زرافة [zarāfa] ; zürafa
  fa زرافه [zarāfe] ; zürafa
  az zürafə ; zürafa
  it giraffa ; zürafa
  es jirafa ; zürafa
  fr girafe ; zürafa
  en giraffe ; zürafa
  de Giraffe ; zürafa
  ru жираф [jiraf] ; zürafa
@timsah into_turkish
  ar تمساح [timsāḥ] ; timsah
  fa تمساح [temsāh] ; timsah
  az timsah ; timsah
  uz timsoh ; timsah
  kk қолтырауын [qoltırauın] ; timsah ; ff:Kazakça başka bir söz kullanır
@akrep into_turkish
  ar عقرب [ʿaqrab] ; akrep
  fa عقرب [ʿaqrab] ; akrep
  az əqrəb ; akrep
  ur عقرب [aqrab] ; akrep
  he עקרב [aqrav] ; akrep ; ff:İbranice biçim Arapça ile ortak Sami köktendir
  uz chayon ; akrep ; ff:Özbekçe Türkçe kökenli çayan sözünü kullanır; Türkiye Türkçesinde çıyan başka bir hayvandır
@tavus into_turkish
  fa طاووس [tāvūs] ; tavus kuşu
  ar طاووس [ṭāwūs] ; tavus kuşu
  az tovuz ; tavus kuşu
  uz tovus ; tavus kuşu
  kk тауыс [tawıs] ; tavus kuşu
  el παγώνι [pagóni] ; tavus kuşu ; ff:Modern Yunanca Latince pavo'dan gelen başka bir söz kullanır; eski taṓs unutulmuştur
@papağan shared_ancestor
  ar ببغاء [babbaġāʾ] ; papağan
  bg папагал [papagal] ; papağan
  sr папагај [papagaj] ; papağan
  mk папагал [papagal] ; papağan
  sq papagall ; papağan
  ro papagal ; papağan
  hu papagáj ; papağan
  el παπαγάλος [papagálos] ; papağan
  it pappagallo ; papağan
  es papagayo ; papağan
  pt papagaio ; papağan
  az tutuquşu ; papağan ; ff:Azerbaycan Türkçesi Farsça tūtī kökünü kullanır
@kumru into_turkish
  ar قمري [qumrī] ; kumru
  fa قمری [qomrī] ; kumru
  az qumru ; kumru
@leylek shared_ancestor
  fa لکلک [laklak] ; leylek
  ar لقلق [laqlaq] ; leylek
  az leylək ; leylek
  uz laylak ; leylek
  kk ләйлек [läylek] ; leylek
  tk leglek ; leylek
  el λελέκι [lelékı] ; leylek ; ff:Yunancaya Türkçeden geçmiştir; asıl Yunanca söz pelargós'tur
  sq lejlek ; leylek
@karga shared_ancestor
  az qarğa ; karga
  kk қарға [qarğa] ; karga
  uz qargʻa ; karga
  ky карга [karga] ; karga
  tk garga ; karga
  ru карга [karga] ; kocakarı, cadı ; ff:Rusçaya Türkçeden geçen karga "huysuz yaşlı kadın" anlamına kaymıştır
@kuzgun shared_ancestor
  az quzğun ; kuzgun
  kk құзғын [quzğın] ; kuzgun
  uz quzgʻun ; kuzgun
  ky кузгун [kuzgun] ; kuzgun
  tk guzgun ; kuzgun
@saksağan shared_ancestor
  az sağsağan ; saksağan
  kk сауысқан [sawısqan] ; saksağan
  uz zagʻizgʻon ; saksağan
  ky сагызган [sagızgan] ; saksağan
@serçe shared_ancestor
  az sərçə ; serçe
  tk serçe ; serçe
  kk торғай [torğay] ; serçe ; ff:Kazakça torğay başka bir Türkçe köktendir
  uz chumchuq ; serçe ; ff:Özbekçe yansıma kökenli başka bir söz kullanır
@kırlangıç shared_ancestor
  az qaranquş ; kırlangıç ; ff:Azerbaycan Türkçesinde "kara kuş" bileşiğine dönüşmüştür
  kk қарлығаш [qarlığaş] ; kırlangıç
  uz qaldirgʻoch ; kırlangıç
  ky карлыгач [karlıgaç] ; kırlangıç
  tk garlawaç ; kırlangıç
@baykuş shared_ancestor
  az bayquş ; baykuş
  tk baýguş ; baykuş
  kk байғұс [bayğus] ; zavallı, biçare ; ff:Kazakçada bayğus "zavallı" anlamına kaymıştır; baykuş için үкі kullanılır
@bıldırcın shared_ancestor
  az bildirçin ; bıldırcın
  kk бөдене [bödene] ; bıldırcın ; ff:Kazakça başka bir Türkçe kök (bödene) kullanır
  uz bedana ; bıldırcın
  tk bedene ; bıldırcın
@keklik shared_ancestor
  az kəklik ; keklik
  kk кекілік [kekilik] ; keklik
  uz kaklik ; keklik
  ky кекилик [kekilik] ; keklik
  tk käkilik ; keklik
@kuğu shared_ancestor
  az qu ; kuğu
  kk аққу [aqqu] ; kuğu ; ff:Kazakçada "ak kuğu" bileşiği tek sözcük olmuştur
  uz oqqush ; kuğu ; ff:Özbekçe "ak kuş" bileşiği kullanır
  ky аккуу [akkuu] ; kuğu
  tk guw ; kuğu
@sungur shared_ancestor
  kk сұңқар [suŋqar] ; sungur, akdoğan
  ky шумкар [şumkar] ; sungur
  uz shunqor ; sungur
  mn шонхор [şonhor] ; sungur ; ff:Moğolcaya Türk dillerinden geçmiştir
@laçin shared_ancestor
  az laçın ; şahin
  kk лашын [laşın] ; şahin
  uz lochin ; şahin
  ky ылаачын [ılaaçın] ; şahin
  tk laçyn ; şahin
@devekuşu shared_ancestor
  az dəvəquşu ; devekuşu
  kk түйеқұс [tüyequs] ; devekuşu
  uz tuyaqush ; devekuşu
  ky төө куш [töö kuş] ; devekuşu
  tk düýeguş ; devekuşu
@kerkenez into_turkish
  el κιρκινέζι [kirkinézi] ; kerkenez
  bg керкенез [kerkenez] ; kerkenez ; ff:Bulgarcaya Türkçe yoluyla geçmiştir
@ispinoz into_turkish
  el σπίνος [spínos] ; ispinoz
@kanarya shared_ancestor
  it canarino ; kanarya
  es canario ; kanarya
  fr canari ; kanarya
  en canary ; kanarya
  de Kanarienvogel ; kanarya
  el καναρίνι [kanaríni] ; kanarya
  bg канарче [kanarçe] ; kanarya
  ru канарейка [kanareyka] ; kanarya
@balina shared_ancestor
  it balena ; balina
  es ballena ; balina
  pt baleia ; balina
  fr baleine ; balina
  ro balenă ; balina
  sq balenë ; balina
  el φάλαινα [fálaina] ; balina ; ff:Eski Yunanca phállaina tüm Latin biçimlerinin kaynağıdır
@istiridye shared_ancestor
  el στρείδι [strídi] ; istiridye
  it ostrica ; istiridye
  es ostra ; istiridye
  pt ostra ; istiridye
  fr huître ; istiridye
  ro stridie ; istiridye
  bg стрида [strida] ; istiridye
@salyangoz into_turkish
  el σαλιγκάρι [saligári] ; salyangoz
@somon shared_ancestor
  fr saumon ; somon
  en salmon ; somon
  it salmone ; somon
  es salmón ; somon
  pt salmão ; somon
  ro somon ; somon
  ru сёмга [syomga] ; somon ; ff:Rusça başka bir Fin kökenli söz kullanır
@ton shared_ancestor
  fr thon ; ton balığı
  it tonno ; ton balığı
  es atún ; ton balığı ; ff:İspanyolca biçim Arapça tanımlık (al-) ile kaynaşmıştır
  pt atum ; ton balığı
  en tuna ; ton balığı
  el τόνος [tónos] ; ton balığı
@zargana into_turkish
  el ζαργάνα [zargána] ; zargana
@kolyoz into_turkish
  el κολιός [koliós] ; kolyoz
@orfoz into_turkish
  el ορφός [orfós] ; orfoz
@lagos into_turkish
  el λαγός [lagós] ; tavşan ; ff:Yunanca lagós "tavşan" demektir; Türkçede yalnızca balık adı olmuştur
@iskorpit into_turkish
  el σκορπίνα [skorpína] ; iskorpit
  it scorfano ; iskorpit
@vatoz into_turkish
  el βάτος [vátos] ; vatoz
@sinarit into_turkish
  el συναγρίδα [synagrída] ; sinarit
@fangri into_turkish
  el φαγκρί [fagkrí] ; fangri
@sargoz shared_ancestor
  el σαργός [sargós] ; sargoz
  it sarago ; sargoz
  es sargo ; sargoz
@mırmır shared_ancestor
  el μουρμούρα [mourmoúra] ; mırmır
  it mormora ; mırmır
@sarpa shared_ancestor
  el σάλπα [sálpa] ; sarpa
  it salpa ; sarpa
  es salpa ; sarpa
@izmarit into_turkish
  el σμαρίδα [smarída] ; izmarit
@tirsi into_turkish
  el θρίσσα [thríssa] ; tirsi
@hani into_turkish
  el χάνος [khános] ; hani balığı
@lapina into_turkish
  el λαπίνα [lapína] ; lapina
@trakonya into_turkish
  el δράκαινα [drákaina] ; dişi ejder; trakonya ; ff:Yunancada asıl anlam "dişi ejder"dir
@melanur into_turkish
  el μελανούρι [melanoúri] ; kara kuyruk; melanur
@kerevit into_turkish
  el καραβίδα [karavída] ; kerevit
@mersin shared_ancestor
  el μυρτιά [myrtiá] ; mersin ağacı
  it mirto ; mersin
  es mirto ; mersin
  fr myrte ; mersin
  en myrtle ; mersin
  de Myrte ; mersin
@havyar shared_ancestor
  fa خاویار [xāviyār] ; havyar
  it caviale ; havyar
  fr caviar ; havyar
  en caviar ; havyar
  el χαβιάρι [khaviári] ; havyar
  ru икра [ikra] ; havyar ; ff:Rusça başka bir söz kullanır; havyar sözü Rusçada yoktur
@böcek shared_ancestor
  az böcək ; böcek
  ky бөжөк [böjök] ; küçük böcek, haşere
  kk бөжек [böjek] ; yavru, küçük yaratık ; ff:Kazakçada "yavru, ufaklık" anlamına kaymıştır
@çekirge shared_ancestor
  az çəyirtkə ; çekirge
  kk шегіртке [şegirtke] ; çekirge
  uz chigirtka ; çekirge
  ky чегиртке [çegirtke] ; çekirge
  tk çekirtge ; çekirge
@kene shared_ancestor
  az gənə ; kene
  kk кене [kene] ; kene
  uz kana ; kene
  ky кене [kene] ; kene
  tk sakyrtga ; kene ; ff:Türkmence başka bir söz kullanır
@pire shared_ancestor
  az birə ; pire
  kk бүрге [bürge] ; pire
  uz burga ; pire
  ky бүргө [bürgö] ; pire
  tk büre ; pire
@güve shared_ancestor
  az güvə ; güve
  kk күйе [küye] ; güve
  uz kuya ; güve
  ky күбө [kübö] ; güve
  tk güýe ; güve
@sülük shared_ancestor
  kk сүлік [sülik] ; sülük
  uz zuluk ; sülük
  ky сүлүк [sülük] ; sülük
  tk sülük ; sülük
  az zəli ; sülük ; ff:Azerbaycan Türkçesi Farsça zalū kökünü kullanır
@kurbağa shared_ancestor
  az qurbağa ; kurbağa
  kk құрбақа [qurbaqa] ; kara kurbağa ; ff:Kazakçada qurbaqa özellikle kara kurbağayı adlandırır; su kurbağası бақа'dır
  uz qurbaqa ; kurbağa
  ky курбака [kurbaka] ; kara kurbağa ; ff:Kırgızcada kurbağa için бака, kara kurbağa için kurbaka kullanılır
  tk gurbaga ; kurbağa
@tosbağa shared_ancestor
  az tısbağa ; kaplumbağa
  kk тасбақа [tasbaqa] ; kaplumbağa
  uz toshbaqa ; kaplumbağa
  ky ташбака [taşbaka] ; kaplumbağa
  tk pyşbaga ; kaplumbağa
@kertenkele shared_ancestor
  az kərtənkələ ; kertenkele
  kk кесіртке [kesirtke] ; kertenkele
  uz kaltakesak ; kertenkele ; ff:Özbekçe "kısa kesik" anlamlı başka bir bileşik kullanır
  ky кескелдирик [keskeldirik] ; kertenkele
@koç shared_ancestor
  az qoç ; koç
  kk қошқар [qoşqar] ; koç
  uz qoʻchqor ; koç
  ky кочкор [koçkor] ; koç
  tk goç ; koç
@buzağı shared_ancestor
  az buzov ; buzağı
  kk бұзау [buzau] ; buzağı
  uz buzoq ; buzağı
  ky музоо [muzoo] ; buzağı
  tk göle ; buzağı ; ff:Türkmence Farsça kökenli başka bir söz kullanır
@dana shared_ancestor
  az dana ; dana
  kk тана [tana] ; iki yaşında düve ; ff:Kazakçada tana yalnızca genç dişi sığırı adlandırır
@toklu shared_ancestor
  az toğlu ; toklu
  kk тоқты [toqtı] ; toklu
  uz toʻqli ; toklu
  ky токту [toktu] ; toklu
  tk tokly ; toklu
@kulun shared_ancestor
  az qulun ; tay
  kk құлын [qulın] ; tay
  uz qulun ; tay
  ky кулун [kulun] ; tay
  tk gulun ; tay
@yele shared_ancestor
  az yal ; yele
  kk жал [jal] ; yele
  uz yol ; yele
  ky жал [jal] ; yele
  tk ýal ; yele
@eyer shared_ancestor
  az yəhər ; eyer
  kk ер [er] ; eyer ; ff:Kazakçada er hem "eyer" hem "erkek, yiğit" anlamına gelir
  uz egar ; eyer
  ky ээр [eer] ; eyer
  tk eýer ; eyer
@üzengi shared_ancestor
  az üzəngi ; üzengi
  kk үзеңгі [üzeŋgi] ; üzengi
  uz uzangi ; üzengi
  ky үзөңгү [üzöŋgü] ; üzengi
  tk üzeňňi ; üzengi
@kamçı from_turkish
  az qamçı ; kamçı
  kk қамшы [qamşı] ; kamçı
  uz qamchi ; kamçı
  ky камчы [kamçı] ; kamçı
  tk gamçy ; kamçı
  ru камча [kamça] ; kamçı ; ff:Rusçada edebî söz кнут'tur; kamça Kazak-Tatar yoluyla girmiştir
  bg камшик [kamşik] ; kamçı
  mk камшик [kamşik] ; kamçı
  sr камџија [kamdžija] ; kamçı
  sq kamxhik ; kamçı
@kırbaç from_turkish
  hu korbács ; kırbaç
  ro gârbaci ; kırbaç
  sq kërbaç ; kırbaç
  sr корбач [korbač] ; kırbaç
  pl karbacz ; kırbaç
@semer shared_ancestor
  el σαμάρι [samári] ; semer
  bg самар [samar] ; semer
  sr самар [samar] ; semer
  mk самар [samar] ; semer
  sq samar ; semer
  ro samar ; semer
@çul from_turkish
  ar جل [jull] ; hayvan örtüsü ; ff:Arapça asıl kaynaktır; Balkan biçimleri Türkçeden alınmıştır
  bg чул [çul] ; at örtüsü
  sq çul ; keçe örtü
  az çul ; çul
@palan into_turkish
  fa پالان [pālān] ; semer
  az palan ; semer
  ur پالان [pālān] ; semer
@hamut into_turkish
  ru хомут [homut] ; hamut
  uk хомут [homut] ; hamut
  pl chomąto ; hamut
  bg хомот [homot] ; hamut
@mahmuz from_turkish
  ar مهماز [mihmāz] ; mahmuz ; ff:Arapça asıl kaynaktır; Balkan biçimleri Türkçeden alınmıştır
  az mahmız ; mahmuz
  bg махмуз [mahmuz] ; mahmuz
  sr мамуза [mamuza] ; mahmuz
  mk мамуза [mamuza] ; mahmuz
  sq mahmuz ; mahmuz
@rahvan into_turkish
  fa رهوار [rahvār] ; rahvan at
  ur رہوار [rahvār] ; rahvan
  az yorğa ; rahvan ; ff:Azerbaycan Türkçesi Türkçe yorga sözünü kullanır
@beygir into_turkish
  fa بارگیر [bārgīr] ; yük hayvanı ; ff:Farsçada "yük tutan" bileşiği genel yük hayvanıdır; Türkçede ata özelleşmiştir
@tımar shared_ancestor
  fa تیمار [tīmār] ; bakım, hasta bakımı ; ff:Farsçada tīmār "hasta bakımı, keder" anlamındadır; at tımarı ve Osmanlı toprak tımarı Türkçe gelişmedir
  az timar ; tımar
  sr тимар [timar] ; Osmanlı toprak dirliği ; ff:Sırpçada yalnızca tarihî tımar sistemi anlamındadır
  bg тимар [timar] ; Osmanlı toprak dirliği
  el τιμάρι [timári] ; Osmanlı toprak dirliği
@tazı shared_ancestor
  fa تازی [tāzī] ; Arap; Arap tazısı ; ff:Farsçada tāzī önce "Arap" demektir; köpek anlamı "Arap köpeği" tamlamasından kısalmıştır
  az tazı ; tazı
  kk тазы [tazı] ; tazı
  uz tozi ; tazı
  tk tazy ; tazı
  ky тайган [taygan] ; tazı ; ff:Kırgızca Eski Türkçe taygan sözünü sürdürür
@tuzak shared_ancestor
  az tuzaq ; tuzak
  kk тұзақ [tuzaq] ; tuzak
  uz tuzoq ; tuzak
  ky тузак [tuzak] ; tuzak
  tk duzak ; tuzak
@kapan from_turkish
  az qapan ; kapan
  bg капан [kapan] ; kapan, tuzak
  mk капан [kapan] ; kapan
  sq kapan ; kapan
@kement into_turkish
  fa کمند [kamand] ; kement
  az kəmənd ; kement
  uz kamand ; kement
  ur کمند [kamand] ; kement
@ökse into_turkish
  el ιξός [iksós] ; ökse otu
@otlamak shared_ancestor
  az otlamaq ; otlamak
  kk оттау [ottau] ; otlamak
  uz oʻtlamoq ; otlamak
  ky оттоо [ottoo] ; otlamak
  tk otlamak ; otlamak
@gütmek shared_ancestor
  az güdmək ; gütmek; gözetlemek
  kk күту [kütü] ; beklemek; bakmak ; ff:Kazakçada kütü "beklemek, bakımını üstlenmek" anlamına kaymıştır
  uz kutmoq ; beklemek ; ff:Özbekçede "beklemek" anlamındadır
  ky күтүү [kütüü] ; beklemek; bakmak ; ff:Kırgızcada "beklemek" anlamı öne çıkar
  tk gütmek ; gütmek
@sağmak shared_ancestor
  az sağmaq ; sağmak
  kk сауу [sauw] ; sağmak
  uz sogʻmoq ; sağmak
  ky саап [saap] ; sağmak
  tk sagmak ; sağmak
@kırkmak shared_ancestor
  az qırxmaq ; kırkmak
  kk қырқу [qırqu] ; kırkmak
  uz qirqmoq ; kesmek, kırkmak
  ky кыркуу [kırkuu] ; kırkmak
  tk gyrkmak ; kırkmak
@ötmek shared_ancestor
  az ötmək ; ötmek
  kk өту [ötü] ; geçmek ; ff:Kazakça ötü "geçmek" anlamındadır; ötmek için сайрау kullanılır
  uz oʻtmoq ; geçmek ; ff:Özbekçede "geçmek" anlamındadır
  ky өтүү [ötüü] ; geçmek ; ff:Kırgızcada "geçmek" anlamındadır
  tk ötmek ; ötmek; geçmek
@ulumak shared_ancestor
  az ulamaq ; ulumak
  kk ұлу [ulu] ; ulumak
  uz uvlamoq ; ulumak
  ky улуу [uluu] ; ulumak
  tk uwlamak ; ulumak
@kişnemek shared_ancestor
  az kişnəmək ; kişnemek
  kk кісіну [kisinu] ; kişnemek
  uz kishnamoq ; kişnemek
  ky кишенөө [kişenöö] ; kişnemek
  tk kişňemek ; kişnemek
@kükremek shared_ancestor
  az kükrəmək ; kükremek
  kk күркіреу [kürkireu] ; gürlemek ; ff:Kazakçada gök gürlemesi için kullanılır
  ky күркүрөө [kürküröö] ; gürlemek ; ff:Kırgızcada gök gürlemesi anlamı öne çıkar
  uz kukramoq ; kükremek
@melemek shared_ancestor
  az mələmək ; melemek
  tk mälemek ; melemek
  kk маңырау [maŋırau] ; melemek ; ff:Kazakça başka bir yansıma kök kullanır
@anırmak shared_ancestor
  az anqırmaq ; anırmak
  uz hangramoq ; anırmak
  tk aňňyrmak ; anırmak
@böğürmek shared_ancestor
  az böyürmək ; böğürmek
  kk мөңіреу [möŋireu] ; böğürmek ; ff:Kazakça başka bir yansıma kök kullanır
@boynuz shared_ancestor
  az buynuz ; boynuz
  kk мүйіз [müyiz] ; boynuz ; ff:Kazakça Eski Türkçe müŋüz biçimini sürdürür; Türkçe boynuz boyun sözüyle yeniden kurulmuştur
  uz muguz ; boynuz
  ky мүйүз [müyüz] ; boynuz
  tk şah ; boynuz ; ff:Türkmence Farsça şāḫ sözünü kullanır
@kuyruk shared_ancestor
  az quyruq ; kuyruk
  kk құйрық [quyrıq] ; kuyruk
  uz quyruq ; kuyruk
  ky куйрук [kuyruk] ; kuyruk
  tk guýruk ; kuyruk
@tüy shared_ancestor
  az tük ; tüy
  kk түк [tük] ; tüy
  uz tuk ; tüy
  ky түк [tük] ; tüy
  tk tüý ; tüy
@kanat shared_ancestor
  az qanad ; kanat
  kk қанат [qanat] ; kanat
  uz qanot ; kanat
  ky канат [kanat] ; kanat
  tk ganat ; kanat
@toynak shared_ancestor
  kk тұяқ [tuyaq] ; toynak
  uz tuyoq ; toynak
  ky туяк [tuyak] ; toynak
  tk toýnak ; toynak
  az dırnaq ; tırnak; toynak ; ff:Azerbaycan Türkçesinde toynak için de dırnaq kullanılır
@meme shared_ancestor
  az məmə ; meme
  kk емшек [emşek] ; meme ; ff:Kazakça em- "emmek" kökünden başka bir söz kullanır
  tk emjek ; meme ; ff:Türkmence em- kökünden başka bir söz kullanır
@yüzgeç shared_ancestor
  az üzgəc ; yüzgeç
  tk ýüzgüç ; yüzgeç
  kk қанат [qanat] ; yüzgeç ; ff:Kazakçada balığın yüzgeci için "kanat" sözü kullanılır
@kıl shared_ancestor
  az qıl ; kıl
  kk қыл [qıl] ; kıl
  uz qil ; kıl
  ky кыл [kıl] ; kıl
  tk gyl ; kıl
@döl shared_ancestor
  az döl ; döl
  kk төл [töl] ; yavru, döl
  ky төл [töl] ; yavru
  tk döl ; döl
@civciv shared_ancestor
  az cücə ; civciv
  tk jüýje ; civciv
  kk балапан [balapan] ; civciv ; ff:Kazakça bala "çocuk" kökünden türeyen başka bir söz kullanır
@pençe into_turkish
  fa پنجه [panje] ; el; pençe ; ff:Farsçada panj "beş"ten türeyen panje önce "el" demektir
  az pəncə ; pençe
  uz panja ; pençe
  ur پنجہ [panjā] ; pençe
  tk penje ; pençe
@moher shared_ancestor
  en mohair ; moher
  fr mohair ; moher
  it mohair ; moher
  de Mohair ; moher
  ar مخير [muḫayyar] ; seçilmiş ; ff:Arapçada asıl anlam "seçilmiş, seçkin (kumaş)"tır
@ardıç shared_ancestor
  az ardıc ; ardıç
  kk арша [arşa] ; ardıç ; ff:Kazakça başka bir Türkçe biçim (arça) kullanır
  uz archa ; ardıç; çam ağacı ; ff:Özbekçede archa yılbaşı çamı için de kullanılır
  ky арча [arça] ; ardıç
  tk arça ; ardıç
@söğüt shared_ancestor
  az söyüd ; söğüt
  tk sögüt ; söğüt
  kk тал [tal] ; söğüt ; ff:Kazakça Türkçe tal "dal" sözünü söğüt için kullanır
  uz tol ; söğüt ; ff:Özbekçede tol "söğüt" demektir
@kamış from_turkish
  az qamış ; kamış
  kk қамыс [qamıs] ; kamış
  uz qamish ; kamış
  ky камыш [kamış] ; kamış
  tk gamyş ; kamış
  ru камыш [kamış] ; kamış ; ff:Rusçaya Türk dillerinden geçmiştir
  uk комиш [komış] ; kamış
  bg камъш [kamăş] ; kamış
@diken shared_ancestor
  az tikan ; diken
  kk тікен [tiken] ; diken
  uz tikan ; diken
  ky тикен [tiken] ; diken
  tk tiken ; diken
@budak shared_ancestor
  az budaq ; dal
  kk бұтақ [butaq] ; dal
  uz butoq ; dal
  ky бутак [butak] ; dal
@kütük shared_ancestor
  az kötük ; kütük
  tk kötük ; kütük
  kk түбір [tübir] ; kütük; kök ; ff:Kazakça "dip" anlamlı başka bir söz kullanır
@çekirdek shared_ancestor
  az çəyirdək ; çekirdek
  tk çigit ; çekirdek ; ff:Türkmence çigit genel çekirdek anlamındadır; Türkçede çiğit pamuk tohumuna özelleşmiştir
  kk дән [dän] ; tane, çekirdek ; ff:Kazakça Farsça dāne kökünü kullanır
@çiğit shared_ancestor
  az çiyid ; pamuk tohumu
  kk шиіт [şiyit] ; pamuk tohumu
  uz chigit ; pamuk tohumu
  tk çigit ; çekirdek, tohum
@başak shared_ancestor
  kk масақ [masaq] ; başak
  uz boshoq ; başak
  ky машак [maşak] ; başak
  az sünbül ; başak ; ff:Azerbaycan Türkçesi Farsça sünbül sözünü kullanır
@kepek shared_ancestor
  az kəpək ; kepek
  kk кебек [kebek] ; kepek
  uz kepak ; kepek
  ky кебек [kebek] ; kepek
  tk kepek ; kepek
@iğde shared_ancestor
  az iydə ; iğde
  kk жиде [jide] ; iğde
  uz jiyda ; iğde
  ky жийде [jiyde] ; iğde
  tk igde ; iğde
@sakız from_turkish
  az saqqız ; sakız
  kk сағыз [sağız] ; sakız
  uz saqich ; sakız
  ky сагыз [sagız] ; sakız
  tk sakgyç ; sakız
  bg сакъз [sakăz] ; sakız
  sq sakëz ; sakız
@bakla from_turkish
  ar باقلاء [bāqillāʾ] ; bakla ; ff:Arapça asıl kaynaktır; Balkan biçimleri Türkçeden alınmıştır
  fa باقلا [bāqelā] ; bakla
  az paxla ; bakla
  bg бакла [bakla] ; bakla
  mk бакла [bakla] ; bakla
@kereviz shared_ancestor
  fa کرفس [karafs] ; kereviz
  ar كرفس [karafs] ; kereviz
  az kərəviz ; kereviz
  bg керевиз [kereviz] ; kereviz
@karnabahar into_turkish
  ar قرنبيط [qarnabīṭ] ; karnabahar
  az gül kələm ; karnabahar ; ff:Azerbaycan Türkçesi "gül lahana" bileşiğini kullanır
@tere into_turkish
  fa تره [tare] ; yeşillik, pırasa ; ff:Farsçada tare genel "yeşillik, taze sebze" demektir; Türkçede tek bir bitkiye daralmıştır
  az vəzəri ; tere ; ff:Azerbaycan Türkçesi başka bir söz kullanır
@muşmula shared_ancestor
  el μούσμουλο [moúsmoulo] ; muşmula
  bg мушмула [muşmula] ; muşmula
  sr мушмула [mušmula] ; muşmula
  mk мушмула [muşmula] ; muşmula
  sq mushmollë ; muşmula
  ro moșmon ; muşmula
@alıç into_turkish
  fa آلوچه [ālūçe] ; küçük erik ; ff:Farsçada ālūçe "küçük erik, can eriği"dir; Türkçede başka bir meyveye kaymıştır
  az alça ; yabani erik ; ff:Azerbaycan Türkçesinde alça "yeşil erik" demektir
@harnup shared_ancestor
  ar خروب [ḫarrūb] ; keçiboynuzu
  fa خرنوب [ḫarnūb] ; keçiboynuzu
  el χαρούπι [kharoúpi] ; keçiboynuzu
  it carruba ; keçiboynuzu
  es algarroba ; keçiboynuzu ; ff:İspanyolca biçim Arapça tanımlık (al-) ile kaynaşmıştır
  pt alfarroba ; keçiboynuzu
@hünnap into_turkish
  ar عناب [ʿunnāb] ; hünnap
  fa عناب [ʿonnāb] ; hünnap
  az innab ; hünnap
  ur عناب [unnāb] ; hünnap
@narenciye shared_ancestor
  fa نارنج [nāranj] ; turunç
  ar نارنج [nāranj] ; turunç
  es naranja ; portakal ; ff:İspanyolcada naranja tatlı portakalı adlandırır
  pt laranja ; portakal
  it arancia ; portakal
  fr orange ; portakal
  en orange ; portakal
  hu narancs ; portakal
  el νεράντζι [nerántzi] ; turunç
@avokado shared_ancestor
  es aguacate ; avokado
  en avocado ; avokado
  fr avocat ; avokado; avukat ; ff:Fransızcada avocat hem "avukat" hem "avokado" anlamına gelir
  it avocado ; avokado
  pt abacate ; avokado
  de Avocado ; avokado
  ru авокадо [avokado] ; avokado
@mango shared_ancestor
  en mango ; mango
  es mango ; mango; sap ; ff:İspanyolcada mango ayrıca "sap, tutamak" demektir
  fr mangue ; mango
  it mango ; mango
  pt manga ; mango ; ff:Portekizcede manga ayrıca "elbise kolu" demektir
  de Mango ; mango
@papaya shared_ancestor
  es papaya ; papaya
  en papaya ; papaya
  fr papaye ; papaya
  it papaia ; papaya
  pt papaia ; papaya
  de Papaya ; papaya
@kivi shared_ancestor
  en kiwi ; kivi
  fr kiwi ; kivi
  it kiwi ; kivi
  es kiwi ; kivi
  de Kiwi ; kivi
  ru киви [kivi] ; kivi
@soya shared_ancestor
  en soy ; soya
  fr soja ; soya
  de Soja ; soya
  it soia ; soya
  es soja ; soya
  ru соя [soya] ; soya
@kinoa shared_ancestor
  es quinua ; kinoa
  en quinoa ; kinoa
  fr quinoa ; kinoa
  it quinoa ; kinoa
  de Quinoa ; kinoa
  pt quinoa ; kinoa
@kaju shared_ancestor
  pt caju ; kaju
  en cashew ; kaju
  fr cajou ; kaju
  de Cashew ; kaju
  es anacardo ; kaju ; ff:İspanyolca Yunanca kökenli başka bir söz kullanır
@defne shared_ancestor
  el δάφνη [dáfni] ; defne
  bg дафина [dafina] ; defne
  sq dafinë ; defne
  ro dafin ; defne
  sr ловор [lovor] ; defne ; ff:Sırpça Latince laurus kökünü kullanır
@ıhlamur into_turkish
  el φλαμούρι [flamoúri] ; ıhlamur
  bg липа [lipa] ; ıhlamur ; ff:Bulgarca Slav kökenli başka bir söz kullanır
@papatya into_turkish
  el παπαδιά [papadiá] ; papaz karısı ; ff:Yunancada papadiá "papazın karısı"dır; çiçek adı halk benzetmesidir
@anason shared_ancestor
  el γλυκάνισο [glykániso] ; anason
  ar أنيسون [anīsūn] ; anason
  fa انیسون [anīsūn] ; anason
  it anice ; anason
  fr anis ; anason
  es anís ; anason
  en anise ; anason
  de Anis ; anason
  hu ánizs ; anason
  ro anason ; anason ; ff:Romenceye Türkçe yoluyla geçmiştir
  bg анасон [anason] ; anason
  sq anason ; anason
@rezene into_turkish
  fa رازیانه [rāziyāne] ; rezene
  ar رازيانج [rāziyānaj] ; rezene
  az razyana ; rezene
@zerdeçal into_turkish
  fa زردچوبه [zardçūbe] ; sarı değnek; zerdeçal ; ff:Farsça bileşik "sarı değnek" demektir; Türkçe biçim çūb yerine çāl ile kaynaşmıştır
  az zərdəçal ; zerdeçal
  uz zarchava ; zerdeçal
@kişniş into_turkish
  fa گشنیز [geşnīz] ; kişniş
  az keşniş ; kişniş
  uz kashnich ; kişniş
@sumak shared_ancestor
  ar سماق [summāq] ; sumak
  fa سماق [somāq] ; sumak
  az sumax ; sumak
  en sumac ; sumak
  fr sumac ; sumak
  it sommacco ; sumak
  es zumaque ; sumak
  el σουμάκι [soumáki] ; sumak
@mahlep shared_ancestor
  ar محلب [maḥlab] ; mahlep
  en mahleb ; mahlep
  el μαχλέπι [makhlépi] ; mahlep
@muskat shared_ancestor
  fr muscade ; muskat
  de Muskat ; muskat
  it noce moscata ; muskat
  es nuez moscada ; muskat
  en nutmeg ; muskat ; ff:İngilizce başka bir bileşik kullanır
@lavanta shared_ancestor
  it lavanda ; lavanta
  fr lavande ; lavanta
  en lavender ; lavanta
  es lavanda ; lavanta
  de Lavendel ; lavanta
  el λεβάντα [levánta] ; lavanta
  ru лаванда [lavanda] ; lavanta
@hatmi into_turkish
  ar خطمي [ḫaṭmī] ; hatmi
  fa ختمی [ḫatmī] ; hatmi
  az xətmi ; hatmi
@şakayık into_turkish
  ar شقائق [şaqāʾiq] ; gelincikler ; ff:Arapçada şaqāʾiq al-nuʿmān "gelincik" demektir; Türkçede şakayık başka bir çiçektir
  fa شقایق [şaqāyeq] ; gelincik ; ff:Farsçada da gelincik anlamındadır
@erguvan into_turkish
  fa ارغوان [arġavān] ; erguvan
  ar أرجوان [urjuwān] ; mor renk ; ff:Arapçada urjuwān "mor, erguvan rengi" demektir
  az ərğəvan ; erguvan
  ur ارغوانی [arġavānī] ; mor
@süsen shared_ancestor
  fa سوسن [sūsan] ; süsen, zambak
  ar سوسن [sawsan] ; zambak
  he שושן [şoşan] ; zambak, gül ; ff:İbranice şoşan Sami kökün kaynağıdır; Şoşana adı da buradan gelir
  az süsən ; süsen
@zerrin into_turkish
  fa زرین [zarrīn] ; altın renkli ; ff:Farsçada sıfattır; Türkçede çiçek adı olmuştur
  az zərrin ; altın renkli
@nilüfer into_turkish
  fa نیلوفر [nīlūfar] ; nilüfer
  ar نيلوفر [naylūfar] ; nilüfer
  az nilufər ; nilüfer
  uz nilufar ; nilüfer
  ur نیلوفر [nīlōfar] ; nilüfer
@şebboy into_turkish
  fa شب‌بو [şab-bū] ; gece kokusu; şebboy
  az şəbbu ; şebboy
@hercai into_turkish
  fa هرجایی [harjāyī] ; her yerde bulunan; serseri ; ff:Farsçada "serseri, kararsız" anlamı öne çıkar; Türkçede menekşe adında donmuştur
@mine into_turkish
  fa مینا [mīnā] ; sır, cam, emaye ; ff:Farsçada mīnā önce "cam, emaye"dir; çiçek adı renk benzetmesidir
  az mina ; mine
  ur مینا [mīnā] ; emaye
@ıtır shared_ancestor
  ar عطر [ʿiṭr] ; güzel koku
  fa عطر [ʿatr] ; koku, parfüm
  az ətir ; parfüm ; ff:Azerbaycan Türkçesinde ətir "parfüm" demektir; çiçek anlamı yoktur
  uz atir ; parfüm ; ff:Özbekçede atir "parfüm" demektir
  ur عطر [itr] ; esans
@gonca into_turkish
  fa غنچه [ġonçe] ; gonca
  az qönçə ; gonca
  uz gʻuncha ; gonca
  ur غنچہ [ġunçā] ; gonca
  tk gunça ; gonca
@leylak shared_ancestor
  fa لیلک [līlak] ; leylak
  ar ليلك [laylak] ; leylak
  en lilac ; leylak
  fr lilas ; leylak
  es lila ; leylak; mor ; ff:İspanyolcada lila "leylak rengi, mor" anlamına kaymıştır
  it lillà ; leylak
  bg люляк [lyulyak] ; leylak ; ff:Bulgarcaya Türkçe yoluyla geçmiştir
  ro liliac ; leylak; yarasa ; ff:Romencede liliac hem leylak hem yarasa demektir
@orkide shared_ancestor
  fr orchidée ; orkide
  en orchid ; orkide
  it orchidea ; orkide
  es orquídea ; orkide
  de Orchidee ; orkide
  el ορχιδέα [orkhidéa] ; orkide ; ff:Eski Yunanca órkhis "testis" sözünden türer
  ru орхидея [orhideya] ; orkide
@krizantem shared_ancestor
  fr chrysanthème ; krizantem
  en chrysanthemum ; krizantem
  it crisantemo ; krizantem
  es crisantemo ; krizantem
  de Chrysantheme ; krizantem
  el χρυσάνθεμο [khrysánthemo] ; altın çiçek; krizantem
@manolya shared_ancestor
  fr magnolia ; manolya
  en magnolia ; manolya
  it magnolia ; manolya
  es magnolia ; manolya
  de Magnolie ; manolya
  ru магнолия [magnoliya] ; manolya
@ortanca shared_ancestor
  fr hortensia ; ortanca
  it ortensia ; ortanca
  es hortensia ; ortanca
  de Hortensie ; ortanca
  el ορτανσία [ortansía] ; ortanca
  en hydrangea ; ortanca ; ff:İngilizce Yunanca "su kabı" anlamlı bilimsel adı kullanır
@kaktüs shared_ancestor
  fr cactus ; kaktüs
  en cactus ; kaktüs
  it cactus ; kaktüs
  es cacto ; kaktüs
  de Kaktus ; kaktüs
  el κάκτος [káktos] ; kaktüs
  ru кактус [kaktus] ; kaktüs
@palmiye shared_ancestor
  fr palmier ; palmiye
  it palma ; palmiye
  es palma ; palmiye
  pt palmeira ; palmiye
  en palm ; palmiye; avuç içi ; ff:İngilizcede palm "avuç içi" anlamı da taşır; Latince palma'nın iki anlamı sürer
  de Palme ; palmiye
  ru пальма [palma] ; palmiye
@bambu shared_ancestor
  fr bambou ; bambu
  en bamboo ; bambu
  it bambù ; bambu
  es bambú ; bambu
  pt bambu ; bambu
  de Bambus ; bambu
  ru бамбук [bambuk] ; bambu
@liken shared_ancestor
  fr lichen ; liken
  en lichen ; liken
  it lichene ; liken
  es liquen ; liken
  el λειχήνα [leikhína] ; liken
@polen shared_ancestor
  fr pollen ; polen
  en pollen ; polen
  it polline ; polen
  es polen ; polen
  de Pollen ; polen
@reçine shared_ancestor
  fr résine ; reçine
  en resin ; reçine
  it resina ; reçine
  es resina ; reçine
  el ρητίνη [ritíni] ; reçine
@okaliptüs shared_ancestor
  fr eucalyptus ; okaliptüs
  en eucalyptus ; okaliptüs
  it eucalipto ; okaliptüs
  es eucalipto ; okaliptüs
  de Eukalyptus ; okaliptüs
  el ευκάλυπτος [efkályptos] ; iyi örtülü; okaliptüs
  ru эвкалипт [evkalipt] ; okaliptüs
@akasya shared_ancestor
  fr acacia ; akasya
  en acacia ; akasya
  it acacia ; akasya
  es acacia ; akasya
  de Akazie ; akasya
  el ακακία [akakía] ; akasya
  ru акация [akatsiya] ; akasya
@hindiba shared_ancestor
  ar هندباء [hindibāʾ] ; hindiba
  fa هندبا [hendebā] ; hindiba
  it indivia ; hindiba ; ff:İtalyanca Latince intubus yoluyla gelen akraba biçimdir
  fr endive ; hindiba
  en endive ; hindiba
  es endibia ; hindiba
@radika shared_ancestor
  el ραδίκι [radíki] ; radika
  it radicchio ; radika
  ru редька [redka] ; turp ; ff:Rusçada aynı Latince kökten gelen söz turpu adlandırır
@labada into_turkish
  el λάπαθο [lápatho] ; labada
  bg лобода [loboda] ; kazayağı otu ; ff:Bulgarca loboda başka bir bitkiyi adlandırır; ses benzerliği aldatıcıdır
  ro lobodă ; kazayağı otu ; ff:Romence lobodă başka bir bitkidir
@nişasta from_turkish
  fa نشاسته [neşāste] ; nişasta ; ff:Farsça asıl kaynaktır; Balkan biçimleri Türkçeden alınmıştır
  az nişasta ; nişasta
  ur نشاستہ [nişāstā] ; nişasta
  bg нишесте [nişeste] ; nişasta
  mk нишесте [nişeste] ; nişasta
  sq nishaste ; nişasta
@zahire into_turkish
  ar ذخيرة [ḏaḫīra] ; stok; cephane ; ff:Arapçada ḏaḫīra "stok, cephane" demektir; tahıl anlamı Türkçeye özgüdür
  fa ذخیره [zaḫīre] ; rezerv, stok ; ff:Farsçada "rezerv" anlamındadır
  az zəxirə ; rezerv ; ff:Azerbaycan Türkçesinde "rezerv, stok" anlamındadır
  ur ذخیرہ [zaḫīrā] ; stok, depo
@nebat into_turkish
  ar نبات [nabāt] ; bitki
  fa نبات [nabāt] ; nöbet şekeri ; ff:Farsçada nabāt "kristal şeker" demektir; bitki anlamı Arapçadadır
  ur نبات [nabāt] ; bitki
  az nəbatat ; bitkiler
@vahşi into_turkish
  ar وحشي [waḥşī] ; yabani
  fa وحشی [vahşī] ; yabani
  az vəhşi ; yabani
  uz vahshiy ; yabani
  ur وحشی [vahşī] ; yabani
@ehli into_turkish
  ar أهلي [ahlī] ; aileye ait; yerli; evcil ; ff:Arapçada ahlī öncelikle "yerli, ulusal" demektir; spor kulübü adlarında görülür
  fa اهلی [ahlī] ; evcil
  az əhli ; evcil
  ur اہلی [ahlī] ; evcil
@haşere into_turkish
  ar حشرة [ḥaşara] ; böcek
  fa حشره [haşare] ; böcek
  az həşərat ; böcekler
  uz hasharot ; böcekler
  ur حشرات [haşarāt] ; böcekler
@lif into_turkish
  ar ليف [līf] ; lif
  fa لیف [līf] ; lif; hamam lifi
  az lif ; lif
  uz lif ; lif
@koza into_turkish
  fa غوزه [ġūze] ; pamuk kozası
  az qoza ; koza
  uz gʻoʻza ; pamuk bitkisi ; ff:Özbekçede gʻoʻza pamuk bitkisinin kendisidir
@mamut shared_ancestor
  ru мамонт [mamont] ; mamut
  fr mammouth ; mamut
  en mammoth ; mamut
  de Mammut ; mamut
  it mammut ; mamut
@sincap into_turkish
  fa سنجاب [sencāb] ; sincap
  ar سنجاب [sinjāb] ; sincap
  ur سنجاب [sanjāb] ; sincap
  az sincab ; sincap (edebî) ; ff:Azerbaycan Türkçesinde günlük söz dələ'dir
"""
