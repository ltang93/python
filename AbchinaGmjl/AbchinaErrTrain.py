import csv,random,sys,os
sys.path.append('\\'.join(sys.path[0].split('\\')[:-1]))
from  AbchinaGmjl import AbchinaCsv

def sortcsv():
    try:
        if os.path.exists('error.csv'):
            with open('error.csv', 'r') as errorfile:
                err1, err2, err3 = set([]), set([]), set([])
                for line in errorfile:
                    if line.split(',')[0] == '1':
                        err1.add(int(line.split(',')[1]))
                    elif line.split(',')[0] == '2':
                        err2.add(int(line.split(',')[1]))
                    elif line.split(',')[0] == '3':
                        err3.add(int(line.split(',')[1]))
                print(err1,err2,err3)
        if os.path.exists('finish.csv'):
            with open('finish.csv', 'r') as finishfile:
                fi1, fi2, fi3 = set([]), set([]), set([])
                for line in finishfile:
                    if line.split(',')[0] == '1':
                        fi1.add(int(line.split(',')[1]))
                    elif line.split(',')[0] == '2':
                        fi2.add(int(line.split(',')[1]))
                    elif line.split(',')[0] == '3':
                        fi3.add(int(line.split(',')[1]))
                print(fi1,fi2,fi3)
    except:
        pass
        # print('操作错误，请先进行练习！')

    for i in range(1,3):
        if i ==1:
            for

