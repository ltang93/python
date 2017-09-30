import csv,random,sys
sys.path.append('\\'.join(sys.path[0].split('\\')[:-1]))
from  AbchinaGmjl import AbchinaCsv

try:
    with open('error.csv', 'r') as errorfile:
        s1, s2, s3 = set([]), set([]), set([])
        for line in errorfile:
            if line.split(',')[0] == '1':
                s1.add(int(line.split(',')[1]))
            elif line.split(',')[0] == '2':
                s2.add(int(line.split(',')[1]))
            elif line.split(',')[0] == '3':
                s3.add(int(line.split(',')[1]))
except:
    print('操作错误，没有错题文件，请先进行练习！')

for i in range(1,3):
    pass # do what ??
