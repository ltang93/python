import csv,random,sys
sys.path.append('\\'.join(sys.path[0].split('\\')[:-1]))

def CsvLoadTitle(filesrc,num):
    with open(filesrc,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row['序号']==str(num)):
                return row['题干']

def CsvLoadOption(filesrc,num):
    with open(filesrc,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        oplist=[]
        for row in reader:
            if(row['序号']==str(num)):
                for i in range(0, 4):
                    oplist.append(row[chr(65+i)])
                return oplist

def CsvLoadAnswer(filesrc,num):
    with open(filesrc,'r') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            if(row['序号']==str(num)):
                return row['答案']

if __name__ == '__main__':
    while(1):
        filenum=random.randint(1,3)
        if filenum==1:
            filename='2017-单选.csv'
            num=random.randint(1,807)
        elif filenum==2:
            filename = '2017-多选.csv'
            num = random.randint(1, 599)
        else:
            filename = '2017-判断.csv'
            num = random.randint(1, 598)

        title=CsvLoadTitle(filename,num)
        if filenum==1 or filenum==2:
            if filenum==1:
                title='(单选)'+title
            elif filenum==2:
                title = '(多选)' + title
            options=CsvLoadOption(filename,num)
            i = 0
            for option in options:
                option=str(option).replace(' ','')
                title = title + '\n' + chr(65 + i) + '. ' + option
                i+=1
        else:
            title='(判断题,1=对，0=错)'+title
        print(title)
        print('请输入你的回答')
        useranswer=input()
        answer=CsvLoadAnswer(filename,num)
        if useranswer.upper() == answer.upper():
            print('回答正确')
        elif useranswer=='1' and answer == '对':
            print('回答正确')
        elif useranswer=='0' and answer == '错':
            print('回答正确')
        else:
            print('回答错误')
            print('正确答案:'+str(answer))
            with open('error.csv','a') as errorfile:
                errorfile.write(str(filenum)+','+str(num))
                errorfile.write('\n')
        print('\n')

'''
    def __init__(self):
        self.filename = '2017-单选.csv'
        self.num = random.randint(1, 807)
        self.title = AbchinaCsv.CsvLoadTitle(self.filename, self.num)
        self.options = AbchinaCsv.CsvLoadOption(self.filename, self.num)
        self.answer = AbchinaCsv.CsvLoadAnswer(self.filename, self.num)
        self.title=self.title+'\n'
        i=0
        for option in self.options:
            self.title=self.title+'\n'+chr(65+i)+'. '+option
'''