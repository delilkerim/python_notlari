# Python'da gördüğümüz liste metotları ile ilgili pekiştirme uygulamasıdır.
names = ['Ahmet','Mehmet','Ali','Veli','Ayşe','Aslı']
years = [2000,2005,1998,2003,2001,1990]

# 1- "Celal" ismini listenin sonuna ekleyiniz.
names.append("Celal")
# print(names)
# ------------------------------------------------------------------------------------------------------------

# 2- "Selim" ismini listenin başına ekleyiniz.
# names.insert(0,'Selim')
# print(names) 
# ------------------------------------------------------------------------------------------------------------

# 3- 'Ali' ismini listeden siliniz.
# print(names)
# names.remove('Ali')
# print(names)
# ------------------------------------------------------------------------------------------------------------

# 4- 'Veli' isminin indeks numarasını bulunuz.
# print(names)
# indexNumber = names.index('Veli')
# print(indexNumber)
# ------------------------------------------------------------------------------------------------------------

# 5- 'Ali' listenin bir elemanı mıdır?
# isThere = 'Ali' in names
# print(isThere)
# ------------------------------------------------------------------------------------------------------------

# 6- Listenin elemanlarını ters çeviriniz.
# print(names)
# names.reverse()
# print(names)
# ------------------------------------------------------------------------------------------------------------

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
# print(names)
# names.sort()
# print(names)
# ------------------------------------------------------------------------------------------------------------

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
# years.sort()
# print(years)
# ------------------------------------------------------------------------------------------------------------

# 9- str = "Ankara, Eskişehir" karakter dizisini listeye ekleyiniz.
# str = "Ankara, Eskişehir"
# print(names)
# names.append(str.replace(' ','').split(','))
# print(names)
# ------------------------------------------------------------------------------------------------------------

# 10- years dizisinin en büyük ve en küçük elemanı nedir?
# print(min(years), max(years))
# ------------------------------------------------------------------------------------------------------------

# 11- years dizisinde kaç tane 2000 değeri vardır?
# print(years)
# print(years.count(2000))
# ------------------------------------------------------------------------------------------------------------

# 12- years dizisinin tüm elemanlarını siliniz.
# print(years)
# years.clear()
# print(years)
# ------------------------------------------------------------------------------------------------------------

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
# marks = []
# marks.append(input('Marka giriniz:'))
# marks.append(input('Marka giriniz:'))
# marks.append(input('Marka giriniz:'))
# print(marks)
