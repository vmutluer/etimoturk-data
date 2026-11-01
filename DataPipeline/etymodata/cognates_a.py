# -*- coding: utf-8 -*-
"""Uluslarla ortak sözcükler – bölüm A (Türkçeden dünyaya yayılanlar: Turcisms).

DSL:
  @lemma direction            -> direction: from_turkish | into_turkish | shared_ancestor
    code foreign [roman] ; meaning ; ff:not   (roman ve ff isteğe bağlı)
"""

COGNATES_A = r"""
@yoğurt from_turkish
  en yogurt ; yoğurt
  fr yaourt ; yoğurt
  de Joghurt ; yoğurt
  it yogurt ; yoğurt
  es yogur ; yoğurt
  el γιαούρτι [giaoúrti] ; yoğurt
  bg йогурт [yogurt] ; yoğurt
  sr јогурт [jogurt] ; yoğurt
  sq jogurt ; yoğurt
  ro iaurt ; yoğurt
  mk јогурт [jogurt] ; yoğurt
  hu joghurt ; yoğurt
  ru йогурт [yogurt] ; yoğurt
  uk йогурт [yohurt] ; yoğurt
  pl jogurt ; yoğurt
  ar ياغورت [yāġūrt] ; yoğurt (Levant ve Mağrip'te)
  az qatıq ; yoğurt ; ff:Azerbaycan'da "yoğurt" yerine qatıq kullanılır; yoğurt ise süzme yoğurt anlamına kayar
  kk қатық [qatıq] ; yoğurt benzeri süt ürünü
@köşk from_turkish
  en kiosk ; büfe, küçük satış kulübesi ; ff:İngilizcede "kiosk" bahçe köşkü değil, gazete/bilet kulübesi anlamına kaymıştır
  fr kiosque ; büfe, gazete kulübesi ; ff:Fransızcada bahçe köşkü yerine satış kulübesi anlamındadır
  de Kiosk ; büfe ; ff:Almancada küçük satış dükkânı anlamındadır
  it chiosco ; büfe, köşk
  es quiosco ; büfe
  el κιόσκι [kióski] ; köşk, büfe
  bg кьошк [kyoşk] ; köşk, çardak
  sr ћошак [ćošak] ; köşe ; ff:Sırpçada ćošak "köşe" anlamına kaymıştır
  ro chioșc ; büfe
  ru киоск [kiosk] ; büfe
  pl kiosk ; büfe
  hu kioszk ; büfe
  fa کوشک [kūşk] ; köşk, saray
@kayık from_turkish
  en caique ; Boğaz kayığı
  fr caïque ; kayık
  it caicco ; kayık
  el καΐκι [kaíki] ; kayık, tekne
  bg каик [kaik] ; kayık
  sr кајак [kajak] ; kano
  ro caic ; kayık
  ru каик [kaik] ; kayık
@divan shared_ancestor
  en divan ; sedir; divan (kurul)
  fr divan ; sedir
  de Diwan ; sedir; şiir divanı
  it divano ; kanepe
  es diván ; sedir
  el ντιβάνι [divāni] ; sedir
  bg диван [divan] ; kanepe
  sr диван [divan] ; kanepe; muhteşem ; ff:Sırpçada divan aynı zamanda "harika, muhteşem" anlamında sıfattır
  sq divan ; kanepe
  ro divan ; sedir; divan (kurul)
  hu dívány ; kanepe
  ru диван [divan] ; kanepe
  uk диван [dyvan] ; kanepe
  pl dywan ; halı ; ff:Lehçede dywan "halı" anlamına kaymıştır
  fa دیوان [dīvān] ; defter, şiir kitabı, daire
  ar ديوان [dīwān] ; daire, kurul, şiir divanı
  ur دیوان [dīvān] ; şiir divanı
@börek from_turkish
  el μπουρέκι [mpouréki] ; börek
  bg бюрек [byurek] ; börek
  sr бурек [burek] ; börek
  sq byrek ; börek
  ro burec ; börek
  mk бурек [burek] ; börek
  hu burek ; börek
  ru бурек [burek] ; börek
  en burek ; Balkan böreği
  az börək ; börek
  kk бөрек [börek] ; börek
  ar بوريك [būrīk] ; börek (Mağrip)
@baklava from_turkish
  en baklava ; baklava
  fr baklava ; baklava
  de Baklava ; baklava
  it baklava ; baklava
  el μπακλαβάς [mpaklavás] ; baklava
  bg баклава [baklava] ; baklava
  sr баклава [baklava] ; baklava
  sq bakllava ; baklava
  ro baclava ; baklava
  mk баклава [baklava] ; baklava
  hu baklava ; baklava
  ru пахлава [pahlava] ; baklava
  uk пахлава [pahlava] ; baklava
  ar بقلاوة [baqlāwa] ; baklava
  fa باقلوا [bāqlavā] ; baklava
  az paxlava ; baklava
  uz paxlava ; baklava
  tk paklava ; baklava
@dolma from_turkish
  en dolma ; dolma
  el ντολμάς [dolmás] ; dolma
  bg долма [dolma] ; dolma
  sr долма [dolma] ; dolma
  sq dollma ; dolma
  ro dolma ; dolma
  ru долма [dolma] ; dolma
  ar دولمة [dōlma] ; dolma
  fa دلمه [dolme] ; dolma
  az dolma ; dolma
  hy տոլմա [tolma] ; dolma
  uz do'lma ; dolma
@şiş from_turkish
  en shish (kebab) ; şiş kebap
  fr chiche-kebab ; şiş kebap
  el σις κεμπάπ [sis kebáp] ; şiş kebap
  bg шиш [şiş] ; şiş
  sr шиш [šiš] ; şiş
  ro șiș ; şiş
  ru шиш [şiş] ; şiş; hiçbir şey ; ff:Rusçada "şiş" argoda "hiçbir şey, nanay" anlamına gelir
  ar شيش [şīş] ; şiş
@bergamot from_turkish
  en bergamot ; bergamot
  fr bergamote ; bergamot
  it bergamotto ; bergamot
  de Bergamotte ; bergamot
  es bergamota ; bergamot
  el περγαμόντο [pergamónto] ; bergamot
  ru бергамот [bergamot] ; bergamot
@turkuaz from_turkish
  en turquoise ; turkuaz (Türk taşı)
  fr turquoise ; turkuaz
  de Türkis ; turkuaz
  it turchese ; turkuaz
  es turquesa ; turkuaz
  ru бирюза [biryuza] ; turkuaz
  hu türkiz ; turkuaz
  pl turkus ; turkuaz
@çorba from_turkish
  el τσορβάς [tsorvás] ; çorba
  bg чорба [çorba] ; çorba
  sr чорба [čorba] ; çorba
  sq çorbë ; çorba
  ro ciorbă ; ekşili çorba
  mk чорба [čorba] ; çorba
  hu csorba ; çentik, kırık ; ff:Macarcada csorba "çentikli, kırık" anlamındadır; çorba için "leves" kullanılır
  ru шурпа [şurpa] ; et çorbası
  az şorba ; çorba
  kk сорпа [sorpa] ; et suyu
  uz sho'rva ; çorba
  tk çorba ; çorba
  ky шорпо [şorpo] ; çorba
  fa شوربا [şōrbā] ; çorba
  ar شوربة [şōrba] ; çorba
  ur شوربہ [şorba] ; çorba
@köfte shared_ancestor
  en kofta ; köfte
  el κεφτές [keftés] ; köfte
  bg кюфте [kyufte] ; köfte
  sr ћуфте [ćufte] ; köfte
  sq qofte ; köfte
  ro chiftea ; köfte
  mk ќофте [kjofte] ; köfte
  hu köfte ; köfte
  fa کوفته [kūfte] ; köfte
  ar كفتة [kufta] ; köfte
  ur کوفتہ [kofta] ; köfte
  az küftə ; köfte
  hy քյուֆթա [kyufta] ; köfte
@kebap shared_ancestor
  en kebab ; kebap
  fr kebab ; döner kebap
  de Kebab ; kebap
  el κεμπάπ [kebáp] ; kebap
  bg кебап [kebap] ; kebap
  sr ћевап [ćevap] ; köfte kebabı
  sq qebap ; kebap
  ro chebap ; kebap
  ru кебаб [kebab] ; kebap
  ar كباب [kabāb] ; kebap
  fa کباب [kabāb] ; kebap
  ur کباب [kabāb] ; kebap
  az kabab ; kebap
  uz kabob ; kebap
  hy քաբաբ [kabab] ; kebap
@pilav shared_ancestor
  en pilaf ; pilav
  fr pilaf ; pilav
  el πιλάφι [piláfi] ; pilav
  bg пилаф [pilaf] ; pilav
  sr пилав [pilav] ; pilav
  sq pilaf ; pilav
  ro pilaf ; pilav
  ru плов [plov] ; pilav
  uk плов [plov] ; pilav
  fa پلو [polow] ; pilav
  ar بيلاف [bīlāf] ; pilav
  ur پلاؤ [pulāo] ; pilav
  az plov ; pilav
  uz palov ; pilav
  kk палау [palau] ; pilav
  tk palaw ; pilav
  ky палоо [paloo] ; pilav
  hy փլավ [plav] ; pilav
@kaymak from_turkish
  en kaymak ; kaymak
  el καϊμάκι [kaïmáki] ; kaymak; kahve köpüğü
  bg каймак [kaymak] ; kaymak
  sr кајмак [kajmak] ; kaymak
  sq kajmak ; kaymak
  ro caimac ; kaymak
  ru каймак [kaymak] ; kaymak
  az qaymaq ; kaymak
  kk қаймақ [qaymaq] ; kaymak
  uz qaymoq ; kaymak
  ky каймак [kaymak] ; kaymak
  fa قیماق [qeymāq] ; kaymak
@ayran from_turkish
  en ayran ; ayran
  de Ayran ; ayran
  bg айрян [ayryan] ; ayran
  sr ајран [ajran] ; ayran
  sq ajran ; ayran
  mk ајран [ajran] ; ayran
  ru айран [ayran] ; ayran
  az ayran ; ayran
  kk айран [ayran] ; ayran
  ky айран [ayran] ; ayran
  uz ayron ; ayran
  tk aýran ; ayran
  fa آیران [āyrān] ; ayran
  ar عيران [ʿayrān] ; ayran
@pastırma from_turkish
  en pastrami ; pastırma
  ro pastramă ; pastırma
  bg пастърма [pastırma] ; pastırma
  sr пастрма [pastrma] ; pastırma
  el παστουρμάς [pastourmás] ; pastırma
  sq pastërma ; pastırma
  ru бастурма [basturma] ; pastırma
  hy բաստուրմա [basturma] ; pastırma
  ar بسطرمة [basṭirma] ; pastırma
@sucuk from_turkish
  bg суджук [sudjuk] ; sucuk
  sr суџук [sudžuk] ; sucuk
  el σουτζούκι [soutzoúki] ; sucuk; cevizli sucuk
  sq suxhuk ; sucuk
  ro sugiuc ; cevizli sucuk ; ff:Rumencede sugiuc genellikle tatlı cevizli sucuğu anlatır
  mk суџук [sudžuk] ; sucuk
  ru суджук [sudjuk] ; sucuk
  ar سجق [sucuq] ; sucuk
  hy սուջուխ [sujukh] ; cevizli sucuk
  az sucuq ; cevizli sucuk
@bulgur from_turkish
  en bulgur ; bulgur
  fr boulgour ; bulgur
  de Bulgur ; bulgur
  el πλιγούρι [pligoúri] ; bulgur
  bg булгур [bulgur] ; bulgur
  sr булгур [bulgur] ; bulgur
  ar برغل [burġul] ; bulgur
  hy բլղուր [blghur] ; bulgur
  ru булгур [bulgur] ; bulgur
@sarma from_turkish
  bg сарма [sarma] ; sarma
  sr сарма [sarma] ; sarma
  sq sarma ; sarma
  ro sarma ; sarma
  mk сарма [sarma] ; sarma
  hu szárma ; sarma
  el σαρμάς [sarmás] ; sarma
  ru сарма [sarma] ; sarma
  az sarma ; sarma
@tepsi from_turkish
  bg тепсия [tepsiya] ; tepsi
  sr тепсија [tepsija] ; tepsi
  sq tepsi ; tepsi
  ro tipsie ; tepsi
  mk тепсија [tepsija] ; tepsi
  el ταψί [tapsí] ; tepsi
  hu tepsi ; fırın tepsisi
  az təpsi ; tepsi
  kk тепсі [tepsi] ; tepsi
@kazan from_turkish
  bg казан [kazan] ; kazan
  sr казан [kazan] ; kazan
  sq kazan ; kazan
  ro cazan ; kazan
  mk казан [kazan] ; kazan
  el καζάνι [kazáni] ; kazan
  ru казан [kazan] ; kazan
  uk казан [kazan] ; kazan
  hu kazán ; kazan
  az qazan ; kazan
  kk қазан [qazan] ; kazan
  uz qozon ; kazan
  ky казан [kazan] ; kazan
  tk gazan ; kazan
@kaşık from_turkish
  sr кашика [kašika] ; kaşık
  bg кашик [kaşik] ; kaşık (ağız)
  sq kashik ; kaşık (ağız)
  mk кашика [kašika] ; kaşık
  ro cașic ; kepçe
  az qaşıq ; kaşık
  kk қасық [qasıq] ; kaşık
  uz qoshiq ; kaşık
  ky кашык [kaşık] ; kaşık
  tk çemçe ; kaşık ; ff:Türkmencede kaşık için çemçe kullanılır; "gaşyk" ise seyrektir
@çanak from_turkish
  el τσανάκι [tsanáki] ; çanak
  bg чанак [çanak] ; çanak
  sr чанак [čanak] ; çanak
  sq çanak ; çanak
  ro cionac ; çanak
  az çanaq ; çanak
  kk шанақ [şanaq] ; çanak
@bardak from_turkish
  ru бардак [bardak] ; karışıklık, dağınıklık ; ff:Rusçada bardak "kaos, dağınıklık" anlamına kaymıştır; su bardağı için "stakan" kullanılır
  uk бардак [bardak] ; karışıklık ; ff:Ukraynacada bardak "karmaşa" anlamındadır
  bg бардак [bardak] ; genelev (argo) ; ff:Bulgarcada bardak argoda genelev anlamına gelir
  sr бардак [bardak] ; testi, sürahi
  el μπαρδάκι [mpardáki] ; küçük sürahi
  az bardaq ; sürahi, testi ; ff:Azerbaycan Türkçesinde bardaq "testi"dir; içme bardağı için "stəkan" kullanılır
  pl bardak ; dağınıklık ; ff:Lehçede dağınıklık anlamındadır
@kaldırım from_turkish
  bg калдъръм [kaldırım] ; Arnavut kaldırımı, taş döşeme ; ff:Bulgarcada yalnızca taş döşemeli yol anlamındadır; yaya yolu için "trotoar" kullanılır
  sr калдрма [kaldrma] ; taş döşeme
  sq kalldrëm ; taş döşeme
  ro caldarâm ; taş döşeme
  mk калдрма [kaldrma] ; taş döşeme
  el καλντερίμι [kalderími] ; taş döşeme yol
@subay from_turkish
  az subay ; bekâr ; ff:Azerbaycan Türkçesinde subay "evli olmayan, bekâr" anlamındadır; subay için "zabit" kullanılır
  kk сыбай [sıbay] ; yakın, bitişik ; ff:Kazakçada sıbay "yakın, bitişik" anlamındadır
@kişi shared_ancestor
  az kişi ; erkek, adam ; ff:Azerbaycan Türkçesinde kişi "erkek" anlamındadır; "insan" için adam/insan kullanılır
  kk кісі [kisi] ; kişi, insan
  uz kishi ; kişi, insan
  ky киши [kişi] ; kişi, insan
  tk kişi ; kişi
@sümük shared_ancestor
  az sümük ; kemik ; ff:Azerbaycan Türkçesinde sümük "kemik" anlamındadır; Türkçedeki burun akıntısı anlamı yoktur
  kk сүйек [süyek] ; kemik
  tk süňk ; kemik
@pis shared_ancestor
  az pis ; kötü ; ff:Azerbaycan Türkçesinde pis "kötü" anlamındadır; "kirli" için çirkli kullanılır
  tk pis ; kötü
@kıç shared_ancestor
  az qıç ; bacak ; ff:Azerbaycan Türkçesinde qıç "bacak" anlamındadır
  tk gyç ; bacak
@düşmek shared_ancestor
  az düşmək ; düşmek; inmek ; ff:Azerbaycan Türkçesinde "avtobusdan düşmək" otobüsten inmek demektir
  kk түсу [tüsü] ; düşmek; inmek
  uz tushmoq ; düşmek; inmek
  ky түшүү [tüşüü] ; düşmek; inmek
  tk düşmek ; düşmek
@saklamak shared_ancestor
  az saxlamaq ; tutmak, muhafaza etmek ; ff:Azerbaycan Türkçesinde saxlamaq "durdurmak, tutmak" anlamındadır; gizlemek için gizlətmək kullanılır
  kk сақтау [saqtau] ; saklamak, korumak
  uz saqlamoq ; saklamak, korumak
  tk saklamak ; korumak
@yabancı shared_ancestor
  sr јабанџија [jabandžija] ; yabancı
  bg ябанджия [yabandjiya] ; yabancı, dışarıdan gelen
  sq jabanxhi ; yabancı
  az yabançı ; yabancı
@vişne shared_ancestor
  bg вишна [vişna] ; vişne
  sr вишња [višnja] ; vişne
  ro vișină ; vişne
  ru вишня [vişnya] ; vişne; kiraz ; ff:Rusçada vişnya hem vişneyi hem bazı bölgelerde kirazı karşılar
  uk вишня [vyşnya] ; vişne
  pl wiśnia ; vişne
  mk вишна [višna] ; vişne
  el βύσσινο [výssino] ; vişne
  sq vishnje ; vişne
  hu visnye ; vişne (ağız)
@durak into_turkish
  ru дурак [durak] ; aptal ; ff:Rusça durak (aptal) ile Türkçe durak arasında köken bağı yoktur; yalnızca ses benzerliğiyle "yalancı arkadaş"tır
  uk дурак [durak] ; aptal ; ff:Ses benzerliği; köken ilişkisi yok
  pl durak ; bir kâğıt oyunu ; ff:Lehçede Rusçadan alınmış oyun adı
@tabak into_turkish
  ru табак [tabak] ; tütün ; ff:Rusça tabak (tütün) Türkçe tabakla ses benzerliğinden ibarettir; köken bağı yoktur
  bg табак [tabak] ; tütün (ağız) ; ff:Köken ilişkisi yok
  pl tabaka ; enfiye ; ff:Köken ilişkisi yok
  ar طبق [ṭabaq] ; tabak, kat
  fa طبق [ṭabaq] ; tepsi; kat
  ur طبق [tabaq] ; tabak
@kulak shared_ancestor
  ru кулак [kulak] ; yumruk; zengin köylü ; ff:Rusça kulak (yumruk) ile Türkçe kulak arasında köken bağı yoktur
  uk кулак [kulak] ; yumruk ; ff:Köken ilişkisi yok
  az qulaq ; kulak
  kk құлақ [qulaq] ; kulak
  uz quloq ; kulak
  ky кулак [kulak] ; kulak
  tk gulak ; kulak
@kabak shared_ancestor
  ru кабак [kabak] ; meyhane ; ff:Rusça kabak "meyhane" demektir; Türkçe kabak (sebze) ile köken bağı kurulmaz
  az qabaq ; kabak; ön ; ff:Azerbaycan Türkçesinde qabaq aynı zamanda "ön, önce" anlamındadır
  kk қабақ [qabaq] ; göz kapağı; kabak ; ff:Kazakçada qabaq öncelikle "göz kapağı, kaş" anlamındadır
  uz qovoq ; kabak
  ky кабак [kabak] ; kabak
@merak into_turkish
  el μεράκι [meráki] ; tutku, bir işi ruhla yapma ; ff:Yunancada meraki "işini aşkla yapma" anlamına kaymıştır
  sr мерак [merak] ; keyif, zevk ; ff:Sırpçada merak "keyif, haz" anlamındadır
  bg мерак [merak] ; arzu, heves ; ff:Bulgarcada merak "heves, arzu" anlamındadır
  sq merak ; kaygı, endişe ; ff:Arnavutçada merak "endişe" anlamındadır
  mk мерак [merak] ; haz, heves
  ro merac ; heves
  ar مراق [marāq] ; kara sevda
@keyif into_turkish
  ro chef ; eğlence, parti; keyif ; ff:Rumencede chef "parti, eğlence" anlamına kaymıştır
  sr ћеф [ćef] ; keyif, heves
  bg кеф [kef] ; keyif, zevk
  sq qejf ; keyif
  el κέφι [kéfi] ; neşe, coşku
  mk ќеф [kjef] ; keyif
  ar كيف [kayf] ; durum; keyif
  fa کیف [keyf] ; keyif, zevk
  ur کیف [kaif] ; keyif, sarhoşluk
@rahat into_turkish
  ro rahat ; lokum; (kaba) dışkı ; ff:Rumencede "rahat" lokum anlamından argoda kaba bir anlama kaymıştır
  bg рахат [rahat] ; rahat, huzur
  sr рахат [rahat] ; rahat, huzurlu
  sq rehat ; rahat
  el ραχάτι [racháti] ; tembellik, rahatlık ; ff:Yunancada "rahati" tembellik çağrışımı taşır
  ar راحة [rāḥa] ; dinlenme, rahat
  fa راحت [rāḥat] ; rahat
  ur راحت [rāḥat] ; rahat
  az rahat ; rahat
@sanat into_turkish
  sr занат [zanat] ; zanaat, el işi ; ff:Sırpçada zanat "zanaat" anlamındadır; "sanat" için umetnost kullanılır
  bg занаят [zanayat] ; zanaat ; ff:Bulgarcada zanayat "el zanaatı" demektir
  sq zanat ; zanaat, meslek
  mk занает [zanaet] ; zanaat
  ro zanat ; zanaat (ağız)
  ar صنعة [ṣanʿa] ; zanaat, meslek
  fa صنعت [ṣanʿat] ; sanayi, endüstri ; ff:Farsçada san'at "endüstri" anlamındadır; sanat için "honar" kullanılır
  az sənət ; sanat; meslek
  uz san'at ; sanat
  kk өнер [öner] ; sanat ; ff:Kazakçada sanat için Türkçe "hüner"le akraba öner kullanılır
@çadır from_turkish
  bg чадър [çadır] ; şemsiye ; ff:Bulgarcada çadır "şemsiye" anlamına kaymıştır; çadır için "palatka" kullanılır
  sr шатор [šator] ; çadır
  sq çadër ; şemsiye; çadır ; ff:Arnavutçada çadër öncelikle şemsiye anlamındadır
  mk чадор [čador] ; şemsiye ; ff:Makedoncada şemsiye anlamındadır
  ro cort ; çadır ; ff:Rumence cort Latince kökenlidir; şator ağızlarda kalmıştır
  hu sátor ; çadır
  ru шатёр [şatyor] ; büyük çadır
  uk шатро [şatro] ; çadır
  pl szatra ; çingene çadırı
  el τσαντίρι [tsantíri] ; çadır
  az çadır ; çadır
  kk шатыр [şatır] ; çadır; çatı
  fa چادر [çādor] ; çarşaf, kadın örtüsü ; ff:Farsçada çador öncelikle kadınların bütün vücudu örten örtüsüdür
  ur چادر [çādar] ; şal, örtü
@cep into_turkish
  sr џеп [džep] ; cep
  bg джоб [djob] ; cep
  sq xhep ; cep
  mk џеб [džeb] ; cep
  el τσέπη [tsépi] ; cep
  hu zseb ; cep
  ro gebea ; cep (ağız)
  ar جيب [cayb] ; cep
  fa جیب [cīb] ; cep
  ur جیب [cēb] ; cep
  az cib ; cep
@cam into_turkish
  el τζάμι [tzámi] ; pencere camı
  sr џам [džam] ; cam
  bg джам [djam] ; pencere camı
  sq xham ; cam
  ro geam ; pencere camı
  mk џам [džam] ; cam
  fa جام [cām] ; kadeh ; ff:Farsçada cām "kadeh, kâse" anlamındadır; pencere camı için "şīşe" kullanılır
  ar جام [cām] ; kadeh
@cami into_turkish
  el τζαμί [tzamí] ; cami
  sr џамија [džamija] ; cami
  bg джамия [djamiya] ; cami
  sq xhami ; cami
  ro geamie ; cami
  mk џамија [džamija] ; cami
  hu dzsámi ; cami
  ar جامع [cāmiʿ] ; büyük cami
  fa جامع [cāmeʿ] ; toplayan; ulu cami
@pencere into_turkish
  sr пенџер [pendžer] ; pencere
  bg пенджера [pendjera] ; pencere (ağız)
  sq penxhere ; pencere
  mk пенџере [pendžere] ; pencere
  ro pengere ; pencere (ağız)
  fa پنجره [pancare] ; pencere
  ur پنجرہ [pincra] ; kafes ; ff:Urducada pincra "kuş kafesi" anlamındadır
  az pəncərə ; pencere
@dolap into_turkish
  el ντουλάπι [doulápi] ; dolap
  sr долап [dolap] ; su çarkı; dolap ; ff:Sırpçada dolap daha çok su çarkı anlamındadır
  bg долап [dolap] ; duvar dolabı
  sq dollap ; dolap
  ro dulap ; dolap
  mk долап [dolap] ; dolap
  ar دولاب [dūlāb] ; tekerlek; dolap ; ff:Arapçada dūlāb "tekerlek, çıkrık" anlamındadır
  fa دولاب [dūlāb] ; su çarkı
  az dolab ; dolap
@tavan into_turkish
  bg таван [tavan] ; tavan; tavan arası
  sr таван [tavan] ; tavan arası ; ff:Sırpçada tavan "çatı katı" anlamına kaymıştır
  sq tavan ; tavan
  ro tavan ; tavan
  mk таван [tavan] ; tavan arası
  el ταβάνι [taváni] ; tavan
  hu tavan ; tavan (ağız)
@kat from_turkish
  bg кат [kat] ; kat; tabaka
  sr кат [kat] ; kat
  sq kat ; kat
  mk кат [kat] ; kat
  el κατ [kat] ; kat (ağız)
  az qat ; kat, tabaka
  kk қат [qat] ; kat, tabaka
@çarşı into_turkish
  sr чаршија [čaršija] ; çarşı
  bg чаршия [çarşiya] ; çarşı
  sq çarshi ; çarşı
  mk чаршија [čaršija] ; çarşı
  el τσαρσί [tsarsí] ; çarşı
  ro cearșaf ; çarşaf ; ff:Rumence cearșaf "çarşaf"tır; çarşı ile karışmamalı
  fa چهارسو [çahārsū] ; dört yol, pazar
@dükkân into_turkish
  sr дућан [dućan] ; dükkân
  bg дюкян [dyukyan] ; dükkân
  sq dyqan ; dükkân
  mk дуќан [dukjan] ; dükkân
  ro dugheană ; dükkân, baraka ; ff:Rumencede dugheană "köhne dükkân" çağrışımlıdır
  el ντουκιάνι [doukiáni] ; dükkân (ağız)
  ar دكان [dukkān] ; dükkân
  fa دکان [dokkān] ; dükkân
  ur دکان [dukān] ; dükkân
  az dükan ; dükkân
  uz do'kon ; dükkân
  kk дүкен [düken] ; dükkân
@komşu from_turkish
  sr комшија [komšija] ; komşu
  bg комшия [komşiya] ; komşu
  sq komshi ; komşu
  mk комшија [komšija] ; komşu
  ro comșu ; komşu (ağız)
  el κομσού [komsoú] ; komşu (ağız)
  az qonşu ; komşu
  kk көрші [körşi] ; komşu
  uz qo'shni ; komşu
  ky коңшу [koñşu] ; komşu
  tk goňşy ; komşu
@sokak into_turkish
  sr сокак [sokak] ; sokak
  bg сокак [sokak] ; dar sokak
  sq sokak ; sokak
  mk сокак [sokak] ; sokak
  el σοκάκι [sokáki] ; dar sokak
  ro socac ; sokak (ağız)
  ar زقاق [zuqāq] ; dar sokak
@mahalle into_turkish
  sr махала [mahala] ; mahalle
  bg махала [mahala] ; mahalle
  sq mëhallë ; mahalle
  mk маало [maalo] ; mahalle
  ro mahala ; kenar mahalle, varoş ; ff:Rumencede mahala "varoş, yoksul mahalle" çağrışımı taşır
  el μαχαλάς [machalás] ; mahalle
  ar محلة [maḥalla] ; mahalle
  fa محله [maḥalle] ; mahalle
  ur محلہ [muhalla] ; mahalle
  az məhəllə ; mahalle
  uz mahalla ; mahalle
@pazar into_turkish
  el παζάρι [pazári] ; pazar; pazarlık
  bg пазар [pazar] ; pazar; alışveriş
  sr пазар [pazar] ; pazar; alışveriş
  sq pazar ; pazar
  ro bazar ; pazar
  mk пазар [pazar] ; pazar
  hu bazár ; pazar
  ru базар [bazar] ; pazar; gürültü ; ff:Rusçada bazar aynı zamanda "gürültü, kargaşa" anlamında kullanılır
  uk базар [bazar] ; pazar
  pl bazar ; pazar
  en bazaar ; doğu pazarı
  fr bazar ; pazar; dağınıklık ; ff:Fransızcada bazar "karmakarışık yer" anlamına da gelir
  it bazar ; pazar
  de Basar ; pazar
  fa بازار [bāzār] ; pazar
  ar بازار [bāzār] ; pazar
  ur بازار [bāzār] ; pazar
  az bazar ; pazar; pazar günü
  kk базар [bazar] ; pazar
  uz bozor ; pazar
  ky базар [bazar] ; pazar
  tk bazar ; pazar
  hy բազար [bazar] ; pazar
  ka ბაზარი [bazari] ; pazar
@çay shared_ancestor
  en chai ; baharatlı sütlü çay ; ff:İngilizcede chai yalnızca Hint usulü baharatlı çayı anlatır
  ru чай [çay] ; çay
  uk чай [çay] ; çay
  pl czaj ; demli çay (ağız)
  bg чай [çay] ; çay
  sr чај [čaj] ; çay
  sq çaj ; çay
  ro ceai ; çay
  mk чај [čaj] ; çay
  el τσάι [tsái] ; çay
  fa چای [çāy] ; çay
  ar شاي [şāy] ; çay
  ur چائے [çāe] ; çay
  az çay ; çay
  kk шай [şay] ; çay
  uz choy ; çay
  ky чай [çay] ; çay
  tk çaý ; çay
  hy թեյ [t'ey] ; çay ; ff:Ermenice tey Batı dillerindeki "tea" biçiminden gelir
  ka ჩაი [çai] ; çay
  pt chá ; çay
@kahve shared_ancestor
  en coffee ; kahve
  fr café ; kahve; kahvehane
  de Kaffee ; kahve
  it caffè ; kahve
  es café ; kahve
  el καφές [kafés] ; kahve
  bg кафе [kafe] ; kahve
  sr кафа [kafa] ; kahve
  sq kafe ; kahve
  ro cafea ; kahve
  mk кафе [kafe] ; kahve
  hu kávé ; kahve
  ru кофе [kofe] ; kahve
  uk кава [kava] ; kahve
  pl kawa ; kahve
  ar قهوة [qahwa] ; kahve
  fa قهوه [qahve] ; kahve
  ur قہوہ [qahva] ; kahve
  az qəhvə ; kahve
  kk кофе [kofe] ; kahve
  uz qahva ; kahve
  hy սուրճ [surch] ; kahve ; ff:Ermenicede kahve için farklı kökenli "surch" kullanılır
  ka ყავა [q'ava] ; kahve
@şeker shared_ancestor
  en sugar ; şeker
  fr sucre ; şeker
  de Zucker ; şeker
  it zucchero ; şeker
  es azúcar ; şeker
  el ζάχαρη [záchari] ; şeker
  bg захар [zahar] ; şeker
  sr шећер [šećer] ; şeker
  sq sheqer ; şeker
  ro zahăr ; şeker
  mk шеќер [šekjer] ; şeker
  hu cukor ; şeker
  ru сахар [sahar] ; şeker
  uk цукор [tsukor] ; şeker
  pl cukier ; şeker
  fa شکر [şakar] ; şeker
  ar سكر [sukkar] ; şeker
  ur شکر [şakar] ; şeker
  az şəkər ; şeker
  kk шекер [şeker] ; şeker
  uz shakar ; şeker
  ky шекер [şeker] ; şeker
  tk şeker ; şeker
  hy շաքար [shak'ar] ; şeker
  ka შაქარი [şakari] ; şeker
@cezve into_turkish
  en cezve ; cezve
  sr џезва [džezva] ; cezve
  bg джезве [djezve] ; cezve
  sq xhezve ; cezve
  mk џезве [džezve] ; cezve
  ro ibric ; cezve ; ff:Rumencede cezve için Türkçe "ibrik" kullanılır
  el τζεζβές [tzezvés] ; cezve
  hu dzsezva ; cezve
  ru джезва [cezva] ; cezve
  ar جذوة [caḏwa] ; kor, köz ; ff:Arapça caḏwa "yanan kor" anlamındadır; kahve kabı anlamı Türkçede gelişmiştir
@masa shared_ancestor
  ro masă ; masa; yemek
  bg маса [masa] ; masa
  sr маса [masa] ; kitle, yığın ; ff:Sırpçada masa "kitle, yığın" demektir; masa için "sto" kullanılır
  es mesa ; masa
  pt mesa ; masa
  it mensa ; yemekhane ; ff:İtalyancada mensa "yemekhane" anlamına kaymıştır; masa için tavolo kullanılır
  en mess ; askerî yemekhane ; ff:İngilizce mess (yemekhane) aynı Latince köktendir
  az masa ; masa
  ru масса [massa] ; kitle ; ff:Rusça massa (kitle) farklı Latince kökten gelir
@liman shared_ancestor
  el λιμάνι [limáni] ; liman
  bg лиман [liman] ; lagün, kıyı gölü ; ff:Bulgarcada liman "lagün" anlamındadır
  ro liman ; kıyı gölü, lagün; (mecazi) kurtuluş ; ff:Rumencede liman hem lagün hem de "sığınılan yer" anlamındadır
  ru лиман [liman] ; nehir ağzı gölü ; ff:Rusçada liman "haliç, lagün" anlamındadır
  uk лиман [lyman] ; haliç
  sr лиман [liman] ; haliç
  sq liman ; liman
  ar ليمان [līmān] ; liman; hapishane ; ff:Mısır Arapçasında līmān "zindan" anlamına kaymıştır
  az liman ; liman
  hu limány ; durgun su
@anahtar into_turkish
  el ανοιχτήρι [anoichtíri] ; açacak ; ff:Yunancada anoichtíri "şişe/konserve açacağı"dır; anahtar için kleidí kullanılır
  bg анахтар [anahtar] ; anahtar (ağız)
  sq anahtar ; anahtar (ağız)
  az açar ; anahtar ; ff:Azerbaycan Türkçesinde Türkçe "açar" kullanılır
  kk кілт [kilt] ; anahtar ; ff:Kazakça kilt Yunanca kleidí kökenli "kilit"le aynı kaynaktandır
  uz kalit ; anahtar
  ky ачкыч [açkıç] ; anahtar
@fırtına into_turkish
  it fortuna ; şans, talih; (eski) deniz fırtınası ; ff:İtalyanca fortuna "şans" demektir; fırtına anlamı denizcilik dilinde kalmıştır
  el φουρτούνα [fourtoúna] ; fırtına
  bg фъртуна [fırtuna] ; fırtına
  sr фортуна [fortuna] ; fırtına (ağız); talih
  sq furtunë ; fırtına
  ro furtună ; fırtına
  en fortune ; servet, şans ; ff:İngilizce fortune "şans, servet" demektir; aynı Latince kökten
  fr fortune ; servet, şans
  es fortuna ; şans, servet
  az fırtına ; fırtına
@sabun shared_ancestor
  en soap ; sabun
  fr savon ; sabun
  de Seife ; sabun
  it sapone ; sabun
  es jabón ; sabun
  el σαπούνι [sapoúni] ; sabun
  bg сапун [sapun] ; sabun
  sr сапун [sapun] ; sabun
  sq sapun ; sabun
  ro săpun ; sabun
  mk сапун [sapun] ; sabun
  hu szappan ; sabun
  ru мыло [mılo] ; sabun ; ff:Rusçada sabun için Slav kökenli mılo kullanılır
  ar صابون [ṣābūn] ; sabun
  fa صابون [ṣābūn] ; sabun
  ur صابن [sābun] ; sabun
  az sabun ; sabun
  kk сабын [sabın] ; sabun
  uz sovun ; sabun
  ky самын [samın] ; sabun
  tk sabyn ; sabun
  hy սապոն [sapon] ; sabun
  ka საპონი [saponi] ; sabun
@biber shared_ancestor
  en pepper ; biber
  fr poivre ; karabiber
  de Pfeffer ; biber
  it pepe ; biber
  el πιπέρι [pipéri] ; biber
  bg пипер [piper] ; biber
  sr бибер [biber] ; karabiber
  sq piper ; biber
  ro piper ; biber
  mk бибер [biber] ; biber
  hu bors ; biber ; ff:Macarca bors Türkçe "burç" (baharat) ile ilişkilendirilir
  ru перец [perets] ; biber
  ar فلفل [filfil] ; biber
  fa فلفل [felfel] ; biber
  az bibər ; biber
  kk бұрыш [burış] ; biber
  uz murch ; biber
@karpuz shared_ancestor
  ro harbuz ; karpuz (Moldova ağzı)
  bg карпуз [karpuz] ; karpuz
  sr карпуза [karpuza] ; karpuz (ağız)
  el καρπούζι [karpoúzi] ; karpuz
  sq karpuz ; karpuz (ağız)
  mk карпуз [karpuz] ; karpuz
  uk гарбуз [harbuz] ; bal kabağı ; ff:Ukraynacada harbuz "bal kabağı" anlamına kaymıştır
  ru арбуз [arbuz] ; karpuz
  pl arbuz ; karpuz
  fa خربزه [ḫarboze] ; kavun ; ff:Farsçada ḫarboze "kavun" demektir; karpuz için hendevāne kullanılır
  ur خربوزہ [ḫarbūza] ; kavun ; ff:Urducada kavun anlamındadır
  az qarpız ; karpuz
  kk қарбыз [qarbız] ; karpuz
  uz tarvuz ; karpuz
  ky дарбыз [darbız] ; karpuz
  tk garpyz ; karpuz
@satranç shared_ancestor
  en chess ; satranç ; ff:İngilizce chess, Farsça "şah" sözcüğünden Eski Fransızca eschec yoluyla gelir
  fr échecs ; satranç
  de Schach ; satranç
  it scacchi ; satranç
  es ajedrez ; satranç
  el σκάκι [skáki] ; satranç
  ru шахматы [şahmatı] ; satranç
  pl szachy ; satranç
  hu sakk ; satranç
  bg шах [şah] ; satranç
  sr шах [šah] ; satranç
  ro șah ; satranç
  fa شطرنج [şaṭranc] ; satranç
  ar شطرنج [şaṭranc] ; satranç
  ur شطرنج [şatranj] ; satranç
  az şahmat ; satranç
  kk шахмат [şahmat] ; satranç
  uz shaxmat ; satranç
@bahçe shared_ancestor
  bg бахча [bahça] ; bostan, sebze bahçesi
  sr башта [bašta] ; bahçe
  sq bahçe ; bahçe
  ro bahcea ; bostan (ağız)
  mk бавча [bavča] ; bahçe
  el μπαξές [mpaxés] ; bahçe
  ru бахча [bahça] ; kavun karpuz tarlası ; ff:Rusçada bahça yalnızca kavun karpuz tarlasıdır
  uk баштан [baştan] ; bostan
  fa باغچه [bāġçe] ; küçük bahçe
  ur باغیچہ [bāġīça] ; küçük bahçe
  az bağça ; bahçe; anaokulu ; ff:Azerbaycan Türkçesinde bağça aynı zamanda "anaokulu" anlamındadır
  kk бақша [baqşa] ; bostan; anaokulu
  uz bog'cha ; anaokulu ; ff:Özbekçede bog'cha "anaokulu" anlamına kaymıştır
  ky бакча [bakça] ; bahçe
@terzi shared_ancestor
  sr терзија [terzija] ; terzi
  bg терзия [terziya] ; terzi
  sq terzi ; terzi
  mk терзија [terzija] ; terzi
  el τερζής [terzís] ; terzi (ağız)
  fa درزی [darzī] ; terzi
  ur درزی [darzī] ; terzi
  az dərzi ; terzi
  uz darz ; terzi (ağız)
@kasket into_turkish
  fr casquette ; kasket
  ro cașchetă ; kasket
  bg каскет [kasket] ; kasket
  sr кашкет [kašket] ; kasket
  ru каскетка [kasketka] ; kasket
  hu kasket ; kasket (ağız)
  el κασκέτο [kaskéto] ; kasket
@su shared_ancestor
  az su ; su
  kk су [su] ; su
  uz suv ; su
  ky суу [suu] ; su
  tk suw ; su
  hu só ; tuz ; ff:Macarca só "tuz" demektir; su ile köken bağı yoktur; yalancı arkadaştır
@göz shared_ancestor
  az göz ; göz
  kk көз [köz] ; göz
  uz ko'z ; göz
  ky көз [köz] ; göz
  tk göz ; göz
  hu szem ; göz ; ff:Macarcada göz için Fin-Ugor kökenli szem kullanılır
@elma shared_ancestor
  az alma ; elma
  kk алма [alma] ; elma
  uz olma ; elma
  ky алма [alma] ; elma
  tk alma ; elma
  hu alma ; elma
  mn алим [alim] ; elma
@arslan from_turkish
  hu oroszlán ; aslan
  bg арслан [arslan] ; aslan (ağız; kişi adı)
  ru Руслан [Ruslan] ; kişi adı (Arslan'dan)
  az aslan ; aslan
  kk арыстан [arıstan] ; aslan
  uz arslon ; aslan
  ky арстан [arstan] ; aslan
  tk arslan ; aslan
  mn арслан [arslan] ; aslan
  ka ასლანი [aslani] ; aslan (kişi adı)
@kapı from_turkish
  hu kapu ; kapı, bahçe kapısı
  sr капија [kapija] ; avlu kapısı
  bg капия [kapiya] ; büyük kapı
  sq kapi ; kapı (ağız)
  mk капија [kapija] ; kapı
  ro capie ; kapı (ağız)
  az qapı ; kapı
  kk қақпа [qaqpa] ; büyük kapı
  uz qopqa ; kapı
  ky капка [kapka] ; kapı
  tk gapy ; kapı
@ütü from_turkish
  ru утюг [utyug] ; ütü
  uk утюг [utyuh] ; ütü
  bg ютия [yutiya] ; ütü
  sr утија [utija] ; ütü
  mk утија [utija] ; ütü
  sq hekur ; ütü ; ff:Arnavutçada ütü için "hekur" (demir) kullanılır
  az ütü ; ütü
  kk үтік [ütik] ; ütü
  uz dazmol ; ütü ; ff:Özbekçede ütü için Farsça kökenli dazmol kullanılır
  tk ütük ; ütü
"""
