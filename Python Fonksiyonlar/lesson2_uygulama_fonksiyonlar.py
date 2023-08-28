# Python'da fonksiyonların pekiştirilmesi için uygulamalar
# 1- Gönderilen bir kelimeye belirtilen sayıda ekrana yazdıran fonk. yazınız.

# def displayWord(word,count):
#     for i in range(count):
#         print(word)
# displayWord('kerim',10)
# -----------------------------------------------------------------------------------------------------

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonk. yazınız.
# def makeList(*args):
#     list = []
#     for n in args:
#         list.append(n)
#     return list

# list1 = makeList(1,2,45,6,7,6577,5756,756,7,767567,567,567,543,23,34,324,453)
# print(type(list1))
# print(list1)
# -----------------------------------------------------------------------------------------------------

# 3- Gönderilen iki sayı arasındaki asal sayıları bulan fonksiyonu yazınız.

# def convert(list):
#     return tuple(list)

# def asalSayiBul(sayi1, sayi2):
#     asalSayilar =[]
#     for sayi in range(sayi1, sayi2+1):
#         if sayi>1:
#             for s in range(2,sayi):
#                 if (sayi % s == 0):
#                     # print('asal değil')
#                     break
#             else:
#                     # print('asal')
#                 asalSayilar.append(sayi)
#                 print(sayi)
#     return asalSayilar
   
# print(asalSayiBul(10,30))
# -----------------------------------------------------------------------------------------------------

# 4- Kendisine gönderilen bir sayının tam bölenlerini bulup, döndüren fonk. yazınız.

def tamBolenleriSayisi(sayi):
    list = []
    for i in range(2, sayi+1):
        if (sayi % i == 0):
            list.append(i)
    return list

print(tamBolenleriSayisi(100))