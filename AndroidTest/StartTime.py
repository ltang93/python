import os
import time
from AndroidTest import makechart

class Start(object):
    def __init__(self):
        self.content=''
        self.timelist = []
    def run(self):
        cmd='adb shell am start -W -n com.android.mms/.ui.ConversationList'
        self.content=os.popen(cmd).read()
    def stop(self):
        cmd='adb shell am force-stop com.android.mms'
        os.popen(cmd)
    def FindTime(self):
        for times in self.content.split('\n'):
            if 'ThisTime' in times:
                #self.Time=times.split(':')[1]
                self.timelist.append(times.split(':')[1])
                print(str(self.timelist))
                break
        return self.timelist


class begin(object):
    def __init__(self,count):
        self.count=count
        self.times=[]
    def RunForTimes(self):
        s=Start()
        for i in range(self.count):
            print('Running no.'+str(i+1)+' time')
            s.run()
            time.sleep(3)
            s.stop()
            time.sleep(3)
            self.times=s.FindTime()
            time.sleep(5)
    def RecordCSV(self):
        m=makechart.chart()
        for onetime in self.times:
            m.WriteTime(onetime)
            #print(onetime)
        m.DrawChart()


if __name__ == '__main__':
    b=begin(5)
    b.RunForTimes()
    b.RecordCSV()