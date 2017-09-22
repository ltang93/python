import requests,time,random
from bs4 import BeautifulSoup

def gettype(line):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3051.400 QQBrowser/9.6.11301.400'}
    re=requests.get('http://www.baidu.com/s?ie=UTF-8&wd='+line,headers=header)
    re.encoding='utf-8'
    soup=BeautifulSoup(re.content,'html.parser')
    # print(soup)
    outfile = open('E://机型//1.txt', 'a')
    digitals = soup.find_all('div', 'ecl-pc-digital-overflow')
    if digitals != []:
        for d in digitals:
            try:
                if d.find('span',attrs={'class':'c-gray'}).text=='主屏：':
                    type=d.text[4:-1].strip()
                    if type[-1]=='像':
                        type=type[:-2]
                    if type[-2:]=='像素':
                        type = type[:-3]
                    if type[-3:]=='108' or type[-3:]=='144' or type[-2:]=='72' or type[-2:]=='54' or type[-2:]=='32' or type[-2:]=='64':
                        type=str(type)+str('0')
                    with open('E://机型//1.txt', 'a') as outfile:
                        outfile.write(line.strip()+','+type+'\n')
                        print(line.strip()+','+type)
                    break
            except:
                with open('E://机型//1.txt', 'a') as outfile:
                    outfile.write(line.strip() + ',' + '\n')
                    print(line.strip() + ',')
                break

    else:
        with open('E://机型//1.txt', 'a') as outfile:
            outfile.write(line.strip() + ',' + '\n')
            print(line.strip() + ',' )

with open('E://机型//机型.txt') as f:
    for i in range(1500):
        line=f.readline()
        gettype(line)
        time.sleep(1)

