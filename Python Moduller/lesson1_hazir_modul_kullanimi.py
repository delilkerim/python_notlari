# Modül nedir? Programlarımız büyüdükçe bunları parçalara ayırmamız çok mantıklıdır. Böylece yoğun kod kalabalığından ve hata yapma olasılığından kurtulmuş oluruz. Sadece istenilen parçada müdahele ederek daha sağlam kodlar yazılabilir. Bunun için Python'da modüller oluşturabiliriz veya oluşturulmuştur. 
# Modüller 2 çeşit olmaktadır.
# 1- Kendimizin yazdığı modüller
# 2- Hazır Modüller: Hazır modüller de 2 ye ayrılır.
# 2-a) Standart Kütüphane modülleri
# 2-b) Üçüncü Şahıs modülleri (https://pypi.org/ adresinden bakabiliriz. )


# HAZIR MODÜLLERİ IMPORT EDERKEN 2 YÖNTEM KULLANILIR. 
# ! 1. YÖNTEM
# -------------------------------------------------------------------------------------------------
# Şimdi biz hazır modüllerin standart Kütüphane modüllerinden math modülünü(kütüphanesini) inceleyelim :)
# math modülünü dosyamıza dahil etmek için "import" ifadesini kullanırız.
# -------------------------------------------------------------------------------------------------
# import math
# Yukarıdaki kodun açıklaması: math modülünün içerisindeki herşeyi dosyamıza (dolaylı olarak projemize) dahil etmiş olduk.

# dahil edilen modülün içerisindeki metotları listelemek için
# values = dir(math)
# print(values)

# dahil edilen modülün metotları hakkında daha geniş bir bilgi almak istersek;
# values = help(math)
# print(values)

# dahil edilen modülün sadece istenilen metodu hakkında bilgi almak istersek;
# value = help(math.ceil)
# print(value)
# -------------------------------------------------------------------------------------------------

# import modül_adi     yerine; import modül_adi as ma şeklinde modül ismine takma ad da takılabilir.
# import math as islem

# value = islem.ceil(3.08)
# print(value)

# ! 2. YÖNTEM
# -------------------------------------------------------------------------------------------------
# from modul_adi import * [metotadlari]
# from math import *
# Yukarıdaki kodun anlamı math modülündeki herşeyi dahil et anlamındadır.
# "import math"  arasındaki fark ise; "import math" 'de metotları kullanmak için önce modülün adı, sonra ".", sonra da metodun adını yazmak zorundayız. "from math imporrt *" ifadesinde ise direk metotudu yazabiliriz.
# value = ceil(23.45)
# print(value)

# -------------------------------------------------------------------------------------------------
# from math import factorial, ceil,sqrt
# Yukarıdaki kodun anlamı: math modülünden sadece factorial, ceil ve sqrt metotlarını dahil et.
# value = factorial(26)
# print(value)

# -------------------------------------------------------------------------------------------------
# Dahil edilen bir modüldeki metotun aynı ismiyle kendimiz bir metot yazarsak hangisi çalışır?
# CEVAP: Yukarıdan aşağıya sıralamada hangi metot en sonda ise o baskın olur.

