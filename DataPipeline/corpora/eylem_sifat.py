# -*- coding: utf-8 -*-
"""Korpus 3 — Günlük eylemler, sıfatlar ve zarflar (ağırlıkla öz Türkçe kökler)."""

WORDS = r"""
oturmak|v|tr|oltur-|oturmak|ORH||
kalkmak|v|tr|kalk-|kalkmak|DLT|*kalk-|
yatmak uzanmak|v|tr|yat-|uzanmak|ORH|*yat-|
uzanmak|v|tr|uzan-|boylu boyunca yatmak|OSM||
uzamak|v|tr|uza-|uzun olmak|DLT||
uzatmak|v|tr|uzat-|uzun hâle getirmek|DLT||
kısalmak|v|tr|kısal-|kısa olmak|OSM||
büyümek|v|tr|bedü-|büyük olmak|ORH||
küçülmek|v|tr|kiçig|küçük olmak|OSM||
yükselmek yücelmek|v|tr|yüksel-|yükselmek|EAT|*yük-|
alçalmak|v|tr|alçal-|aşağı inmek|OSM||
alçak|adj|tr|alçak|aşağıda; aşağılık|DLT||
inip çıkmak|v|tr|én-|inip çıkmak|OSM|*in-|
tırmanmak|v|tr|tırman-|yukarı çıkmak|OSM|*tırma-|
atlamak|v|tr|atla-|sıçramak|DLT|*at-|
sıçramak|v|tr|sıçra-|zıplamak|DLT||
zıplamak|v|tr|zıpla-|sıçramak|OSM||
koşturmak|v|tr|koştur-|koşmasını sağlamak|OSM|*koş-|
yürüyüşe çıkmak|v|tr|yorı-|yürümek|OSM|*yürü-|
adımlamak|v|tr|adım|adım adım yürümek|OSM||
adım|n|tr|adım|adım|DLT||
durup beklemek|v|tr|tur-|durmak|OSM|*dur-|
dinmek|v|tr|tın-|kesilmek|DLT||
bitirmek tamamlamak|v|tr|bütür-|tamamlamak|DLT|*bit-|
tamamlamak|v|ar|tamām|bitirmek|OSM||
sürdürmek|v|tr|sürdür-|devam ettirmek|DD|*sür-|
başlatmak|v|tr|başlat-|başlamasını sağlamak|TDK||
bırakmak|v|tr|bırak-|terk etmek|DLT||
terk|n|ar|tark|bırakma|EAT|T-R-K|
vazgeçmek|v|fa|bāz|bırakmak|OSM|*geç-|
unutmak|v|tr|unıt-|hatırlamamak|ORH||
hatırlamak|v|ar|ḫāṭir|anımsamak|OSM||
anlatmak|v|tr|aŋlat-|açıklamak|DLT|*an-|
açıklamak|v|tr|açıkla-|izah etmek|DD|*aç-|
sormak soruşturmak araştırmak|v|tr|sor-|sormak|DLT|*sor-|
yanıt vermek|v|tr|yanıt|cevaplamak|DD||
cevaplamak|v|ar|cawāb|yanıtlamak|OSM||
bağırmak|v|tr|bakır-|yüksek sesle seslenmek|DLT|*bağır|
çağırmak|v|tr|çakır-|seslenmek|DLT||
çığırmak|v|tr|çıkır-|türkü söylemek|DLT||
seslenmek|v|tr|ses|ses etmek|OSM||
fısıldamak|v|tr|fısılda-|alçak sesle konuşmak|OSM||
susmak|v|tr|sus-|konuşmamak|DLT||
sessizleşmek|v|tr|sessiz|sesini kesmek|TDK||
ağlaşmak|v|tr|ıgla-|birlikte ağlamak|DLT|*ağla-|
gülüşmek|v|tr|kül-|birlikte gülmek|DLT|*gül-|
sevinmek coşmak|v|tr|sebin-|sevinmek|ORH|*sev-|
coşmak|v|tr|çoş-|taşmak|OSM||
kızmak|v|tr|kız-|öfkelenmek|DLT||
öfkelenmek|v|tr|öpke|kızmak|OSM||
küsmek|v|tr|küs-|gücenmek|DLT||
darılmak|v|tr|tarıl-|gücenmek|OSM||
barışmak|v|tr|barış-|uzlaşmak|DLT||
uzlaşmak|v|tr|uzlaş-|anlaşmak|DD|*uz|
anlaşıp uzlaşmak|v|tr|aŋla-|anlaşmak|OSM|*an-|
kavga etmek|v|fa|ġavġā|dövüşmek|OSM||
kavga|n|fa|ġavġā|gürültü; dövüş|EAT||
dövmek|v|tr|tög-|vurmak|DLT||
dövüşmek|v|tr|tögüş-|karşılıklı dövmek|DLT||
itmek|v|tr|it-|itmek|DLT||
çekiştirmek|v|tr|çekiş-|çekmek|OSM|*çek-|
kaldırmak|v|tr|kaldır-|yukarı almak|DLT||
taşımak götürmek|v|tr|taşı-|taşımak|DLT|*taşı-|
götürmek|v|tr|kötür-|alıp gitmek|ORH||
getirip götürmek|v|tr|keltür-|getirmek|ORH|*gel-|
göndermek|v|tr|könder-|yollamak|DLT||
yollamak|v|tr|yolla-|göndermek|OSM||
ulaştırmak|v|tr|ulaştır-|götürmek|DD|*ulaş-|
dağıtmak|v|tr|tagıt-|yaymak|DLT||
dağılmak|v|tr|tagıl-|parçalanmak|DLT||
toplamak biriktirmek|v|tr|topla-|toplamak|DLT||
biriktirmek|v|tr|biriktir-|toplamak|OSM||
saklamak gizlemek|v|tr|sakla-|gizlemek|DLT||
gizlemek|v|tr|kizle-|saklamak|DLT||
gizli|adj|tr|kizlig|saklı|DLT||
aramak|v|tr|ara-|bulmaya çalışmak|DLT||
bulup çıkarmak|v|tr|bul-|bulmak|DLT|*bul-|
kaybetmek yitirmek|v|tr|yit-|yitirmek|DLT||
yitirmek|v|tr|yitür-|kaybetmek|DLT||
yitmek|v|tr|yit-|kaybolmak|DLT||
kazanmak elde etmek|v|tr|kazgan-|kazanmak|ORH||
yenmek|v|tr|yéŋ-|galip gelmek|ORH||
yenilmek|v|tr|yéŋil-|mağlup olmak|DLT||
yarışmak|v|tr|yarış-|rekabet etmek|DLT||
oynaşmak|v|tr|oyna-|birlikte oynamak|DLT||
eğlenmek|v|tr|eglen-|hoşça vakit geçirmek|EAT||
eğlence|n|tr|eğlence|zevkli vakit|OSM||
dinlenip eğlenmek|v|tr|tınlan-|dinlenmek|DLT||
uyuyakalmak|v|tr|udı-|uykuya dalmak|OSM||
uyandırmak|v|tr|odgur-|uyandırmak|DLT||
düş görmek|v|tr|tüş|rüya görmek|DLT|*kör-|
yıkanmak|v|tr|yukan-|banyo yapmak|DLT||
yıkamak|v|tr|yu-|temizlemek|ORH||
temizlemek|v|ar|tamīz|arıtmak|OSM||
temiz|adj|ar|tamīz|arı|EAT|M-Y-Z|
kirlenmek|v|tr|kir|pislenmek|OSM||
kir|n|tr|kir|pislik|DLT||
kirli|adj|tr|kirlig|pis|DLT||
taramak düzeltmek|v|tr|tara-|taramak|DLT||
giyinmek|v|tr|kedin-|giysi giymek|DLT||
soyunmak|v|tr|soyun-|giysi çıkarmak|DLT||
soymak|v|tr|soy-|kabuğunu çıkarmak|DLT||
örtünmek|v|tr|örtün-|örtü ile kapanmak|DLT|*ört-|
pişirmek|v|tr|bışur-|pişirmek|DLT||
pişmek|v|tr|bış-|pişmek|DLT||
kızartmak|v|tr|kızart-|kızartmak|OSM||
kaynatmak|v|tr|kaynat-|kaynatmak|DLT||
kaynamak|v|tr|kayna-|kaynamak|DLT|*kayna-|
haşlamak|v|tr|haşla-|kaynar suda pişirmek|OSM||
doğramak|v|tr|togra-|parçalara ayırmak|DLT||
ezmek|v|tr|ez-|ezmek|DLT||
karıştırmak|v|tr|karıştur-|karmak|DLT||
karmak|v|tr|kar-|karıştırmak|ORH||
yoğurmak|v|tr|yogur-|hamur yoğurmak|DLT||
tatmak|v|tr|tat-|tadına bakmak|DLT||
yutmak|v|tr|yut-|yutmak|DLT||
çiğnemek|v|tr|çeyne-|çiğnemek|DLT||
ısırmak|v|tr|ısır-|dişlemek|DLT||
emmek|v|tr|em-|emmek|DLT|*em-|
doymak|v|tr|tod-|doymak|ORH||
acıkmak|v|tr|açık-|aç olmak|DLT||
aç|adj|tr|aç|aç|ORH||
susamak|v|tr|suvsa-|su istemek|DLT||
tok|adj|tr|tok|doymuş|ORH||
beslemek|v|tr|besle-|yedirmek|DLT||
besin|n|tr|besin|gıda|DD||
gıda|n|ar|ġiḏāʾ|besin|EAT||
büyütmek|v|tr|bedüt-|yetiştirmek|DLT||
yetiştirmek|v|tr|yetiştür-|büyütmek|OSM||
yetişmek|v|tr|yetiş-|erişmek|DLT||
ekmek dikmek|v|tr|ek-|tohum ekmek|ORH|*ek-|
sulamak|v|tr|suvla-|su vermek|DLT||
budamak|v|tr|buta-|dal kesmek|DLT||
biçmek kesmek|v|tr|biç-|biçmek|DLT|*kes-|
toplayıp derlemek|v|tr|térle-|derlemek|DLT||
öğütmek|v|tr|ögit-|un yapmak|DLT||
dövmek harman|v|tr|tög-|harman dövmek|DLT||
satın almak|v|tr|satıgın al-|satın almak|OSM|*sat-|
ödemek harcamak|v|tr|öte-|ödemek|DLT||
harcamak|v|ar|ḫarc|para sarf etmek|OSM|H-R-C|
harç|n|ar|ḫarc|gider; sıva|EAT|H-R-C|
masraf|n|ar|maṣraf|gider|EAT|S-R-F|
biriktirip saklamak|v|tr|birik-|biriktirmek|OSM||
ölçmek|v|tr|ölç-|ölçmek|DLT||
ölçü|n|tr|ölçüg|miktar|DLT||
ölçek|n|tr|ölçek|ölçü aracı|DLT||
saymak hesaplamak|v|tr|sa-|saymak|ORH|*say-|
hesaplayıp bölmek|v|tr|böl-|bölmek|DLT|*böl-|
çarpıp toplamak|v|tr|çarp-|çarpmak|DLT||
yazıp çizmek|v|tr|yaz-|yazmak|ORH|*yaz-|
okuyup anlamak|v|tr|okı-|okumak|ORH|*oku-|
öğretip öğrenmek|v|tr|ögren-|öğrenmek|DLT|*ög-|
ezberlemek|v|fa|az bar|belleğe almak|OSM||
ezber|n|fa|az bar|bellekten|EAT||
çözümlemek|v|tr|çözümle-|analiz etmek|DD|*çöz-|
çözümleme|n|tr|çözümleme|analiz|DD|*çöz-|
denemek sınamak|v|tr|sına-|denemek|DLT||
başarmak kazanmak|v|tr|başar-|başarmak|DLT||
beceri|n|tr|beceri|yetenek|DD||
becermek|v|tr|becer-|yapabilmek|OSM||
yetenek|n|tr|yetenek|kabiliyet|DD||
kabiliyet|n|ar|qābiliyya|yeterlilik|OSM||
yeterli|adj|tr|yeter|kâfi|OSM||
yetmek|v|tr|yét-|erişmek; kâfi gelmek|ORH||
eksik|adj|tr|egsük|noksan|DLT||
eksilmek|v|tr|egsü-|azalmak|DLT||
artmak|v|tr|art-|çoğalmak|ORH||
artırmak|v|tr|artur-|çoğaltmak|DLT||
azalmak|v|tr|azal-|eksilmek|OSM||
çoğalmak|v|tr|çokal-|artmak|OSM||
doldurup boşaltmak|v|tr|tol-|doldurmak|DLT|*dol-|
akıtmak|v|tr|akıt-|akmasını sağlamak|DLT||
dökmek|v|tr|tök-|dökmek|ORH||
dökülmek|v|tr|tökül-|saçılmak|DLT||
sızmak|v|tr|sız-|yavaş akmak|DLT||
damlamak|v|tr|tamla-|damla damla akmak|DLT||
damla|n|tr|tamla|damla|DLT||
ıslanmak|v|tr|ıslan-|sulanmak|OSM||
ıslak|adj|tr|ıslak|nemli|OSM||
kurumak|v|tr|kurı-|suyu gitmek|DLT|*kork-|
kurutmak|v|tr|kurıt-|kurutmak|DLT||
nemli|adj|ar|nam|rutubetli|OSM||
nem|n|ar|nam|rutubet|OSM||
rutubet|n|ar|ruṭūba|yaşlık|EAT||
donmak|v|tr|toŋ-|buz tutmak|DLT|*don-|
erimek|v|tr|eri-|sıvı olmak|DLT||
eritmek|v|tr|erit-|eritmek|DLT||
ısıtmak|v|tr|ısıt-|sıcak hâle getirmek|DLT||
ısınmak|v|tr|ısın-|sıcak olmak|DLT|*ısı-|
soğutmak|v|tr|sogıt-|soğuk hâle getirmek|DLT||
soğumak|v|tr|sogı-|soğuk olmak|DLT||
üflemek|v|tr|üfle-|soluk vermek|OSM||
esip savurmak|v|tr|es-|esmek|DLT||
savurmak|v|tr|sabur-|rüzgâra atmak|DLT||
uçurmak|v|tr|uçur-|uçmasını sağlamak|DLT|*uç-|
düşürmek yıkmak|v|tr|tüşür-|düşürmek|DLT|*düş-|
devirmek|v|tr|tevür-|yıkmak|DLT||
devrilmek|v|tr|tevril-|yan yatmak|OSM||
dayamak|v|tr|taya-|yaslamak|DLT||
dayanmak|v|tr|tayan-|yaslanmak; katlanmak|DLT||
dayanıklı|adj|tr|dayanıklı|sağlam|TDK||
yaslanmak|v|tr|yasla-|dayanmak|OSM||
eğilmek|v|tr|egil-|bükülmek|DLT||
bükmek|v|tr|bük-|kıvırmak|DLT||
bükülmek|v|tr|bükül-|kıvrılmak|DLT||
kıvırmak|v|tr|kıvır-|bükmek|OSM||
katlamak|v|tr|katla-|kat yapmak|OSM||
açılıp kapanmak|v|tr|aç-|açılmak|ORH|*aç-|
kapanmak|v|tr|kapan-|örtülmek|DLT|*kap-|
kilitlemek|v|el|kleidí|kilit vurmak|OSM||
sürgülemek|v|tr|sürgü|sürgü ile kapamak|OSM|*sür-|
delmek|v|tr|tel-|delik açmak|DLT||
delik|n|tr|telük|oyuk|DLT||
oymak|v|tr|oy-|çukur açmak|DLT||
kazıp oymak|v|tr|kaz-|kazmak|DLT||
yontup biçimlemek|v|tr|yon-|yontmak|DLT||
çakmak vurmak|v|tr|çak-|çakmak|DLT||
takmak|v|tr|tak-|iliştirmek|DLT|*tak-|
çıkartmak|v|tr|çıkart-|çıkarmak|OSM|*çık-|
sökmek|v|tr|sök-|yerinden çıkarmak|DLT||
sökülmek|v|tr|sökül-|çözülmek|DLT||
dikip onarmak|v|tr|tik-|dikmek|ORH|*dik-|
yamamak|v|tr|yama-|yama yapmak|DLT||
yama|n|tr|yama|yama|DLT||
boyayıp süslemek|v|tr|bodu-|boyamak|DLT||
süslemek|v|tr|süsle-|bezemek|OSM||
süs|n|tr|süs|bezek|OSM||
bezemek|v|tr|beze-|süslemek|DLT||
bezek|n|tr|bezek|süs|DLT||
parlatmak|v|tr|parlat-|parlak hâle getirmek|OSM||
parlak|adj|tr|parlak|ışıltılı|OSM||
sönmek|v|tr|sön-|ışığı kesilmek|DLT||
söndürmek|v|tr|söndür-|söndürmek|DLT||
yakıp yıkmak|v|tr|yak-|yakmak|ORH|*yan-|
tutuşmak|v|tr|tutuş-|alev almak|OSM|*tut-|
alev|n|fa|ʿalaw|yalım|EAT||
yalım|n|tr|yalın|alev|DLT|*yal-|
duman|n|tr|tuman|duman|DLT||
kül|n|tr|kül|kül|DLT||
kömür|n|tr|kömür|kömür|DLT||
odun|n|tr|otuŋ|yakacak|ORH||
hızlı|adj|tr|hız|süratli|DD||
çabuk|adj|fa|çābuk|hızlı|EAT||
tez elden|adv|fa|tēz|hızlıca|OSM||
ağır ağır|adv|tr|agır|yavaşça|OSM||
derin|adj|tr|teriŋ|derin|ORH||
sığ|adj|tr|sıg|derin olmayan|DLT||
dar|adj|tr|tar|dar|DLT||
kalın|adj|tr|kalın|kalın|DLT||
seyrek|adj|tr|seyrek|aralıklı|DLT||
sık|adj|tr|sık|yoğun|DLT||
yoğun|adj|tr|yogun|kalın, sık|DLT||
dolgun|adj|tr|dolgun|tombul|OSM|*dol-|
tombul|adj|tr|tombul|şişman|OSM||
cılız|adj|tr?|cılız|zayıf|OSM||
sağlam yapılı|adj|tr|saglam|güçlü|OSM||
çürük|adj|tr|çürük|bozulmuş|DLT||
çürümek|v|tr|çürü-|bozulmak|DLT||
taze|adj|fa|tāze|yeni|EAT||
bayat|adj|ar|bāʾit|gecelemiş|EAT||
olgunlaşmak|v|tr|olgun|yetişmek|TDK|*ol-|
ham|adj|fa|ḫām|olmamış|EAT||
pişkin|adj|tr|bışgın|iyi pişmiş|DLT||
sıcakkanlı|adj|tr|ısıg kan|cana yakın|OSM||
soğukkanlı|adj|tr|sogık kan|serinkanlı|OSM||
içten|adj|tr|içten|samimi|DD||
samimi|adj|ar|ṣamīmī|özden|OSM||
dürüst|adj|fa|durust|doğru|EAT||
sahtekârlıkla|adv|fa|sāḫte|hileyle|OSM||
kurnaz|adj|fa?|kūrnāz|zeki ve hileci|OSM||
saf|adj|ar|ṣāf|arı; kolay aldanan|EAT||
cesur yürekli|adj|tr|yürek|cesur|OSM|*yürü-|
yürekli|adj|tr|yüreklig|cesur|DLT|*yürü-|
korkak ürkek|adj|tr|ürk-|ürkek|DLT||
ürkmek|v|tr|ürk-|korkup kaçmak|DLT||
ürkek|adj|tr|ürkek|çekingen|OSM||
çekingen|adj|tr|çekingen|utangaç|TDK|*çek-|
utangaç|adj|tr|utangaç|sıkılgan|OSM||
sabırlı dayanıklı|adj|ar|ṣabr|sabırlı|OSM|S-B-R|
aceleci|adj|ar|ʿacala|sabırsız|OSM||
acele|n|ar|ʿacala|çabukluk|EAT||
tembel uyuşuk|adj|fa|tanbal|tembel|OSM||
uyuşuk|adj|tr|uyuşuk|hareketsiz|OSM||
çalışkan gayretli|adj|tr|çalış-|gayretli|OSM|*çal-|
titiz|adj|tr|titiz|özenli|OSM||
özenli|adj|tr|özen|dikkatli|DD||
özen|n|tr|özen|itina|DD||
dikkatli|adj|ar|diqqa|özenli|OSM||
dikkat|n|ar|diqqa|incelik|EAT||
dağınık|adj|tr|dağınık|düzensiz|OSM||
düzenli|adj|tr|düzen|muntazam|OSM||
tertipli|adj|ar|tartīb|düzenli|OSM||
tertip|n|ar|tartīb|sıralama|EAT|R-T-B|
kibirli|adj|ar|kibr|büyüklenen|OSM||
alçakgönüllü|adj|tr|alçak köŋül|mütevazı|OSM||
mütevazı|adj|ar|mutawāḏiʿ|alçakgönüllü|OSM||
cömert eli açık|adj|fa|cuvān-mard|cömert|OSM||
eli açık|adj|tr|elig|cömert|OSM||
pinti|adj|tr|pinti|cimri|OSM||
hasis|adj|ar|ḫasīs|cimri|EAT||
şen şakrak|adj|fa|şen|neşeli|OSM||
şakrak|adj|tr|şakrak|neşeli|OSM||
neşeli|adj|ar|naşʾa|sevinçli|OSM|N-Ş-A|
kederli|adj|ar|kadar|üzgün|OSM||
hüzünlü|adj|ar|ḥuzn|üzgün|OSM||
melankolik|adj|fr|mélancolique|kara safralı|CUM||grc:melankholía>fr:mélancolique>tr:melankolik
kaygılı|adj|tr|kadgu|endişeli|OSM||
endişeli|adj|fa|andīşe|kaygılı|OSM||
rahatsız|adj|ar|rāḥa|huzursuz|OSM|R-W-H|
huzursuz|adj|ar|ḥuḏūr|rahatsız|OSM||
sakin|adj|ar|sākin|durgun|EAT||
dingin|adj|tr|tın-|sakin|DD||
heyecanlı|adj|ar|hayacān|coşkulu|OSM||
heyecan|n|ar|hayacān|coşku|OSM19||
coşkulu|adj|tr|coşku|heyecanlı|DD||
coşku|n|tr|coşku|heyecan|DD||
meraklı|adj|ar|marāq|ilgili|OSM||
ilgili|adj|tr|ilgi|alakalı|DD||
ilgi|n|tr|ilgi|alaka|DD||
alaka|n|ar|ʿalāqa|bağ|EAT||
ilginç|adj|tr|ilgi|enteresan|DD||
enteresan|adj|fr|intéressant|ilgi çeken|CUM||la:interesse>fr:intéressant>tr:enteresan
sıkıcı|adj|tr|sık-|bunaltıcı|OSM||
sıkmak|v|tr|sık-|sıkmak|DLT||
sıkılmak|v|tr|sıkıl-|bunalmak|OSM||
bunalmak|v|tr|bunal-|sıkıntı duymak|OSM||
bunalım|n|tr|bunalım|kriz|DD||
kriz|n|fr|crise|karar anı|CUM|krinein|grc:krísis>fr:crise>tr:kriz
"""
