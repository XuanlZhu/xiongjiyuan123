# _*_ coding: UTF-8 _*_
# @Time : 2020/1/2 10:30
# @Author : Xuanl Zhu
# @Site : 
# @File : zentao_login.py
# @Software : PyCharm

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#定义禅道的登录界面
class ZentaoLogin:
    #变量
    def __init__(self,driver):
        self.driver = driver#driver在实例化对象时传入
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,60)#实例化wait对象

        self.url = 'http://127.0.0.1/zentao/user-login.html'
        self.title = '用户登录 - 禅道'

        #定位符
        self.user_id = 'account'#user:id
        self.pawd_name = 'password'#pwd:name
        self.rem_pwd_id = 'keepLogin[]'#remeber_pwd:id
    #方法
    #输入用户名
    def input_user(self,user):
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID,self.user_id)))
        self.driver.find_element_by_id('self.user_id').clear()
        self.driver.find_element_by_id('self.user_id').send_keys(user)

    #输入密码
    def input_pwd(self,pwd):
        self.wait.until(expected_conditions.visibility_of_element_located((By.NAME,self.pawd_name)))
        self.driver.find_element_by_id('self.pawd_name').clear()
        self.driver.find_element_by_id('self.pawd_name').send_keys(pwd)

    #记住密码
    def click_remeber_pwd(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.NAME, self.pawd_name)))

    #点击登录
    def click_login(self):
        pass

    #点击忘记密码
    def forget_pwd(self):


    #切换语言

