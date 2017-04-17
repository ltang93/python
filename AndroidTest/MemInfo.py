import os,re,time
from AndroidTest import makechart

class Start(object):
    def __init__(self,count):
        self.vsslist=[]
        self.rsslist=[]
        self.count=count
        self.cmd=''
    def MemInfo(self):
        cmd='adb shell top -d 1 -n +'+str(self.count)
        self.cmd=os.popen(cmd).read()
    def FindData(self):
        for line in self.cmd.split('\n'):
            if 'com.android.mms' in line:
                replaceone = re.compile(r'\s+')
                data = replaceone.sub(' ', line)
                self.vsslist.append(data.split(' ')[6])
                self.rsslist.append(data.split(' ')[7])
        return self.vsslist,self.rsslist

class Begin(object):
    def __init__(self,second):
        self.second=second
        self.s=Start(self.second)
    def RunForTimes(self):
        self.s.MemInfo()
        time.sleep(self.second)
    def RecordCSV(self):
        vsslist,rsslist=self.s.FindData()
        print('vss:'+str(vsslist)+'\nrss:'+str(rsslist))
        m1 = makechart.chart()
        for vss in vsslist:
            m1.WriteTime(timein=vss.replace('K',''))
        m1.DrawChart(name='MemvssInfo', title='mem')
        m2=makechart.chart()
        for rss in rsslist:
            m2.WriteTime(timein=rss.replace('K',''))
        m2.DrawChart(name='MemrssInfo',title='mem')

if __name__ == '__main__':
    b=Begin(5)
    b.RunForTimes()
    b.RecordCSV()