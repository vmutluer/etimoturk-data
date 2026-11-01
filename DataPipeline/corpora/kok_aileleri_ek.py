# -*- coding: utf-8 -*-
"""Korpus 4 — Ek kök aileleri ve üyeleri (Öz Türkçe, Arapça sülasi, Farsça bileşik, Latince/Yunanca)."""

FAMILIES = r"""
*yaş-göz|tr|yaş, gözyaşı; nem|Eski Türkçe yaş "nem, gözyaşı" adından; yaşarmak, yaşlanmak (gözleri), yaş (ıslak) aynı kökten gelir.
*kıl-|tr|yapmak, etmek|Orhun Yazıtları'ndaki kıl- fiili; kılık (yapılış, görünüş), kılgı (uygulama), kılınç aynı kökten gelir.
*ak-|tr|akmak|Eski Türkçe ak- fiili; akın (hücum), akıntı, akarsu, akım (cereyan), akar aynı kökten türetilmiştir.
*kaç-|tr|kaçmak|Eski Türkçe kaç- fiili; kaçak, kaçış, kaçamak, kaçınmak, kaçınılmaz aynı kökten gelir.
*sök-|tr|sökmek|Eski Türkçe sök- fiili; söküm, sökük, sökülmek aynı kökten gelir.
*düz-|tr|düz, düzenlemek|Eski Türkçe tüz "düz, doğru" sözcüğünden; düzen, düzey, düzgün, düzelmek, düzlük aynı kökten türetilmiştir.
*top-|tr|yuvarlak, toplamak|Eski Türkçe top "yuvarlak nesne"; toplamak, toplum, toplantı, toplam, topak, topuk aynı kökten gelir.
*ağır|tr|ağır, saygın|Eski Türkçe agır "ağır; değerli"; ağırlık, ağırlamak (saygı göstermek), ağırbaşlı aynı kökten gelir.
K-S-M|ar|bölmek, pay etmek|Arapça q-s-m kökü; qısm (bölüm), qısmet (pay), taqsīm (bölüştürme), muqassem aynı kökten türer.
S-K-N|ar|yerleşmek, dinmek|Arapça s-k-n kökü; sākin (oturan, durgun), mesken (konut), sükūn (dinginlik), iskān (yerleştirme), teskīn aynı kökten gelir.
C-R-H|ar|yaralamak|Arapça c-r-ḥ kökü; cerrāḥ (yara iyileştiren), cerīḥa? (yara), mecrūḥ (yaralı), cerahat aynı kökten türer.
Ş-R-B|ar|içmek|Arapça ş-r-b kökü; şarāb (içecek), şerbet, şurup (şarāb'ın Fransızca yoluyla dönüşü), meşrubat aynı kökten gelir.
N-S-B|ar|ilişki, soy|Arapça n-s-b kökü; nisbet (oran), nesep (soy), münasebet (ilişki), münasip (uygun), nispeten aynı kökten türer.
K-R-M|ar|cömertlik, yücelik|Arapça k-r-m kökü; kerem, kerīm, ikrām (ağırlama), ikrāmiye, mükerrem aynı kökten gelir.
W-F-K|ar|uyuşmak|Arapça w-f-q kökü; muvāfaqat (onay), ittifāq (birlik), tevfīq, muvaffaq (başarılı), muvaffaqiyet aynı kökten türer.
Ẕ-R-F|ar|incelik, zariflik|Arapça ẕ-r-f kökü; ẕarīf (ince, zarif) > zarif, zarifçe ve ẕarāfa > zarafet aynı kökten gelir.
T-R-B|ar|toprak|Arapça t-r-b kökü; turāb (toprak) ve türbe (toprak; anıt mezar) aynı kökten gelir. Terbiye ise r-b-w "büyütmek" kökünden gelen ayrı bir sözcüktür.
F-R-K|ar|ayırmak|Arapça f-r-q kökü; farq (ayrım), firqa (bölük, parti), tefrīq (ayırma) ve fırka aynı kökten türer. Müfreze, f-r-z "ayırıp koymak" kökünden gelen ayrı bir sözcüktür.
H-D-M|ar|hizmet etmek|Arapça ḫ-d-m kökü; ḫidmet, ḫādim, hademe (hizmetçiler), müstahdem aynı kökten gelir.
A-R-D|ar|sunmak, genişlik|Arapça ʿ-r-ḏ kökü; ʿarḏ (sunma), arzuhal (hâl sunma), maʿrūḏ, taʿrīḏ (sataşma), ʿarīḏa (dilekçe) aynı kökten türer.
M-R-D|ar|hastalık|Arapça m-r-ḏ kökü; maraḏ (hastalık), marīḏ (hasta), emrāḏ, mütemāriz aynı kökten gelir.
N-Ş-R|ar|yaymak|Arapça n-ş-r kökü; neşr (yayma), neşriyāt (yayınlar), nāşir (yayıncı), menşūr (yayılmış), intişār aynı kökten türer.
K-Ş-F|ar|açmak, ortaya çıkarmak|Arapça k-ş-f kökü; keşf (bulma), kāşif (bulan), mükāşefe, keşşāf (izci) aynı kökten gelir.
dāştan|fa|tutmak|Farsça dāştan "tutmak" fiilinin -dāşt/-dāşte türevleri; yāddāşt (hatıra notu) ve dār- ailesi ile akrabadır.
-gāh|fa|yer|Farsça gāh "yer, zaman"; dergâh (kapı yeri), tezgâh (el yeri), ordugâh, karargâh, ikametgâh, secdegâh aynı ikinci öğeyle kurulmuştur.
-ī (nisbet)|fa|aitlik eki|Farsça -ī aitlik eki; Türkçede şarkı (şarqī: doğulu), gümrükçü değil; cengî, hâkî (toprak rengi), meyvî, kirazî gibi renk/aitlik adları kurar.
-ane|fa|biçim zarfı|Farsça -āne eki; şahane, dostane, merdane, cahilane, çocukça anlamında mahçubane gibi zarflar kurar.
nav-|fa|yeni|Farsça nav "yeni"; nevruz (yeni gün), nevzat (yeni doğan), nevbahar aynı kökten gelir; Latince novus ile Hint-Avrupa akrabasıdır.
kar-|la|yakmak, ısı|Latince calor/calere "ısı"; kalori, kalorifer, şofben? (fr chauffe-bain), şömine? ; kesin: kalori, kalorifer, kaloriferci.
scribere|la|yazmak|Latince scribere "yazmak"; skript (senaryo metni), manuskript, deskripsiyon, transkripsiyon aynı kökten gelir.
nomen|la|ad|Latince nomen "ad"; nominal, nomenklatür ve Yunanca ónoma kökenli anonim, sinonim, antonim aynı Hint-Avrupa kökündendir.
genus|la|soy, doğuş|Latince genus "soy" ve Yunanca génos; jen, jenerasyon, jeneratör, jenerik, genetik, jenosit? aynı kökten gelir.
forma|la|biçim|Latince forma "biçim"; form, formül, format, formalite, reform, uniforma, deformasyon aynı kökten türer.
korda|el|bağırsak, tel|Eski Yunanca khordḕ "bağırsak teli"; kord (ip), kordon, kordele ve kurdele aynı kökten gelir. Akor ise Latince cor "kalp" kökünden (accordare) gelir.
skopein|el|bakmak|Eski Yunanca skopeîn "bakmak"; teleskop, mikroskop, periskop, skop, episkopos (piskopos) aynı kökten gelir.
cor|la|kalp|Latince cor (cordis) "kalp"; accordare "kalpleri uyuşturmak" > Fransızca accord > akor ve akordeon aynı kökten gelir. Rekor da (recordari "kalbe geri getirmek") aynı Latince köke bağlanır.
A-Ṣ-R|ar|çağ; sıkmak|Arapça ʿ-ṣ-r kökü; ʿaṣr (çağ, yüzyıl; ikindi) > asır ve asri (çağdaş) aynı kökten gelir. Eser ve tesir, ʾ-ṯ-r "iz" kökünden gelen ayrı bir ailedir.
A-Ẕ-M|ar|büyük olmak|Arapça ʿ-ẕ-m kökü; ʿaẕamet (büyüklük) > azamet, muʿaẕẕam > muazzam ve aʿẕam (en büyük) ile kurulan sadrazam (ṣadr-ı aʿẕam) aynı kökten gelir. Azim, ʿ-z-m "kararlı olmak" kökünden gelen ayrı bir ailedir.
K-Ṯ-R|ar|çok olmak|Arapça k-ṯ-r kökü; kaṯra (çokluk) > kesret aynı kökten gelir. Kesir ve inkisar, k-s-r "kırmak" kökünden gelen ayrı bir ailedir.
Q-Ṣ-R|ar|kısa olmak, eksik kalmak|Arapça q-ṣ-r kökü; quṣūr (eksiklik) > kusur, kusurlu, kusursuz ve taqṣīr (kısaltma; ihmal) > taksir aynı kökten gelir. Kesir ve inkisar, k-s-r "kırmak" kökünden gelen ayrı bir ailedir.
A-D-N|ar|yerleşmek; maden yatağı|Arapça ʿ-d-n kökü; maʿdin "maden ocağı, kaynak" > maden, madeni, madenci, madencilik ve madenbilim aynı kökten gelir. Medeniyet, m-d-n "şehirleşmek" kökünden gelen ayrı bir ailedir.
*ört-|tr|örtmek, kapamak|Eski Türkçe ört- "kapamak, gizlemek" fiili; örtü (örtüg) ve örtünmek aynı kökten gelir. Örmek (ör-) ayrı bir köktür.
*ilet-|tr|götürmek, ulaştırmak|Eski Türkçe ilet- / elt- "götürmek" fiili; iletmek, iletken, iletim ile Dil Devrimi türetmeleri ileti ve iletişim aynı kökten gelir. Ulaşmak (ula-) ve il- ayrı köklerdir.
Ğ-N-Y|ar|şarkı söylemek; zengin olmak|Arapça ġ-n-y kökü; ġannā "şarkı söylemek" > muganni (şarkıcı) ve teganni (şarkı söyleme) bu köktendir. Nağme, n-ġ-m "ezgi" kökünden gelen ayrı bir sözcüktür.
R-ʾ-Y|ar|görmek|Arapça r-ʾ-y kökü; ruʾyā (görme; düş) > rüya, riyāʾ (gösteriş) > riya ve murāʾī (ikiyüzlü) > mürai aynı kökten gelir. Mera ve riayet, r-ʿ-y "gütmek" kökünden gelen ayrı bir ailedir.
C-D-L|ar|çekişmek, tartışmak|Arapça c-d-l kökü; mucādala (çekişme, boğuşma) > mücadele ve mücadeleci aynı kökten gelir. Cihat ve mücahit, c-h-d "çabalamak" kökünden gelen ayrı bir ailedir.
A-N-N|ar|-den (aktarım)|Arapça ʿan "-den" edatının yinelenmesiyle kurulan ʿanʿana, hadisin "falandan, o da falandan" diye aktarılan rivayet zincirini anlatır; buradan "kuşaktan kuşağa aktarılan gelenek" anlamına geçen anane (an'ane) ve ananevi (geleneksel) aynı kökten gelir.
"""

WORDS = r"""
yaşarmak|v|tr|yaşar-|gözleri sulanmak|OSM|*yaş-göz|
ıslaklık|n|tr|ıslak|nem|OSM||
kılık|n|tr|kılık|görünüş|DLT|*kıl-|
kılgı|n|tr|kılgı|uygulama|DD|*kıl-|
kılınç|n|tr|kılınç|davranış|DLT|*kıl-|
akın|n|tr|akın|hücum|DLT|*ak-|
akıntı|n|tr|akıntı|akan su|OSM|*ak-|
akar|n|ar|ʿaqār|gelir getiren mülk|OSM||
akıcı|adj|tr|akıcı|akışkan|TDK|*ak-|
akış|n|tr|akış|akma|OSM|*ak-|
kaçamak|n|tr|kaçamak|kaçış yolu|OSM|*kaç-|
kaçınmak|v|tr|kaçın-|sakınmak|DLT|*kaç-|
kaçınılmaz|adj|tr|kaçınılmaz|zorunlu|DD|*kaç-|
kaçırmak|v|tr|kaçur-|kaçmasına yol açmak|DLT|*kaç-|
söküm|n|tr|söküm|sökme işi|TDK|*sök-|
sökük|adj|tr|sökük|sökülmüş|OSM|*sök-|
düzelmek|v|tr|tüzel-|düz olmak|DLT|*düz-|
düzeltmek|v|tr|tüzelt-|düzeltmek|OSM|*düz-|
düzlük|n|tr|tüzlük|ova|DLT|*düz-|
düzenbaz adam|n|tr|düzen|hileci|OSM|*düz-|
düzmece|adj|tr|düzmece|sahte|OSM|*düz-|
topak|n|tr|topak|yuvarlak parça|DLT|*top-|
topuk|n|tr|topık|ayak arkası|DLT|*top-|
toplanmak|v|tr|toplan-|bir araya gelmek|DLT|*top-|
toplayıcı|n|tr|toplayıcı|toplayan|TDK|*top-|
ağırlamak|v|tr|agırla-|saygı göstermek|ORH|*ağır|
ağırbaşlı|adj|tr|agır baş|olgun|OSM|*ağır|
ağırlaşmak|v|tr|agırlaş-|ağır olmak|DLT|*ağır|
kısım|n|ar|qism|bölüm|EAT|K-S-M|
taksim|n|ar|taqsīm|bölüştürme|EAT|K-S-M|
kısmetli|adj|ar|qisma|şanslı|OSM|K-S-M|
mukassem|adj|ar|muqassam|bölünmüş|OSM|K-S-M|
taksimat|n|ar|taqsīmāt|bölümlemeler|OSM19|K-S-M|
mesken|n|ar|maskan|konut|EAT|S-K-N|
iskân|n|ar|iskān|yerleştirme|OSM|S-K-N|
teskin|n|ar|taskīn|yatıştırma|OSM|S-K-N|
sükûn|n|ar|sukūn|dinginlik|EAT|S-K-N|
sakinleşmek|v|ar|sākin|durulmak|TDK|S-K-N|
cerahat|n|ar|cirāḥa|yara akıntısı|EAT|C-R-H|
mecruh|adj|ar|macrūḥ|yaralı|OSM|C-R-H|
cerrahi|adj|ar|cirāḥī|ameliyatla ilgili|OSM19|C-R-H|
meşrubat|n|ar|maşrūbāt|içecekler|OSM19|Ş-R-B|
şurup kıvamı|n|ar|şarāb|kıvam|OSM|Ş-R-B|
şerbetçi|n|ar|şarba|şerbet satan|OSM|Ş-R-B|
nispet|n|ar|nisba|oran|EAT|N-S-B|
nesep|n|ar|nasab|soy|EAT|N-S-B|
münasebet|n|ar|munāsaba|ilişki|EAT|N-S-B|
münasip|adj|ar|munāsib|uygun|EAT|N-S-B|
nispeten|adv|ar|nisbatan|oranla|OSM|N-S-B|
kerim|adj|ar|karīm|cömert|EAT|K-R-M|
mükerrem|adj|ar|mukarram|saygın|OSM|K-R-M|
ikram etmek|v|ar|ikrām|ağırlamak|EAT|K-R-M|
muvafakat|n|ar|muwāfaqa|onay|OSM|W-F-K|
muvaffak|adj|ar|muwaffaq|başarılı|OSM|W-F-K|
muvaffakiyet|n|ar|muwaffaqiyya|başarı|OSM19|W-F-K|
tevfik|n|ar|tawfīq|uygun kılma|EAT|W-F-K|
zarafet|n|ar|ẕarāfa|incelik|OSM|Ẕ-R-F|
zarifçe|adv|ar|ẕarīf|incelikle|OSM|Ẕ-R-F|
terbiye|n|ar|tarbiya|yetiştirme|EAT|R-B-W|
terbiyeli|adj|ar|tarbiya|görgülü|OSM|R-B-W|
türbedar|n|ar|turba-dār|türbe bekçisi|OSM|dār-|
toprak türab|n|ar|turāb|toprak|EAT|T-R-B|
fark|n|ar|farq|ayrım|EAT|F-R-K|
farklı|adj|ar|farq|başka|OSM|F-R-K|
tefrik|n|ar|tafrīq|ayırma|OSM|F-R-K|
müfreze|n|ar|mufraza|ayrılmış birlik|OSM19||
hadim|n|ar|ḫādim|hizmet eden|EAT|H-D-M|
müstahdem|n|ar|mustaḫdam|çalıştırılan|OSM19|H-D-M|
arz|n|ar|ʿarḏ|sunma; genişlik|EAT|A-R-D|
arıza|n|ar|ʿāriḏa|engel; bozukluk|OSM|A-R-D|
maruz|adj|ar|maʿrūḏ|sunulmuş; açık|OSM|A-R-D|
tariz|n|ar|taʿrīḏ|sataşma|OSM|A-R-D|
mariz|adj|ar|marīḏ|hasta|OSM|M-R-D|
emraz|n|ar|amrāḏ|hastalıklar|OSM|M-R-D|
neşir|n|ar|naşr|yayma|OSM|N-Ş-R|
neşriyat|n|ar|naşriyyāt|yayınlar|OSM19|N-Ş-R|
naşir|n|ar|nāşir|yayıncı|OSM19|N-Ş-R|
menşur|n|ar|manşūr|prizma; yayılmış|OSM|N-Ş-R|
intişar|n|ar|intişār|yayılma|OSM|N-Ş-R|
keşif|n|ar|kaşf|bulma|EAT|K-Ş-F|
kâşif|n|ar|kāşif|bulan|OSM|K-Ş-F|
keşşaf|n|ar|kaşşāf|izci|OSM19|K-Ş-F|
mükâşefe|n|ar|mukāşafa|açılma|EAT|K-Ş-F|
yaddaşt|n|fa|yād-dāşt|not|OSM|dāştan|
dergâh|n|fa|dar-gāh|kapı yeri|EAT|-gāh|
karargâh|n|ar|qarār-gāh|karar yeri|OSM|-gāh|ar:qarār>fa:qarār-gāh>tr:karargâh
ikametgâh|n|ar|iqāmat-gāh|oturma yeri|OSM19|-gāh|ar:iqāma>fa:iqāmet-gāh>tr:ikametgâh
secdegâh|n|ar|sacda-gāh|secde yeri|OSM|-gāh|
güzergâh|n|fa|guzar-gāh|geçiş yeri|OSM|-gāh|
tezgâh başı|n|fa|dast-gāh|tezgâh|OSM|-gāh|
hâki|adj|fa|ḫākī|toprak rengi|OSM19|-ī (nisbet)|
cengî|n|fa|cangī|savaşçı; dansçı|OSM|-ī (nisbet)|
şarkî|adj|ar|şarqī|doğuya ait|OSM|-ī (nisbet)|
garbî|adj|ar|ġarbī|batıya ait|OSM|-ī (nisbet)|
dostane|adv|fa|dōstāne|dostça|OSM|-ane|
merdane tavır|n|fa|mardāne|erkekçe|OSM|-ane|
cahilane|adv|ar|cāhilāne|bilgisizce|OSM|-ane|
mahcubane|adv|ar|maḥcūbāne|utangaçça|OSM|-ane|
nevzat|n|fa|nav-zād|yeni doğan|OSM|nav-|
nevbahar|n|fa|nav-bahār|ilkbahar|EAT|nav-|
kalori|n|fr|calorie|ısı birimi|CUM|kar-|la:calor>fr:calorie>tr:kalori
kalorimetre|n|fr|calorimètre|ısı ölçer|CUM|kar-|la:calor+grc:métron>fr:calorimètre>tr:kalorimetre
skript|n|en|script|yazı|NEW|scribere|la:scriptum>en:script>tr:skript
manuskript|n|fr|manuscrit|elle yazılmış|CUM|scribere|la:manu scriptus>fr:manuscrit>tr:manuskript
transkripsiyon|n|fr|transcription|öteye yazma|CUM|scribere|la:transcriptio>fr:transcription>tr:transkripsiyon
deskriptif|adj|fr|descriptif|betimleyici|MOD|scribere|la:descriptivus>fr:descriptif>tr:deskriptif
nominal|adj|fr|nominal|ada ilişkin|CUM|nomen|la:nominalis>fr:nominal>tr:nominal
anonim|adj|fr|anonyme|adsız|CUM|nomen|grc:anṑnymos>fr:anonyme>tr:anonim
sinonim|n|fr|synonyme|eş adlı|CUM|nomen|grc:synṑnymon>fr:synonyme>tr:sinonim
antonim|n|fr|antonyme|karşıt adlı|MOD|nomen|grc:antí+ónoma>fr:antonyme>tr:antonim
nomenklatür|n|fr|nomenclature|ad çağırma|MOD|nomen|la:nomenclatura>fr:nomenclature>tr:nomenklatür
jenerasyon|n|fr|génération|doğurma|CUM|genus|la:generatio>fr:génération>tr:jenerasyon
jenerik|adj|fr|générique|türe ait|MOD|genus|la:genus>fr:générique>tr:jenerik
genetik|n|fr|génétique|doğuşla ilgili|CUM|genus|grc:genetikós>fr:génétique>tr:genetik
jen|n|fr|gène|gen|CUM|genus|grc:génos>de:Gen>fr:gène>tr:jen
gen|n|fr|gène|kalıtım birimi|CUM|genus|grc:génos>de:Gen>fr:gène>tr:gen
form|n|fr|forme|biçim|CUM|forma|la:forma>fr:forme>tr:form
format|n|fr|format|biçim|MOD|forma|la:formatus>fr:format>tr:format
formalite|n|fr|formalité|biçimsellik|CUM|forma|la:formalitas>fr:formalité>tr:formalite
reform|n|fr|réforme|yeniden biçimleme|OSM19|forma|la:reformare>fr:réforme>tr:reform
üniforma|n|fr|uniforme|tek biçim|OSM19|forma|la:uniformis>fr:uniforme>tr:üniforma
deformasyon|n|fr|déformation|biçim bozulması|CUM|forma|la:deformatio>fr:déformation>tr:deformasyon
platform|n|fr|plate-forme|düz biçim|CUM|forma|fr:plate-forme>tr:platform
kord|n|fr|corde|ip|CUM|korda|grc:khordḕ>la:chorda>fr:corde>tr:kord
kordon|n|fr|cordon|küçük ip|OSM19|korda|la:chorda>fr:cordon>tr:kordon
akor|n|fr|accord|uyuşma|CUM|cor|la:accordare>fr:accord>tr:akor
akordeon|n|fr|accordéon|akor çalgısı|CUM|cor|de:Akkordeon>fr:accordéon>tr:akordeon
kordele|n|it|cordella|küçük ip|OSM19|korda|la:chorda>it:cordella>tr:kordele
periskop|n|fr|périscope|çevreyi gören|CUM|skopein|grc:perí+skopeîn>fr:périscope>tr:periskop
stetoskop|n|fr|stéthoscope|göğsü dinleyen|OSM19|skopein|grc:stêthos+skopeîn>fr:stéthoscope>tr:stetoskop
skop|n|en|scope|kapsam; gözlem aracı|NEW|skopein|grc:skopós>en:scope>tr:skop
burç|n|ar|burc|kule; burç|EAT||grc:pýrgos>ar:burc>tr:burç
kehribar|n|fa|kahrubā|saman çeken|EAT||fa:kāh-rubā>tr:kehribar
kalaycı|n|tr|kalay|kalay yapan|OSM||
maşa|n|fa|māşe|kıskaç|EAT||
tuğra|n|tr|tugrag|hükümdar imzası|DLT||
yastıkçı|n|tr|yastuk|yastık yapan|OSM||
zerdali|n|fa|zard-ālū|sarı erik|EAT||
çizmeci|n|tr|çizme|çizme yapan|OSM||
"""
