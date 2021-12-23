import unittest
import traceback
import time
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import sys
import threading




class TestHomePage(unittest.TestCase):


    def setUp(self) -> None:
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'  # 系统名称
        self.desired_caps['platformVersion'] = '5.1.1'  # 系统版本号
        self.desired_caps['deviceName'] = 'Android Xiong'  # 设备名称
        self.desired_caps['appPackage'] = 'hxqc.com.business'  # app包名
        self.desired_caps['appActivity'] = 'com.hxqc.business.activity.LaunchActivity'  # app入口的activity
        self.desired_caps['noReset'] = 'True'  # 不重置app的缓存文件
        self.desired_caps['unicodeKeyboard'] = 'True'  # 设置键盘支持中文输入
        self.desired_caps['resetKeyboard'] = 'True'  # 重置键盘

        # 连接appium server,告诉appium，代码要操作哪个设备上的哪个app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.ta = TouchAction(self.driver)  # 实例化一个touchaction
        # 解包aapt dump badging D:\calculator.apk > d:\log.txt

        self.driver.implicitly_wait(8)



    def test_001(self):
        while True:
            try:
                self.driver.find_element_by_id('hxqc.com.business:id/k5').click()
                #点击移动考勤
            except:
                time.sleep(0.3)
            else:
                break

        while True:
            try:
                self.driver.find_element_by_id('hxqc.com.business:id/hz').click()
                #点击打卡
            except:
                time.sleep(0.3)
            else:
                break

        time.sleep(1)
        while True:
            try:
                self.driver.find_element_by_id('hxqc.com.business:id/ia').click()
                #打卡
            except:
                time.sleep(0.3)
            else:
                break

        while True:
            time.sleep(0.1)
            try:
                self.driver.find_element_by_id('android:id/button2').click()
                # 标记下班卡
            except:
                pass

            try:
                text=self.driver.find_element_by_id('hxqc.com.business:id/bbg').text
                #获取打卡消息
            except:
                time.sleep(0.1)
            else:
                break

        assert '打卡成功' in text

    def tearDown(self) -> None:
        self.driver.quit()



