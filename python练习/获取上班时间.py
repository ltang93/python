import sys,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
#sys.path.append('\\'.join(os.getcwd().split('\\')[:-1]))
sys.path.append('\\'.join(sys.path[0].split('\\')[:-1]))
from python练习 import 时间

driver=webdriver.PhantomJS()
#mainhandle=driver.current_window_handle  #获得主页句柄
driver.get('http://eipinfo.aspirecn.com/default.aspx')
print('已进入：'+driver.title+' ,开始获取...')
driver.get(driver.find_element_by_link_text('考勤审批').get_attribute('href'))
#driver.find_element_by_link_text('考勤审批').click()
#driver.close()
time.sleep(5)
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
driver.switch_to.frame('Frame_Content')
loc=driver.find_element_by_id('ContentPlaceHolder1_btn_UserSearch').send_keys(Keys.ENTER)

times=driver.find_element_by_id('ContentPlaceHolder1_panel_User')
# for i in range(30):
#     try:
#         times=driver.find_element_by_id('ContentPlaceHolder1_panel_User')
#         if times.is_displayed():
#             print('Click')
#             break
#     except:
#         pass
#     time.sleep(1)
#     print(str(i))
#     if i==29:
#         print('Time out.')
#         driver.close()
#         sys.exit()


soup=BeautifulSoup(driver.page_source,"html.parser").find('table',attrs={'id':'ContentPlaceHolder1_GridView_User'}).find_all('td')
i=0
day=False
time=2400
timelist=[]
for tds in soup:
    i=i+1
    if(i==2):
        day=时间.wday(tds.get_text())
    if(i==3 and day==True):
        trytime=时间.wtime(tds.get_text())
        if int(trytime) < int(time):
            time = trytime
        timelist.append(int(trytime))
    if(i==4):
        i=0
        day=False
driver.close()
print('上班时间为：'+str(时间.totime(time)))

# timelist=[930,1000,1100,1200,1400,1300,1453]
timelist.append(1200)
timelist=sorted(timelist)

for i in range(1,8):
    try:
        if timelist[timelist.index(1200)+i+1]-timelist[timelist.index(1200)+i]>15:
            print('当天吃饭时间为 ：'+str(时间.totime(timelist[timelist.index(1200)+i]))+' - '+str(时间.totime(timelist[timelist.index(1200)+i+1])))
            break
    except:
        pass
'''



'''