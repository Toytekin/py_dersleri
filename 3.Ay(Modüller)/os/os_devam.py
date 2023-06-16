import os
from datetime import datetime

print(os.getcwd())
print(os.listdir())

##! STAT fonksiyonu
##! Saniye cinsinden dosyanın değiştirme zamanı
degistermeZamaniSaniye=os.stat("yazi.txt").st_mtime
print(degistermeZamaniSaniye)

##! Anlaşılır formata çevirme

print(datetime.fromtimestamp(degistermeZamaniSaniye))




