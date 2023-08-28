# Python'da bir Class başka bir Class'ı miras alabilir. Buna programlamada inheritance(miras) denilmektedir. Miras alınan sınıfın tüm özelliklerine ve metotlarına erişebiliriz.
# Örnek: Person isminde bir sınıfımız olsa; 
# name, lastName, age, city gibi attributes'leri olabilir.
# sleep(), drink(), eat(), run(), speak() gibi de metotları olabilir.

# Peki bir Student class'ı oluşturacağımızı düşünelim. Bu classda da name, lastName, age vb. attributes'ler ve drink(), run(), speak() vb. metotların olması lazımdır. O zaman biz Student class'ının Person class'ından miras yoluyla oluşturabiliriz. Oluşturmak için sadece Student class'ının yazımının sonuna () parantezler içerisine parent class'ının adını yazarız.

# class Person:
#     def __init__(self):
#         print("Person created")
        

# class Student(Person):
#     # Student class'ının kendine ait constructor metodu olabilir. Yazıldığı anda parent class'ındaki constructor metodunu ezmiş (override) etmiş olur. 
#     def __init__(self):
#         Person.__init__(self) # Fakat bazı zamanlar parent class'ındaki attributes'ler lazım olabilmektedir. onun için hem parent class'ının constructor'ını hem de kendi constructor'ını çalıştırma imkanı bulunmaktadır. 
#         print("Student created")

# p1 = Person()
# s1 = Student()

# ! NOT: Eğer Person class'ında firstName ve lastName parametreleri constructor'a gelecek ise bunun da Student class'ında kullanılması için yukarıdaki kodlar aşağıdaki kodlara çevrilir.

class Person:
    def __init__(self,firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        # print("Person created")
    
    # Person class'ında bir metot tanımlayalım.
    def who_am_i(self):
        print('I am a person')
# -------------------------------------------------------------------------------------------------      

class Student(Person):
    # Student class'ının kendine ait constructor metodu olabilir. Yazıldığı anda parent class'ındaki constructor metodunu ezmiş (override) etmiş olur. 
    def __init__(self,firstName,lastName, number):# ESKİ HALİ:def __init__(self):
        self.number = number # Student classının instance'ına özel bir attribute
        Person.__init__(self, firstName, lastName) # ESKİ HALİ: Person.__init__(self)  
        # Fakat bazı zamanlar parent class'ındaki attributes'ler lazım olabilmektedir. onun için hem parent class'ının constructor'ını hem de kendi constructor'ını çalıştırma imkanı bulunmaktadır. 
        # print("Student created")
        
    # who_am_i metodunu override (ezme) edelim.
    def who_am_i(self):
        print("I am a student")
# -------------------------------------------------------------------------------------------------      

class Teacher(Person):
    def __init__(self,firstName, lastName, branch):
        self.branch = branch
        super().__init__(firstName, lastName) # ESKİ YAZILIMI: Person.__init__(self, firstName,lastName)      
        
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")


p1 = Person("ali","demir")
s1 = Student("ayhan","solak",5689)
t1 = Teacher("Kerim","DELİL","Bilişim")

# print(s1.firstName, s1.lastName)
# Yukarıdaki kodda görüldüğü gibi s1 nesnesinin firstName ve lastName bilgilerine erişebilmekteyiz.

print(s1.number)
p1.who_am_i()
s1.who_am_i()
t1.who_am_i()


