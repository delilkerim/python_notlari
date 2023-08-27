# Listeler hakkında öğrenmiş olduğumuz konuları pekiştirmek için uygulama sorularıdır.

# 1- "bwm, mercedes, opel, mazda" elemanlarına sahip bir liste oluşturunuz.
# Yukarıdaki gibi string olarak geldiğini düşünelim. Bunları bir liste yapmak için split() metodunu kullanabiliriz. Hadi yapalım.
cars = "bwm, mercedes, opel, mazda".replace(' ','').title().split(',')
# Yukarıdaki koda bakıldığı zaman title() metodu ile tüm kelimelerin ilk harfleri büyük yapıldı. split() metodu ile "," karakterinden ayrılarak dizi haline döndürüldü.replace() metodu ile de ',' karakterinden sonraki boşluklar alındı.
print(cars)
# ---------------------------------------------------------------------------------------------------

# 2- Oluşturulan dizi kaç elemanlıdır?
# print(len(cars))
# ---------------------------------------------------------------------------------------------------

# 3- Dizinin ilk ve son elemanları nelerdir?
# print(f'dizinin ilk elemanı: {cars[0]} son elemanı:{cars[-1]}')
# ---------------------------------------------------------------------------------------------------

# 4- Mazda değerini Toyota ile değiştiriniz.
# cars[-1] = 'Toyota'
# print(cars)
# ---------------------------------------------------------------------------------------------------

# 5- Mercedes listenin bir elemanımıdır?
# isThere = 'Mercedes' in cars
# print(isThere)
# ---------------------------------------------------------------------------------------------------

# 6- Listenin -2. indeksindeki değer nedir?
# print(cars[-2])
# ---------------------------------------------------------------------------------------------------

# 7- Listenin ilk 3 elemanını alınız.
# print(cars[:3])
# ---------------------------------------------------------------------------------------------------

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyiniz.
# print(cars[-2:])
# cars[-2:] = ['Toyota','Renault']
# print(cars)
# ---------------------------------------------------------------------------------------------------

# 9- Listenin üzerine "Audio" ve "Nissan" değerlerini ekleyin.
cars = cars + ["Auido","Nissan"]
print(cars)
# ---------------------------------------------------------------------------------------------------

# 10- Listenin son elemanını siliniz.
del cars[-1]
print(cars)
# ---------------------------------------------------------------------------------------------------

# 11- Listenin elemanlarını tersten yazdırınız.
print(cars[::-1])
# ---------------------------------------------------------------------------------------------------

# 12- Aşağıdaki verileri bir liste şeklinde saklayınız.
# studentA: Ahmet Doğru 2000, (90,80,90)
# studentB: Mehmet Yeni 2002, (60,50,100)
# studentC: Ali Dere 2001, (70,100,70)

studentA = ['Ahmet', 'Doğru' ,'2000',[90,80,90]]
studentB = ['Mehmet' ,'Yeni' ,'2002',[60,82,100]]
studentC = ['Ali', 'Dere', '2001',[70,100,70]]

# 13- Liste elemanlarını ekranda gösteriniz.
students = [studentA, studentB, studentC]
print(students)

# 14- "Mehmet Yeni 21 yaşında ve not ortalaması 70" gibi bir ifade yazdırınız.
print(f'{students[1][0]} {students[1][1]} {2023-int(students[1][2])} yaşında ve not ortalaması {((students[1][3][0] +students[1][3][1] + students[1][3][2] )/3):1.2f}')
