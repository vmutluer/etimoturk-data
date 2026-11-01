# -*- coding: utf-8 -*-
"""Korpus 15 — Ortak sözcükler III: Türk dünyası ses denklikleri (sayılar, renkler, beden, doğa, akrabalık),
Balkan ve Macar Türkizmleri, Osmanlı yönetim/askerlik terimlerinin Avrupa'ya yayılışı ve yalancı arkadaşlar.

DSL: @lemma yön  /  kod biçim [okunuş] ; anlam ; ff:not
"""

COGNATES = r"""@göz shared_ancestor
  az göz ; göz
  kk көз [köz] ; göz
  uz koʻz ; göz
  ky көз [köz] ; göz
  tk göz ; göz
@su shared_ancestor
  az su ; su
  kk су [su] ; su
  uz suv ; su
  ky суу [suu] ; su
  tk suw ; su
@at shared_ancestor
  az at ; at
  kk ат [at] ; at
  uz ot ; at
  ky ат [at] ; at
  tk at ; at
  mn адуу [aduu] ; at sürüsü
@taş shared_ancestor
  az daş ; taş
  kk тас [tas] ; taş
  uz tosh ; taş
  ky таш [taş] ; taş
  tk daş ; taş
@dağ shared_ancestor
  az dağ ; dağ
  kk тау [taw] ; dağ
  uz togʻ ; dağ
  ky тоо [too] ; dağ
  tk dag ; dağ
@yol shared_ancestor
  az yol ; yol
  kk жол [jol] ; yol
  uz yoʻl ; yol
  ky жол [jol] ; yol
  tk ýol ; yol
@yıl shared_ancestor
  az il ; yıl
  kk жыл [jıl] ; yıl
  uz yil ; yıl
  ky жыл [jıl] ; yıl
  tk ýyl ; yıl
@kuş shared_ancestor
  az quş ; kuş
  kk құс [qus] ; kuş
  uz qush ; kuş
  ky куш [kuş] ; kuş
  tk guş ; kuş
@balık shared_ancestor
  az balıq ; balık
  kk балық [balıq] ; balık
  uz baliq ; balık
  ky балык [balık] ; balık
  tk balyk ; balık
  ru Балык [balık] ; tuzlanmış kurutulmuş balık sırtı ; ff:Rusçada balık yalnızca "tuzlanmış balık filetosu" demektir; genel balık için рыба kullanılır
@et shared_ancestor
  az ət ; et
  kk ет [et] ; et
  uz et ; et
  ky эт [et] ; et
  tk et ; et
@süt shared_ancestor
  az süd ; süt
  kk сүт [süt] ; süt
  uz sut ; süt
  ky сүт [süt] ; süt
  tk süýt ; süt
@bal shared_ancestor
  az bal ; bal
  kk бал [bal] ; bal
  ky бал [bal] ; bal
  tk bal ; bal
  uz bol ; bal (eski); asal yaygındır
@tuz shared_ancestor
  az duz ; tuz
  kk тұз [tuz] ; tuz
  uz tuz ; tuz
  ky туз [tuz] ; tuz
  tk duz ; tuz
@un shared_ancestor
  az un ; un
  kk ұн [un] ; un
  uz un ; un
  ky ун [un] ; un
  tk un ; un
@ot shared_ancestor
  az ot ; ot
  kk от [ot] ; ateş ; ff:Kazakçada ot "ateş" demektir (Türkçe od); ot için шөп kullanılır
  uz oʻt ; ateş; ot ; ff:Özbekçede oʻt hem "ateş" hem "ot" anlamına gelir
  ky от [ot] ; ateş ; ff:Kırgızcada от "ateş"; ot için чөп kullanılır
  tk ot ; ot; ateş
@diş shared_ancestor
  az diş ; diş
  kk тіс [tis] ; diş
  uz tish ; diş
  ky тиш [tiş] ; diş
  tk diş ; diş
@kol shared_ancestor
  az qol ; kol
  kk қол [qol] ; el; kol
  uz qoʻl ; el; kol
  ky кол [kol] ; el; kol
  tk gol ; kol
@ayak shared_ancestor
  az ayaq ; ayak
  kk аяқ [ayaq] ; ayak
  uz oyoq ; ayak
  ky аяк [ayak] ; ayak; son ; ff:Kırgızcada аяк aynı zamanda "son, bitiş" demektir
  tk aýak ; ayak
@kan shared_ancestor
  az qan ; kan
  kk қан [qan] ; kan
  uz qon ; kan
  ky кан [kan] ; kan
  tk gan ; kan
@yürek shared_ancestor
  az ürək ; yürek
  kk жүрек [jürek] ; yürek
  uz yurak ; yürek
  ky жүрөк [jürök] ; yürek
  tk ýürek ; yürek
@kulak shared_ancestor
  az qulaq ; kulak
  kk құлақ [qulaq] ; kulak
  uz quloq ; kulak
  ky кулак [kulak] ; kulak
  tk gulak ; kulak
  ru кулак [kulak] ; yumruk; zengin köylü ; ff:Rusça кулак "yumruk" demektir; Türkçe kulak ile ses benzerliği rastlantıdır
@burun shared_ancestor
  az burun ; burun
  kk мұрын [murın] ; burun
  uz burun ; burun
  ky мурун [murun] ; burun
  tk burun ; burun
@ağız shared_ancestor
  az ağız ; ağız
  kk ауыз [awız] ; ağız
  uz ogʻiz ; ağız
  ky ооз [ooz] ; ağız
  tk agyz ; ağız
@bir shared_ancestor
  az bir ; bir
  kk бір [bir] ; bir
  uz bir ; bir
  ky бир [bir] ; bir
  tk bir ; bir
@iki shared_ancestor
  az iki ; iki
  kk екі [eki] ; iki
  uz ikki ; iki
  ky эки [eki] ; iki
  tk iki ; iki
@üç shared_ancestor
  az üç ; üç
  kk үш [üş] ; üç
  uz uch ; üç
  ky үч [üç] ; üç
  tk üç ; üç
@dört shared_ancestor
  az dörd ; dört
  kk төрт [tört] ; dört
  uz toʻrt ; dört
  ky төрт [tört] ; dört
  tk dört ; dört
@beş shared_ancestor
  az beş ; beş
  kk бес [bes] ; beş
  uz besh ; beş
  ky беш [beş] ; beş
  tk bäş ; beş
@altı shared_ancestor
  az altı ; altı
  kk алты [altı] ; altı
  uz olti ; altı
  ky алты [altı] ; altı
  tk alty ; altı
@yedi shared_ancestor
  az yeddi ; yedi
  kk жеті [jeti] ; yedi
  uz yetti ; yedi
  ky жети [jeti] ; yedi
  tk ýedi ; yedi
@sekiz shared_ancestor
  az səkkiz ; sekiz
  kk сегіз [segiz] ; sekiz
  uz sakkiz ; sekiz
  ky сегиз [segiz] ; sekiz
  tk sekiz ; sekiz
@dokuz shared_ancestor
  az doqquz ; dokuz
  kk тоғыз [toğız] ; dokuz
  uz toʻqqiz ; dokuz
  ky тогуз [toguz] ; dokuz
  tk dokuz ; dokuz
@on shared_ancestor
  az on ; on
  kk он [on] ; on
  uz oʻn ; on
  ky он [on] ; on
  tk on ; on
@yüz shared_ancestor
  az yüz ; yüz; çehre
  kk жүз [jüz] ; yüz; çehre
  uz yuz ; yüz; çehre
  ky жүз [jüz] ; yüz
  tk ýüz ; yüz
@bin shared_ancestor
  az min ; bin
  kk мың [mıñ] ; bin
  uz ming ; bin
  ky миң [miñ] ; bin
  tk müň ; bin
@kara shared_ancestor
  az qara ; kara
  kk қара [qara] ; kara
  uz qora ; kara
  ky кара [kara] ; kara
  tk gara ; kara
  ru Кара- [kara] ; yer adlarında (Karaganda, Karakum)
@kızıl shared_ancestor
  az qızıl ; altın ; ff:Azerbaycan Türkçesinde qızıl "altın" demektir; kırmızı için qırmızı kullanılır
  kk қызыл [qızıl] ; kızıl
  uz qizil ; kızıl
  ky кызыл [kızıl] ; kızıl
  tk gyzyl ; kızıl
  ru Кызыл [kızıl] ; Tuva'nın başkenti
@boz shared_ancestor
  az boz ; boz
  kk боз [boz] ; boz
  uz boʻz ; boz
  ky боз [boz] ; boz
  tk boz ; boz
@gök shared_ancestor
  az göy ; gök; mavi
  kk көк [kök] ; gök; mavi; yeşil
  uz koʻk ; mavi; yeşil
  ky көк [kök] ; mavi; yeşil
  tk gök ; gök; mavi
  hu kék ; mavi ; ff:Macarca kék (mavi) Eski Türkçe kök'ten alınmıştır
@ana shared_ancestor
  az ana ; anne
  kk ана [ana] ; anne
  uz ona ; anne
  ky эне [ene] ; anne
  tk ene ; anne
  hu anya ; anne
@ata shared_ancestor
  az ata ; baba
  kk ата [ata] ; dede
  uz ota ; baba
  ky ата [ata] ; baba
  tk ata ; baba
  hu atya ; baba (eski, dinî)
@kardeş shared_ancestor
  az qardaş ; kardeş
  kk қарындас [qarındas] ; kız kardeş ; ff:Kazakçada qarındas yalnızca "kız kardeş" demektir
  uz qarindosh ; akraba ; ff:Özbekçede qarindosh "akraba" anlamına kaymıştır
  ky карындаш [karındaş] ; kız kardeş
  tk gardaş ; kardeş
@oğul shared_ancestor
  az oğul ; oğul
  kk ұл [ul] ; oğul
  uz oʻgʻil ; oğul
  ky уул [uul] ; oğul
  tk ogul ; oğul
@gelin shared_ancestor
  az gəlin ; gelin
  kk келін [kelin] ; gelin
  uz kelin ; gelin
  ky келин [kelin] ; gelin
  tk gelin ; gelin
@ev shared_ancestor
  az ev ; ev
  kk үй [üy] ; ev
  uz uy ; ev
  ky үй [üy] ; ev
  tk öý ; ev
@kapı from_turkish
  hu kapu ; kapı
  sr капија [kapija] ; büyük bahçe kapısı
  bg капия [kapiya] ; kapı
  mk капија [kapija] ; kapı
@elma shared_ancestor
  az alma ; elma
  kk алма [alma] ; elma
  uz olma ; elma
  ky алма [alma] ; elma
  tk alma ; elma
  hu alma ; elma
  mn алим [alim] ; elma
@arpa shared_ancestor
  az arpa ; arpa
  kk арпа [arpa] ; arpa
  uz arpa ; arpa
  ky арпа [arpa] ; arpa
  tk arpa ; arpa
  hu árpa ; arpa
  mn арвай [arvay] ; arpa
@buğday shared_ancestor
  az buğda ; buğday
  kk бидай [biday] ; buğday
  uz bugʻdoy ; buğday
  ky буудай [buuday] ; buğday
  tk bugdaý ; buğday
  hu búza ; buğday
@keçi from_turkish
  hu kecske ; keçi
  az keçi ; keçi
  kk ешкі [eşki] ; keçi
  uz echki ; keçi
  ky эчки [eçki] ; keçi
  tk geçi ; keçi
@öküz shared_ancestor
  az öküz ; öküz
  kk өгіз [ögiz] ; öküz
  uz hoʻkiz ; öküz
  ky өгүз [ögüz] ; öküz
  tk öküz ; öküz
  hu ökör ; öküz
@tavuk shared_ancestor
  az toyuq ; tavuk
  kk тауық [tawıq] ; tavuk
  uz tovuq ; tavuk
  ky тоок [took] ; tavuk
  tk towuk ; tavuk
  hu tyúk ; tavuk
@deniz from_turkish
  hu tenger ; deniz
  az dəniz ; deniz
  kk теңіз [teñiz] ; deniz
  uz dengiz ; deniz
  ky деңиз [deñiz] ; deniz
  tk deňiz ; deniz
@boğa shared_ancestor
  az buğa ; boğa
  kk бұқа [buqa] ; boğa
  uz buqa ; boğa
  ky бука [buka] ; boğa
  tk buga ; boğa
  hu bika ; boğa
@yüzük shared_ancestor
  az üzük ; yüzük
  kk жүзік [jüzik] ; yüzük
  uz uzuk ; yüzük
  ky жүзүк [jüzük] ; yüzük
  tk ýüzük ; yüzük
  hu gyűrű ; yüzük
@yemiş shared_ancestor
  az yemiş ; kavun ; ff:Azerbaycan Türkçesinde yemiş "kavun" demektir
  kk жеміс [jemis] ; meyve
  uz yemish ; yiyecek; meyve
  tk ýemiş ; meyve
  hu gyümölcs ; meyve
@sayı shared_ancestor
  az say ; sayı
  kk сан [san] ; sayı
  uz son ; sayı
  ky сан [san] ; sayı
  tk san ; sayı
  hu szám ; sayı
@çadır from_turkish
  hu sátor ; çadır
  sr чадор [čador] ; çadır ; ff:Sırpçada čador "çadır", Makedonca ve Bulgarcada "şemsiye" anlamına kaymıştır
  bg чадър [çadır] ; şemsiye ; ff:Bulgarcada чадър "şemsiye" demektir
  mk чадор [čador] ; şemsiye ; ff:Makedoncada чадор "şemsiye" anlamındadır
  sq çadër ; çadır; şemsiye
  ro ciadâr ; çadır (eski)
  ru шатёр [şatyor] ; büyük çadır
@kuyu shared_ancestor
  az quyu ; kuyu
  kk құдық [qudıq] ; kuyu
  uz quduq ; kuyu
  ky кудук [kuduk] ; kuyu
  tk guýy ; kuyu
  hu kút ; kuyu
@deve shared_ancestor
  az dəvə ; deve
  kk түйе [tüye] ; deve
  uz tuya ; deve
  ky төө [töö] ; deve
  tk düýe ; deve
  hu teve ; deve
  mn тэмээ [temee] ; deve
@sakal shared_ancestor
  az saqqal ; sakal
  kk сақал [saqal] ; sakal
  uz soqol ; sakal
  ky сакал [sakal] ; sakal
  tk sakgal ; sakal
  hu szakáll ; sakal
@süpürge from_turkish
  hu seprű ; süpürge
  az süpürgə ; süpürge
  kk сыпырғы [sıpırğı] ; süpürge
  uz supurgi ; süpürge
  ky шыпыргы [şıpırgı] ; süpürge
@bilge from_turkish
  hu bölcs ; bilge, akıllı
  az bilgə ; bilge
  kk білгір [bilgir] ; bilgili
  uz bilga ; bilge
@töre from_turkish
  hu törvény ; yasa, kanun
  az törə ; töre
  kk төре [töre] ; yargıç; soylu ; ff:Kazakçada төре "soylu, yargıç" anlamına kaymıştır
  uz toʻra ; soylu; yargıç
  ky төрө [törö] ; soylu
  mn төр [tör] ; devlet ; ff:Moğolca төр "devlet, düzen" demektir
@tanık from_turkish
  hu tanú ; tanık
  az tanıq ; tanık
  kk таныс [tanıs] ; tanıdık
  uz tanish ; tanıdık
@yas from_turkish
  hu gyász ; yas
  az yas ; yas
  kk жас [jas] ; yaş (göz yaşı); genç ; ff:Kazakçada жас "gözyaşı" ve "genç" anlamlarındadır
  tk ýas ; yas
@kenevir shared_ancestor
  hu kender ; kenevir
  az kənaf ; kenevir
  kk кенеп [kenep] ; kenevir bezi
@ordu from_turkish
  en horde ; kalabalık, sürü ; ff:İngilizcede horde "düzensiz kalabalık" anlamına kaymıştır
  fr horde ; kalabalık, çete ; ff:Fransızcada horde olumsuz anlamda "yağmacı kalabalık" demektir
  de Horde ; sürü, kalabalık
  ru орда [orda] ; Altın Orda; kalabalık
  pl horda ; kalabalık
  hu horda ; kalabalık, sürü
  it orda ; kalabalık
  es horda ; kalabalık
  uk орда [orda] ; kalabalık
  az ordu ; ordu
  kk орда [orda] ; han karargâhı; merkez
  uz oʻrda ; han sarayı
  ky ордо [ordo] ; karargâh; başkent
  tk orda ; ordu
  mn орд [ord] ; saray, karargâh
@tabur from_turkish
  hu tábor ; kamp, ordugâh ; ff:Macarca tábor "kamp" anlamındadır
  ru табор [tabor] ; Çingene kampı ; ff:Rusçada табор "göçer kampı" anlamına kaymıştır
  ro tabără ; kamp
  pl tabor ; konvoy, kamp
  sr табор [tabor] ; kamp
  bg табор [tabor] ; tabur; kamp
@yeniçeri from_turkish
  en janissary ; yeniçeri
  fr janissaire ; yeniçeri
  de Janitschar ; yeniçeri
  it giannizzero ; yeniçeri
  hu janicsár ; yeniçeri
  ro ienicer ; yeniçeri
  sr јаничар [janičar] ; yeniçeri
  bg еничар [yeniçar] ; yeniçeri
  sq jeniçer ; yeniçeri
  pl janczar ; yeniçeri
  ru янычар [yanıçar] ; yeniçeri
  el γενίτσαρος [genítsaros] ; yeniçeri
@sipahi from_turkish
  hu szpáhi ; sipahi
  ro spahiu ; sipahi
  sr спахија [spahija] ; toprak sahibi ; ff:Sırpçada spahija "büyük toprak ağası" anlamındadır
  bg спахия [spahiya] ; sipahi
  sq spahi ; sipahi
  en spahi ; Kuzey Afrika Fransız süvarisi ; ff:Fransızca ve İngilizcede spahi, Osmanlı değil Fransız sömürge süvarisini anlatır
  fr spahi ; Fransız sömürge süvarisi
@haydut from_turkish
  hu hajdú ; çoban asker; Hajdú ili ; ff:Macarcada hajdú "sığır çobanı; serbest asker" anlamındadır, olumsuz anlam yoktur
  sr хајдук [hajduk] ; dağ eşkıyası; halk kahramanı ; ff:Sırpçada hajduk Osmanlı'ya karşı savaşan "halk kahramanı"dır
  bg хайдук [hayduk] ; eşkıya; halk kahramanı
  ro haiduc ; eşkıya kahraman
  sq hajdut ; hırsız
  mk ајдук [ajduk] ; eşkıya; kahraman
  pl hajduk ; uşak; piyade ; ff:Lehçede hajduk saray uşağı ve Macar piyadesi anlamındadır
  uk гайдук [hayduk] ; piyade; uşak
@paşa from_turkish
  en pasha ; paşa
  fr pacha ; paşa; lüks içinde yaşayan ; ff:Fransızcada "vivre comme un pacha" (paşa gibi yaşamak) deyimi vardır
  de Pascha ; paşa; şımartılan erkek ; ff:Almancada Pascha "evde hizmet bekleyen erkek" anlamında alaycı kullanılır
  it pascià ; paşa
  es pachá ; paşa
  hu pasa ; paşa
  ro pașă ; paşa
  sr паша [paša] ; paşa
  bg паша [paşa] ; paşa
  sq pasha ; paşa
  ru паша [paşa] ; paşa
  el πασάς [pasás] ; paşa
  pl pasza ; paşa
@bey from_turkish
  hu bég ; bey
  sr бег [beg] ; bey
  bg бей [bey] ; bey
  sq bej ; bey
  ro bei ; bey
  en bey ; bey
  fr bey ; bey (Tunus)
  ru бей [bey] ; bey
  el μπέης [béis] ; bey
  az bəy ; bey; damat ; ff:Azerbaycan Türkçesinde bəy aynı zamanda "damat" demektir
  kk би [bi] ; yargıç, bey
  uz bek ; bey
  ky бий [biy] ; yargıç, bey
  tk beg ; bey
@ağa from_turkish
  hu aga ; ağa
  sr ага [aga] ; ağa
  bg ага [aga] ; ağa
  sq aga ; ağa
  ro agă ; ağa
  en agha ; ağa
  el αγάς [agás] ; ağa
  ru ага [aga] ; ağa
  az ağa ; ağa; efendi
  kk ағa [ağa] ; ağabey ; ff:Kazakçada ağa "ağabey" demektir
  uz aka ; ağabey
  ky ага [aga] ; ağabey
@efendi from_turkish
  sr ефендија [efendija] ; efendi
  bg ефенди [efendi] ; efendi
  sq efendi ; efendi
  ro efendi ; efendi
  en effendi ; efendi
  fr effendi ; efendi
  ar afandī ; efendi
  el αφέντης [aféntis] ; efendi, sahip ; ff:Türkçeye Rumcadan gelen efendi, aynı biçimde Yunancada "sahip, patron" anlamını sürdürür
@kadı from_turkish
  sr кадија [kadija] ; kadı
  bg кадия [kadiya] ; kadı
  sq kadi ; kadı
  ro cadiu ; kadı
  en qadi ; kadı
  es alcalde ; belediye başkanı ; ff:İspanyolca alcalde (belediye başkanı) Arapça al-qāḍī'den gelir; Türkçe kadı ile aynı köktendir
  pt alcaide ; kale komutanı; belediye başkanı
@vezir from_turkish
  hu vezér ; önder, komutan ; ff:Macarca vezér "lider" anlamındadır
  sr везир [vezir] ; vezir
  bg везир [vezir] ; vezir
  sq vezir ; vezir
  en vizier ; vezir
  fr vizir ; vezir
  de Wesir ; vezir
  ru визирь [vizir] ; vezir
  es alguacil ; mübaşir, icra memuru ; ff:İspanyolca alguacil (icra memuru) Arapça al-wazīr'den gelir
@sancak from_turkish
  sr санџак [sandžak] ; Sancak bölgesi; sancak ; ff:Sırpçada Sandžak, Sırbistan–Karadağ arasındaki bölgenin adıdır
  bg санджак [sancak] ; sancak
  sq sanxhak ; sancak
  mk санџак [sandžak] ; sancak
  az sancaq ; sancak; iğne ; ff:Azerbaycan Türkçesinde sancaq "çengelli iğne" demektir
  hu szandzsák ; Osmanlı sancağı
@barut from_turkish
  sr барут [barut] ; barut
  bg барут [barut] ; barut
  sq barut ; barut
  mk барут [barut] ; barut
  el μπαρούτι [baroúti] ; barut ; ff:Türkçe barut Rumca pyrítis'ten gelir; Yunanca μπαρούτι Türkçeden geri alınmıştır
@top from_turkish
  sr топ [top] ; top (silah) ; ff:Sırpçada top yalnızca "ateşli silah" demektir, oyun topu için lopta kullanılır
  bg топ [top] ; top (silah); satranç kalesi ; ff:Bulgarcada топ satrançta "kale" taşıdır
  sq top ; top (silah); top (oyun)
  mk топ [top] ; top (silah)
  ro tun ; top (silah)
  az top ; top
  kk доп [dop] ; oyun topu
  uz top ; top (silah)
@bayrak from_turkish
  sr барјак [barjak] ; bayrak
  bg байрак [bayrak] ; bayrak
  sq bajrak ; bayrak; kabile birliği ; ff:Arnavutçada bajrak Osmanlı döneminde "kabile bölgesi" anlamını almıştır
  mk бајрак [bajrak] ; bayrak
  az bayraq ; bayrak
  kk байрақ [bayraq] ; ödül; sancak ; ff:Kazakçada байрақ "yarış ödülü" anlamındadır
  uz bayroq ; bayrak
  ky байрак [bayrak] ; ödül; bayrak
  tk baýdak ; bayrak
@davul from_turkish
  sr даул [daul] ; davul (eski)
  bg даул [daul] ; davul
  sq daulle ; davul
  mk тапан [tapan] ; davul
  el νταούλι [daoúli] ; davul
@zurna from_turkish
  sr зурла [zurla] ; zurna
  bg зурна [zurna] ; zurna
  sq surle ; zurna
  mk зурла [zurla] ; zurna
  el ζουρνάς [zournás] ; zurna
  hy զուռնա [zuṙna] ; zurna
  ka ზურნა [zurna] ; zurna
@saz from_turkish
  sr саз [saz] ; saz
  bg саз [saz] ; saz
  sq saze ; saz; çalgı takımı
  el σάζι [sázi] ; saz
  hy սազ [saz] ; saz
@kaval from_turkish
  sr кавал [kaval] ; kaval
  bg кавал [kaval] ; kaval
  sq kavall ; kaval
  mk кавал [kaval] ; kaval
  ro caval ; kaval
@düdük from_turkish
  hy դուդուկ [duduk] ; düdük (Ermeni üflemeli çalgısı) ; ff:Ermenice duduk, Türkçe düdük'ten gelir ancak özel bir çalgıyı adlandırır
  sr дудук [duduk] ; kaval
  bg дудук [duduk] ; kaval
  ka დუდუკი [duduki] ; düdük
  ru дудка [dudka] ; düdük
@cambaz from_turkish
  sr џамбас [džambas] ; at tüccarı ; ff:Sırpçada džambas "at tüccarı" anlamındadır
  bg джамбаз [cambaz] ; at tüccarı; cambaz
  sq xhambaz ; at tüccarı; hilekâr
  ro geambaș ; at tüccarı ; ff:Rumencede geambaș "at tüccarı, hileci" demektir
  mk џамбаз [džambaz] ; cambaz
@pehlivan from_turkish
  sr пеливан [pelivan] ; güreşçi
  bg пехливан [pehlivan] ; güreşçi
  sq pehlivan ; güreşçi; akrobat
  ro pehlivan ; düzenbaz, hileci ; ff:Rumencede pehlivan "üçkâğıtçı" anlamına kaymıştır
  mk пеливан [pelivan] ; güreşçi
  fa پهلوان [pahlavān] ; yiğit, kahraman ; ff:Farsça pahlavān "yiğit, şampiyon" demektir; Türkçede güreşçiye özelleşmiştir
@haydi from_turkish
  sr хајде [hajde] ; haydi
  bg хайде [hayde] ; haydi
  sq hajde ; haydi
  mk ајде [ajde] ; haydi
  ro haide ; haydi
  el άντε [ánde] ; haydi
  ru айда [ayda] ; haydi
  uk гайда [hayda] ; haydi
  hy հայդե [hayde] ; haydi
@yavaş from_turkish
  sr јаваш [javaš] ; yavaş; umursamaz ; ff:Sırpçada javašluk "umursamazlık, savsaklama" demektir
  bg яваш [yavaş] ; yavaş
  sq javash ; yavaş
  mk јаваш [javaš] ; yavaş
  el γιαβάς [giavás] ; yavaş yavaş
@aman from_turkish
  sr аман [aman] ; aman
  bg аман [aman] ; aman; yeter
  sq aman ; aman
  ro aman ; aman (eski)
  el αμάν [amán] ; aman
  mk аман [aman] ; aman
@bre from_turkish
  sr бре [bre] ; bre, ya ; ff:Sırpçada bre çok sık kullanılan pekiştirme ünlemidir
  bg бре [bre] ; bre
  sq bre ; bre
  ro bre ; bre
  el βρε [vre] ; bre; be ; ff:Türkçe bre'nin kaynağı Rumca moré/vre'dir; Balkanlarda karşılıklı alışverişle yayılmıştır
  mk бре [bre] ; bre
@tamam from_turkish
  sr таман [taman] ; tam, tamam
  bg таман [taman] ; tamam; tam o sırada ; ff:Bulgarcada таман "tam o anda" anlamında zarftır
  sq tamam ; tamam
  mk таман [taman] ; tam
  ro taman ; tam; sadece
  el ταμάμ [tamám] ; tamam (halk ağzı)
@kolay from_turkish
  sr колај [kolaj] ; kolay
  bg колай [kolay] ; kolaylık, çare ; ff:Bulgarcada колай "çare, yol" anlamındadır
  sq kollaj ; kolay
  mk колај [kolaj] ; kolay
@vakit from_turkish
  sr вакат [vakat] ; vakit
  bg вакът [vakıt] ; vakit
  sq vakt ; vakit
  mk вакат [vakat] ; vakit
@sabah from_turkish
  sr сабах [sabah] ; sabah namazı ; ff:Sırpçada (Boşnak ağzı) sabah yalnızca "sabah namazı" anlamındadır
  bg сабах [sabah] ; sabah
  sq sabah ; sabah
  mk сабајле [sabajle] ; sabahleyin
  el σαμπάχ [sabáh] ; sabah (eski)
@akşam from_turkish
  sr акшам [akšam] ; akşam namazı; akşam
  bg акшам [akşam] ; akşam
  sq aksham ; akşam
  mk акшам [akšam] ; akşam
  az axşam ; akşam
  kk ақшам [aqşam] ; akşam
  uz oqshom ; akşam
  tk agşam ; akşam
@çarşı from_turkish
  sr чаршија [čaršija] ; çarşı; eski kent merkezi ; ff:Sırpçada čaršija aynı zamanda "dedikodu yapan kasaba halkı" demektir
  bg чаршия [çarşiya] ; çarşı
  sq çarshi ; çarşı
  mk чаршија [čaršija] ; çarşı
  el τσαρσί [tsarsí] ; çarşı
@bakkal from_turkish
  sr бакал [bakal] ; bakkal
  bg бакал ; bakkal; bakkaliye ; ff:Bulgarcada бакалия "bakkaliye malı" demektir
  sq bakall ; bakkal
  mk бакал [bakal] ; bakkal
  ro băcan ; bakkal ; ff:Rumence băcan bakkal, băcănie bakkal dükkânı anlamındadır
  el μπακάλης [bakális] ; bakkal
@kasap from_turkish
  sr касапин [kasapin] ; kasap
  bg касап [kasap] ; kasap; kıyıcı
  sq kasap ; kasap
  mk касап [kasap] ; kasap
  ro casap ; kasap (eski)
  el χασάπης [chasápis] ; kasap
@kuyumcu from_turkish
  sr кујунџија [kujundžija] ; kuyumcu
  bg куюмджия [kuyumciya] ; kuyumcu
  sq kujunxhi ; kuyumcu
  mk кујунџија [kujundžija] ; kuyumcu
@boyacı from_turkish
  sr бојаџија [bojadžija] ; boyacı
  bg бояджия [boyaciya] ; boyacı
  sq bojaxhi ; boyacı
  mk бојаџија [bojadžija] ; boyacı
  el μπογιατζής [bogiatzís] ; boyacı
@nalbant from_turkish
  sr налбанта [nalbanta] ; nalbant
  bg налбант [nalbant] ; nalbant
  sq nallban ; nalbant
  mk налбат [nalbat] ; nalbant
  el ναλμπάντης [nalbándis] ; nalbant
@hamal from_turkish
  sr амал [amal] ; hamal
  bg хамал [hamal] ; hamal
  sq hamall ; hamal
  ro hamal ; hamal
  mk амал [amal] ; hamal
  el χαμάλης [chamális] ; hamal; kaba adam ; ff:Yunancada χαμάλης "kaba, görgüsüz adam" anlamında da kullanılır
@çoban from_turkish
  sr чобан [čoban] ; çoban
  bg чобан [çoban] ; çoban
  sq çoban ; çoban
  ro cioban ; çoban
  mk чобан [čoban] ; çoban
  hu csobán ; çoban (ağızlarda)
  el τσομπάνης [tsobánis] ; çoban
  uk чабан [çaban] ; çoban
  ru чабан [çaban] ; çoban
@budala from_turkish
  sr будала [budala] ; budala
  bg будала [budala] ; budala
  sq budalla ; budala
  mk будала [budala] ; budala
  ro budalà ; budala (eski)
  el μπουνταλάς [boundalás] ; budala
@deli from_turkish
  sr делија [delija] ; yiğit, kabadayı ; ff:Sırpçada delija "yiğit, delikanlı" anlamına kaymıştır
  bg делия [deliya] ; yiğit; deli
  sq deli ; yiğit, cesur ; ff:Arnavutçada deli "cesur" demektir
  mk делија [delija] ; yiğit
  ro deliu ; cesur; Osmanlı atlısı
@hoca from_turkish
  sr хоџа [hodža] ; hoca
  bg ходжа [hoca] ; hoca
  sq hoxhë ; hoca
  mk оџа [odža] ; hoca
  ro hoge ; hoca
  en hodja ; hoca (Nasreddin Hoca)
  az xoca ; hoca
  kk қожа [qoja] ; hoca; efendi
  uz xoʻja ; efendi; hoca
  tk hoja ; hoca
@mahalle from_turkish
  sr махала [mahala] ; mahalle
  bg махала [mahala] ; mahalle; köy bölümü
  sq mëhallë ; mahalle
  ro mahala ; kenar mahalle, varoş ; ff:Rumencede mahala "yoksul kenar mahalle" anlamına kaymıştır
  mk маало [maalo] ; mahalle
  el μαχαλάς [machalás] ; mahalle
@sokak from_turkish
  sr сокак [sokak] ; dar sokak
  bg сокак [sokak] ; sokak
  sq sokak ; sokak
  mk сокак [sokak] ; sokak
  el σοκάκι [sokáki] ; dar sokak
@kaldırım from_turkish
  sr калдрма [kaldrma] ; taş döşeme yol ; ff:Sırpçada kaldrma "parke taşlı yol" demektir; yaya kaldırımı için trotoar kullanılır
  bg калдъръм [kaldırım] ; taş döşeme yol
  sq kalldrëm ; taş yol
  ro caldarâm ; taş döşeme ; ff:Rumencede caldarâm "arnavut kaldırımı" anlamındadır
  mk калдрма [kaldrma] ; taş yol
  el καλντερίμι [kalderími] ; taş döşeme yol ; ff:Türkçe kaldırım Rumca kalódromos'tan gelir; Yunanca καλντερίμι Türkçeden geri alınmıştır
@çeşme from_turkish
  sr чесма [česma] ; çeşme
  bg чешма [çeşma] ; çeşme; musluk ; ff:Bulgarcada чешма aynı zamanda "musluk" demektir
  sq çezmë ; çeşme
  ro cișmea ; çeşme
  mk чешма [češma] ; çeşme; musluk
  el τσεσμές [tsesmés] ; çeşme
@pınar from_turkish
  sr бунар [bunar] ; kuyu ; ff:Sırpçada bunar "kuyu" anlamına kaymıştır
  bg бунар [bunar] ; kuyu
  sq bunar ; kuyu
  mk бунар [bunar] ; kuyu
@han from_turkish
  sr хан [han] ; han
  bg хан [han] ; han
  sq han ; han
  ro han ; han
  mk ан [an] ; han
  el χάνι [cháni] ; han
@konak from_turkish
  sr конак [konak] ; konak; gecelik konaklama ; ff:Sırpçada konak aynı zamanda "bir gecelik yol" demektir
  bg конак [konak] ; konak; karakol
  sq konak ; konak; konaklama
  ro conac ; çiftlik evi, malikâne ; ff:Rumencede conac "boyar malikânesi" anlamındadır
  mk конак [konak] ; konak
  el κονάκι [konáki] ; konak
@çardak from_turkish
  sr чардак [čardak] ; cumba; köşk
  bg чардак [çardak] ; balkon, veranda ; ff:Bulgarcada чардак "üstü kapalı balkon" demektir
  sq çardak ; çardak
  ro cerdac ; veranda ; ff:Rumencede cerdac "ev önü verandası" demektir
  mk чардак [čardak] ; çardak
@kule from_turkish
  sr кула [kula] ; kule
  bg кула [kula] ; kule
  sq kullë ; kule; Arnavut taş evi ; ff:Arnavutçada kullë geleneksel kule biçimli taş evi adlandırır
  ro culă ; kule ev
  mk кула [kula] ; kule
  el κούλα [koúla] ; kule
@tavan from_turkish
  sr таван [tavan] ; tavan arası ; ff:Sırpçada tavan "tavan arası, çatı katı" demektir
  bg таван [tavan] ; tavan; tavan arası
  sq tavan ; tavan
  ro tavan ; tavan
  mk таван [tavan] ; tavan arası
  el ταβάνι [taváni] ; tavan
@oda from_turkish
  sr одаја [odaja] ; oda
  bg одая [odaya] ; oda
  sq odë ; oda; misafir odası ; ff:Arnavutçada odë özellikle "erkek misafir odası" anlamındadır
  ro odaie ; oda
  mk одаја [odaja] ; oda
  el οντάς [ondás] ; oda
@kat from_turkish
  sr кат [kat] ; kat
  bg кат [kat] ; kat; takım
  sq kat ; kat
  mk кат [kat] ; kat
@avlu from_turkish
  sr авлија [avlija] ; avlu
  bg авлия [avliya] ; avlu
  sq avlli ; avlu
  mk авлија [avlija] ; avlu
  el αυλή [avlí] ; avlu ; ff:Türkçe avlu Rumca avlí'den gelir; Balkan Slav dillerine Türkçe yoluyla geçmiştir
@bahçe from_turkish
  sr башта [bašta] ; bahçe
  bg бахча [bahça] ; bostan ; ff:Bulgarcada бахча "sebze bostanı" anlamındadır
  sq bahçe ; bahçe
  mk бавча [bavča] ; bahçe
  ru бахча [bahça] ; karpuz-kavun tarlası ; ff:Rusçada бахча "karpuz tarlası" demektir
  uk баштан [baştan] ; bostan
  el μπαξές [baxés] ; bahçe
@cami from_turkish
  sr џамија [džamija] ; cami
  bg джамия [camiya] ; cami
  sq xhami ; cami
  mk џамија [džamija] ; cami
  hu dzsámi ; cami
  ro geamie ; cami
  el τζαμί [tzamí] ; cami
@hamam from_turkish
  sr хамам [hamam] ; hamam
  bg хамам [hamam] ; hamam
  sq hamam ; hamam
  mk амам [amam] ; hamam
  en hammam ; Türk hamamı
  fr hammam ; Türk hamamı
  de Hamam ; Türk hamamı
  el χαμάμ [chamám] ; hamam
  ro hamam ; hamam
@türbe from_turkish
  sr турбе [turbe] ; türbe
  bg тюрбе [tyurbe] ; türbe
  sq tyrbe ; türbe
  mk турбе [turbe] ; türbe
  ro turbe ; türbe
@tekke from_turkish
  sr текија [tekija] ; tekke
  bg теке [teke] ; tekke
  sq teqe ; tekke
  mk теќе [teḱe] ; tekke
  el τεκές [tekés] ; tekke; esrarkeş yuvası ; ff:Yunancada τεκές "esrar içilen yer" anlamına kaymıştır
@kutu from_turkish
  sr кутија [kutija] ; kutu
  bg кутия [kutiya] ; kutu
  sq kuti ; kutu
  mk кутија [kutija] ; kutu
  el κουτί [koutí] ; kutu ; ff:Türkçe kutu Rumca koutí'den gelir; Slav dillerine Türkçe yoluyla geçmiştir
@sandık from_turkish
  sr сандук [sanduk] ; sandık
  bg сандък [sandık] ; sandık
  sq sënduk ; sandık
  mk сандак [sandak] ; sandık
  ro sunduc ; sandık (eski)
  ru сундук [sunduk] ; sandık
  uk сундук [sunduk] ; sandık
@dolap from_turkish
  sr долап [dolap] ; dolap; su dolabı
  bg долап [dolap] ; dolap
  sq dollap ; dolap
  ro dulap ; dolap
  mk долап [dolap] ; dolap
  el ντουλάπι [doulápi] ; dolap
@yastık from_turkish
  sr јастук [jastuk] ; yastık
  sq jastëk ; yastık
  mk јастак [jastak] ; yastık
  el γιαστίκι [giastíki] ; yastık (ağızlarda)
@yorgan from_turkish
  sr јорган [jorgan] ; yorgan
  bg юрган [yurgan] ; yorgan
  sq jorgan ; yorgan
  mk јорган [jorgan] ; yorgan
  ro iorgan ; yorgan (ağızlarda)
  el γιοργάνι [giorgáni] ; yorgan (ağızlarda)
@çarşaf from_turkish
  sr чаршав [čaršav] ; çarşaf; masa örtüsü ; ff:Sırpçada čaršav "masa örtüsü" anlamında da kullanılır
  bg чаршаф [çarşaf] ; çarşaf
  sq çarçaf ; çarşaf
  ro cearșaf ; çarşaf
  mk чаршаф [čaršaf] ; çarşaf
  el τσαρσάφι [tsarsáfi] ; çarşaf
@peşkir from_turkish
  sr пешкир [peškir] ; havlu
  bg пешкир [peşkir] ; havlu
  sq peshqir ; havlu
  mk пешкир [peškir] ; havlu
  ro peșchir ; havlu (eski)
  el πεσκίρι [peskíri] ; peçete
@kilim from_turkish
  sr ћилим [ćilim] ; kilim
  bg килим [kilim] ; kilim; halı
  sq qilim ; kilim
  ro chilim ; kilim
  mk килим [kilim] ; kilim
  hu kilim ; kilim
  en kilim ; kilim
  fr kilim ; kilim
  de Kelim ; kilim
  ru килим [kilim] ; kilim
  uk килим [kılım] ; halı ; ff:Ukraynacada килим genel olarak "halı" demektir
  pl kilim ; kilim
  el κιλίμι [kilími] ; kilim
@minder from_turkish
  sr миндер [minder] ; minder
  bg миндер [minder] ; sedir, minder
  sq minder ; minder
  mk миндер [minder] ; minder
  el μιντέρι [mindéri] ; minder
@çorap from_turkish
  sr чарапа [čarapa] ; çorap
  bg чорап [çorap] ; çorap
  sq çorape ; çorap
  ro ciorap ; çorap
  mk чорап [čorap] ; çorap
  el τσουράπι [tsourápi] ; yün çorap
@pabuç from_turkish
  sr папуча [papuča] ; terlik ; ff:Sırpçada papuča "terlik" demektir
  bg папук [papuk] ; terlik
  sq papuçe ; terlik
  ro papuc ; terlik
  hu papucs ; terlik ; ff:Macarca papucs "terlik" anlamındadır
  mk папуче [papuče] ; terlik
  fr babouche ; şark terliği
  en babouche ; şark terliği
@yelek from_turkish
  sr јелек [jelek] ; yelek
  bg елек [elek] ; yelek
  sq jelek ; yelek
  ro ilic ; yelek
  mk елек [elek] ; yelek
  el γιλέκο [giléko] ; yelek
  fr gilet ; yelek ; ff:Fransızca gilet, Türkçe yelek'ten İspanyolca jileco ve Arapça yoluyla alınmıştır
  es chaleco ; yelek
  it gilè ; yelek
  en gilet ; yelek
@şalvar from_turkish
  sr шалваре [šalvare] ; şalvar
  bg шалвари [şalvari] ; şalvar
  sq shallvare ; şalvar
  ro șalvari ; şalvar
  mk шалвари [šalvari] ; şalvar
  el σαλβάρι [salvári] ; şalvar
  ru шаровары [şarovarı] ; şalvar
  uk шаровари [şarovarı] ; Kazak şalvarı
  fa شلوار [şalvār] ; pantolon ; ff:Türkçe şalvar Farsçadan gelir; Farsçada şalvār genel olarak "pantolon" demektir
  ur شلوار [şalvār] ; şalvar
@fes from_turkish
  sr фес [fes] ; fes
  bg фес [fes] ; fes
  sq fes ; fes
  ro fes ; fes
  mk фес [fes] ; fes
  en fez ; fes
  fr fez ; fes
  de Fes ; fes
  el φέσι [fési] ; fes
@kalpak from_turkish
  sr калпак [kalpak] ; kalpak
  bg калпак [kalpak] ; kalpak
  sq kallpak ; kalpak
  ro calpac ; kalpak
  hu kalpag ; kalpak
  ru колпак [kolpak] ; abajur; külah ; ff:Rusçada колпак "abajur, kapak, külah" anlamlarına kaymıştır
  uk ковпак [kovpak] ; külah
  pl kołpak ; kalpak
  el καλπάκι [kalpáki] ; kalpak
@düğme from_turkish
  sr дугме [dugme] ; düğme
@para from_turkish
  sr пара [para] ; para; kuruş ; ff:Sırpçada para hem "para" hem dinarın yüzde biri "kuruş"tur
  bg пара [para] ; para
  sq para ; para
  ro para ; para; metelik ; ff:Rumencede para "değersiz küçük para" demektir
  mk пара [para] ; para
  el παράς [parás] ; para (halk ağzı)
@kese from_turkish
  sr кеса [kesa] ; torba, poşet ; ff:Sırpçada kesa "plastik poşet" dâhil her tür torba demektir
  bg кесия [kesiya] ; kese; cüzdan
  sq qese ; torba
  mk кеса [kesa] ; torba
  ro chisea ; kese (eski)
  el κεσές [kesés] ; kese
@pazar from_turkish
  sr пазар [pazar] ; pazar; alışveriş ; ff:Sırpçada pazar "alışveriş, satış" anlamında da kullanılır
  bg пазар [pazar] ; pazar; piyasa
  sq pazar ; pazar
  mk пазар [pazar] ; pazar
  el παζάρι [pazári] ; pazar; pazarlık
@bedava from_turkish
  sr бадава [badava] ; bedava; boşuna ; ff:Sırpçada badava daha çok "boşuna, nafile" anlamındadır
  bg бадева [badeva] ; boşuna
  sq badihava ; bedava
  mk бадијала [badijala] ; boşuna
@bereket from_turkish
  sr берићет [berićet] ; bereket
  bg берекет [bereket] ; bereket
  sq bereqet ; bereket; ekin ; ff:Arnavutçada bereqet "tahıl ürünü" anlamına da gelir
  mk бериќет [beriḱet] ; bereket
  ro berechet ; bolluk; bol bol ; ff:Rumencede berechet "bol bol" zarfıdır
@kısmet from_turkish
  sr кисмет [kismet] ; kısmet
  bg късмет [kısmet] ; şans, talih ; ff:Bulgarcada късмет en yaygın "şans" sözcüğüdür
  sq kësmet ; kısmet
  mk к'смет [k'smet] ; şans
  en kismet ; kader
  fr kismet ; kader
  de Kismet ; kader
  el κισμέτ [kismét] ; kader
@kavga from_turkish
  sr кавга [kavga] ; kavga
  bg кавга [kavga] ; kavga
  sq kavgë ; kavga
  mk кавга [kavga] ; kavga
  el καβγάς [kavgás] ; kavga
@kabadayı from_turkish
  sr кабадахија [kabadahija] ; kabadayı
  bg кабадая [kabadaya] ; kabadayı
  sq kabadai ; kabadayı
  mk кабадаија [kabadaija] ; kabadayı
  el καμπαντάης [kabadáis] ; kabadayı
@yabancı from_turkish
  sr јабанџија [jabandžija] ; yabancı ; ff:Sırpçada jabandžija "yabancı, dışarıdan gelen" demektir
  bg ябанджия [yabanciya] ; yabancı
  sq jabanxhi ; yabancı
  mk јабанџија [jabandžija] ; yabancı
  el γιαμπαντζής [giabantzís] ; yabancı (ağızlarda)
@dost from_turkish
  sr дост [dost] ; dost
  bg дост [dost] ; dost
  sq dost ; dost
  mk дост [dost] ; dost
  fa دوست [dūst] ; dost ; ff:Türkçe dost Farsçadan gelir; Farsçada dūst aynı anlamdadır
  ur دوست [dost] ; dost
  ur दोस्त [dost] ; dost
@merak from_turkish
  sr мерак [merak] ; keyif, zevk ; ff:Sırpçada merak "derin keyif, tutku" anlamına kaymıştır
  bg мерак [merak] ; arzu, istek ; ff:Bulgarcada мерак "istek, heves" demektir
  sq merak ; kaygı, tasa ; ff:Arnavutçada merak "kaygı" anlamındadır
  mk мерак [merak] ; keyif; arzu
  el μεράκι [meráki] ; özenle yapılan iş; tutku ; ff:Yunancada μεράκι "bir işi sevgiyle yapma" demektir
@sevda from_turkish
  sr севдах [sevdah] ; aşk hüznü; Boşnak şarkısı ; ff:Sırpça/Boşnakçada sevdah hem "aşk acısı" hem de sevdalinka türkülerinin duygusudur
  bg севда [sevda] ; sevda
  sq sevda ; sevda
  mk севда [sevda] ; sevda
  el σεβντάς [sevdás] ; sevda
@inat from_turkish
  sr инат [inat] ; inat, nispet ; ff:Sırpçada inat "başkasına nispet yapma" anlamında ulusal bir karakter özelliği sayılır
  bg инат [inat] ; inat
  sq inat ; inat; öfke
  mk инает [inaet] ; inat
@keyif from_turkish
  sr ћеиф [ćeif] ; keyif
  bg кеф [kef] ; keyif
  sq qejf ; keyif
  mk ќеф [ḱef] ; keyif
  ro chef ; eğlence, âlem ; ff:Rumencede chef "içkili eğlence, âlem" demektir
  el κέφι [kéfi] ; neşe, keyif ; ff:Yunancada κέφι "coşkulu neşe" anlamında temel bir kavramdır
@zanaat from_turkish
  sr занат [zanat] ; zanaat
  bg занаят [zanayat] ; zanaat
  sq zanat ; zanaat
  mk занаат [zanaat] ; zanaat
@esnaf from_turkish
  sr еснаф [esnaf] ; esnaf; lonca
  bg еснаф [esnaf] ; esnaf; dar görüşlü ; ff:Bulgarcada еснаф "dar kafalı küçük burjuva" anlamında da kullanılır
  sq esnaf ; esnaf
  mk еснаф [esnaf] ; esnaf
  el εσνάφι [esnáfi] ; lonca
@kalfa from_turkish
  sr калфа [kalfa] ; kalfa
  bg калфа [kalfa] ; kalfa
  sq kallfë ; kalfa
  mk калфа [kalfa] ; kalfa
  ro calfă ; kalfa
@usta from_turkish
  bg уста [usta] ; usta
  sq usta ; usta
  mk уста [usta] ; usta
  el ουστάς [oustás] ; usta (ağızlarda)
  az usta ; usta
  kk ұста [usta] ; demirci; usta ; ff:Kazakçada ұста özellikle "demirci" demektir
  uz usta ; usta
  ky уста [usta] ; usta
  tk ussa ; usta
@sofra from_turkish
  sr софра [sofra] ; sofra; alçak yemek masası
  bg софра [sofra] ; alçak yemek masası
  sq sofër ; sofra
  mk софра [sofra] ; sofra
  el σοφράς [sofrás] ; alçak masa
@tepsi from_turkish
  sr тепсија [tepsija] ; tepsi; fırın kabı
  bg тепсия [tepsiya] ; tepsi
  sq tepsi ; tepsi
  mk тепсија [tepsija] ; tepsi
  ro tipsie ; tepsi
  el ταψί [tapsí] ; fırın tepsisi
@tencere from_turkish
  sr тенџера [tendžera] ; tencere
  bg тенджера [tencera] ; tencere
  sq tenxhere ; tencere
  mk тенџере [tendžere] ; tencere
  el τέντζερης [téntzeris] ; tencere
@tava from_turkish
  sr тава [tava] ; tava
  bg тава [tava] ; tepsi ; ff:Bulgarcada тава "fırın tepsisi" demektir
  sq tavë ; tava; güveç yemeği ; ff:Arnavutçada tavë fırında pişen güveç yemeğidir (tavë kosi)
  ro tavă ; tepsi
  mk тава [tava] ; tava
  el ταβάς [tavás] ; tava
@kazan from_turkish
  sr казан [kazan] ; kazan
  bg казан [kazan] ; kazan; rakı kazanı
  sq kazan ; kazan
  ro cazan ; kazan
  mk казан [kazan] ; kazan
  hu kazán ; kazan
  ru казан [kazan] ; kazan; Kazan kenti
  uk казан [kazan] ; kazan
  el καζάνι [kazáni] ; kazan
  az qazan ; kazan
  kk қазан [qazan] ; kazan; ekim ayı ; ff:Kazakçada қазан aynı zamanda ekim ayının adıdır
  uz qozon ; kazan
  ky казан [kazan] ; kazan
  tk gazan ; kazan
@ibrik from_turkish
  sr ибрик [ibrik] ; ibrik
  bg ибрик [ibrik] ; ibrik
  sq ibrik ; ibrik
  ro ibric ; cezve ; ff:Rumencede ibric "kahve cezvesi" demektir
  mk ибрик [ibrik] ; ibrik
  el μπρίκι [bríki] ; cezve ; ff:Yunancada μπρίκι "kahve cezvesi" anlamındadır
@fincan from_turkish
  sr филџан [fildžan] ; fincan
  bg филджан [filcan] ; fincan
  sq filxhan ; fincan
  mk филџан [fildžan] ; fincan
  el φλιτζάνι [flitzáni] ; fincan
@çakı from_turkish
  sr чакија [čakija] ; çakı
  bg чакия [çakiya] ; çakı
  sq çakí ; çakı
  mk чакија [čakija] ; çakı
@meze from_turkish
  sr мезе [meze] ; meze
  bg мезе [meze] ; meze
  sq meze ; meze
  mk мезе [meze] ; meze
  ro mezel ; şarküteri ürünü ; ff:Rumencede mezel "sucuk, salam gibi et ürünü" demektir
  el μεζές [mezés] ; meze
  en meze ; meze
  fr mezzé ; meze
  fa مزه [maze] ; tat, lezzet ; ff:Türkçe meze Farsça maze "tat"tan gelir
@köfte from_turkish
  sr ћуфте [ćufte] ; köfte
  bg кюфте [kyufte] ; köfte
  sq qofte ; köfte
  ro chiftea ; köfte
  mk ќофте [ḱofte] ; köfte
  el κεφτές [keftés] ; köfte
  en kofta ; köfte
  fa کوفته [kūfte] ; köfte ; ff:Türkçe köfte Farsça kūfte "dövülmüş"ten gelir
  ur کوفتہ [kofta] ; köfte
@börek from_turkish
  sr бурек [burek] ; börek
  bg бюрек [byurek] ; börek
  sq byrek ; börek
  mk бурек [burek] ; börek
  el μπουρέκι [bouréki] ; börek
  en börek ; börek
  hu burek ; börek
  az börək ; börek
  kk бүрек [bürek] ; böbrek ; ff:Kazakçada бүрек "böbrek" demektir; börek ile ses benzerliği yanıltıcıdır
@pilav from_turkish
  sr пилав [pilav] ; pilav
  bg пилаф [pilaf] ; pilav
  sq pilaf ; pilav
  ro pilaf ; pilav
  mk пилав [pilav] ; pilav
  el πιλάφι [piláfi] ; pilav
  en pilaf ; pilav
  fr pilaf ; pilav
  ru плов [plov] ; pilav
  hu piláf ; pilav
  fa پلو [polō] ; pilav ; ff:Türkçe pilav Farsça pilāv'dan gelir
  uz palov ; pilav
  az plov ; pilav
@sarma from_turkish
  sr сарма [sarma] ; sarma
  bg сарма [sarma] ; sarma
  sq sarmë ; sarma
  ro sarma ; sarma ; ff:Rumencede sarmale ulusal yemek sayılır
  mk сарма [sarma] ; sarma
  el σαρμάς [sarmás] ; sarma
@lokum from_turkish
  sr ратлук [ratluk] ; lokum ; ff:Sırpçada ratluk, rahat-ı hulkum'un kısalmış biçimidir
  bg локум [lokum] ; lokum
  sq llokum ; lokum
  ro rahat ; lokum ; ff:Rumencede rahat "lokum" demektir; Türkçe rahat ile biçim benzerliği güldürücü bir yalancı arkadaştır
  mk локум [lokum] ; lokum
  el λουκούμι [loukoúmi] ; lokum
  en Turkish delight ; lokum
  fr loukoum ; lokum
@helva from_turkish
  sr алва [alva] ; helva
  bg халва [halva] ; helva
  sq hallvë ; helva
  ro halva ; helva
  mk алва [alva] ; helva
  el χαλβάς [chalvás] ; helva
  en halva ; helva
  ru халва [halva] ; helva
  ar حلوى [ḥalwā] ; tatlı ; ff:Türkçe helva Arapça ḥalwā "tatlı"dan gelir; Arapçada her tatlı için kullanılır
  he חלבה [ḥalva] ; helva
@kadayıf from_turkish
  sr кадаиф [kadaif] ; kadayıf
  bg кадаиф [kadaif] ; kadayıf
  sq kadaif ; kadayıf
  ro cataif ; kadayıf
  mk кадаиф [kadaif] ; kadayıf
  el καταΐφι [kataífi] ; kadayıf
@kaymak from_turkish
  sr кајмак [kajmak] ; kaymak
  bg каймак [kaymak] ; kaymak; köpük
  sq kajmak ; kaymak
  ro caimac ; kaymak; kahve köpüğü ; ff:Rumencede caimac aynı zamanda "kahve köpüğü" demektir
  mk кајмак [kajmak] ; kaymak
  el καϊμάκι [kaimáki] ; kaymak; kahve köpüğü
  ru каймак [kaymak] ; kaymak
  az qaymaq ; kaymak
  kk қаймақ [qaymaq] ; kaymak
  uz qaymoq ; kaymak
  ky каймак [kaymak] ; kaymak
@boza from_turkish
  sr боза [boza] ; boza
  bg боза [boza] ; boza ; ff:Bulgarcada боза aynı zamanda "sıkıcı, tatsız şey" demektir
  sq bozë ; boza
  mk боза [boza] ; boza
  ro bragă ; boza
  en booze ; içki ; ff:İngilizce booze (içki) Felemenkçe būsen'den gelir; boza ile ilgisi tartışmalıdır
@simit from_turkish
  bg симит [simit] ; simit
  sq simite ; simit
  mk симит [simit] ; simit
  el σιμίτι [simíti] ; simit
  sr симит [simit] ; simit
@tulumba from_turkish
  bg тулумба [tulumba] ; tulumba tatlısı
  sq tullumbë ; tulumba
  mk тулумба [tulumba] ; tulumba
  el τουλούμπα [touloúmba] ; tulumba
  sr тулумба [tulumba] ; tulumba
@rakı from_turkish
  sr ракија [rakija] ; rakı; meyve brendisi ; ff:Sırpçada rakija anason içermeyen meyve brendisidir
  bg ракия [rakiya] ; meyve brendisi
  sq raki ; rakı; üzüm brendisi
  ro rachiu ; brendi
  mk ракија [rakija] ; brendi
  el ρακί [rakí] ; rakı
  en raki ; rakı
  fr raki ; rakı
  ar عرق [ʿaraq] ; ter; rakı ; ff:Türkçe rakı Arapça ʿaraq "ter"den gelir; Arapçada arak hem ter hem içkidir
@çakmak from_turkish
  sr чакмак [čakmak] ; çakmak taşı
  bg чакмак [çakmak] ; çakmak
  sq çakmak ; çakmak
  mk чакмак [čakmak] ; çakmak
  az çaxmaq ; çakmak
  kk шақпақ [şaqpaq] ; çakmak
@nal from_turkish
  ar نعل [naʿl] ; nal; ayakkabı ; ff:Türkçe nal Arapça naʿl'dan gelir; Arapçada "ayakkabı" anlamı da vardır
@araba from_turkish
  bg араба [araba] ; araba (eski)
  ro haraba ; büyük at arabası
  ru арба [arba] ; iki tekerlekli at arabası ; ff:Rusçada арба yalnızca "iki tekerlekli yük arabası" demektir
  uk гарба [harba] ; yük arabası
  pl arba ; yük arabası
  az araba ; araba
  kk арба [arba] ; at arabası
  uz arava ; araba
  ky араба [araba] ; araba
  tk araba ; araba
@çizme from_turkish
  sr чизма [čizma] ; çizme
  bg чизма [çizma] ; çizme
  sq çizme ; çizme
  mk чизма [čizma] ; çizme
  ro cizmă ; çizme
  hu csizma ; çizme ; ff:Macarcada csizma geleneksel çizmedir
  pl ciżma ; çizme (eski)
@düğün from_turkish
  az toy ; düğün ; ff:Azerbaycan Türkçesinde düğün için toy kullanılır; düyün "düğüm" demektir
  kk той [toy] ; düğün, şölen
  uz toʻy ; düğün
  ky той [toy] ; düğün, şölen
  tk toý ; düğün
@damga from_turkish
  ru тамга [tamga] ; damga, mühür; vergi ; ff:Rusçada тамга Altın Orda döneminde "mühür ve vergi" anlamını taşımıştır
  uk тамга [tamha] ; damga
  pl tamga ; damga
  mn тамга [tamga] ; mühür, damga
  az damğa ; damga
  kk таңба [tañba] ; damga; simge
  uz tamgʻa ; damga
  ky тамга [tamga] ; damga
@yarlık from_turkish
  ru ярлык [yarlık] ; etiket ; ff:Rusçada ярлык "etiket, yafta" anlamına kaymıştır; Altın Orda hanlarının fermanı anlamından gelir
  uk ярлик [yarlık] ; etiket
@kazak from_turkish
  ru казак [kazak] ; Kazak (Rus Kazağı)
  uk козак [kozak] ; Kazak ; ff:Ukrayna Kazakları (козак) adını Türkçe kazak "özgür, başıboş" sözcüğünden alır
  pl kozak ; Kazak
  en Cossack ; Kazak
  fr cosaque ; Kazak
  hu kozák ; Kazak
  kk қазақ [qazaq] ; Kazak (halk adı)
@ataman from_turkish
  ru атаман [ataman] ; Kazak reisi
  uk отаман [otaman] ; reis
  pl ataman ; Kazak reisi
@kurgan from_turkish
  ru курган [kurgan] ; höyük, kurgan ; ff:Rusçada курган arkeolojide "mezar höyüğü" terimi olmuştur
  uk курган [kurhan] ; höyük
  pl kurhan ; höyük
  en kurgan ; kurgan
  de Kurgan ; kurgan
  hu kurgán ; kurgan
  kk қорған [qorğan] ; kale; koruma ; ff:Kazakçada қорған "kale, savunma" demektir
  az qurğan ; kurgan
@balta from_turkish
  hu balta ; balta
  sr балта [balta] ; balta (ağızlarda)
  bg балтия [baltiya] ; balta
  az balta ; balta
  kk балта [balta] ; balta
  uz bolta ; balta
  ky балта [balta] ; balta
  tk palta ; balta
@kılıç shared_ancestor
  az qılınc ; kılıç
  kk қылыш [qılış] ; kılıç
  uz qilich ; kılıç
  ky кылыч [kılıç] ; kılıç
  tk gylyç ; kılıç
@bıçak shared_ancestor
  az bıçaq ; bıçak
  kk пышақ [pışaq] ; bıçak
  uz pichoq ; bıçak
  ky бычак [bıçak] ; bıçak
  tk byçak ; bıçak
  hu bicska ; çakı ; ff:Macarca bicska (çakı) Türkçe bıçak'tan gelir
@ok shared_ancestor
  az ox ; ok
  kk оқ [oq] ; ok; kurşun ; ff:Kazakçada оқ aynı zamanda "mermi, kurşun" demektir
  uz oʻq ; ok; kurşun
  ky ок [ok] ; ok; kurşun
  tk ok ; ok
@kılavuz from_turkish
  sr калауз [kalauz] ; maymuncuk; kılavuz ; ff:Sırpçada kalauz "maymuncuk anahtar" anlamına kaymıştır
  bg калауз [kalauz] ; kılavuz
  hu kalauz ; biletçi; rehber ; ff:Macarcada kalauz "tren biletçisi, kondüktör" demektir
  ro călăuză ; rehber, kılavuz
@tercüman from_turkish
  hu tolmács ; tercüman ; ff:Macarca tolmács Eski Türkçe tılmaç (dilmaç) sözcüğünden gelir
  ru толмач [tolmaç] ; tercüman (eski)
  pl tłumacz ; tercüman ; ff:Lehçe tłumacz (tercüman) Türkçe dilmaç/tılmaç'tan gelir
  uk тлумач [tlumaç] ; yorumcu
  de Dolmetscher ; sözlü tercüman ; ff:Almanca Dolmetscher, Macarca yoluyla Türkçe tılmaç'tan gelir
  sr тумач [tumač] ; tercüman; yorumcu
  bg тълмач [tılmaç] ; tercüman (eski)
  ro tălmaci ; tercüman
"""
