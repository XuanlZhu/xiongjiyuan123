# _*_ coding:UTF-8 _*_
# @Time     :2020/3/20 18:20
# @Author   :Xiong

import unittest
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction


class CalTest(unittest.TestCase):
    #用例3要素：前置条件，测试输入，预期结果

    def setUp(self) -> None:
        desired_caps={}
        desired_caps['platformName'] = 'Android' #系统名称
        desired_caps['platformVersion']= '5.1.1' #系统版本号
        desired_caps['deviceName']= 'Android Xiong' #设备名称
        desired_caps['appPackage'] = 'com.netease.cloudmusic' #app包名
        desired_caps['appActivity'] = 'com.netease.cloudmusic.activity.LoadingActivity' #app入口的activity
        desired_caps['noReset']='True' #不重置app的缓存文件
        desired_caps['unicodeKeyboard']='True' #设置键盘支持中文输入
        desired_caps['resetKeyboard']='True' #重置键盘

        #连接appium server,告诉appium，代码要操作哪个设备上的哪个app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.ta = TouchAction(self.driver) #实例化一个touchaction
        #解包aapt dump badging D:\calculator.apk > d:\log.txt



    #测试输入
    def test_001(self):
        # self.driver.find_element_by_id().click()
        # self.driver.find_element_by_id()

        #tap,单次点击
        time.sleep(7)
        # self.ta.tap(self.driver.find_element_by_id('com.netease.cloudmusic:id/agree')).perform()
        self.ta.tap([(12,23)])
        # time.sleep(3)

        #向下滑动
        # self.driver.swipe(720/2,1280/2,720/2,1280/2+200)
        # time.sleep(3)
        # self.action.press(x=720/2,y=1280/2).wait(1000).move_to(x=720/2,y=1280/2+400).release().perform()
        # time.sleep(3)

        #向上滑动
        # self.driver.swipe(360,640,360,640-500)
        # time.sleep(3)

        #输入
        # self.driver.find_element_by_id().send_keys()

        #按压
        self.action.press(self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.RelativeLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.LinearLayout[1]/android.widget.FrameLayout[4]/android.widget.ImageView')).release().perform()
        time.sleep(3)

        




    #后置处理
    def tearDown(self) -> None:
        self.driver.quit()

#进行调试
if __name__=="__main__":
    CalTest.test_001()

