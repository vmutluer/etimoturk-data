# EtimoTürk Açık Veri / EtimoTürk Open Data

[EtimoTürk](https://github.com/vmutluer) iOS uygulamasının etimoloji veritabanı ve onu üreten veri hattı.
Veri **CC BY-SA 4.0**, betikler **MIT** lisansıyla sunulur (bkz. [LICENSE.md](LICENSE.md), [ATTRIBUTION.md](ATTRIBUTION.md)).

*The etymology database behind the EtimoTürk iOS app and the pipeline that builds it. Data: CC BY-SA 4.0; scripts: MIT.*

## İçerik

| Yol | Açıklama |
|---|---|
| `data/etymoturk.sqlite` | Uygulamanın kullandığı veritabanı (şema 4, FTS5). 17.246 sözcük (11.272 denetlenmiş künye, 825 tanıklanmış türetme, 5.149 Wiktionary kaydı), 1.351 kök ailesi, 12.446 "uluslarla ortak sözcük" (28 dil), 291 yer adı, 325 deyim kökeni — Türkçe ve İngilizce |
| `data/etymoturk.json` | Aynı verinin JSON yedeği |
| `data/denetim_raporu.csv` | Son içerik denetiminin şüpheli kayıt listesi (inceleme için uyarılar) |
| `DataPipeline/` | Korpuslar (`corpora/*.py`, `etymodata/*.py`), İngilizce çeviriler (`english/*.tsv`), Wiktionary ETL, `build_database.py`, biçimsel doğrulayıcı `validate_corpora.py`, içerik denetçisi `audit_database.py` |

## Veri katmanları

| `words.data_source` | Kaynak | Lisans |
|---|---|---|
| `curated` | Elle yazılmış korpuslar: kaynak dil, kaynak biçim, anlam, dönem, kök ailesi, ses zinciri — telife tabi olmayan dilbilimsel olgular; künye cümleleri şablonla üretilir | CC BY-SA 4.0 (bu depo) |
| `derived` | Kural tabanlı yapım eki türetmeleri; yalnızca açık lisanslı sözlükte madde başı olarak tanıklananlar | CC BY-SA 4.0 (bu depo) |
| `wiktionary` | Kaikki.org (wiktextract) Türkçe Wiktionary dökümünden yapısal etimoloji olguları ve İngilizce anlamlar | CC BY-SA 4.0 (Wiktionary katkıcıları) |

Wiktionary kökenli kayıtlar filtrelenmiş, bu şemaya dönüştürülmüş ve içerik denetimiyle düzeltilmiştir; özgün metinlerle
birebir aynı değildir. CC BY-SA 4.0'ın 4(b) maddesi gereği bu veritabanının tamamı aynı lisansla paylaşılır.

## Yeniden üretme ve denetim

```bash
python3 DataPipeline/validate_corpora.py     # biçimsel denetim (0 hata beklenir)
python3 DataPipeline/build_database.py       # data/etymoturk.sqlite ve .json üretir
python3 DataPipeline/audit_database.py --report data/denetim_raporu.csv   # içerik denetimi (0 hata beklenir)
```

Python 3.10+, ek bağımlılık yok. Wiktionary katmanını yenilemek için `etl_wiktionary.py` kullanılır; Kaikki.org'un
JSONL dökümü "deprecated" olarak işaretlendiğinden kaynak adresi güncellenmelidir.

## Uygulamaya aktarma

Bu depo verinin tek kaynağıdır. EtimoTürk uygulama deposundaki `Scripts/update_database.sh`, bu depoyu çekip
`validate_corpora.py` → `build_database.py --data-commit <sha>` → `audit_database.py` zincirini çalıştırır ve yalnızca
denetim sıfır hata verirse üretilen `etymoturk.sqlite` dosyasını `App/Resources/` altına kopyalar. Veritabanının `meta`
tablosundaki `data_commit` anahtarı hangi commit'ten üretildiğini gösterir.

## Düzeltme göndermek

Yanlış ya da eksik bir köken için **Issue** açın ya da ilgili korpus satırını düzelten bir **Pull Request** gönderin
(`lemma|pos|origin|kaynak biçim|anlam|dönem|aile|zincir`; `?` kökenin tartışmalı olduğunu işaretler). Her PR'da
`validate_corpora.py` ve `audit_database.py` sıfır hata vermelidir.

Kök ailesi kodları Arapça kök harflerini Latin harfleriyle verir; **ḥ/ḫ/h, q/k, ṣ/ṯ/s, ḍ/ḏ/z, ʿ/ʾ gibi farklı
harfleri aynı koda toplamayın** (`H-Y-R` ḥ-y-r "şaşırmak", `Ḫ-Y-R` ḫ-y-r "iyilik"). Aynı kodu iki ayrı kök için
kullanmak üyeleri birbirine karıştırır; `validate_corpora.py` bunu hata olarak, kaynak biçimi kök harflerine uymayan
üyeyi de uyarı olarak bildirir.

## Güvenilirlik notu

Veri 2026-11-01 tarihli içerik denetiminden geçmiştir (curated ↔ Wiktionary köken uyumu %94,1; kalan farklar yakın/uzak
kaynak ayrımıdır). `historical_attestation` alanı gerçek ilk tanıklanma değil, dönem etiketidir; deyim köken anlatıları
yalnızca yazılı kaynağa dayananlarda "kesin" etiketlidir. Kök ailesi üyeliklerinin tamamı (1.351 aile, ~6.500 üyelik)
2026-11-01'de elle gözden geçirilmiş; aynı koda toplanan farklı Arapça köklerden doğan 30 karışma ve 7 Yunanca/Latince/
Türkçe yanlış bağlantı ayrılmıştır (örn. kubbe ≠ kebap, akor ≠ kordon, taksimetre ≠ taktik, hayır ≠ hayret). Hataları bildirmeniz veriyi herkes için iyileştirir.
