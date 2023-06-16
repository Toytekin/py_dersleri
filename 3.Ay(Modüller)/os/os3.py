import os

##! Bir dosyadakii tüm verileri, dosyaları alma

print(os.getcwd())

for klasorYolu,klasorIsimnleri,dosyaIsimleri in os.walk("/Users/ibrahimtoytekin/Desktop"):
        # print("klasor Yolu",klasorYolu)
        # print("Klasör  İsimleri",klasorIsimnleri)
        # print("Dosya İsimleri",dosyaIsimleri)
        for i in dosyaIsimleri:
                print(i)
                
print('****************************************')                
                
print('\n')  
print('FİLTRELEME')                
              
for klasorYolu,klasorIsimnleri,dosyaIsimleri in os.walk("/Users/ibrahimtoytekin/Desktop"):
        # print("klasor Yolu",klasorYolu)
        # print("Klasör  İsimleri",klasorIsimnleri)
        # print("Dosya İsimleri",dosyaIsimleri)
        for i in dosyaIsimleri:
                if(i.endswith(".txt")):
                        print(i)            