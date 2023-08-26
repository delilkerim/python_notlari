# python'da istenilen değerlerin istenilen şekilde gösterilmesi için bir çok yol vardır.

name = "Kerim"
lastName = "DELİL"
age = 43
city = "ESKİŞEHİR"

result = "Hi. My name is " + name + " " + lastName + ". I'am " + str(age) + " years old. I live in " + city
print(result)

# Yukarıdaki ifadeyi format metodu ile de yazabiliriz. 
result = "Hi. My name is {} {}. I'am {} years old. I live in {}".format(name, lastName, age, city)
print(result)

# format metodunda string ifadenin içerisindeki her bir süslü parantez aslında sıfırdan başlayan bir indeksleme işlemine gider. format ifadesinde yazılan sıraya göre de indeks değerlerine, istenilen değerler gönderilmiş olur.
result = "Hi. My name is {1} {0}. I'am {2} years old. I live in {3}".format(name, lastName, age, city)
print(result)
# yukarıdaki gibi örneği değiştirecek olursak; 1. indekse name, 0. indekse lastName, 2. indekse age ve 3. indekse ise city değişkenlerinin değerleri gönderilmiş olur.

# format metodunda süslü parantezlere etiketler tanımlayarak sıranın önemini pas geçebiliriz.
result = "Hi. My name is {n} {l}. I'am {a} years old. I live in {c}".format(c=city, a=age, l=lastName, n=name)
print(result)

# format metodunda float türünde virgülden önce ve sonra gösterilecek hane sayısını belirtmek için; 1.3 dersek tam sayı kısmı 1 hane, ondalıklı kısım ise 3 hane olacak şekilde yaz anlamına gelir. Ondalıklı kısım 3 hane olarak yazılırken 4. hanenin 5'e eşit veya büüyk olma durumuna göre 3. hane aşağıya veya yukarıya yuvarlanır.
result = 200/700
print("Sonuç:{0:2.5}".format(result))

# format metodunun haricinde f string metodu da vardır. Bu metot ile daha kolay değişkenlerimizi string ifadelerin içerisinde gösterebiliriz.
result = f"Hi. My name is {name} {lastName}. I'm {age} years old. I live in {city}."
print(result)

