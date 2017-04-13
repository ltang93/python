import time

def wday(datein):
    day=time.localtime(time.time()).tm_mday
    if(str(datein[-2:])==str(day)):
        return True
    else:
        return False

def wtime(timein):
    timein=timein.replace(':','')
    return timein

def totime(totimein):
    if(len(str(totimein))==3):
        totimein=str(totimein)[0]+':'+str(totimein)[1:]
    elif(len(str(totimein))==4):
        totimein=str(totimein)[0:2]+':'+str(totimein)[2:]
    return totimein

#print(time.localtime(time.time()))
#wday('2017-03-24')
#wtime('9:41')
#totime(941)
#totime(1012)