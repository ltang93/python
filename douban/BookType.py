import pymysql, requests
from bs4 import BeautifulSoup


def BookTypeSpider():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3051.400 QQBrowser/9.6.11301.400'}
    re = requests.get('https://book.douban.com/tag/?icn=index-nav', headers=header)
    soup = BeautifulSoup(re.text, 'html.parser')
    for tags in soup.find_all('table', 'tagCol'):
        for type in tags.find_all('a'):
            # print(type.text, type['href'])
            bd = BookTypeDb(type=type.text, url=type['href'])
            url = bd.BookTypeDbFind()
            if (url is None):
                bd.BookTypeDbInsert()
            elif (url != type['href']):
                bd.BookTypeDbChange()


class BookTypeDb(object):
    def __init__(self, type='', url=''):
        self.type = type
        self.url = url

    def BookTypeDbFind(self):
        # Connect to the database
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='wangmeng', db='amazon', charset='utf8')
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "select url from type where type ='%s' " % self.type
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()
        db.close()
        return data

    def BookTypeDbInsert(self):
        # Connect to the database
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='wangmeng', db='amazon', charset='utf8')
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "insert into type(type,url) values('%s','%s')" % (self.type, self.url)
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        db.commit()
        db.close()

    def BookTypeDbChange(self):
        # Connect to the database
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='wangmeng', db='amazon', charset='utf8')
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "UPDATE type set url='%s' where type='%s'" % (self.url, self.type)
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        db.commit()
        db.close()

    def BookTypeDbFindAll(self):
        db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='wangmeng', db='amazon', charset='utf8')
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        sql = "select * from type"
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        db.close()
        return data

if __name__ == '__main__':
    # BookTypeSpider()
    d=BookTypeDb()
    data=d.BookTypeDbFindAll()
    print(data)