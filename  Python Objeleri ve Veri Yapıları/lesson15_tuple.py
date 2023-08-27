# Python'da tuple'lar aynı listeler gibidir. Tek farkı listelelerin elemanlarını değiştirebiliriz, ama tuple'ların elemanlarını değiştiremeyiz. Anca sıfırdan eleman yükleyebiliriz.
# tuple tanımlamak için ya () yada hiç bir şey koymadan değer atanabilir.
# tuple1 = (1,2,3,4)
# print(type(tuple1))

# tuple2 = 5,6,7,True, 34.23
# print(type(tuple2))

tuple = (1,2,3,4,5,4,23,34,21,2,4,3,2)

# tuple'da çok fazla bir metot yoktur. Ayrıntı için; https://www.w3schools.com/python/python_ref_tuple.asp adresine bakabilirsiniz.

# count() => tuple listesinin içerisinde aranan değerden kaç tane olduğunu döndürür. Yoksa 0 sıfır döndürür.
# print(tuple.count(2))

# index() => tuple listesinde aranan değerin indeks numarasını döndürür. Bulduktan sonra diğer değerlere bakmaz.
print(tuple.index(2)) 

