import sys
sys.path.append(r'D:\xiong\hello_world')
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pacs_release.SMTP  import smtp
from pacss测试线.id_code import create_id_code
import win32gui,win32api,win32con

driver=webdriver.Chrome()
driver.implicitly_wait(8)
driver.get("https://dms.t.hxqcgf.com/#/sso/login")
driver.maximize_window()

#输入账号密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/input').send_keys("HD340400")
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/div/div/input').send_keys("A04L")
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[3]/div/div/input').send_keys("aA3251002!")

#生成动作链对象
actions = ActionChains(driver)
element_slider=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[4]/div/div[3]')
actions.drag_and_drop_by_offset(element_slider,500,10).perform()   #拖动滑块
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[5]/button').click()  #登录
print("登录成功")

driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[10]').click()  # 点击人资系统
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="fir_ul"]/li[4]').click()  # 点击人才招聘管理
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="fir_ul"]/li[4]/ul/li[3]/ul/li[3]').click()  # 点击报到入职确认






