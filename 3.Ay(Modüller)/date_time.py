from datetime import datetime

## dil değişimi yapmak için  <locale > kütüphanesini indirelkim

import locale

locale.setlocale(locale.LC_ALL,'')
         


suankii_zaman=datetime.now()
## print(suankii_zaman)  şuan ki zamanı veriri

print(suankii_zaman.year)  ## yıl
print(suankii_zaman.month)      ## ay
print(suankii_zaman.day)        ## gün
print(suankii_zaman.hour)       ## saat
print(suankii_zaman.second)     ## dakika

print(datetime.strftime(suankii_zaman,'%Y'))     ## yil
print(datetime.strftime(suankii_zaman,'%B'))     ## ay
print(datetime.strftime(suankii_zaman,'%A'))     ## Gün
print(datetime.strftime(suankii_zaman,'%X'))     ## Saat Bilgisi  20:30:05
print(datetime.strftime(suankii_zaman,'%D'))     ## Gün Bilgisi   06/04/2023
print('İbrahim Toytekin')


print('\n')
##! timestap

zaman=datetime.now()
saniye=datetime.timestamp(zaman)
print('Saniye cinsinden yazımım')
print(saniye)

##? Saniye cinsinden verilen değerii şuanki zamana çevirme
print('\n')

zaman2=datetime.fromtimestamp(saniye)
print('Saniyenin çevirilmiş hali')
print(zaman2)
print('\n')
print('İKİ TARİH ARASINDAKİ FARKI BULMA')
girilen_tarih=datetime(2019,10,15)
simdikizaman=datetime.now()
deger=simdikizaman-girilen_tarih
print(deger)








