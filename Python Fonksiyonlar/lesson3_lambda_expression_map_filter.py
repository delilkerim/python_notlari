# Python'da bir fonk. bilindiği gibi çağrılır ve çalıştırılır. Örnek: sayıların karesini alan bir fonk. yazalım.

# def square(num):
#     return num**2
# print(square(5))

# Python'da tek satır çalıştırılan fonk. tanımıyla birlikte tek satırda da yazabiliriz.
def square(num): return num**2

# Elimizde bir dizimiz olsun. Bu elemanların karelerini alıp bir listede tutmak isteyelim.
# 1. Yol:
numbers = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# for num in numbers:
#     list2.append(square(num))

# print(list2)
# 2. Yol:
# list2 = list( map(square,numbers) )
# print(list2)

# map metodu dizilerin içerisindeki elemanların tek tek istenilen fonksiyona gönderilmesini sağlar ve geriye list metodu ile de bir liste dönmüş olur.

# map() metodunun içerisinde bir fonk. çağırabildiğimiz gibi direk fonk. kodlarını da yazabiliriz. Bu tür fonk. "anonymous function" denilir. Sadece başına bir de "lambda" ifadesini yazmak zorunludur.

# list2 = list(map(lambda num: num**2, numbers))
# print(list2)

# Bazı yerlerde "lambda num: num**2" ifadesinin bir değişkene tanımlandığını o ifade yerine değişken isminin geçtiğini de görebilirsiniz. Python'da yapılan işlem sonucu aslında değişken artık bir fonk. gibi davranmaktadır.

# kareAl = lambda num: num**2
# list2 = list( map(kareAl, numbers) )
# print(list2)
# -----------------------
# map() metodunda dizinin tüm elemanlarına bakılıp aynı fonksiyonda işlem yaptırılmaktadır. Filter() metodundan ise istenilen şartları sağlayan değerler için sadece fonksiyon çağırılabilir. Buyrun görelim :)

# Örnek numbers dizisindeki sadece tek sayıların karelerini almak istersek;
# list2 = list( map(lambda num:num**2, list( filter(lambda num:num%2==1, numbers) ) ) )
# print(list2)

cities = ['eskişehir','aydın','izmir','ankara','istanbul','hakkari','urfa']
# Yukarıdaki cities dizisinde, sadece harf sayısı en fazla 5 olan şehirlerin başlarına yıldız işareti koymak için;

selectedCities = list( map( lambda c:'*'+c, list( filter( lambda c: len(c)<=5, cities ) ) ))
print(selectedCities)