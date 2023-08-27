# Python'daki bir çok string metodu bulunmaktadır. Bunlara ulaşmak için; https://www.w3schools.com/python/python_ref_string.asp adresine bakılabilir.


message = "Hello There. My name is Kerim DELİL. çğıöü - ÇĞİÖÜ"
# upper() => tüm karakterleri büyük harfe çevirir.
# message = message.upper()

# lower() => tüm karakterleri küçük harfe çevirir.
# message = message.lower()

# title() => tüm kelimelerin sadece baş harflerini büyük yapar.
# message = message.title()

# capitalize() => Cümlenin sadece ilk kelimesinin ilk harfini büyük yapar.
# message = message.capitalize()

# strip() => İfadenin başındaki ve sonundaki boşlukları silmek için kullanılır.
# message = "                Hello There. My name is Kerim DELİL. çğıöü - ÇĞİÖÜ               "
# message = "." + message.strip() + "."

# message = "//   Hello There. My name is Kerim DELİL. çğıöü - ÇĞİÖÜ   //"
# message = "." + message.strip('/').strip() + "."
# Yukarıdaki örnekte ifadenin başındaki hem '//' işaretlerini hem de boşluk karakterleri silinmiştir.

# split() => İfadeyi istenilen karakterden ayırıp bir dizinin içerisine atar. Hiçbir şey yazılmazsa boşluk karakterinden ayırma yapar.

# message = message.split()
# "." dan ifadeyi ayırmak istersek;
# message = message.split(".")

# join() => dizinin elemanlarını aralara istenilen karakter/karakterler konularak birleştirme yapar.
# Örneğimizde öncelikle message değişkeninin içerisindeki ifadeyi boşluk karakterleri ile ayırıp dizi haline getirelim. Daha sonra da dizi halindeki yapıyı aralarına "*" karakteri koyarak tekrar birleştirelim.

# message = message.split()
# print(message)
# message = '*'.join(message)

# find() => İfadenin içerisinde istenilen ifadeyi arar. İlk bulduğunun başlangıç indeks numarasını döndürür.
# indexNumber = message.find('kerim')
# print(indexNumber)

# ! NOT: ARAMA İŞLEMİNDE BÜYÜK KÜÇÜK HARF DUYARLILIĞI UNUTULMAMALIDIR. EĞER ARANAN İFADE YOKSA -1 DEĞERİ DÖNER.

# startswith() => ifadenin istenilen karakter/karakterler ile başlarsa True, başlamazsa False döner.
# isFound = message.startswith('H')
# isFound = message.startswith('C')
# print(isFound)

# endswith() => ifadenin istenilen karakter/karakterler ile bitiyorsa True, bitmiyorsa False döner.
# isFound = message.endswith('Ü')
# isFound = message.endswith('ü')
# print(isFound)

# replace() => Verilen ifadede istenilen karakteri arar, bulduğu karakter yerine konulması istenilen karakteri koyar.
# Örnek: message değişkenindeki boşluk karakterleri yerine "---" ifadesi koyduralım.
# message = message.replace(' ','---')
# NOT: iç içe de replace() metodu kullanılabilir.

# message = message.replace('ç','c').replace('ü','u').replace('ı','i').replace('ö','o').replace('ğ','g')
# Yukarıdaki örnekte Türkçe karakterler ingilizce karakterlere çevrilmiştir.

# cenrter() => Verilen ifadeyi istenilen karakter sayısı içerisinin tam ortasına yazmayı ve başına ve sonuna da istenilen karakterlerin gelmesini sağlar.

# message ="." +  message.center(100) + "."
# message ="." +  message.center(100,'*') + "."

print(message)