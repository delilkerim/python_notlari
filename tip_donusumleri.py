# Python'da tip dönüşümleri
# --------------------------------------------------------------------------------------------
# int() => integer türüne dönüştürür.
# a = "23"
# a= 213.34
# result = int(a)
# print(type(result))

# ! NOT: EĞER DÖNÜŞTÜRTÜLECEK OLAN DEĞERİN HER HANGİ BİR YERİNDE HARF OLURSA PYTHON HATA VERİR.
# --------------------------------------------------------------------------------------------
# float() => float türüne dönüştürür.
# b = 23
# result = float(b)
# print(result)  

# --------------------------------------------------------------------------------------------
# str() => String türüne dönüştürür.
# a = 23
# result = str(23)
# print(type(result))

# --------------------------------------------------------------------------------------------
# bool() => Bool türüne dönüştürür.
isim =0
result = bool(isim)
print(result)
# ! NOT: SAYISAL SİSTEMLERDE 0 BOOL DÖNÜŞÜMÜ FALSE, DİĞER TÜM SAYILAR İÇİN TRUE OLMAKTADIR.
# ! NOT: STRING TÜRLERİNDE İÇERİSİ BOŞ İSE FALSE, DİĞERLERİNDE TRUE OLMAKTADIR.

