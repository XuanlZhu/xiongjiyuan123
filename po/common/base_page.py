# _*_ coding: UTF-8 _*_
# # @Time :2020/1/6 3:53
# # @Author : Xuanl Zhu
# # @Site : 
# # @File :base_page.py
# # @Software : PyCharm

from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# self.driver = webdriver.Chrome()
# self.driver.maximize_window()
# self.driver.get('https://www.baidu.com/')
class BasePage:
    def __init__(self):
        pass#element格式(by,value) ('id','')('xpath','')('link text','')

    def setUp(self,url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver,5)

    def wait_element(self,element):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(element))
        except:
            self.driver.get_screenshot_as_file('../log/找不到元素%s %s.png' % (' '.join(element),time.strftime('%Y-%m-%d %H %M %S', time.gmtime())))

    def text(self,element):
        self.wait_element(element)
        try:
            self.driver.find_element(*element).text
        except:
            pass




    def click(self,element):
        self.wait_element(element)
        try:
            self.driver.find_element(*element).click()
        except:
            pass

    def sendkeys(self,element,value):
        self.wait_element(element)
        try:
            self.driver.find_element(*element).send_keys(value)
        except:
            pass

    def clear(self,element):
        self.wait_element(element)
        try:
            self.driver.find_element(*element).clear()
        except:
            pass










