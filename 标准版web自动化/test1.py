from selenium import webdriver
import time
from auto_table import table_para
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import csv
from auto_table.common import add_field
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from 标准版web自动化.id_code import create_id_code
import win32gui,win32con,win32api
from selenium.webdriver.support.select import Select
import unittest

# 环境设置
es1 = "http://epm.boxingqiche.com:19061/sso/platform.do"

driver=webdriver.Chrome()
driver.implicitly_wait(8)
driver.get(es1)
driver.maximize_window()
time.sleep(0.5)



#输入账号密码
driver.find_element_by_xpath('//*[@id="login_form"]/form/div[2]/label/input').send_keys("ST000000")
driver.find_element_by_xpath('//*[@id="login_form"]/form/div[3]/label/input').send_keys("Admin")
driver.find_element_by_xpath('//*[@id="login_form"]/form/div[4]/label/input').send_keys("2019standard!")

#生成动作链对象
actions = ActionChains(driver)
element_slider=driver.find_element_by_xpath('//*[@id="mpanel1"]/div/div/div')
actions.drag_and_drop_by_offset(element_slider,500,10).perform()   #拖动滑块
driver.find_element_by_xpath('//*[@id="button"]').click()  #登录

#进入界面
driver.find_element_by_xpath('/html/body/div[3]/ul/li[6]/a/img').click()  #点击EHR
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="details-header-top"]/ul/li[4]/a').click()  #点击切换店铺
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="select_combbox"]/span/input[1]').clear()  #清空内容
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="select_combbox"]/span/input[1]').send_keys("ST999991郑州博行测试店铺")  #输入店铺
time.sleep(1)

driver.find_element_by_xpath('//*[@id="changeCompany"]').click()  #点击切换
time.sleep(0.1)


#已切换店铺################################################################################################################

# 切换到父frame
time.sleep(0.5)
driver.switch_to.parent_frame()

driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[4]/p').click()  # 点击人员变动管理
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[4]/ul/li[3]/p').click()  # 点击人员离职
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[4]/ul/li[3]/ul/li[1]/a').click()  # 点击离职申请
time.sleep(0.5)

# 切换到子frame
driver.switch_to.frame(driver.find_element_by_name('a42'))

driver.find_element_by_xpath('//*[@id="add"]').click()  # 点击增加
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="vexplain"]').send_keys('1')  # 输入离职说明
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="effectdate"]').click()  # 点击生效日期
time.sleep(0.1)

# 切换到父frame
driver.switch_to.parent_frame()

# 切换到子frame
driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div[3]/iframe'))

driver.find_element_by_xpath('//*[@id="dpTodayInput"]').click()  # 选择今天

# 切换到父frame
driver.switch_to.parent_frame()

# 切换到子frame
driver.switch_to.frame(driver.find_element_by_name('a42'))

driver.find_element_by_xpath('//*[@id="html_1"]/div[1]/ul/li[3]/button').click()  # 点击编辑人员
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="selectPeople"]/button').click()  # 点击增加人员
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="company_dep_tree"]').click()  # 点击店铺
time.sleep(0.5)

psn_id = '21031008'
driver.find_element_by_xpath('//*[@id="aaa"]').send_keys(psn_id)  # 输入人员编码
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="tb"]/a').click()  # 点击搜索
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]/td[1]/div').click()  # 勾选人员
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div[3]/button').click()  # 点击确认选择
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="html_2"]/div[2]/div/div[2]/div/div[2]/div[2]/input').click()  # 点击搜离职后类别
time.sleep(1)

driver.find_element_by_xpath('//*[@id="datagrid-row-r3-2-0"]/td[1]/div').click()  # 选择离职类别
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="psncl-btn"]').click()  # 点击确定
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="html_2"]/div[1]/ul/li[3]/button').click()  # 点击保存
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="save"]').click()  # 点击保存
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击保存
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]').click()  # 选中单据
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="submitCheck"]').click()  # 点击提交
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()  # 点击确定
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()  # 点击确定
time.sleep(0.5)

# 切换到父frame
driver.switch_to.parent_frame()

driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[4]/ul/li[3]/ul/li[2]/a').click()  # 点击调配审批
time.sleep(0.5)

# 切换到子frame
driver.switch_to.frame(driver.find_element_by_name('a43'))

ActionChains(driver).double_click(driver.find_element_by_id('datagrid-row-r1-2-0')).perform()  # 双击单据
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="audit"]').click()  # 点击审批操作
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="approveCheck"]/a').click()  # 点击批准
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="audit_submit"]').click()  # 点击确定
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击确定
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="audit"]').click()  # 点击审批操作
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="approveCheck"]/a').click()  # 点击批准
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="audit_submit"]').click()  # 点击确定
time.sleep(0.5)

driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击确定
time.sleep(0.5)