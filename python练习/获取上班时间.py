from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from python练习 import 时间
import time

driver=webdriver.Ie()
mainhandle=driver.current_window_handle  #获得主页句柄
driver.get('aspireurl')
driver.find_element_by_link_text('考勤审批').click()
driver.close()
time.sleep(5)
for handle in driver.window_handles:
    driver.switch_to.window(handle)
driver.switch_to.frame('Frame_Content')
loc=driver.find_element_by_id('ContentPlaceHolder1_btn_UserSearch').send_keys(Keys.ENTER)
for i in range(30):
    try:
        times=driver.find_element_by_id('ContentPlaceHolder1_panel_User')
        if times.is_displayed():
            print('Click')
            break
    except:
        pass
    time.sleep(1)
    print(str(i))
    if i==29:
        print('Time out.')


soup=BeautifulSoup(driver.page_source,"html.parser").find('table',attrs={'id':'ContentPlaceHolder1_GridView_User'}).find_all('td')
i=0
day=False
time=2400
for tds in soup:
    i=i+1
    if(i==2):
        day=时间.wday(tds.get_text())
    if(i==3 and day==True):
        trytime=时间.wtime(tds.get_text())
        if int(trytime) < int(time):
            time = trytime
    if(i==4):
        i=0
        day=False
#driver.quit()
print(str(时间.totime(time)))



'''



'''