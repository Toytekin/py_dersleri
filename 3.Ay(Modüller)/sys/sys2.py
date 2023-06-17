import sys

#! sys.stderr.write() Hata mesajı yazdırma
print("\n")
sys.stderr.write('Bu bir hata mesajıdır !')
print("\n")
#! sys.stdout.write() Normaal mesaj
sys.stdout.write('Bu normal bir mesajdır.\n\n')


  
for i in sys.argv:
        print('******')
        print(i)
