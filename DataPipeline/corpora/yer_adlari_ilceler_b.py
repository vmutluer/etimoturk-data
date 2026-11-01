# -*- coding: utf-8 -*-
"""Korpus 29 — Tarihî ilçe, semt, antik kent ve bölge adları (B): İç Anadolu, Karadeniz, Doğu ve Güneydoğu Anadolu.

DSL ve telif notu için bkz. yer_adlari_iller_a.py.
"""

TOPONYMS = r"""
# ===================================================================== İÇ ANADOLU
@Kapadokya|bölge|Nevşehir|İç Anadolu||fa
chain: hit:Katta peda>fa:Katpatuka>el:Kappadokía>la:Cappadocia>tr:Kapadokya
era: Ahameniş dönemi (MÖ 6. yy)
meaning: Eski Farsça Katpatuka "güzel atlar ülkesi" (yaygın yorum); Hititçe katta peda "aşağı ülke" ile de ilişkilendirilir
story: Pers kralı Dareios'un Behistun yazıtında Katpatuka adıyla sayılan satraplık, Yunan yazarlarca Kappadokia olarak anıldı; ad Eski Farsça "güzel atlar ülkesi" diye yorumlanır, ancak Hititçe "aşağı ülke" anlamındaki katta peda'ya dayandığı da önerilir. Herodotos Kapadokyalıları Suriyeliler diye anar. Peribacaları, kaya kiliseleri ve yeraltı kentleri bölgenin volkanik tüfünde oyulmuştur.
source: Behistun Yazıtı (olgu); Herodotos I; Strabon, Geographika XII
coords: 38.6500,34.8500

@Göreme|ilçe|Nevşehir|İç Anadolu||el
chain: el:Kórama>ota:Göreme>tr:Göreme
era: Bizans dönemi (6. yy)
meaning: Bizans dönemi Korama yerleşim adının Türkçe söyleyişi; halk Türkçe "görme" (gizli, görülmeyen yer) ile açıklar
story: Kapadokya'nın kaya kiliselerle dolu vadisi, Bizans azizler menkıbelerinde Korama adıyla geçer; Türkçede Göreme biçimini alan ad, halk arasında Arap akınlarından saklanan Hristiyanların "görülmeyen" köyü olarak yorumlanır. Osmanlı döneminde Maçan adıyla anılan köy, 1980'lerde Göreme adını geri aldı; Açık Hava Müzesi UNESCO listesindedir.
source: Bizans azizler menkıbeleri (Aziz Hieron, olgu); Osmanlı Niğde sancağı tahrirleri
coords: 38.6431,34.8289

@Ürgüp|ilçe|Nevşehir|İç Anadolu||el
chain: el:Hágios Prokópios>ota:Ürküp>ota:Ürgüp>tr:Ürgüp
era: Bizans dönemi (10. yy)
meaning: Rumca Hagios Prokopios "Aziz Prokopios" ad öbeğinin Türkçe söyleyişi
story: Kapadokya'nın kaya oyma kasabası, Bizans döneminde Aziz Prokopios'a adanmış kilisesi nedeniyle Hagios Prokopios diye anılıyordu; Rumlar 1923'e kadar Prokopi derdi. Türkçede Ürküp, sonra Ürgüp biçimini alan ad, Osmanlı belgelerinde de böyle geçer. Şarapçılık ve peribacaları kasabanın simgeleridir.
source: Bizans kaynakları (olgu); Osmanlı Niğde sancağı tahrirleri; mübadele belgeleri
coords: 38.6311,34.9128

@Avanos|ilçe|Nevşehir|İç Anadolu||el
chain: el:Ouénasa>el:Avanós>ota:Avanos>tr:Avanos
era: Antik dönem (MÖ 1. yy)
meaning: Strabon'un andığı, Zeus tapınağıyla ünlü Venasa (Ouenasa) kutsal alanının adından
story: Kızılırmak kıyısındaki çömlekçi kasabası, Strabon'un Kapadokya'da üç bin tapınak kölesi bulunan Zeus Venasa kutsal alanı olarak anlattığı yerin üstündedir. Yunanca Ouenasa adı Türkçede Avanos oldu. Hititlerden beri sürdürülen kırmızı kil çömlekçiliği kasabanın kimliğidir.
source: Strabon, Geographika XII; Osmanlı Niğde sancağı tahrirleri
coords: 38.7153,34.8469

@Hattuşa|antik_kent|Çorum|İç Anadolu||hat
chain: hat:Ḫattuš>hit:Ḫattuša>ota:Boğazköy>tr:Hattuşa
era: Hatti dönemi (MÖ 3. binyıl)
meaning: Hattice Hattuş kent adından; Hitit İmparatorluğu'nun başkenti, Hitit dili "nešili" burada çözüldü
story: Hatti halkının Ḫattuš adlı kenti, MÖ 17. yüzyılda Hitit kralı I. Hattušili'nin başkenti oldu; kral adını kentten aldı. Kadeş Antlaşması'nın tablet nüshası ve otuz bin çivi yazılı tablet burada bulundu; Aslanlı Kapı ve Yerkapı tüneli surların parçasıdır. Osmanlı köyü Boğazköy'ün adı 1950'lerde Boğazkale olarak değiştirildi; UNESCO Dünya Mirası listesindedir.
source: Hitit çivi yazılı arşivi (Boğazköy tabletleri); UNESCO kayıtları (olgu)
coords: 40.0197,34.6153

@Alacahöyük|antik_kent|Çorum|İç Anadolu||tr
chain: ota:Alaca Höyük>tr:Alacahöyük
era: Osmanlı dönemi (19. yy)
meaning: Türkçe alaca "karışık renkli" + höyük "yığma tepe": höyüğün renkli toprak katmanlarından
story: Hitit öncesi Tunç Çağı kral mezarlarıyla ünlü höyük, Türkçe alaca ve höyük sözcükleriyle adlandırılmıştır; Hititçe adının Arinna (Güneş Tanrıçası kenti) olabileceği tartışılır. 1935'te Atatürk'ün isteğiyle başlayan kazı Türk arkeolojisinin ilk büyük projesidir; güneş kursları burada bulundu. Höyük sözcüğü Eski Türkçe üyük biçimindendir.
source: Alacahöyük kazı yayınları (1935, olgu); Hitit çivi yazılı metinler
coords: 40.2333,34.6950

@Gordion|antik_kent|Ankara|İç Anadolu||phr
chain: phr:Gordion>el:Górdion>la:Gordium>ota:Yassıhöyük>tr:Gordion
era: Frig dönemi (MÖ 8. yy)
meaning: Frig kralı Gordios'un adından; Midas'ın başkenti, "Gordion düğümü"nün kesildiği kent
story: Sakarya kıyısındaki Frig başkenti, söylenceye göre öküz arabasıyla kente gelip kral olan Gordios'un adını taşır; kral Midas'ın tümülüsü dünyanın en eski ahşap yapılarından birini saklar. Büyük İskender MÖ 333'te burada ünlü düğümü kılıcıyla kesti. Osmanlı köyü Yassıhöyük'ün yanındaki kazılar 1950'den beri sürer.
source: Arrianus, Anabasis Alexandri II; Strabon, Geographika XII; Gordion kazı yayınları (olgu)
coords: 39.6553,31.9947

@Polatlı|ilçe|Ankara|İç Anadolu||fa
chain: fa:pūlād>ota:Polatlı>tr:Polatlı
era: Osmanlı dönemi (19. yy)
meaning: Farsça pūlād "çelik" (Türkçe polat) + -lı: Polat adlı bir kişinin ya da çelik gibi sert bir yerin köyü
story: Ankara'nın batısındaki bozkır kasabası, Farsça "çelik" anlamındaki pūlād'dan gelen ve Türkçede kişi adı olarak da kullanılan polat sözcüğüyle adlandırılmıştır. 1921 Sakarya Meydan Muharebesi'nin merkezi olan kasaba, Frig başkenti Gordion'a komşudur. Polat, Moğolca ve Türk dillerinde "çelik" anlamıyla yaygındır.
source: Osmanlı Ankara sancağı tahrirleri; Sakarya Muharebesi kayıtları (olgu)
coords: 39.5842,32.1472

@Beypazarı|ilçe|Ankara|İç Anadolu||tr
chain: el:Lagáneia>ota:Beğpazarı>ota:Beypazarı>tr:Beypazarı
era: Osmanlı dönemi (15. yy)
meaning: Türkçe bey + Farsça pazar: Germiyan beyinin kurduğu pazar yerinden; antik adı Lagania
story: Roma yol istasyonu Lagania'nın yerindeki kasaba, Türk döneminde bir beyin kurduğu haftalık pazar yeri olarak Beğpazarı adıyla anıldı. Osmanlı konakları, gümüş işçiliği ve havuç üretimi kasabanın kimliğidir; Suluhan kervansarayı İpek Yolu'nun izidir. Bey sözcüğü Eski Türkçe beg biçiminden gelir.
source: Osmanlı Ankara sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 40.1675,31.9211

@Ulus|semt|Ankara|İç Anadolu||mn
chain: mn:ulus>ota:Taşhan Meydanı>cum:Ulus>tr:Ulus
era: Cumhuriyet dönemi (1930'lar)
meaning: Moğolca ulus "halk, millet": Dil Devrimi'nde millet karşılığı olarak canlandırılan sözcük; Birinci Meclis'in meydanı
story: Ankara'nın eski merkezi Taşhan Meydanı, Birinci Meclis binası ve Zafer Anıtı ile Kurtuluş Savaşı'nın kalbiydi. 1930'larda meydana, Moğolcadan Eski Türkçeye geçmiş ve Dil Devrimi'nde "millet" karşılığı canlandırılan ulus sözcüğü ad olarak verildi. Augustus Tapınağı ve Hacı Bayram Camii aynı semttedir.
source: Dil Devrimi sözcük listeleri (olgu); Cumhuriyet dönemi Ankara şehir planları
coords: 39.9417,32.8550

@Çankaya|semt|Ankara|İç Anadolu||tr
chain: ota:Çankaya (bağ)>cum:Çankaya>tr:Çankaya
era: Cumhuriyet dönemi (1921)
meaning: Türkçe çan + kaya: çan sesi veren kayalıklardan ya da Çankırı'ya bakan kayalıktan; Cumhurbaşkanlığı köşkünün semti
story: Ankara'nın güneyindeki bağlık tepede 1921'de Mustafa Kemal'e armağan edilen bağ evi Cumhurbaşkanlığı Köşkü oldu; semt adı bağ bölgesinin eski adından gelir ve çan ile kaya sözcüklerine bağlanır. Elçilikler ve TBMM'nin bulunduğu Çankaya, Cumhuriyet başkentinin siyasi merkezidir.
source: Cumhuriyet dönemi Ankara şehir planları; Osmanlı Ankara bağ kayıtları (olgu)
coords: 39.9179,32.8627

@Kızılay|semt|Ankara|İç Anadolu||tr
chain: ota:Hilâl-i Ahmer>cum:Kızılay>tr:Kızılay
era: Cumhuriyet dönemi (1935)
meaning: Türkçe kızıl + ay: Hilâl-i Ahmer Cemiyeti'nin 1935'te aldığı Kızılay adından; derneğin genel merkez binasının meydanı
story: 1868'de kurulan Osmanlı Hilâl-i Ahmer Cemiyeti, 1935'te Türkçe karşılık olarak Kızılay adını aldı; Yenişehir'deki genel merkez binasının önündeki meydan bu adla anıldı. Kızıl sözcüğü Eski Türkçe kızıl "kırmızı" biçimiyle Orhun Yazıtları'nda geçer. Güvenpark ve Atatürk Bulvarı semtin eksenidir.
source: Kızılay Derneği kuruluş belgeleri (olgu); Cumhuriyet dönemi Ankara şehir planları
coords: 39.9208,32.8541

@Akşehir|ilçe|Konya|İç Anadolu||tr
chain: el:Philomḗlion>sel:Akşehir>ota:Akşehir>tr:Akşehir
era: Selçuklu dönemi (12. yy)
meaning: Türkçe ak + Farsça şehir: "beyaz şehir"; Nasreddin Hoca'nın yaşadığı kasaba, antik adı Philomelion
story: Sultan Dağları'nın eteğindeki Philomelion, Bizans'ın Konya yolundaki kalesiydi; Selçuklular beyaz taşlı evleri ve kar başlı dağları için Akşehir dediler. Nasreddin Hoca'nın türbesi ve 1402 Ankara Savaşı'ndan sonra Timur'un esiri Yıldırım Bayezid'in öldüğü yer olarak bilinir. Kiraz üretimi ve Nasreddin Hoca şenlikleri kasabayla özdeştir.
source: Anna Komnena, Aleksiad (Philomelion); Evliya Çelebi Seyahatnâmesi; Nasreddin Hoca fıkraları
coords: 38.3575,31.4164

@Beyşehir|ilçe|Konya|İç Anadolu||tr
chain: el:Karállia>sel:Viranşehir>ota:Beyşehir>tr:Beyşehir
era: Beylikler dönemi (13. yy)
meaning: Türkçe bey + Farsça şehir: Eşrefoğlu Beyliği'nin kurucusu Süleyman Bey'in imar ettiği "bey şehri"
story: Beyşehir Gölü kıyısındaki kasaba, Eşrefoğlu Süleyman Bey'in 13. yüzyıl sonunda Viranşehir'in yerine kurduğu beylik merkezidir; adı "beyin şehri" anlamındadır. Ahşap sütunlu Eşrefoğlu Camii (1299) Anadolu'nun en büyük ahşap camisidir. Göl kıyısındaki Hitit kaya anıtı Eflatunpınar ve Kubadabad Sarayı iki ayrı çağın izleridir.
source: Eşrefoğlu Camii kitabesi (olgu); Osmanlı Konya sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 37.6772,31.7261

@Ereğli|ilçe|Konya|İç Anadolu||el
chain: el:Hērákleia (Kybistra)>ar:Hiraqla>sel:Ereğli>ota:Ereğli>tr:Ereğli
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca Herakleia "Herakles'in kenti" adının Türkçe söyleyişi; Anadolu'da aynı adı taşıyan üç Ereğli'den biri
story: Toros geçitlerinin kuzey ağzındaki Kybistra, Roma döneminde Herakles'e adanan Herakleia adını taşıyordu; Arap akınlarında Hiraqla biçimiyle geçer ve Harun Reşid kenti 806'da aldı. Türkçede Ereğli olan ad, Karadeniz Ereğlisi ve Marmara Ereğlisi'nde de aynı Yunanca addan gelir. İvriz'deki Geç Hitit kaya kabartması ilçe sınırlarındadır.
source: Arap-Bizans savaş kronikleri (olgu); İvriz kaya anıtı; Osmanlı Konya sancağı tahrirleri
coords: 37.5131,34.0467

@Çatalhöyük|antik_kent|Konya|İç Anadolu||tr
chain: ota:Çatal Höyük>tr:Çatalhöyük
era: Neolitik dönem (MÖ 7. binyıl)
meaning: Türkçe çatal + höyük: yan yana iki tepeden oluşan "çatal" biçimli höyük
story: Konya Ovası'ndaki Neolitik yerleşim, MÖ 7400'e uzanan dünyanın en eski kentlerinden biridir; evlerin damlarından girilen bu yerleşimde duvar resimleri ve ana tanrıça heykelcikleri bulundu. Türkçe adı, doğu ve batı olmak üzere iki tepeden oluşan höyüğün çatal görünümünden gelir. 2012'de UNESCO Dünya Mirası oldu.
source: Çatalhöyük kazı yayınları (1961–, olgu); UNESCO kayıtları
coords: 37.6667,32.8283

@Kültepe|antik_kent|Kayseri|İç Anadolu||hit
chain: hit:Kaneš / Neša>akk:Kaniš>ota:Kültepe>tr:Kültepe
era: Asur Ticaret Kolonileri dönemi (MÖ 20. yy)
meaning: Türkçe kül + tepe: höyüğün kül renkli toprağından; antik adı Kaneš/Neša, Hititlerin dillerine "nešili" demesinin kaynağı
story: Asurlu tüccarların MÖ 20. yüzyılda kurduğu Kaniš karumu, Anadolu'nun en eski yazılı belgeleri olan 23 bin çivi yazılı tableti verdi. Hititler bu kente Neša diyor ve kendi dillerine "nešili" adını veriyordu. Türkçe Kültepe adı, yüzyıllarca gübre olarak kazılan kül renkli höyük toprağından gelir. Kazılar 1948'den beri sürer.
source: Kültepe tabletleri (olgu); Hitit çivi yazılı belgeleri (Anitta metni)
coords: 38.8497,35.6353

@Erciyes Dağı|dağ|Kayseri|İç Anadolu||el
chain: el:Argaîos>la:Argaeus>ota:Erciyes>tr:Erciyes Dağı
era: Antik dönem (MÖ 1. yy)
meaning: Yunanca Argaios "parlak, beyaz" (argós) dağ adının Türkçe söyleyişi; Kapadokya'nın volkanik zirvesi
story: Strabon'un "zirvesinden iki denizin görüldüğü" diye anlattığı Argaios, 3917 metrelik sönmüş bir volkandır ve Kayseri'nin antik sikkelerinde dağ tasvir edilir; adı Yunanca "parlak, beyaz" sözcüğüyle açıklanır. Türkçede Erciyes biçimini alan dağ, Kapadokya tüfünü püskürten volkandır. Kayak merkezi ve Yörük yaylaları dağın eteklerindedir.
source: Strabon, Geographika XII; Kayseri antik sikkeleri (olgu); Evliya Çelebi Seyahatnâmesi
coords: 38.5333,35.4500

@Divriği|ilçe|Sivas|İç Anadolu||el
chain: el:Tephrikḗ>ar:Abrīq>sel:Divriği>ota:Divriği>tr:Divriği
era: Bizans dönemi (9. yy)
meaning: Bizans dönemindeki Tephrike kale adının Türkçe söyleyişi; Pavlikanların 9. yüzyıl başkenti
story: 9. yüzyılda Pavlikan mezhebinin başkenti olan Tephrike, Bizans ve Arap kaynaklarında geçer; Türkçede Divriği biçimini aldı. Mengücek beyi Ahmed Şah'ın 1228'de yaptırdığı Ulu Cami ve Darüşşifa, taş işçiliğinin doruğu olarak UNESCO listesindedir. Demir madeni yüzyıllardır işletilmektedir.
source: Bizans kronikleri (Theophanes Continuatus, olgu); Divriği Ulu Camii kitabesi; UNESCO kayıtları
coords: 39.3714,38.1147

@Tyana|antik_kent|Niğde|İç Anadolu||hit
chain: hit:Tuwanuwa>el:Týana>la:Tyana>ota:Kemerhisar>tr:Tyana
era: Hitit dönemi (MÖ 2. binyıl)
meaning: Hitit metinlerindeki Tuwanuwa kentinin adından; Geç Hitit Tabal krallığının merkezi
story: Hitit belgelerinde Tuwanuwa, Geç Hitit döneminde Tuwana adıyla Tabal krallığının merkezi olan kent, Roma'da filozof Apollonios'un doğum yeri olarak ünlendi. Roma su kemerleri Osmanlı köyüne Kemerhisar adını verdirdi. Kral Warpalawas'ın İvriz kabartması bu krallığın eseridir.
source: Hitit çivi yazılı belgeleri; Strabon, Geographika XII; Philostratos (Apollonios'un Yaşamı)
coords: 37.8483,34.6111

@Hacıbektaş|ilçe|Nevşehir|İç Anadolu||ar
chain: ota:Sulucakarahöyük>ota:Hacıbektaş>tr:Hacıbektaş
era: Osmanlı dönemi (16. yy)
meaning: Bektaşîliğin kurucusu Hacı Bektaş Veli'nin adından; Arapça ḥācc "hacı" + Farsça Bektaş kişi adı
story: 13. yüzyılda Horasan'dan gelip Sulucakarahöyük köyüne yerleşen Hacı Bektaş Veli'nin dergâhı, Bektaşîliğin ve Yeniçeri Ocağı'nın manevi merkezi oldu; köy onun adıyla anıldı. Dergâh 1925'te tekkelerin kapatılmasından sonra 1964'te müze oldu; her ağustos anma törenleri düzenlenir. Bektaş adı Farsça kökenli bir kişi adıdır.
source: Vilâyetnâme-i Hacı Bektaş Veli; Evliya Çelebi Seyahatnâmesi
coords: 38.9425,34.5583

@Sivrihisar|ilçe|Eskişehir|İç Anadolu||tr
chain: el:Iustinianoúpolis>ota:Sivrihisar>tr:Sivrihisar
era: Osmanlı dönemi (14. yy)
meaning: Türkçe sivri + Arapça hisar "kale": sivri kayalıklar üstündeki kaleden; Bizans adı Iustinianopolis
story: Frigya'nın Pessinus kutsal kentine komşu olan kasaba, Bizans döneminde Iustinianopolis adını taşıyordu; Türkler sivri kayalıklar üzerindeki kalesi için Sivrihisar dediler. Ahşap direkli Ulu Cami (1274) ve Nasreddin Hoca'nın doğum yeri sayılan Hortu köyü kasabanın belleğidir. Pessinus'ta Kybele'nin kara taşı Roma'ya buradan götürülmüştü.
source: Strabon, Geographika XII (Pessinus); Sivrihisar Ulu Camii kitabesi (olgu); Evliya Çelebi Seyahatnâmesi
coords: 39.4506,31.5361

@Seyitgazi|ilçe|Eskişehir|İç Anadolu||ar
chain: el:Nakóleia>ota:Seyyid Gazi>tr:Seyitgazi
era: Osmanlı dönemi (13. yy)
meaning: Arap-Bizans savaşlarının destan kahramanı Seyyid Battal Gazi'nin adından; Arapça sayyid "efendi" + ğāzī
story: Bizans'ın Nakoleia kentinin yanındaki tepede, 8. yüzyıl Arap-Bizans savaşlarının efsanevi kahramanı Battal Gazi'nin türbesi 13. yüzyılda Selçuklu sultanının annesi tarafından yaptırıldı; çevresindeki külliye Bektaşî dergâhı oldu. Battalnâme destanı Anadolu'da yüzyıllarca okundu; kasaba onun adını taşır. Frig vadisinin Midas anıtı yakınındadır.
source: Battalnâme; Seyyid Battal Gazi külliyesi kitabeleri (olgu); Evliya Çelebi Seyahatnâmesi
coords: 39.4461,30.6914

@Tuz Gölü|göl|Aksaray|İç Anadolu||tr
chain: el:Tátta>ota:Tuz Gölü>tr:Tuz Gölü
era: Antik dönem (MÖ 1. yy)
meaning: Türkçe tuz + göl: Türkiye'nin ikinci büyük gölü, yazın kuruyan tuz tabakasından; antik adı Tatta
story: Strabon'un Tatta adıyla andığı ve "kuşların tüylerinin tuzla kaplandığı" diye anlattığı sığ göl, Anadolu'nun tuz ihtiyacını yüzyıllardır karşılar. Türkçe tuz sözcüğü Eski Türkçe tuz biçimiyle Orhun Yazıtları'nda geçer. Göl yazın kuruyarak beyaz bir düzlüğe dönüşür; flamingo kolonileriyle de bilinir.
source: Strabon, Geographika XII; Dîvânu Lugâti't-Türk (tuz)
coords: 38.7500,33.3500

@Kızılırmak|nehir|Kırşehir|İç Anadolu||tr
chain: hit:Marassantiya>el:Hálys>ota:Kızılırmak>tr:Kızılırmak
era: Hitit dönemi (MÖ 2. binyıl)
meaning: Türkçe kızıl + ırmak: taşıdığı kızıl renkli alüvyondan; Yunanca Halys "tuzlu", Hititçe Marassantiya
story: Türkiye'nin en uzun ırmağı, Hitit metinlerinde Marassantiya, Yunan kaynaklarında tuzlu topraklardan aktığı için Halys adıyla geçer; Lidya kralı Kroisos'un "Halys'i geçersen büyük bir imparatorluğu yıkacaksın" kehaneti bu ırmakla ilgilidir. Türkler taşıdığı kızıl alüvyonlardan dolayı Kızılırmak dediler. Irmak sözcüğü Eski Türkçe ırmak "akarsu" biçiminden gelir.
source: Herodotos I (Kroisos kehaneti); Hitit çivi yazılı belgeleri; Dîvânu Lugâti't-Türk
coords: 39.5000,34.5000

# ===================================================================== KARADENİZ
@Safranbolu|ilçe|Karabük|Karadeniz||ar
chain: el:Dadýbra>sel:Zalifre>ota:Taraklıborlu>ota:Safranbolu>tr:Safranbolu
era: Osmanlı dönemi (17. yy)
meaning: Arapça zaʿfarān "safran" + Yunanca pólis "şehir" (Türkçe bolu): safran yetiştirilen şehir
story: Bizans'ın Dadybra kalesi Selçuklu belgelerinde Zalifre, Osmanlı'da Taraklıborlu adıyla geçer; 17. yüzyıldan sonra yörede yetiştirilen safran nedeniyle Safranbolu adı yerleşti. Bolu öğesi Yunanca pólis sözcüğünden, safran Arapçadan gelir. Osmanlı ahşap konaklarıyla UNESCO Dünya Mirası olan kasaba, Cinci Hanı ve Köprülü Camii ile ünlüdür.
source: Evliya Çelebi Seyahatnâmesi; Osmanlı Bolu sancağı tahrirleri; UNESCO kayıtları (olgu)
coords: 41.2508,32.6936

@Amasra|ilçe|Bartın|Karadeniz||el
chain: el:Sēsamós>el:Ámastris>la:Amastris>ota:Amasra>tr:Amasra
era: Antik dönem (MÖ 4. yy)
meaning: Pers prensesi Amastris'in (Dareios'un yeğeni) kurduğu kentin adı; eski adı Sesamos
story: Homeros'un andığı Sesamos, MÖ 300 dolaylarında Herakleia Pontika tiranının eşi Pers prensesi Amastris tarafından yeniden kurulup onun adını aldı. Cenevizliler 13.–15. yüzyılda kaleyi onardı; Fatih 1460'ta kenti alınca "çeşm-i cihan" (dünyanın gözü) dediği aktarılır. Türkçede Amasra biçimini alan kasaba kalesi ve limanıyla ünlüdür.
source: Homeros, İlyada II; Strabon, Geographika XII; Pîrî Reis, Kitâb-ı Bahriye
coords: 41.7489,32.3864

@Çarşamba|ilçe|Samsun|Karadeniz||fa
chain: fa:çahār-şanba>ota:Çarşamba Pazarı>tr:Çarşamba
era: Osmanlı dönemi (17. yy)
meaning: Farsça çahār-şanba "dördüncü gün": haftanın çarşamba günü kurulan pazardan
story: Yeşilırmak deltasındaki kasaba, haftanın çarşamba günleri kurulan büyük pazarından adını aldı; aynı yolla Cumapazarı, Perşembe gibi başka Anadolu kasabaları da gün adlarıyla anılır. Çarşamba sözcüğü Farsça çahār "dört" ve şanba "gün" öğelerinden gelir. Ovanın Hitit dönemi yerleşimi İkiztepe yakındadır.
source: Osmanlı Canik sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 41.1986,36.7211

@Fatsa|ilçe|Ordu|Karadeniz||el
chain: el:Phadisánē>el:Polemṓnion>ota:Fatsa>tr:Fatsa
era: Antik dönem (MÖ 1. yy)
meaning: Antik Phadisane limanının adından; Roma döneminde kral Polemon'un adıyla Polemonion
story: Karadeniz kıyısındaki liman, Arrianus'un Periplus'unda Phadisane olarak geçer; Pontus kralı Polemon kenti yeniden kurup Polemonion adını verdi. Türkçede Fatsa biçimini alan kasabanın yakınındaki Cıngırt Kayası antik akropoldür. Fındık ve balıkçılık kasabanın yaşamıdır.
source: Arrianus, Periplus Ponti Euxini; Pîrî Reis, Kitâb-ı Bahriye
coords: 41.0300,37.5000

@Ünye|ilçe|Ordu|Karadeniz||el
chain: el:Oinóē>ota:Ünye>tr:Ünye
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca oínos "şarap" sözcüğünden Oinoe "bağlık, şarap yeri"
story: Ksenophon'un ordusunun uğradığı kıyıdaki Oinoe, adını Yunanca şarap sözcüğünden alır; Bizans ve Trabzon Rum İmparatorluğu döneminde kale kentiydi. Türkçede Ünye olan kasaba, 18. yüzyılda Canikli Ali Paşa'nın saray kenti olarak zenginleşti. Ünye Kalesi ve Çakırtepe kasabanın simgeleridir.
source: Ksenophon, Anabasis V; Arrianus, Periplus; Evliya Çelebi Seyahatnâmesi
coords: 41.1275,37.2883

@Tirebolu|ilçe|Giresun|Karadeniz||el
chain: el:Trípolis>ota:Tirebolu>tr:Tirebolu
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca trí- "üç" + pólis "şehir": üç kale ya da üç yerleşimden oluşan kent
story: Harşit Çayı'nın ağzındaki Tripolis, üç kalesi (Aziz Yuhanna, Andoz ve Bedrama) nedeniyle "üç şehir" adını taşıyordu; Türkçe söyleyiş Tirebolu, -polis öğesini bolu biçiminde korur. 1461'de Osmanlı'ya katılan kasaba, Osmanlı ve Rus savaşlarında sınır hattında kaldı. Fındık ve balıkçılık ekonomisinin temelidir.
source: Arrianus, Periplus; Pîrî Reis, Kitâb-ı Bahriye; Evliya Çelebi Seyahatnâmesi
coords: 41.0058,38.8167

@Şebinkarahisar|ilçe|Giresun|Karadeniz||ar
chain: el:Kolṓneia>sel:Karahisar>ota:Şebinkarahisar>tr:Şebinkarahisar
era: Osmanlı dönemi (16. yy)
meaning: Arapça şebb "şap" (Türkçe şebin) + Karahisar: şap madeniyle ünlü kara kale
story: Roma'nın Koloneia adlı askerî kolonisinin yerindeki kale, Türk döneminde Karahisar diye anıldı; 15.–17. yüzyıllarda Avrupa'ya satılan şap madeni nedeniyle Şebin (şap) sözcüğü eklendi. Anadolu'daki öteki Karahisarlardan bu ekle ayrılır. Pontus kralı Mithridates'in kalesi ve Meryemana Manastırı kasabanın tarihî yapılarıdır.
source: Osmanlı maden kayıtları (olgu); Evliya Çelebi Seyahatnâmesi; Strabon, Geographika XII
coords: 40.2886,38.4236

@Akçaabat|ilçe|Trabzon|Karadeniz||tr
chain: el:Platána>ota:Pulathane>cum:Akçaabat>tr:Akçaabat
era: Cumhuriyet dönemi (1920'ler)
meaning: Türkçe akça "beyazımsı" + Farsça ābād "bayındır yer"; Rumca Platana "çınar" (Osmanlı Pulathane)
story: Trabzon'un batısındaki liman kasabası, kıyısındaki çınarlardan dolayı Rumca Platana adını taşıyor ve Osmanlı belgelerinde Pulathane yazılıyordu. 1920'lerde Türkçe akça ile Farsça kökenli -abat öğesinden oluşan Akçaabat adı verildi; aynı -abat öğesi Arnavutköy'den Hereke'ye birçok adda görülür. Akçaabat köftesi ve horon kasabayla anılır.
source: Pîrî Reis, Kitâb-ı Bahriye (Platana); Osmanlı Trabzon salnameleri
coords: 41.0211,39.5711

@Maçka|ilçe|Trabzon|Karadeniz||el
chain: el:Matzoúka>ota:Maçka>tr:Maçka
era: Bizans dönemi (13. yy)
meaning: Bizans dönemi Matzouka vadi adının Türkçe söyleyişi; Sümela Manastırı'nın bulunduğu vadi
story: Trabzon'un güneyindeki dağlık vadi, Trabzon Rum İmparatorluğu kayıtlarında Matzouka adıyla geçer; 4. yüzyılda kurulan Sümela (Panagia Soumela) Manastırı bu vadinin kayalığına yapılmıştır. Türkçede Maçka biçimini alan kasaba, yaylaları ve Zigana geçidiyle İran transit yolunun üzerindeydi.
source: Trabzon Rum İmparatorluğu belgeleri (olgu); Evliya Çelebi Seyahatnâmesi
coords: 40.8100,39.6150

@Of|ilçe|Trabzon|Karadeniz||el
chain: el:Óphis>ota:Of>tr:Of
era: Antik dönem (MÖ 1. yy)
meaning: Yunanca óphis "yılan": kıvrılarak akan Of (Solaklı) Deresi'nin adından
story: Türkiye'nin en kısa adlı ilçesi, Arrianus'un Periplus'unda Ophis "yılan" adıyla geçen derenin ağzındadır; ad derenin kıvrımlı akışına bağlanır. Osmanlı döneminde medreseleriyle ünlenen kasaba "Of'un hocaları" deyişine kaynak oldu. Çay bahçeleri ve Sultan Murad yaylası kasabanın simgeleridir.
source: Arrianus, Periplus Ponti Euxini; Osmanlı Trabzon salnameleri
coords: 40.9500,40.2667

@Sürmene|ilçe|Trabzon|Karadeniz||el
chain: el:Sourména>ota:Sürmene>tr:Sürmene
era: Antik dönem (MÖ 4. yy)
meaning: Ksenophon'un andığı Hyssos limanı yakınındaki Sourmena yerleşiminin adından
story: Onbinler'in Trabzon'a varmadan önce konakladığı Hyssos limanına komşu olan Sourmena, Bizans kayıtlarında geçer; Türkçede Sürmene oldu. Yakut saplı bıçakları ve ahşap tekne yapımıyla bilinen kasabanın Memiş Ağa Konağı Osmanlı sivil mimarisinin örneğidir.
source: Ksenophon, Anabasis IV; Arrianus, Periplus; Osmanlı Trabzon salnameleri
coords: 40.9100,40.1200

@Pazar|ilçe|Rize|Karadeniz||tr
chain: el:Athḗnai>ota:Atina>cum:Pazar>tr:Pazar
era: Cumhuriyet dönemi (1928)
meaning: Farsça kökenli Türkçe pazar: haftalık pazar yerinden; antik adı Athenai (Atina), 1928'de değiştirildi
story: Lazların yaşadığı kıyı kasabası, Arrianus'ta Athenai adıyla geçen antik limanın yerindedir; Osmanlı'da Atina yazılan ad, Yunanistan'ın başkentiyle karışmasın diye 1928'de kasabanın pazar yeri özelliğine göre Pazar olarak değiştirildi. Lazca ve çay kültürü kasabanın kimliğidir; Kız Kalesi kıyıdaki Orta Çağ yapısıdır.
source: Arrianus, Periplus Ponti Euxini; 1928 tarihli ad değişikliği kararı
coords: 41.1797,40.8872

@Ardeşen|ilçe|Rize|Karadeniz||ka
chain: lzz:Art'aşeni>ota:Ardeşen>tr:Ardeşen
era: Osmanlı dönemi (17. yy)
meaning: Lazca yer adı; Laz dilinde "Art'aşeni" biçiminin Türkçe söyleyişi
story: Fırtına Deresi'nin Karadeniz'e döküldüğü yerdeki kasaba, Lazca Art'aşeni adının Türkçeleşmiş biçimidir; Lazca, Gürcüceyle akraba bir Güney Kafkas dilidir ve yöredeki birçok yer adının kaynağıdır. Fırtına Vadisi'nin Osmanlı kemer köprüleri ve Hemşin yaylaları ilçe sınırlarındadır.
source: Osmanlı Rize kazası tahrirleri; Lazca yer adı derlemeleri (olgu)
coords: 41.1917,40.9867

@Hopa|ilçe|Artvin|Karadeniz||ka
chain: lzz:Xopa>ota:Hopa>tr:Hopa
era: Osmanlı dönemi (17. yy)
meaning: Lazca yer adı Xopa'nın Türkçe söyleyişi; Gürcistan sınırındaki liman
story: Türkiye'nin en kuzeydoğu limanı, Lazca Xopa adıyla anılır; Lazca x sesi Türkçede h'ye dönüşmüştür. Osmanlı döneminde Batum'a bağlı olan kasaba, 1878'den sonra sınır kasabası oldu. Sarp sınır kapısı ve çay fabrikalarıyla tanınır.
source: Osmanlı Lazistan sancağı kayıtları; Lazca yer adı derlemeleri (olgu)
coords: 41.3903,41.4225

@Şavşat|ilçe|Artvin|Karadeniz||ka
chain: ka:Şavşeti>ota:Şavşat>tr:Şavşat
era: Orta Çağ Gürcü kaynakları (9. yy)
meaning: Gürcüce Şavşeti "Şavşların ülkesi": Gürcü Bagrat krallığının bir bölgesinin adı
story: Gürcü vakayinamelerinde Şavşeti adıyla geçen dağlık bölge, Orta Çağ Gürcü kilise ve kalelerini barındırır; Tbeti Kilisesi bunlardandır. Osmanlı 16. yüzyılda bölgeyi aldı; Türkçede Şavşat oldu. Karagöl ve Sahara yaylası ilçenin doğal mirasıdır.
source: Gürcü vakayinameleri (Kartlis Tskhovreba); Osmanlı Çıldır eyaleti tahrirleri
coords: 41.2444,42.3658

@Yusufeli|ilçe|Artvin|Karadeniz||tr
chain: ota:Kiskim>ota:Yusufeli>tr:Yusufeli
era: Osmanlı dönemi (1914)
meaning: Veliaht Yusuf İzzeddin Efendi'nin adından "Yusuf'un ili"; Arapça Yūsuf + Türkçe el "yurt"
story: Çoruh vadisindeki Kiskim kazasına 1914'te, dönemin veliahdı Yusuf İzzeddin Efendi'nin adıyla Yusufeli adı verildi; -eli öğesi Kocaeli ve Tunceli'de olduğu gibi "yurt" anlamındaki Türkçe el sözcüğüdür. Gürcü kiliseleri (İşhan, Barhal) ve rafting yapılan Çoruh, ilçenin mirasıdır; eski kasaba 2023'te baraj gölü altında kaldı.
source: Osmanlı salnameleri (1914 kazası); Cumhuriyet dönemi idari kayıtları
coords: 40.8219,41.5406

@Kelkit|ilçe|Gümüşhane|Karadeniz||hy
chain: hy:Gayl-get>el:Lýkos>ota:Kelkit>tr:Kelkit
era: Antik dönem (MÖ 1. yy)
meaning: Ermenice gayl "kurt" + get "ırmak": "kurt ırmağı"; Yunanca Lykos aynı anlamın çevirisidir
story: Yeşilırmak'ın en uzun kolu olan Kelkit Çayı, antik çağda Yunanca "kurt" anlamındaki Lykos adını taşıyordu; Ermenice Gayl-get aynı anlamı verir ve Türkçe Kelkit bu biçimden gelir. Irmağın kaynak vadisindeki kasaba 1071 öncesinden beri Türk akınlarına açık bir geçit yoluydu; Sadak köyündeki Satala lejyon kampı Roma dönemine aittir.
source: Strabon, Geographika XII (Lykos); Osmanlı Erzurum eyaleti tahrirleri
coords: 40.1292,39.4383

@İnebolu|ilçe|Kastamonu|Karadeniz||el
chain: el:Abōnóteichos>el:Iōnópolis>ota:İnebolu>tr:İnebolu
era: Antik dönem (MÖ 1. binyıl)
meaning: Yunanca Ionopolis "İyonya kenti" adının Türkçe söyleyişi; eski adı Abonouteichos
story: Lucianus'un yalancı kâhin Aleksandros hikâyesine konu olan Abonouteichos, kâhinin isteğiyle 2. yüzyılda Ionopolis adını aldı; Türkçe İnebolu bu adın -polis öğesini bolu biçiminde korur. Kurtuluş Savaşı'nda İstanbul'dan gelen silahların Anadolu'ya çıkarıldığı liman olduğu için İstiklal Madalyası aldı; Atatürk Şapka İnkılâbı yolculuğuna buradan başladı.
source: Lucianus, Alexandros (olgu); Pîrî Reis, Kitâb-ı Bahriye; Kurtuluş Savaşı belgeleri
coords: 41.9750,33.7617

@Taşköprü|ilçe|Kastamonu|Karadeniz||tr
chain: el:Pompēioúpolis>ota:Taşköprü>tr:Taşköprü
era: Osmanlı dönemi (15. yy)
meaning: Türkçe taş + köprü: Gökırmak üzerindeki taş köprüden; antik adı Pompeiopolis
story: Roma komutanı Pompeius'un MÖ 64'te Paflagonya'da kurduğu Pompeiopolis'in kalıntıları Zımbıllı Tepe'dedir; Türk kasabası ise Gökırmak üzerindeki Selçuklu dönemi taş köprüsünden adını aldı. Sarımsak üretimiyle Türkiye çapında tanınır; köprü sözcüğü Eski Türkçe köprüg biçiminden gelir.
source: Strabon, Geographika XII; Osmanlı Kastamonu sancağı tahrirleri
coords: 41.5097,34.2131

@Karadeniz Ereğli|ilçe|Zonguldak|Karadeniz||el
chain: el:Hērákleia Pontikḗ>la:Heraclea Pontica>gen:Pontaraclia>ota:Ereğli>tr:Karadeniz Ereğli
era: Antik dönem (MÖ 6. yy)
meaning: Yunanca Herakleia "Herakles'in kenti": Herakles'in Kerberos'u yeraltından çıkardığına inanılan Akheron mağarasının kenti
story: Megaralıların MÖ 560'ta kurduğu Herakleia Pontika, söylenceye göre Herakles'in yeraltı köpeği Kerberos'u çıkardığı Akheron mağarasının (Cehennemağzı) yanındadır. Cenevizlilerin Pontaraclia dediği kent 1360'ta Osmanlı'ya geçti; Türkçe Ereğli adı Konya ve Marmara Ereğlilerinden Karadeniz sözcüğüyle ayrılır. 1829'da taş kömürünün bulunması ve demir-çelik fabrikası kentin modern kimliğidir.
source: Ksenophon, Anabasis VI; Strabon, Geographika XII; Pîrî Reis, Kitâb-ı Bahriye
coords: 41.2833,31.4167

@Terme|ilçe|Samsun|Karadeniz||el
chain: el:Thermṓdōn>ota:Terme>tr:Terme
era: Antik dönem (MÖ 1. binyıl)
meaning: Söylencede Amazonların ülkesindeki Thermodon Irmağı'nın adından
story: Yunan söylencesi Amazonların başkenti Themiskyra'yı Thermodon Irmağı'nın ağzına yerleştirir; Herodotos ve Strabon bu ırmağı anlatır. Türkçede Terme olan ad kasabaya ve ırmağa verilmiştir. Çarşamba Ovası'nın doğusundaki kasaba pirinç tarımıyla bilinir.
source: Herodotos IV; Strabon, Geographika XII; Osmanlı Canik sancağı tahrirleri
coords: 41.2092,36.9719

@Zile|ilçe|Tokat|Karadeniz||el
chain: el:Zḗla>la:Zela>ota:Zile>tr:Zile
era: Antik dönem (MÖ 1. binyıl)
meaning: Anaitis tapınağıyla ünlü Pontus kenti Zela'nın adından; Sezar'ın "veni, vidi, vici" dediği savaşın yeri
story: Pers tanrıçası Anaitis'in tapınak kenti Zela, MÖ 47'de Iulius Caesar'ın Pontus kralı Pharnakes'i yendiği ve Roma'ya "geldim, gördüm, yendim" diye yazdığı savaşın yeridir. Türkçede Zile biçimini alan kasaba, Osmanlı'da pekmeziyle ünlendi; kalesi ve Roma tiyatrosu höyük üzerindedir.
source: Suetonius, Divus Iulius 37; Strabon, Geographika XII; Evliya Çelebi Seyahatnâmesi
coords: 40.3031,35.8856

@Niksar|ilçe|Tokat|Karadeniz||el
chain: el:Kábeira>el:Neokaisáreia>ar:Nīksār>sel:Niksar>tr:Niksar
era: Roma dönemi (1. yy)
meaning: Yunanca Neokaisareia "yeni Kayser (Sezar) kenti" adının Türkçe söyleyişi
story: Pontus kralı Mithridates'in sarayının bulunduğu Kabeira, Roma döneminde Neokaisareia adını aldı; 4. yüzyılda Aziz Gregorios Thaumaturgos'un piskoposluk kentiydi. Danişmend Gazi 11. yüzyılda kenti başkent yaptı; adı Niksar biçimine dönüştü ve Danişmendnâme'de Niksar kalesi anlatılır. Ayvaz suyu ve ceviz üretimiyle bilinir.
source: Strabon, Geographika XII; Danişmendnâme; Evliya Çelebi Seyahatnâmesi
coords: 40.5914,36.9517

@Boyabat|ilçe|Sinop|Karadeniz||tr
chain: ota:Boyâbâd>tr:Boyabat
era: Selçuklu dönemi (13. yy)
meaning: Türkçe boy "oymak, aşiret" + Farsça ābād "bayındır yer": bir Türkmen boyunun yerleştiği yer
story: Gökırmak vadisindeki kasabanın adı, Türkçe boy "oymak" ve Farsça -abad "bayındır" öğelerinin birleşmesinden oluşur; Selçuklu döneminde yöreye yerleşen Türkmen boylarını anlatır. Kalesi Paflagonya döneminden kalmadır; Boyabat Kaya Mezarları ve çeltik üretimi kasabanın simgeleridir.
source: Osmanlı Kastamonu sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 41.4686,34.7667

@Akçakoca|ilçe|Düzce|Karadeniz||tr
chain: el:Diápolis>ota:Akçaşehir>cum:Akçakoca>tr:Akçakoca
era: Cumhuriyet dönemi (1934)
meaning: Osmanlı'nın ilk fetihlerini yapan komutan Akça Koca'nın adından; Türkçe akça "beyaz" + koca "yaşlı, ulu"
story: Bizans'ın Diapolis kasabası Osmanlı döneminde Akçaşehir adıyla anılıyordu; 1934'te, Orhan Gazi döneminde Kocaeli'ni fetheden ve türbesi burada olan Akça Koca'nın adı verildi. Fındık bahçeleri ve Ceneviz Kalesi kasabanın simgeleridir; Türkçe koca sözcüğü Eski Türkçe koca "yaşlı, saygın" anlamındadır.
source: Âşıkpaşazâde Tarihi; Osmanlı Bolu sancağı tahrirleri; 1934 tarihli ad değişikliği kararı
coords: 41.0867,31.1150

@Vakfıkebir|ilçe|Trabzon|Karadeniz||ar
chain: el:Kerasoûs (Büyükliman)>ota:Vakf-ı Kebîr>tr:Vakfıkebir
era: Osmanlı dönemi (16. yy)
meaning: Arapça vakf-ı kebîr "büyük vakıf": kasabanın büyük bir vakfa bağlı arazi olmasından
story: Trabzon'un batısındaki Büyükliman koyundaki kasaba, Osmanlı döneminde gelirleri büyük bir vakfa ayrılmış arazi olduğu için Arapça "büyük vakıf" anlamındaki Vakf-ı Kebir adıyla anıldı. Vakfıkebir ekmeği ve tereyağı kasabayla özdeştir; antik dönemde bölgede bir başka Kerasous limanı bulunduğu aktarılır.
source: Osmanlı Trabzon sancağı vakıf kayıtları (olgu); Evliya Çelebi Seyahatnâmesi
coords: 41.0458,39.2797

@Bafra|ilçe|Samsun|Karadeniz||unk
chain: el:Paûra>ota:Bafra>tr:Bafra
era: Osmanlı dönemi (15. yy)
meaning: Kökeni tartışmalı; antik Paura yerleşimi ya da Rumca bir yer adıyla ilişkilendirilir
story: Kızılırmak deltasındaki kasaba, Osmanlı belgelerinde Bafra adıyla geçer; adın antik Paura yerleşiminden ya da Rumca bir sözcükten geldiği ileri sürülür ancak kanıt kesin değildir. İkiztepe höyüğü Tunç Çağı'na uzanır; tütün ve pide kasabanın simgeleridir. Kızılırmak Deltası kuş cenneti UNESCO geçici listesindedir.
source: Osmanlı Canik sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 41.5678,35.9069

@Merzifon|ilçe|Amasya|Karadeniz||unk
chain: hy:Marzvan>ota:Merzifon>tr:Merzifon
era: Osmanlı dönemi (14. yy)
meaning: Kökeni tartışmalı; Ermenice Marzvan ya da Farsça merz "sınır" ile "sınır boyu" anlamıyla ilişkilendirilir
story: Amasya'nın batısındaki ova kasabası, Ermeni kaynaklarında Marzvan, Osmanlı belgelerinde Merzifon yazılır; adın Farsça merz "sınır" sözcüğüyle ilişkisi ya da daha eski bir Anadolu adı olabileceği tartışılır. Kara Mustafa Paşa'nın külliyesi ve II. Murad'ın medresesi Osmanlı eserleridir; Anadolu Koleji 19. yüzyılda burada kuruldu.
source: Osmanlı Amasya sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 40.8750,35.4628

# ===================================================================== DOĞU ANADOLU
@Ani|antik_kent|Kars|Doğu Anadolu||hy
chain: hy:Ani>ota:Anı>tr:Ani
era: Orta Çağ (10. yy)
meaning: Ermenice Ani, İran tanrıçası Anahit'in adıyla ilişkilendirilen kale ve kent adı
story: Arpaçay vadisinin kenarındaki Ani, 961'de Bagratlı Ermeni Krallığı'nın başkenti oldu ve "bin bir kiliseli kent" diye anıldı; adı Anahit kültüyle ilişkilendirilen eski bir kale adından gelir. Selçuklular 1064'te kenti aldı; Anadolu'daki ilk Türk camisi Menuçehr Camii burada yapıldı. Moğol istilası ve depremler kenti ıssızlaştırdı; 2016'da UNESCO Dünya Mirası oldu.
source: Ermeni vakayinameleri (olgu); Selçuklu kaynakları (Ani fethi, 1064); UNESCO kayıtları
coords: 40.5067,43.5728

@Sarıkamış|ilçe|Kars|Doğu Anadolu||tr
chain: ota:Sarıkamış>tr:Sarıkamış
era: Osmanlı dönemi (18. yy)
meaning: Türkçe sarı + kamış: sarı kamışlıkların bulunduğu yer; 1914 Sarıkamış Harekâtı'nın yeri
story: Allahuekber Dağları'nın eteğindeki kasabanın adı, çayır ve bataklıklardaki sarı kamışlıklardan gelir. 1878–1918 Rus yönetiminde Çarlık subaylarının kışlalarıyla gelişti; Aralık 1914'te Osmanlı ordusunun donarak büyük kayıp verdiği harekât bu dağlarda yaşandı. Sarıçam ormanları ve kayak merkezi bugünkü kimliğidir.
source: Osmanlı Kars eyaleti kayıtları; Sarıkamış Harekâtı askerî raporları (olgu)
coords: 40.3333,42.5833

@Oltu|ilçe|Erzurum|Doğu Anadolu||ka
chain: ka:Oltisi>ota:Oltu>tr:Oltu
era: Orta Çağ Gürcü kaynakları (10. yy)
meaning: Gürcü kaynaklarındaki Oltisi kale adının Türkçe söyleyişi; Oltu taşı (kara kehribar) yöresi
story: Çoruh havzasının Gürcü Tao-Klarceti bölgesindeki Oltisi kalesi, Orta Çağ vakayinamelerinde geçer; Türkçede Oltu olmuştur. 1878–1918 arasında Rus yönetiminde kaldı. Yörede çıkarılan kara kehribar "Oltu taşı" tespih ve takı yapımında kullanılır; kalesi kasabanın üstündedir.
source: Gürcü vakayinameleri (olgu); Osmanlı Erzurum eyaleti tahrirleri
coords: 40.5461,41.9878

@İspir|ilçe|Erzurum|Doğu Anadolu||hy
chain: hy:Sper>el:Syspirîtis>ota:İspir>tr:İspir
era: Antik dönem (MÖ 1. yy)
meaning: Ermenice Sper bölge adından; Strabon'un altın madenleriyle andığı Syspiritis
story: Çoruh'un yukarı vadisindeki İspir, Strabon'un altın madenleriyle ünlü Syspiritis bölgesine karşılık gelir; Ermenice Sper adı Bagratlı hanedanının kökeniyle ilişkilendirilir. Selçuklu ve Saltuklu döneminde kalesi onarıldı; Türkçede İspir oldu. Yaylaları ve Çoruh rafting parkurlarıyla bilinir.
source: Strabon, Geographika XI; Ermeni vakayinameleri (olgu); Osmanlı Erzurum eyaleti tahrirleri
coords: 40.4833,41.0000

@Pasinler|ilçe|Erzurum|Doğu Anadolu||hy
chain: hy:Basean>ota:Hasankale>cum:Pasinler>tr:Pasinler
era: Antik dönem (MÖ 1. binyıl)
meaning: Ermenice Basean ovasının adından; Osmanlı adı Hasankale, Akkoyunlu beyi Hasan'ın kalesinden
story: Aras'ın kaynak ovası Ermeni kaynaklarında Basean adıyla geçer ve Türkçe Pasin biçimine dönüşmüştür. Kasaba Osmanlı döneminde, 15. yüzyılda Akkoyunlu Uzun Hasan'ın onardığı kaleden dolayı Hasankale adını taşıdı; 1930'larda Pasinler oldu. 1048 Pasinler Savaşı Selçukluların Bizans'a karşı ilk büyük zaferidir; kaplıcaları ünlüdür.
source: Ermeni vakayinameleri (olgu); Osmanlı Erzurum eyaleti tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 39.9797,41.6756

@Tuşba|ilçe|Van|Doğu Anadolu||xur
chain: xur:Tušpa>hy:Tosp>cum:Tuşba>tr:Tuşba
era: Urartu dönemi (MÖ 9. yy)
meaning: Urartu Krallığı'nın başkenti Tušpa'nın adından; 2013'te kurulan merkez ilçeye verildi
story: Van Kalesi kayalığına MÖ 9. yüzyılda kurulan Tušpa, Urartu krallarının başkentiydi; kaya mezarları ve çivi yazılı yazıtlar kalededir. Ermenice Tosp biçimiyle yaşayan ad, 2013'te Van'ın merkez ilçelerinden birine Tuşba olarak verildi. Van Gölü Urartu metinlerinde "Tušpa denizi" olarak anılır.
source: Urartu çivi yazılı yazıtları; Ermeni vakayinameleri (olgu); 2013 tarihli idari düzenleme
coords: 38.5000,43.3800

@Akdamar|ada|Van|Doğu Anadolu||hy
chain: hy:Aghtamar>ota:Akdamar>tr:Akdamar
era: Orta Çağ (10. yy)
meaning: Ermenice Aghtamar ada adından; söylencede sevgilisine yüzen gencin "Ah Tamar!" çığlığına bağlanır
story: Van Gölü'ndeki küçük adada Vaspurakan kralı Gagik'in 915–921'de yaptırdığı Kutsal Haç Kilisesi, dış duvarlarındaki kabartmalarla Ermeni sanatının başyapıtıdır. Ad, adada yaşayan Tamar adlı kıza her gece yüzerek giden gencin boğulurken "Ah Tamar!" diye bağırdığı söylencesiyle açıklanır; bu bir halk etimolojisidir. Kilise 2007'de onarılıp müze oldu.
source: Ermeni vakayinameleri (Vaspurakan, olgu); Evliya Çelebi Seyahatnâmesi
coords: 38.3408,43.0369

@Erciş|ilçe|Van|Doğu Anadolu||hy
chain: xur:Arṣaškun>hy:Arčēš>ar:Arjīsh>ota:Erciş>tr:Erciş
era: Urartu dönemi (MÖ 9. yy)
meaning: Ermenice Arčēš kent adından; Urartu dönemindeki Arṣaškun ile ilişkilendirilir
story: Van Gölü'nün kuzey kıyısındaki kent, Ermeni kaynaklarında Arčēš, Arap kaynaklarında Arjīsh olarak geçer; Urartu kralı Arame'nin başkenti Arṣaškun'la ilişkilendirilir. Göl sularının yükselmesiyle eski kent su altında kaldı ve kasaba 19. yüzyılda kuzeye taşındı. Karakoyunlu Hükümdarı Kara Yusuf burada doğdu; Çelebibağı mezarlığı Orta Çağ eseridir.
source: Urartu yazıtları (olgu); Yakut el-Hamevî, Muʿcemü'l-Büldân; Osmanlı Van eyaleti tahrirleri
coords: 39.0283,43.3586

@Van Gölü|göl|Van|Doğu Anadolu||tr
chain: xur:Tušpa Denizi>el:Thōspîtis>ota:Van Deryası>tr:Van Gölü
era: Urartu dönemi (MÖ 9. yy)
meaning: Türkçe göl + Van kentinin adı; Urartuca "Tušpa denizi", Yunanca Thospitis
story: Türkiye'nin en büyük gölü, Urartu metinlerinde başkent Tušpa'nın adıyla anılır; Strabon ve Ptolemaios Thospitis diye yazar. Sodalı suyu nedeniyle Osmanlı belgelerinde "Van Deryası" diye deniz gibi anılan gölde Akdamar Adası ve inci kefali bulunur. Göl sözcüğü Eski Türkçe köl biçimiyle Orhun Yazıtları'nda geçer.
source: Urartu çivi yazılı yazıtları; Strabon, Geographika XI; Evliya Çelebi Seyahatnâmesi
coords: 38.6000,42.9000

@Ağrı Dağı|dağ|Iğdır|Doğu Anadolu||xur
chain: xur:Urarṭu>akk:Ararat>hy:Masis>ota:Ağrı Dağı>tr:Ağrı Dağı
era: Urartu dönemi (MÖ 9. yy)
meaning: Türkiye'nin en yüksek dağı (5137 m); Tevrat'taki Ararat adı Urartu krallığının adından, Ermenice adı Masis
story: Asur yıllıklarında Urarṭu diye geçen krallığın adı, Tevrat'ta Nuh'un gemisinin oturduğu Ararat dağları olarak yaşadı; Ermeniler dağa Masis, Türkler Ağrı Dağı dediler. Marco Polo dağın hiç erimeyen karından söz eder; Evliya Çelebi dağı Van'dan görünüşüyle anlatır. Türkçe ağrı sözcüğünün dağla ilişkisi, "ulu, yüksek" anlamıyla açıklanır; ilk tırmanış 1829'da Parrot tarafından yapıldı.
source: Asur yıllıkları; Tekvin 8 (olgu); Marco Polo Seyahatnâmesi; Evliya Çelebi Seyahatnâmesi
coords: 39.7019,44.2983

@Doğubayazıt|ilçe|Ağrı|Doğu Anadolu||ar
chain: xur:Daroynk>hy:Daroynk>ota:Bâyezîd>cum:Doğubayazıt>tr:Doğubayazıt
era: Osmanlı dönemi (16. yy)
meaning: Celayirli Sultan Ahmed'in oğlu Bayezid'in (ya da Yıldırım Bayezid'in) adından; 1934'te Doğu sözcüğü eklendi
story: Urartu kalesi Daroynk'un yerindeki kasaba, 14. yüzyıl sonunda Celayirli hanedanından Bayezid'in kaleyi onarmasıyla Bayezid adını aldı; Osmanlı belgelerinde Bâyezîd sancağı olarak geçer. Çıldıroğlu İshak Paşa'nın 1784'te tamamlanan sarayı Osmanlı mimarisinin son büyük anıtlarındandır. 1934'te Bursa'daki Yenişehir Bayezid ile karışmaması için Doğubayazıt yapıldı. Bayezid adı Arapça Bāyazīd'dan gelir.
source: Osmanlı Bâyezîd sancağı tahrirleri; İshak Paşa Sarayı kitabesi (olgu); 1934 tarihli ad değişikliği
coords: 39.5469,44.0844

@Malazgirt|ilçe|Muş|Doğu Anadolu||hy
chain: xur:Menua (kral adı)>hy:Manazkert>ar:Manāzjird>sel:Malazgird>tr:Malazgirt
era: Urartu dönemi (MÖ 8. yy)
meaning: Ermenice Manazkert "Manaz'ın kalesi": Urartu kralı Menua'nın kurduğu kaleye bağlanan ad
story: Murat Irmağı'nın kuzeyindeki ova kasabası, Ermeni kaynaklarında Manazkert adıyla geçer ve Urartu kralı Menua'nın adıyla ilişkilendirilir; -kert öğesi Ermenicede "kuran, yapan" anlamındadır. 26 Ağustos 1071'de Sultan Alp Arslan'ın Bizans imparatoru Romanos Diogenes'i yendiği Malazgirt Savaşı Anadolu'nun Türkleşmesinin başlangıcı sayılır. Kalesi ve Ulu Camii kasabada durur.
source: Urartu yazıtları (olgu); Mikhael Attaleiates (Malazgirt Savaşı); Osmanlı Muş sancağı tahrirleri
coords: 39.1436,42.5400

@Ahlat|ilçe|Bitlis|Doğu Anadolu||hy
chain: hy:Khlat>ar:Khilāṭ>sel:Ahlat>ota:Ahlat>tr:Ahlat
era: Erken Orta Çağ (7. yy)
meaning: Ermenice Khlat kent adının Arapça Khilāṭ yoluyla Türkçe söyleyişi; Selçuklu mezar taşlarıyla ünlü kent
story: Van Gölü'nün batı kıyısındaki Ahlat, Ermenice Khlat, Arapça Khilāṭ adlarıyla anılırdı; 12.–13. yüzyılda Ahlatşahlar'ın başkentiydi ve "Kubbetü'l-İslam" diye övülürdü. Selçuklu mezarlığındaki taş işçiliğiyle ünlü mezar taşları ve kümbetleri UNESCO geçici listesindedir. 1071'de Alp Arslan ordusuyla Malazgirt'e buradan yürüdü.
source: Yakut el-Hamevî, Muʿcemü'l-Büldân; Evliya Çelebi Seyahatnâmesi; Ahlat mezar taşı kitabeleri (olgu)
coords: 38.7522,42.4825

@Tatvan|ilçe|Bitlis|Doğu Anadolu||unk
chain: hy:Datvan>ota:Tatvan>tr:Tatvan
era: Osmanlı dönemi (16. yy)
meaning: Kökeni tartışmalı; Ermenice Datvan köy adının ya da Türkçe tat "yabancı" sözcüğüyle "Tatlar yurdu" biçiminin Türkçeleşmesi
story: Van Gölü'nün güneybatı ucundaki kasaba, Osmanlı belgelerinde Tatvan biçiminde geçer; ad Ermenice bir köy adına ya da Eski Türkçede Türk olmayan yerleşikler için kullanılan tat sözcüğüne bağlanır. Nemrut Krater Gölü ve 1971'den beri çalışan feribot limanı kasabanın kimliğidir; Van Gölü ekspresi buradan Van'a feribotla geçer.
source: Osmanlı Bitlis sancağı tahrirleri; Dîvânu Lugâti't-Türk (tat)
coords: 38.5042,42.2817

@Yüksekova|ilçe|Hakkâri|Doğu Anadolu||tr
chain: ku:Gever>ota:Gever>cum:Yüksekova>tr:Yüksekova
era: Cumhuriyet dönemi (1936)
meaning: Türkçe yüksek + ova: 1900 metre rakımlı ovadan; eski adı Kürtçe Gever
story: Cilo ve Sat dağlarının arasındaki yüksek ova kasabası, Kürtçe Gever adıyla biliniyordu; 1936'da ovanın rakımını anlatan Yüksekova adı verildi. Yüksek sözcüğü Eski Türkçe yüksek, ova ise oba sözcüğüyle akrabadır. Nasturi ve Kürt aşiretlerinin yaşadığı ova, Türkiye'nin en soğuk yerlerindendir.
source: Osmanlı Hakkâri sancağı kayıtları; 1936 tarihli idari düzenleme
coords: 37.5736,44.2847

@Harput|semt|Elazığ|Doğu Anadolu||hy
chain: xur:Ḫarputa>hy:Kharberd>ar:Ḥiṣn Ziyād>ota:Harput>tr:Harput
era: Urartu dönemi (MÖ 8. yy)
meaning: Ermenice khar "kaya" + berd "kale": "kaya kale"; Urartu yazıtlarındaki Ḫarputa ile ilişkilendirilir
story: Elazığ'ın üstündeki kayalık tepeye kurulu eski kent, Ermenice "kaya kalesi" anlamındaki Kharberd adını taşır; Arap kaynakları Ḥiṣn Ziyād "Ziyad'ın kalesi" dedi. Artuklu Ulu Camii (1156) ve Süt Kalesi kentin anıtlarıdır. 1862'de yönetim ovaya inince Harput boşaldı; Harput müziği ve "Çayda Çıra" oyunu kültürünü yaşatır.
source: Urartu yazıtları (olgu); Arap coğrafyacıları; Evliya Çelebi Seyahatnâmesi
coords: 38.7047,39.2550

@Arslantepe|antik_kent|Malatya|Doğu Anadolu||tr
chain: hit:Maldiya>akk:Meliddu>ota:Aslan Tepe>tr:Arslantepe
era: Tunç Çağı (MÖ 4. binyıl)
meaning: Türkçe arslan + tepe: höyükte bulunan Geç Hitit aslan heykellerinden; antik adı Melid
story: Malatya'nın yanı başındaki höyük, MÖ 4. binyılda dünyanın en eski saray yapılarından birini barındırıyordu; Geç Hitit krallığı Melid'in kapı aslanları höyüğe Türkçe adını verdi. Arslan sözcüğü Eski Türkçe arslan biçimiyle Orhun Yazıtları'nda geçer ve Macarcaya oroszlán olarak geçmiştir. 2021'de UNESCO Dünya Mirası listesine girdi.
source: Arslantepe kazı yayınları (olgu); Asur yıllıkları; UNESCO kayıtları
coords: 38.3814,38.3611

@Darende|ilçe|Malatya|Doğu Anadolu||hit
chain: hit:Taranta>el:Taránta>ar:Darenda>ota:Darende>tr:Darende
era: Hitit dönemi (MÖ 2. binyıl)
meaning: Hitit metinlerindeki Taranta kent adından; Tohma Çayı vadisindeki kale kenti
story: Tohma Çayı'nın oyduğu vadideki kale kenti, Hitit belgelerindeki Taranta ile özdeşleştirilir; Bizans ve Arap kaynakları aynı adı sürdürdü. Zengibar Kalesi ve Somuncu Baba (Şeyh Hamid-i Veli) külliyesi kasabanın belleğidir; Gürpınar Şelalesi vadinin doğal güzelliğidir.
source: Hitit çivi yazılı belgeleri (olgu); Osmanlı Malatya sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 38.5522,37.5042

@Kemah|ilçe|Erzincan|Doğu Anadolu||hy
chain: hy:Kamakh (Ani-Kamakh)>ar:Kamākh>sel:Kemah>tr:Kemah
era: Antik dönem (MÖ 1. yy)
meaning: Ermenice Kamakh kale adından; Anaitis tapınağının kutsal kenti Ani-Kamakh
story: Fırat'ın dar bir boğazındaki kaya kalesi, Ermeni kaynaklarında Ani-Kamakh adıyla anılır ve Pers tanrıçası Anaitis'in tapınağıyla, Arşaklı krallarının mezarlarıyla ünlüydü. Mengücek Gazi'nin türbesi Selçuklu dönemindendir; Osmanlı belgelerinde Kemah sancağı olarak geçer. Kemah tulum peyniri kasabayla anılır.
source: Strabon, Geographika XI; Ermeni vakayinameleri (olgu); Evliya Çelebi Seyahatnâmesi
coords: 39.6028,39.0353

@Kağızman|ilçe|Kars|Doğu Anadolu||hy
chain: hy:Kaghzvan>ota:Kağızman>tr:Kağızman
era: Orta Çağ (10. yy)
meaning: Ermenice Kaghzvan yer adının Türkçe söyleyişi; Aras vadisindeki tuz madeni kasabası
story: Aras Irmağı'nın güneyindeki kasaba, Ermeni kaynaklarında Kaghzvan adıyla geçer; Türkçede Kağızman olmuştur. Bizans ve Selçuklu dönemlerinden kalma tuz madenleri yüzyıllardır işletilir. Camuşlu'daki kaya resimleri bölgenin tarih öncesi tanığıdır; Kağızman elması yöresel üründür.
source: Ermeni vakayinameleri (olgu); Osmanlı Kars eyaleti tahrirleri
coords: 40.1553,43.1336

@Çıldır Gölü|göl|Ardahan|Doğu Anadolu||ka
chain: ka:Çrdili>ota:Çıldır>tr:Çıldır Gölü
era: Osmanlı dönemi (16. yy)
meaning: Gürcüce kökenli Çıldır bölge adıyla; Osmanlı Çıldır eyaletinin merkezi olan yayla gölü
story: Türkiye'nin en yüksek büyük gölü, Osmanlı döneminde Ahıska merkezli Çıldır eyaletine adını veren bölgededir; bölge adı Gürcüce bir yer adından gelir. 1578 Çıldır Savaşı'nda Lala Mustafa Paşa Safevîleri yendi. Kışın donan göl üstünde atlı kızak ve buz balıkçılığı yapılır; Akçakale adası Orta Çağ kalesi taşır.
source: Osmanlı Çıldır eyaleti kayıtları; Evliya Çelebi Seyahatnâmesi
coords: 41.0500,43.2500

@Palandöken|dağ|Erzurum|Doğu Anadolu||tr
chain: ota:Palandöken>tr:Palandöken
era: Osmanlı dönemi (17. yy)
meaning: Türkçe palan "semer, eyer yastığı" (Farsça pālān) + döken: dikliğinden yük hayvanlarının palanını döken dağ
story: Erzurum'un güneyindeki 3271 metrelik dağın adı, geçitlerinin dikliğinden ötürü yük hayvanlarının semerlerini (palan) düşürmesine bağlanır; palan sözcüğü Farsça pālān'dan gelir. Evliya Çelebi dağın soğuğunu anlatır. 1990'lardan beri kayak merkezi olan dağ, 2011 Üniversite Kış Oyunları'na ev sahipliği yaptı.
source: Evliya Çelebi Seyahatnâmesi; Osmanlı Erzurum eyaleti kayıtları
coords: 39.8167,41.2833

@Fırat|nehir|Elazığ|Doğu Anadolu||akk
chain: sum:Buranun>akk:Purattu>el:Euphrátēs>ar:al-Furāt>tr:Fırat
era: Sümer dönemi (MÖ 3. binyıl)
meaning: Sümerce Buranun / Akadca Purattu "büyük ırmak" adından; Arapça al-Furāt yoluyla Türkçe Fırat
story: Mezopotamya uygarlıklarının yaşam kaynağı olan ırmak, Sümer tabletlerinde Buranun, Akad metinlerinde Purattu adıyla geçer; Yunanca Euphrates bu addan türedi. Araplar al-Furāt dedi ve Türkçe Fırat bu biçimdendir. Karasu ve Murat kollarının Keban'da birleşmesiyle oluşan ırmak, Kur'an ve Tevrat'ta cennet ırmaklarından sayılır; Keban ve Atatürk barajları üzerindedir.
source: Sümer ve Akad çivi yazılı metinler (olgu); Herodotos I; Tekvin 2; Evliya Çelebi Seyahatnâmesi
coords: 38.5000,38.5000

@Dicle|nehir|Diyarbakır|Güneydoğu Anadolu||akk
chain: sum:Idigna>akk:Idiglat>el:Tígris>ar:Dijla>tr:Dicle
era: Sümer dönemi (MÖ 3. binyıl)
meaning: Sümerce Idigna "hızlı akan ırmak" adından; Arapça Dijla yoluyla Türkçe Dicle, Yunanca Tigris "kaplan, ok"
story: Sümerce Idigna, Akadca Idiglat adlı ırmağın adı Eski Farsçada Tigrā "ok" sözcüğüyle yorumlanarak Yunancaya Tigris biçiminde geçti; Arapça Dijla biçimi Türkçede Dicle oldu. Diyarbakır surlarının eteğinden geçen ırmak Hasankeyf'i aşarak Irak'a iner; On Gözlü Köprü (1065) Mervanî eseridir. Ilısu Barajı 2019'da doldu.
source: Sümer ve Akad çivi yazılı metinler (olgu); Strabon, Geographika XI; Evliya Çelebi Seyahatnâmesi
coords: 37.9000,40.2000

@Munzur Dağları|dağ|Tunceli|Doğu Anadolu||unk
chain: ota:Munzur>tr:Munzur Dağları
era: Osmanlı dönemi (16. yy)
meaning: Yöre inanışında kutsal sayılan Munzur Baba'nın adından; kökeni tartışmalı
story: Tunceli'nin kuzeyini kaplayan dağ silsilesi, Alevi inanışında kutsal sayılan Munzur Baba söylencesiyle anılır; çoban Munzur'un kerametleri Dersim ağızlarında yaşar. Adın Zazaca ya da daha eski bir dilden geldiği tartışılır. Munzur Vadisi Millî Parkı, Munzur Çayı'nın kaynağındaki gözelerle ünlüdür.
source: Dersim sözlü geleneği; Osmanlı Dersim sancağı kayıtları (olgu)
coords: 39.4000,39.4000

# ===================================================================== GÜNEYDOĞU ANADOLU
@Midyat|ilçe|Mardin|Güneydoğu Anadolu||syc
chain: akk:Matiate>syc:Midyad>ar:Midyāt>ota:Midyat>tr:Midyat
era: Asur dönemi (MÖ 9. yy)
meaning: Asur yıllıklarındaki Matiate "mağaralar kenti" adından; Süryanice Midyad
story: Tur Abdin yaylasının merkezi Midyat, Asur kralı II. Aşurnasirpal'in yıllıklarında Matiate adıyla geçer; ad "mağaralar" anlamıyla açıklanır ve kentin kaya oyma mahzenlerine uyar. Süryani Ortodoks kiliseleri (Mor Gabriel Manastırı 397'den beri) ve taş konakları kentin kimliğidir; telkâri gümüş işçiliği ünlüdür. Süryanice, Arapça, Kürtçe ve Türkçe bir arada konuşulur.
source: Asur yıllıkları (olgu); Süryani vakayinameleri; Osmanlı Mardin sancağı tahrirleri
coords: 37.4197,41.3453

@Nusaybin|ilçe|Mardin|Güneydoğu Anadolu||akk
chain: akk:Naṣibina>el:Nísibis>la:Nisibis>ar:Naṣībīn>ota:Nusaybin>tr:Nusaybin
era: Asur dönemi (MÖ 9. yy)
meaning: Asur yıllıklarındaki Naṣibina kent adından; Süryani Nusaybin Okulu'nun kenti
story: Asur kaynaklarında Naṣibina olarak geçen kent, Roma-Pers sınırında defalarca kuşatıldı; 363'te Roma'nın Perslere bıraktığı Nisibis, Doğu Kilisesi'nin ünlü teoloji okuluna ev sahipliği yaptı. Mor Yakup Kilisesi (4. yy) ve Zeynel Abidin Camii kentin anıtlarıdır; Arapça Naṣībīn biçimi Türkçede Nusaybin oldu. Karşısında Suriye'nin Kamışlı kenti yer alır.
source: Asur yıllıkları; Ammianus Marcellinus XXV; Süryani kaynakları (Nisibis Okulu, olgu)
coords: 37.0750,41.2156

@Hasankeyf|ilçe|Batman|Güneydoğu Anadolu||ar
chain: syc:Kepha>el:Kiphas>ar:Ḥiṣn Kayfā>ota:Hısn-ı Keyf>tr:Hasankeyf
era: Roma dönemi (4. yy)
meaning: Arapça ḥiṣn "kale" + Süryanice kepha "kaya": "kaya kalesi"
story: Dicle'nin kayalık vadisindeki kent, Süryanice "kaya" anlamındaki Kepha adıyla anılıyordu; Araplar Ḥiṣn Kayfā "kaya kalesi" dedi ve Türkçe Hasankeyf halk söyleyişinde kişi adı Hasan'a benzetildi. Artuklu köprüsü, Eyyubi camileri ve Zeynel Bey Türbesi kentin anıtlarıydı; 2020'de Ilısu Barajı suları eski kenti kapladı, anıtlar yeni yerleşime taşındı.
source: Arap coğrafyacıları (olgu); Evliya Çelebi Seyahatnâmesi; Osmanlı Diyarbekir eyaleti tahrirleri
coords: 37.7142,41.4133

@Harran|ilçe|Şanlıurfa|Güneydoğu Anadolu||akk
chain: akk:Ḫarrānu>syc:Ḥarrān>el:Kárrhai>ar:Ḥarrān>tr:Harran
era: Asur dönemi (MÖ 2. binyıl)
meaning: Akadca ḫarrānu "yol, kervan yolu": kervan yollarının kavşağındaki kent
story: Mezopotamya'nın en eski kentlerinden Harran, adını Akadca "yol" sözcüğünden alır; Hz. İbrahim'in Kenan'a giderken konakladığı kent olarak Tevrat'ta geçer. Ay tanrısı Sin'in tapınağı ve dünyanın ilk üniversitelerinden sayılan Harran medresesi burada kuruldu; Roma komutanı Crassus MÖ 53'te Karrhai'de Partlara yenildi. Kümbet evleri kentin simgesidir.
source: Asur yıllıkları (olgu); Tekvin 11–12; Plutarkhos, Crassus; Evliya Çelebi Seyahatnâmesi
coords: 36.8647,39.0314

@Göbeklitepe|antik_kent|Şanlıurfa|Güneydoğu Anadolu||tr
chain: ota:Göbekli Tepe>tr:Göbeklitepe
era: Neolitik dönem (MÖ 10. binyıl)
meaning: Türkçe göbek + -li + tepe: ortasındaki yuvarlak höyükten "göbekli tepe"
story: Şanlıurfa'nın kuzeydoğusundaki tepe, MÖ 9600'e tarihlenen dünyanın en eski tapınak yapılarını barındırır; T biçimli dikilitaşlar yazının ve tarımın icadından önce yontulmuştur. Türkçe adı tepenin ortasındaki göbek gibi yükselen höyükten gelir; Kürtçe Xirabreşk "kara harabe" adı da kullanılır. 2018'de UNESCO Dünya Mirası oldu.
source: Göbeklitepe kazı yayınları (1995–, olgu); UNESCO kayıtları
coords: 37.2233,38.9225

@Birecik|ilçe|Şanlıurfa|Güneydoğu Anadolu||syc
chain: syc:Birtha>el:Bírtha>ar:al-Bīra>ota:Birecik>tr:Birecik
era: Antik dönem (MÖ 1. yy)
meaning: Aramice birtha "kale, hisar" sözcüğünden; Fırat kıyısındaki kale kenti, Türkçe -cik küçültme ekiyle
story: Fırat'ın batı yakasındaki kale kenti, Aramice "kale" anlamındaki birtha adıyla anılırdı; Arapça al-Bīra biçimine Türkçe -cik eki eklenerek Birecik oldu. Memlük-Osmanlı sınırındaki kale 1516'da Yavuz Sultan Selim'in eline geçti; Fırat üzerindeki köprüsü 1956'da yapıldı. Kelaynak kuşlarının son yuvası buradadır.
source: Arap coğrafyacıları (olgu); Evliya Çelebi Seyahatnâmesi; Osmanlı Urfa sancağı tahrirleri
coords: 37.0256,37.9775

@Halfeti|ilçe|Şanlıurfa|Güneydoğu Anadolu||unk
chain: ar:Kalʿat ar-Rūm (Rumkale)>ota:Halfeti>tr:Halfeti
era: Osmanlı dönemi (16. yy)
meaning: Kökeni tartışmalı; Süryanice ya da Arapça bir yer adının Türkçe söyleyişi, Rumkale'nin karşısındaki kasaba
story: Fırat kıyısındaki kasaba, Ermeni Katolikosluğu'nun 12.–13. yüzyılda merkez edindiği Rumkale'nin (Arapça Kalʿat ar-Rūm) karşısında yer alır; Halfeti adının kökeni kesin olarak bilinmez. 2000'de Birecik Barajı eski kasabayı sular altında bıraktı; "batık şehir" tekne turlarıyla gezilir. Siyah gülü ile tanınır.
source: Osmanlı Urfa sancağı tahrirleri; Ermeni Katolikosluk kayıtları (Rumkale, olgu)
coords: 37.2472,37.8686

@Suruç|ilçe|Şanlıurfa|Güneydoğu Anadolu||syc
chain: syc:Sarug>el:Bátnai>ar:Sarūj>ota:Suruç>tr:Suruç
era: Antik dönem (MÖ 1. binyıl)
meaning: Süryanice Sarug bölge adından; Süryani şairi Yakup'un (Mor Yakup Sarugli) yurdu
story: Urfa'nın güneybatısındaki ova, Süryanice Sarug adıyla anılır ve 6. yüzyıl Süryani şair-piskoposu Suruçlu Yakup'un adıyla kilise edebiyatında yaşar; Roma döneminde Batnai, Arap döneminde Sarūj dendi. Osmanlı'da Urfa sancağının kazası olan kasaba, Suriye sınırındaki Kobani'nin karşısındadır.
source: Süryani kilise kaynakları (olgu); Arap coğrafyacıları; Osmanlı Urfa sancağı tahrirleri
coords: 36.9761,38.4250

@Viranşehir|ilçe|Şanlıurfa|Güneydoğu Anadolu||fa
chain: syc:Tella>el:Konstantína>ota:Viranşehir>tr:Viranşehir
era: Osmanlı dönemi (17. yy)
meaning: Farsça vīrān "yıkık" + şahr "şehir": antik Konstantina'nın yıkıntıları üstündeki "yıkık şehir"
story: Süryanilerin Tella dediği kent, Bizans döneminde Konstantina adını taşıyordu ve 6. yüzyılda Pers savaşlarında yıkıldı. Osmanlı'da yıkıntılarıyla "viran şehir" diye anılan yer, 19. yüzyılda Milli aşiretinin yerleşmesiyle yeniden kasaba oldu; her iki öğe de Farsçadır. Sekizgen Bizans kilisesinin kalıntıları kasabanın ortasındadır.
source: Prokopios, Yapılar Üzerine (Konstantina); Osmanlı Urfa sancağı tahrirleri
coords: 37.2306,39.7625

@Ceylanpınar|ilçe|Şanlıurfa|Güneydoğu Anadolu||tr
chain: syc:Rēš ʿAynā>ar:Raʾs al-ʿAyn>ota:Resülayn>cum:Ceylanpınar>tr:Ceylanpınar
era: Cumhuriyet dönemi (1927)
meaning: Türkçe ceylan (Farsça) + pınar: yörede yaşayan ceylanlardan; eski adı Arapça Raʾs al-ʿAyn "pınar başı"
story: Habur Çayı'nın kaynak pınarlarındaki antik kent, Süryanice ve Arapça "pınar başı" anlamına gelen Rēš ʿAynā / Raʾs al-ʿAyn adıyla anılırdı. 1920'lerde sınır bölündüğünde Türkiye'de kalan kesime, yöredeki ceylan sürülerinden esinle Ceylanpınar adı verildi; ceylan sözcüğü Farsça cerān'dan gelir. Devlet üretme çiftliği Türkiye'nin en büyük tarım işletmesidir.
source: Arap coğrafyacıları (olgu); 1927 tarihli idari düzenleme
coords: 36.8464,40.0481

@Siverek|ilçe|Şanlıurfa|Güneydoğu Anadolu||hy
chain: hy:Sevaverak>ar:Suwaydāʾ>ota:Siverek>tr:Siverek
era: Orta Çağ (10. yy)
meaning: Ermenice sev "kara" + averak "harabe": "kara harabe"; kasabanın bazalt kalesinden
story: Karacadağ volkanının eteğindeki kasaba, Ermenice "kara harabe" anlamındaki Sevaverak adını bazalt taşlı kalesinden alır; Arapça Suwaydāʾ "karaca" da aynı rengi anlatır. Osmanlı'da Diyarbekir eyaletine bağlı olan kasaba, Türkçede Siverek oldu. Kalesi ve Çarşı Camii tarihî yapılarıdır.
source: Ermeni vakayinameleri (olgu); Osmanlı Diyarbekir eyaleti tahrirleri
coords: 37.7506,39.3169

@Silvan|ilçe|Diyarbakır|Güneydoğu Anadolu||unk
chain: hy:Nprkert>el:Martyroúpolis>ar:Mayyāfāriqīn>ota:Silvan>tr:Silvan
era: Roma dönemi (5. yy)
meaning: Silvan adının kökeni tartışmalıdır; eski adları Ermenice Nprkert, Yunanca Martyropolis "şehitler kenti", Arapça Meyyafarikin
story: Diyarbakır'ın doğusundaki kent, 5. yüzyılda piskopos Maruthas'ın Pers şehitlerinin kemiklerini getirmesiyle Martyropolis "şehitler kenti" adını aldı; Araplar Mayyāfāriqīn dedi. Mervanî ve Artuklu dönemlerinde başkentlik yaptı; Selahaddin Eyyubî'nin Malabadi Köprüsü yakındadır. Türkçe Silvan adının kökeni kesin olarak bilinmez.
source: Prokopios; Arap coğrafyacıları (olgu); Evliya Çelebi Seyahatnâmesi
coords: 38.1403,41.0078

@Ergani|ilçe|Diyarbakır|Güneydoğu Anadolu||hy
chain: hy:Arkni>ar:Arghana>ota:Ergani>tr:Ergani
era: Orta Çağ (10. yy)
meaning: Ermenice Arkni yer adının Arapça Arghana yoluyla Türkçe söyleyişi; bakır madeniyle ünlü kasaba
story: Dicle'nin kaynak bölgesindeki kasaba, Ermeni kaynaklarında Arkni, Osmanlı belgelerinde Ergani Madeni adıyla geçer; bakır yatakları Tunç Çağı'ndan beri işletilir. Hilar mağaraları ve Çayönü Neolitik yerleşimi (MÖ 7000) ilçe sınırlarındadır; Zülküf Dağı Hz. Zülkifl'in makamı sayılır.
source: Osmanlı Ergani Madeni sancağı kayıtları (olgu); Çayönü kazı yayınları
coords: 38.2667,39.7667

@Çermik|ilçe|Diyarbakır|Güneydoğu Anadolu||hy
chain: hy:Jermuk>ota:Çermik>tr:Çermik
era: Osmanlı dönemi (16. yy)
meaning: Ermenice jermuk "sıcak su, ılıca": kasabanın kaplıcalarından
story: Diyarbakır'ın batısındaki kasaba, kaplıcalarıyla ünlüdür ve adı Ermenice "sıcak su kaynağı" anlamındaki jermuk sözcüğünden gelir; Ermenistan'daki Jermuk kaplıcası aynı adı taşır. Osmanlı belgelerinde Çermik yazılan kasabanın Haburman Köprüsü Artuklu eseridir (1179).
source: Osmanlı Diyarbekir eyaleti tahrirleri; Haburman Köprüsü kitabesi (olgu)
coords: 38.1364,39.4486

@Dülük|antik_kent|Gaziantep|Güneydoğu Anadolu||hit
chain: hit:Tulukha>el:Dolíchē>la:Doliche>ar:Dulūk>tr:Dülük
era: Hitit dönemi (MÖ 2. binyıl)
meaning: Hitit belgelerindeki Tulukha kentinin adından; Roma'da Iuppiter Dolichenus kültünün merkezi Doliche
story: Gaziantep'in kuzeyindeki tepe, Hitit metinlerinde Tulukha olarak geçer; Roma döneminde fırtına tanrısı Iuppiter Dolichenus'un kültü buradan bütün imparatorluğa yayıldı. Arap kaynakları Dulūk dedi; Türkçe Dülük bu biçimdendir. Mithras tapınağı ve Paleolitik taş aletleri Anadolu'nun en eski yerleşim izlerindendir.
source: Hitit çivi yazılı belgeleri (olgu); Dolichenus yazıtları; Arap coğrafyacıları
coords: 37.1489,37.3694

@Zeugma|antik_kent|Gaziantep|Güneydoğu Anadolu||el
chain: el:Seleúkeia (Euphrátou)>el:Zeûgma>la:Zeugma>ota:Belkıs>tr:Zeugma
era: Helenistik dönem (MÖ 3. yy)
meaning: Yunanca zeûgma "köprü, boyunduruk": Fırat üzerindeki duba köprüsünden
story: Seleukos I'in Fırat'ın iki yakasına kurduğu kentler, ırmağı aşan duba köprüsünden dolayı Zeugma "köprü" adıyla anıldı; Roma lejyonunun üssü olan kent mozaikleriyle ünlüdür. Osmanlı köyü Belkıs'ın adı halk anlatısında Saba melikesine bağlanır. 2000'de Birecik Barajı kentin bir bölümünü kapladı; Çingene Kızı mozaiği müzededir.
source: Strabon, Geographika XVI; Plinius, Naturalis Historia V; Zeugma kazı yayınları (olgu)
coords: 37.0583,37.8719

@Islahiye|ilçe|Gaziantep|Güneydoğu Anadolu||ar
chain: ota:Fırka-i Islâhiye>ota:Islahiye>tr:Islahiye
era: Osmanlı dönemi (1866)
meaning: Arapça iṣlāḥ "düzeltme, ıslah" + -iyye: aşiretleri iskân eden Fırka-i Islahiye harekâtının adından
story: 1865–1866'da Çukurova ve Amanos'taki göçebe aşiretleri yerleşik düzene geçiren Fırka-i Islahiye ordusunun karargâhı olarak kurulan kasaba, harekâtın adını aldı; aynı harekâtla Osmaniye de kuruldu. Zincirli höyüğündeki Geç Hitit krallığı Samal'ın kalıntıları ve Yesemek heykel atölyesi ilçe sınırlarındadır.
source: Fırka-i Islahiye raporları (olgu); Osmanlı Halep eyaleti kayıtları
coords: 37.0272,36.6336

@Tillo|ilçe|Siirt|Güneydoğu Anadolu||syc
chain: syc:Tillo>ar:Tillū>ota:Tillo>cum:Aydınlar>tr:Tillo
era: Osmanlı dönemi (17. yy)
meaning: Süryanice "yüksek tepe" anlamıyla açıklanan yer adı; 1960'ta Aydınlar oldu, 2013'te Tillo adı geri verildi
story: Siirt'in doğusundaki tepe kasabası, Süryanice "yüksek yer" anlamına gelen bir adla anılır; 18. yüzyılda İsmail Fakirullah ve öğrencisi İbrahim Hakkı Erzurumî'nin ilim merkezi oldu. Türbede gün doğumunda ışığın kabre düşmesini sağlayan ışık düzeneği astronomi bilgisini gösterir. 1960'ta kasabaya Aydınlar adı verildi; 2013'te eski adına döndü.
source: Mârifetnâme (İbrahim Hakkı Erzurumî, 1757); 2013 tarihli ad değişikliği kararı
coords: 37.9447,42.0128

@Cizre|ilçe|Şırnak|Güneydoğu Anadolu||ar
chain: ar:Jazīrat Ibn ʿUmar>ota:Cezîre>tr:Cizre
era: Erken İslam dönemi (9. yy)
meaning: Arapça jazīra "ada": Dicle'nin bir kıvrımıyla ada gibi çevrelenen kent, "İbn Ömer'in adası"
story: Dicle'nin bir kıvrımında kurulan kent, Arapça "ada" anlamındaki jazīra sözcüğüyle Jazīrat Ibn ʿUmar diye anılırdı; Türkçede Cizre oldu. Cizre beyleri, Kürt edebiyatının klasik şairi Ehmedê Xanî ve İsmail Ebul İz el-Cezerî (12. yüzyıl mühendisi) bu kentle anılır; Kırmızı Medrese ve Ulu Cami tarihî yapılarıdır.
source: Arap coğrafyacıları (olgu); el-Cezerî, Kitâbü'l-Hiyel; Evliya Çelebi Seyahatnâmesi
coords: 37.3250,42.1878

@Cudi Dağı|dağ|Şırnak|Güneydoğu Anadolu||ar
chain: syc:Qardū>ar:al-Jūdī>ota:Cûdî>tr:Cudi Dağı
era: Erken İslam dönemi (7. yy)
meaning: Arapça al-Jūdī: Kur'an'da Nuh'un gemisinin oturduğu bildirilen dağ; Süryani geleneğinde Qardu
story: Kur'an'da (Hûd suresi) Nuh'un gemisinin oturduğu yer olarak anılan Cûdî, Süryani ve Yahudi geleneğinde Qardu dağlarıyla özdeşleştirilir; Hristiyan ve Müslüman kaynaklarda dağın tepesindeki "gemi yeri" ziyaret edilmiştir. Türkçe adı Arapça biçimden gelir; 2114 metrelik dağ Şırnak'ın güneyinde Irak sınırına bakar.
source: Kur'an, Hûd 44 (olgu); Süryani kaynakları (Qardu); Evliya Çelebi Seyahatnâmesi
coords: 37.3667,42.4000

@Sason|ilçe|Batman|Güneydoğu Anadolu||hy
chain: hy:Sasun>ota:Sason>tr:Sason
era: Orta Çağ (9. yy)
meaning: Ermenice Sasun bölge adından; "Sasunlu Davit" destanının geçtiği dağlık yöre
story: Batman'ın kuzeyindeki dağlık bölge, Ermeni halk destanı "Sasunlu Davit"in anlatıldığı Sasun yöresidir; ad Orta Çağ Ermeni kaynaklarında geçer. Osmanlı belgelerinde Sason yazılan kasaba, 19. yüzyılda özerk aşiretlerle tanınır. Kozluk'un (Hazzo) kalesi ve yaylaları bölgenin doğal mirasıdır.
source: Ermeni halk destanı Sasna Dzrer (olgu); Osmanlı Bitlis vilayeti salnameleri
coords: 38.3286,41.4192

@Dara|antik_kent|Mardin|Güneydoğu Anadolu||syc
chain: syc:Dara>el:Anastasioúpolis>ar:Dārā>ota:Dara>tr:Dara
era: Bizans dönemi (505)
meaning: Pers kralı Dareios'un adıyla ilişkilendirilen köy adı; İmparator Anastasios'un kurduğu sınır kalesi Anastasiopolis
story: Mardin'in güneydoğusundaki köy, 505'te İmparator Anastasios'un Perslere karşı kurduğu Anastasiopolis sınır kalesinin yerindedir; Prokopios kentin su sarnıçlarını ve surlarını anlatır. Köyün adı, söylenceye göre Dareios'un buradaki savaşından gelir. Kaya oyma nekropol ve dev sarnıç kalıntıları görülebilir.
source: Prokopios, Savaşlar Üzerine I; Süryani vakayinameleri (olgu)
coords: 37.1797,40.9489

@Kızıltepe|ilçe|Mardin|Güneydoğu Anadolu||tr
chain: ar:Dunaysir>ota:Koçhisar>cum:Kızıltepe>tr:Kızıltepe
era: Cumhuriyet dönemi (1930'lar)
meaning: Türkçe kızıl + tepe: kasabanın yanındaki kızıl renkli tepeden; eski adları Arapça Dunaysir, Osmanlı Koçhisar
story: Mardin'in güneyindeki ova kasabası, Artuklu döneminde Dunaysir adıyla bir ticaret merkeziydi ve Ulu Camii (1204) bu dönemin eseridir; Osmanlı belgelerinde Koçhisar diye geçer. 1930'larda kasabaya yanındaki kızıl topraklı tepeden dolayı Kızıltepe adı verildi. Tahıl ambarı olan ova "Mezopotamya'nın buğday tarlası" diye anılır.
source: Artuklu kitabeleri (Dunaysir Ulu Camii, olgu); Osmanlı Mardin sancağı tahrirleri
coords: 37.1931,40.5861

@Nemrut Dağı|dağ|Adıyaman|Güneydoğu Anadolu||ar
chain: he:Nimrōd>ar:Namrūd>ota:Nemrud Dağı>tr:Nemrut Dağı
era: Osmanlı dönemi (17. yy)
meaning: Arapça Namrūd (İbranice Nimrod): halk inanışında dağa adını veren efsanevi kral; Kommagene kralı Antiokhos'un anıt mezarı
story: Kommagene kralı I. Antiokhos'un MÖ 1. yüzyılda yaptırdığı dev heykelli tümülüs, halk arasında İbrahim'i ateşe atan efsanevi kral Nemrut'a bağlanmış ve dağ onun adıyla anılmıştır; bu bir halk etimolojisidir. Nemrut adı Arapçaya İbraniceden geçmiştir. Dağın 2150 metrelik zirvesindeki heykeller 1881'de yeniden keşfedildi; 1987'de UNESCO Dünya Mirası oldu.
source: Kommagene yazıtları (olgu); Tekvin 10 (Nimrod); Evliya Çelebi Seyahatnâmesi; UNESCO kayıtları
coords: 37.9806,38.7406

@Kâhta|ilçe|Adıyaman|Güneydoğu Anadolu||unk
chain: ota:Kâhta>tr:Kâhta
era: Osmanlı dönemi (16. yy)
meaning: Kökeni tartışmalı; Kommagene dönemi kalesinin eteğindeki kasaba, Yeni Kale'nin adıyla anılır
story: Nemrut Dağı'na çıkış noktası olan kasaba, Osmanlı belgelerinde Kâhta adıyla geçer; adın kökeni kesin olarak bilinmez ve yerel bir dile ait olduğu düşünülür. Kommagene krallarının Arsameia yazlık sarayı, Karakuş Tümülüsü ve Roma'nın Cendere Köprüsü ilçe sınırlarındadır; Memlük dönemi Yeni Kale vadiye hâkimdir.
source: Kommagene yazıtları (Arsameia, olgu); Osmanlı Malatya sancağı tahrirleri
coords: 37.7861,38.6222

@Besni|ilçe|Adıyaman|Güneydoğu Anadolu||hy
chain: hy:Behesni>ar:Bahasnā>ota:Behisni>tr:Besni
era: Orta Çağ (11. yy)
meaning: Ermenice Behesni kale adının Arapça Bahasnā yoluyla Türkçe söyleyişi
story: Kilikya Ermeni Krallığı ile Memlükler arasında el değiştiren Behesni kalesi, Haçlı ve Arap kaynaklarında geçer; Osmanlı belgelerinde Behisni yazılır ve Türkçede Besni oldu. Eski kasaba 1950'lerde kayalık yamaçtan ovaya taşındı; kuru üzümü ve pekmeziyle bilinir.
source: Haçlı kronikleri (olgu); Osmanlı Malatya sancağı tahrirleri; Evliya Çelebi Seyahatnâmesi
coords: 37.6925,37.8614

@Samsat|ilçe|Adıyaman|Güneydoğu Anadolu||el
chain: hit:Kummuḫ>el:Samósata>la:Samosata>ar:Sumaysāṭ>ota:Samsat>tr:Samsat
era: Helenistik dönem (MÖ 2. yy)
meaning: Kommagene kralı Samos'un adından Samosata "Samos'un kenti"; hicivci Lukianos'un doğum yeri
story: Fırat kıyısındaki Kommagene başkenti, Orontes hanedanından kral Samos'un adıyla Samosata diye anıldı; Nemrut Dağı anıtını yaptıran Antiokhos'un sarayı buradaydı ve Lukianos burada doğdu. Geç Hitit Kummuh krallığının merkezi de aynı yerdeydi. Eski Samsat 1989'da Atatürk Barajı sularının altında kaldı; kasaba yeni yerine taşındı.
source: Strabon, Geographika XVI; Lukianos (olgu); Osmanlı Malatya sancağı tahrirleri
coords: 37.5811,38.4797

@Nizip|ilçe|Gaziantep|Güneydoğu Anadolu||unk
chain: syc:Nṣībīn (?)>ar:Nazīb>ota:Nizib>tr:Nizip
era: Osmanlı dönemi (16. yy)
meaning: Kökeni tartışmalı; Süryanice ya da Arapça bir yer adının Türkçeleşmiş biçimi, 1839 Nizip Savaşı'nın yeri
story: Fırat'ın batısındaki kasaba Osmanlı belgelerinde Nizib adıyla geçer; adın Süryanice bir köy adından geldiği düşünülür. 1839'da Mısır valisi Mehmed Ali Paşa'nın oğlu İbrahim Paşa'nın Osmanlı ordusunu yendiği Nizip Savaşı burada yapıldı; genç Moltke Osmanlı tarafındaki danışmanlardandı. Zeugma antik kenti ilçe sınırlarındadır; zeytinyağı ve fıstık ekonomisidir.
source: Osmanlı Halep eyaleti tahrirleri; Nizip Savaşı raporları (Moltke'nin mektupları, olgu)
coords: 37.0097,37.7950
"""
