# Python'da fonksiyonlar parametre alan, almayan ve değer döndüren ve döndürmeyen olarak çeşitlere ayrılırlar.
# Bazı fonksiyonların alacağı parametreler sabittir. Mesela sadece 2 tane parametre alabilirler. 3. parametre aldığında hata verirler. Bazı fonk. ise ne kadar parametre alacağı bilinmeyebilir. Mesela fonk. gönderilen tüm sayıları toplayıp geri döndüren bir fonk. gibi.
# Çok konuştuk, şimdi icrate başlayalım :)

# def twoNumberSum(a,b):
#     return a+b

# print(twoNumberSum(3,4))

# def allNumberSum(*params):
#     # return sum(params) # Yerine
#     sum = 0
#     for p in params:
#         sum += p
#     return sum

# print(allNumberSum(12,23,4,4,4353,534,54,646,56675,7676,8,86,867,34))

# ! NOT: Eğer ne kadar parametre alacağı bilinmeyen bir fonk. için parametre ifadesi yazılırken başına "*" tek yıldız konulursa aslında bu fonk. bizden tuple tipinde bir liste istemektedir.

# Peki bazı fonksiyonlar ise dictionary tipinden birden fazla key->value değerleri almak da isteyebilir. O zaman ne yapacağız?

# def displayUser(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
#     print("-"*50)


# displayUser(name='kerim', surname='DELİL')
# displayUser(name='selim', surname='DELİL', age= 9)

# Bazı fonksiyonlar ise hem kesin alması gerekli parametre, sonra birden çok parametre ve key->value şeklinde de parametreler almak isteyebilir. O zaman da;

def myVarFunc(a,b,c, *args , **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myVarFunc(1,2,3,3,5,66,65,46,4, key1='1', key2= '2', key3 = '3')
# Yukarıdaki kod ve çıktısı incelendiği zaman illaki gereken a,b ve c parametrelerinin değerleri verildikten sonra kalan değerler tuple olarak args parametresine aktarıldı. key=value şeklindeki yapılar ise kwargs parametresine aktarıldı.

    
