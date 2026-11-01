# -*- coding: utf-8 -*-
"""Kök aileleri: kod | köken dili | çekirdek anlam | açıklama.
Üyeler lexicon.py içindeki sözcüklerin `family` alanından toplanır."""

ROOT_FAMILIES_RAW = r"""
*kör-|tr|görmek, bakmak|Eski Türkçe kör- "görmek" fiilinden; göz sözcüğü aynı kökün ad biçimi olan köz'den gelir. Görev, görgü, gösteri gibi türevler Dil Devrimi döneminde de aynı kökten üretilmiştir.
*yat-|tr|yatmak, uzanmak|Eski Türkçe yat- fiili; yatak, yatay, yatkın gibi türevler aynı kökten gelir. "Yatırım" sözcüğü 20. yüzyılda ekonomi terimi olarak türetilmiştir.
*böl-|tr|bölmek, ayırmak|Eski Türkçe böl- "ayırmak" fiilinden; bölük (askerî birlik), bölge ve bölüm aynı kökten türetilmiştir.
*bil-|tr|bilmek, tanımak|Orhun Yazıtları'ndan beri belgelenen bil- fiili; bilge, bilgi, bilim ve 1960'ların türetmesi bilgisayar aynı kökten gelir.
*yaz-|tr|yazmak, çizmek|Eski Türkçe yaz- fiili; yazı, yazgı (alın yazısı), yazıt ve yazılım aynı kökten türetilmiştir.
*oku-|tr|okumak, seslenmek|Eski Türkçe okı- "çağırmak, seslenmek" fiilinden; yazılı metni sesli okuma anlamına evrilmiştir. Okul sözcüğü 1930'larda Fransızca école'ün ses benzerliğinden yararlanılarak oku- kökünden türetilmiştir.
*sev-|tr|sevmek|Eski Türkçe seb- / sev- fiili; sevgi, sevinç, sevimli aynı kökten gelir.
*kal-|tr|kalmak, geride durmak|Eski Türkçe kal- fiili; kalıntı, kalıcı, kalan aynı kökten türetilmiştir.
*al-|tr|almak, elde etmek|Eski Türkçe al- fiili; alım, alıcı, alıntı, alışkanlık, alışveriş aynı kökten gelir.
*ver-|tr|vermek|Eski Türkçe bér- fiilinden (b- > v- değişimi); veri, verim, vergi aynı kökten türetilmiştir.
*gel-|tr|gelmek|Eski Türkçe kel- fiilinden (k- > g- değişimi); gelir, gelin, gelenek, gelecek aynı kökten gelir.
*git-|tr|gitmek|Eski Türkçe kit- / két- fiilinden; gidiş, gider, gidermek aynı kökten gelir.
*dur-|tr|durmak, ayakta olmak|Eski Türkçe tur- fiilinden (t- > d- değişimi); durum, durak, duruşma aynı kökten gelir.
*tut-|tr|tutmak, yakalamak|Eski Türkçe tut- fiili; tutum, tutsak, tutanak, tutku, tutkal aynı kökten gelir.
*kes-|tr|kesmek|Eski Türkçe kes- fiili; kesin, kesim, kesit, kesinti aynı kökten türetilmiştir.
*sür-|tr|sürmek, devam ettirmek|Eski Türkçe sür- fiili; süre, sürekli, süreç, sürgün, sürücü aynı kökten gelir.
*bak-|tr|bakmak|Eski Türkçe bak- fiili; bakım, bakış, bakan, bakanlık aynı kökten gelir. Bakan "devlet işine bakan kişi" anlamıyla 1930'larda Arapça vekil / nazır yerine türetilmiştir.
*say-|tr|saymak, hesaplamak; saygı göstermek|Eski Türkçe sa- / say- fiilinden; sayı, sayım, saygı, sayın, sayaç aynı kökten gelir.
*düş-|tr|düşmek|Eski Türkçe tüş- fiilinden; düşünce, düşünmek (tüşün- "aklına düşmek"), düşük, düşkün aynı kökten gelir.
*ol-|tr|olmak, var olmak|Eski Türkçe bol- fiilinden (b- düşmesi); olay, olanak, olası, oluşum, olgu aynı kökten türetilmiştir.
*bul-|tr|bulmak|Eski Türkçe bul- fiili; buluş, bulgu, buluntu aynı kökten gelir.
*geç-|tr|geçmek, aşmak|Eski Türkçe keç- fiilinden; geçit, geçmiş, geçerli, geçim aynı kökten gelir.
*aç-|tr|açmak|Eski Türkçe aç- fiili; açık, açıklama, açılış aynı kökten türetilmiştir.
*yap-|tr|yapmak, inşa etmek|Eski Türkçe yap- "örtmek, kapamak, inşa etmek" fiilinden; yapı, yapım, yapıt, yapay aynı kökten gelir.
*çek-|tr|çekmek|Eski Türkçe çek- fiili; çekim, çekici, çekince, çekiç aynı kökten türetilmiştir.
*koş-|tr|koşmak; katmak|Eski Türkçe koş- "katmak, yan yana koymak" fiilinden; koşu, koşul (şart) ve koşucu aynı kökten gelir.
*sor-|tr|sormak|Eski Türkçe sor- fiili; soru, sorun, sorgu, sorumlu aynı kökten türetilmiştir.
*bağ-|tr|bağlamak|Eski Türkçe ba- "bağlamak" fiilinin ad biçimi olan bağ'dan; bağlantı, bağlam, bağımlı, bağımsız aynı kökten gelir.
*doğ-|tr|doğmak|Eski Türkçe tog- / tug- fiilinden; doğu (güneşin doğduğu yön), doğa, doğal, doğum aynı kökten türetilmiştir.
*bat-|tr|batmak|Eski Türkçe bat- fiili; batı (güneşin battığı yön), batak, batkın aynı kökten gelir.
*yaş-|tr|yaşamak; yaş, ömür|Eski Türkçe yaş "yıl, ömür" adından ve yaşa- fiilinden; yaşam, yaşıt, yaşlı aynı kökten gelir.
*uç-|tr|uçmak|Eski Türkçe uç- fiili; uçak (1930'lar türetmesi), uçuş, uçurtma, uçurum aynı kökten gelir.
*bin-|tr|binmek|Eski Türkçe bin- / mün- fiilinden; binek, binici aynı kökten gelir.
*in-|tr|inmek|Eski Türkçe én- / in- fiilinden; iniş, indirim aynı kökten gelir.
*çık-|tr|çıkmak|Eski Türkçe çık- / taşık- fiilinden; çıkış, çıkar, çıktı, çıkıntı aynı kökten türetilmiştir.
*gir-|tr|girmek|Eski Türkçe kir- fiilinden; giriş, girdi, girişim aynı kökten gelir.
*taşı-|tr|taşımak|Eski Türkçe taşı- fiili; taşıt, taşıma, taşınmak aynı kökten gelir.
*ye-|tr|yemek|Eski Türkçe yé- fiili; yem, yemiş, yiyecek aynı kökten gelir. Ünlü daralması: ye-yor > yiyor.
*iç-|tr|içmek|Eski Türkçe iç- fiili; içki, içecek, içim aynı kökten gelir.
*öl-|tr|ölmek|Eski Türkçe öl- fiili; ölüm, ölü, öldürmek, ölümsüz aynı kökten gelir.
*ög-|tr|akıl, düşünce; öğrenmek|Eski Türkçe ög "akıl" adından ve ögren- fiilinden; öğrenci, öğretmen, öğüt, öğreti aynı kökten türetilmiştir.
*ür-|tr|çoğalmak, üremek|Eski Türkçe ür- / üre- fiilinden; ürün, üretim, üretmek aynı kökten gelir.
*bit-|tr|bitmek; bitmek (yetişmek)|Eski Türkçe büt- "tamamlanmak" ve bit- "yetişmek" fiillerinden; bitki, bitim, bitirmek aynı kökten gelir.
*yan-|tr|yanmak; yakmak|Eski Türkçe yan- fiili ve ettirgeni yak-; yangın, yanık, yakıt, yakıcı aynı kökten gelir.
*kır-|tr|kırmak|Eski Türkçe kır- fiili; kırık, kırılgan, kırıntı, kırgın aynı kökten gelir.
*sat-|tr|satmak|Eski Türkçe sat- fiili; satış, satıcı, satın aynı kökten gelir.
*at-|tr|atmak, fırlatmak|Eski Türkçe at- fiili; atış, atılım, atık aynı kökten gelir.
*dik-|tr|dikmek|Eski Türkçe tik- fiilinden; dikiş, dikey, dikili aynı kökten gelir.
*ek-|tr|ekmek, tohum saçmak|Eski Türkçe ek- fiili; ekin, ekim ve ekmek (yiyecek: ek- + -mek) aynı kökten gelir.
*yük-|tr|yüklemek, yükselmek|Eski Türkçe yük adından; yüklemek, yüksek, yükselmek aynı kökten gelir.
*bas-|tr|basmak|Eski Türkçe bas- fiili; baskı, basın, basamak, baskın, basınç aynı kökten türetilmiştir.
*kap-|tr|kapmak, kapamak|Eski Türkçe kap- fiili; kapı, kapak, kapalı, kaplamak, kapsamak aynı kökten gelir.
*ör-|tr|örmek, dokumak|Eski Türkçe ör- fiili; örgü, örgüt, örücü aynı kökten gelir. Örtmek ve örtü ayrı bir kök olan ört- fiilinden gelir.
*çal-|tr|çalmak, vurmak|Eski Türkçe çal- "vurmak" fiilinden; çalgı, çalışmak, çalışma aynı kökten gelir.
*an-|tr|anmak, hatırlamak|Eski Türkçe an- fiili; anı, anıt, anlam, anlamak, anlaşma aynı kökten türetilmiştir.
*tanı-|tr|tanımak|Eski Türkçe tanu- fiilinden; tanık, tanım, tanıtım aynı kökten gelir.
*var-|tr|varmak, ulaşmak; var olmak|Eski Türkçe bar- fiilinden (b- > v-); varlık, varış, varsayım aynı kökten gelir.
*de-|tr|demek, söylemek|Eski Türkçe té- fiilinden; deyim, dedikodu aynı kökten gelir. Ünlü daralması: de-yor > diyor.
*dön-|tr|dönmek|Eski Türkçe tön- fiilinden; dönem, dönüş, dönüşüm, döngü aynı kökten gelir.
*ulaş-|tr|ulaşmak, erişmek|Eski Türkçe ula- "eklemek, bağlamak" fiilinden; ulak, ulaşım, ulaştırma aynı kökten gelir.
*kon-|tr|konmak, yerleşmek|Eski Türkçe kon- fiili; konak, konu, konuk, konum, konut ve komşu (konşı) aynı kökten gelir.
*tüt-|tr|tütmek, duman çıkarmak|Eski Türkçe tüt- fiili; tütün, tütsü aynı kökten gelir.
*yor-|tr|yormak; yorumlamak|Eski Türkçe yor- "yorumlamak, tabir etmek" ve yor- "yormak" fiillerinden; yorgun, yorum aynı kökten gelir.
*boğ-|tr|boğmak|Eski Türkçe bog- fiilinden; boğaz, boğum aynı kökten gelir.
*çöz-|tr|çözmek|Eski Türkçe çöz- fiili; çözüm, çözelti aynı kökten gelir.
*üz-|tr|üzmek, kırmak|Eski Türkçe üz- "kesmek, kırmak" fiilinden; üzüntü, üzgün aynı kökten gelir.
*dol-|tr|dolmak|Eski Türkçe tol- fiilinden; dolu, dolma, dolgu aynı kökten gelir. Dolma Balkan dillerine ve Yunancaya geçmiştir.
*boş|tr|boş|Eski Türkçe boş sözcüğü; boşluk, boşanmak, boşaltmak aynı kökten gelir.
*yürü-|tr|yürümek|Eski Türkçe yorı- fiilinden; yürüyüş, yürek (yüre- "çarpmak") aynı kökten sayılır.
*kork-|tr|korkmak|Eski Türkçe kork- fiili; korku, korkunç, korkak aynı kökten gelir.
*gül-|tr|gülmek|Eski Türkçe kül- fiilinden; gülüş, gülünç, güldürü aynı kökten gelir.
*ağla-|tr|ağlamak|Eski Türkçe ıgla- fiilinden; ağlayış, ağıt aynı kökten gelir.
*sığ-|tr|sığmak|Eski Türkçe sıg- fiili; sığınak, sığınmak, sığınmacı aynı kökten gelir.
*ışı-|tr|ışımak, parlamak|Eski Türkçe yaşu- / ışı- fiilinden; ışık, ışın, ışıldak aynı kökten gelir.
K-T-B|ar|yazmak|Arapça k-t-b "yazmak" üçlü kökü; kitâb (yazılı şey), kâtib (yazan), mektûb (yazılmış), mekteb (yazı yazılan yer) aynı kökün farklı kalıplarıdır.
H-K-M|ar|hükmetmek, yargılamak|Arapça ḥ-k-m kökü; ḥakīm (bilge, hekim), ḥākim (hükmeden), ḥukm (yargı), maḥkeme (yargı yeri), ḥikmet (bilgelik) aynı kökten türer.
S-L-M|ar|esenlik, barış, teslim olmak|Arapça s-l-m kökü; selâm (esenlik), İslâm (teslimiyet), müslim (teslim olan), teslîm, selâmet aynı kökten gelir.
İ-L-M|ar|bilmek|Arapça ʿ-l-m kökü; ʿilm (bilgi), ʿālim (bilen), muʿallim (öğreten), taʿlîm (öğretme), maʿlûm (bilinen), ʿalem (dünya) aynı kökten türer.
K-L-M|ar|söz söylemek|Arapça k-l-m kökü; kelime (söz), kelâm (konuşma), mükâleme (karşılıklı konuşma) aynı kökten gelir.
A-K-L|ar|akıl, bağlamak|Arapça ʿ-q-l kökü "bağlamak, dizginlemek"; ʿaql (akıl), ʿāqil (akıllı), maʿqūl (akla uygun) aynı kökten türer.
F-K-R|ar|düşünmek|Arapça f-k-r kökü; fikr (düşünce), tefekkür (derin düşünme), mütefekkir (düşünür), efkâr (düşünceler; Türkçede "kaygı") aynı kökten gelir.
K-D-R|ar|ölçmek, güç yetirmek|Arapça q-d-r kökü; qader (ölçülen kısmet), qudret (güç), taqdîr (ölçüp biçme), miqdâr (ölçü), iqtidâr (güç sahibi olma) aynı kökten türer.
H-S-B|ar|saymak, hesaplamak|Arapça ḥ-s-b kökü; ḥisâb (hesap), muḥâsebe (hesaplaşma) aynı kökten gelir.
Ş-K-R|ar|şükretmek|Arapça ş-k-r kökü; şükr, teşekkür, şükrân, müteşekkir aynı kökten türer.
R-H-M|ar|acımak, merhamet|Arapça r-ḥ-m kökü; raḥmet, merḥamet, raḥîm, raḥmân, merḥûm (rahmete kavuşmuş) aynı kökten gelir.
K-W-N|ar|olmak, var olmak|Arapça k-w-n kökü; mekân (olunan yer), kâinât (var olanlar), imkân (olabilirlik), mümkün aynı kökten türer.
K-W-M|ar|ayağa kalkmak, dik durmak|Arapça q-w-m kökü; qiyâm, qiyâmet, maqâm (durulan yer), muqâvemet (direnme), qavim, istiqâmet, taqvîm aynı kökten gelir.
A-M-L|ar|iş, çalışmak|Arapça ʿ-m-l kökü; ʿamel (iş), ʿamele (işçi), muʿâmele (işlem), maʿmûl (yapılmış), teʿâmül aynı kökten türer.
Ş-H-D|ar|tanık olmak, görmek|Arapça ş-h-d kökü; şâhid (tanık), şehîd (tanıklık eden, şehit), şehâdet, müşâhede aynı kökten gelir.
H-S-N|ar|güzel olmak, iyilik|Arapça ḥ-s-n kökü; ḥüsn (güzellik), iḥsân (iyilik), taḥsîn (beğenme), muḥsin aynı kökten türer.
S-F-R|ar|yola çıkmak|Arapça s-f-r kökü; sefer (yolculuk), müsâfir (yolcu), sefîr (elçi), sefâret ve sofra (yol azığı sergisi) aynı kökten gelir.
N-Z-R|ar|bakmak|Arapça n-ẕ-r kökü; naẕar (bakış), manẕara (bakılan yer), nâẕır (bakan), naẕariye (kuram), münâẕara aynı kökten türer.
Z-K-R|ar|anmak, hatırlamak|Arapça ẕ-k-r kökü; ẕikr (anma), teẕkere, müẕâkere (karşılıklı anma, görüşme), meẕkûr aynı kökten gelir.
H-B-R|ar|haber vermek|Arapça ḫ-b-r kökü; ḫaber, muḫâbir, muḫâbere, iḫbâr, istiḫbârât aynı kökten türer.
T-L-B|ar|istemek, aramak|Arapça ṭ-l-b kökü; ṭaleb (istek), ṭalebe (isteyenler, öğrenci), ṭâlib, maṭlûb aynı kökten gelir.
D-R-S|ar|ders vermek, öğrenmek|Arapça d-r-s kökü; ders, medrese (ders yeri), müderris, tedrîs, tedrisat aynı kökten türer.
A-R-F|ar|bilmek, tanımak|Arapça ʿ-r-f kökü; ʿârif (bilen), ʿirfân, maʿrifet, iʿtirâf, ʿörf (bilinen gelenek), taʿrîf, maʿrûf aynı kökten gelir.
H-R-K|ar|hareket etmek|Arapça ḥ-r-k kökü; ḥareket, taḥrîk, ḥarekât, müteḥarrik aynı kökten türer.
W-S-L|ar|ulaşmak, kavuşmak|Arapça w-ṣ-l kökü; vuṣlat (kavuşma), vesîle (aracı), vâṣıl, ittiṣâl aynı kökten gelir.
T-B-A|ar|basmak, damga vurmak; yaratılış|Arapça ṭ-b-ʿ kökü; ṭabîʿat (yaratılış), ṭabîʿî, maṭbaʿa (basımevi), maṭbûʿât aynı kökten türer.
T-B-B|ar|tedavi etmek|Arapça ṭ-b-b kökü; ṭıbb (tıp), ṭabîb (hekim), ṭabâbet aynı kökten gelir.
A-D-L|ar|adil olmak, denge|Arapça ʿ-d-l kökü; ʿadâlet, ʿâdil, ʿadliye, iʿtidâl (denge), muʿâdil, taʿdîl aynı kökten türer.
H-K-K|ar|gerçek olmak, hak|Arapça ḥ-q-q kökü; ḥaqq (gerçek, hak), ḥaqîqat, ḥuqûq (haklar), ḥaqîqî, taḥqîq, muḥaqqaq aynı kökten gelir.
A-Ş-K|ar|sarmaşık gibi sarılmak, sevmek|Arapça ʿ-ş-q kökü; ʿaşq, ʿâşıq, maʿşûq aynı kökten türer.
R-S-M|ar|çizmek, iz bırakmak|Arapça r-s-m kökü; resm (çizim), resmî (kayıtlı), merâsim (törenler), ressâm aynı kökten gelir.
N-Z-M|ar|dizmek, düzenlemek|Arapça n-ẕ-m kökü; niẕâm (düzen), intiẕâm, muntaẕam, nâẕım, manẕûm, tanẕîm (Tanzimat) aynı kökten türer.
H-Y-Y|ar|yaşamak|Arapça ḥ-y-y kökü; ḥayât (yaşam), ḥayvân (canlı), iḥyâ (canlandırma) aynı kökten gelir.
M-L-K|ar|sahip olmak, hükmetmek|Arapça m-l-k kökü; mülk, melik (kral), memleket, mülkiyet, mâlik, emlâk aynı kökten türer.
H-R-R|ar|özgür olmak; yazmak|Arapça ḥ-r-r kökü; ḥürr (özgür), ḥürriyet, taḥrîr (yazma, kurtarma), muḥarrir (yazar) aynı kökten gelir.
Ş-R-K|ar|ortak olmak|Arapça ş-r-k kökü; şirket (ortaklık), şerîk (ortak), iştirâk, müşterek, şirk aynı kökten türer.
C-M-A|ar|toplamak|Arapça c-m-ʿ kökü; câmiʿ (toplayan), cumʿa (toplanma günü), cemâʿat, cemiyet, mecmûʿa (derleme), ictimâʿ aynı kökten gelir.
C-M-L|ar|güzellik; bütün|Arapça c-m-l kökü; cümle (bütün), cemâl (güzellik), cemîl aynı kökten türer.
K-L-B|ar|döndürmek, çevirmek|Arapça q-l-b kökü; qalb (dönen şey, kalp), qâlib (kalıp), inqılâb (devrim) aynı kökten gelir.
K-W-L|ar|söylemek|Arapça q-w-l kökü; qavl (söz), maqâle (söylenen), muqâvele (karşılıklı söz, sözleşme) aynı kökten türer.
W-C-D|ar|bulmak, var olmak|Arapça w-c-d kökü; vücûd (varlık, beden), mevcûd, vecd, vicdân, îcâd (bulma) aynı kökten gelir.
N-K-L|ar|taşımak, aktarmak|Arapça n-q-l kökü; naql, naqliye, naqliyât, menqûl, intiqâl aynı kökten türer.
W-K-L|ar|vekil kılmak, güvenmek|Arapça w-k-l kökü; vekîl, vekâlet, tevekkül, müvekkil aynı kökten gelir.
Ş-A-R|ar|duymak, bilmek|Arapça ş-ʿ-r kökü; şiʿr (şiir), şâʿir, şuʿûr (bilinç) aynı kökten türer.
Ş-H-R|ar|tanınmak, yaymak|Arapça ş-h-r kökü; şöhret, meşhûr, teşhîr aynı kökten gelir.
F-A-L|ar|yapmak, eylemek|Arapça f-ʿ-l kökü; fiʿl (eylem), fâʿil (yapan), faʿâl, faʿâliyet, mefʿûl aynı kökten türer.
A-B-D|ar|kulluk etmek|Arapça ʿ-b-d kökü; ʿibâdet, maʿbed (ibadet yeri), maʿbûd (tapılan), ʿubûdiyet aynı kökten gelir.
K-S-R|ar|kırmak|Arapça k-s-r kökü; kesr (kırık, kesir) ve inkisâr aynı kökten türer. Kusur ise q-ṣ-r "kısa kalmak, eksik kalmak" kökünden gelen ayrı bir sözcüktür.
H-F-Z|ar|korumak, saklamak|Arapça ḥ-f-ẕ kökü; ḥâfıẕ, ḥıfẕ, muḥâfaẕa, muḥâfıẕ, maḥfûẕ, ḥâfıẕa aynı kökten gelir.
S-N-A|ar|yapmak, imal etmek|Arapça ṣ-n-ʿ kökü; ṣanʿat (yapma ustalığı), ṣanâyiʿ (zanaatlar), ṣınâʿî aynı kökten türer.
M-D-N|ar|şehirleşmek|Arapça m-d-n kökü; medeniyet, medenî, Medîne (şehir) aynı kökten gelir.
S-Y-S|ar|yönetmek, at bakmak|Arapça s-y-s kökü; siyâset (at terbiyesi > yönetim), siyâsî, seyis (at bakıcısı) aynı kökten türer.
D-W-R|ar|dönmek|Arapça d-w-r kökü; devr (dönüş), devre, dâire (dönen, çember), idâre (döndürme), müdîr (döndüren), devrân aynı kökten gelir.
T-R-F|ar|yan, kenar|Arapça ṭ-r-f kökü; ṭaraf, eṭrâf (yanlar), bîṭaraf, ṭaraftâr aynı kökten türer.
W-Z-N|ar|tartmak|Arapça w-z-n kökü; vezn (ölçü), mîzân (terazi), vezne aynı kökten gelir.
H-M-L|ar|yüklenmek, taşımak|Arapça ḥ-m-l kökü; ḥammâl, ḥâmile (yük taşıyan), ḥamle, taḥammül, iḥtimâl aynı kökten türer.
H-R-F|ar|harf, kenar|Arapça ḥ-r-f kökü; ḥarf, taḥrîf (harf değiştirme), ḥarfiyen aynı kökten gelir.
A-H-D|ar|söz vermek|Arapça ʿ-h-d kökü; ʿahd, taʿahhüd, muʿâhede aynı kökten türer.
F-T-R|ar|yarmak, yaratmak; orucu açmak|Arapça f-ṭ-r kökü; fıṭrat (yaratılış), ifṭâr (oruç açma), fiṭre aynı kökten gelir.
S-C-D|ar|yere kapanmak|Arapça s-c-d kökü; secde, mescid (secde yeri), seccâde aynı kökten türer.
S-L-H|ar|iyi olmak, düzeltmek|Arapça ṣ-l-ḥ kökü; ṣulḥ (barış), ıṣlâḥ, ṣâliḥ, maṣlaḥat aynı kökten gelir.
D-A-W|ar|çağırmak|Arapça d-ʿ-w kökü; duʿâ (çağrı), daʿvâ (iddia), daʿvet, iddiʿâ aynı kökten türer.
T-L-A|ar|doğmak, yükselmek|Arapça ṭ-l-ʿ kökü; ṭâliʿ (yükselen yıldız, talih), muṭâlaʿa (inceleme) aynı kökten gelir.
H-W-L|ar|durum, dönüşmek|Arapça ḥ-w-l kökü; ḥâl, aḥvâl, ḥavâle, taḥvîl aynı kökten türer.
H-L-K|ar|yaratmak|Arapça ḫ-l-q kökü; ḫalq (yaratılanlar, halk), ḫilqat, aḫlâq (huylar), maḫlûq aynı kökten gelir.
S-D-K|ar|doğru olmak|Arapça ṣ-d-q kökü; ṣâdıq, ṣadaqa, ṣadâqat, taṣdîq aynı kökten türer.
A-Z-M|ar|kararlı olmak|Arapça ʿ-z-m kökü; ʿazm (kararlılık), azim, azimli ve azimsiz aynı kökten gelir. Azamet ve muazzam, ʿ-ẕ-m "büyük olmak" kökünden gelen ayrı bir ailedir.
K-M-L|ar|tam olmak|Arapça k-m-l kökü; kemâl, kâmil, tekâmül, mükemmel, ikmâl aynı kökten türer.
S-W-R|ar|biçim vermek|Arapça ṣ-w-r kökü; ṣûret (biçim), taṣvîr, taṣavvur aynı kökten gelir.
N-F-S|ar|nefes almak, can|Arapça n-f-s kökü; nefes, nefis (can, benlik), nüfûs (canlar), teneffüs aynı kökten türer.
H-D-Y|ar|yol göstermek, armağan|Arapça h-d-y kökü; hediye, hidâyet aynı kökten gelir.
K-F-R|ar|örtmek, inkâr etmek|Arapça k-f-r kökü; kâfir, küfür, kefâret aynı kökten türer.
S-B-R|ar|dayanmak|Arapça ṣ-b-r kökü; ṣabr, ṣâbir, ṣabûr aynı kökten gelir.
Z-H-R|ar|görünmek|Arapça ẕ-h-r kökü; ẕâhir, ẕuhûr, teẕâhür, maẕhar aynı kökten türer.
H-K-Y|ar|anlatmak|Arapça ḥ-k-y kökü; ḥikâye, ḥikâyet aynı kökten gelir.
A-K-D|ar|bağlamak, düğümlemek|Arapça ʿ-q-d kökü; ʿaqd (sözleşme), ʿaqîde (inanç), iʿtiqâd aynı kökten türer.
C-H-D|ar|çabalamak|Arapça c-h-d kökü; cehd, cihâd, ictihâd, mücâhid aynı kökten gelir.
dār-|fa|tutan, sahip olan|Farsça dāştan "tutmak" fiilinin -dār türevi; hükümdar, defterdar, dindar, taraftar, hissedar, bayraktar, sancaktar aynı ekle kurulmuştur.
-hāne|fa|ev, yer|Farsça ḫāne "ev"; hastane, postane, kütüphane, eczane, pastane, dershane, kahvehane, meyhane, hapishane aynı ikinci öğeyle kurulmuştur.
-kār|fa|yapan, eden|Farsça kerden "yapmak" fiilinden -kār eki; sanatkâr, hizmetkâr, bestekâr, günahkâr, sahtekâr, fedakâr aynı ekle kurulmuştur.
-zede|fa|vurulmuş, uğramış|Farsça zeden "vurmak" fiilinden -zede; afetzede, kazazede, depremzede aynı ekle kurulmuştur.
-istān|fa|yer, ülke|Farsça -stān "yer" eki; bostan, gülistan, Hindistan, Yunanistan, Macaristan, Türkistan aynı ekle kurulmuştur.
-nāme|fa|yazı, mektup|Farsça nāme "mektup, yazı"; beyanname, seyahatname, nizamname, vekâletname, şahname aynı ikinci öğeyle kurulmuştur.
-bāz|fa|oynayan|Farsça bāzīden "oynamak" fiilinden -bāz; cambaz, hokkabaz, düzenbaz, kumarbaz, sihirbaz aynı ekle kurulmuştur.
şāh|fa|hükümdar|Eski Farsça xšāyaθiya "kral"; şah, padişah, şehzade, şahane ve satrançtaki "şah mat" aynı kökten gelir.
pā|fa|ayak|Farsça pā(y) "ayak"; pabuç (pā-pūş: ayak örtüsü), paça, pijama (pā-cāme: ayak giysisi, Urduca yoluyla), payitaht aynı kökten gelir.
ser|fa|baş|Farsça ser "baş"; serdar, serbest (başı bağlı), sermaye (ana para), serüven (ser-güzeşt), serhat aynı kökten gelir.
āb|fa|su|Farsça āb "su"; abdest (el suyu), hoşaf (hoş su), gülab aynı kökten gelir.
specere|la|bakmak, görmek|Latince specere "bakmak"; spektrum (görünen), perspektif (içinden bakma), prospektüs (ileriye bakış), spekülasyon (gözlem), spesifik aynı kökten gelir.
trahere|la|çekmek|Latince trahere / tractare "çekmek"; traktör (çeken), kontrat (birlikte çekilen), portre (çekilip çıkarılan), tren, antrenman aynı kökten gelir.
graphein|el|yazmak, çizmek|Eski Yunanca gráphein "kazımak, yazmak"; fotoğraf, telgraf, paragraf, coğrafya, grafik, program, gramer, biyografi aynı kökten gelir.
logos|el|söz, akıl|Eski Yunanca lógos "söz, akıl"; analog, diyalog, katalog, biyoloji, psikoloji, teknoloji, ekoloji aynı kökten gelir.
tekhne|el|zanaat, beceri|Eski Yunanca tékhnē "zanaat"; teknik, teknoloji, teknisyen, teknokrat aynı kökten gelir.
polis|el|şehir|Eski Yunanca pólis "şehir"; politika, polis, metropol, polisiye, kozmopolit aynı kökten gelir.
caput|la|baş|Latince caput "baş"; kaptan (baş olan), kapital (baş para), kapitalizm, kapitülasyon, kep, şapka, kapüşon aynı kökten gelir.
mittere|la|göndermek|Latince mittere "göndermek"; misyon, komisyon, komite, mesaj, emisyon, transmisyon aynı kökten gelir.
ponere|la|koymak|Latince ponere "koymak"; pozisyon, pozitif, kompozisyon, depo, depozito aynı kökten gelir.
facere|la|yapmak|Latince facere "yapmak"; fabrika, fakülte, efekt, fason, ofis aynı kökten gelir.
videre|la|görmek|Latince videre "görmek"; video, vizyon, televizyon, vize, revizyon aynı kökten gelir.
currere|la|koşmak|Latince currere "koşmak"; kurs, koridor, kurye, konkur aynı kökten gelir.
ducere|la|götürmek, yönetmek|Latince ducere "götürmek"; prodüktör, prodüksiyon, kondüktör, redüksiyon, dük, düşes aynı kökten gelir.
portare|la|taşımak|Latince portare "taşımak"; rapor, pasaport, portatif, transport aynı kökten gelir.
stare|la|durmak|Latince stare "durmak" ve Yunanca hístanai; istasyon, statü, istatistik, enstitü, sistem, asistan aynı Hint-Avrupa kökünden gelir.
phone|el|ses|Eski Yunanca phōnḕ "ses"; telefon, mikrofon, fonetik, senfoni, megafon aynı kökten gelir.
kyklos|el|çember, tekerlek|Eski Yunanca kýklos "çember"; bisiklet, siklon, ansiklopedi, sirk, sirkülasyon aynı kökten gelir.
kratos|el|güç, yönetim|Eski Yunanca krátos "güç"; demokrasi, bürokrasi, aristokrasi, otokrasi, teknokrat aynı kökten gelir.
demos|el|halk|Eski Yunanca dḕmos "halk"; demokrasi, demografi, epidemi, pandemi aynı kökten gelir.
phainein|el|görünmek, ışımak|Eski Yunanca phaínein "göstermek, ışımak"; fener, fanus, fantezi, fenomen, fantastik, fantom aynı kökten gelir.
pan|el|bütün, hep|Eski Yunanca pân "hep"; panayır (pan-ēgyris: tüm toplanma), pandemi, panorama, panteon, pankreas aynı kökten gelir.
metron|el|ölçü|Eski Yunanca métron "ölçü"; metre, termometre, kilometre, geometri, simetri, parametre, barometre aynı kökten gelir.
hodos|el|yol|Eski Yunanca hodós "yol"; metot (yol boyu gidiş), periyot (çevrim yolu), katot, anot, elektrot aynı kökten gelir.
"""
