from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


driver=webdriver.Chrome()
driver.get("http://localhost/upload/article.php?id=33")
driver.maximize_window()



driver.find_element_by_xpath('//div[@class="left_help clearfix"]/dl/dd[1]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@class="left_help clearfix"]/dl/dd[2]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//div[@class="left_help clearfix"]/dl/dd[3]/a').click()
time.sleep(1)


