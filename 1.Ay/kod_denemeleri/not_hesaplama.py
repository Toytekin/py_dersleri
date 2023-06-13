


def not_hesapla(satir):
    
   satir=satir[:-1]
   liste=satir.split(',')

   not1=int(liste[1])*3/10
   not2=int(liste[2])*3/10
   not3=int(liste[3])*4/10

   toplam_not=not1+not2+not3



   if toplam_not>=90:
        harf='AA'
   elif toplam_not>=80:
        harf='BA'
   elif toplam_not>=75:
        harf='BB'
   elif toplam_not>=70:
        harf='CA'
   elif toplam_not>=65:
        harf='CB'
   elif toplam_not>=75:
        harf='CC'
   elif toplam_not>=60:
        harf='DA'
   elif toplam_not>=50:
        harf='DB'
   elif toplam_not>=45:
        harf='DC'
   elif toplam_not>=30:
        harf='DD'
   else:

        print('Hesaplanamadı')

   return str(f'{liste[0]}+----------  {harf}')    



with open('notlar.txt','r', encoding='utf-8') as file:
    eklenecekler=[]
    for i in file:
     eklenecekler.append( not_hesapla(i))
       
     print(eklenecekler)
    

    with open('notSonuc.txt','w', encoding='utf-8') as file2:
      for gelen in eklenecekler:  
       file2.write(gelen)
       file2.close()   