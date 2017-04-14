import os
import time
from AndroidTest import makechart

class Start(object):
    def __init__(self):
        self.content=''
        self.CPUlist=[]
    def CPUInfo(self):
        cmd='adb shell dumpsys cpuinfo | findstr com.android.mms'
        self.content=os.popen(cmd).read()
    def FindCpuData(self):
        self.CPUlist.append(self.content.split('%')[0])
        print(self.CPUlist)
        return self.CPUlist

class begin(object):
    def __init__(self,count):
        self.count=count
        self.CPUs=[]
    def RunForTimes(self):
        s=Start()
        for i in range(self.count):
            s.CPUInfo()
            self.CPUs=s.FindCpuData()
            time.sleep(5)
    def RecordCSV(self):
        c=makechart.chart()
        for cputime in self.CPUs:
            c.WriteTime(cputime)
        c.DrawChart(name='CpuInfo',title='percent')

if __name__ == '__main__':
    b=begin(5)
    b.RunForTimes()
    b.RecordCSV()