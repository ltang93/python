import os
import time
import re
from AndroidTest import makechart

class Start(object):
    def __init__(self):
        self.datalist=[]
    def DataUsage(self):
        Receive = 0
        Transmit = 0
        replacenone=re.compile(r'\s+')
        cmd='adb shell ps | findstr com.android.browser'
        pid=replacenone.sub(' ',os.popen(cmd).read()).split(' ')[1]
        cmd='adb shell cat /proc/'+pid+'/net/dev'
        for line in os.popen(cmd).read().split('\n'):
            if 'eth' in line:
                Receive=Receive+int(replacenone.sub(' ',line.split(':')[1]).split(' ')[1])
                Transmit=Transmit+int(replacenone.sub(' ',line.split(':')[1]).split(' ')[9])
        self.datalist.append(Receive+Transmit)
        # print(self.datalist)
    def FindData(self):
        # print('finddata'+str(self.datalist))
        return self.datalist

class begin(object):
    def __init__(self,second=1):
        self.second=second
        self.s = Start()
        self.datalist=[]
    def RunForTimes(self):
        while self.second>0:
            self.s.DataUsage()
            time.sleep(1)
            print(self.second)
            self.second-=1
        self.datalist=self.s.FindData()
    def RecordCSV(self):
        c=makechart.chart()
        print(self.datalist)
        l=len(self.datalist)-1
        while l >0:
            data=self.datalist[l]-self.datalist[l-1]
            c.WriteTime(data)
            l-=1
        c.DrawChart(name='DataUsage',title='bit')
if __name__ == '__main__':
    b=begin(5)
    b.RunForTimes()
    b.RecordCSV()