# Python dilinde atama operatörü "=" ifadesidir. Bütün programlama dillerinde olduğu gibi sağdaki değer soldaki değişkene aktarılır.
a = 3
# Yukarıdaki kodun açıklaması: 3 değeri a değişkenine aktarılmıştır.

a += 5 # a = a + 5 anlamına gelir. Çıkarma, çarpma, bölme, tam sayılı bölme, mod alma vb. hepsi aynıdır.

# Python'da çoklu değişken atamaları yapılabilir.
# x,y,z = 10,20,30
# print(x,y,z)

# Python'da çoklu değişken atamalarında değişken sayısı ile onlara atanacak değerlerin sayısı eşit olmalıdır. Ama bazı zamanlar tüm değerleri bir yerlere atamak istiyorsak, çok değer atamak istediğimiz değişkenin başına "*" yıldız işareti koyarız. O zaman Python öncelikle tek tek değerleri ilgili değişkenlere atar, fazla kalan değerleri ise * işareti olan değişkene dizi şeklinde atar.
x,*y,z = 10,11,12,13,14,15
print(x,y,z)
