from selenium import webdriver
import time
from auto_table import table_para
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import csv
from auto_table.common import add_field

es_01 = ["https://dms.t.hxqcgf.com/#/sso/","HD340400","A04L","aA250252614!"]   #测试线
es_02 = ["https://dms.hxqcgf.com/#/sso/",'HD420610','A0KJ','aA3251002!']     #预上线
es_03 = ["https://pacss.hxqcgf.com/",'HX420125',"GXTR",'aA3251002!']    #正式线
es = es_03  #环境配置

driver=webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(es[0])
driver.maximize_window()

#输入账号密码
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/input').send_keys(es[1])
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/div/div/input').send_keys(es[2])
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[3]/div/div/input').send_keys(es[3])

#生成动作链对象
actions = ActionChains(driver)
element_slider=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[4]/div/div[3]')
actions.drag_and_drop_by_offset(element_slider,500,10).perform()   #拖动滑块
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[5]/button').click()  #登录

#添加展开行
# def add_deploy():
#     f = csv.reader(open(r"D:\xiong\hello_world\auto_table\table_data\调配弹出框", encoding='utf-8'))
#     # driver.find_element_by_xpath('//input[@placeholder="触发按钮名称"]').send_keys("查看人员")  # 输入按钮名称
#     # driver.find_element_by_xpath('//input[@placeholder="展示形式"]').click()  # 输入按钮名称
#     # driver.find_element_by_xpath('//span[text()="弹框"]').click()  # 点击弹框
#     n=0
#     for i in f:
#         n+=1
#         c = i[0].split('\t')
#         driver.find_element_by_xpath('//span[text()=" 添加列"]').click()  # 点击弹框
#         time.sleep(0.5)
#         e1=f'//span[text()="展 示 形 式："]/../following-sibling::div[{n}]/div[1]/div/div/input'
#         e2=f'//span[text()="展 示 形 式："]/../following-sibling::div[{n}]/div[2]/div/div/input'
#         driver.find_element_by_xpath(e1).send_keys(c[0])  # 输入列名称
#         time.sleep(0.2)
#         driver.find_element_by_xpath(e2).send_keys(c[1])  # 输入列字段
#         time.sleep(0.2)



def add_deploy():
    f = csv.reader(open(r"D:\xiong\hello_world\auto_table\table_data\转正申请弹出框", encoding='utf-8'))
    # driver.find_element_by_xpath('//input[@placeholder="触发按钮名称"]').send_keys("查看人员")  # 输入按钮名称
    # driver.find_element_by_xpath('//input[@placeholder="展示形式"]').click()  # 输入按钮名称
    # driver.find_element_by_xpath('//span[text()="弹框"]').click()  # 点击弹框
    n=0
    for i in f:
        n+=1
        c = i[0].split('\t')
        driver.find_element_by_xpath('//span[text()="添加"]').click()  # 点击弹框
        time.sleep(0.5)
        e1=f'//span[text()="添加"]/../../following-sibling::div[1]/ul/li[{n}]/div[1]/input'
        e2=f'//span[text()="添加"]/../../following-sibling::div[1]/ul/li[{n}]/div[2]/input'
        driver.find_element_by_xpath(e1).send_keys(c[0])  # 输入列名称
        time.sleep(0.2)
        driver.find_element_by_xpath(e2).send_keys(c[1])  # 输入列字段
        time.sleep(0.2)
