import requests,logging
from bs4 import BeautifulSoup

def output(address):
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.debug(address)
    re1 = requests.get(address)
    re1.encoding = 'utf-8'
    soup1 = BeautifulSoup(re1.content, 'html.parser').find('div', attrs={'itemprop': 'articleBody'})
    title = soup1.find('h1').get_text()
    txt=open('D://1//'+title[0:-1].replace('/','／').replace('*','星')+'.txt','w',encoding='utf-8')
    txt.write(str(soup1.get_text()))
    txt.close()
    #print(title)
    #print(soup1.get_text())
    # soup1=soup1.find('div',attrs={'class':'line-block'})
    '''bodys=soup1.find_all('div',attrs={'class':'line'})
    for body in bodys:
        print(body.get_text())'''

    logging.debug('====================NEXT====================')
    return 0

re=requests.get('http://python3-cookbook.readthedocs.io/zh_CN/latest/copyright.html')
re.encoding='utf-8'
soup=BeautifulSoup(re.text, 'html.parser')
list=soup.find('ul',attrs={'class':'current'})
for link in list.find_all('a'):
    if(link.get('href')=='#'):
        addre='http://python3-cookbook.readthedocs.io/zh_CN/latest/copyright.html'
        output(addre)
    else:
        if(link.get('href')[0:2]=='ch'):
            addre = 'http://python3-cookbook.readthedocs.io/zh_CN/latest/' + link.get('href')
            re2 = requests.get(addre)
            re2.encoding = 'utf-8'
            soup2 = BeautifulSoup(re2.content, 'html.parser').find('div', attrs={'class': 'toctree-wrapper compound'})
            for addre1 in soup2.find_all('a'):
                output('http://python3-cookbook.readthedocs.io/zh_CN/latest/' + str(addre1.get('href'))[3:])
        else:
            addre='http://python3-cookbook.readthedocs.io/zh_CN/latest/'+link.get('href')
            output(addre)
