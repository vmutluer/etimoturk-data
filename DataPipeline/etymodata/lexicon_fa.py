# -*- coding: utf-8 -*-
"""Farsça kökenli sözcükler.
Biçim: lemma|pos|origin|kaynak biçim|kaynak anlam|dönem|kök ailesi|zincir"""

LEXICON_FA = r"""
hane|n|fa|ḫāne|ev|EAT|-hāne|
postane|n|it|posta-ḫāne|posta evi|OSM19|-hāne|it:posta>fa:posta-ḫāne>tr:postane
pastane|n|it|pasta-ḫāne|pasta evi|CUM|-hāne|it:pasta>fa:pasta-ḫāne>tr:pastane
kahvehane|n|ar|qahwa-ḫāne|kahve evi|OSM|-hāne|ar:qahwa>fa:qahve-ḫāne>tr:kahvehane
meyhane|n|fa|mey-ḫāne|şarap evi|EAT|-hāne|
hapishane|n|ar|ḥabs-ḫāne|tutukevi|OSM|-hāne|ar:ḥabs>fa:ḥabs-ḫāne>tr:hapishane
şifahane|n|ar|şifā-ḫāne|hastane|EAT|-hāne|ar:şifāʾ>fa:şifā-ḫāne>tr:şifahane
tımarhane|n|fa|tīmār-ḫāne|bakım evi|OSM|-hāne|
tersane|n|it|darsena|gemi yapım yeri|OSM||ar:dār aṣ-ṣināʿa>it:darsena>tr:tersane
afetzede|n|ar|āfet-zede|afete uğramış|OSM19|-zede|ar:āfa>fa:āfet-zede>tr:afetzede
kazazede|n|ar|qaḏā-zede|kazaya uğramış|OSM19|-zede|ar:qaḏāʾ>fa:kazā-zede>tr:kazazede
depremzede|n|tr|deprem-zede|depreme uğramış|MOD|-zede|
felaketzede|n|ar|falāka-zede|felakete uğramış|OSM19|-zede|ar:falāka>fa:felāket-zede>tr:felaketzede
gülistan|n|fa|gulistān|gül bahçesi|EAT|-istān|
Hindistan|n|fa|Hindūstān|Hintliler ülkesi|EAT|-istān|
Yunanistan|n|fa|Yūnānistān|Yunanlar ülkesi|OSM|-istān|ar:yūnān>fa:Yūnānistān>tr:Yunanistan
Macaristan|n|fa|Macaristān|Macarlar ülkesi|OSM|-istān|hu:magyar>fa:Macaristān>tr:Macaristan
Türkistan|n|fa|Turkistān|Türkler ülkesi|EAT|-istān|
Kazakistan|n|fa|Qazaqistān|Kazaklar ülkesi|CUM|-istān|
Özbekistan|n|fa|Özbekistān|Özbekler ülkesi|CUM|-istān|
Türkmenistan|n|fa|Türkmenistān|Türkmenler ülkesi|CUM|-istān|
Kırgızistan|n|fa|Qırğızistān|Kırgızlar ülkesi|CUM|-istān|
Afganistan|n|fa|Afġānistān|Afganlar ülkesi|OSM|-istān|
Ermenistan|n|fa|Armanistān|Ermeniler ülkesi|OSM|-istān|
Gürcistan|n|fa|Gurcistān|Gürcüler ülkesi|OSM|-istān|
Bulgaristan|n|fa|Bulġāristān|Bulgarlar ülkesi|OSM|-istān|
Sırbistan|n|fa|Sırbistān|Sırplar ülkesi|OSM|-istān|
Hırvatistan|n|fa|Hırvatistān|Hırvatlar ülkesi|OSM|-istān|
Arnavutluk|n|tr|Arnavut-luk|Arnavutlar ülkesi|OSM||
name|n|fa|nāme|mektup, yazı|EAT|-nāme|
seyahatname|n|ar|siyāḥat-nāme|gezi yazısı|OSM|-nāme|ar:siyāḥa>fa:siyāḥat-nāme>tr:seyahatname
seyahat|n|ar|siyāḥa|gezi|EAT|S-Y-H|
vekâletname|n|ar|wakālat-nāme|vekillik belgesi|OSM19|-nāme|ar:wakāla>fa:vekālet-nāme>tr:vekâletname
şahname|n|fa|şāh-nāme|şahlar kitabı|EAT|-nāme|
kanunname|n|ar|qānūn-nāme|yasa kitabı|OSM|-nāme|
siyasetname|n|ar|siyāsat-nāme|yönetim kitabı|EAT|-nāme|
cambaz|n|fa|cān-bāz|canla oynayan|EAT|-bāz|
hokkabaz|n|ar|ḥuqqa-bāz|hokka ile oynayan|OSM|-bāz|ar:ḥuqqa>fa:ḥuqqa-bāz>tr:hokkabaz
hokka|n|ar|ḥuqqa|küçük kutu|EAT||
düzenbaz|n|tr|düzen-bāz|düzen kuran|OSM|-bāz|
kumarbaz|n|ar|qimār-bāz|kumar oynayan|OSM|-bāz|ar:qimār>fa:qimār-bāz>tr:kumarbaz
kumar|n|ar|qimār|şans oyunu|EAT||
sihirbaz|n|ar|siḥr-bāz|sihir yapan|EAT|-bāz|ar:siḥr>fa:siḥr-bāz>tr:sihirbaz
sihir|n|ar|siḥr|büyü|EAT||
ateşbaz|n|fa|āteş-bāz|ateşle oynayan|OSM|-bāz|
madrabaz|n|fa|madra-bāz|hileci tüccar|OSM|-bāz|
şah|n|fa|şāh|hükümdar|EAT|şāh|
padişah|n|fa|pādişāh|koruyucu şah|EAT|şāh|
şehzade|n|fa|şāh-zāde|şah oğlu|EAT|şāh|
şahane|adj|fa|şāhāne|şaha yakışır|OSM|şāh|
şahmat|n|fa|şāh māt|şah öldü|EAT|şāh|
satranç|n|fa|çatrang|dört kol|EAT||sa:caturaṅga>pal:çatrang>fa:şatranc>tr:satranç
şehinşah|n|fa|şāhān-şāh|şahlar şahı|EAT|şāh|
pabuç|n|fa|pā-pūş|ayak örtüsü|EAT|pā|
paça|n|fa|pāçe|küçük ayak|EAT|pā|
pijama|n|fr|pyjama|ayak giysisi|CUM||
payitaht|n|fa|pāy-i taḫt|taht ayağı|OSM|pā|
piyade|n|fa|piyāde|yaya|EAT|pā|
serdar|n|fa|ser-dār|baş tutan|EAT|ser|
serbest|adj|fa|ser-best|başı bağlı|EAT|ser|
serüven|n|fa|ser-guzeşt|baştan geçen|OSM|ser|
sergüzeşt|n|fa|ser-guzeşt|baştan geçen|EAT|ser|
serhat|n|fa|ser-ḫadd|sınır başı|EAT|ser|
serlevha|n|fa|ser-lawḥa|başlık|OSM|ser|
seraser|n|fa|ser-ā-ser|baştan başa|EAT|ser|
serasker|n|fa|ser-ʿasker|ordu başı|OSM|ser|
abdest|n|fa|āb-dest|el suyu|EAT|āb|
gülab|n|fa|gul-āb|gül suyu|EAT|āb|
abıhayat|n|fa|āb-i ḥayāt|yaşam suyu|EAT|āb|
hoşab|n|fa|ḫoş-āb|tatlı su|EAT|āb|
sirke|n|fa|sirke|sirke|EAT||
turşu|n|fa|turşī|ekşi|EAT||
çorba|n|fa|şōrbā|tuzlu su|EAT||
pilav|n|fa|pilāv|pilav|EAT||
köfte|n|fa|kūfte|dövülmüş|EAT||
yahni|n|fa|yaḫnī|et yemeği|EAT||
kavurma yahnisi|n|fa|yaḫnī|yahni|OSM||
peynir|n|fa|panīr|peynir|EAT||
tarhana|n|fa|tarḫāne|tarhana|OSM||
pekmez|n|tr|bekmes|üzüm şırası|DLT||
bekmez|n|tr|bekmes|pekmez|DLT||
reçel|n|fa|rīçāl|meyve ezmesi|OSM||
kayısı kurusu|n|el|kaísi|kuru kayısı|OSM||
şeftali|n|fa|şaftālū|tüylü erik|EAT||
kiraz|n|el|kerási|kiraz|EAT||grc:kerásion>el:kerási>tr:kiraz
vişne|n|sl|višnja|vişne|OSM||bg:višnja>tr:vişne
dut|n|fa|tūt|dut|EAT||
üzümcü|n|tr|üzüm|üzüm satan|OSM||
ceviz içi|n|ar|cawz|ceviz|EAT||
leblebi|n|fa|lablabū|kavrulmuş nohut|OSM||
pazarlık|n|fa|bāzār|fiyat tartışması|OSM||
bazar|n|fa|bāzār|çarşı|DLT||
dükkâncı|n|ar|dukkān|dükkân sahibi|OSM||
çeşme|n|fa|çeşme|göz; kaynak|EAT||
havuz|n|ar|ḥawḏ|havuz|EAT||
şadırvan|n|fa|şādurvān|fıskiyeli havuz|EAT||
bağ bozumu|n|fa|bāġ|bağ bozumu|OSM||
bahar|n|fa|bahār|ilkbahar|EAT||
baharat|n|ar|bahārāt|kokulu bitkiler|OSM||
gül|n|fa|gul|gül|EAT||
bülbül|n|fa|bulbul|bülbül|EAT||
lale|n|fa|lāle|lale|EAT||
sümbül|n|fa|sunbul|sümbül|EAT||
nergis|n|fa|nargis|nergis|EAT||grc:nárkissos>fa:nargis>tr:nergis
menekşe|n|fa|banafşe|menekşe|EAT||
yasemin|n|fa|yāsamīn|yasemin|EAT||
zambak|n|ar|zanbaq|zambak|EAT||
çınar|n|fa|çinār|çınar|EAT||
servi|n|fa|sarv|servi|EAT||
kavak|n|tr|kavak|kavak|DLT||
çam|n|tr|çam|çam|EAT||
meşe|n|fa|mīşe|meşe|EAT||
ceviz ağacı|n|ar|cawz|ceviz ağacı|EAT||
fidan|n|el|fytáni|fidan|EAT||
tohumluk|n|fa|tuḫm|tohum|EAT||
can|n|fa|cān|ruh, hayat|EAT||
canavar|n|fa|cānāvar|canlı, hayvan|EAT||
cihan|n|fa|cihān|dünya|EAT||
cihangir|n|fa|cihān-gīr|dünya tutan|EAT||
derya|n|fa|daryā|deniz|EAT||
âb-ı revan|n|fa|āb-i revān|akarsu|EAT|āb|
ateş|n|fa|ātaş|ateş|EAT||
rüzgâr|n|fa|rōzgār|zaman, devran|EAT||
hava|n|ar|hawāʾ|hava|EAT||
asuman|n|fa|āsmān|gök|EAT||
sitare|n|fa|sitāre|yıldız|EAT||
mah|n|fa|māh|ay|EAT||
hurşit|n|fa|ḫorşīd|güneş|EAT||
şeb|n|fa|şab|gece|EAT||
ruz|n|fa|rōz|gün|EAT||
nevruz|n|fa|nav-rōz|yeni gün|EAT||
şehriyar|n|fa|şahriyār|hükümdar|EAT||
hane halkı|n|fa|ḫāne|ev halkı|OSM|-hāne|
hanedan|n|fa|ḫānedān|soy|EAT||
şehzade sarayı|n|fa|şāh-zāde|şehzade konağı|OSM|şāh|
taht|n|fa|taḫt|hükümdar koltuğu|EAT||
taç|n|fa|tāc|taç|EAT||
tahtırevan|n|fa|taḫt-i revān|yürüyen taht|EAT||
peygamber|n|fa|payġāmbar|haber getiren|EAT||
peygamberlik|n|fa|payġāmbar|nebilik|EAT||
ferman|n|fa|farmān|buyruk|EAT||
berat|n|ar|barāʾa|belge|EAT|B-R-A|
divanhane|n|fa|dīvān-ḫāne|divan odası|OSM|-hāne|
vezir|n|ar|wazīr|yük taşıyan|EAT|W-Z-R|
sadrazam|n|ar|ṣadr-i aʿẕam|en büyük baş|OSM|A-Ẕ-M|
paşa|n|fa|pādişāh|yüksek rütbeli|EAT||
ağa kapısı|n|tr|aga|ağa konağı|OSM||
çavuş|n|tr|çavuş|haberci subay|DLT||
yeniçeri|n|tr|yeni çeri|yeni asker|EAT||
çeri|n|tr|çerig|asker|ORH||
leventlik|n|it|levante|doğulu denizci|OSM||
levent|n|it|levante|doğu; denizci|OSM||it:levante>tr:levent
sipahi|n|fa|sipāhī|asker|EAT||
sipah|n|fa|sipāh|ordu|EAT||
pehlivan|n|fa|pahlavān|yiğit|EAT||
kahraman|n|fa|qahramān|yiğit|EAT||
şahbaz|n|fa|şāh-bāz|kral kuşu, yiğit|EAT|şāh|
merdane|adj|fa|mardāne|erkekçe|EAT||
mert|adj|fa|mard|erkek, yiğit|EAT||
namert|adj|fa|nā-mard|yiğit olmayan|EAT||
dilaver|adj|fa|dilāver|yürekli|EAT||
dilber|n|fa|dilber|gönül alan|EAT||
dil|n|fa|dil|gönül|EAT||
gönülçelen|n|tr|köŋül|gönül çelen|OSM||
yâr-i vefadar|n|fa|yār|vefalı yâr|OSM||
dost meclisi|n|fa|dōst|dost toplantısı|OSM||
düşmanlık|n|fa|duşman|husumet|EAT||
ahenk|n|fa|āhang|uyum|EAT||
nağme|n|ar|naġma|ezgi|EAT|N-Ğ-M|
makam müziği|n|ar|maqām|makam|OSM|K-W-M|
saz|n|fa|sāz|çalgı|EAT||
tambur|n|fa|tanbūr|telli çalgı|EAT||
kanun çalgısı|n|ar|qānūn|çalgı|EAT||
ney|n|fa|nay|kamış|EAT||
kemençe|n|fa|kemānçe|küçük yay|EAT||
keman|n|fa|kemān|yay|EAT||
def|n|ar|daff|def|EAT||
davul|n|tr|tavul|davul|DLT||
zurna|n|fa|sūrnāy|düğün kamışı|EAT||
çeng|n|fa|çang|arp|EAT||
rakkase|n|ar|raqqāṣa|dansçı kadın|OSM||
raks|n|ar|raqṣ|dans|EAT||
hanende|n|fa|ḫānende|okuyan|OSM||
sazende|n|fa|sāzende|çalan|OSM||
şarkıcı|n|fa|şarqī|şarkı söyleyen|OSM||
güfte|n|fa|gufte|söylenmiş|OSM||
beste yapımı|n|fa|beste|beste|OSM||
hoş|adj|fa|ḫoş|güzel, iyi|EAT||
hoşnut|adj|fa|ḫoşnūd|memnun|EAT||
hoşgörü|n|tr|hoş-görü|tolerans|DD||
şad|adj|fa|şād|sevinçli|EAT||
şen|adj|hy|şēn|bayındır, şenlikli|EAT||
mutlu haber|n|tr|mutlu|müjde|OSM||
müjde|n|fa|muzhde|iyi haber|EAT||
armağan|n|tr|armagan|hediye|DLT||
bahşiş|n|fa|baḫşīş|bağış|EAT||
bağışlamak|v|tr|bagışla-|affetmek|DLT|*bağ-|
ihsan etmek|v|ar|iḥsān|bağışlamak|OSM|H-S-N|
pişman|adj|fa|paşīmān|pişman|EAT||
perişan|adj|fa|parīşān|dağınık|EAT||
divane|adj|fa|dīvāne|deli|EAT||
deli|adj|tr|telve|deli|DLT||
sersem|adj|fa|sersām|baş dönmesi|EAT||
tembel|adj|fa|tanbal|tembel|EAT||
çalak|adj|fa|çālāk|çevik|EAT||
çevik|adj|tr|çevik|atik|EAT||
zor|n|fa|zōr|güç|EAT||
zorba|n|fa|zōr-bā|zorla alan|OSM||
zorluk|n|fa|zōr|güçlük|OSM||
kolay|adj|tr|kolay|basit|EAT||
güç yetirmek|v|tr|küç|gücü yetmek|OSM||
nazik|adj|fa|nāzuk|ince|EAT||
nazlı|adj|fa|nāz|naz eden|EAT||
naz|n|fa|nāz|cilve|EAT||
cilve|n|ar|cilwa|görünme|EAT||
işve|n|fa|işve|cilve|EAT||
zarif|adj|ar|ẕarīf|ince|EAT|Ẕ-R-F|
kibar|adj|ar|kibār|büyükler|OSM||
hürmetkâr|adj|ar|ḥurmet-kār|saygılı|OSM|-kār|ar:ḥurma>fa:ḥurmet-kār>tr:hürmetkâr
aferin|intj|fa|āferīn|övgü|EAT||
maşallah|intj|ar|mā şāʾa llāh|Allah ne dilerse|EAT||
inşallah|intj|ar|in şāʾa llāh|Allah dilerse|EAT||
elhamdülillah|intj|ar|al-ḥamdu li-llāh|Allah'a hamd|EAT||
bismillah|intj|ar|bi-smi llāh|Allah'ın adıyla|EAT||
hayhay|intj|tr|hay hay|elbette|OSM||
haydi|intj|tr|haydi|çabuk|OSM||
hadi|intj|tr|haydi|çabuk|OSM||
heyhat|intj|ar|hayhāt|ne yazık|EAT||
eyvah|intj|fa|ay vāh|ne yazık|EAT||
vay|intj|tr|vay|şaşma ünlemi|EAT||
yazık|intj|tr|yazuk|günah; acıma|DLT||
peki|intj|fa|pek-i|tamam|OSM||
evet|intj|tr|evet|olumlu yanıt|DLT||
hayır|intj|ar|ḫayr|iyilik; olumsuz yanıt|EAT|Ḫ-Y-R|
yok|adv|tr|yok|mevcut değil|ORH||
tamam|adj|ar|tamām|bütün|EAT||
bitti|intj|tr|bütti|tamamlandı|DLT|*bit-|
tane|n|fa|dāne|tohum, adet|EAT||
adet|n|ar|ʿadad|sayı|EAT||
çift|n|fa|cuft|çift|EAT|cuft|
tek|adj|tr|tek|yalnız|DLT||
hane sayısı|n|fa|ḫāne|ev sayısı|OSM|-hāne|
numara|n|it|numero|sayı|OSM19||la:numerus>it:numero>tr:numara
rakam|n|ar|raqam|işaret, sayı|OSM||
sıfır|n|ar|ṣifr|boş|OSM||ar:ṣifr>tr:sıfır
hiçlik|n|fa|hīç|yokluk|OSM||
yarı yarıya|adv|tr|yarı|eşit bölünmüş|OSM||
avare|adj|fa|āvāre|başıboş|EAT||
yaban|n|fa|yābān|çöl, kır|EAT||
yabancı|n|fa|yābān|yabandan gelen|EAT||
yabani|adj|fa|yābān|vahşi|EAT||
sahra|n|ar|ṣaḥrāʾ|çöl|EAT||
çöl|n|tr|çöl|çöl|DLT||
kır|n|tr|kır|kır|DLT||
ova|n|tr|oba|düzlük|EAT||
vadi|n|ar|wādī|dere yatağı|EAT||
tepe|n|tr|töpü|tepe|DLT||
yamaç|n|tr|yamaç|yan|OSM||
kaya|n|tr|kaya|kaya|DLT||
mağara|n|ar|maġāra|mağara|EAT||
ada|n|tr|ada|ada|DLT||
yarımada|n|tr|yarım ada|yarımada|DD||
kıyı|n|tr|kıdıg|kenar|DLT||
sahil|n|ar|sāḥil|kıyı|EAT||
liman|n|el|limáni|liman|EAT||grc:limḕn>el:limáni>tr:liman
körfez|n|el|kólpos|koy|OSM||
boğaz köprüsü|n|tr|boguz|boğaz köprüsü|MOD|*boğ-|
harman|n|fa|ḫarman|ekin yığını|EAT||
hasat|n|ar|ḥaṣād|biçme|OSM|H-S-D|
çiftçi|n|fa|cuft|çift süren|EAT|cuft|
çiftlik|n|fa|cuft|çiftlik|OSM|cuft|
rençber|n|fa|ranc-bar|zahmet taşıyan|EAT||
bağban|n|fa|bāġbān|bağ bekçisi|EAT||
bahçıvan|n|fa|bāġçevān|bahçe bakıcısı|EAT||
çoban|n|fa|şubān|koyun bakan|EAT||
kervancı|n|fa|kārvān|kervan sahibi|EAT||
seyyah|n|ar|sayyāḥ|gezgin|OSM|S-Y-H|
gezgin|n|tr|gezgin|seyyah|DD|*gez-|
gezmek|v|tr|kez-|dolaşmak|DLT|*gez-|
gezi|n|tr|gezi|seyahat|DD|*gez-|
yolcu|n|tr|yolçı|yola giden|DLT||
yolculuk|n|tr|yolçılık|seyahat|OSM||
menzil|n|ar|manzil|konak yeri|EAT|N-Z-L|
konak yeri|n|tr|konak|menzil|OSM|*kon-|
tüccar kervanı|n|ar|tuccār|kervan|OSM||
ipek yolu|n|tr|yipek|İpek Yolu|MOD||
sınır boyu|n|tr|sınır|serhat|OSM||
hudut|n|ar|ḥudūd|sınırlar|EAT|H-D-D|
gümrük|n|el|kommérkion|ticaret vergisi|EAT||la:commercium>el:kommérkion>tr:gümrük
vergi memuru|n|tr|bérgü|vergi memuru|OSM|*ver-|
"""
