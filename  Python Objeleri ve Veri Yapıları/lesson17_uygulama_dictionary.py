# Python'da dictionary liste tipi hakkında öğrendiklerimizi pekiştirebileceğimiz bir uygulama
""" ogrenciler = {
    '120':{
        'name':'Ahmet',
        'surname':'DERE',
        'phone':'555 232 32 32'
    },
    '121':{
        'name':'Mehmet',
        'surname':'KEMİK',
        'phone':'543 123 32 30'
    },
} """
# 1- Kullanıcıdan yukarıdaki bilgileri elde edebileceğimiz ifadeleri alıp bir dictionary yapısı yapınız.
studentNumber = input('Öğrenci numarası giriniz:')
studentName = input('Öğrenci Adı:')
studentSurname = input('Öğrenci Soyadı:')
studentPhone = input('Telefon:')

ogrenciler={}
ogrenciler[studentNumber]={
    'name':studentName,
    'surname':studentSurname,
    'phone':studentPhone
} 

studentNumber = input('Öğrenci numarası giriniz:')
studentName = input('Öğrenci Adı:')
studentSurname = input('Öğrenci Soyadı:')
studentPhone = input('Telefon:')

# ogrenciler ={}
ogrenciler[studentNumber]={
    'name':studentName,
    'surname':studentSurname,
    'phone':studentPhone
} 

print(ogrenciler)

# 2- Öğrenci numarasını kullanıcıdan alıp, o öğrencinin bilgilerini ekranda gösteriniz.
searchStudentNumber = input('Aranacak öğrenci numarası:')
print(ogrenciler[searchStudentNumber])
# Daha güzel bir formatta yazmak istersek;
print(f'Aranan öğrencinin adı: {ogrenciler[searchStudentNumber]["name"]} \
                          soyadı: {ogrenciler[searchStudentNumber]["surname"]}\
                          telefonu: {ogrenciler[searchStudentNumber]["phone"]}')

