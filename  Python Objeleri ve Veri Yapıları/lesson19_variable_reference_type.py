# Python'da değişkenler 2 şekilde saklanırlar. 
""" 1- Variable Type: number ve string türünden değişkenler variable type olarak saklanırlar. Yani her yeni değişken tanımlandığında RAM'da bir adres alanı açılır ve değer oraya kaydedilir.
2- Reference Type: listeler, sınıflar bu türdendir. Bir liste veya sınıftan bir nesne oluşturulduğunda RAM'de bir adres açılır. Eğer başka bir liste oluşturulup değeri önceki listeden alınırsa veya sınıftan nesne tekrar üretilirse aslında RAM'de yeni bir adres oluşturmak yerine önceki listenin veya sınıfın adresine referans verilir. Böylece RAM'da fazla bellek kullanımının önüne geçilmiş olur. """

x = 3
y = 10
x = y
y = 20
print(x,y)

listA = [1,2,3,4]
listB = [11,12,13,14]
listA = listB
listB[0]= 100
print(listA, listB)