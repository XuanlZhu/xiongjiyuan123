import sys
sys.path.append(r'D:\xiong\hello_world')
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pacs_release.SMTP  import smtp

try:
    # 环境设置
    driver=webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get("https://pacss.hxqcgf.com/#/sso/")
    driver.maximize_window()

    #输入账号密码
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/div/div/div[1]/input').send_keys("HX420125")
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[2]/div/div/input').send_keys("GXTR")
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[3]/div/div/input').send_keys("aA250252614!")

    #生成动作链对象
    actions = ActionChains(driver)
    element_slider=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[4]/div/div[3]')
    actions.drag_and_drop_by_offset(element_slider,500,10).perform()   #拖动滑块
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[5]/button').click()  #登录
    print("登录成功")

    #点击部门编制
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[10]').click()  # 点击人资系统
    driver.find_element_by_xpath('//*[@id="fir_ul"]/li[1]/ul/li[1]/ul/li[1]').click()  # 点击部门编制
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[6]')))
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[6]').click()  # 点击网络营销部
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[4]/div[2]/div[2]/table/tbody/tr[2]')))
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/button[1]').click()  # 点击修改
    ActionChains(driver).double_click(driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div[4]/div[2]/div[2]/table/tbody/tr[2]/td[6]')).perform()  # 双击部门岗位
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/button[2]').click()  # 点击保存
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[@role="alert"]/p')))
    assert driver.find_element_by_xpath('/html/body/div[@role="alert"]/p').text == "操作成功"
    print("部门编制成功")

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[10]')))
    #点击人员信息维护
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[10]').click()  #点击人资系统
    driver.find_element_by_xpath('//*[@id="fir_ul"]/li[4]').click()  #点击员工事务管理
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="fir_ul"]/li[4]/ul/li[1]/ul/li[2]')))
    driver.find_element_by_xpath('//*[@id="fir_ul"]/li[4]/ul/li[1]/ul/li[2]').click()  #点击人员信息维护

    #打开人员信息维护详情
    driver.execute_script('window.open("https://pacss.hxqcgf.com/#/ehr/staff/psninfoMaintainDetail?psndocId=107495&psnbasdocId=86265&currentCompanyId=254&mode=edit&breadName=%E4%BA%BA%E5%91%98%E4%BF%A1%E6%81%AF%E7%BB%B4%E6%8A%A4-%E7%BC%96%E8%BE%91")')
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[1]/button[1]')))
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/button[1]').click()  #点击保存
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div[2]/p')))
    assert driver.find_element_by_xpath("/html/body/div[2]/p").text=="操作成功"
    print("人员信息维护成功")
    driver.quit()
except:
    smtp()
    raise
