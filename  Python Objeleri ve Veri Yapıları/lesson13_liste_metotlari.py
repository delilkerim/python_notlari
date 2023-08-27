# Python dilinde bir çok liste metodu vardır. Daha fazla ayrıntı için; https://www.w3schools.com/python/python_ref_list.asp adresine bakılabilir.

# min() => dizi içerisindeki en küçük elemanı bulur. Dizi rakamlardan oluşuyorsa en küçük rakamı, harflerden oluşuyorsa alfabetik olarak en küçük harfi bulur. (NOT: Türkçe karakterleri bulamıyor!!!)

numbers = [4,2,4,5,2,9,10]
letters = ['ç','d','ğ','z','c']

# print(min(numbers))
# print(min(letters))

# ------------------------------------------------------------------------------------------------------------
# max() => Dizi içerisindeki en büyük elemanı bulur.
# print(max(numbers))

# ------------------------------------------------------------------------------------------------------------
# istenilen indeksler arasındaki değerleri karakter dizilerindeki gibi alabiliriz. Son yazılan dahil değildir.
# print(numbers[2:5])

# ------------------------------------------------------------------------------------------------------------
# append() => Listenin sonuna yeni eleman eklemek için kullanılır. 
numbers.append(12)
# print(numbers)

# ------------------------------------------------------------------------------------------------------------
# insert() => Listenin istenilen indeks'ine eleman eklemek için kullanılır. Eleman eklendiği zaman eski indeks'deki eleman bir sağa kayar.
numbers.insert(2,34)
# print(numbers)
# ------------------------------------------------------------------------------------------------------------

# pop() => Listenin son elemanını veya istenilen indeksindeki elemanı silmek için kullanılır. Parantezlerin içerisi boş ise son eleman silinir.
# print(numbers)
# numbers.pop()
# print(numbers)
# ------------------------------------------------------------------------------------------------------------

# remove() => Listenin istenilen elemanının değerini vererek silme işlemi yapar. İlk bulduğu değeri siler. 
# print(numbers)
# numbers.remove(4)
# print(numbers)
# ------------------------------------------------------------------------------------------------------------

# # sort() => Listeyi küçükten büyüğe doğru sıralar. Türkçe karakterler sıralamaya girmez!!!
# numbers.sort()
# print(numbers)
# letters.sort()
# print(letters)
# ------------------------------------------------------------------------------------------------------------

# reverse() => Listeyi büyükten küçüğe doğru sıralar.
# numbers.reverse()
# print(numbers)
# ------------------------------------------------------------------------------------------------------------

# len() => Dizinin uzunluğunu yani kaç değeri olduğunu döndürür.
# print(len(numbers))
# ------------------------------------------------------------------------------------------------------------

# count() => istenilen değerin liste içerisinde kaç tane olduğunu bize döndürür.
# print(numbers.count(4))
# ------------------------------------------------------------------------------------------------------------

# clear() => Listenin tüm elemanlarını silmek için kullanılır.
# print(numbers)
# numbers.clear()
# print(numbers)
# ------------------------------------------------------------------------------------------------------------

