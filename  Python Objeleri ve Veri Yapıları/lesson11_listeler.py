# Python'da listeler [] köşeli parantezler içerisinde değer alırlar. Boş bir liste oluşturmak için;
# myList=[]
# print(type(myList))

# Önemli: Listelerin içerisinde illaki aynı türden veri olmak zorunda değildir.
# myList = [1,2,12.23, True, 'Ahmet','Selim',[12,34]]
# print(myList)

# Karakter dizileri de bir liste(dizi) olduğu için string ifadelerdeki tüm işlemleri burada da yapabiliriz.

# Listeleri birbiri ile toplayabiliriz.
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

# listelerin uzunluğunu bulabiliriz.
print(len(list3))

# listenin elemanlarına indeks numarası ile erişebiliriz.
print(list3[3])

# listenin içerisine 1,2,3 şeklinde eleman ekleyebildiğimiz gibi [[1,2,3],[3,4,5]] şeklinde listelerde sakyalabiliriz.
productA = ['televizyon','Lg']
productB = ['telefon','samsung']
products1 =productA + productB
products2 = [productA, productB]
print(products1, products2)

# iç içe listelerdeki elemanlara ulaşmak için yine iç içe indeks numaralarından yararlanılır.
print(products2[0][0])
# Yukarıdaki kodun açıklaması products2 dizisinin 0. elemanı yani productA'ya ulaş. Oradan da 0. elemanına yani 'televizyon'a ulaş.

