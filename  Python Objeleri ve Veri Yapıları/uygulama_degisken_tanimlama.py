""" 
SUAL-1
Bir öğrencinin aşağıdaki bilgileri için değişkenleri oluşturunuz.

Öğrenci adı
Öğrenci Soyadı
Öğrenci Ad + Soyad
Öğrenci cinsiyet
Öğrenci tc kimlik
Öğrenci doğum yılı
Öğrenci doğum yeri
Öğrenci yaş
Öğrenci numara
Öğrenci sınıf 
"""
# CEVAP-1
studentName = "kerim"
studentLastName = "Delil"
studentNameLastName = studentName + " " + studentLastName
studentGender = "Erkek" # veya studentGender = true (tabi true ifadesinin Erkek, false ifadesinin Kadın olduğuna önceden karar vermek gerekir.)
studentTC ='12321312312312' # öğrencinin TC kimlik numarası ile toplama, çıkarma vb. bir işlem yapılmayacağı için string olarak tanımlamak mantıklıdır.
studentBirthYear = 1980 # doğum yılı ile işlem  yapılabileceği için integer olarak tanımlanmıştır.
studentBirthPlace = "Zonguldak"
studentAge = 2023 - studentBirthYear
studentNumber = 5689
studentClass = "AMP12E"

""" 
SUAL-2
Aşağıdaki bir öğrenciye ait olan 3 notun toplamını bulmak için her bir notu değişken haline getirip değerlerini atayınız ve sonucu ekranda gösteriniz. 
"""
# CEVAP-2:
exam1= 90
exam2 = 100
exam3 = 60
averageOfExams = ( exam1 + exam2 + exam3 ) /3
print(averageOfExams)

