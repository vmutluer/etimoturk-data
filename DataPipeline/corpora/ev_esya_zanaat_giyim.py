# -*- coding: utf-8 -*-
"""Korpus 23 — Ev eşyası, aletler, zanaat, giyim-kuşam, müzik ve oyun: mobilya, kaplar, dokuma ve dikiş, giysi ve ayakkabı,
mücevher ve bakım, demirci-dökümcü-saraç gibi zanaatlar, çalgılar ve müzik türleri, dans, oyunlar ve spor terimleri;
Balkan ve Macar Türkizmleri ile Türk dünyası denklikleri üzerinde durulmuştur."""

WORDS = r"""
# --- Ev döşemesi, mobilya ---
şilte|n|fa|şilte|ince döşek, minder|OSM||
cibinlik|n|tr|çibin|sinek; sinek örtüsü|OSM||
sini|n|fa|sīnī|Çin işi büyük tepsi|EAT||
konsol|n|fr|console|dayanak; duvar masası|OSM19||
komodin|n|it|comodino|küçük yatak dolabı|OSM19||la:commodus>it:comodino>tr:komodin
şifonyer|n|fr|chiffonnier|çekmeceli giysi dolabı|CUM|chiffe|
gardırop|n|fr|garde-robe|giysi koruyan; giysi dolabı|CUM||
büfe|n|fr|buffet|servis dolabı|OSM19||
beşik|n|tr|beşik|bebek yatağı|DLT||
salıncak|n|tr|salın-|sallanmak|OSM||
hamak|n|fr|hamac|asma yatak|CUM||es:hamaca>fr:hamac>tr:hamak
puf|n|fr|pouf|yumuşak alçak tabure|MOD||
şezlong|n|fr|chaise longue|uzun iskemle|CUM||
tabure|n|fr|tabouret|arkalıksız iskemle|OSM19||
kürsü|n|ar|kursī|taht, oturak|EAT||
rahle|n|ar|raḥl|deve semeri; kitap sehpası|EAT||
pike|n|fr|piqué|iğnelenmiş; kabartmalı dokuma|CUM||
seki|n|tr|sekü|yüksek oturma yeri|DLT||
tutamak|n|tr|tut-|tutmak|TDK|*tut-|
tutamaç|n|tr|tut-|tutmak|TDK|*tut-|
askılık|n|tr|as-|asmak|MOD||
vestiyer|n|fr|vestiaire|giysilik|CUM||la:vestiarium>fr:vestiaire>tr:vestiyer
küllük|n|tr|kül|kül kabı|OSM||
tabla|n|ar|ṭabla|tepsi; tahta|OSM|T-B-L|la:tabula>ar:ṭabla>tr:tabla
tablakâr|n|ar|ṭabla + fa. -kār|tepsi taşıyan|OSM|T-B-L|
çekmece|n|tr|çek-|çekmek|OSM|*çek-|
yolluk|n|tr|yol|yol halısı; yol azığı|OSM||
korniş|n|fr|corniche|perde çubuğu; saçak|CUM||it:cornice>fr:corniche>tr:korniş
stor|n|fr|store|sarmalı perde|MOD||it:stuoia>fr:store>tr:stor
aplik|n|fr|applique|duvara takılan lamba|MOD||
pösteki|n|fa|pōstakī|koyun postu|EAT||
döşemek|v|tr|töşe-|yaymak, sermek|DLT|*döşe-|
döşemeci|n|tr|töşe-|döşeme ustası|OSM|*döşe-|
döşemecilik|n|tr|töşe-|döşeme işi|MOD|*döşe-|
döşekçi|n|tr|töşe-|döşek yapan|OSM|*döşe-|
yorgancı|n|tr|yogurkan|yorgan diken|OSM||
mefruşat|n|ar|mafrūşāt|döşenmişler; ev tekstili|OSM19||
# --- Kaplar, kutular, mutfak eşyası ---
küfe|n|el?|kófinos|büyük sırt sepeti|OSM||grc:kóphinos>el:kófinos>tr:küfe
hurç|n|ar|ḫurc|büyük heybe|EAT||
çıkın|n|tr|çıkın|küçük bohça|OSM||
kap|n|tr|kap|kap, kılıf, zarf|DLT|*kap-|
mahfaza|n|ar|maḥfaẓa|koruma kutusu|OSM|H-F-Z|
ambalaj|n|fr|emballage|balya yapma; sarmalama|CUM||
koli|n|fr|colis|paket|CUM||it:collo>fr:colis>tr:koli
fıçı|n|el|boutsí|ağaç varil|EAT||la:buttis>el:boutsí>tr:fıçı
varil|n|fr|baril|fıçı|OSM19||
damacana|n|it|damigiana|büyük hasırlı cam şişe|OSM19||fr:dame-jeanne>it:damigiana>tr:damacana
matara|n|ar|maṭhara|temizlenme kabı; su kabı|EAT||
şişe|n|fa|şīşe|cam; cam kap|EAT||
sitil|n|el|sítla|kova|OSM||la:situla>el:sítla>tr:sitil
bakraç|n|tr|bakır|bakırdan küçük kova|OSM||
demlik|n|fa|dam|dem, buhar; demleme|OSM19||
çaydanlık|n|fa|çāy-dān|çay kabı|OSM19|-dān|zh:chá>fa:çāy-dān>tr:çaydanlık
yağdan|n|fa|-dān|kap eki; yağ kabı|OSM|-dān|
sürmedan|n|fa|surme-dān|sürme kabı|OSM|-dān|
çatal|n|tr|çat-|çatmak, birleştirmek|EAT|*çat-|
kütük|n|tr|kütük|ağaç gövdesi|DLT||
kalbur|n|ar|ġirbāl|iri elek|EAT||la:cribellum>ar:ġirbāl>tr:kalbur
tekne|n|tr|tekne|oyuk kap; hamur teknesi|EAT||
yayık|n|tr|yay-|çalkalamak|DLT|*yay|
küp|n|tr|küp|büyük toprak kap|DLT||
zembil|n|ar|zanbīl|hasır sepet|EAT||fa:zanbīl>ar:zanbīl>tr:zembil
hasırcı|n|ar|ḥaṣīr|hasır ören|OSM||
sacayak|n|tr|saç ayak|üç ayaklı ocak demiri|OSM||
kuzine|n|it|cucina|mutfak; mutfak sobası|OSM19||la:coquina>it:cucina>tr:kuzine
soba|n|hu|szoba|oda; ısıtılan oda|OSM||de:Stube>hu:szoba>tr:soba
tandır|n|ar|tannūr|toprak ocak|EAT||akk:tinūru>ar:tannūr>tr:tandır
kibrit|n|ar|kibrīt|kükürt|EAT||akk:kibrītu>ar:kibrīt>tr:kibrit
mandal|n|el|mándalos|sürgü, kapı kilidi|OSM||
süzgeç|n|tr|süz-|süzmek|OSM|*süz-|
süzgü|n|tr|süz-|süzmek|OSM|*süz-|
süzmek|v|tr|süz-|süzmek, arıtmak|DLT|*süz-|
dibek|n|tr|dibek|taş havan|OSM||
soku|n|tr|sok-|sokmak; taş dibek|OSM||
kıskaç|n|tr|kıs-|kısmak, sıkmak|OSM||
maşrapacı|n|ar|maşraba|maşrapa yapan|OSM||
çömlekçi|n|tr|çölmek|çömlek|OSM||
çömlekçilik|n|tr|çölmek|çömlek yapımı|MOD||
sırça|n|tr|sırıçga|cam|DLT||
billur|n|ar|billawr|kristal|EAT||grc:bḗryllos>ar:billawr>tr:billur
fağfur|n|fa|faġfūr|Çin imparatoru; Çin porseleni|EAT||
çinici|n|fa|çīnī|Çin işi|OSM||
çinicilik|n|fa|çīnī|çini yapımı|MOD||
mine|n|fa|mīnā|sırça; cam süs; emaye|EAT||
emaye|n|fr|émail|mine, sır|CUM||ger:smalt>fr:émail>tr:emaye
fırınlamak|v|el|foúrnos|fırın|MOD||
çıra|n|fa|çerāġ|kandil; çıra|DLT||
kav|n|tr|kav|tutuşturucu mantar|DLT||
gazyağı|n|fr|gaz|gaz|OSM19||
fitil|n|ar|fatīl|bükülmüş ip|EAT||
mumcu|n|fa|mūm|mum yapan|OSM||
sabuncu|n|ar|ṣābūn|sabun yapan|OSM||
sandıkçı|n|ar|ṣundūq|sandık yapan|OSM||
kutucu|n|el|koutí|kutu yapan|OSM||
bardakçı|n|tr|bardak|bardak yapan|OSM||
fincancı|n|ar|fincān|fincan satan|OSM||
kaşıkçı|n|tr|kaşuk|kaşık yapan|OSM||
bıçakçı|n|tr|bıçak|bıçak yapan|OSM||
kalburcu|n|ar|ġirbāl|kalbur yapan|OSM||
# --- İplik, dokuma, kumaş ---
hallaç|n|ar|ḥallāc|pamuk atıcı|EAT||
dokumacı|n|tr|toku-|dokumak|OSM|*doku-|
dokumacılık|n|tr|toku-|dokumacılık|MOD|*doku-|
dokuyucu|n|tr|toku-|dokumak|MOD|*doku-|
çulha|n|fa|cūlāh|dokumacı|EAT||
çul|n|ar|cull|at örtüsü; kaba kilim|EAT||
keçeci|n|tr|kéçe|keçe yapan|OSM||
kendir|n|tr|kendir|kenevir|DLT||
jüt|n|fr|jute|Hint keneviri|CUM||en:jute>fr:jute>tr:jüt
çile|n|fa|çille|kırk gün; iplik demeti|EAT||
yumak|n|tr|yum-|yummak, yuvarlamak|DLT|*yum-|
bobin|n|fr|bobine|makara|CUM||
kıl|n|tr|kıl|kıl|DLT||
kıtık|n|tr|kıtık|dolgu lifi|OSM||
koza|n|fa|ġōze|pamuk kozası|OSM||
kozacı|n|fa|ġōze|koza üreten|MOD||
ipekçi|n|tr|yipek|ipek üreten|OSM||
ipekçilik|n|tr|yipek|ipek üretimi|MOD||
iplikçi|n|tr|yip|ip yapan|OSM||
eğirmek|v|tr|egir-|eğirmek|DLT|*eğir-|
iğ|n|tr|ig|eğirme çubuğu|DLT|*eğir-|
büküm|n|tr|bük-|bükmek|OSM|*bük-|
bükülü|adj|tr|bük-|bükmek|OSM|*bük-|
çıkrık|n|tr|çıgrı|döner eğirme tezgâhı|DLT||
mekik|n|ar|makkūk|dokuma mekiği|EAT||
kirkit|n|tr|kirkit|halı tarağı|OSM||
nesic|n|ar|nasīc|dokunmuş; doku|OSM|N-S-C|
mensucat|n|ar|mansūcāt|dokunmuşlar|OSM19|N-S-C|
nessac|n|ar|nassāc|dokumacı|OSM|N-S-C|
kanaviçe|n|it|canovaccio|kaba kenevir bezi|OSM19|cannabis|la:cannabis>it:canovaccio>tr:kanaviçe
kanava|n|fr|canevas|kaba bez|CUM|cannabis|la:cannabis>fr:canevas>tr:kanava
etamin|n|fr|étamine|seyrek dokuma|CUM||la:stamen>fr:étamine>tr:etamin
organze|n|fr|organza|ince sert ipekli|CUM||
şifon|n|fr|chiffon|paçavra; ince ipekli|CUM|chiffe|
krep|n|fr|crêpe|kıvırcık dokuma|CUM||la:crispus>fr:crêpe>tr:krep
flanel|n|fr|flanelle|yumuşak yünlü|CUM||en:flannel>fr:flanelle>tr:flanel
pamuklu|adj|tr|pamuk|pamuk|OSM||
tafta|n|it|taffettà|parlak ipekli|OSM||fa:tāfte>it:taffettà>tr:tafta
muslin|n|fr|mousseline|Musul kumaşı|CUM||ar:Mawṣil>it:mussolina>fr:mousseline>tr:muslin
patiska|n|it|battista|ince pamuklu|OSM19||fr:batiste>it:battista>tr:patiska
basma|n|tr|bas-|basmak; baskılı pamuklu|OSM|*bas-|
yazma|n|tr|yaz-|yazmak; elle boyanmış örtü|OSM|*yaz-|
alaca|n|tr|ala|ala; çizgili kumaş|DLT||
çuha|n|fa|çūḫā|yünlü kumaş|EAT||
aba|n|ar|ʿabāʾ|yünden kaba kumaş; üstlük|EAT||
kebe|n|tr|kebe|kalın keçe|OSM||
kepenek|n|tr|kepenek|çoban keçesi|DLT||
yamçı|n|tr|yamçı|kıldan yağmurluk|OSM||
tiftik|n|tr|tiftik|keçi yünü|OSM||
tiftikçi|n|tr|tiftik|tiftik satan|OSM||
mohair|n|en|mohair|tiftik|MOD||ar:muḫayyar>it:mocaiarro>en:mohair>tr:mohair
angora|n|fr|angora|Ankara|CUM||tr:Ankara>fr:angora>tr:angora
merinos|n|fr|mérinos|merinos koyunu|CUM||es:merino>fr:mérinos>tr:merinos
polyester|n|fr|polyester|çok ester|MOD||
sentetik|adj|fr|synthétique|bireşimsel|MOD||grc:synthetikós>fr:synthétique>tr:sentetik
likra|n|en|Lycra|marka adı|MOD||
denim|n|en|denim|Nîmes kenti kumaşı|MOD||
tela|n|it|tela|bez; ara bez|OSM19||la:tela>it:tela>tr:tela
vatka|n|sl|vatka|pamuk dolgu|CUM||de:Watte>ru:vatka>tr:vatka
bürümcük|n|tr|bürün-|bürünmek|OSM||
kutnu|n|ar|quṭnī|pamuklu|OSM||
canfes|n|fa|cānfes|ince ipekli|OSM||
diba|n|fa|dībā|ipekli kumaş|EAT||
kemha|n|fa|kamḫā|sırmalı ipekli|EAT||
hare|n|fa|ḫāre|dalgalı kumaş|OSM||
kurdele|n|it|cordella|ipcik|OSM19|korda|la:chorda>it:cordella>tr:kurdele
sırma|n|el|sýrma|tel|OSM||
sim|n|fa|sīm|gümüş; gümüş tel|EAT||
payet|n|fr|paillette|küçük saman; pul|CUM||la:palea>fr:paillette>tr:payet
kaytan|n|ar|qayṭān|örme şerit|EAT||
sırmakeş|n|fa|sīm-keş|tel çeken|OSM||
kazaz|n|ar|qazzāz|ipek işleyen|OSM||
bezirgân|n|fa|bāzargān|tüccar|EAT||
çeyiz|n|ar|cihāz|donanım|EAT|C-H-Z|
cihaz|n|ar|cihāz|donanım, aygıt|OSM|C-H-Z|
teçhizat|n|ar|tachīzāt|donatım|OSM19|C-H-Z|
mücehhez|adj|ar|mucahhaz|donatılmış|OSM|C-H-Z|
# --- Dikiş, nakış, örgü ---
nakışçı|n|ar|naqş|nakış işleyen|OSM|N-K-Ş|
nakkaş|n|ar|naqqāş|süsleme ustası|EAT|N-K-Ş|
nakkaşlık|n|ar|naqqāş|nakkaş işi|OSM|N-K-Ş|
menkuş|adj|ar|manqūş|nakışlı|OSM|N-K-Ş|
gergef|n|fa|kār-gāh|iş yeri; nakış çerçevesi|EAT|-gāh|
kasnak|n|tr|kasnak|çember|OSM||
yüksük|n|tr|yüksük|parmak kılıfı|OSM||
tığ|n|tr|tıg|örgü iğnesi|DLT||
iğnelik|n|tr|yigne|iğne kabı|OSM||
çuvaldız|n|fa|cuvāl-dūz|çuval diken|EAT|dūz-|
terzilik|n|fa|darzī|terzi işi|OSM|dūz-|
ilmik|n|tr|il-|iliştirmek|OSM|*il-|
ilmek|n|tr|il-|iliştirmek|OSM|*il-|
ilik|n|tr|il-|düğme deliği|DLT|*il-|
iliklemek|v|tr|il-|düğmeyi iliğe geçirmek|OSM|*il-|
fiyonk|n|it|fiocco|kurdele düğümü|OSM19||
kıvrım|n|tr|kıvır-|kıvırmak|OSM||
pli|n|fr|pli|kıvrım|CUM||la:plicare>fr:pli>tr:pli
pile|n|fr|plissé|kırmalı|CUM||la:plicare>fr:plissé>tr:pile
kırma|n|tr|kır-|kırmak; kıvrım|OSM|*kır-|
büzgü|n|tr|büz-|büzmek|OSM||
dikişçi|n|tr|tik-|dikmek|OSM|*dik-|
dikim|n|tr|tik-|dikmek|MOD|*dik-|
biçki|n|tr|bıç-|biçmek|OSM|*biç-|
bıçkı|n|tr|bıç-|biçmek; büyük testere|DLT|*biç-|
örücü|n|tr|ör-|örmek|OSM|*ör-|
düğümlemek|v|tr|tüg-|düğüm|OSM|*tüg-|
düğmelemek|v|tr|tüg-|düğme|OSM|*tüg-|
sarmalamak|v|tr|sar-|sarmak|OSM|*sar-|
ütülemek|v|tr|üt-|ütmek, yakmak|OSM|*üt-|
ütücü|n|tr|üt-|ütü yapan|OSM|*üt-|
kola|n|el|kólla|tutkal|OSM|kolla|
kolalamak|v|el|kólla|tutkal|OSM|kolla|
çitilemek|v|tr|çit-|ovalamak|OSM||
yırtmak|v|tr|yırt-|yırtmak|DLT|*yırt-|
yırtmaç|n|tr|yırt-|yırtmak|OSM|*yırt-|
kırpmak|v|tr|kırp-|kırpmak|DLT||
kırkmak|v|tr|kırk-|kırkmak|DLT|*kırk-|
kırkım|n|tr|kırk-|kırkmak|OSM|*kırk-|
yolmak|v|tr|yul-|yolmak|DLT||
# --- Giyim-kuşam ---
giyecek|n|tr|ked-|giymek|OSM|*giy-|
giydirmek|v|tr|ked-|giymek|DLT|*giy-|
giyinik|adj|tr|ked-|giymek|MOD|*giy-|
kuşanmak|v|tr|kurşan-|kuşak bağlamak|DLT|*kuşa-|
kuşam|n|tr|kuşa-|kuşanma|OSM|*kuşa-|
takınmak|v|tr|tak-|takmak|DLT|*tak-|
süslenmek|v|tr|süs|süs|OSM||
don|n|tr|ton|giysi, elbise|ORH||
donatmak|v|tr|ton|giysi; donanım|DLT||
kıyafet|n|ar|qiyāfa|iz sürme; görünüş|OSM||
kisve|n|ar|kiswa|örtü, giysi|EAT|K-S-W|
kispet|n|ar|kiswa|giysi; güreşçi donu|OSM|K-S-W|
libas|n|ar|libās|giysi|EAT|L-B-S|
melbusat|n|ar|malbūsāt|giyilenler|OSM19|L-B-S|
urba|n|it|roba|eşya; giysi|OSM19||ger:rauba>it:roba>tr:urba
esvap|n|ar|aṯwāb|giysiler|EAT||
külot|n|fr|culotte|kısa pantolon|CUM||la:culus>fr:culotte>tr:külot
sutyen|n|fr|soutien-gorge|göğüs desteği|CUM||
korse|n|fr|corset|gövdeyi saran iç giysi|CUM||la:corpus>fr:corset>tr:korse
kombinezon|n|fr|combinaison|birleşim; iç giysi|CUM||
jüpon|n|fr|jupon|iç etek|CUM||ar:cubba>it:giubba>fr:jupon>tr:jüpon
kaşkol|n|fr|cache-col|boyun gizleyen|CUM||
papyon|n|fr|papillon|kelebek|CUM||la:papilio>fr:papillon>tr:papyon
boyunbağı|n|tr|boyun bağı|kravat|CUM|*bağ-|
manşet|n|fr|manchette|kol ağzı|CUM||la:manica>fr:manchette>tr:manşet
astar|n|fa|āstar|iç kumaş|EAT||
çıtçıt|n|tr|çıt|ses yansıması|MOD||
kayış|n|tr|kadış|deri şerit|DLT||
paçavra|n|fa|pāçe-pāre|parça bez|OSM||
eteklik|n|tr|etek|etek kumaşı|OSM||
gecelik|n|tr|kéçe|gece|OSM||
sabahlık|n|ar|ṣabāḥ|sabah giysisi|OSM19||
bornoz|n|ar|burnus|kukuletalı pelerin|OSM||ber:abernus>ar:burnus>tr:bornoz
önlük|n|tr|öŋ|ön|OSM|*ön|
kot|n|tr|Kot|soyadı; markadan|MOD||
süveter|n|en|sweater|terleten giysi|CUM||
triko|n|fr|tricot|örgü|CUM||
mont|n|en|Montgomery|mareşal adı; kısa palto|MOD||
parka|n|en|parka|kürklü ceket|MOD||ru:parka>en:parka>tr:parka
anorak|n|fr|anorak|kapüşonlu ceket|MOD||unk:anoraq>fr:anorak>tr:anorak
bluz|n|fr|blouse|gömlek|CUM||
tunik|n|fr|tunique|uzun gömlek|CUM||la:tunica>fr:tunique>tr:tunik
frak|n|fr|frac|kuyruklu ceket|OSM19||en:frock>fr:frac>tr:frak
smokin|n|fr|smoking|sigara ceketi|CUM||en:smoking jacket>fr:smoking>tr:smokin
redingot|n|fr|redingote|binici paltosu|OSM19||en:riding coat>fr:redingote>tr:redingot
trençkot|n|en|trench coat|siper paltosu|MOD||
pardösü|n|fr|pardessus|üstüne giyilen|CUM||
pelerin|n|fr|pèlerine|hacı pelerini|CUM||la:peregrinus>fr:pèlerine>tr:pelerin
atkı|n|tr|at-|atmak|OSM|*at-|
poşu|n|fa|pūşū|örtü|MOD||
fötr|n|fr|feutre|keçe|CUM||ger:filtir>fr:feutre>tr:fötr
melon|n|fr|melon|kavun; yuvarlak şapka|CUM||la:melo>fr:melon>tr:melon
silindir|n|fr|cylindre|yuvarlak gövde; silindir şapka|OSM19||grc:kýlindros>fr:cylindre>tr:silindir
serpuş|n|fa|ser-pūş|baş örtüsü|EAT||
kavuk|n|tr|kavuk|içi boş; kabarık başlık|DLT||
külah|n|fa|kulāh|başlık|EAT||
türban|n|fr|turban|sarık|CUM||fa:dulband>it:turbante>fr:turban>tr:türban
tülbent|n|fa|dulband|sarık bezi|EAT||
başörtü|n|tr|baş örtüsü|baş örtüsü|OSM||
duvak|n|tr|tugak|örtü|DLT||
peçe|n|it|pezza|bez parçası|OSM||
yaşmak|n|tr|yaşmak|örtü|EAT||
nikap|n|ar|niqāb|yüz örtüsü|EAT||
ferace|n|ar|faraciyya|geniş üst giysi|EAT||
entari|n|ar|ʿantarī|Antere'ye özgü giysi|OSM||
cübbe|n|ar|cubba|üst giysi|EAT||
mintan|n|fa|nīm-tan|yarım beden|OSM||
potur|n|tr|potur|kırmalı şalvar|OSM||
çakşır|n|tr|çakşır|dar pantolon|OSM||
fistan|n|el|foustáni|etek, entari|OSM||ar:Fusṭāṭ>it:fustagno>el:foustáni>tr:fistan
üstlük|n|tr|üst|üst giysi|OSM||
samur|n|fa|samūr|samur kürkü|EAT||
kakım|n|fa|qāqum|kakım (ermin) kürkü|OSM||
astragan|n|fr|astrakan|Astrahan kuzu kürkü|CUM||ru:Astrahan>fr:astrakan>tr:astragan
kukuleta|n|it|cucullo|başlık|OSM19||la:cucullus>it:cucullo>tr:kukuleta
yakalık|n|tr|yaka|yaka|OSM||
kolluk|n|tr|kol|kol|OSM||
pazubent|n|fa|bāzū-band|kol bağı|OSM||
dizlik|n|tr|tiz|diz|OSM||
göğüslük|n|tr|köküz|göğüs|OSM||
uçkur|n|tr|içkur|iç kuşak|DLT|*kur-|
yünlü|adj|tr|yuŋ|yün|OSM||
giyimli|adj|tr|ked-|giymek|OSM|*giy-|
# --- Ayakkabı, deri, koşum ---
mest|n|ar|masḥ|meshetme; mesh ayakkabısı|EAT|M-S-H|
mesaha|n|ar|misāḥa|yer ölçme|OSM|M-S-H|
iskarpin|n|it|scarpino|küçük ayakkabı|OSM19||
botin|n|fr|bottine|kısa çizme|CUM||
potin|n|fr|bottine|kısa çizme|OSM19||
şıpıdık|n|tr|şıp|ses yansıması|MOD||
tozluk|n|tr|toz|toz|OSM||
pençe|n|fa|panca|beş parmak; ayakkabı tabanı|EAT||
ökçe|n|tr|ökçe|topuk|DLT||
bağcık|n|tr|bağ|bağ|MOD|*bağ-|
gön|n|tr|kön|işlenmiş deri|DLT||
kösele|n|fa|gūsāle|dana; dana derisi|EAT||
sahtiyan|n|fa|saḫtiyān|keçi derisi|EAT||
meşin|n|fa|mīşīn|koyun derisi|EAT||
vaketa|n|it|vacchetta|dana derisi|OSM19||la:vacca>it:vacchetta>tr:vaketa
rugan|n|fa|rawġan|yağ; cila|OSM||
süet|n|fr|suède|İsveç|CUM||
nubuk|n|en|nubuck|yeni kadife|MOD||
debbağ|n|ar|dabbāġ|derici|EAT|D-B-Ğ|
debbağhane|n|ar|dabbāġ + fa. -ḫāne|derici işliği|OSM|D-B-Ğ|
dibagat|n|ar|dibāġa|deri işleme|OSM|D-B-Ğ|
tabaklamak|v|ar|dabbāġ|deri işlemek|OSM|D-B-Ğ|
tabakçı|n|ar|dabbāġ|derici|OSM|D-B-Ğ|
tabakhane|n|ar|dabbāġ + fa. -ḫāne|deri işleme yeri|OSM|-hāne|
çarıkçı|n|tr|çaruk|çarık yapan|OSM||
yemenici|n|ar|yamanī|yemeni yapan|OSM||
kavaf|n|ar|ḫaffāf|ayakkabıcı|OSM||
eskici|n|tr|eski|eski eşya alan|OSM||
kunduracılık|n|el|koundoúra|kundura yapımı|MOD||
ayakkabıcı|n|tr|adak kap|ayakkabı yapan|CUM||
nalça|n|ar|naʿl|nal|OSM||
eyer|n|tr|eder|at oturağı|DLT||
palan|n|fa|pālān|yük semeri|EAT||
semer|n|el|samári|yük eyeri|EAT||grc:ságma>el:samári>tr:semer
semerci|n|el|samári|semer yapan|OSM||
semercilik|n|el|samári|semercilik|MOD||
üzengi|n|tr|üzeŋgü|üzengi|DLT||
dizgin|n|tr|tizgin|dizgin|DLT|*diz-|
yular|n|tr|yular|yular|DLT||
kolan|n|tr|kolan|eyer kayışı|DLT||
mıh|n|fa|mīḫ|çivi|EAT||
mıhlamak|v|fa|mīḫ|çivilemek|OSM||
koşum|n|tr|koş-|koşmak, bağlamak|OSM|*koş-|
saraç|n|ar|sarrāc|koşum yapan|EAT|S-R-C|
saraçlık|n|ar|sarrāc|saraç işi|OSM|S-R-C|
saraçhane|n|ar|sarrāc + fa. -ḫāne|saraç çarşısı|OSM|S-R-C|
# --- Aletler, zanaat, metal ---
alet|n|ar|āla|araç|EAT||
edevat|n|ar|adawāt|araçlar|OSM||
avadanlık|n|fa|āvandān|kap; takım|OSM||
balyoz|n|el|variós|ağır çekiç|OSM||
örs|n|tr|örs|demirci kütüğü|DLT||
körük|n|tr|körük|hava üfleyici|DLT||
mengene|n|el|mángano|sıkıştırma aleti|OSM||grc:mánganon>el:mángano>tr:mengene
kelepçe|n|fa|kalab-çe|küçük kıskaç|OSM||
kerpeten|n|ar|kalbatān|iki köpek; kıskaç|EAT||
kargaburun|n|tr|karga burun|karga burnu|OSM||
pim|n|en|pin|iğne|MOD||
perçin|n|fa|parçīn|çivi başı ezme|OSM||
perçinlemek|v|fa|parçīn|perçin|OSM||
kama|n|tr|kama|takoz; kısa kılıç|DLT||
takoz|n|el|tákos|kama|OSM||
mil|n|ar|mīl|çubuk; eksen|EAT||
mihver|n|ar|miḥwar|eksen|OSM||
çark|n|fa|çarḫ|tekerlek|EAT||
dişli|n|tr|tiş|diş|MOD||
makara|n|ar|bakara|makara|EAT||
palanga|n|it|palanca|makaralı kaldıraç|OSM||grc:phálanx>la:palanga>it:palanca>tr:palanga
kriko|n|it|cricco|kaldırma aleti|CUM||
vinç|n|en|winch|kaldırma makinesi|CUM||
levye|n|fr|levier|kaldıraç|CUM||la:levare>fr:levier>tr:levye
kaldıraç|n|tr|kaldır-|kaldırmak|DD|*kalk-|
kazık|n|tr|kazguk|kazık|DLT|*kaz-|
yonga|n|tr|yon-|yontmak|DLT||
talaş|n|fa|tarāşe|yontma kırıntısı|OSM|tarāş|
tıraş|n|fa|tarāş|yontma, kesme|EAT|tarāş|
delgi|n|tr|tel-|delmek|DD|*del-|
delgeç|n|tr|tel-|delmek|DD|*del-|
burgu|n|tr|bur-|burmak|DLT|*bur-|
burmak|v|tr|bur-|bükmek, çevirmek|DLT|*bur-|
burma|n|tr|bur-|burulmuş; burma bilezik|OSM|*bur-|
eğe|n|tr|egek|törpü|DLT|*eğe-|
eğelemek|v|tr|egek|eğe|OSM|*eğe-|
iskarpela|n|it|scalpello|keski|OSM19||la:scalprum>it:scalpello>tr:iskarpela
raptiye|n|ar|rabṭiyya|bağlayıcı|CUM|R-B-T|
rapt|n|ar|rabṭ|bağlama|OSM|R-B-T|
merbut|adj|ar|marbūṭ|bağlı|OSM|R-B-T|
ataş|n|fr|attache|bağ|CUM||
rulo|n|fr|rouleau|tomar|CUM||la:rotula>fr:rouleau>tr:rulo
mala|n|fa|māle|sıvacı aleti|EAT||
mastar|n|ar|misṭar|satır çizme cetveli|OSM||
şakul|n|ar|şāqūl|çekül|OSM||
çekül|n|tr|çek-|çekmek|DD|*çek-|
terazi|n|fa|tarāzū|tartı|EAT||
gönye|n|el|gonía|açı|OSM||grc:gōnía>el:gonía>tr:gönye
mezura|n|fr|mesure|ölçü|CUM||la:mensura>fr:mesure>tr:mezura
spatula|n|it|spatola|kürekçik|MOD||la:spathula>it:spatola>tr:spatula
zımpara|n|fa|sunbāde|aşındırıcı|OSM||
zımparalamak|v|fa|sunbāde|zımpara|OSM||
bilemek|v|tr|bile-|bilemek|DLT|*bile-|
bileği|n|tr|bile-|bileme taşı|DLT|*bile-|
bileme|n|tr|bile-|bilemek|OSM|*bile-|
bileyici|n|tr|bile-|bileyen|OSM|*bile-|
torna|n|it|torno|döndürerek işleme|OSM19|tornare|la:tornare>it:torno>tr:torna
tornacı|n|it|torno|torna ustası|CUM|tornare|
tornacılık|n|it|torno|tornacılık|MOD|tornare|
tornalamak|v|it|torno|torna|MOD|tornare|
tesviye|n|ar|taswiya|düzleme|OSM|S-W-Y|
tesviyeci|n|ar|taswiya|metal düzleyen|CUM|S-W-Y|
tesviyecilik|n|ar|taswiya|tesviyecilik|MOD|S-W-Y|
freze|n|fr|fraise|çilek; frezeleme|MOD||
pres|n|fr|presse|baskı|CUM||la:pressare>fr:presse>tr:pres
döküm|n|tr|tök-|dökmek|OSM|*dök-|
dökümcü|n|tr|tök-|dökmek|OSM|*dök-|
dökümcülük|n|tr|tök-|dökmek|MOD|*dök-|
dökümhane|n|tr|tök- + fa. -ḫāne|dökme yeri|OSM19|-hāne|
demirhane|n|tr|temir + fa. -ḫāne|demir işliği|OSM|-hāne|
demircilik|n|tr|temir|demir|MOD||
bakırcı|n|tr|bakır|bakır işleyen|OSM||
bakırcılık|n|tr|bakır|bakır işi|MOD||
tenekeci|n|it|tenecca|teneke işleyen|OSM19||
tenekecilik|n|it|tenecca|tenekecilik|MOD||
lehim|n|ar|liḥām|kaynak|OSM|L-Ḥ-M|
lehimci|n|ar|liḥām|lehim yapan|OSM19|L-Ḥ-M|
lehimlemek|v|ar|liḥām|lehim|OSM|L-Ḥ-M|
kaynakçı|n|tr|kayna-|kaynamak|MOD|*kayna-|
kaynakçılık|n|tr|kayna-|kaynakçılık|MOD|*kayna-|
nikel|n|fr|nickel|cin bakırı|CUM||de:Kupfernickel>fr:nickel>tr:nikel
platin|n|fr|platine|gümüşçük|OSM19||es:platina>fr:platine>tr:platin
bronz|n|fr|bronze|tunç|CUM||it:bronzo>fr:bronze>tr:bronz
yaldız|n|tr|yal-|parlamak|OSM|*yal-|
yaldızlamak|v|tr|yal-|parlamak|OSM|*yal-|
kaplama|n|tr|kapla-|kaplamak|OSM|*kap-|
döven|n|tr|tög-|dövmek|DLT|*döv-|
dövme|n|tr|tög-|dövmek|OSM|*döv-|
oyma|n|tr|oy-|oymak|OSM|*oy-|
oymacı|n|tr|oy-|oymak|OSM|*oy-|
oymacılık|n|tr|oy-|oymak|MOD|*oy-|
kakmak|v|tr|kak-|vurmak, çakmak|DLT|*kak-|
kakma|n|tr|kak-|kakmak|OSM|*kak-|
kakmacı|n|tr|kak-|kakma yapan|OSM|*kak-|
kabartma|n|tr|kabar-|kabarmak|OSM|*kabar-|
kabartmak|v|tr|kabar-|kabarmak|OSM|*kabar-|
kabarık|adj|tr|kabar-|kabarmak|OSM|*kabar-|
kalemkâr|n|ar|qalam + fa. -kār|kalem işçisi|OSM|-kār|
müzehhip|n|ar|muḏahhib|yaldızlayan|OSM||
ciltçi|n|ar|cild|cilt yapan|OSM|C-L-D|
ciltçilik|n|ar|cild|ciltçilik|MOD|C-L-D|
mücellit|n|ar|mucallid|cilt yapan|OSM|C-L-D|
mücellitlik|n|ar|mucallid|mücellit işi|OSM|C-L-D|
doğramacı|n|tr|toğra-|doğramak|OSM|*doğra-|
doğramacılık|n|tr|toğra-|doğrama işi|MOD|*doğra-|
sıvacı|n|tr|sıva-|sıvamak|OSM||
sıvacılık|n|tr|sıva-|sıvacılık|MOD||
boyacılık|n|tr|boya|boya|MOD||
boyahane|n|tr|boya + fa. -ḫāne|boya yeri|OSM|-hāne|
camcı|n|fa|cām|cam|OSM||
camcılık|n|fa|cām|cam|MOD||
marangozluk|n|el|marangós|marangoz|MOD||
dülgerlik|n|fa|durūdgar|dülger|OSM||
cila|n|ar|cilāʾ|parlatma|OSM|C-L-W|
cilalamak|v|ar|cilāʾ|cila|OSM|C-L-W|
cilacı|n|ar|cilāʾ|cila yapan|OSM19|C-L-W|
mücella|adj|ar|mucallā|parlatılmış|OSM|C-L-W|
vernik|n|it|vernice|cila|OSM19||grc:berenikē>la:vernix>it:vernice>tr:vernik
zamk|n|ar|ṣamġ|ağaç sakızı|EAT||
kalıplamak|v|ar|qālab|kalıp|OSM||
vidalamak|v|it|vite|vida|MOD||
çivilemek|v|tr|çıbı|çivi|OSM||
rendelemek|v|fa|rande|rende|OSM||
törpülemek|v|tr|törpü|törpü|OSM||
tutkallamak|v|tr|tutkal|tutkal|OSM|*tut-|
yapıştırmak|v|tr|yap-|yapmak|DLT|*yap-|
yapıştırıcı|n|tr|yap-|yapmak|MOD|*yap-|
badanalamak|v|ar|badana|badana|OSM||
ustalık|n|fa|ustād|usta|OSM||
kalfalık|n|ar|ḫalīfa|kalfa|OSM||
çıraklık|n|fa|çarāġ|çıra; çırak|OSM||
lonca|n|it|loggia|kemerli yer; esnaf birliği|OSM||ger:laubja>it:loggia>tr:lonca
zanaatçı|n|ar|ṣanʿa|zanaat|MOD|S-N-A|
kuyum|n|tr|kuy-|dökmek|OSM|*kuy-|
kuyumculuk|n|tr|kuy-|dökmek|MOD|*kuy-|
sarraflık|n|ar|ṣarrāf|sarraf işi|OSM|S-R-F|
telkâri|n|fa|tel-kārī|tel işi|OSM|-kār|
savat|n|ar|sawād|karalık; gümüş işleme|OSM||
hakkâk|n|ar|ḥakkāk|kazıyıcı|OSM||
hakketmek|v|ar|ḥakk|kazımak|OSM||
hakkâklık|n|ar|ḥakkāk|hakkâk işi|OSM||
mihenk|n|ar|miḥakk|denek taşı|OSM||
# --- Mücevher, süs ---
mücevher|n|ar|mucawhar|cevherli|OSM|C-W-H-R|
mücevherat|n|ar|mucawharāt|mücevherler|OSM|C-W-H-R|
mücevherci|n|ar|mucawhar|mücevher satan|OSM19|C-W-H-R|
cevahir|n|ar|cawāhir|cevherler|EAT|C-W-H-R|
cevher|n|ar|cawhar|öz; değerli taş|EAT|C-W-H-R|fa:gawhar>ar:cawhar>tr:cevher
ziynet|n|ar|zīna|süs|EAT|Z-Y-N|
tezyin|n|ar|tazyīn|süsleme|OSM|Z-Y-N|
tezyinat|n|ar|tazyīnāt|süslemeler|OSM|Z-Y-N|
müzeyyen|adj|ar|muzayyan|süslenmiş|OSM|Z-Y-N|
bezeme|n|tr|beze-|süslemek|OSM||
akik|n|ar|ʿaqīq|akik taşı|EAT||
firuze|n|fa|fīrūze|turkuaz|EAT||
zümrüt|n|ar|zumurrud|yeşil değerli taş|EAT||grc:smáragdos>ar:zumurrud>tr:zümrüt
yakut|n|ar|yāqūt|kırmızı değerli taş|EAT||grc:hyákinthos>ar:yāqūt>tr:yakut
elmas|n|ar|almās|elmas|EAT||grc:adámas>ar:almās>tr:elmas
pırlanta|n|it|brillante|parlayan|OSM19||
safir|n|fr|saphir|mavi değerli taş|OSM19||grc:sáppheiros>la:sapphirus>fr:saphir>tr:safir
topaz|n|fr|topaze|topaz|CUM||grc:tópazos>fr:topaze>tr:topaz
opal|n|fr|opale|opal|CUM||sa:upala>la:opalus>fr:opale>tr:opal
sedef|n|ar|ṣadaf|deniz kabuğu|EAT||
lal|n|fa|laʿl|kırmızı değerli taş|EAT||
alyans|n|fr|alliance|birlik; nişan yüzüğü|CUM||la:alligare>fr:alliance>tr:alyans
hızma|n|ar|ḫizām|burun halkası|OSM||
halhal|n|ar|ḫalḫāl|ayak bileziği|EAT||
bileklik|n|tr|bilek|bilek|OSM||
madalyon|n|fr|médaillon|büyük madalya|OSM19||it:medaglione>fr:médaillon>tr:madalyon
madalya|n|it|medaglia|madalya|OSM19||la:metallum>it:medaglia>tr:madalya
pandantif|n|fr|pendentif|sarkan|CUM|pendere|
diadem|n|fr|diadème|taç|CUM||grc:diádēma>fr:diadème>tr:diadem
tepelik|n|tr|töpü|tepe|OSM||
hatem|n|ar|ḫātam|mühür yüzüğü|EAT|H-T-M|
hitam|n|ar|ḫitām|son, bitiş|OSM|H-T-M|
kaşe|n|fr|cachet|mühür|CUM||la:coactare>fr:cachet>tr:kaşe
nazarlık|n|ar|naẓar|bakış|OSM|N-Z-R|
kırat|n|ar|qīrāṭ|keçiboynuzu çekirdeği; ağırlık birimi|EAT||grc:kerátion>ar:qīrāṭ>tr:kırat
karat|n|fr|carat|ağırlık birimi|CUM||grc:kerátion>ar:qīrāṭ>it:carato>fr:carat>tr:karat
# --- Bakım, süslenme, hamam ---
allık|n|tr|al|kırmızı|OSM||
rastık|n|fa|rāsuḫt|kaş boyası|OSM||
rimel|n|fr|Rimmel|markadan|MOD||
esans|n|fr|essence|öz|CUM||la:essentia>fr:essence>tr:esans
koku|n|tr|kok-|kokmak|DLT||
ıtır|n|ar|ʿiṭr|güzel koku|EAT|A-T-R|
ıtriyat|n|ar|ʿiṭriyyāt|kokular|OSM19|A-T-R|
pomat|n|fr|pommade|elma merhemi|CUM||la:pomum>fr:pommade>tr:pomat
briyantin|n|fr|brillantine|parlatıcı|CUM||
ustura|n|fa|ustura|tıraş bıçağı|EAT||
berberlik|n|it|barbiere|berber|OSM||
bıyık|n|tr|bıdık|bıyık|DLT||
perçem|n|fa|parçam|kâkül|EAT||
kâkül|n|fa|kākul|alın saçı|EAT||
zülüf|n|fa|zulf|şakak saçı|EAT||
topuz|n|tr|topuz|yuvarlak baş; saç topuzu|DLT|*top-|
firkete|n|it|forchetta|çatalcık|OSM19||la:furca>it:forchetta>tr:firkete
kurna|n|el|krounós|musluk, çeşme|OSM||
tellak|n|ar|dallāk|ovucu|OSM|D-L-K|
tellaklık|n|ar|dallāk|tellak işi|OSM|D-L-K|
natır|n|ar|nāṭūr|bekçi; kadınlar hamamı görevlisi|OSM||
peştemal|n|fa|puşt-māl|sırt silen|EAT||
lif|n|ar|līf|hurma lifi|OSM||
külhan|n|fa|kulḫan|hamam ocağı|OSM||
külhancı|n|fa|kulḫan|külhan yakan|OSM||
hamamcılık|n|ar|ḥammām|hamam işletme|MOD|H-M-M|
sauna|n|unk|sauna|Fin hamamı|MOD||
küvet|n|fr|cuvette|küçük kap|CUM||la:cupa>fr:cuvette>tr:küvet
musluk|n|ar|maslak|akıtma yolu|OSM||
sifon|n|fr|siphon|boru|CUM||grc:síphōn>fr:siphon>tr:sifon
kenef|n|ar|kanīf|gizlenmiş yer|OSM||
# --- Müzik: çalgılar ---
cura|n|tr?|cura|küçük bağlama|OSM||
rebap|n|ar|rabāb|yaylı çalgı|EAT||
santur|n|fa|santūr|telli vurmalı çalgı|OSM||grc:psaltḗrion>fa:santūr>tr:santur
kopuz|n|tr|kopuz|telli çalgı|DLT||
çöğür|n|tr|çöğür|büyük saz|OSM||
sipsi|n|tr|sip|ses yansıması|OSM||
çığırtma|n|tr|çığır-|bağırmak|OSM||
gayda|n|sl|gayda|tulum çalgısı|OSM19||
bendir|n|ar|bandīr|büyük def|OSM||
çalpara|n|fa|çahār-pāre|dört parça|OSM||
nakkare|n|ar|naqqāra|küçük kös|EAT||
kös|n|fa|kūs|büyük davul|EAT||
trombon|n|it|trombone|büyük boru|CUM||
tuba|n|la|tuba|boru|CUM||
korno|n|it|corno|boynuz|CUM||la:cornu>it:corno>tr:korno
obua|n|fr|hautbois|yüksek sesli odun|CUM||
fagot|n|it|fagotto|demet|CUM||
viyola|n|it|viola|viyola|CUM||
viyolonsel|n|fr|violoncelle|küçük viyolon|CUM||it:violoncello>fr:violoncelle>tr:viyolonsel
çello|n|it|cello|viyolonsel|MOD||
kontrbas|n|fr|contrebasse|karşı bas|CUM||it:contrabbasso>fr:contrebasse>tr:kontrbas
arp|n|fr|harpe|arp|CUM||ger:harpa>fr:harpe>tr:arp
org|n|fr|orgue|org|CUM||grc:órganon>la:organum>fr:orgue>tr:org
armonika|n|it|armonica|uyumlu|CUM||grc:harmonikós>it:armonica>tr:armonika
mızıka|n|it|musica|müzik|OSM19||grc:mousikḗ>it:musica>tr:mızıka
mandolin|n|it|mandolino|küçük mandola|OSM19||
cümbüş|n|fa|cunbiş|hareket, eğlence|OSM||
mızrap|n|ar|miḍrāb|vurma aleti|EAT||
akort|n|fr|accord|uyum|CUM||la:accordare>fr:accord>tr:akort
telli|adj|tr|tel|tel|OSM||
nefesli|adj|ar|nafas|nefes|MOD|N-F-S|
vurmalı|adj|tr|vur-|vurmak|MOD||
çalgıcı|n|tr|çal-|çalmak|OSM|*çal-|
kemancı|n|fa|kamān|yay|OSM||
kemençeci|n|fa|kamānçe|kemençe|OSM||
udi|n|ar|ʿūdī|ud çalan|OSM||
tamburi|n|fa|ṭanbūrī|tambur çalan|OSM||
zurnacı|n|fa|sūrnā|zurna|OSM||
davulcu|n|ar|ṭabl|davul|OSM|T-B-L|
darbukacı|n|ar|darbukka|darbuka|MOD||
kavalcı|n|tr|kaval|kaval|OSM||
bağlamacı|n|tr|bağla-|bağlamak|MOD|*bağ-|
# --- Müzik: türler, kavramlar ---
tını|n|tr|tın-|ses vermek|OSM|*tın-|
tınlamak|v|tr|tın-|ses vermek|DLT|*tın-|
tıngırdatmak|v|tr|tıngır|ses yansıması|OSM|*tın-|
çınlamak|v|tr|çıŋ|ses yansıması|DLT|*çın-|
çınlama|n|tr|çıŋ|ses yansıması|OSM|*çın-|
ıslık|n|tr|ıs|ses yansıması|OSM||
mırıldanmak|v|tr|mırıl|ses yansıması|OSM||
koşma|n|tr|koş-|koşmak, eklemek|OSM|*koş-|
semai|n|ar|samāʿī|işitmeyle ilgili|OSM||
varsağı|n|tr|Varsak|Varsak boyu|OSM||
bozlak|n|tr|boz|boz; bozlamak|OSM||
ninni|n|tr|nenni|ses yansıması|OSM||
mani|n|ar|maʿnā|anlam|OSM|A-N-Y|
hoyrat|n|el|khoriátis|köylü|OSM||
muganni|n|ar|muġannī|şarkıcı|OSM|Ğ-N-Y|
teganni|n|ar|taġannī|şarkı söyleme|OSM|Ğ-N-Y|
gazelhan|n|ar|ġazal + fa. -ḫān|gazel okuyan|OSM||
türkücü|n|tr|Türk|Türk|MOD||
ağıtçı|n|tr|ağıt|ağıt|OSM||
destancı|n|fa|dāstān|destan|OSM||
besteci|n|fa|baste|bağlanmış|CUM||
bestelemek|v|fa|baste|beste|CUM||
müzisyen|n|fr|musicien|müzikçi|CUM||
solo|n|it|solo|tek|CUM||la:solus>it:solo>tr:solo
düet|n|it|duetto|ikili|CUM||
operet|n|fr|opérette|küçük opera|OSM19||it:operetta>fr:opérette>tr:operet
sonat|n|it|sonata|çalınan|CUM|sonus|la:sonare>it:sonata>tr:sonat
konçerto|n|it|concerto|uyum|CUM||
tempo|n|it|tempo|zaman|CUM||la:tempus>it:tempo>tr:tempo
oktav|n|fr|octave|sekizinci|CUM||la:octavus>fr:octave>tr:oktav
ton|n|fr|ton|ses; gerilim|CUM||grc:tónos>la:tonus>fr:ton>tr:ton
repertuvar|n|fr|répertoire|dizin|CUM||la:repertorium>fr:répertoire>tr:repertuvar
prova|n|it|prova|deneme|OSM19||la:proba>it:prova>tr:prova
kulis|n|fr|coulisse|kayan|CUM||
fasıl|n|ar|faṣl|bölüm|EAT|F-S-L|
fasıla|n|ar|fāṣila|ara|OSM|F-S-L|
mufassal|adj|ar|mufaṣṣal|ayrıntılı|OSM|F-S-L|
peşrev|n|fa|pīş-rev|önde giden|OSM||
sanatçı|n|ar|ṣanʿa|sanat|CUM|S-N-A|
icracı|n|ar|icrāʾ|yürütme|MOD|C-R-Y|
# --- Dans, eğlence, seyirlik ---
zeybek|n|tr|zeybek|Ege efesi; oyun|OSM||
halay|n|unk|halay|halka oyunu|OSM||
horon|n|el|chorós|dans|OSM|khoros|
koreografi|n|fr|chorégraphie|dans yazımı|MOD|khoros|grc:choreía>fr:chorégraphie>tr:koreografi
koreograf|n|fr|chorégraphe|dans düzenleyen|MOD|khoros|
çiftetelli|n|tr|çift telli|iki telli|OSM|cuft|
karşılama|n|tr|karşı|karşı|OSM||
köçek|n|fa|kūçak|küçük|OSM||
çengi|n|fa|çang|çeng çalgısı|OSM||
rakkas|n|ar|raqqāṣ|dansçı; sarkaç|OSM|R-K-S|
raksetmek|v|ar|raqṣ|dans etmek|OSM|R-K-S|
dans|n|fr|danse|dans|OSM19||
vals|n|fr|valse|vals|OSM19||de:Walzer>fr:valse>tr:vals
tango|n|es|tango|tango|CUM||
polka|n|fr|polka|Leh kadını|OSM19||pl:polka>fr:polka>tr:polka
balerin|n|fr|ballerine|bale dansçısı|CUM|ballare|it:ballerina>fr:ballerine>tr:balerin
balo|n|it|ballo|dans eğlencesi|OSM19|ballare|
oynak|adj|tr|oyna-|oynamak|OSM|*oyna-|
oynaş|n|tr|oyna-|oynamak|DLT|*oyna-|
oynatmak|v|tr|oyna-|oynamak|DLT|*oyna-|
oyunculuk|n|tr|oyna-|oyuncu işi|MOD|*oyna-|
oyuncakçı|n|tr|oyna-|oyuncak satan|OSM|*oyna-|
ortaoyunu|n|tr|orta oyunu|meydan oyunu|OSM|*oyna-|
kukla|n|el|koúkla|bebek|OSM||la:cuculla>el:koúkla>tr:kukla
kuklacı|n|el|koúkla|kukla oynatan|OSM||
karagöz|n|tr|kara göz|kara göz|OSM||
hacivat|n|ar|Ḥācī ʿİvāẓ|Hacı İvaz|OSM||
meddah|n|ar|maddāḥ|övücü|EAT|M-D-H|
medih|n|ar|madḥ|övgü|EAT|M-D-H|
methiye|n|ar|madḥiyya|övgü şiiri|OSM|M-D-H|
akrobat|n|fr|acrobate|uçta yürüyen|CUM|akros|grc:akrobátēs>fr:acrobate>tr:akrobat
akrobasi|n|fr|acrobatie|akrobatlık|CUM|akros|
lunapark|n|it|luna park|ay parkı|CUM||
atlıkarınca|n|tr|atlı karınca|atlı karınca|OSM||
trapez|n|fr|trapèze|yamuk; salıncak|CUM||grc:trapézion>fr:trapèze>tr:trapez
# --- Oyunlar ---
bezik|n|fr|bésigue|bezik|OSM19||
briç|n|en|bridge|köprü|CUM||
poker|n|en|poker|poker|CUM||
pişti|n|tr|piş-|pişmek|MOD||
tombala|n|it|tombola|tombala|CUM||
loto|n|fr|loto|loto|CUM||it:lotto>fr:loto>tr:loto
bilye|n|it|biglia|bilye|OSM19||
misket|n|fr|mousquet|tüfek; tüfek saçması|OSM19||it:moschetto>fr:mousquet>tr:misket
aşık|n|tr|aşuk|aşık kemiği|DLT||
seksek|n|tr|sek-|sekmek|MOD|*sek-|
sektirmek|v|tr|sek-|sekmek|OSM|*sek-|
körebe|n|tr|kör ebe|kör ebe|OSM||
saklambaç|n|tr|sakla-|saklamak|OSM||
yakantop|n|tr|yakan top|yakan top|MOD||
birdirbir|n|tr|bir dir bir|bir|OSM||
topaç|n|tr|top|yuvarlak|OSM|*top-|
zıpzıp|n|tr|zıp|ses yansıması|MOD||
kaydırak|n|tr|kay-|kaymak|OSM|*kay-|
fırıldak|n|tr|fırıl|ses yansıması|OSM||
sapan|n|tr|sapan|taş atma aleti|DLT||
bulmaca|n|tr|bul-|bulmak|MOD|*bul-|
tekerleme|n|tr|teker|tekerlemek|OSM||
yanıltmaç|n|tr|yaŋıl-|yanılmak|MOD||
mola|n|it|molla|gevşetme|OSM||
sayışmaca|n|tr|say-|saymak|MOD|*say-|
kumarhane|n|ar|qimār + fa. -ḫāne|kumar yeri|OSM|-hāne|
bahis|n|ar|baḥṯ|araştırma; iddia|OSM|B-H-S|
mebhas|n|ar|mabḥaṯ|araştırma konusu|OSM|B-H-S|
satranççı|n|fa|şaṭranc|satranç|MOD||
# --- Spor ---
binicilik|n|tr|bin-|binmek|MOD|*bin-|
yüzme|n|tr|yüz-|yüzmek|OSM|*yüz-|
yüzmek|v|tr|yüz-|suda yüzmek|DLT|*yüz-|
yüzücü|n|tr|yüz-|yüzmek|MOD|*yüz-|
yüzücülük|n|tr|yüz-|yüzücülük|MOD|*yüz-|
dalmak|v|tr|tal-|dalmak|DLT|*dal-|
dalgıç|n|tr|tal-|dalmak|OSM|*dal-|
dalış|n|tr|tal-|dalmak|MOD|*dal-|
atlama|n|tr|atla-|atlamak|OSM|*at-|
halter|n|fr|haltère|ağırlık|CUM||grc:haltḗres>fr:haltère>tr:halter
halterci|n|fr|haltère|halter kaldıran|MOD||
eskrim|n|fr|escrime|kılıç oyunu|CUM||ger:skirmjan>it:scrima>fr:escrime>tr:eskrim
eskrimci|n|fr|escrime|eskrim yapan|MOD||
atletizm|n|fr|athlétisme|atletlik|CUM|athlon|grc:âthlon>fr:athlétisme>tr:atletizm
dekatlon|n|fr|décathlon|on yarışma|MOD|athlon|
triatlon|n|fr|triathlon|üç yarışma|NEW|athlon|
maraton|n|fr|marathon|Marathon ovası|CUM|Marathōn|grc:Marathṓn>fr:marathon>tr:maraton
maratoncu|n|fr|marathon|maraton koşucusu|MOD|Marathōn|
maç|n|en|match|karşılaşma|CUM||
idman|n|ar|idmān|alışma, düşkünlük|OSM||
rekor|n|fr|record|kayıt|CUM|recordari|en:record>fr:record>tr:rekor
rekortmen|n|fr|recordman|rekor kıran|CUM|recordari|
sporcu|n|fr|sport|spor|CUM||
amatör|n|fr|amateur|seven|CUM||la:amator>fr:amateur>tr:amatör
profesyonel|n|fr|professionnel|meslekî|CUM||la:professio>fr:professionnel>tr:profesyonel
pinpon|n|en|ping-pong|ses yansıması|CUM||
badminton|n|en|Badminton|köşk adı|MOD||
hokey|n|en|hockey|hokey|CUM||
ragbi|n|en|rugby|Rugby okulu|MOD||
beyzbol|n|en|baseball|kale topu|MOD||
boksör|n|fr|boxeur|boks yapan|CUM||en:boxer>fr:boxeur>tr:boksör
boksörlük|n|fr|boxeur|boksörlük|MOD||
karate|n|ja|karate|boş el|MOD||
judo|n|ja|jūdō|yumuşak yol|MOD||
kayakçı|n|tr|kay-|kaymak|MOD|*kay-|
kayakçılık|n|tr|kay-|kayakçılık|MOD|*kay-|
kızak|n|tr|kızak|kayan taşıt|OSM||
paten|n|fr|patin|kayma ayakkabısı|CUM||
bisikletçi|n|fr|bicyclette|bisiklet|CUM||
motosiklet|n|fr|motocyclette|motorlu bisiklet|CUM||
ralli|n|en|rally|toplanma|MOD||
uçurtmacı|n|tr|uç-|uçurtma|MOD|*uç-|
okçu|n|tr|ok|ok|DLT||
jokey|n|en|jockey|binici|CUM||
yarışma|n|tr|yarış-|yarışmak|MOD||
müsabaka|n|ar|musābaqa|yarışma|OSM|S-B-K|
müsabık|n|ar|musābiq|yarışmacı|OSM|S-B-K|
turnuva|n|fr|tournoi|döndürme yarışı|CUM|tornare|la:tornare>fr:tournoi>tr:turnuva
şampiyona|n|fr|championnat|şampiyonluk|CUM|campus|la:campus>fr:championnat>tr:şampiyona
şampiyonluk|n|fr|champion|şampiyon|MOD|campus|
puan|n|fr|point|nokta|CUM||la:punctum>fr:point>tr:puan
saha|n|ar|sāḥa|alan, meydan|OSM||
stat|n|fr|stade|stadyum|CUM||grc:stádion>fr:stade>tr:stat
pist|n|fr|piste|iz|CUM||it:pista>fr:piste>tr:pist
kort|n|en|court|avlu|CUM||la:cohors>fr:court>en:court>tr:kort
ring|n|en|ring|halka|CUM||
galip|adj|ar|ġālib|üstün gelen|EAT|Ğ-L-B|
mağlup|adj|ar|maġlūb|yenilmiş|EAT|Ğ-L-B|
galebe|n|ar|ġalaba|üstün gelme|EAT|Ğ-L-B|
galibiyet|n|ar|ġālibiyya|üstünlük|OSM|Ğ-L-B|
mağlubiyet|n|ar|maġlūbiyya|yenilgi|OSM|Ğ-L-B|
berabere|adv|fa|barābar|eşit|OSM||
beraberlik|n|fa|barābar|eşitlik|OSM||
tekme|n|tr|tep-|tepmek|OSM|*tep-|
tekmelemek|v|tr|tep-|tepmek|OSM|*tep-|
tepmek|v|tr|tep-|tepmek|DLT|*tep-|
yumruklamak|v|tr|yum-|yummak|OSM|*yum-|
kapışmak|v|tr|kap-|kapmak|DLT|*kap-|
kapışma|n|tr|kap-|kapmak|OSM|*kap-|
güreşçi|n|tr|küreş-|güreşmek|OSM|*küreş-|
pehlivanlık|n|fa|pahlavān|pehlivan|OSM||
başpehlivan|n|fa|baş + pahlavān|baş pehlivan|OSM||
kürekçi|n|tr|kürek|kürek çeken|OSM||
hakemlik|n|ar|ḥakam|hakem|MOD|H-K-M|
kaleci|n|ar|qalʿa|kale|CUM||
golcü|n|en|goal|gol|MOD||
futbolcu|n|en|football|futbol|CUM||
basketbolcu|n|en|basketball|basketbol|MOD||
voleybolcu|n|en|volleyball|voleybol|MOD||
tenisçi|n|en|tennis|tenis|MOD||
jimnastikçi|n|fr|gymnastique|jimnastik|CUM||
olimpik|adj|fr|olympique|Olimpos'a ait|CUM||grc:Olympikós>fr:olympique>tr:olimpik
sprint|n|en|sprint|kısa koşu|MOD||
depar|n|fr|départ|kalkış|CUM||
krampon|n|fr|crampon|çengel|CUM||
raket|n|fr|raquette|avuç içi|CUM||ar:rāḥa>fr:raquette>tr:raket
frikik|n|en|free kick|serbest vuruş|MOD||
smaç|n|en|smash|çarpma|MOD||
antrenörlük|n|fr|entraîneur|antrenör|MOD||
# --- Taşıtlar, tarım aletleri ---
landon|n|fr|landau|dört tekerlekli araba|OSM19||de:Landau>fr:landau>tr:landon
talika|n|hu|taliga|hafif araba|OSM||
yaylı|n|tr|yay|yaylı araba|OSM|*yay|
kağnı|n|tr|kaŋlı|iki tekerlekli araba|DLT||
fayton|n|fr|phaéton|Phaethon|OSM19||grc:Phaéthōn>fr:phaéton>tr:fayton
boyunduruk|n|tr|boyunduruk|boyun ağacı|DLT||
yaba|n|tr|yaba|ot atma çatalı|OSM||
dirgen|n|tr|dirgen|yaba|OSM||
arabacı|n|tr|araba|araba süren|OSM||
tekerlekçi|n|tr|tegirmek|tekerlek yapan|OSM||
orakçı|n|tr|orgak|orak biçen|OSM||
# --- Esnaf ve zanaat adları ---
yorgancılık|n|tr|yogurkan|yorgancılık|MOD||
çorapçı|n|fa|cūrāb|çorap satan|OSM||
kürkçü|n|tr|kürk|kürk işleyen|OSM||
şapkacı|n|sl|şapka|şapka yapan|OSM19||
fesçi|n|ar|Fās|Fas kenti|OSM19||
tespihçi|n|ar|tasbīḥ|tespih yapan|OSM||
kuşakçı|n|tr|kurşag|kuşak dokuyan|OSM||
halıcılık|n|fa|ġālī|halıcılık|MOD||
kilimcilik|n|fa|gilīm|kilimcilik|MOD||
sepetçi|n|fa|sapad|sepet ören|OSM||
keresteci|n|fa|ḫarasta|kereste satan|OSM||
nalbantlık|n|ar|naʿl-band|nalbant işi|OSM||
ipçi|n|tr|yip|ip yapan|OSM||
urgan|n|tr|urgan|kalın ip|DLT||
urgancı|n|tr|urgan|urgan yapan|OSM||
sicim|n|tr|sicim|ince ip|OSM||
"""

FAMILIES = r"""
*biç-|tr|kesmek, kumaş kesmek|Eski Türkçe bıç- "kesmek"; biçki (kumaş kesme), bıçkı (büyük testere) ve bıçak aynı kökten türer.
*giy-|tr|giymek|Eski Türkçe ked- "giymek" > giy-; giyecek, giydirmek, giyinik, giyimli bu kökün türevleridir.
*kuşa-|tr|kuşak bağlamak, sarmak|Eski Türkçe kurşa- "çevrelemek" (kur- kökünden) > kuşa-; kurşan- > kuşan-; kuşanmak ve kuşam aynı aileden gelir.
*eğir-|tr|iplik bükmek|Eski Türkçe egir- "iğde bükmek"; eğirmek eylemi ve iğ (eğirme çubuğu) aynı kökü paylaşır.
*bük-|tr|bükmek, kıvırmak|Eski Türkçe bük- "eğmek, bükmek"; büküm ve bükülü bu kökten türemiştir.
*kırk-|tr|yün kesmek|Eski Türkçe kırk- "yün kırkmak"; kırkmak ve kırkım (yün kesme mevsimi) aynı köktendir.
*oy-|tr|oymak, kazımak|Eski Türkçe oy- "çukur açmak, oymak"; oyma, oymacı ve oymacılık bu kökten türer.
*kak-|tr|vurmak, çakmak|Eski Türkçe kak- "vurmak, çakmak"; kakmak, kakma (metal süsleme) ve kakmacı aynı aileyi oluşturur.
*kabar-|tr|şişmek, yükselmek|Eski Türkçe kabar- "şişmek"; kabartma, kabartmak ve kabarık bu kökten türemiştir.
*dök-|tr|akıtmak, metal dökmek|Eski Türkçe tök- "dökmek"; döküm, dökümcü ve dökümcülük metal dökme sanatını adlandırır.
*bile-|tr|keskinleştirmek|Eski Türkçe bile- "bıçak keskinleştirmek"; bilemek, bileği (bileme taşı), bileme ve bileyici aynı köktendir.
*tın-|tr|ses vermek|Eski Türkçe tın- "ses çıkarmak, soluk almak"; tını, tınlamak ve tıngırdatmak bu kökten gelir.
*çın-|tr|çınlamak|Ses yansımalı çıŋ kökü; çınlamak ve çınlama madenî sesi anlatır.
*yüz-|tr|suda yüzmek|Eski Türkçe yüz- "suda ilerlemek"; yüzmek, yüzme, yüzücü ve yüzücülük bu kökten türer.
*dal-|tr|suya girmek|Eski Türkçe tal- "dalmak, batmak"; dalmak, dalgıç ve dalış aynı kökü paylaşır.
*tep-|tr|ayakla vurmak|Eski Türkçe tep- "tepmek"; tepmek, tekme (tep-me) ve tekmelemek bu kökten gelir.
*yum-|tr|yuvarlamak, kapamak|Eski Türkçe yum- "yummak, topaklamak"; yumak ve yumruklamak (yumruk) aynı köktendir.
*bur-|tr|bükerek çevirmek|Eski Türkçe bur- "burmak, çevirmek"; burmak, burgu ve burma (burulmuş bilezik) bu kökten türer.
*del-|tr|delik açmak|Eski Türkçe tel- "delmek"; delgi ve delgeç Dil Devrimi döneminde bu kökten türetilmiştir.
*süz-|tr|süzmek, arıtmak|Eski Türkçe süz- "arıtmak"; süzmek, süzgeç ve süzgü bu kökten gelir.
*döv-|tr|dövmek|Eski Türkçe tög- "dövmek, ezmek"; döven (harman aleti) ve dövme (dövülmüş metal) aynı köktendir.
*kuy-|tr|dökmek, kalıba akıtmak|Eski Türkçe kuy- "dökmek"; kuyum (dökülmüş metal) ve kuyumculuk bu kökten türer.
*döşe-|tr|yaymak, sermek|Eski Türkçe töşe- "yaymak"; döşemek, döşemeci, döşemecilik ve döşekçi bu kökten gelir.
*doğra-|tr|parçalamak, kesmek|Eski Türkçe toğra- "doğramak"; doğramacı ve doğramacılık ahşap işçiliğini adlandırır.
*eğe-|tr|törpülemek|Eski Türkçe egek "törpü"; eğe ve eğelemek aynı kökü paylaşır.
*kay-|tr|kaymak|Eski Türkçe kay- "kaymak"; kaydırak, kayakçı ve kayakçılık bu kökten türer.
*yırt-|tr|yırtmak|Eski Türkçe yırt- "yırtmak"; yırtmak ve yırtmaç (etek yırtmacı) aynı köktendir.
*sek-|tr|sıçramak|Eski Türkçe sek- "sıçramak"; seksek oyunu ve sektirmek bu kökten gelir.
*üt-|tr|alevden geçirmek, ütülemek|Eski Türkçe üt- "alevde yakmak"; ütü, ütülemek ve ütücü aynı köktendir.
N-K-Ş|ar|nakış, süsleme|Arapça n-q-ş kökü "kazımak, süslemek"; nakkaş, nakkaşlık, nakışçı ve menkuş (nakışlı) bu kökten gelir.
Z-Y-N|ar|süslemek|Arapça z-y-n kökü; ziynet (süs), tezyin (süsleme), tezyinat ve müzeyyen (süslenmiş) aynı köktendir.
L-B-S|ar|giymek|Arapça l-b-s kökü "giymek"; libas (giysi) ve melbusat (giyilenler) bu kökten türer.
N-S-C|ar|dokumak|Arapça n-s-c kökü "dokumak"; nesic (doku), mensucat (dokumalar) ve nessac (dokumacı) aynı aileyi oluşturur.
C-W-H-R|ar|cevher, öz|Farsça gōhar'dan Arapçaya geçen c-w-h-r kökü; cevher, cevahir, mücevher, mücevherat ve mücevherci bu köktendir.
D-B-Ğ|ar|deri işlemek|Arapça d-b-ġ kökü "tabaklamak"; debbağ, debbağhane, dibagat, tabaklamak ve tabakçı aynı köktendir.
L-Ḥ-M|ar|kaynatmak, birleştirmek|Arapça l-ḥ-m kökü "et; kaynak yapmak"; liḥām > lehim, lehimci ve lehimlemek bu kökten gelir. İlham, l-h-m kökünden gelen ayrı bir ailedir.
T-B-L|ar|davul; tepsi|Arapça ṭ-b-l kökü; tabla, tablakâr ve davulcu (ṭabl "davul") aynı köktendir.
C-L-D|ar|deri, cilt|Arapça c-l-d kökü "deri"; ciltçi, ciltçilik, mücellit ve mücellitlik kitap ciltleme sanatını adlandırır.
Ğ-L-B|ar|üstün gelmek|Arapça ġ-l-b kökü; galip, mağlup, galebe, galibiyet ve mağlubiyet aynı kökten türer.
S-B-K|ar|yarışmak, öne geçmek|Arapça s-b-q kökü "öne geçmek"; müsabaka (yarışma) ve müsabık (yarışmacı) bu köktendir.
R-K-S|ar|dans etmek|Arapça r-q-ṣ kökü; rakkas (dansçı, sarkaç) ve raksetmek aynı kökten gelir.
N-Ğ-M|ar|ezgi|Arapça n-ġ-m kökü; naġma (ezgi) > nağme bu köktendir. Muganni ve teganni, ġ-n-y "şarkı söylemek" kökünden gelen ayrı bir ailedir.
K-S-W|ar|giydirmek, örtmek|Arapça k-s-w kökü; kisve (giysi) ve kispet (güreşçi donu) aynı kökü paylaşır.
C-L-W|ar|parlatmak, açığa çıkarmak|Arapça c-l-w kökü; cila, cilalamak, cilacı ve mücella (parlatılmış) bu kökten türer.
M-D-H|ar|övmek|Arapça m-d-ḥ kökü; meddah (övücü, hikâye anlatıcısı), medih ve methiye aynı köktendir.
H-T-M|ar|mühürlemek, bitirmek|Arapça ḫ-t-m kökü; hatem (mühür yüzüğü) ve hitam (son) bu kökten gelir.
R-B-T|ar|bağlamak|Arapça r-b-ṭ kökü; rapt, raptiye ve merbut (bağlı) aynı kökten türer.
S-W-Y|ar|düzlemek, eşitlemek|Arapça s-w-y kökü; tesviye, tesviyeci ve tesviyecilik metal düzleme işini adlandırır.
D-L-K|ar|ovmak|Arapça d-l-k kökü "ovmak"; tellak (hamamda ovucu) ve tellaklık bu köktendir.
A-T-R|ar|güzel koku|Arapça ʿ-ṭ-r kökü; ıtır ve ıtriyat (kokular) aynı kökten gelir.
B-H-S|ar|araştırmak, tartışmak|Arapça b-ḥ-ṯ kökü; bahis (iddia, konu) ve mebhas (araştırma konusu) bu köktendir.
C-H-Z|ar|donatmak|Arapça c-h-z kökü; çeyiz, cihaz, teçhizat ve mücehhez (donatılmış) aynı kökten türer.
S-R-C|ar|eyer|Arapça s-r-c kökü "eyer"; saraç, saraçlık ve saraçhane koşum zanaatını adlandırır.
M-S-H|ar|elle sıvazlamak, ölçmek|Arapça m-s-ḥ kökü; mest (mesh edilen ayakkabı) ve mesaha (yer ölçme) bu köktendir.
F-S-L|ar|bölmek, ayırmak|Arapça f-ṣ-l kökü; fasıl (bölüm, müzik faslı), fasıla (ara) ve mufassal (ayrıntılı) aynı köktendir.
dūz-|fa|dikmek|Farsça dūḫtan/dūz- "dikmek" ve darzī "terzi" aynı kökten; çuvaldız (çuval diken iğne) ve terzilik bu aileye girer.
tarāş|fa|yontmak, kesmek|Farsça tarāşīdan "yontmak"; tıraş ve talaş (yontma kırıntısı) bu kökten gelir.
-dān|fa|kap, mahfaza|Farsça -dān "kap" eki; çaydanlık, yağdan ve sürmedan bu ekle kurulmuştur.
chiffe|fr|paçavra, ince bez|Fransızca chiffe "paçavra"; şifon (ince kumaş) ve şifonyer (çamaşır dolabı) aynı sözcükten türer.
cannabis|la|kenevir|Latince cannabis "kenevir"; kanaviçe ve kanava kenevir bezinden ad alır.
tornare|la|döndürmek|Latince tornare "torna ile döndürmek"; torna, tornacı, tornacılık, tornalamak ve turnuva aynı köktendir.
recordari|la|hatırlamak, kaydetmek|Latince recordari "hatırlamak"; rekor ve rekortmen İngilizce record üzerinden Türkçeye gelmiştir.
athlon|el|yarışma, ödül|Eski Yunanca âthlon "yarışma"; atletizm, dekatlon ve triatlon bu köktendir.
Marathōn|el|Marathon ovası|Eski Yunanca Marathṓn yer adı; maraton ve maratoncu bu addan türemiştir.
akros|el|uç, tepe|Eski Yunanca ákros "uç, en yüksek"; akrobat (uçta yürüyen) ve akrobasi aynı köktendir.
khoros|el|dans, koro|Eski Yunanca chorós "dans, oyun topluluğu"; horon, koreografi ve koreograf bu kökten gelir.
ballare|la|dans etmek|Geç Latince ballare "dans etmek"; balo ve balerin İtalyanca üzerinden Türkçeye geçmiştir.
campus|la|alan, savaş alanı|Latince campus "alan"; şampiyon (campio "alan savaşçısı"), şampiyona ve şampiyonluk aynı köktendir.
"""

COGNATES = r"""
@soba shared_ancestor
  hu szoba ; oda ; ff:Macarca szoba "oda" demektir; Türkçeye geçerken anlam "odayı ısıtan araç"a kaymıştır
  de Stube ; oda, oturma odası ; ff:Almanca Stube "oda"; Macarca szoba bu sözcükten gelir
  bg соба [soba] ; oda ; ff:Bulgarcada соба "oda" anlamındadır
  sr соба [soba] ; oda ; ff:Sırpçada soba "oda"; soba için peć kullanılır
  mk соба [soba] ; oda
@soba from_turkish
  ro sobă ; soba
  sq sobë ; soba
  el σόμπα [sóba] ; soba
@tandır shared_ancestor
  ar تنور [tannūr] ; fırın, tandır
  fa تنور [tanūr] ; tandır
  ur تندور [tandūr] ; tandır
  en tandoor ; tandır
  az təndir ; tandır
  uz tandir ; tandır
  kk тандыр [tandır] ; tandır
  ky тандыр [tandır] ; tandır
  he תנור [tanur] ; fırın, ocak
  ka თონე [tone] ; tandır
  hy թոնիր [tonir] ; tandır
@kibrit shared_ancestor
  ar كبريت [kibrīt] ; kükürt ; ff:Arapçada kibrīt yalnızca "kükürt"; kibrit için ʿūd ṯiqāb denir
  fa کبریت [kibrīt] ; kibrit
  az kibrit ; kibrit
  ro chibrit ; kibrit
  bg кибрит [kibrit] ; kibrit
  mk кибрит [kibrit] ; kibrit
  he גופרית [gofrit] ; kükürt
@mandal into_turkish
  el μάνδαλος [mándalos] ; sürgü, kapı mandalı
@mandal from_turkish
  bg мандало [mandalo] ; sürgü
  sr мандал [mandal] ; sürgü, mandal
  sq mandall ; sürgü
  mk мандало [mandalo] ; sürgü
@çıkrık from_turkish
  bg чекрък [čekrăk] ; çıkrık
  sr чекрк [čekrk] ; çıkrık, makara
  mk чекрек [čekrek] ; çıkrık
  sq çikrik ; çıkrık
@mekik shared_ancestor
  ar مكوك [makkūk] ; mekik
  az məkik ; mekik
  uz moku ; mekik
@körük shared_ancestor
  az körük ; körük
  kk көрік [körik] ; körük
  ky көөрүк [köörük] ; körük
  tk körük ; körük
@kerpeten shared_ancestor
  ar كلبتان [kalbatān] ; kıskaç ; ff:Arapçada "iki köpek" anlamındaki ikil biçim; kıskacın iki çenesini anlatır
  bg керпеден [kerpeden] ; kerpeten
  sq kërpetë ; kerpeten
@makara shared_ancestor
  ar بكرة [bakara] ; makara
  bg макара [makara] ; makara
  sr макара [makara] ; makara
  mk макара [makara] ; makara
  sq makara ; makara
  el μακαράς [makarás] ; makara
@küp shared_ancestor
  az küp ; küp
  sr ћуп [ćup] ; küp, çömlek
  mk ќуп [ḱup] ; küp
  bg кюп [kyup] ; küp
@gön shared_ancestor
  az gön ; gön, deri
  kk көн [kön] ; işlenmiş deri
  uz koʻn ; deri
  ky көн [kön] ; deri
  bg гьон [gyon] ; ayakkabı tabanı derisi
  sr ђон [đon] ; ayakkabı tabanı ; ff:Sırpçada đon yalnızca "ayakkabı tabanı" demektir
  mk ѓон [ǵon] ; ayakkabı tabanı
@kösele into_turkish
  fa گوساله [gūsāle] ; dana, buzağı ; ff:Farsçada gūsāle "dana"; Türkçede dana derisine, sonra kalın tabanlık deriye kaymıştır
@sahtiyan shared_ancestor
  fa سختیان [saḫtiyān] ; keçi derisi
  ru сафьян [saf'yan] ; sahtiyan
  bg сахтиян [sahtiyan] ; sahtiyan
  sr сахтијан [sahtijan] ; sahtiyan
  pl safian ; sahtiyan
  hu szattyán ; sahtiyan
@meşin shared_ancestor
  fa میشین [mīşīn] ; koyun derisi
  bg мешин [mešin] ; meşin
  sr мешина [mešina] ; tulum, deri kırba ; ff:Sırpçada mešina "deri tulum"
@aba shared_ancestor
  ar عباء [ʿabāʾ] ; aba, üstlük
  en abaya ; kadın üstlüğü
  bg аба [aba] ; aba kumaşı
  sr аба [aba] ; aba
  mk аба [aba] ; aba
  ro aba ; aba
  hu aba ; kaba yünlü kumaş
  sq abë ; aba
@tafta shared_ancestor
  fa تافته [tāfte] ; dokunmuş ; ff:Farsça tāfte "bükülmüş, dokunmuş" sıfatıdır
  it taffettà ; tafta
  fr taffetas ; tafta
  en taffeta ; tafta
  ru тафта [tafta] ; tafta
@muslin shared_ancestor
  fr mousseline ; muslin
  en muslin ; muslin
  it mussolina ; muslin
  ar موصلي [mawṣilī] ; Musul'a ait ; ff:Kumaş Musul kentinin adından türemiştir
  ru муслин [muslin] ; muslin
@patiska shared_ancestor
  it battista ; patiska
  fr batiste ; patiska
  en batiste ; patiska
  ru батист [batist] ; patiska
@basma from_turkish
  bg басма [basma] ; basma kumaş
  mk басма [basma] ; basma
  sq basmë ; basma
  ro basma ; başörtüsü ; ff:Rumencede basma "başörtüsü, eşarp" anlamına kaymıştır
@alaca shared_ancestor
  az alaca ; alaca
  uz olacha ; çizgili pamuklu kumaş
  kk ала [ala] ; alaca, benekli
@çuha shared_ancestor
  fa چوخا [çūḫā] ; yünlü kumaş
  bg чоха [čoha] ; çuha
  sr чоха [čoha] ; çuha
  mk чоја [čoja] ; çuha
  sq çohë ; çuha
  el τσόχα [tsócha] ; çuha
  hu csuha ; keşiş cübbesi ; ff:Macarca csuha "keşiş cübbesi" anlamına kaymıştır
  ka ჩოხა [chokha] ; geleneksel erkek kaftanı ; ff:Gürcücede çokha ulusal erkek giysisinin adıdır
@kurdele shared_ancestor
  it cordella ; ipcik, kurdele
  el κορδέλα [kordéla] ; kurdele
  bg кордела [kordela] ; kurdele
@sırma into_turkish
  el σύρμα [sýrma] ; tel ; ff:Yunanca sýrma genel olarak "tel"; Türkçede gümüş işleme teli
@sırma from_turkish
  bg сърма [sărma] ; sırma
  sr срма [srma] ; sırma
  mk срма [srma] ; sırma
  sq sërmë ; sırma
  ro sârmă ; tel ; ff:Rumence sârmă genel "tel" anlamındadır
@kaytan shared_ancestor
  ar قيطان [qayṭān] ; kaytan
  bg гайтан [gaytan] ; kaytan
  sr гајтан [gajtan] ; kaytan
  mk гајтан [gajtan] ; kaytan
  sq gajtan ; kaytan
  ro găitan ; kaytan
  el γαϊτάνι [gaïtáni] ; kaytan
@yaşmak from_turkish
  en yashmak ; yaşmak
  fr yachmak ; yaşmak
  bg яшмак [yašmak] ; yaşmak
  ru яшмак [yašmak] ; yaşmak
@ferace shared_ancestor
  ar فرجية [faraciyya] ; geniş üst giysi
  bg фередже [feredže] ; ferace
  sr фереџа [feredža] ; ferace
  mk фереџе [feredže] ; ferace
  sq ferexhe ; ferace
  ro feregea ; ferace
  el φερετζές [feretzés] ; ferace
@entari shared_ancestor
  ar عنتري [ʿantarī] ; entari
  bg антерия [anteriya] ; entari
  sr антерија [anterija] ; entari
  mk антерија [anterija] ; entari
  sq anteri ; entari
  ro anteriu ; entari
  el αντερί [anderí] ; entari
@mintan shared_ancestor
  fa نیم‌تن [nīmtan] ; yarım beden, kısa ceket
  bg минтан [mintan] ; mintan
  sr минтан [mintan] ; mintan
  mk минтан [mintan] ; mintan
  sq mintan ; mintan
  ro mintean ; mintan
@potur from_turkish
  bg потури [poturi] ; potur
  sq poture ; potur
  mk потури [poturi] ; potur
@çakşır from_turkish
  bg чакшири [čakširi] ; çakşır
  sr чакшире [čakšire] ; pantolon ; ff:Sırpçada čakšire genel olarak "pantolon" demektir
  mk чакшири [čakširi] ; çakşır
@fistan shared_ancestor
  el φουστάνι [foustáni] ; elbise
  bg фустан [fustan] ; fistan, elbise
  sr фистан [fistan] ; fistan
  mk фустан [fustan] ; elbise
  sq fustan ; elbise
  ro fustă ; etek ; ff:Rumence fustă yalnızca "etek"
  it fustagno ; kadife benzeri pamuklu ; ff:İtalyanca fustagno bir kumaş adıdır, giysi değil
  en fustian ; kalın pamuklu kumaş
@pelerin shared_ancestor
  fr pèlerine ; pelerin
  en pilgrim ; hacı ; ff:İngilizce pilgrim "hacı"; pelerin hacı giysisinden ad alır
  it pellegrina ; pelerin
  de Pelerine ; pelerin
  ru пелерина [pelerina] ; pelerin
@mest shared_ancestor
  ar مسح [masḥ] ; silme, meshetme ; ff:Arapçada masḥ "elle sıvazlama"; Türkçede mesh edilen ayakkabı
  bg местове [mestove] ; mest
  sr местве [mestve] ; mest
  sq mest ; mest
@iskarpin shared_ancestor
  it scarpino ; küçük ayakkabı
  es escarpín ; patik, hafif ayakkabı
  fr escarpin ; iskarpin
@halhal shared_ancestor
  ar خلخال [ḫalḫāl] ; halhal
  fa خلخال [ḫalḫāl] ; halhal
  az xalxal ; halhal
@zümrüt shared_ancestor
  ar زمرد [zumurrud] ; zümrüt
  fa زمرد [zumurrud] ; zümrüt
  az zümrüd ; zümrüt
  uz zumrad ; zümrüt
  ur زمرد [zumurrud] ; zümrüt
  el σμαράγδι [smarágdi] ; zümrüt
  en emerald ; zümrüt
  fr émeraude ; zümrüt
  it smeraldo ; zümrüt
  ru изумруд [izumrud] ; zümrüt
  hu smaragd ; zümrüt
@yakut shared_ancestor
  ar ياقوت [yāqūt] ; yakut
  fa یاقوت [yāqūt] ; yakut
  az yaqut ; yakut
  uz yoqut ; yakut
  ur یاقوت [yāqūt] ; yakut
  el υάκινθος [yákinthos] ; sümbül ; ff:Yunanca hyákinthos "sümbül"; taş adı bitkiden gelir
  en jacinth ; sarı-kızıl değerli taş
  ru яхонт [yaxont] ; yakut, safir (eski)
@elmas shared_ancestor
  ar ألماس [almās] ; elmas
  fa الماس [almās] ; elmas
  az almaz ; elmas
  kk алмас [almas] ; elmas
  uz olmos ; elmas
  ky алмаз [almaz] ; elmas
  tk almaz ; elmas
  ru алмаз [almaz] ; ham elmas ; ff:Rusçada almaz işlenmemiş elmas; işlenmişi brilliant
  uk алмаз [almaz] ; elmas
  ur الماس [almās] ; elmas
  el αδάμας [adámas] ; elmas ; ff:Eski Yunanca adámas "yenilmez" demektir
  en diamond ; elmas
  fr diamant ; elmas
  bg елмаз [elmaz] ; elmas
@pırlanta shared_ancestor
  it brillante ; parlayan; pırlanta
  fr brillant ; pırlanta
  en brilliant ; parlak ; ff:İngilizcede brilliant daha çok "parlak, zeki" sıfatıdır
  ru бриллиант [brilliant] ; pırlanta
  bg брилянт [brilyant] ; pırlanta
  az brilyant ; pırlanta
@firuze shared_ancestor
  fa فیروزه [fīrūze] ; firuze
  ar فيروز [fayrūz] ; firuze
  az firuzə ; firuze
  uz feruza ; firuze
  ur فیروزہ [fīrozā] ; firuze
  fr turquoise ; firuze ; ff:Fransızca "Türk taşı" demektir; taş Avrupa'ya Türkiye üzerinden ulaşmıştır
  en turquoise ; firuze
  ru бирюза [biryuza] ; firuze
  hy փիրուզ [p'iruz] ; firuze
  ka ფირუზი [piruzi] ; firuze
@akik shared_ancestor
  ar عقيق [ʿaqīq] ; akik
  fa عقیق [ʿaqīq] ; akik
  az əqiq ; akik
  uz aqiq ; akik
  ur عقیق [ʿaqīq] ; akik
@sedef shared_ancestor
  ar صدف [ṣadaf] ; deniz kabuğu, sedef
  fa صدف [ṣadaf] ; sedef
  az sədəf ; sedef
  uz sadaf ; sedef
  ur صدف [ṣadaf] ; sedef
  bg седеф [sedef] ; sedef
  sr седеф [sedef] ; sedef
  mk седеф [sedef] ; sedef
  sq sedef ; sedef
  ro sidef ; sedef
  el σεντέφι [sedéfi] ; sedef
@lal shared_ancestor
  fa لعل [laʿl] ; lal taşı
  ar لعل [laʿl] ; lal
  az ləl ; lal
  uz laʼl ; lal
  ur لعل [laʿl] ; lal
  ru лал [lal] ; yakut (eski)
@safir shared_ancestor
  fr saphir ; safir
  en sapphire ; safir
  el σάπφειρος [sápfeiros] ; safir
  he ספיר [sapir] ; safir
  ru сапфир [sapfir] ; safir
  it zaffiro ; safir
  de Saphir ; safir
@topaz shared_ancestor
  en topaz ; topaz
  el τοπάζι [topázi] ; topaz
  ru топаз [topaz] ; topaz
  it topazio ; topaz
  de Topas ; topaz
@platin shared_ancestor
  es platina ; gümüşçük ; ff:İspanyolca plata "gümüş" küçültmesi
  fr platine ; platin
  en platinum ; platin
  ru платина [platina] ; platin
  de Platin ; platin
  it platino ; platin
@bronz shared_ancestor
  it bronzo ; bronz
  fr bronze ; bronz
  en bronze ; bronz
  de Bronze ; bronz
  ru бронза [bronza] ; bronz
  fa برنج [birinc] ; pirinç ; ff:İtalyanca bronzo'nun Farsça birinc "pirinç"ten geldiği öne sürülür
@alyans shared_ancestor
  fr alliance ; ittifak; nişan yüzüğü ; ff:Fransızcada alliance öncelikle "ittifak, birlik"
  en alliance ; ittifak ; ff:İngilizcede yalnızca "ittifak"; yüzük anlamı yoktur
  it alleanza ; ittifak ; ff:İtalyancada yalnızca "ittifak"
@madalyon shared_ancestor
  fr médaillon ; madalyon
  it medaglione ; madalyon
  en medallion ; madalyon
  ru медальон [medal'on] ; madalyon
  bg медальон [medalyon] ; madalyon
@madalya shared_ancestor
  it medaglia ; madalya
  fr médaille ; madalya
  en medal ; madalya
  ru медаль [medal'] ; madalya
  bg медал [medal] ; madalya
  de Medaille ; madalya
  es medalla ; madalya
  ar ميدالية [mīdāliyya] ; madalya
  az medal ; madalya
@hatem shared_ancestor
  ar خاتم [ḫātam] ; mühür; yüzük; son
  fa خاتم [ḫātam] ; mühür yüzüğü
  ur خاتم [ḫātam] ; mühür
  az xatəm ; mühür yüzüğü
  he חותם [ḥotam] ; mühür
@kaşe shared_ancestor
  fr cachet ; mühür; sanatçı ücreti ; ff:Fransızcada cachet "sanatçı ücreti, prestij" anlamı da taşır
  en cachet ; saygınlık, prestij ; ff:İngilizcede yalnızca "prestij, ayırt edici nitelik"
@cevher shared_ancestor
  fa گوهر [gawhar] ; cevher, inci ; ff:Sözcüğün asıl kaynağı Farsçadır; Arapçaya cawhar olarak geçmiştir
  ar جوهر [cawhar] ; öz, töz; mücevher
  ur جوہر [jauhar] ; öz; yetenek ; ff:Urducada jauhar "yetenek, cevher" anlamında da kullanılır
  az cövhər ; cevher
  uz javhar ; cevher
  kk жауһар [jawhar] ; cevher, mücevher
@cevahir shared_ancestor
  ar جواهر [cawāhir] ; mücevherler
  fa جواهر [cavāhir] ; mücevher
  az cəvahir ; mücevher
  uz javohir ; mücevher
  ur جواہر [javāhir] ; mücevherler
@ziynet shared_ancestor
  ar زينة [zīna] ; süs
  fa زینت [zīnat] ; süs
  az zinət ; süs
  uz ziynat ; süs
  ur زینت [zīnat] ; süs
@cila shared_ancestor
  ar جلاء [cilāʾ] ; parlaklık; açıklık ; ff:Arapçada cilāʾ "açıklık, netlik; sürgün" anlamları da taşır
  az cila ; cila
  uz jilo ; cila, parlaklık
  ur جلا [jilā] ; parlaklık
@vernik shared_ancestor
  it vernice ; vernik; boya
  fr vernis ; vernik
  en varnish ; vernik
  de Firnis ; vernik
  es barniz ; vernik
  el βερνίκι [verníki] ; vernik
@zamk shared_ancestor
  ar صمغ [ṣamġ] ; zamk
  fa صمغ [ṣamġ] ; zamk
@kalbur shared_ancestor
  ar غربال [ġirbāl] ; kalbur
  fa غربال [ġirbāl] ; kalbur
  az xəlbir ; kalbur
  uz gʻalvir ; kalbur
  es garbillo ; kalbur
  it crivello ; elek ; ff:Latince cribellum'dan; Arapça ġirbāl ile aynı kaynak
  fr crible ; elek
@semer into_turkish
  el σαμάρι [samári] ; semer
@semer from_turkish
  bg самар [samar] ; semer
  sr самар [samar] ; semer
  mk самар [samar] ; semer
  sq samar ; semer
  ro samar ; semer
@eyer shared_ancestor
  az yəhər ; eyer
  kk ер [er] ; eyer
  uz egar ; eyer
  ky ээр [eer] ; eyer
  tk eýer ; eyer
@üzengi shared_ancestor
  az üzəngi ; üzengi
  kk үзеңгі [üzeŋgi] ; üzengi
  uz uzangi ; üzengi
  ky үзөңгү [üzöŋgü] ; üzengi
  tk üzeňňi ; üzengi
@dizgin shared_ancestor
  kk тізгін [tizgin] ; dizgin
  ky тизгин [tizgin] ; dizgin
  uz tizgin ; dizgin
@mıh shared_ancestor
  fa میخ [mīḫ] ; çivi
  az mıx ; çivi
  uz mix ; çivi
  ur میخ [meḫ] ; çivi
@palan shared_ancestor
  fa پالان [pālān] ; semer
  az palan ; palan
  ur پالان [pālān] ; semer
@talika into_turkish
  hu taliga ; el arabası, iki tekerlekli araba ; ff:Macarcada taliga daha çok "el arabası"
@talika from_turkish
  bg талига [taliga] ; araba
  sr таљиге [taljige] ; at arabası
  mk талига [taliga] ; araba
@fayton shared_ancestor
  fr phaéton ; fayton
  en phaeton ; fayton
  bg файтон [fayton] ; fayton
  mk фајтон [fajton] ; fayton
  sq pajton ; fayton
  ru фаэтон [faeton] ; fayton
@boyunduruk shared_ancestor
  az boyunduruq ; boyunduruk
  kk мойынтұрық [moyıntırıq] ; boyunduruk
  uz boʻyinturuq ; boyunduruk
  ky моюнтурук [moyunturuk] ; boyunduruk
  tk boýuntyryk ; boyunduruk
@çaydanlık shared_ancestor
  az çaydan ; çaydanlık
  fa چایدان [çāydān] ; çay kabı
  kk шәйнек [şäynek] ; çaydanlık ; ff:Kazakça biçim Rusça чайник'ten alınmıştır
  ru чайник [čaynik] ; çaydanlık ; ff:Aynı Çince çay köküne Rusça -nik, Türkçeye Farsça -dān eklenmiştir
@zembil shared_ancestor
  ar زنبيل [zanbīl] ; zembil
  fa زنبیل [zanbīl] ; sepet
  bg зембил [zembil] ; zembil
  sr зембиљ [zembilj] ; zembil
  mk зембил [zembil] ; zembil
  el ζεμπίλι [zembíli] ; zembil
@küfe shared_ancestor
  el κοφίνι [kofíni] ; sepet
  en coffin ; tabut ; ff:İngilizce coffin aynı Yunanca kóphinos'tan "tabut" anlamına kaymıştır
  fr couffin ; bebek sepeti
@fıçı shared_ancestor
  el βουτσί [voutsí] ; fıçı
  sr бачва [bačva] ; fıçı
  it botte ; fıçı
  en butt ; büyük fıçı (eski)
  de Bottich ; fıçı, tekne
@varil shared_ancestor
  fr baril ; varil
  en barrel ; varil
  es barril ; varil
  it barile ; varil
  bg варел [varel] ; varil
@damacana shared_ancestor
  it damigiana ; damacana
  fr dame-jeanne ; damacana ; ff:Halk etimolojisiyle "Bayan Jeanne" biçimine girmiştir
  en demijohn ; damacana
  es damajuana ; damacana
  bg дамаджана [damadžana] ; damacana
  ro damigeană ; damacana
  el νταμιτζάνα [damitzána] ; damacana
@matara shared_ancestor
  ar مطهرة [maṭhara] ; abdest ibriği ; ff:Arapçada maṭhara "temizlenme kabı"; Türkçede su kabına kaymıştır
  bg матара [matara] ; matara
  sr матара [matara] ; matara
  mk матара [matara] ; matara
@şişe shared_ancestor
  fa شیشه [şīşe] ; cam; şişe
  az şüşə ; cam ; ff:Azerbaycancada şüşə öncelikle "cam"
  uz shisha ; cam ; ff:Özbekçede shisha "cam, pencere camı"
  ur شیشہ [şīşa] ; cam; ayna ; ff:Urducada şīşa "ayna" anlamında da kullanılır
  bg шише [šiše] ; şişe
  mk шише [šiše] ; şişe
  sq shishe ; şişe
@bakraç from_turkish
  bg бакрач [bakrač] ; bakır kova
  sr бакрач [bakrač] ; bakraç
  mk бакрач [bakrač] ; bakraç
  hu bogrács ; kazan ; ff:Macarca bogrács "üçayak üzerinde asılan yemek kazanı"; gulaş kazanı
@hallaç shared_ancestor
  ar حلاج [ḥallāc] ; pamuk atıcı
  fa حلاج [ḥallāc] ; hallaç
  az hallac ; hallaç
@çulha shared_ancestor
  fa جولاه [cūlāh] ; dokumacı
  ur جولاہا [julāhā] ; dokumacı
@çul shared_ancestor
  ar جل [cull] ; at örtüsü
  bg чул [čul] ; çul
  sq çul ; çul
@saraç shared_ancestor
  ar سراج [sarrāc] ; saraç
  bg сарач [sarač] ; saraç
  sr сарач [sarač] ; saraç
  mk сарач [sarač] ; saraç
  sq saraç ; saraç
@boyacılık from_turkish
  bg бояджия [boyadžiya] ; boyacı
  sr бојаџија [bojadžija] ; boyacı
  mk бојаџија [bojadžija] ; boyacı
  sq bojaxhi ; boyacı
  ro boiangiu ; boyacı
  el μπογιατζής [bogiatzís] ; boyacı
@doğramacı from_turkish
  bg дограмаджия [dogramadžiya] ; doğramacı
  mk дограмаџија [dogramadžija] ; doğramacı
  sq dogramaxhi ; doğramacı
@kanaviçe shared_ancestor
  it canovaccio ; kanaviçe; taslak ; ff:İtalyancada canovaccio "senaryo taslağı" anlamı da taşır
  fr canevas ; kanaviçe; taslak
  en canvas ; branda bezi; tuval ; ff:İngilizce canvas "tuval, branda" anlamındadır
@şifon shared_ancestor
  fr chiffon ; paçavra; ince kumaş ; ff:Fransızcada chiffon öncelikle "paçavra, bez"
  en chiffon ; şifon
  ru шифон [šifon] ; şifon
@krep shared_ancestor
  fr crêpe ; krep kumaş; ince gözleme ; ff:Fransızca crêpe hem kumaş hem gözleme
  en crepe ; krep
  it crespo ; kıvırcık; krep
@flanel shared_ancestor
  fr flanelle ; flanel
  en flannel ; flanel
  ru фланель [flanel'] ; flanel
  bg фланела [flanela] ; tişört, fanila ; ff:Bulgarcada фланела "tişört, fanila"
@kendir shared_ancestor
  az kəndir ; ip, halat ; ff:Azerbaycancada kəndir "ip, halat" demektir
  kk кендір [kendir] ; kenevir
  ky кендир [kendir] ; kenevir
  tk kendir ; kenevir
@çile shared_ancestor
  fa چله [çille] ; kırk gün; yay kirişi; iplik çilesi
  az çillə ; kış soğuğu dönemi ; ff:Azerbaycancada çillə "kışın en soğuk kırk günü"
  uz chilla ; kırk günlük dönem ; ff:Özbekçede chilla "kırk gün"; yaz veya kış çillesi
  ur چلہ [çilla] ; kırk günlük inziva ; ff:Urducada çilla "kırk günlük ibadet"
@yumak shared_ancestor
  az yumaq ; yumak
  uz yumaloq ; yuvarlak ; ff:Özbekçede yumaloq "yuvarlak" sıfatıdır
@kıl shared_ancestor
  az qıl ; kıl
  kk қыл [qıl] ; kıl
  uz qil ; kıl
  ky кыл [kıl] ; kıl
  tk gyl ; kıl
@koza shared_ancestor
  fa غوزه [ġōze] ; pamuk kozası
  az qoza ; koza
  uz gʻoʻza ; pamuk bitkisi ; ff:Özbekçede gʻoʻza "pamuk bitkisi" demektir
@eğirmek shared_ancestor
  az əyirmək ; eğirmek
  kk иіру [iyirw] ; eğirmek
  uz yigirmoq ; eğirmek
  ky ийрүү [iyrüü] ; eğirmek
  tk egirmek ; eğirmek
@iğ shared_ancestor
  az iy ; iğ
  tk ik ; iğ
@nakkaş shared_ancestor
  ar نقاش [naqqāş] ; ressam; nakkaş
  fa نقاش [naqqāş] ; ressam ; ff:Farsçada naqqāş günümüzde "ressam"
  az nəqqaş ; nakkaş
  uz naqqosh ; nakkaş
  ur نقاش [naqqāş] ; ressam ; ff:Urducada naqqāş "ressam"
@gergef shared_ancestor
  fa کارگاه [kārgāh] ; atölye; tezgâh ; ff:Farsçada kārgāh "atölye, iş yeri"; Türkçede nakış çerçevesine daralmıştır
  bg гергеф [gergef] ; gergef
  sr ђерђеф [đerđef] ; gergef
  mk ѓерѓеф [ǵerǵef] ; gergef
  sq gjergjef ; gergef
  ro gherghef ; gergef
@fiyonk shared_ancestor
  it fiocco ; püskül; fiyonk; kar tanesi ; ff:İtalyanca fiocco "kar tanesi" anlamı da taşır
  bg фльонга [flyonga] ; fiyonk
  sq fjongo ; kurdele, fiyonk
  el φιόγκος [fiógos] ; fiyonk
@pile shared_ancestor
  fr plissé ; pile
  en pleat ; pile
  de Plissee ; pile
  ru плиссе [plisse] ; pile
@kıyafet shared_ancestor
  ar قيافة [qiyāfa] ; iz sürme; görünüşten tanıma ; ff:Arapçada qiyāfa "iz sürme, fizyonomi"; giysi anlamı Türkçeye özgüdür
  az qiyafə ; görünüş, çehre ; ff:Azerbaycancada qiyafə "dış görünüş"
  uz qiyofa ; görünüş, çehre ; ff:Özbekçede qiyofa "yüz, görünüş"
  ur قیافہ [qiyāfa] ; tahmin; görünüş ; ff:Urducada qiyāfa "tahmin yürütme"
@libas shared_ancestor
  ar لباس [libās] ; giysi
  fa لباس [libās] ; giysi
  ur لباس [libās] ; giysi
  az libas ; giysi
  uz libos ; giysi
@urba shared_ancestor
  it roba ; eşya, şey ; ff:İtalyanca roba genel olarak "eşya, şey"
  es ropa ; giysi
  fr robe ; kadın elbisesi
  en robe ; cübbe, sabahlık
  de Robe ; tören giysisi
  bg роба [roba] ; sabahlık ; ff:Bulgarcada роба "sabahlık, bornoz"
  ru роба [roba] ; iş tulumu ; ff:Rusçada роба "iş giysisi"
@don shared_ancestor
  az don ; kadın elbisesi ; ff:Azerbaycancada don "elbise"; iç giysi anlamı yoktur
  kk тон [ton] ; kürk palto ; ff:Kazakçada тон "kürk, palto"
  uz toʻn ; kaftan, cüppe ; ff:Özbekçede toʻn "geleneksel çapan"
  ky тон [ton] ; kürk palto
  tk don ; elbise, giysi
@külot shared_ancestor
  fr culotte ; kısa pantolon; külot ; ff:Fransızcada culotte tarihsel olarak "diz pantolonu"
  en culottes ; etek pantolon ; ff:İngilizcede culottes "etek görünümlü pantolon"
  bg кюлоти [kyuloti] ; külot
@sutyen shared_ancestor
  fr soutien-gorge ; sutyen
  bg сутиен [sutien] ; sutyen
  ro sutien ; sutyen
  el σουτιέν [soutién] ; sutyen
  sq sutjena ; sutyen
@korse shared_ancestor
  fr corset ; korse
  en corset ; korse
  ru корсет [korset] ; korse
  it corsetto ; korse
@jüpon shared_ancestor
  fr jupon ; iç etek
  fr jupe ; etek
  it giubba ; ceket ; ff:İtalyanca giubba "ceket"; Arapça cubba'dan
  es jubón ; yelek, kısa ceket ; ff:İspanyolca jubón "sıkı yelek"
  ru юбка [yubka] ; etek ; ff:Rusça юбка "etek"; aynı Arapça cubba'dan Lehçe yoluyla
  ar جبة [cubba] ; cübbe
@papyon shared_ancestor
  fr papillon ; kelebek ; ff:Fransızcada papillon "kelebek"; papyon kravat "nœud papillon"
  it papillon ; papyon kravat
@manşet shared_ancestor
  fr manchette ; kol ağzı; gazete başlığı
  ru манжета [manžeta] ; kol ağzı
  bg маншет [manšet] ; kol ağzı
  de Manschette ; kol ağzı
@astar shared_ancestor
  fa آستر [āstar] ; astar
  az astar ; astar
  uz astar ; astar
  ur استر [astar] ; astar
  bg астар [astar] ; astar
  sq astar ; astar
  mk астар [astar] ; astar
@kayış shared_ancestor
  az qayış ; kayış
  kk қайыс [qayıs] ; kayış
  uz qayish ; kayış
  ky кайыш [kayış] ; kayış
  tk gaýyş ; kayış
  bg каиш [kaiš] ; kayış
  sr каиш [kaiš] ; kayış, kemer
  mk каиш [kaiš] ; kayış
@paçavra from_turkish
  bg пачавра [pačavra] ; paçavra
  sr пачавра [pačavra] ; paçavra
  mk пачавра [pačavra] ; paçavra
  sq paçavure ; paçavra
  el πατσαβούρα [patsavoúra] ; paçavra
@bornoz shared_ancestor
  ar برنس [burnus] ; kukuletalı pelerin
  fr burnous ; bornoz
  en burnous ; Arap pelerini
  es albornoz ; bornoz
  ru бурнус [burnus] ; bornoz
@önlük shared_ancestor
  az önlük ; önlük
  tk öňlük ; önlük
@süveter shared_ancestor
  en sweater ; süveter
  ru свитер [sviter] ; süveter
  uz sviter ; süveter
  az sviter ; süveter ; ff:Azerbaycancaya Rusça yoluyla girmiştir
@triko shared_ancestor
  fr tricot ; örgü
  en tricot ; triko kumaş
  ru трико [triko] ; tayt, mayo ; ff:Rusçada трико "tayt, jimnastik giysisi"
@parka shared_ancestor
  en parka ; parka
  ru парка [parka] ; parka
  fr parka ; parka
@anorak shared_ancestor
  en anorak ; anorak
  fr anorak ; anorak
  de Anorak ; anorak
  ru анорак [anorak] ; anorak
@bluz shared_ancestor
  fr blouse ; bluz; iş önlüğü ; ff:Fransızcada blouse "iş önlüğü" anlamı da taşır
  en blouse ; bluz
  ru блузка [bluzka] ; bluz
  bg блуза [bluza] ; bluz
  de Bluse ; bluz
@tunik shared_ancestor
  fr tunique ; tunik
  en tunic ; tunik
  it tunica ; tunik
  ru туника [tunika] ; tunik
@frak shared_ancestor
  fr frac ; frak
  de Frack ; frak
  ru фрак [frak] ; frak
  en frock ; elbise; cübbe ; ff:İngilizce frock "kadın elbisesi, rahip cübbesi"
  bg фрак [frak] ; frak
  pl frak ; frak
@smokin shared_ancestor
  fr smoking ; smokin
  ru смокинг [smoking] ; smokin
  de Smoking ; smokin
  it smoking ; smokin
  es esmoquin ; smokin
  en smoking ; sigara içme ; ff:İngilizcede smoking giysi adı değildir; tuxedo veya dinner jacket denir
@redingot shared_ancestor
  fr redingote ; redingot
  en riding coat ; binici paltosu
  ru редингот [redingot] ; redingot
  it redingote ; redingot
@fötr shared_ancestor
  fr feutre ; keçe ; ff:Fransızca feutre genel olarak "keçe"
  en felt ; keçe
  de Filz ; keçe
  it feltro ; keçe
  ru фетр [fetr] ; keçe; fötr
@melon shared_ancestor
  fr melon ; kavun; melon şapka
  en melon ; kavun ; ff:İngilizcede melon yalnızca kavun; şapka için bowler denir
  it melone ; kavun
  de Melone ; kavun; melon şapka
@serpuş shared_ancestor
  fa سرپوش [sarpūş] ; kapak; başlık ; ff:Farsçada sarpūş "tencere kapağı" anlamı da taşır
  ur سرپوش [sarpoş] ; kapak ; ff:Urducada sarpoş "kapak"
@türban shared_ancestor
  fr turban ; türban
  en turban ; sarık
  it turbante ; sarık
  de Turban ; sarık
  ru тюрбан [tyurban] ; sarık
  es turbante ; sarık
  fa دلبند [dulband] ; sarık ; ff:Avrupa dillerindeki biçim Farsça dulband'dan Türkçe tülbent yoluyla gelir
@tülbent shared_ancestor
  fa دلبند [dulband] ; sarık bezi
  bg тюлбен [tyulben] ; tülbent
  el τουλπάνι [toulpáni] ; tülbent
  en tulip ; lale ; ff:İngilizce tulip de dulband'dan gelir; çiçek sarığa benzetilmiştir
  fr tulipe ; lale ; ff:Lale adı aynı sarık sözcüğünden türemiştir
@duvak shared_ancestor
  az duvaq ; duvak
  uz duvoq ; duvak
@nikap shared_ancestor
  ar نقاب [niqāb] ; yüz örtüsü
  fa نقاب [niqāb] ; maske; peçe
  ur نقاب [niqāb] ; peçe
  en niqab ; peçe
@samur shared_ancestor
  fa سمور [samūr] ; samur
  ar سمور [sammūr] ; samur
  az samur ; samur
  uz samur ; samur
@astragan shared_ancestor
  ru Астрахань [Astraxan'] ; Astrahan kenti ; ff:Kürk, Hazar kıyısındaki Astrahan kentinden ad alır
  fr astrakan ; astragan
  en astrakhan ; astragan
@botin shared_ancestor
  fr bottine ; kısa çizme
  ru ботинок [botinok] ; ayakkabı ; ff:Rusçada ботинок genel "ayakkabı"
@pençe shared_ancestor
  fa پنجه [panca] ; el; pençe; beş ; ff:Farsça panca "beş parmak, el" demektir
  az pəncə ; pençe
  uz panja ; pençe; parmaklar
  ur پنجہ [panja] ; pençe; el
@ökçe shared_ancestor
  kk өкше [ökşe] ; ökçe, topuk
  az ökçə ; ökçe
@vaketa shared_ancestor
  it vacchetta ; dana derisi
  es vaqueta ; vaketa
  fr vachette ; dana derisi
@rugan shared_ancestor
  fa روغن [rawġan] ; yağ ; ff:Farsçada rawġan "yağ"; Türkçede cilalı deriye kaymıştır
  ur روغن [rauġan] ; yağ ; ff:Urducada rauġan "yağ"
@süet shared_ancestor
  fr suède ; İsveç; süet ; ff:Fransızca "İsveç" adından; İsveç eldivenlerinden
  en suede ; süet
@debbağ shared_ancestor
  ar دباغ [dabbāġ] ; derici
  fa دباغ [dabbāġ] ; derici
  az dabbağ ; derici
  bg табак [tabak] ; derici ; ff:Türkçe tabak (derici) biçiminden; tütün anlamıyla karışmaz
  sr табак [tabak] ; derici
  sq tabak ; derici
@torna shared_ancestor
  it tornio ; torna
  es torno ; torna
  fr tour ; tur; torna ; ff:Fransızca tour hem "dönüş, tur" hem "torna"
  en turn ; dönmek
  el τόρνος [tórnos] ; torna ; ff:Sözcüğün en eski kaynağı Yunanca tórnos "pergel, torna"dır
@lehim shared_ancestor
  ar لحام [liḥām] ; kaynak, lehim
  az lehim ; lehim
@mihenk shared_ancestor
  ar محك [miḥakk] ; denek taşı
  az məhək ; mihenk
@mengene shared_ancestor
  el μάγγανο [mángano] ; mengene, bocurgat
  en mangonel ; mancınık ; ff:Aynı Yunanca mánganon'dan; Batı'da savaş makinesi anlamına kaymıştır
  it mangano ; pres, mengene
@takoz shared_ancestor
  el τάκος [tákos] ; takoz
@terazi shared_ancestor
  fa ترازو [tarāzū] ; terazi
  az tərəzi ; terazi
  uz tarozi ; terazi
  kk таразы [tarazı] ; terazi
  ur ترازو [tarāzū] ; terazi
  ka თარაზო [tarazo] ; su terazisi ; ff:Gürcücede tarazo "su terazisi, düzeç"
@şakul shared_ancestor
  ar شاقول [şāqūl] ; çekül
  az şaqul ; çekül
@mala shared_ancestor
  fa ماله [māle] ; mala
  az mala ; mala
  uz mola ; mala; tırmık
@zımpara shared_ancestor
  fa سنباده [sunbāde] ; zımpara
  az sumbata ; zımpara
  uz sumbata ; zımpara
@çark shared_ancestor
  fa چرخ [çarḫ] ; tekerlek; çark; gök
  az çarx ; çark
  uz charx ; çark; çıkrık
  ur چرخ [çarḫ] ; tekerlek
  kk шарық [şarıq] ; bileği çarkı
@mil shared_ancestor
  ar ميل [mīl] ; sürmelik çubuğu; mil
  az mil ; mil
  en mile ; mil (uzunluk) ; ff:Uzunluk ölçüsü olan mil Latince milia'dan, ayrı köktendir
@makara shared_ancestor
  fa بکره [bakra] ; makara
@dişli shared_ancestor
  az dişli ; dişli
  kk тісті [tisti] ; dişli
@kriko shared_ancestor
  it cricco ; kriko
  fr cric ; kriko
@vinç shared_ancestor
  en winch ; vinç
  de Winde ; vinç
@levye shared_ancestor
  fr levier ; kaldıraç
  en lever ; kaldıraç
  it leva ; kaldıraç
@rebap shared_ancestor
  ar رباب [rabāb] ; rebap
  fa رباب [rubāb] ; rebap
  ur رباب [rabāb] ; rebap
  es rabel ; ortaçağ yaylı çalgısı
  fr rebec ; ortaçağ kemanı
  en rebec ; ortaçağ kemanı
  az rübab ; rebap
  uz rubob ; rebap
@santur shared_ancestor
  fa سنتور [santūr] ; santur
  ar سنطور [sanṭūr] ; santur
  el σαντούρι [santoúri] ; santur
  en santur ; santur
@kopuz shared_ancestor
  az qopuz ; kopuz
  kk қобыз [qobız] ; kobız (yaylı çalgı)
  ky комуз [komuz] ; komuz (üç telli çalgı)
  uz qoʻbiz ; kopuz
  tk gopuz ; kopuz
  hu koboz ; ortaçağ lavtası ; ff:Macarcaya Kuman-Kıpçak dilinden geçmiştir
  ru кобза [kobza] ; kobza (telli çalgı)
  uk кобза [kobza] ; kobza
  pl kobza ; kobza; tulum ; ff:Lehçede kobza bazen "tulum çalgısı"
  ro cobză ; cobza (lavta)
@gayda into_turkish
  bg гайда [gayda] ; tulum
  mk гајда [gajda] ; tulum
  sr гајде [gajde] ; tulum
  sq gajde ; tulum
  el γκάιντα [gáida] ; tulum
  es gaita ; tulum (Galiçya) ; ff:İber gaita'sı ile Balkan gayda'sının ortak kökeni tartışmalıdır
@nakkare shared_ancestor
  ar نقارة [naqqāra] ; nakkare
  fa نقاره [naqqāre] ; nakkare
  en naker ; ortaçağ dümbeleği
  it nacchera ; kastanyet ; ff:İtalyanca nacchera "kastanyet" anlamına kaymıştır
  fr nacaire ; ortaçağ dümbeleği
  ur نقارہ [naqqāra] ; nakkare
  uz nogora ; nağara
  az nağara ; nağara
@kös shared_ancestor
  fa کوس [kūs] ; büyük davul
  ur کوس [kos] ; kös
@bendir shared_ancestor
  ar بندير [bandīr] ; bendir
@çalpara shared_ancestor
  fa چهارپاره [çahārpāra] ; dört parça ; ff:Farsçada "dört parça" anlamında; Türkçede çalgı adı olmuştur
@korno shared_ancestor
  it corno ; boynuz; korno ; ff:İtalyanca corno öncelikle "boynuz"
  fr cor ; korno
  en horn ; boynuz; korno
  de Horn ; boynuz; korno
@obua shared_ancestor
  fr hautbois ; obua ; ff:Fransızca "yüksek sesli odun" demektir
  en oboe ; obua
  it oboe ; obua
  de Oboe ; obua
@arp shared_ancestor
  fr harpe ; arp
  en harp ; arp
  de Harfe ; arp
  it arpa ; arp
  ru арфа [arfa] ; arp
@org shared_ancestor
  fr orgue ; org
  en organ ; organ; org ; ff:İngilizce organ hem beden organı hem çalgı
  de Orgel ; org
  it organo ; org; organ
  el όργανο [órgano] ; alet; organ; çalgı
  ru орган [organ] ; organ ; ff:Rusçada орган "organ"; çalgı için vurgu farklı: оргáн
@armonika shared_ancestor
  it armonica ; armonika
  en harmonica ; ağız mızıkası
  de Harmonika ; akordeon ; ff:Almanca Harmonika daha çok "akordeon"
  ru гармонь [garmon'] ; akordeon ; ff:Rusçada гармонь "akordeon"
@mızıka shared_ancestor
  it musica ; müzik ; ff:İtalyanca musica "müzik"; Türkçede ağız çalgısı adı olmuştur
  en music ; müzik
  fr musique ; müzik
  ru музыка [muzyka] ; müzik
  bg музика [muzika] ; müzik
  el μουσική [mousikí] ; müzik
@mandolin shared_ancestor
  it mandolino ; mandolin
  fr mandoline ; mandolin
  en mandolin ; mandolin
  ru мандолина [mandolina] ; mandolin
@cümbüş shared_ancestor
  fa جنبش [cunbiş] ; hareket, devinim ; ff:Farsçada cunbiş "hareket"; Türkçede eğlence ve çalgı
  az cümbüş ; eğlence
  uz jumbush ; hareket ; ff:Özbekçede jumbush "hareket, kıpırdama"
  ur جنبش [junbiş] ; hareket ; ff:Urducada junbiş "titreme, hareket"
@mızrap shared_ancestor
  ar مضراب [miḍrāb] ; mızrap
  fa مضراب [miżrāb] ; mızrap
  az mizrab ; mızrap
  uz mezrob ; mızrap
  ur مضراب [miżrāb] ; mızrap
@akort shared_ancestor
  fr accord ; anlaşma; akor ; ff:Fransızcada accord öncelikle "anlaşma"
  en accord ; anlaşma ; ff:İngilizcede accord "anlaşma"; müzik için chord/tuning
  it accordo ; anlaşma; akor
  de Akkord ; akor; parça başı ücret
  ru аккорд [akkord] ; akor
@köçek shared_ancestor
  fa کوچک [kūçak] ; küçük ; ff:Farsçada kūçak "küçük"; Türkçede erkek dansçı
  bg кючек [kyuček] ; göbek dansı ; ff:Bulgarcada кючек "oryantal dans" demektir
  mk ќочек [ḱoček] ; köçek dansı
  sq qoçek ; köçek
@çengi shared_ancestor
  fa چنگ [çang] ; çeng çalgısı; pençe
  az çəngi ; çengi
@dans shared_ancestor
  fr danse ; dans
  en dance ; dans
  it danza ; dans
  es danza ; dans
  de Tanz ; dans
  ru танец [tanets] ; dans
  bg танц [tants] ; dans
  pl taniec ; dans
  hu tánc ; dans
@vals shared_ancestor
  fr valse ; vals
  de Walzer ; vals ; ff:Almanca walzen "yuvarlanmak" eyleminden
  en waltz ; vals
  it valzer ; vals
  ru вальс [val's] ; vals
@tango shared_ancestor
  es tango ; tango
  en tango ; tango
  fr tango ; tango
  ru танго [tango] ; tango
@polka shared_ancestor
  pl polka ; Polonyalı kadın; polka ; ff:Lehçede polka öncelikle "Polonyalı kadın"
  fr polka ; polka
  en polka ; polka
  ru полька [pol'ka] ; polka; Polonyalı kadın
@balo shared_ancestor
  it ballo ; dans; balo
  fr bal ; balo
  en ball ; balo; top ; ff:İngilizce ball "top" ayrı köktendir
  ru бал [bal] ; balo
@balerin shared_ancestor
  fr ballerine ; balerin
  it ballerina ; dansçı kadın ; ff:İtalyancada ballerina her kadın dansçı
  en ballerina ; balerin
  ru балерина [balerina] ; balerin
@horon into_turkish
  el χορός [chorós] ; dans ; ff:Yunanca chorós genel "dans"; Türkçede Karadeniz oyunu
@zeybek from_turkish
  el ζεϊμπέκικο [zeïbékiko] ; zeybek dansı
@çiftetelli from_turkish
  el τσιφτετέλι [tsiftetéli] ; çiftetelli
  bg чифтетели [čifteteli] ; çiftetelli
@hoyrat into_turkish
  el χωριάτης [choriátis] ; köylü ; ff:Yunanca "köylü"; Türkçede kaba kimse ve halk ezgisi
@semai shared_ancestor
  ar سماعي [samāʿī] ; işitmeye dayalı
  fa سماعی [samāʿī] ; semai
@muganni shared_ancestor
  ar مغني [muġannī] ; şarkıcı
  fa مغنی [muġannī] ; şarkıcı
  az müğənni ; şarkıcı ; ff:Azerbaycancada müğənni günümüzde de "şarkıcı"
  ur مغنی [muġannī] ; şarkıcı
@meddah shared_ancestor
  ar مداح [maddāḥ] ; övücü
  fa مداح [maddāḥ] ; dinî övgü okuyan ; ff:Farsçada maddāḥ "dinî methiye okuyan"
  az məddah ; övücü
  ur مداح [maddāḥ] ; övücü
@müzisyen shared_ancestor
  fr musicien ; müzisyen
  en musician ; müzisyen
  it musicista ; müzisyen
  ru музыкант [muzykant] ; müzisyen
  de Musiker ; müzisyen
@solo shared_ancestor
  it solo ; yalnız; tek ; ff:İtalyanca solo "yalnız" sıfatı
  fr solo ; solo
  en solo ; solo
  es solo ; yalnız
  ru соло [solo] ; solo
@düet shared_ancestor
  it duetto ; düet
  fr duo ; düet
  en duet ; düet
  ru дуэт [duet] ; düet
  de Duett ; düet
@operet shared_ancestor
  it operetta ; operet
  fr opérette ; operet
  en operetta ; operet
  ru оперетта [operetta] ; operet
  de Operette ; operet
@sonat shared_ancestor
  it sonata ; sonat
  fr sonate ; sonat
  en sonata ; sonat
  ru соната [sonata] ; sonat
@konçerto shared_ancestor
  it concerto ; konser; konçerto ; ff:İtalyancada concerto hem konser hem konçerto
  fr concerto ; konçerto
  en concerto ; konçerto
  de Konzert ; konser; konçerto
  ru концерт [kontsert] ; konser ; ff:Rusçada концерт "konser"
@tempo shared_ancestor
  it tempo ; zaman; hava; tempo ; ff:İtalyanca tempo "zaman, hava durumu"
  fr tempo ; tempo
  en tempo ; tempo
  es tiempo ; zaman; hava ; ff:İspanyolca tiempo "zaman"
@oktav shared_ancestor
  fr octave ; oktav
  en octave ; oktav
  it ottava ; oktav
  ru октава [oktava] ; oktav
@repertuvar shared_ancestor
  fr répertoire ; repertuvar
  en repertoire ; repertuvar
  ru репертуар [repertuar] ; repertuvar
  de Repertoire ; repertuvar
@prova shared_ancestor
  it prova ; deneme; kanıt ; ff:İtalyanca prova "kanıt, deneme"
  es prueba ; kanıt; sınav
  fr preuve ; kanıt ; ff:Fransızca preuve yalnızca "kanıt"
  en proof ; kanıt
  ru проба [proba] ; deneme; ayar
@kulis shared_ancestor
  fr coulisse ; kulis; kayar kapı yuvası
  en coulisse ; kulis
  ru кулисы [kulisy] ; kulis
  de Kulisse ; sahne dekoru ; ff:Almanca Kulisse "sahne dekoru, arka plan"
@fasıl shared_ancestor
  ar فصل [faṣl] ; bölüm; mevsim ; ff:Arapçada faṣl "mevsim" anlamı yaygındır
  fa فصل [faṣl] ; mevsim; bölüm ; ff:Farsçada faṣl öncelikle "mevsim"
  ur فصل [faṣl] ; mevsim; ekin ; ff:Urducada faṣl "hasat, ekin"
  az fəsil ; mevsim; bölüm
  uz fasl ; mevsim
@peşrev shared_ancestor
  fa پیشرو [pīşrav] ; öncü, önde giden ; ff:Farsçada pīşrav "öncü, ilerici"
  ar بشرف [başraf] ; peşrev ; ff:Arap müziğine Türkçeden geçmiştir
@gazelhan shared_ancestor
  fa غزل‌خوان [ġazalḫvān] ; gazel okuyan
  ur غزل خواں [ġazal-ḫvāṉ] ; gazel okuyan
@berabere shared_ancestor
  fa برابر [barābar] ; eşit; karşı karşıya
  ur برابر [barābar] ; eşit; yanında ; ff:Urducada barābar "yan yana, sürekli" anlamları da taşır
  az bərabər ; eşit; birlikte
  uz barobar ; eşit; birlikte
@galip shared_ancestor
  ar غالب [ġālib] ; üstün gelen; çoğunlukla ; ff:Arapçada ġāliban "çoğunlukla" zarfı da yaygındır
  az qalib ; galip
  uz gʻolib ; galip
  ur غالب [ġālib] ; galip; baskın
  fa غالب [ġālib] ; baskın, çoğunluk
@mağlup shared_ancestor
  ar مغلوب [maġlūb] ; yenilmiş
  az məğlub ; mağlup
  uz magʻlub ; mağlup
  fa مغلوب [maġlūb] ; yenilmiş
@müsabaka shared_ancestor
  ar مسابقة [musābaqa] ; yarışma
  fa مسابقه [musābaqe] ; maç, yarışma ; ff:Farsçada spor karşılaşması için en yaygın sözcük
  az müsabiqə ; yarışma
  uz musobaqa ; yarışma
  ur مسابقہ [musābaqa] ; yarışma
@saha shared_ancestor
  ar ساحة [sāḥa] ; meydan; avlu
  fa ساحه [sāḥe] ; alan
  az sahə ; alan; bölge; sektör ; ff:Azerbaycancada sahə "bölge, sektör"
  uz soha ; alan; sektör ; ff:Özbekçede soha "sektör, bilim dalı"
@idman shared_ancestor
  ar إدمان [idmān] ; bağımlılık ; ff:Arapçada idmān "bağımlılık, düşkünlük"
  az idman ; spor ; ff:Azerbaycancada idman genel olarak "spor" demektir
  fa ادمان [idmān] ; bağımlılık
@maraton shared_ancestor
  el Μαραθώνας [Marathónas] ; Marathon ovası; maraton
  fr marathon ; maraton
  en marathon ; maraton
  ru марафон [marafon] ; maraton
  ar ماراثون [mārāthūn] ; maraton
@atletizm shared_ancestor
  fr athlétisme ; atletizm
  en athletics ; atletizm
  el αθλητισμός [athlitismós] ; spor ; ff:Yunanca athlitismós genel "spor"
  it atletica ; atletizm
  es atletismo ; atletizm
  ru атлетика [atletika] ; atletizm
@halter shared_ancestor
  fr haltère ; halter
  el αλτήρες [altíres] ; dambıl ; ff:Eski Yunanca haltḗres uzun atlamada kullanılan ağırlıklardı
  en halteres ; antik atlama ağırlıkları
@eskrim shared_ancestor
  fr escrime ; eskrim
  it scherma ; eskrim
  es esgrima ; eskrim
  pt esgrima ; eskrim
  en skirmish ; çatışma ; ff:İngilizce skirmish aynı Germen kökten "küçük çarpışma"
@maç shared_ancestor
  fr match ; maç
  en match ; maç; eş; kibrit ; ff:İngilizce match "kibrit" anlamı ayrı köktendir
  ru матч [matč] ; maç
  bg мач [mač] ; maç
  ro meci ; maç
  de Match ; maç
@rekor shared_ancestor
  fr record ; rekor
  en record ; kayıt; plak; rekor ; ff:İngilizce record öncelikle "kayıt"
  ru рекорд [rekord] ; rekor
  bg рекорд [rekord] ; rekor
  de Rekord ; rekor
  es récord ; rekor
  az rekord ; rekor
@rekortmen shared_ancestor
  fr recordman ; rekortmen ; ff:Fransızcada uydurulmuş sözde İngilizce biçim; İngilizcede record holder denir
  ru рекордсмен [rekordsmen] ; rekortmen
@amatör shared_ancestor
  fr amateur ; seven; amatör
  en amateur ; amatör
  it amatore ; seven; âşık ; ff:İtalyanca amatore "seven, hayran"
  ru любитель [lyubitel'] ; amatör; sever ; ff:Rusça çeviri yoluyla aynı kavram
@profesyonel shared_ancestor
  fr professionnel ; profesyonel
  en professional ; profesyonel
  ru профессионал [professional] ; profesyonel
  de Profi ; profesyonel
@briç shared_ancestor
  en bridge ; köprü; briç ; ff:İngilizce bridge "köprü"; oyun adının kökeni tartışmalı
  fr bridge ; briç
  ru бридж [bridž] ; briç
@poker shared_ancestor
  en poker ; poker
  fr poker ; poker
  ru покер [poker] ; poker
  de Poker ; poker
@bezik shared_ancestor
  fr bésigue ; bezik
  en bezique ; bezik
  ru безик [bezik] ; bezik
@tombala shared_ancestor
  it tombola ; tombala
  es tómbola ; tombala; çekiliş
  en tombola ; tombala
  bg томбола [tombola] ; tombala
  ro tombolă ; tombala
@loto shared_ancestor
  fr loto ; loto
  it lotto ; piyango ; ff:İtalyanca lotto "piyango"
  en lotto ; loto
  ru лото [loto] ; loto
  de Lotto ; piyango
@bilye shared_ancestor
  it biglia ; bilye
  fr bille ; bilye
  en billiards ; bilardo ; ff:Bilardo adı Fransızca bille "bilye"den türemiştir
@misket shared_ancestor
  it moschetto ; tüfek ; ff:Misket, tüfek saçmasından ad alır; İtalyanca moschetto "tüfek"
  fr mousquet ; tüfek
  en musket ; tüfek
@aşık shared_ancestor
  az aşıq ; aşık kemiği
  kk асық [asıq] ; aşık kemiği
  uz oshiq ; aşık kemiği
  tk aşyk ; aşık
  bg ашик [ašik] ; aşık kemiği
@kukla shared_ancestor
  el κούκλα [koúkla] ; oyuncak bebek; güzel kız ; ff:Yunanca koúkla "bebek"; Türkçede ipli oyuncak
  bg кукла [kukla] ; oyuncak bebek
  ru кукла [kukla] ; oyuncak bebek
  mk кукла [kukla] ; oyuncak bebek
  sq kukull ; oyuncak bebek
  en cowl ; başlık ; ff:Latince cuculla "başlık"tan; İngilizce cowl "keşiş başlığı"
@karagöz from_turkish
  el Καραγκιόζης [Karagiózis] ; gölge oyunu kahramanı
  bg карагьоз [karagyoz] ; soytarı ; ff:Bulgarcada карагьоз "palyaço, soytarı"
  sr карађоз [karađoz] ; soytarı
  sq karagjoz ; palyaço
  ro caraghios ; gülünç ; ff:Rumence caraghios "gülünç, komik" sıfatıdır
@akrobat shared_ancestor
  fr acrobate ; akrobat
  en acrobat ; akrobat
  el ακροβάτης [akrovátis] ; akrobat
  ru акробат [akrobat] ; akrobat
  it acrobata ; akrobat
@lunapark shared_ancestor
  en Luna Park ; Coney Island eğlence parkı ; ff:Bir özel ad genel ada dönüşmüştür
  it luna park ; lunapark
  ru луна-парк [luna-park] ; lunapark
  el λούνα παρκ [loúna park] ; lunapark
@trapez shared_ancestor
  fr trapèze ; yamuk; trapez
  en trapeze ; trapez
  el τραπέζι [trapézi] ; masa ; ff:Yunanca trapézi "masa"; trapézio "yamuk"
  ru трапеция [trapetsiya] ; yamuk; trapez
@kispet shared_ancestor
  ar كسوة [kiswa] ; giysi; Kâbe örtüsü ; ff:Arapçada kiswa "örtü, giysi"; Türkçede güreşçi donu
@pinpon shared_ancestor
  en ping-pong ; masa tenisi
  ru пинг-понг [ping-pong] ; masa tenisi
  fr ping-pong ; masa tenisi
@badminton shared_ancestor
  en Badminton ; Gloucestershire'daki köşk ; ff:Oyun, Badminton House'dan ad alır
  ru бадминтон [badminton] ; badminton
  fr badminton ; badminton
@hokey shared_ancestor
  en hockey ; hokey
  ru хоккей [xokkey] ; hokey
  fr hockey ; hokey
  de Hockey ; hokey
@ragbi shared_ancestor
  en rugby ; ragbi ; ff:Rugby okulundan ad alır
  ru регби [regbi] ; ragbi
  fr rugby ; ragbi
@beyzbol shared_ancestor
  en baseball ; beyzbol
  ru бейсбол [beysbol] ; beyzbol
  es béisbol ; beyzbol
@boksör shared_ancestor
  fr boxeur ; boksör
  en boxer ; boksör; bokser köpeği ; ff:İngilizce boxer bir köpek cinsinin de adıdır
  ru боксёр [boksyor] ; boksör
  de Boxer ; boksör
@karate shared_ancestor
  en karate ; karate
  ru каратэ [karate] ; karate
  fr karaté ; karate
@judo shared_ancestor
  en judo ; judo
  ru дзюдо [dzyudo] ; judo
  fr judo ; judo
@yüzmek shared_ancestor
  az üzmək ; yüzmek
  kk жүзу [jüzw] ; yüzmek
  uz suzmoq ; yüzmek
  ky сүзүү [süzüü] ; yüzmek
  tk ýüzmek ; yüzmek
@dalgıç shared_ancestor
  az dalğıc ; dalgıç
@paten shared_ancestor
  fr patin ; paten
  it pattino ; paten
  es patín ; paten
@motosiklet shared_ancestor
  fr motocyclette ; motosiklet
  en motorcycle ; motosiklet
  ru мотоцикл [mototsikl] ; motosiklet
@ralli shared_ancestor
  en rally ; toplanma; ralli ; ff:İngilizce rally "miting, toplanma" anlamı da taşır
  fr rallye ; ralli
  ru ралли [ralli] ; ralli
@okçu shared_ancestor
  az oxçu ; okçu
@jokey shared_ancestor
  en jockey ; jokey
  fr jockey ; jokey
  ru жокей [žokey] ; jokey
  de Jockey ; jokey
@turnuva shared_ancestor
  fr tournoi ; turnuva
  en tournament ; turnuva
  it torneo ; turnuva
  es torneo ; turnuva
  de Turnier ; turnuva
  ru турнир [turnir] ; turnuva
@şampiyona shared_ancestor
  fr championnat ; şampiyona
  en championship ; şampiyona
  ru чемпионат [čempionat] ; şampiyona
  bg шампионат [šampionat] ; şampiyona
  es campeonato ; şampiyona
  it campionato ; şampiyona
@puan shared_ancestor
  fr point ; nokta; puan
  en point ; nokta; puan
  it punto ; nokta; puan
  es punto ; nokta; puan
  ru пункт [punkt] ; madde; nokta ; ff:Rusça пункт "madde, nokta"; puan için очко
@stat shared_ancestor
  fr stade ; stadyum; aşama
  en stadium ; stadyum
  el στάδιο [stádio] ; stadyum; aşama ; ff:Yunanca stádio "aşama" anlamında da yaygındır
  ru стадион [stadion] ; stadyum
  it stadio ; stadyum; evre
@pist shared_ancestor
  fr piste ; pist; iz
  it pista ; pist; iz
  en piste ; kayak pisti
  es pista ; pist; ipucu ; ff:İspanyolca pista "ipucu" anlamı da taşır
@kort shared_ancestor
  en court ; mahkeme; avlu; kort ; ff:İngilizce court öncelikle "mahkeme, avlu"
  ru корт [kort] ; kort
  fr court ; kort
@ring shared_ancestor
  en ring ; halka; yüzük; ring ; ff:İngilizce ring "halka, yüzük"
  de Ring ; yüzük; halka ; ff:Almanca Ring "yüzük"
  ru ринг [ring] ; ring
  fr ring ; ring
@sprint shared_ancestor
  en sprint ; sprint
  ru спринт [sprint] ; sprint
  fr sprint ; sprint
@krampon shared_ancestor
  fr crampon ; çengel; krampon
  en crampon ; dağcı kramponu
  de Krampe ; kanca
@raket shared_ancestor
  fr raquette ; raket
  en racket ; raket; gürültü ; ff:İngilizce racket "gürültü, dolandırıcılık" ayrı köktendir
  it racchetta ; raket
  ar راحة [rāḥa] ; avuç içi ; ff:Raket sözcüğünün kaynağı Arapça rāḥa "avuç içi"dir
  ru ракетка [raketka] ; raket
@olimpik shared_ancestor
  fr olympique ; olimpik
  en Olympic ; olimpik
  el ολυμπιακός [olympiakós] ; olimpik
  ru олимпийский [olimpiyskiy] ; olimpik
@tekme shared_ancestor
  az təpik ; tekme
  kk тепкі [tepki] ; tekme
  uz tepki ; tekme
  ky тепки [tepki] ; tekme
@kapışmak shared_ancestor
  az qapışmaq ; kapışmak
@tepmek shared_ancestor
  az təpmək ; tepmek
  kk тебу [tebw] ; tepmek
  uz tepmoq ; tepmek
  ky тебүү [tebüü] ; tepmek
  tk depmek ; tepmek
@yumruklamak shared_ancestor
  az yumruqlamaq ; yumruklamak
  kk жұдырықтау [judırıqtaw] ; yumruklamak
@kağnı shared_ancestor
  kk қаңлы [qaŋlı] ; Kanglı boyu ; ff:Kazakçada qaŋlı bir boy adıdır; arabayla bağlantısı tartışılır
@landon shared_ancestor
  fr landau ; landon
  en landau ; landon
  de Landau ; Landau kenti; landon arabası
  ru ландо [lando] ; landon
@yaba shared_ancestor
  az yaba ; yaba
  tk ýaba ; yaba
@dirgen shared_ancestor
  az dırmıq ; tırmık ; ff:Azerbaycanca dırmıq "tırmık"; dirgen için yaba
@arabacı from_turkish
  bg арабаджия [arabadžiya] ; arabacı
  sr арабаџија [arabadžija] ; arabacı
  mk арабаџија [arabadžija] ; arabacı
  ro arabagiu ; arabacı
  sq arabaxhi ; arabacı
@kuyumculuk shared_ancestor
  az zərgərlik ; kuyumculuk ; ff:Azerbaycanca Farsça zargar "altın işleyen"den
@telkâri shared_ancestor
  az telkari ; telkâri
@hakkâk shared_ancestor
  ar حكاك [ḥakkāk] ; kazıyıcı
  az həkkak ; hakkâk
@savat shared_ancestor
  ar سواد [sawād] ; karalık; kalabalık ; ff:Arapçada sawād "siyahlık; kırsal halk"
  az savad ; savat; okuryazarlık ; ff:Azerbaycancada savad "okuryazarlık" anlamına kaymıştır
  uz savod ; okuryazarlık ; ff:Özbekçede savod "okuryazarlık"
@külhan shared_ancestor
  fa گلخن [gulḫan] ; hamam ocağı
  az külxan ; külhan
@kurna into_turkish
  el κρουνός [krounós] ; musluk, çeşme ; ff:Yunanca krounós "çeşme, musluk"; Türkçede hamam teknesi
@kurna from_turkish
  bg курна [kurna] ; kurna
  mk курна [kurna] ; kurna
@tellak shared_ancestor
  ar دلاك [dallāk] ; ovucu
  bg теляк [telyak] ; tellak
  mk тељак [teljak] ; tellak
@natır shared_ancestor
  ar ناطور [nāṭūr] ; bekçi ; ff:Arapçada nāṭūr "bağ bekçisi"; Türkçede hamam görevlisi
@peştemal shared_ancestor
  fa پشت‌مال [puştmāl] ; sırt havlusu
  bg пещемал [peštemal] ; peştemal
  mk пештемал [peštemal] ; peştemal
  el πεστεμάλι [pestemáli] ; peştemal
@lif shared_ancestor
  ar ليف [līf] ; lif; hurma lifi
  az lif ; lif
@küvet shared_ancestor
  fr cuvette ; küçük leğen; fotoğraf küveti ; ff:Fransızcada cuvette "küçük kap, çukur"; banyo küveti baignoire'dır
  en cuvette ; laboratuvar kabı ; ff:İngilizcede cuvette yalnızca laboratuvar kabı
  ru кювет [kyuvet] ; yol hendeği ; ff:Rusçada кювет "yol kenarı hendeği"
@sifon shared_ancestor
  fr siphon ; sifon
  en siphon ; sifon
  el σίφων [sífon] ; sifon
  ru сифон [sifon] ; sifon
@kenef shared_ancestor
  ar كنيف [kanīf] ; tuvalet
  bg кенеф [kenef] ; tuvalet
  mk кенеф [kenef] ; tuvalet
@ustura shared_ancestor
  fa استره [ustura] ; ustura
  uz ustara ; ustura
  ur استرا [ustrā] ; ustura
  kk ұстара [ustara] ; ustura
  ky устара [ustara] ; ustura
@tıraş shared_ancestor
  fa تراش [tarāş] ; yontma; kesme
  ur تراش [tarāş] ; kesim; biçim ; ff:Urducada tarāş "elbise kesimi, biçim"
  uz tarosh ; tıraş
  az təraş ; tıraş
@perçem shared_ancestor
  fa پرچم [parçam] ; bayrak ; ff:Farsçada parçam "bayrak" anlamına kaymıştır
  az pərçəm ; bayrak ; ff:Azerbaycancada pərçəm "bayrak"
  uz parcham ; bayrak ; ff:Özbekçede parcham "bayrak"
  ur پرچم [parçam] ; bayrak
@kâkül shared_ancestor
  fa کاکل [kākul] ; kâkül
  az kakil ; kâkül
  uz kokil ; kâkül
  ur کاکل [kākul] ; kâkül
@zülüf shared_ancestor
  fa زلف [zulf] ; zülüf
  az zülf ; zülüf
  uz zulf ; zülüf
  ur زلف [zulf] ; zülüf
@firkete shared_ancestor
  it forchetta ; çatal ; ff:İtalyanca forchetta "yemek çatalı"
  fr fourchette ; çatal ; ff:Fransızca fourchette "çatal"
@rimel shared_ancestor
  fr Rimmel ; Eugène Rimmel'in markası ; ff:Marka adı genel ada dönüşmüştür
  it rimmel ; rimel
  es rímel ; rimel
  pt rímel ; rimel
@esans shared_ancestor
  fr essence ; öz; benzin ; ff:Fransızcada essence "benzin" anlamı yaygındır
  en essence ; öz
  it essenza ; öz
  ru эссенция [essentsiya] ; esans
@ıtır shared_ancestor
  ar عطر [ʿiṭr] ; parfüm
  fa عطر [ʿaṭr] ; parfüm
  az ətir ; parfüm
  uz atir ; parfüm
  ur عطر [ʿitr] ; parfüm
@pomat shared_ancestor
  fr pommade ; pomat
  en pomade ; pomat
  ru помада [pomada] ; ruj ; ff:Rusçada помада "ruj"
  bg помада [pomada] ; pomat
@bıyık shared_ancestor
  az bığ ; bıyık
@topuz shared_ancestor
  az topuz ; topuz
  kk тобық [tobıq] ; aşık kemiği ; ff:Kazakça tobıq "bilek kemiği"
@sauna shared_ancestor
  en sauna ; sauna
  de Sauna ; sauna
  ru сауна [sauna] ; sauna
  fr sauna ; sauna
@musluk from_turkish
  bg муслук [musluk] ; musluk
  mk муслук [musluk] ; musluk
@mangal shared_ancestor
  ar منقل [manqal] ; mangal
  bg мангал [mangal] ; mangal
  sr мангал [mangal] ; mangal
  sq mangall ; mangal
  ro mangal ; mangal; odun kömürü ; ff:Rumence mangal "odun kömürü" anlamına kaymıştır
  el μαγκάλι [mangáli] ; mangal
  mk мангал [mangal] ; mangal
  ru мангал [mangal] ; kebap ızgarası ; ff:Rusçada мангал "şiş kebabı ızgarası"
  uk мангал [mangal] ; kebap ızgarası
@kepçe shared_ancestor
  fa کفچه [kafçe] ; kepçe
  az çömçə ; kepçe ; ff:Azerbaycanca farklı bir Farsça sözcük kullanır
  bg кепче [kepče] ; kepçe
  sq kepçe ; kepçe
@orak shared_ancestor
  az oraq ; orak
  kk орақ [oraq] ; orak
  uz oʻroq ; orak
  ky орок [orok] ; orak
  tk orak ; orak
@kaftan shared_ancestor
  fa خفتان [ḫaftān] ; kaftan
  bg кафтан [kaftan] ; kaftan
  sr кафтан [kaftan] ; kaftan
  ro caftan ; kaftan
  el καφτάνι [kaftáni] ; kaftan
  hu kaftán ; kaftan
  ru кафтан [kaftan] ; kaftan
  uk каптан [kaptan] ; kaftan
  pl kaftan ; kaftan; deli gömleği ; ff:Lehçede kaftan bezpieczeństwa "deli gömleği"
  fr caftan ; kaftan
  en caftan ; kaftan
  sq kaftan ; kaftan
@bilezik shared_ancestor
  az bilərzik ; bilezik
  kk білезік [bilezik] ; bilezik
  uz bilaguzuk ; bilezik
  ky билерик [bilerik] ; bilezik
  tk bilezik ; bilezik
  bg белезици [belezitsi] ; kelepçe ; ff:Bulgarcada белезици "kelepçe" anlamına kaymıştır
  sr белензуке [belenzuke] ; bilezik; kelepçe
  mk белегзија [belegzija] ; bilezik
  sq byzylyk ; bilezik
@tambur shared_ancestor
  fa تنبور [tanbūr] ; tambur
  ar طنبور [ṭunbūr] ; tambur
  el ταμπουράς [tambourás] ; tambura
  bg тамбура [tambura] ; tambura
  sr тамбура [tambura] ; tambura ; ff:Sırp halk çalgısı tamburica aynı addan türer
  mk тамбура [tambura] ; tambura
  hu tambura ; tambura
  it tamburo ; davul ; ff:İtalyanca tamburo "davul"; aynı Farsça kaynaktan
  fr tambour ; davul ; ff:Fransızca tambour "davul"
  en tambourine ; tef ; ff:İngilizce tambourine "tef"
@def shared_ancestor
  ar دف [daff] ; def
  fa دف [daf] ; def
  sr деф [def] ; def
  sq def ; def
  el ντέφι [défi] ; def
  mk деф [def] ; def
@tavla shared_ancestor
  it tavola ; masa; tahta ; ff:İtalyanca tavola "masa"; oyun adı tahtadan gelir
  el τάβλι [távli] ; tavla
  bg табла [tabla] ; tavla
  ro table ; tavla
  mk табла [tabla] ; tavla
  sq tavëll ; tavla
  ar طاولة [ṭāwila] ; masa; tavla ; ff:Arapçada ṭāwila "masa"; tavla için de kullanılır
@tezgâh shared_ancestor
  fa دستگاه [dastgāh] ; aygıt; düzenek; makam dizisi ; ff:Farsçada dastgāh "aygıt; klasik müzik makamı"
  bg тезгях [tezgyah] ; tezgâh
  sr тезга [tezga] ; pazar tezgâhı ; ff:Sırpçada tezga "pazar sergisi"
  mk тезга [tezga] ; tezgâh
  sq tezgë ; tezgâh
  ro tejghea ; tezgâh
@leğen shared_ancestor
  fa لگن [lagan] ; leğen
  bg леген [legen] ; leğen
  sr леђен [leđen] ; leğen
  mk леген [legen] ; leğen
  sq legen ; leğen
  ro lighean ; leğen
  el λεκάνη [lekáni] ; leğen; havza ; ff:Farsça lagan Yunanca lekánē'den gelir; aynı kök
@sahan shared_ancestor
  ar صحن [ṣaḥn] ; tabak; avlu ; ff:Arapçada ṣaḥn "tabak; cami avlusu"
  bg сахан [sahan] ; sahan
  sr сахан [sahan] ; sahan
  mk сахан [sahan] ; sahan
  sq sahan ; sahan
  el σαχάνι [saháni] ; sahan
@kevgir shared_ancestor
  fa کفگیر [kafgīr] ; köpük alan; kevgir
  bg кевгир [kevgir] ; kevgir
  az kəfkir ; kevgir
@havan shared_ancestor
  fa هاون [hāvan] ; havan
  bg хаван [havan] ; havan
  sr аван [avan] ; havan
  mk аван [avan] ; havan
  sq havan ; havan
  el χαβάνι [chaváni] ; havan
  az həvəng ; havan
@fırın shared_ancestor
  el φούρνος [foúrnos] ; fırın
  it forno ; fırın
  fr four ; fırın
  es horno ; fırın
  ar فرن [furn] ; fırın
  bg фурна [furna] ; fırın
  sr фуруна [furuna] ; fırın
  sq furrë ; fırın
  mk фурна [furna] ; fırın
@fener shared_ancestor
  el φανάρι [fanári] ; fener
  bg фенер [fener] ; fener
  sr фењер [fenjer] ; fener
  sq fener ; fener
  mk фенер [fener] ; fener
  ro felinar ; fener
  ru фонарь [fonar'] ; fener ; ff:Rusçaya doğrudan Yunancadan geçmiştir
@kova from_turkish
  bg кофа [kofa] ; kova
  sr кофа [kofa] ; kova
  mk кофа [kofa] ; kova
  sq kovë ; kova
@iğne shared_ancestor
  az iynə ; iğne
  kk ине [ine] ; iğne
  uz igna ; iğne
  ky ийне [iyne] ; iğne
  tk iňňe ; iğne
@makas shared_ancestor
  ar مقص [miqaṣṣ] ; makas
  sr маказе [makaze] ; makas
  mk макази [makazi] ; makas
  bg макас [makas] ; makas
@düğüm shared_ancestor
  az düyün ; düğüm
  kk түйін [tüyin] ; düğüm
  uz tugun ; düğüm
  ky түйүн [tüyün] ; düğüm
  tk düwün ; düğüm
@testere shared_ancestor
  fa دست‌اره [dastarra] ; el testeresi
  bg тестер [tester] ; testere
  sr тестера [testera] ; testere
  mk тестера [testera] ; testere
@rende shared_ancestor
  fa رنده [rande] ; rende
  bg ренде [rende] ; rende
  sr ренде [rende] ; rende
  mk ренде [rende] ; rende
  sq rende ; rende
  ro rindea ; rende
@keser from_turkish
  bg кесер [keser] ; keser
  sr кесер [keser] ; keser
  mk кесер [keser] ; keser
@tırpan into_turkish
  el δρεπάνι [drepáni] ; orak; tırpan
@matkap shared_ancestor
  ar مثقب [miṯqab] ; matkap
  az matqab ; matkap
@pense shared_ancestor
  fr pince ; kıskaç; pense
  it pinza ; pense
  es pinza ; mandal; pense
  en pincers ; kerpeten
  de Pinzette ; cımbız ; ff:Almanca Pinzette "cımbız"
@kilit shared_ancestor
  fa کلید [kilīd] ; anahtar ; ff:Farsçada kilīd "anahtar" demektir
  el κλειδί [kleidí] ; anahtar ; ff:Yunanca kleidí "anahtar"; kaynak sözcük
  ar إقليد [iqlīd] ; anahtar
  az kilid ; kilit
  uz kalit ; anahtar ; ff:Özbekçede kalit "anahtar"
  kk кілт [kilt] ; anahtar ; ff:Kazakçada kilt "anahtar"
@zincir shared_ancestor
  fa زنجیر [zancīr] ; zincir
  bg синджир [sindžir] ; zincir
  sr синџир [sindžir] ; zincir
  mk синџир [sindžir] ; zincir
  sq zinxhir ; zincir
  ur زنجیر [zanjīr] ; zincir
  az zəncir ; zincir
  uz zanjir ; zincir
@kanca shared_ancestor
  it gancio ; kanca
  es gancho ; kanca
  sr канџа [kandža] ; pençe ; ff:Sırpçada kandža "pençe, tırnak"
@çengel shared_ancestor
  fa چنگال [çangāl] ; çatal; pençe ; ff:Farsçada çangāl "yemek çatalı"
  az çəngəl ; çatal ; ff:Azerbaycancada çəngəl "yemek çatalı"
  bg ченгел [čengel] ; çengel
  sr ченгеле [čengele] ; çengel
  sq çengel ; çengel
  mk ченгел [čengel] ; çengel
  el τσιγκέλι [tsingéli] ; çengel
@saban shared_ancestor
  ru сабан [saban] ; pulluk (ağız)
@çini shared_ancestor
  fa چینی [çīnī] ; Çin işi; porselen
  ar صيني [ṣīnī] ; Çin işi
  ur چینی [çīnī] ; şeker ; ff:Urducada çīnī "şeker" demektir
  en china ; porselen
@boya shared_ancestor
  az boya ; boya
  kk бояу [boyaw] ; boya
  uz boʻyoq ; boya
  ky боёк [boyok] ; boya
  tk boýag ; boya
  bg боя [boya] ; boya
  sr боја [boja] ; renk ; ff:Sırpçada boja "renk" demektir
  mk боја [boja] ; renk; boya
  sq bojë ; boya
  ro boia ; kırmızı biber tozu ; ff:Rumence boia "toz biber"
  el μπογιά [bogiá] ; boya
@deri shared_ancestor
  az dəri ; deri
  kk тері [teri] ; deri
  uz teri ; deri
  ky тери [teri] ; deri
  tk deri ; deri
@kumaş shared_ancestor
  ar قماش [qumāş] ; kumaş
  ru кумач [kumač] ; kırmızı pamuklu ; ff:Rusçada кумач "kızıl bayrak bezi"
  uk кумач [kumač] ; kırmızı pamuklu
  az qumaş ; kumaş
@bez shared_ancestor
  az bez ; bez
  kk бөз [böz] ; bez
  uz boʻz ; bez
  ky бөз [böz] ; bez
  tk biz ; bez
  ru бязь [byaz'] ; kaba pamuklu
@pamuk shared_ancestor
  fa پنبه [panba] ; pamuk
  az pambıq ; pamuk
  bg памук [pamuk] ; pamuk
  sr памук [pamuk] ; pamuk
  mk памук [pamuk] ; pamuk
  sq pambuk ; pamuk
  hu pamut ; pamuk
  el μπαμπάκι [bambáki] ; pamuk ; ff:Yunancaya Bizans döneminde aynı kaynaktan geçmiştir
@yün shared_ancestor
  az yun ; yün
  kk жүн [jün] ; yün
  uz jun ; yün
  ky жүн [jün] ; yün
  tk ýüň ; yün
@keten shared_ancestor
  ar كتان [kattān] ; keten
  fa کتان [katān] ; keten
  he כותנה [kutna] ; pamuk ; ff:İbranice kutna "pamuk"; aynı Sami kökten
  az kətan ; keten
  uz kanop ; kenevir; keten
@atlas shared_ancestor
  ar أطلس [aṭlas] ; atlas; düz ; ff:Arapçada aṭlas "düz, tüysüz" sıfatı; harita atlası ayrı köktendir
  fa اطلس [aṭlas] ; atlas
  ru атлас [atlas] ; saten
  pl atłas ; saten
  bg атлаз [atlaz] ; atlas
  hu atlasz ; saten
  de Atlas ; saten
@saten into_turkish
  fr satin ; saten
  en satin ; saten
  ar زيتوني [zaytūnī] ; Zeytun (Quanzhou) kumaşı ; ff:Saten adı Çin'deki Zeytun limanından gelir
@şerit shared_ancestor
  ar شريط [şarīṭ] ; şerit; bant; kaset ; ff:Arapçada şarīṭ "kaset, film şeridi"
@kopça into_turkish
  bg копче [kopče] ; düğme ; ff:Bulgarcada копче "düğme"
  sr копча [kopča] ; toka, klips
  mk копче [kopče] ; düğme
@kemer shared_ancestor
  fa کمر [kamar] ; bel ; ff:Farsçada kamar "bel"; kemer için kamarband
  az kəmər ; kemer
  uz kamar ; kemer
  bg кемер [kemer] ; para kemeri
  el κεμέρι [keméri] ; para kemeri
  ro chimir ; para kemeri
@börk shared_ancestor
  az börk ; börk
  kk бөрік [börik] ; kürk başlık
  uz boʻrk ; börk
  ky бөрк [börk] ; börk
@şapka shared_ancestor
  ru шапка [šapka] ; şapka
  bg шапка [šapka] ; şapka
  pl czapka ; şapka
  uk шапка [šapka] ; şapka
  fr chapeau ; şapka
@kasket shared_ancestor
  fr casquette ; kasket
  bg каскет [kasket] ; kasket
  ru кепка [kepka] ; kasket ; ff:Rusça biçim Fransızca képi'den gelir
@yemeni shared_ancestor
  ar يمني [yamanī] ; Yemenli
  bg еминия [eminiya] ; yemeni ayakkabı
  sr јеменија [jemenija] ; yemeni
  sq jemeni ; yemeni
@gömlek shared_ancestor
  az köynək ; gömlek
  kk көйлек [köylek] ; elbise ; ff:Kazakçada көйлек "kadın elbisesi"
  uz koʻylak ; elbise ; ff:Özbekçede koʻylak "elbise; gömlek"
  ky көйнөк [köynök] ; elbise ; ff:Kırgızcada көйнөк "elbise"
  tk köýnek ; gömlek
@pantolon shared_ancestor
  fr pantalon ; pantolon
  it pantalone ; pantolon ; ff:Commedia dell'arte'deki Pantalone karakterinden
  en pantaloons ; bol pantolon (eski)
  bg панталон [pantalon] ; pantolon
  ro pantalon ; pantolon
  ru панталоны [pantalony] ; kadın iç çamaşırı ; ff:Rusçada панталоны "kadın külotu"
@etek shared_ancestor
  az ətək ; etek
  kk етек [etek] ; etek
  uz etak ; etek
  ky этек [etek] ; etek
  tk etek ; etek
@elbise shared_ancestor
  ar ألبسة [albisa] ; giysiler ; ff:Arapçada albisa libās'ın çoğuludur; Türkçede tekil
  fa البسه [albisa] ; giysiler
@ceket shared_ancestor
  fr jaquette ; ceket
  en jacket ; ceket
  bg жакет [žaket] ; ceket
  ru жакет [žaket] ; kadın ceketi
  it giacchetta ; ceket
  ar جاكيت [jākīt] ; ceket
@palto shared_ancestor
  fr paletot ; palto
  ru пальто [pal'to] ; palto
  bg палто [palto] ; palto
  it paltò ; palto
  ar بالطو [bālṭū] ; palto
  uz palto ; palto
@manto shared_ancestor
  fr manteau ; manto; palto
  it manto ; pelerin ; ff:İtalyanca manto "pelerin, örtü"
  en mantle ; pelerin; örtü
  ru манто [manto] ; kürk manto
  ar مانطو [mānṭū] ; manto
@şal shared_ancestor
  fa شال [şāl] ; şal
  en shawl ; şal
  fr châle ; şal
  ru шаль [šal'] ; şal
  ar شال [şāl] ; şal
  hu sál ; atkı
  ur شال [şāl] ; şal
@şal from_turkish
  sq shall ; şal
  bg шал [šal] ; şal
  ro șal ; şal
  sr шал [šal] ; şal
@nalın shared_ancestor
  ar نعلين [naʿlayn] ; iki nal; nalın ; ff:Arapçada "iki nal" anlamında ikil biçim
  bg налъми [nalămi] ; nalın
  sr нануле [nanule] ; nalın
  sq nallane ; nalın
@takunya into_turkish
  el τακούνι [takoúni] ; topuk, ökçe ; ff:Yunanca takoúni "ayakkabı topuğu"
@kundura shared_ancestor
  el κουντούρα [koundoúra] ; kundura
  bg кундури [kunduri] ; kundura
  sr кондуре [kondure] ; kundura
  sq kondura ; kundura
@bot shared_ancestor
  fr botte ; çizme
  en boot ; çizme
  ru боты [boty] ; galoş, bot
@sandalet shared_ancestor
  fr sandale ; sandalet
  en sandal ; sandalet
  el σανδάλι [sandáli] ; sandalet
  ar صندل [ṣandal] ; sandalet
  fa صندل [ṣandal] ; sandalet
@ayakkabı shared_ancestor
  az ayaqqabı ; ayakkabı
  tk aýakgap ; ayakkabı
  kk аяқ киім [ayaq kiyim] ; ayak giyimi ; ff:Kazakça "ayak giyimi" ile kurulmuştur
@gerdanlık shared_ancestor
  fa گردن [gardan] ; boyun ; ff:Farsça gardan "boyun"; Türkçe -lık ekiyle takı adı
  bg гердан [gerdan] ; kolye
  sr ђердан [đerdan] ; kolye
  mk ѓердан [ǵerdan] ; kolye
  sq gjerdan ; kolye
@kolye into_turkish
  fr collier ; kolye; tasma ; ff:Fransızcada collier "köpek tasması" anlamı da taşır
  en collar ; yaka; tasma ; ff:İngilizce collar "yaka, tasma"
  it collana ; kolye
@broş into_turkish
  fr broche ; broş; şiş ; ff:Fransızcada broche "kebap şişi" anlamı da taşır
  en brooch ; broş
@tespih shared_ancestor
  ar تسبيح [tasbīḥ] ; Allah'ı anma ; ff:Arapçada tasbīḥ "tesbih çekme eylemi"; nesne için misbaḥa
  sr теспих [tespih] ; tespih
  sq tespihe ; tespih
  az təsbeh ; tespih
  uz tasbeh ; tespih
@mercan shared_ancestor
  ar مرجان [marcān] ; mercan
  fa مرجان [marcān] ; mercan
  az mərcan ; mercan
  uz marjon ; mercan; boncuk
  kk маржан [marjan] ; inci; boncuk ; ff:Kazakçada маржан "inci, boncuk"
  el μαργαριτάρι [margaritári] ; inci ; ff:Arapça marcān Yunanca margarítēs "inci"den gelir
@pudra shared_ancestor
  fr poudre ; toz; pudra ; ff:Fransızca poudre "toz, barut"
  en powder ; toz; pudra
  it polvere ; toz
  es polvo ; toz
  ru пудра [pudra] ; pudra
@tarak shared_ancestor
  az daraq ; tarak
  kk тарақ [taraq] ; tarak
  uz taroq ; tarak
  ky тарак [tarak] ; tarak
  tk darak ; tarak
@ayna shared_ancestor
  fa آینه [āyine] ; ayna
  az ayna ; ayna
  uz oyna ; pencere; cam ; ff:Özbekçede oyna "pencere, cam" anlamına da gelir
  kk айна [ayna] ; ayna
  ky айнек [aynek] ; cam; pencere ; ff:Kırgızcada айнек "cam, pencere"
  tk aýna ; ayna; pencere
  ur آئینہ [āʾīna] ; ayna
@sabun shared_ancestor
  ar صابون [ṣābūn] ; sabun
  fr savon ; sabun
  it sapone ; sabun
  es jabón ; sabun
  el σαπούνι [sapoúni] ; sabun
  bg сапун [sapun] ; sabun
  sr сапун [sapun] ; sabun
  ro săpun ; sabun
  hu szappan ; sabun
  az sabun ; sabun
  uz sovun ; sabun
  kk сабын [sabın] ; sabun
  ky самын [samın] ; sabun
  tk sabyn ; sabun
  ur صابن [ṣābun] ; sabun
  de Seife ; sabun
  en soap ; sabun
@havlu from_turkish
  bg хавлия [havliya] ; havlu
  mk хавлија [havlija] ; havlu
@bağlama from_turkish
  sq bagllama ; bağlama
@ud shared_ancestor
  ar عود [ʿūd] ; ağaç, odun; ud ; ff:Arapçada ʿūd öncelikle "odun, dal"
  fa عود [ʿūd] ; ud; öd ağacı
  el ούτι [oúti] ; ud
  es laúd ; lavta
  fr luth ; lavta
  en lute ; lavta
  it liuto ; lavta
  de Laute ; lavta
  pt alaúde ; lavta
@kanun shared_ancestor
  ar قانون [qānūn] ; yasa; kanun çalgısı
  fa قانون [qānūn] ; yasa; kanun çalgısı
  el κανονάκι [kanonáki] ; kanun çalgısı
@kemençe shared_ancestor
  fa کمانچه [kamānçe] ; kemençe
  el κεμεντζές [kementzés] ; Pontus kemençesi
  bg кеменче [kemenče] ; kemençe
  mk ќемене [ḱemene] ; kemençe
  sq qemane ; keman
@keman shared_ancestor
  fa کمان [kamān] ; yay ; ff:Farsçada kamān "ok yayı"; çalgı için vīyolon
  ur کمان [kamān] ; yay
  sr ћемане [ćemane] ; keman
  bg кемане [kemane] ; keman
  az kaman ; yay; keman
@darbuka shared_ancestor
  ar دربكة [darbukka] ; darbuka
  bg тарамбука [tarambuka] ; darbuka
  sr дарабука [darabuka] ; darbuka
  mk тарабука [tarabuka] ; darbuka
@makam shared_ancestor
  ar مقام [maqām] ; yer, durak; makam
  fa مقام [maqām] ; yer; mevki; makam
  ur مقام [maqām] ; yer ; ff:Urducada maqām öncelikle "yer, konum"
  bg макам [makam] ; makam
  sq makam ; makam
  el μακάμι [makámi] ; makam
  az məqam ; makam; an
  uz maqom ; makam ; ff:Özbek klasik müziği Shashmaqom aynı sözcükle adlanır
@usul shared_ancestor
  ar أصول [uṣūl] ; kökler; esaslar ; ff:Arapçada uṣūl, aṣl'ın çoğulu; Türkçede tekil yöntem
  fa اصول [uṣūl] ; ilkeler
  az üsul ; yöntem
  uz usul ; yöntem
@nağme shared_ancestor
  ar نغمة [naġma] ; nağme
  fa نغمه [naġme] ; nağme
  ur نغمہ [naġma] ; şarkı
  az nəğmə ; nağme, şarkı
@melodi shared_ancestor
  fr mélodie ; melodi
  en melody ; melodi
  el μελωδία [melodía] ; melodi
  it melodia ; melodi
  de Melodie ; melodi
  ru мелодия [melodiya] ; melodi
@ritim shared_ancestor
  el ρυθμός [rythmós] ; ritim
  fr rythme ; ritim
  en rhythm ; ritim
  ru ритм [ritm] ; ritim
@nota shared_ancestor
  it nota ; not; nota
  fr note ; not; nota
  en note ; not; nota
  ru нота [nota] ; nota; diplomatik nota
@beste shared_ancestor
  fa بسته [basta] ; bağlanmış; paket ; ff:Farsçada basta "kapalı, bağlı; paket"
  az bəstə ; beste
  ur بستہ [basta] ; demet; paket ; ff:Urducada basta "çanta, paket"
@güfte shared_ancestor
  fa گفته [gufta] ; söylenmiş söz ; ff:Farsçada gufta "söylenen"
  az güftə ; güfte
@şarkı shared_ancestor
  ar شرقي [şarqī] ; doğulu ; ff:Arapçada şarqī "doğulu" sıfatıdır; Türkçede şarkı
  fa شرقی [şarqī] ; doğulu
@gazel shared_ancestor
  ar غزل [ġazal] ; aşk sözü; gazel
  fa غزل [ġazal] ; gazel
  ur غزل [ġazal] ; gazel
  az qəzəl ; gazel
  uz gʻazal ; gazel
  en ghazal ; gazel
@oyun shared_ancestor
  az oyun ; oyun
  kk ойын [oyın] ; oyun
  uz oʻyin ; oyun
  ky оюн [oyun] ; oyun
  tk oýun ; oyun
@satranç shared_ancestor
  fa شطرنج [şaṭranc] ; satranç
  ar شطرنج [şaṭranc] ; satranç
  ur شطرنج [şaṭranj] ; satranç
  az şahmat ; satranç ; ff:Azerbaycancada Rusça yoluyla şahmat
  ru шахматы [šaxmaty] ; satranç ; ff:Rusça biçim Farsça şāh māt "şah öldü"den gelir
  es ajedrez ; satranç ; ff:Arapça aş-şaṭranc'dan
  pt xadrez ; satranç
@dama shared_ancestor
  fr dames ; kadınlar; dama ; ff:Fransızca jeu de dames "kadınlar oyunu"
  it dama ; hanım; dama
  es damas ; dama
  bg дама [dama] ; dama
@pul shared_ancestor
  fa پول [pūl] ; para ; ff:Farsçada pūl "para"
  az pul ; para ; ff:Azerbaycancada pul "para"
  uz pul ; para ; ff:Özbekçede pul "para"
  kk пұл [pul] ; para
  ky пул [pul] ; para
  tk pul ; para
  bg пул [pul] ; oyun pulu
  el πούλι [poúli] ; oyun pulu; kuş ; ff:Yunanca poúli hem "kuş" hem "oyun taşı"
  sq pullë ; pul
@güreş shared_ancestor
  az güləş ; güreş
  kk күрес [küres] ; güreş
  uz kurash ; güreş
  ky күрөш [küröş] ; güreş
  tk göreş ; güreş
@sepet shared_ancestor
  fa سبد [sabad] ; sepet
  sr сепет [sepet] ; sepet
  mk сепет [sepet] ; sepet
  bg сепет [sepet] ; sepet
@torba shared_ancestor
  fa توبره [tōbre] ; yem torbası
  bg торба [torba] ; torba
  sr торба [torba] ; çanta ; ff:Sırpçada torba "el çantası"
  mk торба [torba] ; çanta
  sq torbë ; torba
  ru торба [torba] ; yem torbası
  uk торба [torba] ; torba
  pl torba ; çanta ; ff:Lehçede torba günlük "çanta" sözcüğüdür
@çuval shared_ancestor
  fa جوال [cuvāl] ; çuval
  bg чувал [čuval] ; çuval
  mk чувал [čuval] ; çuval
  el τσουβάλι [tsouváli] ; çuval
  az çuval ; çuval
@heybe shared_ancestor
  ar حقيبة [ḥaqība] ; çanta; bavul ; ff:Arapçada ḥaqība genel "çanta, valiz"
  az heybə ; heybe
@bavul shared_ancestor
  it baule ; bavul
  es baúl ; sandık
  pt baú ; sandık
  el μπαούλο [baoúlo] ; sandık
@kanepe shared_ancestor
  fr canapé ; kanepe; küçük sandviç ; ff:Fransızcada canapé "kanepe" ve "kanepe sandviç"
  en canopy ; tente, gölgelik ; ff:İngilizce canopy "gölgelik"; Yunanca kōnōpeîon "cibinlik"ten
  it canapè ; kanepe
  el καναπές [kanapés] ; kanepe
@koltuk shared_ancestor
  az qoltuq ; koltuk altı ; ff:Azerbaycancada qoltuq "koltuk altı"
  kk қолтық [qoltıq] ; koltuk altı ; ff:Kazakçada қолтық "koltuk altı"
  uz qoʻltiq ; koltuk altı
  ky колтук [koltuk] ; koltuk altı
  tk goltuk ; koltuk altı
@divan shared_ancestor
  fa دیوان [dīvān] ; defter; meclis; şiir kitabı
  ar ديوان [dīwān] ; daire; meclis; divan
  en divan ; divan
  fr divan ; divan
  ru диван [divan] ; kanepe
  bg диван [divan] ; kanepe
  sr диван [divan] ; kanepe; harika ; ff:Sırpçada divan sıfat olarak "harika" demektir
  ro divan ; kanepe
  hu dívány ; kanepe
  pl dywan ; halı ; ff:Lehçede dywan "halı" anlamına kaymıştır
  uk диван [divan] ; kanepe
  it divano ; kanepe
  es diván ; divan
@karyola shared_ancestor
  it carriola ; el arabası ; ff:İtalyanca carriola "el arabası"; tekerlekli yatak anlamından
  el καριόλα [karióla] ; karyola
@sandalye shared_ancestor
  ar صندلية [ṣandaliyya] ; sandal ağacından iskemle
@masa shared_ancestor
  ro masă ; masa
  it mensa ; yemekhane ; ff:İtalyanca mensa "yemekhane"
  es mesa ; masa
  pt mesa ; masa
  bg маса [masa] ; masa
  mk маса [masa] ; masa
@hasır shared_ancestor
  ar حصير [ḥaṣīr] ; hasır
  sr асура [asura] ; hasır
  mk асура [asura] ; hasır
  sq hasër ; hasır
@bohça shared_ancestor
  az boğça ; bohça
  uz boʻgʻcha ; bohça
  bg бохча [bohča] ; bohça
  sr бошча [bošča] ; bohça
  mk бовча [bovča] ; bohça
  sq boçe ; bohça
  ro boccea ; bohça
@bardak shared_ancestor
  az bardaq ; testi, çömlek ; ff:Azerbaycancada bardaq "testi"
  bg бардак [bardak] ; genelev; kargaşa ; ff:Bulgarcada бардак "genelev, dağınıklık"
  ru бардак [bardak] ; kargaşa ; ff:Rusçada бардак "dağınıklık, kaos"
  uk бардак [bardak] ; kargaşa
  el μπαρδάκι [bardáki] ; küçük testi
  sr бардак [bardak] ; testi
  mk бардак [bardak] ; testi
@tas shared_ancestor
  fa طاس [ṭās] ; tas
  ar طاس [ṭās] ; tas
  bg тас [tas] ; tas
  sr тас [tas] ; terazi kefesi ; ff:Sırpçada tas "terazi kefesi"
  mk тас [tas] ; tas
  sq tas ; tas
  ro tas ; tas
  el τάσι [tási] ; tas
  fr tasse ; fincan ; ff:Fransızca tasse "fincan"
  de Tasse ; fincan
  it tazza ; fincan
  es taza ; fincan
@tabak shared_ancestor
  ar طبق [ṭabaq] ; tepsi; kat; tabaka ; ff:Arapçada ṭabaq "kat, tabaka; tepsi"
  fa طبق [ṭabaq] ; tepsi; kat
  kk табақ [tabaq] ; büyük tahta tabak
  uz tovoq ; tabak
  ky табак [tabak] ; tabak
@cezve shared_ancestor
  ar جذوة [caḏwa] ; kor, ateş parçası ; ff:Arapçada caḏwa "kor"; kap anlamı Türkçede gelişmiştir
  bg джезве [džezve] ; cezve
  sr џезва [džezva] ; cezve
  mk џезве [džezve] ; cezve
  sq xhezve ; cezve
  hu dzsezva ; cezve
  az cəzvə ; cezve
  ru джезва [džezva] ; cezve
@semaver shared_ancestor
  ru самовар [samovar] ; semaver ; ff:Rusça "kendi kaynayan" demektir
  bg самовар [samovar] ; semaver
  az samovar ; semaver
  uz samovar ; semaver
  kk самаурын [samawrın] ; semaver
  fa سماور [samāvar] ; semaver
  en samovar ; semaver
  ar سماور [samāwar] ; semaver
@sürahi shared_ancestor
  ar صراحي [ṣurāḥī] ; sürahi
  fa صراحی [ṣurāḥī] ; sürahi
  ur صراحی [ṣurāḥī] ; sürahi
  az sürahi ; sürahi
@kaşık shared_ancestor
  az qaşıq ; kaşık
  kk қасық [qasıq] ; kaşık
  uz qoshiq ; kaşık
  ky кашык [kaşık] ; kaşık
  sr кашика [kašika] ; kaşık ; ff:Sırpçada kašika kaşığın tek adıdır
@satır shared_ancestor
  ar ساطور [sāṭūr] ; satır
  bg сатър [satăr] ; satır
  sr сатара [satara] ; satır
  mk сатар [satar] ; satır
  sq satër ; satır
  ro satâr ; satır
@merdane shared_ancestor
  fa مردانه [mardāna] ; erkeğe özgü ; ff:Farsçada mardāna "erkekçe"; Türkçede silindir alet
@terzi shared_ancestor
  fa درزی [darzī] ; terzi
  bg терзия [terziya] ; terzi
  sr терзија [terzija] ; terzi
  mk терзија [terzija] ; terzi
  sq terzi ; terzi
  el τερζής [terzís] ; terzi
@marangoz shared_ancestor
  el μαραγκός [marangós] ; marangoz
  it marangone ; karabatak; marangoz (eski) ; ff:İtalyanca marangone "karabatak kuşu"; dalgıçtan ustaya
  bg марангоз [marangoz] ; marangoz
@dülger shared_ancestor
  fa درودگر [durūdgar] ; dülger
  bg дюлгер [dyulger] ; dülger
  sr дунђер [dunđer] ; dülger
  mk дунѓер [dunǵer] ; dülger
  sq dylgjer ; dülger
  ro dulgher ; dülger
  el ντουλγκέρης [doulgéris] ; dülger
@sarraf shared_ancestor
  ar صراف [ṣarrāf] ; sarraf
  fa صراف [ṣarrāf] ; sarraf
  bg сараф [saraf] ; sarraf
  sr сараф [saraf] ; sarraf
  sq sarraf ; sarraf
  ro zaraf ; sarraf
  el σαράφης [saráfis] ; sarraf
  ur صراف [ṣarrāf] ; sarraf
  az sərraf ; sarraf
@iplik shared_ancestor
  az iplik ; iplik
  kk жіп [jip] ; ip
  uz ip ; ip
  ky жип [jip] ; ip
  tk ýüp ; ip
@kazık shared_ancestor
  az qazıq ; kazık
  kk қазық [qazıq] ; kazık
  uz qoziq ; kazık
  ky казык [kazık] ; kazık
  tk gazyk ; kazık
@kama shared_ancestor
  az qama ; kama
  ru кама [kama] ; kama (hançer) ; ff:Rusçaya Kafkas dillerinden geçmiş hançer adı
@sırça shared_ancestor
  az sırça ; cam
"""
