import unittest
from appium import webdriver
from ddt import ddt,data,unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    @data(('1','1'),('3','13'),('6','136'))
    @unpack
    def test_something(self,num,value):
        self.driver.find_element_by_name(num).click()
        self.assertEqual(self.driver.find_element_by_name(value).is_displayed(), True)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
