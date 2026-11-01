# -*- coding: utf-8 -*-
"""Korpus 28 — Tarihî ilçe, semt, antik kent ve bölge adları (A): Marmara, Ege ve Akdeniz.

DSL ve telif notu için bkz. yer_adlari_iller_a.py. Her kayıtta il alanı yerin bağlı olduğu ildir.
"""

TOPONYMS = r"""
# ===================================================================== MARMARA / İSTANBUL
@Üsküdar|semt|İstanbul|Marmara||el
chain: el:Chrysópolis>el:Skoutárion>ota:Üsküdar>tr:Üsküdar
era: Bizans dönemi (12. yy)
meaning: Yunanca skoutárion "deri kalkan": kalkanlı muhafız birliğinin kışlasından; antik adı Chrysopolis "altın kent"
story: Boğaz'ın Anadolu yakasındaki iskele antik çağda Khalkedon'a bağlı Chrysopolis "altın kent" adını taşıyordu; Perslerin vergi altınlarının toplandığı yer olduğu için bu adı aldığı anlatılır. Bizans'ın son yüzyıllarında burada konuşlanan, deri kalkan (skoutárion) taşıyan muhafız birliğinin adı semte geçti ve Türkçede Üsküdar oldu. Osmanlı döneminde Anadolu'ya giden kervanların ve hac yolunun başlangıç noktasıydı; Mihrimah Sultan ve Yeni Valide külliyeleri bu dönemi yaşatır.
source: Ksenophon, Anabasis VI (Chrysopolis); Evliya Çelebi Seyahatnâmesi I. cilt
coords: 41.0226,29.0150

@Kadıköy|semt|İstanbul|Marmara||tr
chain: el:Chalkēdṓn>la:Chalcedon>ota:Kadıköy>tr:Kadıköy
era: Antik dönem (MÖ 7. yy)
meaning: "Kadı köyü": Fatih'in kenti İstanbul'un ilk kadısı Hızır Bey'e arpalık olarak vermesinden; antik adı Khalkedon
story: Megaralı kolonistlerin MÖ 685'te kurduğu Khalkedon, Byzantion'dan önce kurulduğu ve karşı kıyının üstünlüğünü göremediği için Pers komutanınca "körler ülkesi" diye anılmıştı; 451'deki Kadıköy Konsili burada toplandı. Fetihten sonra Fatih bu yerleşimi İstanbul'un ilk kadısı Hızır Bey'e verdi; halk da "kadının köyü" dedi. Haydarpaşa Garı ve Moda, semtin 19. yüzyıl mirasıdır.
source: Herodotos IV; Strabon, Geographika VII; Evliya Çelebi Seyahatnâmesi
coords: 40.9819,29.0255

@Beşiktaş|semt|İstanbul|Marmara||tr
chain: el:Diplokiónion>ota:Beşiktaş>tr:Beşiktaş
era: Osmanlı dönemi (16. yy)
meaning: "Beşik taş": Barbaros Hayreddin Paşa'nın gemileri bağlamak için diktirdiği beş taş direkten ya da beşik biçimli bir taştan
story: Bizans döneminde kıyıda iki sütun bulunduğu için Diplokionion "çifte sütun" diye anılan koy, Osmanlı'da Kaptan-ı Derya Barbaros Hayreddin Paşa'nın donanma üssü oldu. Evliya Çelebi adı, Barbaros'un gemileri bağlamak için diktirdiği beş taş direğe bağlar; başka bir anlatıya göre Hz. İsa'nın beşiğinden bir taş buradaki kilisede saklanıyordu. Barbaros'un türbesi ve Dolmabahçe Sarayı semtin kimliğidir.
source: Evliya Çelebi Seyahatnâmesi I. cilt; Pîrî Reis, Kitâb-ı Bahriye
coords: 41.0422,29.0067

@Galata|semt|İstanbul|Marmara||unk
chain: el:Sykai>el:Galatás>it:Pera / Galata>ota:Galata>tr:Galata
era: Bizans dönemi (10. yy)
meaning: Kökeni tartışmalı: Yunanca gála "süt" (süt çiftlikleri), Galatlar (Keltler) ya da İtalyanca calata "iskele yolu" ile açıklanır
story: Haliç'in karşı yakasındaki tepe Bizans'ta Sykai "incirlik" adını taşıyor, sonra Galatas diye anılıyordu. Ad için üç açıklama vardır: kıyıdaki süt çiftlikleri (gála), burada konaklayan Galat paralı askerleri ya da Cenevizlilerin "iskeleye inen yol" anlamındaki calata sözcüğü. 1267'den sonra Ceneviz kolonisi olan Galata'nın 1348'de yapılan kulesi bugün de ayaktadır. Osmanlı döneminde Levanten tüccarların ve elçiliklerin semti oldu.
source: Bizans kaynakları (olgu); Ceneviz kolonisi belgeleri; Evliya Çelebi Seyahatnâmesi
coords: 41.0256,28.9744

@Beyoğlu|semt|İstanbul|Marmara||tr
chain: el:Péran>ota:Beyoğlu>tr:Beyoğlu
era: Osmanlı dönemi (16. yy)
meaning: "Bey oğlu": burada oturan bir beyzadenin (Pontus prensi ya da Venedik elçisi Gritti'nin oğlu) lakabından; Rumca Pera "karşı yaka"
story: Rumların Péran "karşı taraf" dediği Galata sırtları, 16. yüzyılda burada konak yaptıran bir beyzade yüzünden Beyoğlu diye anılmaya başladı; bu kişinin Müslüman olan Pontus prensi ya da Venedik dojunun oğlu Alvise Gritti olduğu anlatılır. 19. yüzyılda elçilikler, Pera Palas ve Cadde-i Kebir (İstiklal Caddesi) ile Batılı yaşamın merkezi oldu. Tünel (1875) dünyanın en eski yeraltı füniküleri arasındadır.
source: Evliya Çelebi Seyahatnâmesi; Osmanlı Galata kadı sicilleri (olgu)
coords: 41.0370,28.9850

@Eminönü|semt|İstanbul|Marmara||tr
chain: ota:Gümrük Emini Önü>ota:Eminönü>tr:Eminönü
era: Osmanlı dönemi (17. yy)
meaning: "Gümrük emininin (gümrük müdürünün) dairesinin önü": Haliç limanındaki gümrük binasından
story: Haliç'in ağzındaki iskeleler Osmanlı'nın dış ticaret gümrüğüydü; gümrük işlerini yöneten memura emin denirdi ve dairesinin önündeki meydan Eminönü adını aldı. Emin sözcüğü Arapça amīn "güvenilir" sözcüğünden gelir. Mısır Çarşısı, Yeni Cami ve Galata Köprüsü semtin Osmanlı ve Cumhuriyet dönemi simgeleridir; antik Byzantion'un limanı da buradaydı.
source: Evliya Çelebi Seyahatnâmesi; Osmanlı gümrük defterleri (olgu)
coords: 41.0176,28.9709

@Sultanahmet|semt|İstanbul|Marmara||ar
chain: el:Hippódromos>ota:At Meydanı>ota:Sultanahmet>tr:Sultanahmet
era: Osmanlı dönemi (17. yy)
meaning: I. Ahmed'in 1609–1617 arasında yaptırdığı Sultan Ahmed Camii'nin adından; Arapça sulṭān + Aḥmad
story: Bizans'ın araba yarışları yapılan Hippodromos'u Osmanlı'da At Meydanı adıyla şenlik alanı olarak kullanıldı. Sultan I. Ahmed'in Mimar Sedefkâr Mehmed Ağa'ya yaptırdığı altı minareli cami meydanın güneyinde yükselince semt onun adıyla anılmaya başladı. Ayasofya, Yerebatan Sarnıcı ve Dikilitaş aynı semtte, kentin üç bin yıllık katmanlarını yan yana sergiler.
source: Evliya Çelebi Seyahatnâmesi; Sultan Ahmed Camii vakfiyesi (olgu)
coords: 41.0054,28.9768

@Eyüpsultan|semt|İstanbul|Marmara||ar
chain: el:Kosmídion>ota:Eyüp>cum:Eyüpsultan>tr:Eyüpsultan
era: Osmanlı dönemi (15. yy)
meaning: Hz. Muhammed'in sancaktarı Ebû Eyyûb el-Ensârî'nin adından; Arapça Ayyūb (Eyüp)
story: 674 yılındaki Arap kuşatmasında vefat eden sahabe Ebû Eyyûb el-Ensârî'nin kabrinin fetihten sonra Akşemseddin tarafından bulunduğu anlatılır; Fatih buraya türbe ve cami yaptırdı. Bizans döneminde Kosmidion adlı bir manastır bölgesi olan semt, Osmanlı padişahlarının kılıç kuşandığı kutsal alan oldu. Pierre Loti'nin oturduğu kahve ve Haliç manzarası semtin bir başka yüzüdür; 2017'de ilçe adına Sultan sözcüğü eklendi.
source: Fetih kronikleri (Tursun Bey); Evliya Çelebi Seyahatnâmesi
coords: 41.0484,28.9335

@Fatih|semt|İstanbul|Marmara||ar
chain: ar:al-Fātiḥ>ota:Fatih>tr:Fatih
era: Osmanlı dönemi (15. yy)
meaning: Arapça fātiḥ "fetheden, açan": Fatih Sultan Mehmed'in unvanı; onun yaptırdığı külliyenin çevresi
story: II. Mehmed 1453 fethinden sonra Fatih "fetheden" unvanını aldı ve Havariyyun Kilisesi'nin yerine 1463–1470 arasında kendi adını taşıyan külliyeyi yaptırdı. Caminin çevresinde gelişen semt bu adla anıldı; 1928'de kurulan ilçe, tarihî yarımadanın tamamını kapsar. Fetih sözcüğü Arapça f-t-ḥ "açmak" kökünden gelir.
source: Tursun Bey, Târîh-i Ebü'l-Feth; Evliya Çelebi Seyahatnâmesi
coords: 41.0186,28.9397

@Bakırköy|semt|İstanbul|Marmara||tr
chain: el:Hébdomon>el:Makrochṓrion>ota:Makriköy>cum:Bakırköy>tr:Bakırköy
era: Bizans dönemi (4. yy)
meaning: Osmanlı adı Makriköy, Rumca makrochōrion "uzun köy"den; 1925'te ses benzerliğiyle Bakırköy yapıldı
story: Bizans başkentinin yedinci mil taşındaki Hebdomon, imparatorların taç giydiği saray ve kışla bölgesiydi. Rumların "uzun köy" dediği Makrochorion, Osmanlı'da Makriköy olarak yaşadı. 1925'te Rumca adlar değiştirilirken ses benzerliğinden yararlanılarak Bakırköy adı verildi. Baruthane, Yeşilköy (Ayastefanos) ve Atatürk Havalimanı ilçenin sınırlarındadır.
source: Bizans tören kayıtları (De Ceremoniis); 1925 tarihli ad değişikliği kararı
coords: 40.9800,28.8719

@Kartal|semt|İstanbul|Marmara||el
chain: el:Kartalímēn>ota:Kartal>tr:Kartal
era: Bizans dönemi (12. yy)
meaning: Bizans dönemi Kartalimen liman adının Türkçe söyleyişi; halk Türkçe kartal kuşuyla açıklar
story: Marmara kıyısındaki balıkçı köyü Bizans kaynaklarında Kartalimen adıyla geçer; Türkçede adın ikinci yarısı düşmüş ve ad kartal kuşuyla özdeşleşmiştir. Osmanlı döneminde Üsküdar'a bağlı bir Rum ve Türk köyü olan Kartal, 1947'de ilçe oldu. Aydos Kalesi, Orhan Gazi döneminde fethedilen Bizans kalesidir.
source: Bizans kaynakları (olgu); Osmanlı Üsküdar kadı sicilleri
coords: 40.8878,29.1872

@Pendik|semt|İstanbul|Marmara||el
chain: el:Panteíchion>ota:Pendik>tr:Pendik
era: Bizans dönemi (6. yy)
meaning: Yunanca pán "tüm" + teíchos "sur": "her yanı surlu yer"
story: İmparator Iustinianus'un tarihçisi Prokopios, Marmara kıyısında Panteichion adlı surlu bir yerleşimden söz eder; ad "her tarafı duvarla çevrili" anlamına gelir. Türkçe söyleyişte Pendik biçimini alan köy, Osmanlı'da Rum balıkçılarıyla bilinirdi. Sabiha Gökçen Havalimanı ve tersane ilçenin bugünkü kimliğidir.
source: Prokopios, Yapılar Üzerine; Osmanlı Üsküdar kadı sicilleri (olgu)
coords: 40.8775,29.2333

@Sarıyer|semt|İstanbul|Marmara||tr
chain: ota:Sarıyar>ota:Sarıyer>tr:Sarıyer
era: Osmanlı dönemi (17. yy)
meaning: "Sarı yar": koydaki sarı renkli maden toprağından ya da sarı kayalıklı yardan
story: Boğaz'ın Karadeniz'e açılan ucundaki köy, Evliya Çelebi'de sarı renkli toprağı ve altın madenine benzeyen kayalarıyla anılır; ad sarı ve yar "dik kıyı" sözcüklerinden gelir, zamanla yer biçimine dönüşmüştür. Osmanlı'da balıkçı dalyanları ve yalılarıyla bilinen Sarıyer, Rumeli Hisarı ve Telli Baba türbesini kapsar. Belgrad Ormanı'nın su kemerleri İstanbul'un suyunu buradan taşırdı.
source: Evliya Çelebi Seyahatnâmesi I. cilt; Osmanlı Boğaziçi kayıtları (olgu)
coords: 41.1670,29.0570

@Şişli|semt|İstanbul|Marmara||tr
chain: ota:Şişçi>ota:Şişli>tr:Şişli
era: Osmanlı dönemi (18. yy)
meaning: Burada şiş (kebap şişi, demir çubuk) yapan ustaların "Şişçi" lakabından; -li ekiyle semt adı olmuştur
story: 18. yüzyılda Beyoğlu'nun kuzeyindeki tarlalarda şiş imal eden bir ustanın köşkü ve çevresi "Şişçi" diye anılıyordu; halk ağzında Şişli biçimine dönüşen ad 19. yüzyıl sonunda tramvay hattıyla gelişen semte verildi. Türkçe şiş sözcüğü Eski Türkçe sış "kızartma şişi" biçiminden gelir ve Balkan dillerine de geçmiştir. Atatürk'ün 1918–1919'da oturduğu ev müzedir.
source: Osmanlı Beyoğlu kayıtları (olgu); Dîvânu Lugâti't-Türk (sış)
coords: 41.0602,28.9877

@Kuzguncuk|semt|İstanbul|Marmara||tr
chain: el:Chrysokéramos>ota:Kuzguncuk>tr:Kuzguncuk
era: Osmanlı dönemi (16. yy)
meaning: Türkçe kuzgun + -cuk: fetih döneminde burada yaşayan Kuzgun Baba adlı bir erenin lakabından
story: Bizans'ta altın yaldızlı kiremitli kilisesiyle Chrysokeramos "altın kiremit" diye anılan koy, Osmanlı'da burada yaşayan Kuzgun Baba adlı bir dervişin lakabıyla Kuzguncuk adını aldı. 17. yüzyıldan sonra Yahudi, Rum ve Ermeni cemaatlerinin bir arada yaşadığı semt, ahşap evleri ve cami-kilise-sinagog üçlüsüyle bilinir.
source: Evliya Çelebi Seyahatnâmesi; Bizans kaynakları (Chrysokeramos)
coords: 41.0356,29.0303

@Taksim|semt|İstanbul|Marmara||ar
chain: ar:taqsīm>ota:Taksim (Maksem)>tr:Taksim
era: Osmanlı dönemi (1732)
meaning: Arapça taqsīm "bölüştürme": Belgrad Ormanı'ndan gelen suyun semtlere dağıtıldığı su taksim yapısından
story: I. Mahmud 1732'de Belgrad Ormanı'ndan getirilen suyu Beyoğlu'nun mahallelerine bölüştüren taş bir taksim (maksem) yapısı yaptırdı; meydan adını bu yapıdan aldı. Taksim sözcüğü Arapça q-s-m "bölmek" kökündendir ve müzikte de aynı adla kullanılır. Cumhuriyet Anıtı (1928) ve Gezi Parkı meydanın Cumhuriyet dönemi simgeleridir.
source: Osmanlı su yolu defterleri (Taksim Maksemi, 1732); Osmanlı Beyoğlu kayıtları
coords: 41.0369,28.9850

@Kasımpaşa|semt|İstanbul|Marmara||ar
chain: ota:Güzelce Kasım Paşa Mahallesi>ota:Kasımpaşa>tr:Kasımpaşa
era: Osmanlı dönemi (16. yy)
meaning: Kanuni döneminde semti imar ettiren Güzelce Kasım Paşa'nın adından; Arapça Qāsim "paylaştıran"
story: Haliç'in kuzey kıyısındaki tersane bölgesi, Kanuni'nin veziri Güzelce Kasım Paşa'nın 1530'larda yaptırdığı cami ve hamam çevresinde gelişti. Osmanlı donanmasının Tersane-i Âmire'si ve Kaptan Paşa dairesi burada olduğu için semt denizcilerin yurduydu; "Kasımpaşalı" deyişi bu geleneği yansıtır. Kasım adı Arapça q-s-m kökünden gelir.
source: Evliya Çelebi Seyahatnâmesi; Tersane-i Âmire kayıtları (olgu)
coords: 41.0330,28.9680

@Tophane|semt|İstanbul|Marmara||fa
chain: ota:Tophâne-i Âmire>tr:Tophane
era: Osmanlı dönemi (15. yy)
meaning: Türkçe top + Farsça hāne "ev, atölye": Osmanlı devletinin top döküm atölyesinin bulunduğu yer
story: Fatih'in fetihten hemen sonra Galata surlarının dışında kurdurduğu top dökümhanesi, Kanuni döneminde genişletilerek Tophane-i Âmire adını aldı. Semt, dökümhanenin adıyla anıldı; Kılıç Ali Paşa Camii ve Nusretiye Camii kıyıdaki Osmanlı yapılarıdır. Hane öğesi aynı yapıyla Darphane, Baruthane ve Tersane adlarında da görülür.
source: Osmanlı Tophane-i Âmire defterleri (olgu); Evliya Çelebi Seyahatnâmesi
coords: 41.0268,28.9815

@İstanbul Boğazı|boğaz|İstanbul|Marmara||tr
chain: el:Bósporos>la:Bosporus>ota:Boğaziçi>tr:İstanbul Boğazı
era: Antik dönem (MÖ 1. binyıl)
meaning: Türkçe boğaz "dar geçit"; Yunanca Bósporos "öküz geçidi" (İo söylencesi)
story: Yunan söylencesinde Zeus'un ineğe dönüştürdüğü İo'nun yüzerek geçtiği su yolu Bosporos "öküz geçidi" diye adlandırıldı; Herodotos Pers kralı Dareios'un buraya kurdurduğu gemi köprüsünü anlatır. Türkçede boğaz sözcüğü hem beden organı hem de dar deniz geçidi anlamındadır ve Eski Türkçe boguz biçiminden gelir; Osmanlı'da Boğaziçi, iki kıyıdaki yalı ve köyleri anlatırdı. Rumeli ve Anadolu hisarları geçidin iki kilididir.
source: Herodotos IV; Evliya Çelebi Seyahatnâmesi I. cilt; Pîrî Reis, Kitâb-ı Bahriye
coords: 41.1000,29.0700

@Haliç|körfez|İstanbul|Marmara||ar
chain: el:Chrysókeras>la:Chrysoceras>ota:Haliç>tr:Haliç
era: Antik dönem (MÖ 1. binyıl)
meaning: Arapça ḫalīc "körfez, koy"; Yunanca Chrysokeras "Altın Boynuz" adıyla ünlüdür
story: Byzantion'u yarımada yapan derin koy, Yunanlılarca boynuz biçimi ve zengin balıkçılığı nedeniyle Chrysokeras "Altın Boynuz" diye adlandırıldı; Avrupa dillerindeki Golden Horn bu adın çevirisidir. Osmanlı, Arapça "körfez" anlamındaki ḫalīc sözcüğünü özel ad olarak kullandı. 1453'te gemilerin karadan yürütülüp koya indirilmesi fetih anlatılarının ünlü sahnesidir; tersane ve Fener-Balat kıyıları koyun iki yakasıdır.
source: Strabon, Geographika VII; Fetih kronikleri; Evliya Çelebi Seyahatnâmesi
coords: 41.0300,28.9500

@Büyükada|ada|İstanbul|Marmara||tr
chain: el:Prínkipos>ota:Büyükada>tr:Büyükada
era: Bizans dönemi (9. yy)
meaning: Türkçe "büyük ada": Prens Adaları'nın en büyüğü; Rumca Prinkipo "prens adası"
story: Bizans döneminde sürgün edilen imparatoriçe ve prenslerin manastırlara kapatıldığı adaya Prinkipos "prens adası" dendi; bütün takımadanın Prens Adaları adı buradan gelir. Türkçede adanın büyüklüğü doğrudan ad oldu. 19. yüzyılda Rum ve Levanten yazlıkçıların ahşap köşkleriyle dolan ada, 1929–1933 arasında Troçki'nin sürgün yeriydi. Aya Yorgi Manastırı adanın tepesindedir.
source: Bizans kronikleri (olgu); Evliya Çelebi Seyahatnâmesi
coords: 40.8619,29.1222

# ===================================================================== MARMARA / DİĞER
@Gelibolu|ilçe|Çanakkale|Marmara||el
chain: el:Kallípolis>la:Callipolis>ota:Gelibolu>tr:Gelibolu
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca kallí- "güzel" + pólis "şehir": "güzel şehir"
story: Trakya Khersonesos'unun en dar yerindeki liman kenti, Yunanca "güzel şehir" anlamındaki Kallipolis adını taşıyordu. 1354'te Süleyman Paşa'nın bir depremle yıkılan kaleyi ele geçirmesi Osmanlı'nın Rumeli'ye geçişinin başlangıcıdır; Türkçe söyleyişte Gelibolu olan ad -polis öğesini korur. Osmanlı donanmasının ilk üssü ve Pîrî Reis'in doğduğu kenttir; 1915 Çanakkale Savaşları yarımadanın adıyla anılır.
source: Strabon, Geographika VII; Pîrî Reis, Kitâb-ı Bahriye; Âşıkpaşazâde Tarihi
coords: 40.4103,26.6703

@Çanakkale Boğazı|boğaz|Çanakkale|Marmara||tr
chain: el:Hellḗspontos>el:Dardanéllia>ota:Kal'a-i Sultâniye Boğazı>tr:Çanakkale Boğazı
era: Antik dönem (MÖ 1. binyıl)
meaning: Türkçe boğaz "dar geçit" + Çanakkale; Yunanca Hellespontos "Helle'nin denizi", Batı dillerinde Dardanel (Dardanos kentinden)
story: Söylenceye göre altın postlu koçun sırtından düşen Helle'nin boğulduğu su yolu Hellespontos "Helle'nin denizi" diye anıldı; Pers kralı Kserkses MÖ 480'de buradan gemi köprüsüyle geçti. Batı dillerindeki Dardanelles, Asya kıyısındaki antik Dardanos kentinin adından gelir. Türkçe ad, boğazın en dar yerindeki Çanakkale kentinden alınmıştır. 1915'te boğazı zorlayan İtilaf donanması burada durduruldu.
source: Herodotos VII; Strabon, Geographika XIII; Pîrî Reis, Kitâb-ı Bahriye
coords: 40.2000,26.4000

@Troya|antik_kent|Çanakkale|Marmara||hit
chain: hit:Wiluša / Taruiša>el:Troía / Ílion>la:Troia / Ilium>ota:Truva>tr:Troya
era: Tunç Çağı (MÖ 3. binyıl)
meaning: Hitit metinlerindeki Wiluša (İlion) ve Taruiša (Troya) adlarından; Homeros'un İlyada'sının kenti
story: Hisarlık tepesindeki dokuz katmanlı höyük, Homeros'un İlyada'da anlattığı Troya Savaşı'nın kentiyle özdeşleştirilir; Hitit belgelerinde Batı Anadolu'daki Wiluša krallığı ve Taruiša yer adı, Yunanca İlion ve Troia adlarıyla eşleştirilir. Heinrich Schliemann 1870'te burada kazıya başladı. Türkçedeki Truva biçimi Fransızca Troie söyleyişinden, Troya ise doğrudan Yunancadan gelir. Tahta at söylencesi dünya dillerine "Truva atı" deyimini kazandırmıştır.
source: Homeros, İlyada; Hitit çivi yazılı belgeleri (Alaksandu antlaşması); Strabon, Geographika XIII
coords: 39.9575,26.2389

@Bozcaada|ada|Çanakkale|Marmara||tr
chain: el:Ténedos>ota:Bozcaada>tr:Bozcaada
era: Osmanlı dönemi (15. yy)
meaning: Türkçe boz "gri, çorak" + -ca + ada: "bozumsu ada"; antik adı Tenedos
story: Homeros'un andığı Tenedos, Troya Savaşı'nda Yunanlıların gemilerini sakladığı adadır; Tenes söylencesinden adını alır. Fatih döneminde Osmanlı'ya katılan adaya Türkler kurak görünümünden ötürü Bozcaada dediler; Venedik 1656'da kısa süre adayı aldı. Bağcılık ve kalesiyle bilinen adada Rum ve Türk kültürleri yüzyıllarca birlikte yaşadı.
source: Homeros, İlyada; Pîrî Reis, Kitâb-ı Bahriye; Evliya Çelebi Seyahatnâmesi
coords: 39.8333,26.0667

@Gökçeada|ada|Çanakkale|Marmara||tr
chain: el:Ímbros>ota:İmroz>cum:Gökçeada>tr:Gökçeada
era: Cumhuriyet dönemi (1970)
meaning: Türkçe gökçe "mavimsi, güzel" + ada; 1970'e kadar antik Imbros adından gelen İmroz
story: Ege'nin kuzeyindeki Imbros, Homeros'ta Poseidon'un atlarını sakladığı ada olarak geçer; Osmanlı belgelerinde İmroz yazılır. 1923 Lozan Antlaşması'yla Türkiye'de kalan ada, 1970'te Gökçeada adını aldı. Gökçe sözcüğü Eski Türkçe kök "mavi" kökünden türemiştir; Türkiye'nin en büyük adasıdır ve organik tarımıyla bilinir.
source: Homeros, İlyada XIII; Pîrî Reis, Kitâb-ı Bahriye; 1970 tarihli ad değişikliği kararı
coords: 40.1667,25.9000

@Assos|antik_kent|Çanakkale|Marmara||el
chain: el:Ássos>la:Assus>ota:Behramkale>tr:Assos
era: Antik dönem (MÖ 7. yy)
meaning: Lesboslu kolonistlerin kurduğu Assos kentinin adı; Osmanlı köyü Behramkale, Behram adlı bir beyin kalesinden
story: Lesbos adasından gelen kolonistlerin MÖ 7. yüzyılda kurduğu Assos, Aristoteles'in üç yıl felsefe öğrettiği kenttir; Athena Tapınağı andezit sütunlarıyla tepede durur. Köyün Türkçe adı Behramkale, 14. yüzyılda buradaki kaleyi onaran Behram Bey'e bağlanır; Hüdavendigâr Camii aynı dönemdendir. Assos adı, bölgenin Yunanca öncesi diline aittir.
source: Strabon, Geographika XIII; Osmanlı Biga sancağı tahrirleri (Behramkale)
coords: 39.4875,26.3361

@İznik|ilçe|Bursa|Marmara||el
chain: el:Níkaia>la:Nicaea>el:eis Níkaian>ota:İznik>tr:İznik
era: Helenistik dönem (MÖ 4. yy)
meaning: Lysimakhos'un eşi Nikaia'nın adından; Rumca "eis Nikaian" (Nikaia'ya) söyleyişinden İznik
story: Büyük İskender'in komutanı Lysimakhos MÖ 301'de kente eşi Nikaia'nın adını verdi; 325'teki Birinci Nikaia Konsili Hristiyan inanç bildirgesini burada belirledi. 1081–1097 arasında Anadolu Selçuklularının ilk başkentiydi; Orhan Gazi 1331'de kenti aldı ve ilk Osmanlı medresesini burada kurdu. Rumların "eis Nikaian" söyleyişi Türkçede İznik oldu. 16. yüzyıl İznik çinileri Osmanlı sanatının doruğudur.
source: Strabon, Geographika XII; Nikaia Konsili kayıtları (olgu); Evliya Çelebi Seyahatnâmesi
coords: 40.4294,29.7211

@Mudanya|ilçe|Bursa|Marmara||el
chain: el:Myrleía>el:Apámeia>it:Montagna>ota:Mudanya>tr:Mudanya
era: Antik dönem (MÖ 1. binyıl)
meaning: Bitinya kralı I. Prusias'ın eşi Apama'nın adını taşıyan Apameia'nın İtalyanca Montagna ve Türkçe Mudanya söyleyişi
story: Kolophonluların kurduğu Myrleia, Bitinya kralı I. Prusias tarafından eşi Apama'nın adıyla Apameia olarak yeniden adlandırıldı. Ceneviz ve Venedik portolan haritalarında Montagna yazılan liman, Türkçede Mudanya oldu. Bursa'nın iskelesi olan kasabada 11 Ekim 1922'de Mudanya Ateşkes Antlaşması imzalandı; ipek ve zeytin ticaretiyle bilinir.
source: Strabon, Geographika XII; Ceneviz portolan haritaları (olgu); Mudanya Mütarekesi belgeleri (1922)
coords: 40.3756,28.8822

@İnegöl|ilçe|Bursa|Marmara||el
chain: el:Angelokómē>ota:Ezinegöl>ota:İnegöl>tr:İnegöl
era: Bizans dönemi (13. yy)
meaning: Bizans köyü Angelokome adının Türkçe söyleyişi; halk Türkçe in "mağara" ve göl ile açıklar
story: Osman Gazi'nin ilk çarpıştığı tekfurlardan birinin kalesi Angelokome, Uludağ'ın güneydoğusundaki ovada yer alıyordu; Osmanlı belgelerinde Ezinegöl, sonra İnegöl biçiminde yazıldı. Halk adı "mağaralı göl" diye yorumlar; bu bir halk etimolojisidir. İshak Paşa Külliyesi ve mobilya sanayisi kasabanın kimliğidir.
source: Âşıkpaşazâde Tarihi; Osmanlı Hüdavendigâr sancağı tahrirleri
coords: 40.0781,29.5133

@Uludağ|dağ|Bursa|Marmara||tr
chain: el:Ólympos (Mysías)>ota:Keşiş Dağı>cum:Uludağ>tr:Uludağ
era: Cumhuriyet dönemi (1925)
meaning: Türkçe ulu "yüce, büyük" + dağ; antik adı Mysia Olympos'u, Osmanlı adı Keşiş Dağı
story: Bursa'nın üstünde 2543 metreye yükselen dağ, antik çağda Mysia Olympos'u adıyla anılıyordu; Bizans döneminde yamaçlarındaki manastırlar nedeniyle Osmanlı'da Keşiş Dağı dendi. 1925'te ad, Eski Türkçe ulug "büyük" kökünden gelen ulu sözcüğüyle Uludağ olarak değiştirildi. Türkiye'nin ilk kayak merkezi 1930'larda burada kuruldu.
source: Strabon, Geographika XII; Evliya Çelebi Seyahatnâmesi; 1925 tarihli ad değişikliği kararı
coords: 40.0667,29.2167

@Edremit|ilçe|Balıkesir|Marmara||lyd
chain: lyd:Adramys (kişi adı)>el:Adramýttion>la:Adramyttium>ota:Edremid>tr:Edremit
era: Antik dönem (MÖ 7. yy)
meaning: Lidya kralı Alyattes'in oğlu Adramys'in kurduğu Adramyttion kentinin adından
story: Lidyalı prens Adramys'in kurduğu Adramyttion, Kaz Dağı'nın eteğindeki körfeze adını verdi; Aziz Pavlus'un Roma yolculuğu bu kentin gemisiyle başladı. Karesi Beyliği 14. yüzyılda kenti aldı; Türkçede Edremid, sonra Edremit biçimi yerleşti. Zeytinyağı üretimi ve Kaz Dağı (İda) söylenceleri yörenin kimliğidir.
source: Strabon, Geographika XIII; Resullerin İşleri 27 (olgu); Osmanlı Karesi sancağı tahrirleri
coords: 39.5961,27.0244

@Bandırma|ilçe|Balıkesir|Marmara||el
chain: el:Pánormos>ota:Panderma>ota:Bandırma>tr:Bandırma
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca pánormos "her rüzgârda sığınılabilen liman"
story: Kyzikos'un yanındaki doğal liman, Yunanca "her gemiye uygun liman" anlamındaki Panormos adını taşıyordu; aynı ad Sicilya'daki Palermo'nun da kaynağıdır. Osmanlı belgelerinde Panderma, halk ağzında Bandırma olan kasaba, Marmara'nın güney kıyısındaki en büyük limandır. 19 Mayıs 1919'da Mustafa Kemal'i Samsun'a götüren vapur bu limanın adını taşıyordu.
source: Strabon, Geographika XII; Pîrî Reis, Kitâb-ı Bahriye; Osmanlı salnameleri
coords: 40.3522,27.9767

@Ayvalık|ilçe|Balıkesir|Marmara||tr
chain: el:Kydōníai>ota:Ayvalık>tr:Ayvalık
era: Osmanlı dönemi (16. yy)
meaning: Türkçe ayva + -lık "ayva bahçesi"; Rumca Kydonies aynı anlamın karşılığıdır (kydṓnion "ayva")
story: Ege kıyısındaki kasaba, Rumca "ayvalıklar" anlamına gelen Kydonies adıyla anılırdı; Türkçe Ayvalık adı aynı anlamı taşır ve iki ad yüzyıllarca yan yana yaşadı. 18. yüzyılda özerk bir Rum kasabası olarak zeytinyağı ticaretiyle zenginleşti; 1923 mübadelesinden sonra Midilli ve Giritli Türkler yerleşti. Cunda (Alibey) Adası ve Şeytan Sofrası kasabanın simgeleridir.
source: Osmanlı Karesi sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi; mübadele belgeleri (olgu)
coords: 39.3192,26.6953

@Erdek|ilçe|Balıkesir|Marmara||el
chain: el:Artákē>la:Artace>ota:Erdek>tr:Erdek
era: Antik dönem (MÖ 1. binyıl)
meaning: Miletos kolonisi Artake'nin adından; Kapıdağ Yarımadası'nın güneyindeki liman
story: Kyzikos'un hemen batısında Miletliler tarafından kurulan Artake, Herodotos'ta Pers donanmasının uğrak yeri olarak geçer. Kyzikos'un yıkılmasından sonra bölgenin merkezi olan kasaba, Türkçede Erdek biçimini aldı. Kapıdağ Yarımadası'ndaki Kyzikos kalıntıları ve Marmara Adası'nın mermer ocakları yöreyi tanımlar.
source: Herodotos IV; Strabon, Geographika XII; Pîrî Reis, Kitâb-ı Bahriye
coords: 40.3997,27.7939

@Kapıdağ Yarımadası|yarımada|Balıkesir|Marmara||tr
chain: el:Arktónnēsos>el:Kýzikos>ota:Kapu Dağı>tr:Kapıdağ Yarımadası
era: Antik dönem (MÖ 1. binyıl)
meaning: Türkçe kapı + dağ: Marmara'ya açılan "kapı" konumundaki dağlık yarımada; antik adı Arktonnesos "ayı adası"
story: Antik çağda Arktonnesos "ayı adası" olarak bilinen ada, Kyzikos kentinin iki köprüyle bağlandığı bir yerleşim yeriydi; alüvyonlarla anakaraya bağlanıp yarımadaya dönüştü. Türkler, Marmara'nın güney kıyısında kapı gibi duran dağlık kütleye Kapıdağ dediler. Kyzikos'un Hadrianus Tapınağı antik dünyanın en büyük tapınaklarından biriydi.
source: Strabon, Geographika XII; Plinius, Naturalis Historia V
coords: 40.4500,27.8000

@Marmara Adası|ada|Balıkesir|Marmara||el
chain: el:Prokónnēsos>el:Mármara>ota:Marmara>tr:Marmara Adası
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca mármaron "mermer": adanın ünlü beyaz mermer ocaklarından; Marmara Denizi'nin adı da buradan gelir
story: Antik Prokonnesos adası, Roma ve Bizans başkentinin saray ve kiliselerini süsleyen beyaz mermerin çıkarıldığı yerdi; Yunanca mármaron "parlayan taş" sözcüğü adaya, sonra bütün denize ad oldu. Mermer sözcüğü Türkçeye de Yunancadan geçmiştir. Osmanlı'da mermer ocakları işletilmeye devam etti; Pîrî Reis adayı Marmara adıyla haritalar.
source: Strabon, Geographika XIII; Pîrî Reis, Kitâb-ı Bahriye
coords: 40.6000,27.5500

@Çorlu|ilçe|Tekirdağ|Marmara||el
chain: el:Tzoúroulon>la:Tzurulum>ota:Çorlu>tr:Çorlu
era: Roma dönemi (1. yy)
meaning: Bizans Yunancası Tzouroulon kale adının Türkçe söyleyişi; Trakya'daki Roma yol istasyonu
story: İstanbul'dan Edirne'ye giden Roma yolu üzerindeki Tzurulum, Bizans döneminde Trakya'nın önemli kalelerindendi. Türkçede Çorlu biçimini alan kasaba 1357'de Osmanlı'ya katıldı; 1511'de Yavuz Sultan Selim ile babası II. Bayezid'in orduları burada karşılaştı. Trakya'nın sanayi merkezlerinden biridir.
source: Bizans kaynakları (Prokopios, olgu); Osmanlı kronikleri (Çorlu Savaşı, 1511)
coords: 41.1592,27.8000

@Lüleburgaz|ilçe|Kırklareli|Marmara||el
chain: el:Arkadioúpolis>el:Bergoúle>ota:Lüle Burgaz>tr:Lüleburgaz
era: Roma dönemi (4. yy)
meaning: Yunanca pýrgos "kule" sözcüğünden Türkçe burgaz + Farsça lūle "boru": "lüleli kale", lüle taşı ya da su borusundan
story: İmparator Arcadius'un adıyla Arkadioupolis olarak anılan Trakya kasabası, Bizans'ın son döneminde Bergoule adını taşıyordu; Türkçedeki burgaz sözcüğü Yunanca pýrgos "kule, kale" sözcüğünden gelir. Kasabada yapılan lüle taşı pipo lüleleri ya da çeşmelerin lülelerinden dolayı başına lüle sözcüğü eklendi. Sokollu Mehmed Paşa'nın Mimar Sinan'a yaptırdığı külliye (1569) kasabanın merkezidir.
source: Evliya Çelebi Seyahatnâmesi; Sokollu Mehmed Paşa vakfiyesi (olgu)
coords: 41.4035,27.3575

@Silivri|ilçe|İstanbul|Marmara||thr
chain: thr:Sēlymbría>el:Sēlymbría>ota:Silivri>tr:Silivri
era: Antik dönem (MÖ 7. yy)
meaning: Trakça -bria "kent" öğesiyle "Selys'in kenti": Megaralı kolonistlerin Trak adını koruduğu yerleşim
story: Megaralıların Byzantion'dan önce kurduğu Selymbria, Trak dilinde "kent" anlamına gelen -bria öğesini taşır ve söylenceye göre kurucu Selys'e bağlanır; aynı öğe Mesembria (Nesebar) adında da görülür. Osmanlı'da Silivri biçimini alan kasaba, yoğurduyla ünlendi. Bizans surlarının kalıntıları ve Pîrî Mehmed Paşa Camii kasabanın tarihî yapılarıdır.
source: Strabon, Geographika VII; Pîrî Reis, Kitâb-ı Bahriye; Evliya Çelebi Seyahatnâmesi
coords: 41.0731,28.2467

@Şile|ilçe|İstanbul|Marmara||el
chain: el:Chēlḗ>ota:Şile>tr:Şile
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca chēlḗ "pençe, dalgakıran": kıyıdaki pençe biçimli kayalık burundan
story: Karadeniz kıyısındaki balıkçı kasabası, antik Periplus metinlerinde Chele adıyla geçer; sözcük Yunancada hem yengeç pençesi hem de liman dalgakıranı anlamına gelir ve kasabanın kayalık burnunu anlatır. Osmanlı döneminde Şile bezi dokumacılığıyla tanınan kasabanın feneri (1860) Türkiye'nin en büyük deniz fenerlerindendir.
source: Arrianus, Periplus Ponti Euxini; Osmanlı Kocaeli sancağı tahrirleri
coords: 41.1764,29.6131

@Adapazarı|ilçe|Sakarya|Marmara||tr
chain: ota:Ada Köyü>ota:Adapazarı>tr:Adapazarı
era: Osmanlı dönemi (17. yy)
meaning: Türkçe ada + pazar: Sakarya ile Çark Suyu arasındaki "ada" benzeri alanda kurulan pazar yerinden
story: Sakarya Irmağı ile Sapanca Gölü'nden çıkan Çark Suyu'nun arasında kalan verimli ova, ada gibi görünen bir alandı; 17. yüzyılda burada kurulan pazar yeri çevresinde Adapazarı kasabası gelişti. Pazar sözcüğü Farsça bāzār'dan gelir. 1954'te kurulan Sakarya ilinin merkezi olan kent, 1999 depreminde ağır hasar gördü.
source: Evliya Çelebi Seyahatnâmesi; Osmanlı Kocaeli sancağı kayıtları (Ada kazası)
coords: 40.7806,30.4033

@Söğüt|ilçe|Bilecik|Marmara||tr
chain: el:Thēbásion>ota:Söğüt>tr:Söğüt
era: Osmanlı dönemi (13. yy)
meaning: Türkçe söğüt ağacı: Ertuğrul Gazi'nin Kayı boyuna kışlak olarak verilen söğütlük yöreden
story: Bizans'ın Thebasion adlı sınır kasabası, Selçuklu sultanının Ertuğrul Gazi'ye kışlak olarak verdiği Söğüt oldu; Osman Gazi'nin beyliği burada doğdu. Söğüt sözcüğü Eski Türkçe sögüt biçiminden gelir ve Dîvânu Lugâti't-Türk'te geçer. Ertuğrul Gazi türbesi ve her yıl düzenlenen Yörük şenlikleri kuruluş belleğini yaşatır.
source: Âşıkpaşazâde Tarihi; Dîvânu Lugâti't-Türk (sögüt); Osmanlı Sultanönü sancağı tahrirleri
coords: 40.0194,30.1814

@İzmit|ilçe|Kocaeli|Marmara||el
chain: el:Nikomḗdeia>la:Nicomedia>el:eis Nikomḗdeian>ota:İznikmid>ota:İzmit>tr:İzmit
era: Helenistik dönem (MÖ 3. yy)
meaning: Bitinya kralı I. Nikomedes'in kurduğu Nikomedeia'nın "eis Nikomedeian" söyleyişinden
story: I. Nikomedes'in MÖ 264'te kurduğu Nikomedeia, Diocletianus'un Roma İmparatorluğu'nun doğu başkenti yaptığı kenttir; Hannibal yakınlarda ölmüş, Constantinus burada vaftiz edilmiştir. Rumların "eis Nikomedeian" söyleyişi Türkçede İznikmid, sonra İzmit oldu; Orhan Gazi 1337'de kenti aldı. Osmanlı tersanesi ve Pertev Paşa Camii (Mimar Sinan) kentin Osmanlı mirasıdır.
source: Lactantius, De Mortibus Persecutorum; Evliya Çelebi Seyahatnâmesi; Osmanlı Kocaili sancağı kayıtları
coords: 40.7654,29.9408

@Hereke|semt|Kocaeli|Marmara||el
chain: el:Chárax>ota:Hereke>tr:Hereke
era: Bizans dönemi (6. yy)
meaning: Yunanca chárax "kazıklı sur, palanka": İzmit Körfezi kıyısındaki Bizans palankasından
story: Prokopios'un andığı Charax, körfez kıyısında kazıklı surla korunan bir Bizans istasyonuydu; adı Türkçede Hereke'ye dönüştü. 1843'te Sultan Abdülmecid'in kurdurduğu Hereke Fabrika-i Hümayunu'nun ipek halıları Osmanlı saraylarını döşedi; Hereke halısı dünya markası oldu.
source: Prokopios, Yapılar Üzerine; Hereke Fabrika-i Hümayunu kayıtları (olgu)
coords: 40.7906,29.6203

@Gebze|ilçe|Kocaeli|Marmara||el
chain: el:Dakíbyza>ota:Gekbüze>ota:Gebze>tr:Gebze
era: Bizans dönemi (10. yy)
meaning: Bizans dönemi Dakibyza kasaba adının Türkçe söyleyişi; Hannibal'in mezarının bulunduğu Libyssa'ya komşu
story: Marmara kıyısındaki Dakibyza, Osmanlı belgelerinde Gekbüze biçimiyle geçer ve halk ağzında Gebze'ye dönüştü. Kartacalı komutan Hannibal'in MÖ 183'te öldüğü Libyssa bugünkü Gebze sınırlarındadır; Çoban Mustafa Paşa Külliyesi (1523) kasabanın Osmanlı anıtıdır.
source: Plinius, Naturalis Historia V (Libyssa); Evliya Çelebi Seyahatnâmesi; Osmanlı kadı sicilleri
coords: 40.8028,29.4307

@Karamürsel|ilçe|Kocaeli|Marmara||tr
chain: ota:Kara Mürsel>tr:Karamürsel
era: Osmanlı dönemi (14. yy)
meaning: Orhan Gazi'nin ilk Osmanlı donanmasını kuran denizci komutanı Kara Mürsel Bey'in adından
story: İzmit Körfezi'nin güney kıyısındaki kasaba, 1320'lerde Osmanlı'nın ilk deniz gücünü oluşturan Kara Mürsel Bey'in adını taşır; onun adıyla anılan küçük savaş gemisi türü "karamürsel" Osmanlı denizcilik dilinde yaşamıştır. Kara, Türkçede esmer ya da güçlü anlamıyla lakap olarak kullanılırdı; Mürsel Arapça "gönderilmiş" demektir.
source: Âşıkpaşazâde Tarihi; Kâtip Çelebi, Tuhfetü'l-Kibâr (karamürsel gemileri)
coords: 40.6911,29.6164

@Uzunköprü|ilçe|Edirne|Marmara||tr
chain: ota:Ergene Köprüsü>ota:Uzunköprü>tr:Uzunköprü
era: Osmanlı dönemi (15. yy)
meaning: Türkçe uzun + köprü: II. Murad'ın Ergene Irmağı üzerine yaptırdığı 174 gözlü taş köprüden
story: II. Murad 1426–1443 arasında bataklık Ergene vadisini aşmak için 1392 metre uzunluğunda bir taş köprü yaptırdı; köprünün başında kurulan kasaba Ergene adıyla başladı, sonra köprüden dolayı Uzunköprü dendi. Dünyanın en uzun tarihî taş köprüsü sayılan yapı hâlâ kullanılmaktadır. Köprü sözcüğü Eski Türkçe köprüg biçiminden gelir.
source: Osmanlı kronikleri (II. Murad dönemi); Evliya Çelebi Seyahatnâmesi
coords: 41.2667,26.6833

@Enez|ilçe|Edirne|Marmara||el
chain: el:Aînos>la:Aenus>ota:Enez>tr:Enez
era: Antik dönem (MÖ 7. yy)
meaning: Homeros'un İlyada'da andığı Ainos kentinin adından; Meriç ağzındaki liman
story: Meriç'in Ege'ye döküldüğü yerdeki Ainos, Homeros'ta Trak müttefiklerinin kenti olarak geçer ve Aiol kolonistlerce MÖ 7. yüzyılda yeniden kuruldu. Fatih 1456'da Ceneviz Gattilusi ailesinden aldı; Türkçede Enez oldu. Bizans kalesi ve Ayasofya kilisesi kasabanın tepesindedir.
source: Homeros, İlyada IV; Herodotos VII; Pîrî Reis, Kitâb-ı Bahriye
coords: 40.7256,26.0831

@Vize|ilçe|Kırklareli|Marmara||thr
chain: thr:Bizýē>el:Bizýē>la:Bizya>ota:Vize>tr:Vize
era: Antik dönem (MÖ 1. binyıl)
meaning: Trak Astai kabilesinin başkenti Bizye'nin adından
story: Istranca eteklerindeki Bizye, Trak krallarının son başkentiydi ve Roma döneminde Trakya'nın yerel kral merkeziydi; Bizans'ın Küçük Ayasofya adlı kilisesi ve antik tiyatrosu kasabada durur. Türkçede Vize biçimini alan ad, Trak dilinin Anadolu'ya en yakın tanıklarındandır.
source: Strabon, Geographika VII; Plinius, Naturalis Historia IV; Osmanlı Vize sancağı tahrirleri
coords: 41.5733,27.7653

# ===================================================================== EGE
@Efes|antik_kent|İzmir|Ege||xlu
chain: xlu:Apaša>el:Éphesos>la:Ephesus>ota:Ayasuluk>tr:Efes
era: Tunç Çağı (MÖ 2. binyıl)
meaning: Hitit metinlerindeki Arzawa başkenti Apaša'nın adından; Yunanca Ephesos
story: Hitit belgelerinde Batı Anadolu'daki Arzawa krallığının başkenti olarak geçen Apaša, Yunan kolonistlerce Ephesos adıyla sürdürüldü. Artemis Tapınağı dünyanın yedi harikasından biriydi; Celsus Kitaplığı ve büyük tiyatro Roma döneminin eserleridir. Bizans'ta kent, Aziz Yuhanna'nın kilisesi nedeniyle Hagios Theologos diye anıldı; Türkler bunu Ayasuluk biçiminde söyledi. Efes biçimi Yunanca addan Türkçeye uyarlanmıştır.
source: Hitit çivi yazılı belgeleri (Arzawa); Strabon, Geographika XIV; Evliya Çelebi Seyahatnâmesi (Ayasuluk)
coords: 37.9411,27.3419

@Selçuk|ilçe|İzmir|Ege||tr
chain: el:Hágios Theológos>ota:Ayasuluk>cum:Selçuk>tr:Selçuk
era: Cumhuriyet dönemi (1914)
meaning: Selçuklu hanedanının adından; eski adı Ayasuluk, Rumca Hagios Theologos "Aziz İlahiyatçı (Yuhanna)"
story: Efes'in yanı başındaki tepede Aziz Yuhanna'nın mezarı üstüne Iustinianus'un yaptırdığı bazilika, Rumca "Aziz İlahiyatçı" anlamındaki Hagios Theologos adıyla anılırdı; Türkler bunu Ayasuluk biçiminde benimsediler ve Aydınoğulları burada İsa Bey Camii'ni (1375) yaptırdı. 1914'te kasabaya, Anadolu'yu Türkleştiren Selçuklu hanedanının adı verildi. Selçuk adı, hanedanın atası Selçuk Bey'den gelir.
source: Evliya Çelebi Seyahatnâmesi (Ayasuluk); İsa Bey Camii kitabesi (olgu); 1914 tarihli ad değişikliği
coords: 37.9500,27.3700

@Bergama|ilçe|İzmir|Ege||el
chain: el:Pérgamon>la:Pergamum>ota:Bergama>tr:Bergama
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca pérgamon "kale, yüksek yer" (Anadolu kökenli bir sözcük); parşömen sözcüğü bu kentin adından türemiştir
story: Attalos hanedanının başkenti Pergamon, Zeus Sunağı, Asklepion ve 200 bin rulolu kitaplığıyla Helenistik dünyanın kültür merkeziydi. Mısır papirüs ihracını kesince burada geliştirilen deri yazı malzemesi "pergamenē", Latince pergamenum, Fransızca parchemin ve Türkçe parşömen sözcüklerine kaynak oldu. Türkçede Bergama biçimini alan kent, halı dokumacılığıyla da ünlüdür.
source: Strabon, Geographika XIII; Plinius, Naturalis Historia XIII (parşömen); Evliya Çelebi Seyahatnâmesi
coords: 39.1206,27.1789

@Kuşadası|ilçe|Aydın|Ege||tr
chain: el:Neápolis>gen:Scala Nova>ota:Kuşadası>tr:Kuşadası
era: Osmanlı dönemi (17. yy)
meaning: Türkçe kuş + ada + -sı: limandaki Güvercinada'nın adından; Cenevizliler Scala Nova "yeni iskele" dediler
story: Efes limanının alüvyonla dolmasından sonra Cenevizli ve Venedikli tüccarlar bu koyda Scala Nova "yeni iskele" adıyla bir liman kurdular; Osmanlı 1413'te bölgeyi aldı ve Öküz Mehmed Paşa 1618'de kervansarayı yaptırdı. Türkçe ad, limanın ağzındaki kaleli küçük adanın (Güvercinada) adından gelir. Kuş sözcüğü Eski Türkçe kuş biçimiyle Orhun Yazıtları'nda geçer.
source: Pîrî Reis, Kitâb-ı Bahriye; Evliya Çelebi Seyahatnâmesi; Ceneviz portolan haritaları (olgu)
coords: 37.8597,27.2594

@Çeşme|ilçe|İzmir|Ege||fa
chain: el:Kýssos>fa:çeşme>ota:Çeşme>tr:Çeşme
era: Osmanlı dönemi (15. yy)
meaning: Farsça çeşme "pınar, göz": kıyıdaki tatlı su kaynaklarından; antik adı Kyssos
story: Sakız Adası'nın karşısındaki liman antik çağda Erythrai'ye bağlı Kyssos iskelesiydi. Türkler, gemicilerin su aldığı pınarlar nedeniyle kasabaya Farsça kökenli çeşme sözcüğüyle ad verdiler; çeşme, Farsça çeşm "göz" sözcüğünden gelir ve kaynak anlamı taşır. 1770 Çeşme Deniz Savaşı'nda Osmanlı donanması burada yakıldı; Ceneviz kalesini Bayezid onarmıştır.
source: Pîrî Reis, Kitâb-ı Bahriye; Evliya Çelebi Seyahatnâmesi; Osmanlı deniz savaşı kayıtları (1770)
coords: 38.3236,26.3031

@Foça|ilçe|İzmir|Ege||el
chain: el:Phṓkaia>la:Phocaea>gen:Foggia Vecchia>ota:Foça>tr:Foça
era: Antik dönem (MÖ 8. yy)
meaning: Yunanca phṓkē "fok balığı": koylarında yaşayan Akdeniz foklarından Phokaia
story: İon kenti Phokaia, Marsilya (Massalia) ve İspanya'daki kolonileri kuran cesur denizcilerin yurduydu; adı kıyılarında bugün de yaşayan fok balıklarından gelir. 13.–15. yüzyıllarda Ceneviz şap ticaretinin merkezi olan kasaba, Türkçede Foça oldu. Siren Kayalıkları, Homeros'un Odysseia'sındaki sirenlerle ilişkilendirilir.
source: Herodotos I; Strabon, Geographika XIV; Pîrî Reis, Kitâb-ı Bahriye
coords: 38.6697,26.7567

@Bodrum|ilçe|Muğla|Ege||la
chain: xcr:Halikarnassós>la:Petronium>ota:Bodrum>tr:Bodrum
era: Osmanlı dönemi (15. yy)
meaning: Aziz Petrus Kalesi'nin Latince adı Petronium'un Türkçe söyleyişi; halk Türkçe bodrum "mahzen" ile açıklar
story: Antik Halikarnassos'un kalıntıları üzerine Rodos Şövalyeleri 1402'de Aziz Petrus'a adanmış kaleyi yaptılar; kalenin Latince adı Petronium, Türkçede Bodrum biçimine dönüştü. Halk, Mausoleion'un yıkıntılarındaki mahzenlere bakarak adı Türkçe bodrum sözcüğüyle açıklar; bu bir halk etimolojisidir. Herodotos'un doğduğu kentin anıt mezarı Mausoleion, dünyanın yedi harikasındandı. Mavi yolculuk kültürü 20. yüzyılda burada doğdu.
source: Herodotos; Strabon, Geographika XIV; Pîrî Reis, Kitâb-ı Bahriye; Evliya Çelebi Seyahatnâmesi
coords: 37.0344,27.4305

@Halikarnassos|antik_kent|Muğla|Ege||xcr
chain: xcr:Halikarnassós>el:Halikarnassós>la:Halicarnassus>tr:Halikarnassos
era: Antik dönem (MÖ 1. binyıl)
meaning: Karya dilinden gelen kent adı; Karya satrabı Mausolos'un başkenti
story: Karya dilindeki adı Yunanca metinlerde Halikarnassos olarak geçen kent, satrap Mausolos'un başkentiydi; onun anıt mezarı Mausoleion, "mozole" sözcüğünü dünya dillerine kazandırdı. Tarihin babası Herodotos burada doğdu. Büyük İskender MÖ 334'te kenti kuşatıp aldı; kalıntıları bugünkü Bodrum'un altındadır.
source: Herodotos; Vitruvius, De Architectura II; Strabon, Geographika XIV
coords: 37.0375,27.4242

@Marmaris|ilçe|Muğla|Ege||unk
chain: el:Physkos>ota:Mermeris>ota:Marmaris>tr:Marmaris
era: Osmanlı dönemi (16. yy)
meaning: Kökeni tartışmalı; Yunanca mármaron "mermer" ile ya da Kanuni'nin kale için söylediği "mimar as" sözüyle (halk etimolojisi) açıklanır
story: Antik Physkos'un limanındaki kasaba, Osmanlı belgelerinde Mermeris biçiminde geçer; ad Yunanca mermer sözcüğüyle ilişkilendirilir. Halk anlatısı Kanuni'nin 1522 Rodos seferinde beğenmediği kale için "mimar as" dediğini söyler; bu bir halk etimolojisidir. Kale 1522'de Rodos seferinin üssü olarak yapıldı; yat limanı ve çam ormanları kasabanın bugünkü yüzüdür.
source: Pîrî Reis, Kitâb-ı Bahriye; Evliya Çelebi Seyahatnâmesi; Osmanlı Menteşe sancağı tahrirleri
coords: 36.8500,28.2744

@Fethiye|ilçe|Muğla|Ege||ar
chain: xlc:Telebehi>el:Telmēssós>el:Makrḗ>ota:Meğri>cum:Fethiye>tr:Fethiye
era: Cumhuriyet dönemi (1934)
meaning: 1914'te şehit düşen ilk Türk pilotlardan Fethi Bey'in adından; Arapça fatḥ "fetih"; eski adı Meğri (Rumca Makri "uzun")
story: Likya'nın Telmessos kenti kehanetleriyle ünlüydü; Bizans döneminde Makri "uzun" adıyla anılan liman, Osmanlı'da Meğri oldu. 1934'te kasabaya, 1914'te İstanbul-Kahire uçuşunda şehit düşen pilot Fethi Bey'in adı verildi. Kaya mezarları ve Ölüdeniz lagünü kasabanın simgeleridir; Likçe Telebehi biçimi yerel yazıtlarda geçer.
source: Likçe yazıtlar (olgu); Strabon, Geographika XIV; 1934 tarihli ad değişikliği kararı
coords: 36.6514,29.1231

@Datça|ilçe|Muğla|Ege||el
chain: el:Stádia>ota:Dadya>ota:Datça>tr:Datça
era: Bizans dönemi (10. yy)
meaning: Bizans dönemi Stadia liman adının Türkçe söyleyişi; yarımadanın ucundaki antik Knidos'a komşu
story: Knidos yarımadasının ortasındaki Stadia limanı Bizans kaynaklarında geçer; Osmanlı belgelerinde Dadya, halk ağzında Datça biçimini aldı. Yarımadanın ucundaki Knidos, Praksiteles'in Afrodit heykeli ve Eudoksos'un gözlemeviyle ünlüydü. Badem ve bal üretimiyle bilinen yarımadada Strabon'un da söz ettiği rüzgârlar eser.
source: Strabon, Geographika XIV; Pîrî Reis, Kitâb-ı Bahriye; Osmanlı Menteşe sancağı tahrirleri
coords: 36.7281,27.6886

@Milet|antik_kent|Aydın|Ege||xlu
chain: xlu:Millawanda>el:Mílētos>la:Miletus>ota:Balat>tr:Milet
era: Tunç Çağı (MÖ 2. binyıl)
meaning: Hitit belgelerindeki Millawanda (Milawata) kentinin adından; Yunanca Miletos
story: Hitit metinlerinde Ahhiyawa'ya bağlı Millawanda olarak geçen liman, İon döneminin en güçlü kenti oldu; Thales, Anaksimandros ve Hippodamos buradan çıktı. Menderes'in alüvyonları limanı doldurunca kent küçüldü; Türkler yakındaki köye, Yunanca palátion "saray" sözcüğünden Balat dediler. İlyas Bey Camii (1404) Menteşeoğulları eseridir.
source: Hitit çivi yazılı belgeleri (Milawata mektubu); Herodotos V; Strabon, Geographika XIV
coords: 37.5306,27.2767

@Didim|ilçe|Aydın|Ege||el
chain: el:Dídyma>ota:Yoran>cum:Didim>tr:Didim
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca dídymos "ikiz": Apollon ve Artemis ikizlerine adanmış Didyma kehanet merkezinden
story: Miletos'un kutsal yolunun sonundaki Didyma, Delphoi'den sonra Yunan dünyasının en ünlü Apollon kehanet merkeziydi; dev tapınağın sütunları bugün ayaktadır. Osmanlı köyü Yoran adını taşıyordu; 1990'larda kasaba antik adın Türkçeleşmiş biçimi Didim'i aldı. Altınkum plajı turizm merkezidir.
source: Herodotos VI; Strabon, Geographika XIV; Cumhuriyet dönemi idari kararları
coords: 37.3761,27.2683

@Alaşehir|ilçe|Manisa|Ege||tr
chain: el:Philadélpheia>ota:Alaşehir>tr:Alaşehir
era: Helenistik dönem (MÖ 2. yy)
meaning: Türkçe ala "alaca, kızıl" + Farsça şehir: kızıl topraklı tepelerin eteğindeki şehir; antik adı Philadelphia "kardeş sevgisi"
story: Bergama kralı II. Attalos Philadelphos'un kurduğu Philadelphia, Yuhanna'nın Vahiy kitabındaki yedi kiliseden biridir ve kardeş sevgisi anlamındaki adı ABD'deki Philadelphia'ya da ilham vermiştir. Türkler kızıl renkli tepelerinden dolayı kente Alaşehir dediler. Bizans'ın Anadolu'daki son kalesi olarak 1390'a kadar direndi; sultaniye üzümüyle ünlüdür.
source: Vahiy 3 (olgu); Strabon, Geographika XIII; Evliya Çelebi Seyahatnâmesi
coords: 38.3508,28.5181

@Sardes|antik_kent|Manisa|Ege||lyd
chain: lyd:Sfard>el:Sárdeis>la:Sardis>ota:Sart>tr:Sardes
era: Lidya dönemi (MÖ 7. yy)
meaning: Lidce Sfard kent adından; Lidya Krallığı'nın başkenti, sikkenin icat edildiği kent
story: Lidya kralı Kroisos'un başkenti Sardes, Paktolos (Sart Çayı) alüvyonlarındaki altınla dünyanın ilk sikkelerini bastı; "Karun kadar zengin" deyimi bu kralın adından gelir. Lidce yazıtlarda Sfard olarak geçen ad Yunancada Sardeis oldu; Pers Kral Yolu'nun batı ucuydu. Artemis Tapınağı ve sinagog kalıntıları Sart köyünün yanındadır.
source: Herodotos I; Lidce yazıtlar (olgu); Strabon, Geographika XIII
coords: 38.4883,28.0403

@Akhisar|ilçe|Manisa|Ege||tr
chain: el:Thyáteira>ota:Akhisar>tr:Akhisar
era: Osmanlı dönemi (14. yy)
meaning: Türkçe ak + Arapça hisar "kale": beyaz taşlı kaleden; antik adı Thyateira
story: Vahiy kitabındaki yedi kiliseden Thyateira, boyacılar loncasıyla ünlü bir Lidya kentiydi. Saruhanoğulları döneminde Türkler beyaz taştan kaleye Akhisar dediler; hisar sözcüğü Arapça ḥiṣār "kuşatma, kale" sözcüğünden gelir. Tütün ve zeytin üretimi kasabanın ekonomisidir.
source: Vahiy 2 (olgu); Strabon, Geographika XIII; Osmanlı Saruhan sancağı tahrirleri
coords: 38.9186,27.8392

@Tire|ilçe|İzmir|Ege||el
chain: el:Teíra>ota:Tire>tr:Tire
era: Bizans dönemi (10. yy)
meaning: Bizans dönemi Teira kasaba adının Türkçe söyleyişi; Küçük Menderes ovasındaki Aydınoğlu merkezi
story: Küçük Menderes ovasının güney kenarındaki Teira, Bizans döneminde piskoposluk merkeziydi. Aydınoğulları 14. yüzyılda kenti alıp imar ettiler; Timur 1402'de kışı burada geçirdi. Tire, Osmanlı döneminde keçe ve dokuma zanaatlarıyla, bugün de salı pazarıyla bilinir.
source: Bizans piskoposluk listeleri (olgu); Düstûrnâme-i Enverî; Evliya Çelebi Seyahatnâmesi
coords: 38.0892,27.7350

@Ödemiş|ilçe|İzmir|Ege||tr
chain: ota:Ötemiş>ota:Ödemiş>tr:Ödemiş
era: Osmanlı dönemi (15. yy)
meaning: Türkçe Ötemiş kişi adından (öte- "borcunu ödemek, yerine getirmek"); yöreye yerleşen bir Türkmen beyinin adı
story: Bozdağ'ın eteğindeki kasaba, Aydınoğulları döneminde yöreye yerleşen Ötemiş adlı bir beyin adıyla anılır; Eski Türkçe öte- fiilinden türeyen bu kişi adı, Türkçede ödemiş biçimine dönüşmüştür. Yakındaki Birgi, Aydınoğlu Mehmed Bey'in başkentiydi. Ödemiş patatesi ve Bozdağ yaylası kasabanın simgeleridir.
source: Osmanlı Aydın sancağı tahrirleri; Dîvânu Lugâti't-Türk (öte-)
coords: 38.2281,27.9700

@Gediz|ilçe|Kütahya|Ege||phr
chain: phr:Kadoi>el:Kádoi>ota:Gediz>tr:Gediz
era: Antik dönem (MÖ 1. binyıl)
meaning: Frigya kenti Kadoi'nin adından; Gediz Irmağı (antik Hermos) da bu kasabadan adını alır
story: Frigya'nın Kadoi kenti, Hermos Irmağı'nın kaynak bölgesindeydi; Türkçede Gediz biçimini alan kasaba adı, ırmağın Türkçe adına da kaynak oldu. Antik Hermos, Sardes'in altınlı Paktolos kolunu taşıyan ırmaktır. 1970 depreminden sonra kasaba yeni yerine taşındı.
source: Strabon, Geographika XII; Osmanlı Kütahya sancağı tahrirleri
coords: 39.0392,29.4114

@Pamukkale|semt|Denizli|Ege||tr
chain: el:Hierápolis>ota:Pamukkale>tr:Pamukkale
era: Osmanlı dönemi (17. yy)
meaning: Türkçe pamuk + kale: beyaz travertenlerin pamuk yığınına, tepedeki antik kentin kaleye benzetilmesinden
story: Kalsiyumlu sıcak suların binlerce yılda oluşturduğu beyaz travertenler, Türklerce pamuk yığınlarına benzetildi; tepedeki Hierapolis "kutsal kent" kalıntıları da kale sanıldı. Bergama krallarının kurduğu Hierapolis, kaplıcaları ve Aziz Philippus'un mezarıyla ünlüydü. Pamuk sözcüğü Farsça panbe'den gelir. UNESCO Dünya Mirası listesindedir.
source: Strabon, Geographika XIII; Evliya Çelebi Seyahatnâmesi; UNESCO kayıtları (olgu)
coords: 37.9233,29.1206

@Laodikeia|antik_kent|Denizli|Ege||el
chain: el:Laodíkeia>la:Laodicea>sel:Lâdik>tr:Laodikeia
era: Helenistik dönem (MÖ 3. yy)
meaning: Seleukos kralı II. Antiokhos'un eşi Laodike'nin adından "Laodike'nin kenti"
story: II. Antiokhos MÖ 3. yüzyılda Lykos vadisinde eşi Laodike'nin adını taşıyan kenti kurdu; yün ticareti ve bankacılığıyla zenginleşen kent Vahiy kitabındaki yedi kiliseden biridir. Selçuklular kenti Lâdik adıyla andı; Denizli bu kentin yerine kuruldu. Kazılarda ortaya çıkan stadion ve tiyatrolar Roma dönemini yansıtır.
source: Strabon, Geographika XII; Vahiy 3 (olgu); İbn Battûta Seyahatnâmesi (Lâdik)
coords: 37.8358,29.1075

@Afrodisias|antik_kent|Aydın|Ege||el
chain: el:Aphrodisiás>la:Aphrodisias>ota:Geyre>tr:Afrodisias
era: Helenistik dönem (MÖ 2. yy)
meaning: Tanrıça Aphrodite'nin adından "Afrodit'in kenti"; Osmanlı köyü Geyre, Karya adının kalıntısıdır
story: Karya'nın iç kesimindeki kent Aphrodite kültü ve mermer heykeltıraşlık okuluyla Roma döneminde ün kazandı; Sebasteion kabartmaları ve stadion olağanüstü korunmuştur. Bizans'ta Stauropolis "haç kenti" adını alan yerleşim, Osmanlı köyü Geyre'de yaşadı; Geyre adı Karya bölge adının izidir.
source: Strabon, Geographika XIV; Afrodisias yazıtları (olgu); UNESCO kayıtları
coords: 37.7089,28.7244

@Milas|ilçe|Muğla|Ege||xcr
chain: xcr:Mylasa>el:Mýlasa>la:Mylasa>ota:Milas>tr:Milas
era: Antik dönem (MÖ 1. binyıl)
meaning: Karya dilinden gelen Mylasa kent adı; Karya'nın ilk başkenti, Zeus Karios'un kutsal alanı
story: Karya satraplarının Halikarnassos'tan önceki başkenti Mylasa, Zeus Karios ve Labraunda kutsal alanıyla bölgenin dinî merkeziydi; Strabon kentin mermer zenginliğini anlatır. Menteşeoğulları Beyliği'nin merkezi olan kasaba Türkçede Milas oldu; Firuz Bey Camii (1394) ve Gümüşkesen anıt mezarı iki dönemi yan yana gösterir. Milas halıları ünlüdür.
source: Strabon, Geographika XIV; Osmanlı Menteşe sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 37.3167,27.7833

@Karşıyaka|semt|İzmir|Ege||tr
chain: el:Kordelió>ota:Karşıyaka>tr:Karşıyaka
era: Osmanlı dönemi (19. yy)
meaning: Türkçe karşı + yaka "kıyı": İzmir'in merkezine göre körfezin karşı kıyısı; Rumca adı Kordelio
story: İzmir Körfezi'nin kuzey kıyısındaki Rum ve Levanten sayfiyesi Kordelio adıyla anılıyordu; Türkler merkeze göre körfezin karşı kıyısında kaldığı için buraya Karşıyaka dediler. Yaka sözcüğü Eski Türkçede "kenar, kıyı" anlamındadır. Atatürk'ün annesi Zübeyde Hanım'ın mezarı buradadır.
source: Osmanlı İzmir salnameleri; Evliya Çelebi Seyahatnâmesi
coords: 38.4583,27.1167

@Alsancak|semt|İzmir|Ege||tr
chain: it:Punta>ota:Punta>cum:Alsancak>tr:Alsancak
era: Cumhuriyet dönemi (1922)
meaning: Türkçe al "kırmızı" + sancak "bayrak": kurtuluşta buraya dikilen Türk bayrağından; eski adı İtalyanca Punta "burun"
story: Körfeze uzanan burundaki Levanten mahallesi, İtalyanca punta "burun" sözcüğüyle Punta diye anılıyordu. 9 Eylül 1922'de İzmir'in kurtuluşunda buraya dikilen Türk bayrağının anısına semt Alsancak adını aldı. Sancak sözcüğü Eski Türkçe sanç- "saplamak" kökünden gelir; al ise "kırmızı" anlamındaki eski Türkçe renk adıdır.
source: Osmanlı İzmir salnameleri; Cumhuriyet dönemi idari kararları
coords: 38.4372,27.1431

@Kadifekale|kale|İzmir|Ege||tr
chain: el:Págos>ota:Kadife Kale>tr:Kadifekale
era: Osmanlı dönemi (17. yy)
meaning: Türkçe kadife (Arapça qaṭīfa) + kale: Pagos tepesindeki Helenistik kalenin yumuşak görünümlü surlarından
story: Büyük İskender'in rüyasında gördüğü söylenen Pagos tepesine Lysimakhos İzmir'in yeni kalesini kurdu; Osmanlı döneminde surlar kadife gibi yumuşak görünümlü duvarları nedeniyle Kadifekale diye anıldı. Kadife sözcüğü Arapça qaṭīfa'dan gelir. Kale, körfeze hâkim bir seyir noktasıdır.
source: Strabon, Geographika XIV; Evliya Çelebi Seyahatnâmesi
coords: 38.4139,27.1431

@Priene|antik_kent|Aydın|Ege||xcr
chain: xcr:Priene>el:Priḗnē>la:Priene>ota:Samsun Kalesi>tr:Priene
era: Antik dönem (MÖ 1. binyıl)
meaning: Karya dilinden gelen kent adı; Hippodamos'un ızgara planının uygulandığı İon kenti
story: Mykale Dağı'nın eteğindeki Priene, MÖ 4. yüzyılda ızgara planıyla yeniden kurulan örnek bir İon kentidir; Athena Tapınağı'nı Büyük İskender yaptırmıştır. Yedi bilgeden Bias buradan çıktı. Kentin yanındaki Bizans kalesine Osmanlılar Samsun Kalesi diyordu; antik ad Türkçeye Priene olarak geçti.
source: Strabon, Geographika XIV; Vitruvius, De Architectura I
coords: 37.6597,27.2975

# ===================================================================== AKDENİZ
@Antakya|ilçe|Hatay|Akdeniz||el
chain: el:Antiócheia>la:Antiochia>ar:Anṭākiya>ota:Antakya>tr:Antakya
era: Helenistik dönem (MÖ 4. yy)
meaning: Seleukos I'in babası Antiokhos'un adından "Antiokhos'un kenti"
story: Seleukos I Nikator MÖ 300'de Asi Irmağı kıyısında babası Antiokhos'un adını taşıyan başkenti kurdu; Roma'nın üçüncü büyük kenti olan Antiocheia, Hristiyanlara "Hristiyan" adının ilk kez verildiği yerdir. Arapça Anṭākiya söyleyişi Türkçede Antakya oldu; Haçlı Prensliği, Memlük ve Osmanlı dönemlerini yaşadı. Aziz Petrus Kilisesi ve mozaik müzesi kentin antik mirasıdır.
source: Strabon, Geographika XVI; Resullerin İşleri 11 (olgu); Evliya Çelebi Seyahatnâmesi
coords: 36.2023,36.1613

@İskenderun|ilçe|Hatay|Akdeniz||el
chain: el:Alexándreia kat' Issón>la:Alexandria ad Issum>ar:al-Iskandarūn>ota:İskenderun>tr:İskenderun
era: Helenistik dönem (MÖ 4. yy)
meaning: Büyük İskender'in Issos zaferinden sonra kurduğu Alexandreia'nın Arapça söyleyişi; İskender Arapça al-Iskandar
story: MÖ 333'te Issos'ta Pers kralı Dareios'u yenen Büyük İskender, zaferin anısına körfezin başında kendi adını taşıyan bir liman kurdurdu. Arapçada al-Iskandarūn biçimini alan ad, Türkçede İskenderun oldu; Batı dillerinde Alexandretta "küçük İskenderiye" denir. Osmanlı'nın Halep'e açılan limanıydı; demir-çelik fabrikası ve donanma üssü bugünkü kimliğidir.
source: Arrianus, Anabasis Alexandri; Strabon, Geographika XIV; Pîrî Reis, Kitâb-ı Bahriye
coords: 36.5872,36.1736

@Samandağ|ilçe|Hatay|Akdeniz||el
chain: el:Seleúkeia Piería>el:Hágios Symeṓn>ota:Süveydiye>cum:Samandağ>tr:Samandağ
era: Cumhuriyet dönemi (1948)
meaning: "Aziz Simeon (Samân) dağı": sütun üstünde yaşayan keşiş Simeon Stylites'in tepedeki manastırından
story: Antakya'nın limanı Seleukeia Pieria'nın yakınındaki dağda 6. yüzyılda bir sütun üstünde yaşayan Genç Simeon Stylites'in manastırı vardı; dağ bu azizin adıyla anıldı ve Arapça Samʿān biçimi Türkçede Saman'a dönüştü. Osmanlı adı Süveydiye olan kasaba 1948'de Samandağ oldu; Titus Tüneli Roma mühendisliğinin anıtıdır.
source: Bizans azizler menkıbeleri (olgu); Osmanlı Halep eyaleti kayıtları; 1948 tarihli ad değişikliği
coords: 36.0833,35.9667

@Harbiye|semt|Hatay|Akdeniz||ar
chain: el:Dáphnē>ar:Bayt al-Māʾ>ota:Harbiye>tr:Harbiye
era: Antik dönem (MÖ 3. yy)
meaning: Arapça ḥarbiyya "savaşa ait": Osmanlı döneminde burada konuşlanan askerî birlikten; antik adı Daphne "defne"
story: Antiocheia'nın sayfiyesi Daphne, Apollon'un kovaladığı nympha Daphne'nin defne ağacına dönüştüğü yer sayılırdı; şelaleleri ve Apollon tapınağıyla ünlüydü. Araplar su bolluğundan ötürü Bayt al-Māʾ "su evi" dediler. Osmanlı'nın son döneminde askerî birliklerin konuşlanmasıyla Harbiye adı yerleşti; defne sabunu üretimi antik adı yaşatır.
source: Strabon, Geographika XVI; Libanios (olgu); Osmanlı Halep salnameleri
coords: 36.1447,36.1483

@Alanya|ilçe|Antalya|Akdeniz||ar
chain: el:Korakḗsion>el:Kalonóros>sel:ʿAlāʾiyya>ota:Alaiye>cum:Alanya>tr:Alanya
era: Selçuklu dönemi (1221)
meaning: Selçuklu sultanı Alâeddin Keykubad'ın adından Arapça nisbetle ʿAlāʾiyya "Alâeddin'e ait"; 1935'te Alanya
story: Korsanların sığınağı Korakesion, Bizans döneminde kayalık burnu nedeniyle Kalonoros "güzel dağ" adını taşıyordu. Alâeddin Keykubad 1221'de kaleyi aldı, tersane ve Kızıl Kule'yi yaptırdı; kent onun adıyla Alâiye oldu. 1935'te Atatürk'ün ziyaretinde bir telgraf yazımındaki biçim benimsenerek ad Alanya yapıldı. Selçuklu tersanesi Akdeniz'in korunmuş tek Orta Çağ tersanesidir.
source: İbn Bîbî, el-Evâmirü'l-Alâiyye; Pîrî Reis, Kitâb-ı Bahriye; 1935 tarihli ad değişikliği
coords: 36.5444,31.9954

@Side|antik_kent|Antalya|Akdeniz||unk
chain: unk:Side (Sidece "nar")>el:Sídē>la:Side>ota:Selimiye>tr:Side
era: Antik dönem (MÖ 7. yy)
meaning: Anadolu'nun yerli Side dilinde "nar": kentin sikkelerinde nar simgesi bulunur
story: Pamphylia kıyısındaki Side, kendine özgü bir Anadolu dili konuşan halkıyla ve Yunanca öncesi yazıtlarıyla bilinir; adı Sidecede "nar" anlamına gelir ve nar kentin simgesiydi. Roma'nın köle pazarı ve Apollon Tapınağı'yla ünlüydü. 19. yüzyılda Girit göçmenlerinin kurduğu Selimiye köyü kalıntıların üstündedir.
source: Strabon, Geographika XIV; Side dili yazıtları (olgu); Arrianus, Anabasis Alexandri
coords: 36.7667,31.3889

@Manavgat|ilçe|Antalya|Akdeniz||xlu
chain: xlu:Manawa>el:Mélas (ırmak)>ota:Manavgat>tr:Manavgat
era: Antik dönem (MÖ 1. binyıl)
meaning: Luvi dönemine uzanan bir yerleşim adının Türkçe söyleyişi; Manavgat Irmağı'nın antik adı Melas "kara"
story: Toroslardan inen Manavgat Irmağı antik çağda Melas "kara ırmak" adını taşıyordu; kasabanın adı ise Luvi döneminden kalan bir yerleşim adına bağlanır. Osmanlı belgelerinde Manavgat biçiminde geçen kasaba, Side'nin yanı başındadır; şelalesi ve Oymapınar Barajı ile bilinir.
source: Strabon, Geographika XIV; Osmanlı Teke sancağı tahrirleri
coords: 36.7869,31.4433

@Kaş|ilçe|Antalya|Akdeniz||tr
chain: xlc:Habesos>el:Antíphellos>ota:Andifli>ota:Kaş>tr:Kaş
era: Osmanlı dönemi (19. yy)
meaning: Türkçe kaş "kaş biçimli kıyı, yamaç": kasabanın arkasındaki kaşı andıran sarp yamaçtan; antik adı Antiphellos
story: Likya kenti Antiphellos, Likçe yazıtlarda Habesos olarak geçer; Osmanlı belgelerinde Andifli adıyla anılan kasabaya, denize kaş gibi inen dik yamacı nedeniyle Kaş dendi. Kaş sözcüğü Eski Türkçede hem göz üstündeki kaş hem de "dağ yamacı, kenar" anlamındadır. Likya lahitleri ve Meis adasına bakan limanı kasabanın simgeleridir.
source: Likçe yazıtlar (olgu); Strabon, Geographika XIV; Dîvânu Lugâti't-Türk (kaş)
coords: 36.2019,29.6397

@Demre|ilçe|Antalya|Akdeniz||el
chain: xlc:Myra>el:Mýra>ota:Dembre>cum:Demre>tr:Demre
era: Antik dönem (MÖ 1. binyıl)
meaning: Likya kenti Myra'nın adının Türkçe söyleyişi (Dembre > Demre); Noel Baba'nın (Aziz Nikolaos) kenti
story: Likya Birliği'nin önde gelen kenti Myra, 4. yüzyılda piskoposluk yapan Aziz Nikolaos'un (Noel Baba) kentidir; kaya mezarları ve tiyatrosu ünlüdür. Türkçede Dembre, sonra Demre biçimini alan ad 2005'e kadar resmî belgelerde Kale olarak geçiyordu. Sera domatesi ve Aziz Nikolaos Kilisesi kasabanın iki yüzüdür.
source: Strabon, Geographika XIV; Bizans azizler menkıbeleri (olgu); Osmanlı Teke sancağı tahrirleri
coords: 36.2436,29.9847

@Finike|ilçe|Antalya|Akdeniz||el
chain: el:Phoiníkē>la:Phoenicus>ota:Finike>tr:Finike
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca Phoinike "Fenike": Fenikeli tüccarların kurduğu liman; phoînix aynı zamanda hurma ağacı demektir
story: Likya kıyısındaki liman, Fenikelilerin ticaret üssü olarak kurdukları için Phoinike adını taşıyordu; Yunanca phoînix sözcüğü hem Fenikeli hem de hurma ağacı anlamına gelir ve her iki anlam kasabayla uyuşur. Limyra ve Arykanda antik kentleri yakınındadır; portakal bahçeleri kasabanın bugünkü simgesidir.
source: Strabon, Geographika XIV; Pîrî Reis, Kitâb-ı Bahriye
coords: 36.3000,30.1500

@Kemer|ilçe|Antalya|Akdeniz||fa
chain: fa:kamar>ota:Eski Köy>cum:Kemer>tr:Kemer
era: Cumhuriyet dönemi (1916–1917)
meaning: Farsça kamar "kuşak, kemer": sel sularını tutmak için dağ eteğine örülen kemer biçimli taş setten
story: Beydağları'ndan inen sel sularından korunmak için 1916–1917'de köyün üstüne örülen kilometrelerce uzunluktaki kemer biçimli taş set, Eski Köy'e yeni adını verdi. Kemer sözcüğü Farsça kamar "kuşak" sözcüğünden Türkçeye geçmiştir. Antik Phaselis ve Olympos kalıntıları ilçe sınırlarındadır; 1980'lerden sonra turizm merkezi oldu.
source: Osmanlı Teke sancağı kayıtları; Cumhuriyet dönemi idari kararları
coords: 36.6028,30.5606

@Phaselis|antik_kent|Antalya|Akdeniz||el
chain: el:Phasēlís>la:Phaselis>ota:Tekirova>tr:Phaselis
era: Antik dönem (MÖ 7. yy)
meaning: Rodoslu kolonistlerin kurduğu üç limanlı Likya kentinin adı; Yunanca phásēlos "fasulye" ile ilişkilendirilir
story: MÖ 7. yüzyılda Rodoslu kolonistlerin kurduğu Phaselis, üç doğal limanıyla gül yağı ve kereste ticareti yapan bir Likya kentiydi; Büyük İskender kışı burada geçirdi. Adın Yunanca phásēlos "fasulye; hafif tekne" sözcüğüyle ilişkisi anlatılır. Kalıntılar bugün Tekirova yakınındaki çam ormanı içindedir.
source: Strabon, Geographika XIV; Arrianus, Anabasis Alexandri I
coords: 36.5244,30.5514

@Termessos|antik_kent|Antalya|Akdeniz||pis
chain: pis:Termessós>el:Termēssós>la:Termessus>tr:Termessos
era: Antik dönem (MÖ 1. binyıl)
meaning: Pisidya dilinden gelen kent adı; Büyük İskender'in kuşatmaktan vazgeçtiği kartal yuvası kent
story: Güllük Dağı'nın 1000 metre yükseğindeki Termessos, Pisidyalıların kendilerine Solymler dediği, Homeros'un andığı dağlı halkın kentiydi. Büyük İskender MÖ 333'te kenti kuşattı ancak alamadan geçti. Tiyatrosu, agorası ve lahitleri dağın tepesinde korunmuştur; Pisidce adı Yunan yazarlarca aktarılmıştır.
source: Arrianus, Anabasis Alexandri I; Strabon, Geographika XIII
coords: 36.9833,30.4667

@Perge|antik_kent|Antalya|Akdeniz||hit
chain: hit:Parḫa>el:Pérgē>la:Perga>ota:Aksu>tr:Perge
era: Tunç Çağı (MÖ 2. binyıl)
meaning: Hitit belgelerindeki Parha kentinin adından; Pamphylia'nın Artemis kültü merkezi
story: Hitit kralı IV. Tudhaliya'nın bir antlaşmasında Parha olarak geçen kent, Yunan döneminde Perge adıyla Pamphylia'nın başkenti oldu; Artemis Pergaia tapınağı ve stadionuyla ünlüydü. Matematikçi Apollonios burada doğdu; Aziz Pavlus ilk yolculuğunda kente uğradı. Kalıntılar Aksu kasabasının yanındadır.
source: Hitit çivi yazılı belgeleri (Bronz Tablet); Strabon, Geographika XIV; Resullerin İşleri 13 (olgu)
coords: 36.9617,30.8539

@Aspendos|antik_kent|Antalya|Akdeniz||xlu
chain: xlu:Estwediya>el:Áspendos>la:Aspendus>ota:Belkıs>tr:Aspendos
era: Antik dönem (MÖ 1. binyıl)
meaning: Kentin sikkelerindeki yerli adı Estwediya'dan; Geç Hitit kralı Azatiwada'nın adıyla ilişkilendirilir
story: Köprüçay kıyısındaki Aspendos, kendi sikkelerinde Estwediya adını kullanıyordu; bu ad Karatepe yazıtlarındaki Azatiwada ile ilişkilendirilir. Roma dönemine ait tiyatrosu (MS 2. yy) dünyanın en iyi korunmuş antik tiyatrosudur; halk tiyatroyu Belkıs Sarayı diye anar. Su kemerleri Roma mühendisliğinin örneğidir.
source: Strabon, Geographika XIV; Aspendos sikkeleri (olgu); Evliya Çelebi Seyahatnâmesi
coords: 36.9389,31.1722

@Korkuteli|ilçe|Antalya|Akdeniz||tr
chain: el:Isínda>ota:İstanoz>cum:Korkuteli>tr:Korkuteli
era: Cumhuriyet dönemi (1926)
meaning: II. Bayezid'in Teke sancakbeyi olan oğlu Şehzade Korkut'un adından "Korkut'un ili"
story: Pisidya kenti Isinda'nın yerindeki kasaba Osmanlı'da İstanoz adını taşıyordu. 1926'da kasabaya, 16. yüzyıl başında Antalya'da sancakbeyliği yapan şair şehzade Korkut'un adı verildi; Korkut, Dede Korkut adında da yaşayan eski bir Türk kişi adıdır. Alâeddin Camii ve Sinaneddin Medresesi Selçuklu eseridir.
source: Osmanlı Teke sancağı tahrirleri; 1926 tarihli ad değişikliği kararı
coords: 37.0653,30.1961

@Tarsus|ilçe|Mersin|Akdeniz||hit
chain: hit:Tarša>akk:Tarzi>el:Tarsós>la:Tarsus>ar:Ṭarsūs>ota:Tarsus>tr:Tarsus
era: Hitit dönemi (MÖ 2. binyıl)
meaning: Hitit metinlerindeki Tarša kentinin adından; Kilikya'nın başkenti, Aziz Pavlus'un doğduğu kent
story: Hitit belgelerinde Kizzuwatna'nın Tarša kenti olarak geçen Tarsus, Asur yıllıklarında Tarzi adıyla anılır. Kleopatra ile Antonius burada buluştu; Aziz Pavlus bu kentte doğdu. Arapça Ṭarsūs söyleyişi Türkçede değişmeden kaldı. Ramazanoğulları döneminden Ulu Cami ve Kleopatra Kapısı kentin anıtlarıdır; Gözlükule höyüğü Tunç Çağı'na uzanır.
source: Hitit çivi yazılı belgeleri; Ksenophon, Anabasis I; Strabon, Geographika XIV; Evliya Çelebi Seyahatnâmesi
coords: 36.9165,34.8951

@Silifke|ilçe|Mersin|Akdeniz||el
chain: el:Seleúkeia>la:Seleucia>ar:Salūqiya>ota:Silifke>tr:Silifke
era: Helenistik dönem (MÖ 3. yy)
meaning: Seleukos I Nikator'un adından "Seleukos'un kenti"; Kalykadnos (Göksu) kıyısındaki Seleukeia
story: Seleukos I MÖ 3. yüzyılda Göksu kıyısında kendi adını taşıyan kenti kurdu; Alman imparatoru Friedrich Barbarossa 1190'da Üçüncü Haçlı Seferi sırasında bu ırmakta boğuldu. Arapça Salūqiya biçimi Türkçede Silifke oldu; Karamanoğulları ve Osmanlı kalesi kasabanın tepesindedir. Yöre "Silifke'nin yoğurdu" türküsüyle de anılır.
source: Strabon, Geographika XIV; Haçlı kronikleri (olgu); Evliya Çelebi Seyahatnâmesi
coords: 36.3767,33.9344

@Anamur|ilçe|Mersin|Akdeniz||el
chain: el:Anemoúrion>la:Anemurium>ota:Anamur>tr:Anamur
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca ánemos "rüzgâr" + oúrion "burun": "rüzgârlı burun"; Anadolu'nun en güney ucu
story: Türkiye'nin en güney noktası olan burundaki Anemourion, adını Kıbrıs'a bakan rüzgârlı konumundan alır; Roma dönemi nekropolü ve hamamları burnun yamacında korunmuştur. Karamanoğulları'nın Mamure Kalesi kıyıdaki en sağlam Orta Çağ kalelerindendir. Muz üretimi kasabanın bugünkü simgesidir.
source: Strabon, Geographika XIV; Pîrî Reis, Kitâb-ı Bahriye
coords: 36.0750,32.8361

@Ceyhan|ilçe|Adana|Akdeniz||ar
chain: el:Pýramos>ar:Jayḥān>ota:Ceyhan>tr:Ceyhan
era: Erken İslam dönemi (8. yy)
meaning: Arapça Jayḥān: İslam coğrafyacılarının cennet ırmaklarından Ceyhun ile özdeşleştirdiği Pyramos Irmağı'nın adı
story: Çukurova'nın doğusunu sulayan Pyramos Irmağı, Arap coğrafyacılarınca Orta Asya'daki Ceyhun (Amuderya) gibi cennetten çıkan ırmaklardan sayılıp Jayḥān adıyla anıldı; aynı biçimde Saros'a Seyhan dendi. Irmağın adı 19. yüzyılda kurulan Hamidiye kasabasına 1920'lerde verildi. Yumurtalık limanı ve Yılankale ilçe sınırlarındadır.
source: Arap coğrafyacıları (İbn Havkal, olgu); Strabon, Geographika XII (Pyramos); Osmanlı Adana salnameleri
coords: 37.0247,35.8125

@Seyhan|nehir|Adana|Akdeniz||ar
chain: el:Sáros>ar:Sayḥān>ota:Seyhan>tr:Seyhan
era: Erken İslam dönemi (8. yy)
meaning: Arapça Sayḥān: cennet ırmağı Seyhun (Siriderya) adının Kilikya'daki Saros Irmağı'na verilmesi
story: Toroslardan inip Adana'nın içinden geçen Saros, Arap fetihlerinden sonra Orta Asya'daki Seyhun'un adıyla anıldı; İslam coğrafyacıları Seyhan ve Ceyhan'ı cennet ırmakları olarak yorumladı. Adana'nın Roma dönemi Taşköprüsü bu ırmağı aşar; Seyhan Barajı 1956'da tamamlandı. Adana'nın merkez ilçelerinden biri de ırmağın adını taşır.
source: Arap coğrafyacıları (olgu); Strabon, Geographika XII; Evliya Çelebi Seyahatnâmesi
coords: 37.0000,35.3000

@Kozan|ilçe|Adana|Akdeniz||tr
chain: hy:Sis>ota:Sis>ota:Kozan>tr:Kozan
era: Osmanlı dönemi (18. yy)
meaning: Yöreyi yöneten Kozanoğulları derebeyi ailesinin adından; eski adı Sis, Kilikya Ermeni Krallığı'nın başkenti
story: Kilikya Ermeni Krallığı'nın 1186'dan 1375'e kadar başkenti olan Sis, Katolikosluk merkezi olarak Ermeni kilise tarihinde önemlidir. 18.–19. yüzyılda yöreye hâkim olan Kozanoğulları'nın adı 1865 Fırka-i Islahiye harekâtından sonra sancağa, 1923'te kasabaya verildi. Kozan sözcüğü Türkçe koz "ceviz" ile ilişkilendirilir.
source: Osmanlı Kozan sancağı kayıtları; Ermeni Kilikya kronikleri (olgu)
coords: 37.4478,35.8142

@Anavarza|antik_kent|Adana|Akdeniz||el
chain: el:Anázarbos>la:Anazarbus>ar:ʿAyn Zarba>ota:Anavarza>tr:Anavarza
era: Antik dönem (MÖ 1. yy)
meaning: Yunanca Anazarbos kent adından; Arapça ʿAyn Zarba "Zarba pınarı" halk yorumudur
story: Çukurova'nın doğusunda kayalık bir tepeye yaslanan Anazarbos, Roma'nın Kilikya Secunda eyaletinin başkentiydi; hekim Dioskorides burada doğdu. Araplar adı ʿAyn Zarba "pınar" sözcüğüyle yorumladı; Kilikya Ermeni krallarının kalesi tepededir. Türkçe Anavarza biçimi, Arapça söyleyişten gelir.
source: Strabon, Geographika XIV; Arap coğrafyacıları (olgu); Evliya Çelebi Seyahatnâmesi
coords: 37.2586,35.9064

@Eğirdir|ilçe|Isparta|Akdeniz||el
chain: el:Akrōtḗri>sel:Eğridir>ota:Eğirdir>tr:Eğirdir
era: Selçuklu dönemi (13. yy)
meaning: Yunanca akrōtḗri "burun, yarımada" sözcüğünün Türkçe söyleyişi; göle uzanan yarımada üzerindeki kent
story: Türkiye'nin ikinci büyük tatlı su gölünün kıyısında, göle uzanan bir yarımadaya kurulu kasaba, Bizans döneminde Yunanca "burun" anlamındaki akrotiri sözcüğüyle anılıyordu; Türkçede Eğridir biçimini alan ad, Türkçe eğri sözcüğüyle de ilişkilendirildi. Hamitoğulları'nın merkezi olan kasabada Dündar Bey Medresesi ve Hızır Bey Camii durur. 1980'lerde ad Eğirdir olarak düzeltildi.
source: Osmanlı Hamid sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 37.8742,30.8506

@Yalvaç|ilçe|Isparta|Akdeniz||tr
chain: el:Antiócheia (Pisidías)>sel:Yalvaç>ota:Yalvaç>tr:Yalvaç
era: Selçuklu dönemi (12. yy)
meaning: Eski Türkçe yalavaç "elçi, peygamber": Aziz Pavlus'un vaaz verdiği Pisidya Antiocheia'sına Türklerin verdiği ad
story: Seleukosların kurduğu Pisidya Antiocheia'sı, Aziz Pavlus'un ilk misyon yolculuğunda vaaz verdiği kenttir; Augustus'un Roma kolonisi olarak büyüdü. Türkler, Hristiyan havarinin kenti olduğunu bildiklerinden ya da yöredeki bir ereni anarak kasabaya "elçi, peygamber" anlamındaki Eski Türkçe yalavaç sözcüğünü ad olarak verdiler; bu sözcük Dîvânu Lugâti't-Türk'te geçer. Devlethan Camii Selçuklu eseridir.
source: Resullerin İşleri 13 (olgu); Dîvânu Lugâti't-Türk (yalavaç); Osmanlı Hamid sancağı tahrirleri
coords: 38.2953,31.1783

@Sagalassos|antik_kent|Burdur|Akdeniz||pis
chain: pis:Sagalassós>el:Sagalassós>la:Sagalassus>ota:Ağlasun>tr:Sagalassos
era: Antik dönem (MÖ 1. binyıl)
meaning: Pisidya dilinden gelen kent adı; Osmanlı köyü Ağlasun bu adın Türkçe söyleyişidir
story: Toros Dağları'nın 1500 metre yükseğindeki Sagalassos, Büyük İskender'in MÖ 333'te savaşarak aldığı Pisidya kentlerinin en görkemlisiydi; Antoninus Çeşmesi ve tiyatrosu yeniden ayağa kaldırıldı. Köyün adı Ağlasun, antik adın Türkçe halk söyleyişidir ve antik adların köy adlarında yaşamasının güzel bir örneğidir.
source: Arrianus, Anabasis Alexandri I; Strabon, Geographika XII; Osmanlı Hamid sancağı tahrirleri (Ağlasun)
coords: 37.6775,30.5197

@Elbistan|ilçe|Kahramanmaraş|Akdeniz||hit
chain: hit:Ablasta>el:Ablastha>ar:Ablistān>sel:Elbistan>tr:Elbistan
era: Hitit dönemi (MÖ 2. binyıl)
meaning: Hitit metinlerindeki Ablasta yer adından; Ceyhan'ın kaynak ovasındaki kent
story: Ceyhan Irmağı'nın kaynak ovasındaki kent, Hitit belgelerinde Ablasta olarak geçer; Bizans ve Arap kaynakları aynı adı sürdürdü. 1277'de Memlük sultanı Baybars'ın Moğolları yendiği Elbistan Savaşı burada yapıldı; Dulkadiroğulları Beyliği'nin ilk merkeziydi. Karahöyük'teki Geç Hitit yazıtları adın eskiliğine tanıktır.
source: Hitit çivi yazılı belgeleri (olgu); Memlük kronikleri (Elbistan Savaşı, 1277); Osmanlı Maraş sancağı tahrirleri
coords: 38.2053,37.1964
"""
