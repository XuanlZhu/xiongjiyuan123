import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def init():
    # 环境设置
    es1 = "http://epm.boxingqiche.com:19061/sso/platform.do"

    driver = webdriver.Chrome()
    driver.implicitly_wait(8)
    driver.get(es1)
    driver.maximize_window()
    time.sleep(0.5)

    # 输入账号密码
    driver.find_element_by_xpath('//*[@id="login_form"]/form/div[2]/label/input').send_keys("ST000000")
    driver.find_element_by_xpath('//*[@id="login_form"]/form/div[3]/label/input').send_keys("Admin")
    driver.find_element_by_xpath('//*[@id="login_form"]/form/div[4]/label/input').send_keys("2019standard!")

    # 生成动作链对象
    actions = ActionChains(driver)
    element_slider = driver.find_element_by_xpath('//*[@id="mpanel1"]/div/div/div')
    actions.drag_and_drop_by_offset(element_slider, 500, 10).perform()  # 拖动滑块
    driver.find_element_by_xpath('//*[@id="button"]').click()  # 登录

    # 进入界面
    driver.find_element_by_xpath('/html/body/div[3]/ul/li[6]/a/img').click()  # 点击EHR
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="details-header-top"]/ul/li[4]/a').click()  # 点击切换店铺
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="select_combbox"]/span/input[1]').clear()  # 清空内容
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="select_combbox"]/span/input[1]').send_keys("ST999991郑州博行测试店铺")  # 输入店铺
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="changeCompany"]').click()  # 点击切换
    time.sleep(0.1)

    return driver