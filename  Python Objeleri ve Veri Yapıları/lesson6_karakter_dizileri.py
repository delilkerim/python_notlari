# Pyton'da aslında string ifadeler karakter dizilerinden oluşurlar. Yani bir string ifadenin bütün değerlerine ulaşılabilir.
name = "Kerim"
lastName = "DELİL"
school = "Şehit Murat Tuzsuz Mesleki ve Teknik Anadolu Lisesi"

totalSentence = "Hi. My name is " + name + " " + lastName + " I am working in " + school + " now."
print(totalSentence)

# totalSentence değişkeni karakter dizisidir. PEki bu bizim için ne anlama gelmektedir. 
# totalSentence değişkenin ilk harfini ekrana yazdırmak istersek;
print(totalSentence[0])

# totalSentence değişkenin uzunluğunu yani karakter sayısını bulmak istersek;
print(len(totalSentence))

# totalSentence değişkeninin sonuncu karakterini ekranda göstermek için;
# 1. yol
print(totalSentence[len(totalSentence)-1])
# 2. yol
print(totalSentence[-1])

# ! NOT: KARAKTER DİZİLERİNDE EN SON KARAKTER -1 İLE BAŞLAR VE BAŞA DOĞRU EKSİLEREK DEVAM EDER.

# totalSentence değişkeninin sondan 2. karakterini ekranda göstermek için
print(totalSentence[-2])

# totalSentence değişkeninin 3. karakterden başlayıp 20 karaktere kadar almak istersek;
print(totalSentence[3:20])

# totalSentence değişkeninin 5. karakterden başlayıp geri kalan tüm karakterlerini almak istersek;
print(totalSentence[5:])

# totalSentence değişkeninin -2. karakterden başlayıp başına kadar almak istersek;
print(totalSentence[:-2])
