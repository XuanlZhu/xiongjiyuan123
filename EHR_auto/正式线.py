from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#初始化
driver=webdriver.Chrome()
driver.implicitly_wait(8)
driver.get("https://pacss.hxqcgf.com/#/sso/")
driver.maximize_window()

#输入账号密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/input').send_keys('HX420125')
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/div/div/input').send_keys('GXTR')
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[3]/div/div/input').send_keys('aA3251002!')

#生成动作链对象
actions = ActionChains(driver)
element_slider=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[4]/div/div[3]')
actions.drag_and_drop_by_offset(element_slider,500,10).perform()   #拖动滑块
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[5]/button').click()  #登录


