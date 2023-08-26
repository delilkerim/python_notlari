# Aşağıdaki soruları işlediğiniz karakter dizileri konusuna göre cevaplamaya çalışınız.
webSite = "http://www.kerimdelil.com.tr"
course = "Python kursunu çok seveceksiniz. Python ile yazılım yazmak pc ile konuşmak gibidir."

# 1- 'course' karakter dizisinde kaç karakter vardır?
# 2- 'webSite' içinden www karakterlerini alan kodu yazınız.
# 3- 'webSite' içinden "com" karakterlerini alan kodu yazınız.
# 4- 'course' karakter dizisinin ilk 15 ve son 15 karakterlerini alınız.
# 5- 'course' ifadesindeki karakterleri tersten yazdırınız.

name, surname, age, job = 'kerim','delil',43,'teknik öğretmen'

# 6- Yukarıda verilen değişkenler ile aşağıdaki ifadeyi yazdırınız.
# "Benim adım kerim delil, yaşım 43 ve mesleğim teknik öğretmen."
# 7- "Hello world" ifadesindeki "w" harfini "W" harfine çeviriniz.
# 8- "abc" ifadesini yan yana 3 kere yazdırınız.



# --------------------------CEVAPLAR--------------------------
# 1-
# result = len(course)
# print(result)
# --------------------------

# 2-
# result = webSite[7:10]
# print(result)
# --------------------------

# 3-
# result = webSite[-6:-3]
# print(result)
# --------------------------

# 4- 
# result = course[:15]
# result += course[-15:]
# print(result)
# --------------------------

# 5- 
# result = course[::-1]
# print(result)
# --------------------------

# 6-
# result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}."
# print(result)
# --------------------------

# 7-
# writing = "Hello world"
# result = writing[0:6] + 'W' + writing[-4:]
# print(result)
# --------------------------

# 8-
print("abc"*3)

