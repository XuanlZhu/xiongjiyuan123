# _*_ coding: UTF-8 _*_
# # @Time :2020/1/6 4:35
# # @Author : Xuanl Zhu
# # @Site : 
# # @File :home_page.py
# # @Software : PyCharm

from po.common.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage():
    url = 'http://www.baidu.com/'
    element_search = (By.ID, 'kw')
    element_search_submit = (By.ID,'su')











