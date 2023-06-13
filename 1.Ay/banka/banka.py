from banka.fonksiyonlar import isimKontrol,sifreKontrol



gelenIsim= input('Kullanıcı Adınız :')

if isimKontrol(gelenIsim)==True:
        gelenSifre=input(f'Şifrenizi giriniz sayın {gelenIsim}')
        if sifreKontrol(gelenSifre)==True:
                print('Sisteme Başarıyla Girdiniz')
        else:
                print('Şifren Hatalı')
else:
        gelenIsim=input('Lütfen Geçerli Bir İsim  Gir: ')
