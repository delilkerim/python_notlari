# Python'da Class'larin hem attribute'leri hem de metotları olmaktadır. Şimdi de metot tanımlayalım.
# class Person:
#     # class düzeyinde attribute tanımlayalım.
#     address ="Eskişehir"
#     # Bu sınıftan her nesne üretildiği zaman otomatik olarak address değeri "Eskişehir" olmaktadır.
    
#     def __init__(self, name, birthYear):
#         self.name = name # self.name ifadesindeki "name" ismi instance düzeyindeki attribute'ün ismi oluyor. İstersek bu ismi istediğimiz gibi değiştirebiliriz. "=" eşitliğin sağındaki "name" ismi ise bu constructor metodunun istediği parametre ismi oluyor.
#         self.birthYear = birthYear
        
    
#     # instance method tanımlayalım. Bu metotu instance düzeyinde kullanabilmek için parantezleri içerisine muhakkak "self" ifadesini kullanmak zorundayız. Ayrıca bu metodun içerisindeki attribute'leri kullanmak için de başlarına self.attribute_adi gelmek zorundadır.
#     def intro(self):
#         print(f"Hello {self.name}")
    
#     # Yaş hesaplayan bir metot tanımlayalım.
#     def calculateAge(self):
#         return 2023-self.birthYear
    

# # Şimdide bir tane personel oluşturalım.
# p1 = Person(birthYear=1980, name='kerim')

# # kerim personelinin intro metodunu çağıralım. Metodu çağırırken () unutmayalım!!!
# p1.intro()

# # kerim personelin yaşını hesaplayan metodu çağıralım.
# print(f"Merhaba {p1.name}, Yaşınız: {p1.calculateAge()}")

# --------------------------------------------------------------------------------------------------
# şimdide dairenin alanını ve çevresini hesaplamak için bir tane class oluşturalım. Böylece dairenin alanı veya çevresini hesaplamak istediğimiz zaman yazmış olduğumuz bu class'ı bir ömür boyu kullanabiliriz:)
class Circle:
    # class düzeyinde attribute olarak pi sayısını tanımlayabiliriz.
    pi = 3.14
    
    # instance düzeyinde attribute olarak yaricap tanımlayabiliriz.
    def __init__(self,yaricap=1): # yaricap=1 ifadesinin anlamı: eğer yarıçap girmezlerse default olarak 1 olarak alınacaktır.
        self.yaricap = yaricap
    
    # alan hesaplamak için metodumuz
    def alanHesapla(self):
        return self.yaricap * self.yaricap * self.pi

    # çevre hesaplamak için metodumuz
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

# şimdi de Circle class'ından 2 tane instance(object) nesne üretelim.
c1 = Circle()
c2 = Circle(10)

print(f'c1 nesnesinin çapı: {c1.yaricap} alanı:{c1.alanHesapla()} çevresi:{c1.cevreHesapla()} ')
print(f'c2 nesnesinin çapı: {c2.yaricap} alanı:{c2.alanHesapla()} çevresi:{c2.cevreHesapla():0.2f} ')