# DataPipeline

`python3 build_database.py [--out App/Resources]` — şema sürümü 4; her tabloda Türkçe alanların yanında `*_en` İngilizce alanları üretilir (`meta.languages_supported = tr,en`).

| Dosya | İçerik |
|---|---|
| `etymodata/languages.py` | Köken dili sınıfları (renk), karşılaştırma dilleri (bayrak, bölge, alfabe), dönem/kayıt tabloları |
| `etymodata/root_families.py` | Kök aileleri: Öz Türkçe (`*kör-`), Arapça sülasi (`K-T-B`), Farsça öğeler (`-hāne`), Hint-Avrupa (`specere`) |
| `etymodata/lexicon_*.py` | Sözcük listeleri: `lemma|pos|origin|kaynak biçim|anlam|dönem|aile|zincir` |
| `etymodata/cognates_*.py` | Uluslarla ortak sözcükler DSL'i (`@lemma yön` + `kod biçim [okunuş] ; anlam ; ff:not`) |
| `etymodata/derivation.py` | Ünlü uyumu / ünsüz benzeşmesiyle kural tabanlı yapım eki türetimi |
| `etymodata/templates.py` | SQL şeması ve özgün künye şablonları |
| `etymodata/samples.py` | Metin Röntgeni örnek metinleri |
| `etymodata/phase4.py` | Faz 4 meta verileri: yer adı köken dilleri (Hititçe, Luvice, Urartuca…), bölgeler, yer adı türleri, deyim alanları ve güven düzeyleri |
| `etymodata/phase4_rows.py` | Yer adı ve deyim kayıtlarını özgün şablon metinleriyle satıra çeviren üreticiler |
| `etymodata/templates_en.py` | Akademik İngilizce künye / kök ailesi / yer adı / deyim şablonları (Faz 6) |
| `etymodata/english_vocab.py` | Köken dili, dönem, kayıt, bölge, tür, alan ve güven adlarının denetimli İngilizce karşılıkları |
| `etymodata/english_loader.py` | `english/*.tsv` çevirilerini ve `corpora/generated/glosses_en.json` anlamlarını yükler (`EnglishData`) |
| `english/*.tsv` | Elle çevrilmiş İngilizce metinler: `source_meanings_*` (kaynak anlamı), `cognate_meanings_*`, `false_friends_*`, `families_*`, `toponyms_*` (anlam + hikâye), `idioms_*` (anlam + kelimesi kelimesine + hikâye) — sekmeyle ayrılmış, ilk sütun anahtar |
| `etl_glosses.py` | Kaikki.org Türkçe Wiktionary dökümünden İngilizce anlamları (gloss) çıkarır → `corpora/generated/glosses_en.json` (CC BY-SA 4.0 atfı `meta.glosses_attribution`); `python3 -I` ile çalıştırın |
| `audit_database.py` | **İçerik denetçisi**: üretilmiş SQLite'ı curated↔Wiktionary çapraz kontrolü, harf-sezgisi kökeni, tanıklanmamış türetme, ortak sözcük yönü/çeviri çifti, deyim güven düzeyi, zincir artefaktı, koordinat ve bütünlük açısından ölçer; `--report` ile şüpheli kayıt CSV'si; çıkış kodu 0 = eşikler sağlandı |
| `etymodata/audit_rules.py` | Üretim sırasında uygulanan denetim kuralları: satır düzeyinde geçiş yönü (`resolve_direction`) ve gerekçeli dışlama listesi (`EXCLUDED_COGNATES`) |
| `validate_corpora.py` | Tüm korpus bloklarını veritabanı üretmeden denetler (`--module ad` ile tek modül); İngilizce kapsamı (kök ailesi / yer adı / deyim çevirileri zorunlu, kaynak anlamı uyarı) raporlar; çıkış kodu 0 = hata yok |

Köken kodunun sonundaki `?` (`hy?`) kökenin tartışmalı olduğunu işaretler. `python3 build_database.py` sonrasında `python3 audit_database.py` çalıştırın; sıfır hata beklenir.

## Korpuslar ve ETL

| Dosya | İçerik |
|---|---|
| `corpora/gunluk_yasam.py` | Ev, giyim, alışveriş, ulaşım, meslek, zaman, beden, sağlık, aile sözcükleri |
| `corpora/toplum_bilim.py` | Devlet, hukuk, ekonomi, din, eğitim, matematik/fizik, bilişim, sanat |
| `corpora/eylem_sifat.py` | Günlük eylemler, sıfatlar, zarflar (ağırlıkla öz Türkçe kökler) |
| `corpora/kok_aileleri_ek.py` | 35 ek kök ailesi (`FAMILIES`) ve üyeleri (`WORDS`) |
| `corpora/ortak_sozcukler_ek.py` | Ek ortak sözcük kayıtları ve yalancı arkadaşlar (`COGNATES`) |
| `corpora/bilim_teknoloji.py` … `corpora/ev_esya_zanaat_giyim.py` | Faz 4 alan korpusları (bilim, hayvan/bitki, ekonomi, askerlik/Osmanlı kurumları, din/tasavvuf, coğrafya/iklim, duygu/karakter, ev eşyası/zanaat/giyim) |
| `corpora/yer_adlari_iller_a.py`, `_b.py` | 81 ilin yer adı kayıtları (`TOPONYMS` DSL'i), plaka 01–41 / 42–81 |
| `corpora/yer_adlari_ilceler_a.py`, `_b.py` | 210 tarihî ilçe, semt, antik kent, ada, boğaz, göl, dağ ve nehir kaydı |
| `corpora/deyimler_kokeni_a.py`, `_b.py` | 325 deyim / atasözü / tabir köken kaydı (`IDIOMS` DSL'i), 18 alan |
| `corpora/generated/wiktionary_tr.json` | `etl_wiktionary.py` çıktısı (yapısal olgular; CC BY-SA 4.0 atfı) |
| `etl_wiktionary.py` | Kaikki.org dökümünü indirir/ayrıştırır/doğrular; `cache/` gitignore'dadır |

Yeni bir korpus eklemek için `corpora/` altına `WORDS`, `FAMILIES`, `COGNATES`, `TOPONYMS` ya da `IDIOMS` dizesi
dışa açan bir `.py` dosyası koymak yeterlidir; `build_database.py` modülleri ada göre sıralı yükler, aynı
`(lemma, pos)` / kök ailesi kodu / yer adı / deyim için ilk kayıt kazanır; üyesi kalmayan kök aileleri tabloya alınmaz.

## Faz 4 kayıt DSL'leri

```
@Kayseri|il|Kayseri|İç Anadolu|38|hit            # ad|tür|il|bölge|plaka|köken dili
chain: hit:Mazaka>el:Mázaka / Eusébeia>la:Caesarea>ar:Qayṣariyya>sel:Kayseriyye>ota:Kayseri>tr:Kayseri
era: Hitit dönemi (MÖ 2. binyıl)
meaning: ...        story: ...        source: Strabon, Geographika XII        coords: 38.7312,35.4787

@göz boyamak|deyim|zanaat                        # deyim|tür|alan
meaning: ...   literal: ...   story: ...   era: OSM   source: Lehce-i Osmânî (1876)   words: göz, boyamak   confidence: olası
```
Türler, bölgeler, köken dilleri, alanlar ve güven düzeyleri `etymodata/phase4.py` içinde tanımlıdır.
