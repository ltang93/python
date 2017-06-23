from douban import BookType
import requests, re, pymysql, time,random
from bs4 import BeautifulSoup

class BookDb(object):
    def __init__(self, name='', score='', total='', type=''):
        self.name = name
        self.score = score
        self.total = total
        self.type = type

    def BookDbFind(self):
        # Connect to the database
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='wangmeng', db='amazon', charset='utf8')
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "select * from book where name =%s"
        cursor.execute(sql,self.name)
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        db.close()
        return data

    def BookDbInsert(self):
        # Connect to the database
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='wangmeng', db='amazon', charset='utf8')
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into book(name,score,total,type) values(%s,%s,%s,%s)"
        print(self.name, self.score, self.total, self.type)
        cursor.execute(sql,(self.name, self.score, self.total, self.type))
        # 使用 fetchone() 方法获取单条数据.
        db.commit()
        db.close()

    def BookDbChange(self):
        # Connect to the database
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='wangmeng', db='amazon', charset='utf8')
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "UPDATE book set score=%s , total=%s , type=%s where name=%s"
        cursor.execute(sql,(self.score, self.total, self.type, self.name))
        # 使用 fetchone() 方法获取单条数据.
        db.commit()
        db.close()

    def BookDbFindAll(self):
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='wangmeng', db='amazon', charset='utf8')
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "select * from book"
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        db.close()
        return data

def TagSpider(type, url, pages):
    for i in range(pages):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3051.400 QQBrowser/9.6.11301.400'}
        req = requests.get('https://book.douban.com' + url + '?start=%s&type=T' % (20 * i), headers=header)
        if req.status_code != 200:
            print(BeautifulSoup(req.text, 'html.parser').text)
            raise SystemExit
        soup = BeautifulSoup(req.text, 'html.parser')
        for items in soup.find_all('li', 'subject-item'):
            # for infos in items.find_all('div', 'info'):
            infos=items.find('div',attrs={'class':'info'})
            name = infos.find('a').text.replace(' ', '').replace('\n', '')
            try:
                score = infos.find('span', attrs={'class': 'rating_nums'}).text.replace(' ', '').replace('\n', '')
            except:
                score = 0
            try:
                total = re.compile(r'\d+').search(infos.find('span', attrs={'class': 'pl'}).text.replace(' ', '').replace('\n', '')).group()
            except:
                continue
            print(name, score, total, type)
            dbbook = BookDb(name=name, score=score, total=total, type=type)
            name = dbbook.BookDbFind()
            if (name is None):
                dbbook.BookDbInsert()
            else:
                dbbook.BookDbChange()
            time.sleep(random.randint(1,5))


bd = BookType.BookTypeDb()
typelist = bd.BookTypeDbFindAll()
for type, url in typelist:
    TagSpider(type=type, url=url, pages=10)
    time.sleep(random.randint(1,10))



#
# if __name__ == '__main__':
#     name="世界別為我擔心:Don'tWorry,BeHappy"
#     score='8.6'
#     total='1862'
#     type='jm'
#     dbbook = BookDb(name=name, score=score, total=total, type=type)
#     name = dbbook.BookDbFind()
#     if (name is None):
#         dbbook.BookDbInsert()
#         print('1')
#     else:
#         dbbook.BookDbChange()
#         print('2')
#     time.sleep(random.randint(1, 5))