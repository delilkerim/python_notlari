# Birden fazla aynı işlemlerin yapıldığı yerlerde DÖNGÜLER kullanılır. En çok kullanılan döngülerden birisi de FOR döngüsüdür.

numbers = [23,5,56,76,89,89,90,23]
# print(numbers)

# print ile numbers listesinin tüm elemanlarını yan yana liste işaretleri arasında görebiliriz. Ama bunları alt alta yazdırmak istediğimizde ya da bu elemanlarla işlemler yapmak istediğimizde işte o zaman for döngüsünü kullanırız.
# for num in numbers:
#     print(num)
    
# Yukarıdaki kodun açıklaması: numbers listenin tüm elemanlarını tek tek "num" değişkenine ata. "num" değişkenine atanan değeri ekranda göster.

names = ['ali','Alexandria','Brandyn','Nikki']
# isimleri alt alta ekranda göstermek için
# for name in names:
#     print(f'Hello {name}')
    
# string ifadelerde karakter dizileri olduğu için;
name = 'Kerim DELİL'
# for n in name:
#     print(n)

# For döngüsünü tuple tiplerinde de kullanırız.
tuple = 1,23,4,34.23, True, 'kerim'
# for t in tuple:
#     print(t)

# For döngüsünü liste elemanının içerisinde tuple'lardan oluşabilir.
liste1 = [(1,2),(2,3),(3,4),(4,5)]
# for list in liste1:
#     print(list)

# Eğer yukarıdaki ifadede tuple'ın da elemanlarına erişmek istersek;
# for a,b in liste1:
#     print(a,b)

# For döngüsünü dictionary tiplerde de kullanırız.
dictionary = {'k1':1, 'k2':2, 'k3':3}
for dic in dictionary:
    print(dic)

# Yukarıdaki kod sadece key'lerin isimlerini verir. Value'lerine de ulaşmak istersek;
for dic in dictionary.items():
    print(dic)

# key ve value değerlerine ayrı ayrı ulaşmak istersek;
for key,value in dictionary.items():
    print(f'{key} değerinin value karşılığı: {value}')