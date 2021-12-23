# _*_ coding: UTF-8 _*_
# # @Time :2020/1/6 4:48
# # @Author : Xuanl Zhu
# # @Site : 
# # @File :test_home_page.py
# # @Software : PyCharm

import unittest
from selenium import webdriver
from po.pages.home_page import HomePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys



class TestHomePage(unittest.TestCase):
    def setUp(self) -> None:
        self.home_page = HomePage()
        self.home_page.setUp('http://www.baidu.com/')

    def test_001(self):
        self.home_page.sendkeys(self.home_page.element_search,'ni ma si le')
        self.home_page.click(self.home_page.element_se)
        time.sleep(1)


    def tearDown(self) -> None:
        self.home_page.driver.quit()
