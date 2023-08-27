website = "http://www.kerim.delil.com.tr"
course = "Python çok güzel bir dil. Konuşur gibi yazılım yazmak çok güzel"

# 1- "  Hello World  " ifadesinin başındaki ve sonundaki karakterleri siliniz.
# result = "  Hello World  "
# result = "." + result.strip() + "."
# print(result)
# ----------------------------------------------------------------------------------------------------

# 2- "www.kerimdelil.com" ifadesinin içindeki kerimdelil bilgisi haricindeki her karakteri siliniz.
# result = "www.kerimdelil.com" 
# result = result.strip('w.com')
# print(result)
# ----------------------------------------------------------------------------------------------------

# 3- 'course' karakter dizisinin tüm harflerini küçük harf yapınız.
# course = course.lower()
# print(course)
# ----------------------------------------------------------------------------------------------------

# 4- "website" karakter dizisinin içerisinde kaç tane "a" harfi vardır. (count('a'))
# result = website.count('e')
# print(f"{website} ifadesinin içerisinde toplam a karakterinden {result} adet vardır.")
# ----------------------------------------------------------------------------------------------------

# 5- 'website' karakter dizisi 'www' ile başlayıp 'tr' ile bitiyor mu?
# isFound = website.startswith('www')
# isFound = website.endswith("tr")
# şeklinde şu an için tek tek bakabiliriz.
# ----------------------------------------------------------------------------------------------------

# 6- 'website' karakter dizisinin içerisinde ".com" ifadesi var mı?
# indexNumber = website.find('.com')
# print(indexNumber)
# ----------------------------------------------------------------------------------------------------

# 7- 'course' karakter dizisinin içerisindeki tüm karakterler alfabetik mi? (isalpha, isgidit)
# isAlphabetic = course.isalpha()
# isAlphabetic = "merhaba*".isalpha()
# print(isAlphabetic)
# ! NOT: isalpha() metodunda boşluk karakteri ve özel karakterler harf olarak kabul edilmezler!
# ----------------------------------------------------------------------------------------------------

# 8- 'contents' ifadesini satırda 50 karakter içerisine yerleştirip başlarına ve sonuna "*" işareti koyunuz.
# print('contents'.center(50,'*'))
# ----------------------------------------------------------------------------------------------------

# 9- 'course' karakter dizisindeki tüm boşluklar yerine "-" işareti koyunuz.
# result = course.replace(' ','-')
# print(result)
# ----------------------------------------------------------------------------------------------------

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' ile değiştiriniz.
# result = 'Hello World'
# result = result.replace('World','There')
# print(result)
# ----------------------------------------------------------------------------------------------------

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırınız.
result = course.split()
print(result)
