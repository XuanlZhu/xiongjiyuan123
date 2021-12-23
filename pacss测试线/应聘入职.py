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
driver.find_element_by_xpath('//*[@id="fir_ul"]/li[4]/ul/li[2]/ul').click()  # 点击应聘人员登记

#应聘登记
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[2]/table/tbody')))
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/button[1]').click()  # 点击增加
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/button[3]').click()  # 点击手工修改

driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[2]/div/div/div/input').send_keys("2021-04-26")  # 选择面试日期
driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[3]/div/div/div/input').send_keys("13:58:00")  # 选择面试日时间
driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[4]/div/div/div/div/input').click()  # 点击应聘岗位
driver.find_element_by_xpath('//span[text()="GW00234总经理"]').click()  # 选择应聘岗位
driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[5]/div/div/div/input').send_keys("测试")  # 输入姓名
driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[6]/div/div/div/div/input').click()  # 点击性别
driver.find_element_by_xpath('//span[text()="男"]').click()  # 选择性别
driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[7]/div/div/div/div/input').click()  # 点击民族
driver.find_element_by_xpath('//span[text()="汉族"]').click()  # 选择民族
id_card = create_id_code()
driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[8]/div/div/div[1]/input').send_keys(id_card)  # 输入身份证
driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[9]/div/div/div/div/input').click()  # 点击渠道
driver.find_element_by_xpath('//span[text()="前程无忧"]').click()  # 选择渠道
driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[13]/div/div/div[1]/input').send_keys("17762538939")  # 输入手机号


#维护紧急联系人
# driver.find_element_by_xpath('//*[@id="tab-6"]').click()  # 点击紧急联系人
# driver.find_element_by_xpath('//*[@id="pane-6"]/form/p/button').click()  # 点击增行
# driver.find_element_by_xpath('//*[@id="pane-6"]/form/p/button').click()  # 点击增行

# driver.find_element_by_xpath('//*[@id="pane-6"]/form/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/div').click()  # 点击与本人关系
# time.sleep(0.1)
# driver.find_element_by_xpath('/html/body/div[16]/div[1]/div[1]/ul/li[2]').click()  # 选择父亲
# driver.find_element_by_xpath('//*[@id="pane-6"]/form/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/div/div/div/div/input').send_keys("1")  # 输入姓名
# driver.find_element_by_xpath('//*[@id="pane-6"]/form/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/div/div/div/div/input').send_keys("303657182607164509")  # 输入身份证号码
# driver.find_element_by_xpath('//*[@id="pane-6"]/form/div/div[2]/div[2]/table/tbody/tr[1]/td[6]/div/div/div/div/input').send_keys("17762538939")  # 输入电话
#
# driver.find_element_by_xpath('//*[@id="pane-6"]/form/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/div/div/div').click()  # 点击与本人关系
# time.sleep(0.1)
# driver.find_element_by_xpath('/html/body/div[17]/div[1]/div[1]/ul/li[3]').click()  # 选择母亲
# driver.find_element_by_xpath('//*[@id="pane-6"]/form/div/div[2]/div[2]/table/tbody/tr[2]/td[4]/div/div/div/div/input').send_keys("1")  # 输入姓名
# driver.find_element_by_xpath('//*[@id="pane-6"]/form/div/div[2]/div[2]/table/tbody/tr[2]/td[5]/div/div/div/div/input').send_keys("303657182607164509")  # 输入身份证号码
# driver.find_element_by_xpath('//*[@id="pane-6"]/form/div/div[2]/div[2]/table/tbody/tr[2]/td[6]/div/div/div/div/input').send_keys("17762538939")  # 输入电话

driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/button[1]').click()  # 点击保存
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[@role="alert"]/p')))
assert driver.find_element_by_xpath('/html/body/div[@role="alert"]/p').text == "操作成功"

time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[3]/div/div/button[2]').click()  # 点击编辑
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/button[5]')))
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/button[5]').click()  # 点击打印
time.sleep(0.3)
driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/button[2]').click()  # 点击确定
time.sleep(1)

# 点击取消打印
handle_chrome = win32gui.FindWindow("Chrome_WidgetWin_1", "恒信汽车集团业务管理系统 - Google Chrome")
handle = win32gui.FindWindowEx(handle_chrome, None, "Chrome_RenderWidgetHostHWND", "Chrome Legacy Window")
position = win32api.MAKELONG(1260, 828)
win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, position)
win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, position)

driver.find_element_by_xpath('//*[@id="pane-basicInfo"]/div[1]/form/div[1]/div[22]/div/div/div/input').send_keys("2021-04-27")  # 输入入职日期
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/button[1]').click()  # 点击保存
time.sleep(0.3)
driver.find_element_by_xpath('/html/body/div[10]/div/div[3]/button[2]').click()  # 点击确定
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[@role="alert"]/p')))
assert driver.find_element_by_xpath('/html/body/div[@role="alert"]/p').text == "操作成功"
time.sleep(1)

#录用申请
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/span').click()  # 点勾选人员
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/button').click()  # 点击业务操作
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//li[text()="申请录用"]')))
driver.find_element_by_xpath('//li[text()="申请录用"]').click()  # 点击申请录用
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div[2]/div/div/div/input').send_keys("asd123345")  # 输入单据编号
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[1]/div[7]/div/div/div').click()  # 点击编制类型
driver.find_element_by_xpath('//span[text()="正式编制"]').click()  # 选择编制类型
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/div/div/div/div/input').send_keys("2021-04-27")  # 选择计划报道日期
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div[2]/div[2]/table/tbody/tr/td[3]/div/div/div').click()  # 点击录用部门
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[text()="人事行政部"]')))
driver.find_element_by_xpath('//span[text()="人事行政部"]').click()  # 选择财务部
time.sleep(0.3)
driver.find_element_by_xpath('//span[text()="后勤部"]').click()  # 选择财务部

driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div[2]/div[2]/table/tbody/tr/td[4]/div/div/div').click()  # 点击岗位
driver.find_element_by_xpath('//span[text()="司机"]').click()  # 选择岗位

driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div[2]/div[2]/table/tbody/tr/td[6]/div/div/div').click()  # 点击人员类别
driver.find_element_by_xpath('//span[text()="合同制员工"]').click()  # 选择人员类别
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div[2]/div[2]/table/tbody/tr/td[7]/div/div/div/div[1]/input').send_keys("1")  # 输入工资数额
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div[2]/div[2]/table/tbody/tr/td[8]/div/div/div').click()  # 点击行业精英
driver.find_element_by_xpath('//span[text()="是"]').click()  # 选择人员类别
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/div/div/div[1]/input').send_keys("1")  # 输入试用期限
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div[2]/div[2]/table/tbody/tr/td[11]/div/div/div/div/input').send_keys("2021-04-01")  # 输入试用开始日期
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div[2]/div[2]/table/tbody/tr/td[13]/div/div/div/div[1]/input').send_keys("1")  # 输入试用工资
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/button[1]').click()  # 点击保存

driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[10]').click()  # 点击人资系统
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="fir_ul"]/li[4]').click()  # 点击人才招聘管理
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="fir_ul"]/li[4]/ul/li[3]/ul/li[1]').click()  # 点击录用申请

#录用申请
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div/div/button[4]/span')))
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div/div/button[4]/span').click()  # 点击提交
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[9]/div/div[3]/button[2]').click()  # 点击确定
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[@role="alert"]/p')))
assert driver.find_element_by_xpath('/html/body/div[@role="alert"]/p').text == "提交成功"

