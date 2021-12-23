from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller

driver=webdriver.Chrome()
driver.implicitly_wait(60)
driver.get("https://www.jd.com/")
driver.maximize_window()
keyboard = Controller()


def xiong1():
    win1 = driver.window_handles
    driver.switch_to.window(win1[1])
    e1 = driver.find_element_by_xpath('//*[@class="options-box"]/div/div/input')  #全选按钮

    # def try_click():
    #     try:
    #         e1.click()
    #         print("点击全选")
    #         time.sleep(0.2)
    #         statu = e1.get_attribute("clstag")
    #         print(statu)
    #         if statu != "pageclick|keycount|Shopcart_CheckAll|1":
    #             try_click()
    #     except:
    #         try_click()
    #点击全选
    while True:
        statu = e1.get_attribute("clstag")
        print(statu)
        if statu == "pageclick|keycount|Shopcart_CheckAll|1":
            break

    driver.find_element_by_class_name("btn-area").click()



    # keyboard.type('250252')
    driver.find_element_by_xpath('//*[@id="order-submit"]').click()  #提交订单



def mima():
    win1 = driver.window_handles
    driver.switch_to.window(win1[1])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="quark-pw-list"]/i[1]').click()
    keyboard.type('250252')



    # def try_click2():
    #     try:
    #         driver.find_element_by_id("order-submit").click()
    #     except:
    #         try_click2()
    # #点击提交
    # try_click2()