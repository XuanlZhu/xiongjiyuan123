import unittest
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction

desired_caps={}
desired_caps['platformName'] = 'Android'  # 系统名称
desired_caps['platformVersion'] = '5.1.1'  # 系统版本号
desired_caps['deviceName'] = 'Android Xiong'  # 设备名称
desired_caps['appPackage'] = 'hxqc.com.business'  # app包名
desired_caps['appActivity'] = 'com.hxqc.business.activity.LaunchActivity'  # app入口的activity
desired_caps['noReset'] = 'True'  # 不重置app的缓存文件
desired_caps['unicodeKeyboard'] = 'True'  # 设置键盘支持中文输入
desired_caps['resetKeyboard'] = 'True'  # 重置键盘

# 连接appium server,告诉appium，代码要操作哪个设备上的哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
ta = TouchAction(driver)  # 实例化一个touchaction
# 解包aapt dump badging D:\calculator.apk > d:\log.txt

driver.implicitly_wait(8)