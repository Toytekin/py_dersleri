import os


print('OS MODÜLÜ')

##! Bulunduğum dizini değiştirme
os.chdir("/Users/ibrahimtoytekin/Desktop/PYTHON ÇALIŞMALAR")


##! Bulunduğum dizini veren fonksiyon
print(os.getcwd()) 

##! Bulunduğum dizindeki verileri listeleme
for i in os.listdir():
        print(i)


##! Bulunduğum dizinde bir dosya oluşturma

os.mkdir("deneme1 dosya oluşturma")

##! Bulunduğum dizinde iiç içe dosya oluşturma
os.makedirs("Dosya1/Dosya2/Dosya3")

##! Seçtiiğim dosyayı siler

os.rmdir("Dosya1/Dosya2")

##! Bir dosyanın ismini değiştirme
os.rename('dosyanın varolan ismi', 'Dosyanın yeni ismi')



