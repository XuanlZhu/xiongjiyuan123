from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(8)
driver.get("http://localhost/upload/admin/index.php")
driver.maximize_window()

# WebDriverWait(driver,8).until(expected_conditions.visibility_of_element_located((By.ID,'su')))
driver.find_element_by_name("username").send_keys("a250252614a")
driver.find_element_by_name("password").send_keys("a3251002a")
driver.find_element_by_xpath('//input[@value="进入管理中心"]').click()


driver.switch_to.frame('menu-frame')#菜单

time.sleep(0.2)
driver.find_element_by_xpath('//*[@id="menu-ul"]/li[1]').click()
driver.find_element_by_link_text("商品列表").click()

driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')

time.sleep(0.2)
# driver.find_element_by_name('is_on_sale').click()
Select(driver.find_element_by_name('is_on_sale')).select_by_visible_text("下架")











