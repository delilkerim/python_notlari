# Python'da başka bir liste çeşitide dictionary (sözlük) dir. Aynı sözlük gibi çalışır. Key->value şeklindedir. Bir dictionary'nin key'indeki value'e ulaşmak için ['key_adi'] yazılır.
# Python'da dictionary oluşturmak için {} kullanılır.

# person = {
#     'name':'Kerim',
#     'surname':'DELİL',
#     'age':43
# }

# print(person)
# person dictionary'nin name key'indeki value'ye ulaşmak için
# print(person['name'])
# print(person['surname'])
# print(person['age'])

# Dictionary'de olmayan bir key'i value'si ile beraber ekleyebiliriz.
# person['address'] = 'Yaşamkent Mah.'
# print(person)

# Dictionary'de varolan bir key'in value'sini değiştirebiliriz.
# person['address'] = "Batıkent Mah"
# print(person)

# ---------------------------------------------------------------------------------------------------------
# Python'da dictionary yapısının içinde iç içe dictionary, list, tuple vb. yapılar olabilir.
users = {
    'kerimdelil':{
        'name':'Kerim',
        'surname':'DELİL',
        'age':43,
        'roles':['admin','user'],
        'workingArea':{
            'Eskişehir':5,
            'Aydın':10,
            'Ankara':3
        }
    },
    'selimdelil':{
        'name':'Selim',
        'surname':'DELİL',
        'age':9,
        'roles':['user'],
        'workingArea':{
            'Eskişehir':2,
            'Aydın':0,
            'Ankara':0
        }
    },
}

# Yukarıdaki yapıya göre sadece users'ların isimlerini gösteriniz.
print(users['kerimdelil'])
# kerimdelil kullanıcısının görevlerini gösteriniz.
print(users['kerimdelil']['roles'])
# kerimdelil kullanıcısının çalıştığı yerleri gösteriniz.
print(users['kerimdelil']['workingArea'])
# kerimdelil kullanıcısının eskişehir'de kaç yıl çalıştığını gösteriniz.
print(users['kerimdelil']['workingArea']['Eskişehir'])

# ! NOT: KEY İSİMLERİNİ VERİRKEN TÜRKÇE KARAKTER KULLANMAK SIKINTI VEREBİLİR.


