# Python'da set listeleri de aynı dictionary gibi {} işaretleri ile tanımlanırlar. Farkı ise key->value yapısı yoktur, değerler arasına "," virgül konulur.
# set'lerin en önemli özelliği indekslenmezler ve içerisinde aynı değer bulundurmazlar.

fruits = {'elma','armut','muz'}
# print(type(fruits))

# add() => tek bir eleman eklemek için kullanılır.
fruits.add('nar')
# print(fruits)

# update() => birden fazla eleman eklemek için kullanılır. Bu elemenlar genelde bir listenin içinde olmalıdır.
fruits.update(['üzüm','kivi','şeftali'])
# print(fruits)

# remove() => istenilen değeri set'den silmek için kullanılır.
# print(fruits)
# fruits.remove('elma')
# print(fruits)

# discard() => Yine istenilen değeri set'den silmek için kullanılır.
# print(fruits)
# fruits.discard('elma')
# print(fruits)

# remove() => Tüm set'i silmek için kullanılır.
# print(fruits)
# fruits.clear()
# print(fruits)


