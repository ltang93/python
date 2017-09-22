from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



def login():
    driver = webdriver.Ie()
    driver.get('http://192.168.117.241:8084/swt_cms')
    driver.find_element_by_name('username').send_keys('wuqiong')
    driver.find_element_by_id('passwords').send_keys('test@123')
    for i in range(5):
        if driver.find_element_by_name('post_validate_code').get_attribute('value')  == '':
            time.sleep(10)
            if i==4:
                driver.quit()
        else:
            driver.find_element_by_class_name('Login_button').click()
            return driver

def mmstest(driver,count):
    time.sleep(15)
    driver.find_element_by_id('panel-1036_header_hd').click()

    for _ in range(count):
        driver.find_elements_by_class_name('x-tree-node-text')[4].click()
        driver.find_element_by_css_selector("[data-qtip=最后页]").click()
        driver.find_element_by_name('productId').send_keys('10261')
        driver.find_element_by_name('productId').send_keys(Keys.ENTER)
        page=driver.find_elements_by_css_selector('.x-toolbar-text.x-box-item.x-toolbar-item.x-toolbar-text-default')[2].text
        if '显示记录 1 - 20' not in str(page):
            print(page)
        driver.find_element_by_class_name('x-tab-close-btn').click()
        time.sleep(2)

if __name__ == '__main__':
    driver=login()
    mmstest(driver,100)

