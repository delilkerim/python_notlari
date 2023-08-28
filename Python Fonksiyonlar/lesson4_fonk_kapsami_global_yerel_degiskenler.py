# Python'da yanı isimli değişken hem ana programda hem de fonk. tanımlandılar ise aslında bunlar birbirinden farklı olarak tanımlanmış olurlar. Birbiriyle hiç bir ilişkileri olmaz.
# name = 'kerim'

# def displayUser():
#     name = "Ali"
#     print(name)
    
# displayUser()
# print(name)
# Yukarıdaki kodda; eğer fonk. içerisinde name değişkeni yoksa python fonk. dışında name değişkeni var mı ona bakar. Eğer varsa onun değeri ile işlem yapar. Eğer fonk. içerisinde "name" değişkeni varsa direk onunla işlem yapar.

# Bazı zamanlar fonk. içerisinde de global değişkenleri kullanmak, değiştirmek isteyebiliriz. Öyle durumlarda fonk. içerisinde aynı isimli değişkeni tanımlarken başına "global" ifadesi ile yazmamız gerekir.
name = 'kerim'

def displayUser():
    global name 
    name = "Ali"
    print(name)
    
displayUser()
print(name)
