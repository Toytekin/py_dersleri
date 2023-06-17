import requests
from bs4 import BeautifulSoup


url="https://www.agd.org.tr/"

response=requests.get(url)

html_icerigi=response.content
soup=BeautifulSoup(html_icerigi,"html.parser")


for i in soup.find_all("a"):      ##  a etiketi içindekileri alır 
        print(i)
        print("***************")
        print(i.get("href"))      ## sadece likleri alma
        print(i.text)             ## sadece yazıları alma
        
        
        
  

