# Python'da herşey bir nesnedir. Yani bir class'dan üretilirler. Hemen hemenher class'ında genel metotları bulunmaktadır. Bu metotları kendi oluşturduğumuz class'larda da kullanabiliriz.
# Örnek: Bir tane liste tanımlayalım.
numbers  = [1,2,3,4,5]
print(len(numbers))

class Movie:
    def __init__(self, name, director, duration):
        self.name = name
        self.director = director
        self.duration = duration
    
    # normalde listelerde bulunan "len" metodunun burada olması için (bu genel len() metodu olacak.)
    def __len__(self):
        return self.duration
    
    # normalde str() metodu ile nesnenin içerikleri gösterilebilirken kendi oluşturduğumuz class'dan bir nesne üretildiği zaman sadece onun bir Class'dan üretildiği ve RAM'daki adres bilgisi görüntülenmektedir. Onun yerine istediğimiz bir ifadeyi döndürebiliriz.
    def __str__(self):
        return f"Filmin adı {self.name} yöneticisi: {self.director} Süresi: {self.duration}"
    
m1 = Movie("film adı","yönetmen adı",120)
print(len(m1))

print(str(m1))