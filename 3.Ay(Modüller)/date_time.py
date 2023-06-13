from datetime import datetime



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






