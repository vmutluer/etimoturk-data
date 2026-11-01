# -*- coding: utf-8 -*-
"""Korpus 26 — Anadolu & 81 İl Yer Adları Köken Atlası (A): plaka 01–41.

DSL (parsing.parse_toponyms):
  @Ad|tür|il|bölge|plaka|köken dili
  chain: kod:biçim>kod:biçim>...>tr:Ad      (en eski bilinen biçimden bugüne)
  era: en eski kaydın dönemi   meaning: anlam   story: özgün tarihsel hikâye   source: kamu malı kaynak   coords: enlem,boylam

Telif notu: Hikâyeler yalnızca tarihsel/coğrafi olgulardan (antik kent adları, ses değişimleri, kamu malı kaynaklar:
Strabon Geographika, Ksenophon Anabasis, Evliya Çelebi Seyahatnâmesi, Kâtip Çelebi Cihânnümâ, Pîrî Reis Kitâb-ı Bahriye)
EtimoTürk şablonlarıyla özgün yazılmıştır; telifli sözlük metni kullanılmaz.
"""

TOPONYMS = r"""
@Adana|il|Adana|Akdeniz|1|hit
chain: hit:Adaniya>el:Ádana>la:Adana>ar:Aḏana>ota:Adana>tr:Adana
era: Hitit dönemi (MÖ 2. binyıl)
meaning: Kizzuwatna ülkesindeki Adaniya kentinin adı; Yunan söylencesinde Uranos'un oğlu Adanos'a bağlanır
story: Adın en eski biçimi Hitit çivi yazılı metinlerinde Kizzuwatna krallığının kenti olarak geçen Adaniya'dır. Ses yapısı üç bin yılda neredeyse hiç değişmeden Yunanca Ádana, Latince Adana ve Arapça Aḏana biçimleriyle süregelmiştir. Yunan mitolojisi adı gök tanrısı Uranos'un oğlu Adanos'a bağlar; bu, sonradan uydurulan bir kurucu söylencesidir. Seyhan Irmağı üzerindeki Roma dönemi Taşköprü ve 1352'de kenti alan Ramazanoğulları Beyliği, adın Türkçeye geçtiği dönemin tanıklarıdır.
source: Hitit çivi yazılı belgeler (Kizzuwatna); Strabon, Geographika XIV; Evliya Çelebi Seyahatnâmesi
coords: 37.0000,35.3213

@Adıyaman|il|Adıyaman|Güneydoğu Anadolu|2|ar
chain: el:Pérrē>ar:Ḥiṣn Manṣūr>ota:Hısn-ı Mansur>cum:Adıyaman>tr:Adıyaman
era: Emevî dönemi (8. yy)
meaning: Hısn-ı Mansur "Mansur'un kalesi"; Adıyaman biçimi "adı yaman (ünü çetin)" halk yorumuyla açıklanır
story: Kentin antik çekirdeği Kommagene Krallığı'nın Perre (bugünkü Pirin) yerleşimidir. 8. yüzyılda Emevî komutanı Mansur bin Cavana'nın yaptırdığı kale, Arapça Hısn-ı Mansur adıyla yüzyıllarca bölgenin merkezi olmuştur. Osmanlı belgelerinde Hısn-ı Mansur yazılan ad 1926'da Adıyaman olarak değiştirildi; bu biçim halk arasında "adı yaman", yani ünü ve çetinliği bilinen yer diye yorumlanır. Nemrut Dağı'ndaki Kommagene anıtları il adının tarihsel katmanlarının en görkemli tanığıdır.
source: Kommagene yazıtları; Osmanlı tahrir defterleri (olgu); Cumhuriyet dönemi idari kayıtları
coords: 37.7648,38.2786

@Afyonkarahisar|il|Afyonkarahisar|Ege|3|tr
chain: el:Akroinón>sel:Karahisar>ota:Karahisâr-ı Sâhib>cum:Afyonkarahisar>tr:Afyonkarahisar
era: Bizans dönemi (8. yy)
meaning: "Kara hisar" (koyu renkli volkanik kaya üstündeki kale) + afyon (haşhaş sütü; Arapça afyūn, Yunanca ópion)
story: Kentin 226 metre yüksekliğindeki volkanik kayası üzerindeki kale Bizans döneminde Akroinon adıyla anılırdı; 740 yılında Araplarla Bizans arasında büyük bir savaşa sahne oldu. Türkler kayanın koyu rengi için kaleye Karahisar dediler; Selçuklu veziri Sahip Ata'nın imarından sonra Karahisâr-ı Sâhib biçimi yerleşti. Yörede yüzyıllardır yetiştirilen haşhaştan elde edilen afyon, Osmanlı'nın son döneminde adın başına eklendi ve 1932'de resmî ad Afyonkarahisar oldu.
source: Bizans kronikleri (Akroinon Savaşı); Evliya Çelebi Seyahatnâmesi; Osmanlı salnameleri
coords: 38.7507,30.5567

@Ağrı|il|Ağrı|Doğu Anadolu|4|unk
chain: xur:Urarṭu>hy:Ayrarat>ota:Karaköse>cum:Ağrı>tr:Ağrı
era: Urartu dönemi (MÖ 9. yy)
meaning: Ağrı Dağı'nın adından; dağın adı Urartu / Ermenice Ayrarat bölge adıyla ilişkilendirilir, kesin kökeni tartışmalıdır
story: İl merkezi Osmanlı döneminde Karaköse adını taşıyordu; 1946'da il, ülkenin en yüksek dağı olan Ağrı Dağı'nın adını aldı. Dağın Türkçe adı için iki yorum vardır: Urartu krallığının adından türeyen Ermenice Ayrarat bölge adının Türkçeleşmesi ya da doğrudan Türkçe ağrı sözcüğünün "yüksek, ulu" anlamıyla kullanılması. Asur kaynaklarında Urarṭu, Tevrat'ta Ararat olarak geçen ad, Nuh'un gemisi söylencesiyle dünya kültürüne mal olmuştur. Eski Türkçede dağlar için kullanılan "ağır/ağrı" biçimleri de halk anlatılarında yaşar.
source: Asur yıllıkları (Urarṭu); Urartu yazıtları; Osmanlı salnameleri (Karaköse)
coords: 39.7191,43.0503

@Amasya|il|Amasya|Karadeniz|5|el
chain: el:Amáseia>la:Amasia>ar:Amāsiya>sel:Amasiyye>ota:Amasya>tr:Amasya
era: Helenistik dönem (MÖ 3. yy)
meaning: Amazon kraliçesi Amasis'e bağlanan kurucu adı; Pontus Krallığı'nın ilk başkenti
story: Coğrafyacı Strabon'un doğduğu kent olan Amaseia, Yeşilırmak vadisinde Pontus krallarının kaya mezarlarıyla çevrilidir. Strabon adı Amazon kraliçesi Amasis'e bağlar; bu bir kurucu söylencesidir ve adın Yunanca öncesi Anadolu diline ait olduğu düşünülür. Latince Amasia, Arapça Amāsiya biçimleriyle süren ad Türkçede Amasya oldu. Osmanlı döneminde şehzadelerin vali olarak yetiştirildiği kent, "şehzadeler şehri" diye anılır.
source: Strabon, Geographika XII; Amasya Tarihi (Abdizade Hüseyin Hüsameddin, 1912–1914)
coords: 40.6499,35.8353

@Ankara|il|Ankara|İç Anadolu|6|phr
chain: hit:Ankuwaš>phr:Ankyra>el:Ánkyra>la:Ancyra>ar:Anqira>ota:Engürü / Ankara>tr:Ankara
era: Frig dönemi (MÖ 8. yy)
meaning: Yunanca ánkyra "çapa" (halk yorumu); Frig kuruluşu, olasılıkla Hitit Ankuwaš kentiyle ilişkili
story: Frig kralı Midas'ın kurduğu söylenen Ankyra, Yunan yazarlarınca "çapa" sözcüğüyle açıklanmış, kentin sikkelerine de çapa işlenmiştir; ancak ad büyük olasılıkla Hitit metinlerindeki Ankuwaš gibi daha eski bir Anadolu adının Yunanca'ya uyarlanmasıdır. Galatların başkenti, Roma'nın Galatia eyalet merkezi olan kentte Augustus'un vasiyeti (Monumentum Ancyranum) tapınak duvarına kazınmıştır. Osmanlı belgelerinde Engürü ve Ankara biçimleri yan yana yaşamış, 1923'te Türkiye Cumhuriyeti'nin başkenti olmuştur.
source: Monumentum Ancyranum; Pausanias, Periēgēsis; Evliya Çelebi Seyahatnâmesi
coords: 39.9208,32.8541

@Antalya|il|Antalya|Akdeniz|7|el
chain: el:Attáleia>la:Attalia>ar:Anṭāliya>sel:Adalya>ota:Antalya>tr:Antalya
era: Helenistik dönem (MÖ 2. yy)
meaning: Bergama kralı II. Attalos Philadelphos'un adından "Attalos'un kenti"
story: Bergama kralı II. Attalos MÖ 159 dolaylarında krallığına bir Akdeniz limanı kazandırmak için kenti kurdurmuş ve kendi adını vermiştir. Roma döneminde Hadrianus'un ziyareti için yapılan kapı bugün hâlâ ayaktadır. Arap coğrafyacıları adı Anṭāliya olarak yazdı; Selçuklular 1207'de kenti aldıklarında Adalya biçimini kullandılar. İtalyan denizcilerin Satalia dediği liman, Pîrî Reis'in Kitâb-ı Bahriye'sinde Antalya olarak kaydedilmiştir.
source: Strabon, Geographika XIV; Pîrî Reis, Kitâb-ı Bahriye (1521); Hadrianus Kapısı yazıtı
coords: 36.8969,30.7133

@Artvin|il|Artvin|Karadeniz|8|ka
chain: ka:Artvani>ota:Artvin>ru:Artvin>tr:Artvin
era: Orta Çağ Gürcü kaynakları (10. yy)
meaning: Gürcüce yer adı; Çoruh vadisindeki kale yerleşiminin adı
story: Çoruh Irmağı'nın dik yamaçlarına kurulu kent, Orta Çağ'da Gürcü Bagrat krallığının Klarceti bölgesine bağlıydı ve adı Gürcü kaynaklarında Artvani biçiminde geçer. Ad, bölgenin Gürcü ve Laz dillerindeki yerleşim adı geleneğine aittir; Türkçede son hecesi düşerek Artvin olmuştur. 1878'den 1918'e kadar Rus yönetiminde kalan kent, 1921 Kars Antlaşması'yla Türkiye'ye katıldı ve 1936'da il oldu.
source: Gürcü vakayinameleri (Kartlis Tskhovreba); Osmanlı Livane sancağı kayıtları
coords: 41.1828,41.8183

@Aydın|il|Aydın|Ege|9|tr
chain: el:Trálleis>la:Tralles>sel:Güzelhisar>ota:Aydın Güzelhisarı>tr:Aydın
era: Antik dönem (MÖ 1. binyıl)
meaning: Aydınoğulları Beyliği'nin kurucusu Aydınoğlu Mehmed Bey'in adından; Türkçe aydın "ışıklı, bilgili"
story: Antik Tralleis, Büyük Menderes vadisinin kuzeyinde Karya ile Lidya sınırındaki önemli bir kentti; Strabon kentin zenginliğini ve güzel yapılarını anlatır. Türkler 14. yüzyılda kenti aldıklarında ona Güzelhisar dediler; beyliğin kurucusu Aydınoğlu Mehmed Bey'in adı önce bölgeye, sonra kente verildi. Osmanlı belgelerinde Aydın Güzelhisarı diye geçen ad zamanla yalnızca Aydın'a kısaldı. Aydın sözcüğü Eski Türkçe ay "ay ışığı" kökünden türemiştir.
source: Strabon, Geographika XIV; Düstûrnâme-i Enverî (15. yy); Osmanlı tahrir defterleri
coords: 37.8560,27.8416

@Balıkesir|il|Balıkesir|Marmara|10|el
chain: la:Hadrianutherae>el:Palaiókastron>sel:Balıkesri>ota:Balıkesir>tr:Balıkesir
era: Roma dönemi (2. yy)
meaning: Yunanca palaiókastron "eski kale"; Türkçe ağızlarda Balıkesri biçimine dönüşmüştür
story: İmparator Hadrianus'un bölgede avlanırken kurdurduğu Hadrianutherae kentinin kalıntıları üzerinde Bizans döneminde "eski kale" anlamındaki Palaiokastron yerleşimi vardı. Türkler 14. yüzyıl başında Karesi Beyliği'nin merkezi yaptıkları kente bu adı Balıkesri biçiminde uyarladılar; halk arasında ad "balık hisarı" ya da Balak adlı bir beyin kalesi diye de yorumlanır. Osmanlı salnamelerinde Balıkesir olarak yazılan kent Karesi sancağının merkezi olarak kaldı.
source: Roma dönemi sikkeleri (Hadrianutherae); Osmanlı Karesi sancağı kayıtları; Evliya Çelebi Seyahatnâmesi
coords: 39.6484,27.8826

@Bilecik|il|Bilecik|Marmara|11|el
chain: el:Belokómē>sel:Bilecük>ota:Bilecik>tr:Bilecik
era: Bizans dönemi (12. yy)
meaning: Bizans Yunancası Belokome "güzel köy / beyaz köy" biçiminden Türkçeye uyarlanmıştır
story: Osmanlı Beyliği'nin kuruluş topraklarında yer alan kent, Bizans kaynaklarında Belokome adıyla geçen bir tekfur kalesiydi. Osman Gazi 1299 dolaylarında kaleyi aldı; Türkçe söyleyişte Belokome önce Bilecük, sonra Bilecik oldu. Şeyh Edebali'nin türbesi ve Orhan Gazi Camii, adın Türkçeleştiği kuruluş dönemini bugüne taşır. Kent 1924'te il merkezi oldu.
source: Bizans kaynakları (Pachymeres); Âşıkpaşazâde Tarihi (15. yy)
coords: 40.1426,29.9793

@Bingöl|il|Bingöl|Doğu Anadolu|12|tr
chain: hy:Čapałǰur>ota:Çapakçur>cum:Bingöl>tr:Bingöl
era: Osmanlı dönemi (16. yy)
meaning: "Bin göl": Bingöl Dağları'ndaki sayısız buzul gölünden; eski ad Çapakçur Ermenice kökenlidir
story: Kent Osmanlı belgelerinde Çapakçur adıyla geçer; bu ad Ermenice bir yer adının Türkçe söyleyişidir ve "ırmak" anlamlı -çur öğesi içerir. Çevredeki dağların doruklarında yer alan onlarca buzul gölü yöreye eskiden beri Bingöl Yaylası dedirtiyordu. 1945'te il merkezinin adı bu yayla adına uygun olarak Bingöl yapıldı. Türkçe bin "1000" ve göl sözcükleri, Eski Türkçe bıŋ ve köl biçimlerinden gelir.
source: Osmanlı tahrir defterleri (Çapakçur sancağı); Evliya Çelebi Seyahatnâmesi
coords: 38.8855,40.4966

@Bitlis|il|Bitlis|Doğu Anadolu|13|hy
chain: hy:Bałeš>ar:Badlīs>ota:Bidlis>tr:Bitlis
era: Erken Orta Çağ (7. yy)
meaning: Ermenice Bałeš yer adının Arapça Badlīs yoluyla Türkçeleşmiş biçimi; halk söylencesi İskender'in komutanı Bedlis'e bağlar
story: Van Gölü'nün batısında derin bir vadiye kurulu kent, Ermeni kaynaklarında Bałeš (Baghesh) olarak geçer; Arap coğrafyacıları bu adı Badlīs biçiminde yazmıştır. Halk anlatısı kaleyi Büyük İskender'in komutanı Bedlis'in yaptırdığını söyler; bu, adın sesinden türetilmiş bir söylencedir. Kent 16.–19. yüzyıllarda Kürt Bitlis beylerinin yönetiminde özerk bir hanlıktı; Şerefnâme'nin yazarı Şeref Han bu hanedandandır. Türkçede d sesi t'ye dönüşerek Bitlis biçimi yerleşmiştir.
source: Ermeni vakayinameleri; Arap coğrafyacıları (olgu); Şerefnâme (1597); Evliya Çelebi Seyahatnâmesi
coords: 38.4006,42.1095

@Bolu|il|Bolu|Karadeniz|14|el
chain: el:Bithýnion>la:Claudiopolis>el:Pólis>sel:Bolı>ota:Bolu>tr:Bolu
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca pólis "şehir" sözcüğünün Türkçe söylenişi; Roma adı Claudiopolis "Claudius'un kenti"
story: Bithynia bölgesinin iç kesimindeki kent Hellenistik dönemde Bithynion adını taşıyordu; İmparator Claudius'un döneminde Claudiopolis oldu ve Hadrianus'un sevgilisi Antinoos burada doğdu. Bizans döneminde halk kenti yalnızca "Polis" (şehir) diye anıyordu; Türkler bu sözcüğü Bolı/Bolu biçiminde benimsediler. Aynı pólis öğesi Gelibolu, Safranbolu ve İnebolu adlarında da yaşar. Köroğlu destanının geçtiği Bolu Dağları kentin kültür belleğindedir.
source: Pausanias; Roma dönemi sikkeleri (Claudiopolis); Evliya Çelebi Seyahatnâmesi
coords: 40.7392,31.6089

@Burdur|il|Burdur|Akdeniz|15|el
chain: el:Polydórion>sel:Burdur>ota:Burdur>tr:Burdur
era: Bizans dönemi (10. yy)
meaning: Bizans dönemi Polydorion yerleşim adının Türkçe söyleyişi olduğu düşünülür; kesin köken tartışmalıdır
story: Burdur Gölü kıyısındaki kent, antik Pisidia bölgesinde yer alır; Bizans kaynaklarında yakın çevre için Polydorion adı geçer ve kentin adının bu addan türediği yaygın görüştür. Selçuklu ve Hamitoğulları döneminde Burdur biçimiyle kaydedilen kent, Osmanlı'da Hamid sancağına bağlıydı. Yakındaki Sagalassos ve Kibyra antik kentleri, Türkçe addan önceki Pisidia katmanının görkemli kalıntılarıdır.
source: Bizans idari kayıtları (olgu); Osmanlı Hamid sancağı tahrirleri
coords: 37.7203,30.2908

@Bursa|il|Bursa|Marmara|16|el
chain: el:Proûsa>la:Prusa>ar:Burūsa>ota:Burusa>tr:Bursa
era: Helenistik dönem (MÖ 3. yy)
meaning: Bitinya kralı I. Prusias'ın adından; "Prusias'ın kenti"
story: Bitinya kralı I. Prusias, Kartacalı komutan Hannibal'in de öğüdüyle MÖ 3. yüzyıl sonunda Uludağ'ın eteğine kendi adını taşıyan kenti kurdurdu: Prusa. Roma'nın Prusa ad Olympum dediği kent, Bizans döneminde Prousa biçimiyle anıldı. Orhan Gazi 1326'da kenti alınca Osmanlı'nın ilk başkenti oldu ve Türkçe söyleyişte önce Burusa, ardından Bursa biçimi yerleşti. Evliya Çelebi kentin kaplıcalarını ve ipek çarşılarını uzun uzun anlatır.
source: Strabon, Geographika XII; Plinius, Naturalis Historia; Evliya Çelebi Seyahatnâmesi
coords: 40.1885,29.0610

@Çanakkale|il|Çanakkale|Marmara|17|tr
chain: el:Abydos>ota:Kal'a-i Sultâniye>ota:Çanak Kal'ası>tr:Çanakkale
era: Osmanlı dönemi (15. yy)
meaning: "Çanak kale": Fatih'in yaptırdığı kalenin çevresinde gelişen çanak çömlek üretiminden
story: Boğazın en dar yerinde Fatih Sultan Mehmed 1462'de Kale-i Sultaniye'yi yaptırdı; karşısındaki Kilitbahir ile birlikte boğazı kilitleyen bu kalenin çevresinde kurulan kasaba, Evliya Çelebi'nin de övdüğü sırlı çanak çömlek üretimiyle ünlendi. Halk kaleye Çanak Kalesi dedi; 18. yüzyıldan sonra bu ad resmî belgelere de girdi. Antik Abydos ve Sestos'un karşılıklı kıyıları, Hero ile Leandros efsanesinden 1915 savaşlarına uzanan tarihin sahnesidir.
source: Evliya Çelebi Seyahatnâmesi; Pîrî Reis, Kitâb-ı Bahriye; Osmanlı salnameleri
coords: 40.1553,26.4142

@Çankırı|il|Çankırı|İç Anadolu|18|el
chain: el:Gángra>la:Germanicopolis>ar:Ḫanjara>sel:Kengırı>ota:Çankırı>tr:Çankırı
era: Helenistik dönem (MÖ 1. yy)
meaning: Paflagonya krallığının başkenti Gangra'nın adı; Paflagonya dilinde "keçi" anlamı olduğu aktarılır
story: Paflagonya kralı Deiotaros'un başkenti olan Gangra'nın adı Yunanca metinlerde geçer; Strabon kentin kalesini anlatır. Roma döneminde bir süre Germanicopolis adını alan kent, 4. yüzyılda bir kilise konsiline ev sahipliği yaptı. Arap kaynakları Ḫanjara, Selçuklu ve Osmanlı belgeleri Kengırı yazdı; Türkçe söyleyişte ç- ile başlayan Çankırı biçimi 20. yüzyılda resmîleşti. Kentteki kaya tuzu ocakları Hitit çağından beri işletilmektedir.
source: Strabon, Geographika XII; Gangra Konsili kayıtları (olgu); Osmanlı Kengırı sancağı tahrirleri
coords: 40.6013,33.6134

@Çorum|il|Çorum|Karadeniz|19|tr
chain: sel:Çorumlu>ota:Çorum>tr:Çorum
era: Selçuklu dönemi (12. yy)
meaning: Yöreye yerleşen Çorumlu Oğuz topluluğunun adından olduğu düşünülür; Hitit başkenti Hattuşa'ya komşudur
story: Kent, Hitit İmparatorluğu'nun başkenti Hattuşa'ya ve Alacahöyük'e kırk kilometre uzaklıktadır; ancak Çorum adı antik değil, Türk dönemine aittir. Danişmendliler ve Selçuklular döneminde yöreye yerleşen Çorumlu adlı Oğuz topluluğunun adının kente geçtiği kabul edilir. Osmanlı belgelerinde Çorum sancağı olarak geçen yer, 1923'te il oldu. Halk arasında adın "Çoğu Rum" biçiminden türediği söylenir; bu bir halk etimolojisidir.
source: Danişmendnâme; Osmanlı tahrir defterleri; Hitit başkenti Hattuşa kazı yayınları (olgu)
coords: 40.5506,34.9556

@Denizli|il|Denizli|Ege|20|tr
chain: el:Laodíkeia>sel:Lâdik>ota:Tonguzlu>ota:Denizli>tr:Denizli
era: Selçuklu dönemi (13. yy)
meaning: Türkçe "denizli": kaynak sularının bolluğundan "deniz gibi suyu olan yer"
story: Antik Laodikeia'nın yanı başında kurulan Türk kenti, Selçuklu belgelerinde Lâdik, 14.–16. yüzyıl kayıtlarında ise Tonguzlu biçimiyle geçer. Bu eski adın domuz "yaban domuzu" sözcüğünden geldiği, su kaynaklarının bolluğu nedeniyle halkın kente "denizli" dediği ve iki biçimin birbirine karıştığı kabul edilir. Evliya Çelebi kenti Denizli olarak kaydeder ve bağlarını över. Pamukkale travertenleri ile Hierapolis de bu ilin sınırlarındadır.
source: İbn Battûta Seyahatnâmesi (Tonguzlu); Evliya Çelebi Seyahatnâmesi; Osmanlı tahrir defterleri
coords: 37.7765,29.0864

@Diyarbakır|il|Diyarbakır|Güneydoğu Anadolu|21|ar
chain: akk:Amedi>el:Ámida>la:Amida>ar:Diyār Bakr>ota:Diyarbekir>cum:Diyarbakır>tr:Diyarbakır
era: Asur dönemi (MÖ 9. yy)
meaning: Arapça Diyār Bakr "Bakr oğullarının yurdu"; 1937'de bakır madeniyle ilişkilendirilerek Diyarbakır biçimi verildi
story: Dicle kıyısındaki kent Asur yıllıklarında Amedi, Roma ve Bizans kaynaklarında Amida olarak geçer; bazalttan örülü surları bu dönemin eseridir. 7. yüzyılda bölgeye yerleşen Arap Bakr kabilesinin adıyla çevre Diyār Bakr "Bakr'ın diyarı" olarak anıldı ve bu ad zamanla kente de verildi. Osmanlı belgelerinde Diyarbekir yazılan ad, 1937'de yöredeki bakır madenlerine gönderme yapılarak Diyarbakır biçimine dönüştürüldü. Kara Amid lakabı surların renginden gelir.
source: Asur yıllıkları; Ammianus Marcellinus (Amida kuşatması, 359); Evliya Çelebi Seyahatnâmesi
coords: 37.9144,40.2306

@Edirne|il|Edirne|Marmara|22|la
chain: thr:Uskudama>el:Orestiás>la:Hadrianopolis>el:Adrianoúpolis>ota:Edrene (Edrenebol)>tr:Edirne
era: Roma dönemi (2. yy)
meaning: İmparator Hadrianus'un adından "Hadrianus'un kenti"
story: Trak kabilelerinin Uskudama adlı yerleşiminin yerine İmparator Hadrianus 2. yüzyılda kendi adını taşıyan Hadrianopolis'i kurdu. Bizans'ın Adrianoupolis'i, 1361'de Osmanlı'ya geçince Türkçe söyleyişte Edrene ve -polis öğesini koruyan Edrenebol biçimlerini aldı; sonunda Edirne biçimi yerleşti. Fetihten 1453'e kadar Osmanlı başkenti olan kentte Mimar Sinan'ın Selimiye Camii yükselir. Evliya Çelebi'nin anlattığı Edirne Sarayı ve kırkpınar güreşleri kentin Osmanlı belleğidir.
source: Ammianus Marcellinus (Hadrianopolis Savaşı, 378); Evliya Çelebi Seyahatnâmesi; Osmanlı kronikleri
coords: 41.6771,26.5557

@Elazığ|il|Elazığ|Doğu Anadolu|23|ar
chain: hy:Kharberd>ota:Harput>ota:Mâmûretülazîz>cum:Elazığ>tr:Elazığ
era: Osmanlı dönemi (1862)
meaning: Mâmûretülazîz "Abdülaziz'in bayındır kıldığı yer" (Arapça maʿmūra + Sultan Abdülaziz); 1937'de Elazığ'a kısaltıldı
story: Bölgenin tarihî merkezi, Ermenice "kaya kale" anlamındaki Kharberd adından gelen Harput'tur; Urartu yazıtlarında da kale adı geçer. 1862'de Sultan Abdülaziz döneminde ovaya inilerek kurulan yeni kent, onun adıyla Mâmûretülazîz diye anıldı. Halk dilinde bu uzun ad Elaziz'e kısaldı; 1937'de Atatürk'ün önerisiyle "azık yurdu" anlamına gelecek biçimde Elazığ yazımı benimsendi. Harput Kalesi ve Ulu Cami eski kentin tanıklarıdır.
source: Urartu yazıtları (olgu); Osmanlı salnameleri (Mâmûretülazîz vilayeti); Cumhuriyet dönemi idari kararları
coords: 38.6748,39.2225

@Erzincan|il|Erzincan|Doğu Anadolu|24|hy
chain: hy:Eriza>hy:Erznka>ar:Arzinjān>ota:Erzincan>tr:Erzincan
era: Antik dönem (MÖ 1. yy)
meaning: Ermenice Eriza / Erznka yer adından; Anaitis tapınağıyla ünlü bir kutsal alanın adı
story: Karasu vadisindeki kent, Strabon'un Akilisene bölgesinde andığı Anaitis tapınağının bulunduğu Eriza yerleşimine dayanır. Ermenice Erznka biçimini Arap coğrafyacıları Arzinjān olarak yazdı; Selçuklu ve Mengücek dönemlerinde Erzincan biçimi yerleşti. Mevlâna'nın hocası Burhaneddin Tirmizî'nin yaşadığı, Yunus Emre'nin dolaştığı kent, 1939 depreminde yıkılıp yeniden kuruldu. Marco Polo kenti Arzinga adıyla anar.
source: Strabon, Geographika XI; Marco Polo Seyahatnâmesi; Osmanlı tahrir defterleri
coords: 39.7500,39.5000

@Erzurum|il|Erzurum|Doğu Anadolu|25|ar
chain: hy:Karin>el:Theodosioúpolis>ar:Qālīqalā>ar:Arḍ ar-Rūm>sel:Erzen-i Rûm>ota:Erzurum>tr:Erzurum
era: Bizans dönemi (5. yy)
meaning: Arapça Arḍ ar-Rūm "Rum (Roma) toprağı"; Selçukluların Erzen-i Rûm söyleyişinden
story: Ermenilerin Karin dediği yerde İmparator II. Theodosius 5. yüzyılda Theodosiopolis kalesini kurdurdu; Araplar aynı kente Qālīqalā dediler. Selçuklular 1071'den sonra bölgeyi aldıklarında, Bizans toprağı anlamında Arapça Arḍ ar-Rūm "Rum toprağı" adını kullandılar; yakındaki yıkılmış Erzen kentinin halkı buraya göçünce ad Erzen-i Rûm biçimiyle de söylendi ve iki biçim Erzurum'da birleşti. Çifte Minareli Medrese, Saltuklu ve İlhanlı dönemlerinin tanığıdır; 1919 Erzurum Kongresi burada toplandı.
source: Bizans kronikleri (Theodosiopolis); Arap coğrafyacıları (olgu); Evliya Çelebi Seyahatnâmesi
coords: 39.9043,41.2679

@Eskişehir|il|Eskişehir|İç Anadolu|26|tr
chain: phr:Dorylaion>el:Dorýlaion>la:Dorylaeum>sel:Sultanönü>ota:Eskişehir>tr:Eskişehir
era: Frig dönemi (MÖ 1. binyıl)
meaning: Türkçe "eski şehir": antik Dorylaion kalıntılarının yanına kurulan Türk kentinin adı
story: Frig kralı Dorylaos'a bağlanan Dorylaion, Porsuk Çayı kıyısında Roma ve Bizans dönemlerinin önemli bir kaplıca kentiydi; 1097'de Haçlılar ile Selçuklular burada savaştı. Türkler, Şarhöyük'teki antik kalıntılara "eski şehir" dediler ve bu ad yeni kurulan kente geçti. Selçuklu döneminde bölge Sultanönü sancağı olarak anılıyordu. Lületaşı işçiliği ve Yunus Emre'nin Sarıköy'deki türbesi kentle özdeşleşmiştir.
source: Haçlı kronikleri (Dorylaeum Savaşı, 1097); Osmanlı Sultanönü sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 39.7767,30.5206

@Gaziantep|il|Gaziantep|Güneydoğu Anadolu|27|syc
chain: syc:ʿĒn ṭāb>ar:ʿAynṭāb>ota:Ayntab>cum:Gaziantep>tr:Gaziantep
era: Erken Orta Çağ (7. yy)
meaning: Aramice/Süryanice ʿēn ṭāb "iyi pınar" (Arapça ʿaynṭāb); Gazi unvanı 1921'de TBMM tarafından verildi
story: Kentin eski adı Ayntab, Süryanice "iyi pınar" anlamındaki ʿēn ṭāb ile açıklanır; Arap kaynaklarında ʿAynṭāb, Haçlı belgelerinde Hamtab biçiminde geçer. Kentin çekirdeği, Hitit metinlerindeki Doliche (Dülük) kutsal alanının yakınındaki kaledir. 1920–1921 kuşatmasındaki direniş nedeniyle TBMM 1921'de kente Gazi unvanını verdi; 1928'de Gaziantep resmî ad oldu. Fıstık ve bakır işçiliği gibi kent kültürü Evliya Çelebi'nin de övdüğü çarşılardan gelir.
source: Haçlı kronikleri; Evliya Çelebi Seyahatnâmesi; TBMM kararı (8 Şubat 1921)
coords: 37.0662,37.3833

@Giresun|il|Giresun|Karadeniz|28|el
chain: el:Kerasoûs>la:Cerasus>el:Kerasoûnta>ota:Giresun>tr:Giresun
era: Antik dönem (MÖ 4. yy)
meaning: Yunanca kérasos "kiraz ağacı" ile ilişkili kent adı; kiraz sözcüğü Avrupa dillerine bu kentin adından yayılmıştır
story: Ksenophon'un Onbinler ordusuyla uğradığı Kerasous, Sinop'un bir kolonisiydi. Roma komutanı Lucullus'un MÖ 1. yüzyılda kiraz ağacını buradan İtalya'ya götürdüğü Plinius tarafından anlatılır; Latince cerasus ve ondan türeyen İngilizce cherry, Fransızca cerise kentin adıyla aynı kökü paylaşır. Bizans döneminde Kerasounta denen kent, Türkçede Giresun oldu. Fındık üretimi ve Giresun Adası'ndaki Amazon söylenceleri kentle anılır.
source: Ksenophon, Anabasis V; Plinius, Naturalis Historia XV; Pîrî Reis, Kitâb-ı Bahriye
coords: 40.9128,38.3895

@Gümüşhane|il|Gümüşhane|Karadeniz|29|tr
chain: el:Argyrópolis>ota:Gümüşhane>tr:Gümüşhane
era: Osmanlı dönemi (16. yy)
meaning: Türkçe gümüş + Farsça hāne "ev, ocak": gümüş madeni işletmesi; Yunanca Argyropolis "gümüş kenti" aynı anlamın çevirisidir
story: Harşit vadisindeki gümüş yatakları Bizans döneminden beri işletiliyordu; Rum halkın Argyropolis "gümüş kenti" dediği madenci kasabası, Osmanlı'da gümüş ve hane sözcükleriyle Gümüşhane adını aldı. 16.–18. yüzyıllarda darphanesi bulunan kent, madenlerin tükenmesiyle 19. yüzyılda küçüldü ve yerleşim vadinin aşağısına taşındı. Eski Türkçe kümüş biçiminden gelen gümüş sözcüğü, Macarca ve Slav dillerine de geçmiştir.
source: Osmanlı maden kayıtları (olgu); Evliya Çelebi Seyahatnâmesi; Osmanlı salnameleri
coords: 40.4386,39.5086

@Hakkâri|il|Hakkâri|Doğu Anadolu|30|ku
chain: syc:Ḥakkārī>ar:Hakkāriyya>ota:Hakkâri>tr:Hakkâri
era: Erken İslam dönemi (10. yy)
meaning: Bölgede yaşayan Hakkâri aşiretlerinin adından; Süryani ve Arap kaynaklarında bölge adı olarak geçer
story: Zap suyunun derin vadilerindeki dağlık bölge, Süryani ve Arap coğrafyacılarınca Hakkāriyya adıyla anılıyordu; ad, burada yaşayan Kürt aşiret topluluğunun adından gelir. Kent Osmanlı döneminde Çölemerik adıyla biliniyordu; Hakkâri ise sancak ve bölge adıydı. 1936'da il kurulunca bölge adı kent merkezine de verildi. Nasturi kiliseleri ve Cilo-Sat dağları bu ilin kültürel ve doğal belleğidir.
source: Arap coğrafyacıları (Yakut el-Hamevî, Muʿcemü'l-Büldân, 13. yy); Şerefnâme (1597)
coords: 37.5744,43.7408

@Hatay|il|Hatay|Akdeniz|31|hat
chain: hat:Ḫatti>akk:Ḫatti>cum:Hatay>tr:Hatay
era: Hitit dönemi (MÖ 2. binyıl)
meaning: Hitit ülkesi Ḫatti'nin adından 1936'da türetilen il adı; merkezi Antakya'dır
story: Asur ve Hitit metinleri Orta Anadolu'yu Ḫatti ülkesi, halkını Hattiler diye anar; MÖ 1. binyılda bu ad Kuzey Suriye'deki Geç Hitit krallıkları için de kullanıldı. 1936'da Sancak sorunu gündemdeyken Atatürk, bölgenin Anadolu'yla tarihsel bağını vurgulamak için Hatay adını önerdi. 1938'de kurulan Hatay Devleti 1939'da Türkiye'ye katıldı. İl merkezi Antakya ise Seleukos Krallığı'nın başkenti Antiocheia'dır.
source: Asur ve Hitit çivi yazılı belgeleri (olgu); Hatay Devleti kuruluş belgeleri (1938)
coords: 36.2023,36.1613

@Isparta|il|Isparta|Akdeniz|32|el
chain: el:Báris>el:Spárta (Bizans)>sel:Sparta>ota:Isparta>tr:Isparta
era: Bizans dönemi (10. yy)
meaning: Bizans dönemindeki Sparta adının Türkçe söyleyişi; Yunanistan'daki Sparta ile aynı adı taşır ancak bağlantısı tartışmalıdır
story: Pisidia bölgesindeki kent Roma döneminde Baris adını taşıyordu; Bizans kayıtlarında 10. yüzyıldan sonra Sparta adı görülür ve bunun Mora'daki Sparta'dan gelen yerleşimcilerle ya da Yunanca "ekilmiş yer" anlamıyla ilişkili olduğu tartışılır. Türkçede sözcük başındaki çift ünsüz bir ünlüyle açılarak Isparta oldu. Hamitoğulları Beyliği'nin merkezi olan kent, gül yağı üretimiyle 19. yüzyıldan beri ünlüdür.
source: Bizans idari kayıtları (olgu); Osmanlı Hamid sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 37.7648,30.5566

@Mersin|il|Mersin|Akdeniz|33|el
chain: el:myrsínē>tr:mersin (ağacı)>ota:Mersin İskelesi>tr:Mersin
era: Osmanlı dönemi (19. yy)
meaning: Yunanca myrsínē "mersin ağacı" (murt) sözcüğünden gelen Türkçe bitki adı; kıyıdaki mersin ağaçlıkları
story: Bugünkü kent 19. yüzyılın ilk yarısında, Tarsus'un iskelesi olarak Çukurova pamuğunun ihracıyla gelişti; adı kıyıdaki mersin ağacı topluluklarından ya da aynı adı taşıyan bir Türkmen oymağından gelir. Mersin sözcüğü Yunanca myrsínē'nin Türkçeleşmiş biçimidir. Antik dönemde yakınlardaki Soloi-Pompeiopolis ve Zephyrion limanları bölgenin merkeziydi. İl 2002'ye kadar İçel adını taşıdı.
source: Osmanlı salnameleri (Mersin iskelesi); Strabon, Geographika XIV (Soloi)
coords: 36.8121,34.6415

@İstanbul|il|İstanbul|Marmara|34|el
chain: el:Byzántion>la:Byzantium>el:Konstantinoúpolis>ar:Qusṭanṭīniyya>el:eis tḗn pólin>ota:İstanbul / Kostantiniyye>tr:İstanbul
era: Antik dönem (MÖ 7. yy)
meaning: Yunanca eis tḗn pólin "şehre (doğru)" söz öbeğinin Türkçe söyleyişi; Bizans halkı başkenti yalnızca "şehir" diye anardı
story: Megaralı kolonistler MÖ 7. yüzyılda kurdukları kente önderleri Byzas'ın adıyla Byzantion dediler. 330'da Constantinus kenti Roma'nın yeni başkenti yapınca Konstantinoupolis adı yerleşti; Araplar Qusṭanṭīniyya dedi ve Osmanlı belgelerinde Kostantiniyye yazıldı. Rum halkı başkentten "eis tḗn pólin" yani "şehre" diye söz ederdi; Türkler bu söyleyişi İstanbul biçiminde benimsediler. Dersaadet, Asitane ve İslambol gibi adlar Osmanlı dönemi süslemeleridir; 1930'da İstanbul tek resmî ad oldu.
source: Herodotos IV; Prokopios; Evliya Çelebi Seyahatnâmesi I. cilt; Posta Kanunu (1930)
coords: 41.0082,28.9784

@İzmir|il|İzmir|Ege|35|el
chain: xlu:Tismurna>el:Smýrna>la:Smyrna>el:eis Smýrnēn>sel:İzmir>ota:İzmir>tr:İzmir
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca Smyrna adının "eis Smyrnēn" (Smyrna'ya) söyleyişinden; Anadolu dillerine ait kent adı
story: Kentin adı Yunanca öncesi bir Anadolu diline aittir; Hitit-Luvi metinlerinde Tismurna biçimiyle ilişkilendirilen ad, Yunan söylencesinde Amazon kraliçesi Smyrna'ya bağlanır. Homeros'un doğduğu kentler arasında sayılan Smyrna, Büyük İskender'den sonra Pagos (Kadifekale) eteğine taşındı. Rumların "eis Smyrnēn" söyleyişi Türkçede İzmir oldu; Aydınoğulları 14. yüzyılda kenti aldıklarında bu biçimi kullandılar. Pîrî Reis kenti İzmir adıyla haritalar.
source: Strabon, Geographika XIV; Pausanias; Pîrî Reis, Kitâb-ı Bahriye; Evliya Çelebi Seyahatnâmesi
coords: 38.4237,27.1428

@Kars|il|Kars|Doğu Anadolu|36|unk
chain: hy:Kars>ka:Karsi>ota:Kars>tr:Kars
era: Orta Çağ Ermeni ve Gürcü kaynakları (9. yy)
meaning: Kesin kökeni tartışmalı; Gürcüce "kapı kenti" (kari) ya da Bulgar-Türk Karsak topluluğuyla ilişkilendirilir
story: 10. yüzyılda Ermeni Bagratlı krallığının başkenti olan kentin adı Ermeni ve Gürcü vakayinamelerinde geçer; Gürcüce kari "kapı" sözcüğüne, Kafkasya'ya açılan geçit konumuna ya da bölgeye yerleşen Karsak Türk boyuna bağlanan yorumlar vardır. Selçuklular 1064'te kenti aldı; Osmanlı'da sınır kalesi oldu. 1878–1918 Rus yönetimi kente Baltık tarzı taş yapılar kazandırdı. Kars Antlaşması (1921) sınırı belirledi.
source: Gürcü ve Ermeni vakayinameleri (olgu); Evliya Çelebi Seyahatnâmesi; Osmanlı Kars eyaleti kayıtları
coords: 40.6013,43.0975

@Kastamonu|il|Kastamonu|Karadeniz|37|el
chain: el:Kástra Komnēnṓn>sel:Kastamonı>ota:Kastamonu>tr:Kastamonu
era: Bizans dönemi (11. yy)
meaning: Yunanca Kástra Komnēnṓn "Komnenosların kalesi": Bizans Komnenos hanedanının aile kalesinin adı
story: Bizans'ın Komnenos ailesi 11. yüzyılda Paflagonya'daki bu kaleyi aile yurdu edinmişti; kalenin Kastra Komnenon adı Türkçede Kastamonı biçimine dönüştü. Danişmendliler ve Çobanoğulları döneminde Türkleşen kent, Candaroğulları Beyliği'nin başkenti oldu. Fatih 1461'de Osmanlı'ya kattı; Evliya Çelebi kentin kalesini ve bakırcılarını anlatır. Atatürk 1925 Şapka İnkılâbı'nı burada ilan etti.
source: Bizans kaynakları (Anna Komnena, Aleksiad); Evliya Çelebi Seyahatnâmesi
coords: 41.3887,33.7827

@Kayseri|il|Kayseri|İç Anadolu|38|hit
chain: hit:Mazaka>el:Mázaka / Eusébeia>la:Caesarea>ar:Qayṣariyya>sel:Kayseriyye>ota:Kayseri>tr:Kayseri
era: Hitit dönemi (MÖ 2. binyıl)
meaning: Latince Caesarea "Sezar (imparator) kenti"; eski adı Hitit kökenli Mazaka
story: Erciyes'in eteğindeki kent Hitit metinlerinde Mazaka adıyla geçer; Kapadokya krallarının başkenti olan kent bir süre Eusebeia adını da taşıdı. Roma İmparatoru Tiberius'un döneminde (MS 17) kent Caesarea adını aldı; Arapların Qayṣariyya söyleyişi Selçuklular ve Osmanlılarca Kayseriyye, sonra Kayseri biçiminde sürdürüldü. Yakındaki Kültepe (Kaniş) Asur ticaret kolonisinin tabletleri Anadolu'nun ilk yazılı belgeleridir. Selçuklu başkentlerinden biri olan kentte Hunat Hatun ve Gevher Nesibe külliyeleri ayaktadır.
source: Strabon, Geographika XII; Hitit çivi yazılı metinler; Evliya Çelebi Seyahatnâmesi
coords: 38.7312,35.4787

@Kırklareli|il|Kırklareli|Marmara|39|tr
chain: el:Saránta Ekklēsíes>ota:Kırkkilise>cum:Kırklareli>tr:Kırklareli
era: Bizans dönemi (10. yy)
meaning: Osmanlı adı Kırkkilise, Yunanca Saranta Ekklesies "kırk kilise" adının çevirisidir; 1924'te "kırklar (erenler) ili" olarak değiştirildi
story: Istranca eteklerindeki kent Bizans döneminde Saranta Ekklesies "kırk kilise" adıyla anılırdı; Türkler bu adı Kırkkilise biçiminde çevirerek sürdürdüler. 1363'te I. Murad döneminde Osmanlı'ya katıldı. 1924'te kilise sözcüğü içeren adın değiştirilmesi istendi ve kentin fethinde şehit düşen kırk ereni (kırklar) anan Kırklareli adı benimsendi. Kırk sayısı Türk halk inanışında kutsal bir sayıdır.
source: Bizans kaynakları (olgu); Osmanlı Kırkkilise sancağı kayıtları; 1924 tarihli ad değişikliği kararı
coords: 41.7333,27.2167

@Kırşehir|il|Kırşehir|İç Anadolu|40|tr
chain: el:Mōkissós>sel:Gülşehri>ota:Kırşehir>tr:Kırşehir
era: Selçuklu dönemi (13. yy)
meaning: Türkçe "kır şehir": bozkırın ortasındaki şehir; Selçuklu döneminde Gülşehri adıyla da anılmıştır
story: Orta Anadolu bozkırındaki kent, Bizans döneminde Mokissos adlı piskoposluk merkeziyle ilişkilendirilir. Selçuklular döneminde Gülşehri adıyla anılan kent, Anadolu Ahiliğinin kurucusu Ahi Evran'ın yerleştiği yer oldu; onun türbesi esnaf geleneğinin odağıdır. Kır sözcüğü Eski Türkçede "bozkır, açık arazi" anlamındadır; şehir ise Farsça şahr'dan alınmıştır. Cacabey Medresesi ve Aşık Paşa türbesi kentin Türk dönemi anıtlarıdır.
source: Ahi Evran menakıbnameleri; Osmanlı tahrir defterleri; Evliya Çelebi Seyahatnâmesi
coords: 39.1425,34.1709

@Kocaeli|il|Kocaeli|Marmara|41|tr
chain: el:Nikomḗdeia>ota:İznikmid / Kocaili>cum:Kocaeli>tr:Kocaeli
era: Osmanlı dönemi (14. yy)
meaning: "Akça Koca'nın ili": Orhan Gazi'nin komutanı Akça Koca'nın fethettiği bölge; merkezi İzmit (Nikomedeia)
story: İl, merkezi İzmit'ten değil, bölgeyi 1330'larda fetheden Orhan Gazi'nin komutanı Akça Koca'dan adını alır: Koca-ili "Koca'nın ili". Merkez İzmit ise Bitinya kralı I. Nikomedes'in MÖ 264'te kurduğu Nikomedeia'dır; Diocletianus bu kenti Roma İmparatorluğu'nun doğu başkenti yapmıştı. Rumların "eis Nikomedeian" söyleyişi Türkçede İznikmid, sonra İzmit oldu. Eski Türkçe koca "yaşlı, büyük" sözcüğü ad ve unvan olarak kullanılırdı.
source: Âşıkpaşazâde Tarihi; Lactantius (Nikomedeia); Osmanlı Kocaili sancağı tahrirleri
coords: 40.7654,29.9408
"""
