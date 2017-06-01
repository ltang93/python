import time,sys

def wday(datein):
    day=time.localtime(time.time()).tm_mday
    if(str(datein.split('-')[-1])==str(day)):
        # print('true')
        return True
    else:
        # print('false')
        return False

def wtime(timein):
    timein=timein.replace(':','')
    return timein

def totime(totimein):
    if(len(str(totimein))==3):
        totimein=str(totimein)[0]+':'+str(totimein)[1:]
    elif(len(str(totimein))==4):
        totimein=str(totimein)[0:2]+':'+str(totimein)[2:]
    #print(totimein)
    return totimein

# print(time.localtime(time.time()))
# wday('2017-06-22')
#wtime('9:41')
# totime(941)
# totime(1012)

# timelist=[930,1000,1100,1200,1400,1300,1453,1210]
# timelist.append(1150)
# timelist=sorted(timelist)
# print(timelist)
#
# for i in range(1,5):
#     if timelist[timelist.index(1150)+i+1]-timelist[timelist.index(1150)+i]>15:
#         print('当天吃饭时间为 ：'+str(totime(timelist[timelist.index(1150)+i]))+' - '+str(totime(timelist[timelist.index(1150)+i+1])))
#         break

# print(sys.path[0])