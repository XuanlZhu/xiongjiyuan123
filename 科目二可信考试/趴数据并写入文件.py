import json

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import csv
from auto_table.common import add_field
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



#初始化


driver=webdriver.Chrome()
driver.implicitly_wait(8)
driver.get("https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDIsNiw0LDEsNSw3LDgsOQ%3D%3D&word=cos")
driver.maximize_window()

time.sleep(0.5)
els = driver.find_elements(By.XPATH,"//div[@id='imgid']/div[1]/ul/li")
a = []
for i in els:
    time.sleep(0.1)
    a.append(i.text)


print(a)
with open("shi.txt",mode="r+",encoding="utf-8") as f:
    f.write(json.dumps(a,ensure_ascii=False))

