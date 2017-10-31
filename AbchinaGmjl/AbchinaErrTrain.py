import sys,os
sys.path.append('\\'.join(sys.path[0].split('\\')[:-1]))


def sortCsv(dele=False,filenum=0,num=0):
    err1, err2, err3 = set([]), set([]), set([])
    fi1, fi2, fi3 = set([]), set([]), set([])
    if os.path.exists('error.csv'):
        with open('error.csv', 'r') as errorfile:
            for line in errorfile:
                if line.split(',')[0] == '1':
                    err1.add(int(line.split(',')[1]))
                elif line.split(',')[0] == '2':
                    err2.add(int(line.split(',')[1]))
                elif line.split(',')[0] == '3':
                    err3.add(int(line.split(',')[1]))
            list(err1).sort()
            list(err2).sort()
            list(err3).sort()
            # print(err1,err2,err3)
        os.remove('error.csv')
    if os.path.exists('finish.csv'):
        with open('finish.csv', 'r') as finishfile:

            for line in finishfile:
                if line.split(',')[0] == '1':
                    fi1.add(int(line.split(',')[1]))
                elif line.split(',')[0] == '2':
                    fi2.add(int(line.split(',')[1]))
                elif line.split(',')[0] == '3':
                    fi3.add(int(line.split(',')[1]))
            if dele==True:
                if filenum==1:
                    err1.remove(num)
                elif filenum==2:
                    err2.remove(num)
                elif filenum==3:
                    err3.remove(num)
            list(fi1).sort()
            list(fi2).sort()
            list(fi3).sort()
            # print(fi1,fi2,fi3)
        os.remove('finish.csv')


    for i in range(3):
        if i ==0:
            for item in err1:
                with open('error.csv', 'a') as errorfile:
                    errorfile.write('1' + ',' + str(item))
                    errorfile.write('\n')
            for item in fi1:
                with open('finish.csv', 'a') as finishfile:
                    finishfile.write('1' + ',' + str(item))
                    finishfile.write('\n')
        if i==1:
            for item in err2:
                with open('error.csv', 'a') as errorfile:
                    errorfile.write('2' + ',' + str(item))
                    errorfile.write('\n')
            for item in fi2:
                with open('finish.csv', 'a') as finishfile:
                    finishfile.write('2' + ',' + str(item))
                    finishfile.write('\n')
        if i==2:
            for item in err3:
                with open('error.csv', 'a') as errorfile:
                    errorfile.write('3' + ',' + str(item))
                    errorfile.write('\n')
            for item in fi3:
                with open('finish.csv', 'a') as finishfile:
                    finishfile.write('3' + ',' + str(item))
                    finishfile.write('\n')

if __name__ =='__main__':
    sortCsv(dele=True, filenum=1, num=674)
