import csv,random,sys,linecache
sys.path.append('\\'.join(sys.path[0].split('\\')[:-1]))
from AbchinaGmjl import AbchinaErrTrain

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

def loadQuestion(filename,num,filenum):
    title=''
    title = CsvLoadTitle(filename, num)
    if int(filenum) == 1 or int(filenum) == 2:
        if int(filenum) == 1:
            title = '(单选)' + title
        elif int(filenum) == 2:
            title = '(多选)' + title
        options = CsvLoadOption(filename, int(num))
        i = 0
        for option in options:
            option = str(option).replace(' ', '')
            title = title + '\n' + chr(65 + i) + '. ' + option
            i += 1
    else:
        title = '(判断题,1=对，0=错)' + title
    return title

def answerQuestion(filename,num,filenum):
    print('请输入你的回答')
    useranswer = input()
    answer = CsvLoadAnswer(filename, num)
    with open('finish.csv', 'a') as finishfile:
        finishfile.write(str(filenum) + ',' + str(num))
        finishfile.write('\n')
    if useranswer.upper() == answer.upper():
        print('回答正确')
        with open('right.csv', 'a') as rightfile:
            rightfile.write(str(filenum) + ',' + str(num))
            rightfile.write('\n')
        print('\n')
        return 1
    elif useranswer == '1' and answer == '对':
        print('回答正确')
        with open('right.csv', 'a') as errorfile:
            errorfile.write(str(filenum) + ',' + str(num))
            errorfile.write('\n')
        print('\n')
        return 1
    elif useranswer == '0' and answer == '错':
        print('回答正确')
        with open('right.csv', 'a') as errorfile:
            errorfile.write(str(filenum) + ',' + str(num))
            errorfile.write('\n')
        print('\n')
        return 1
    else:
        print('回答错误')
        print('正确答案:' + str(answer))
        with open('error.csv', 'a') as errorfile:
            errorfile.write(str(filenum) + ',' + str(num))
            errorfile.write('\n')
        print('\n')
        return 0


def guess(filenamelist,numlist):
    while (1):
        filenum = random.randint(1, 3)
        if filenum == 1:
            # filename = '2017-单选.csv'
            filename=filenamelist[0]
            # num = random.randint(1, 807)
            num=random.randint(1,numlist[0])
        elif filenum == 2:
            # filename = '2017-多选.csv'
            filename=filenamelist[1]
            # num = random.randint(1, 599)
            num=random.randint(1,numlist[1])
        else:
            # filename = '2017-判断.csv'
            filename=filenamelist[2]
            # num = random.randint(1, 598)
            num=random.randint(1,numlist[2])

        title=loadQuestion(filename,num,filenum)
        print(title)
        answerQuestion(filename,num,filenum)
        AbchinaErrTrain.sortCsv()

def exercise(filenamelist):
    while(1):
        with open('error.csv') as errorfile:
            count = len(errorfile.readlines())
            i =random.randint(1,count)
            exer = linecache.getline('error.csv', i)
        filenum=exer.split(',')[0]
        if filenum == '1':
            # filename = '2017-单选.csv'
            filename=filenamelist[0]
            # num = random.randint(1, 807)
            num=exer.split(',')[1].replace('\n','')
        elif filenum == '2':
            # filename = '2017-多选.csv'
            filename=filenamelist[1]
            # num = random.randint(1, 599)
            num=exer.split(',')[1].replace('\n','')
        else:
            # filename = '2017-判断.csv'
            filename=filenamelist[2]
            # num = random.randint(1, 598)
            num=exer.split(',')[1].replace('\n','')
        title=loadQuestion(filename,num,filenum)
        print(title)
        result=answerQuestion(filename,num,filenum)
        if result == 0:#wrong
            AbchinaErrTrain.sortCsv()
        elif result == 1:#right
            AbchinaErrTrain.sortCsv(dele=True,filenum=filenum,num=num)

if __name__ == '__main__':
    print('请选择，练习输入1，复习输入2  ：')
    extype=input()
    if extype=='1':
        guess(filenamelist=['2017-单选.csv','2017-多选.csv','2017-判断.csv'],numlist=[807,599,598])
    elif extype=='2':
        exercise(filenamelist=['2017-单选.csv','2017-多选.csv','2017-判断.csv'])
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