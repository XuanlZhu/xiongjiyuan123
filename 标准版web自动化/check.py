import time
from selenium.webdriver.common.action_chains import ActionChains


def check_register(driver,psn_id):
    # 切换到父frame
    time.sleep(0.5)
    driver.switch_to.parent_frame()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[3]/p').click()  # 点击人员信息管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[3]/ul/li[2]/a').click()  # 点击人员信息维护
    time.sleep(0.5)

    # 切换到子frame
    time.sleep(0.5)
    driver.switch_to.frame(driver.find_element_by_name('a98'))
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="theForm"]/div[1]/div[1]/input').send_keys(psn_id)  # 输入人员编码
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="theForm"]/div[2]/div[4]/button').click()  # 点击查询
    time.sleep(1)

    print(driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[3]/div').text)
    assert psn_id == driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[3]/div').text

def check_regular(driver,psn_id):
    # 切换到父frame
    time.sleep(0.5)
    driver.switch_to.parent_frame()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[3]/p').click()  # 点击人员信息管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[3]/ul/li[2]/a').click()  # 点击人员信息维护
    time.sleep(0.5)

    # 切换到子frame
    time.sleep(0.5)
    driver.switch_to.frame(driver.find_element_by_name('a98'))
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="theForm"]/div[1]/div[1]/input').clear()  # 清除人员编码
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="theForm"]/div[1]/div[1]/input').send_keys(psn_id)  # 输入人员编码
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="theForm"]/div[2]/div[4]/button').click()  # 点击查询
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[36]/div/input[@checked]')  # 获取转正属性
    time.sleep(0.5)


#检测调配成功
def check_deploy(driver,psn_id):
    # 切换到父frame
    time.sleep(0.5)
    driver.switch_to.parent_frame()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[3]/p').click()  # 点击人员信息管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[3]/ul/li[2]/a').click()  # 点击人员信息维护
    time.sleep(0.5)

    # 切换到子frame
    time.sleep(0.5)
    driver.switch_to.frame(driver.find_element_by_name('a98'))
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="theForm"]/div[1]/div[1]/input').clear()  # 清除人员编码
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="theForm"]/div[1]/div[1]/input').send_keys(psn_id)  # 输入人员编码
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="theForm"]/div[2]/div[4]/button').click()  # 点击查询
    time.sleep(1)

    print(driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[8]/div').text)

    assert driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[8]/div').text =="出纳"