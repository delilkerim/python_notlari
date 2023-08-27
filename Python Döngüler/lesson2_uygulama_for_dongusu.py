# Python'da For Döngüsü ile ilgili pekiştirme işlemleri için uygulamalar
numbers = [1,3,5,7,9,12,15,17,19,21,23]

# 1- numbers listesindeki hangi sayılar 3'ün katıdır?
# result = []
# for num in numbers:
#     if num%3 == 0:
#         result.append(num)
        
# print(result)
# -------------------------------------------------------------------------------------------------

# 2- numbers listesindeki sayıların toplamı kaçtır?
# result = 0
# for num in numbers:
#     result += num
# print(result)
# -------------------------------------------------------------------------------------------------

# 3- numbers listesindeki tek sayıların karesini alıp gösteriniz.
# result = list()
# for num in numbers:
#     if num%2 == 1:
#         result.append(num**2)
# print(result)
# -------------------------------------------------------------------------------------------------

cities = ['kocaeli','eskişehir','aydın','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterdir?
# for city in cities:
#     if len(city)<=5:
#         print(city)
# -------------------------------------------------------------------------------------------------

products = [
    {'name':'samsung S6', 'price':'3000'},
    {'name':'samsung S7', 'price':'4000'},
    {'name':'samsung S8', 'price':'5000'},
    {'name':'samsung S9', 'price':'6000'},
    {'name':'samsung S10', 'price':'7000'},
]

# 5- Ürünlerin fiyatları toplamı nedir?
# totalPrice = 0
# for product in products:
#     totalPrice += int(product['price'])

# print(f'Ürünlerin fiyat toplamları: {totalPrice} TL.') 
# -------------------------------------------------------------------------------------------------

# 6- Ürünlerden fiyatı sadece 5000TL'den fazla olan ürünleri ekranda gösteriniz.
for product in products:
    if (int(product['price'])<=5000):
        print(f'{product["name"]} isimli ürünün fiyatı {product["price"]}')


