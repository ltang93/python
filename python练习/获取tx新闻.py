import requests
from bs4 import BeautifulSoup

re=requests.get("http://news.qq.com/")
soup=BeautifulSoup(re.text,'html.parser')
#print(soup)
for title in soup.find_all('a','linkto'):
    #print(title)
    print(title.text)
    news=open('D://news.txt','a')
    news.write(title.text+'\n')