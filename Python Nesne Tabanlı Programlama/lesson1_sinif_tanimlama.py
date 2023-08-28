# Python object orianted programming (nesne tabanlı programlama) yapısında bir programlama dilidir. Bu ona daha fazla güç katmaktadır.
# Class tanımlaması yaparken class isminin İLK HARFİNİN BÜYÜK OLMASINA DİKKAT EDİNİZ!!!

# CLASS VE INSTANCE(OBJECT) KAVRAMLARI
# Class ana çatıdır. Class'lar attributes(özellikler) ve methods (metotlar) dan oluşur. Instance(object) ise class'dan üretilendir. Nesnedir, örnektir.
# instance (object)
class Person:
    # attributes (özellikler) Yani değişkenler
    # Bunlarda 2 ye ayrılır. Class attributes, instance attributes
    
    address = "no information" # bu attributes daha sonradan her instance için değiştirilebilir.
    
    # instance attributes'lerin tanımlama yeri constuctur(yapıcı/kurucu) metotların içerisindedir.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("constructor çalıştırıldı.")
        
    # Yukarıkıdaki kod yapısına bakıldığı zaman
    # ! Constructor(yapıcı) metot tanımlaması "__init__(self, attribute_adi)" şeklindedir.
    # ! Bir class'dan nesne üretildiği anda constructor metodu direk çalışır.


p1 = Person('kerim',43)
# Class'dan instance oluşturma yukarıdaki gibi olabileceği gibi aşağıdaki gibi de olabilir.
p2 = Person(age=9, name='Selim')

# Şimdi 2 tane oluşturulan personelin attribute'lerini ekranda gösterelim.
print(f' p1: name: {p1.name} age:{p1.age} address:{p1.address}')
print(f' p2: name: {p2.name} age:{p2.age} address:{p2.address}')

# p1 personelinin ismini "Ayşe", adresini "Batıkent Mah" yapalım.
p1.name="Ayşe"
p1.address = "Batıkent Mah."
print(f' p1: name: {p1.name} age:{p1.age} address:{p1.address}')
print(f' p2: name: {p2.name} age:{p2.age} address:{p2.address}')

# ! NOT: CLASS VEYA INSTANCE ATTRIBUTES'LARININ HEPSİNE ERİŞİLEBİLDİĞİ GİBİ DEĞİŞTİRİLEBİLİR.




