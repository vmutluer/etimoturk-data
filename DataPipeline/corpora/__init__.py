"""Modüler veri üretim korpusları.

Bu paketteki her modül şu değişkenlerden bir ya da birkaçını dışa açar:
  WORDS     – sözlük satırları  (lemma|pos|origin|kaynak biçim|anlam|dönem|aile|zincir)
  FAMILIES  – kök ailesi satırları (kod|dil|çekirdek anlam|açıklama)
  COGNATES  – ortak sözcük DSL'i (@lemma yön / kod biçim [okunuş] ; anlam ; ff:not)
build_database.py bu modülleri otomatik yükler; `generated/` altındaki JSON dosyaları ETL çıktılarıdır.
"""
