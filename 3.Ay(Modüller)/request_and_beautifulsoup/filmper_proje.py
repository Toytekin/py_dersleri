import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/"
response=requests.get(url)
htm_icerigi=response.content
beatiful=BeautifulSoup(htm_icerigi,"html.parser")



filmBaslikleri=beatiful.find_all("td",{"class":"titleColumn"})
filmScorelari=beatiful.find_all("td",{"class":"ratingColumn imdbRating"})



a=float(input("Film scoru gir :"))      ##! Kullanıcıdan veri girmesini istiyoruz

for baslik,score in zip(filmBaslikleri,filmScorelari):
        bs=baslik.text
        score=score.text
        
        bs=bs.strip()                 ##! boşlukları siler      
        bs=bs.replace("\n","")        ##! boşlukları ddeğiştirme  
        
        score=score.strip()
        score=score.replace("\n","")
        
        
          
        if float(score)>a:
        
                print(f"Film Adı: {bs}")
                print(f"Film Score: {score}")
                print("********************")
        else:
                pass    
        

        







