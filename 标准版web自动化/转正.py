import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

def regular(driver,psn_id):
    # 切换到父frame
    time.sleep(0.5)
    driver.switch_to.parent_frame()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[4]/p').click()  # 点击人员变动管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[4]/ul/li[1]/p').click()  # 点击转正管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[4]/ul/li[1]/ul/li[1]/a').click()  # 点击转正申请
    time.sleep(0.5)

    # 切换到子frame
    driver.switch_to.frame(driver.find_element_by_name('a34'))
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="add"]').click()  # 点击增加
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="html_1"]/div[1]/ul/li[3]/button').click()  # 点击编辑人员
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="selectPeople"]/button').click()  # 点击增加人员
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="company_dep_tree"]').click()  # 点击店铺
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="aaa"]').send_keys(psn_id)  # 输入人员编码
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="tb"]/a').click()  # 点击搜索
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r2-2-0"]').click()  # 勾选人员
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div[3]/button').click()  # 点击确定
    time.sleep(0.5)

    Select(driver.find_element_by_xpath('//*[@id="html_2"]/div[2]/div/div[2]/div/div[9]/div[2]/select')).select_by_index(0)  # 选择转正后社保
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="html_2"]/div[2]/div/div[2]/div/div[15]/div[2]/input').send_keys('0')  # 输入基数
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="html_2"]/div[2]/div/div[2]/div/div[16]/div[2]/input').send_keys('0')  # 输入基数
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="html_2"]/div[2]/div/div[2]/div/div[17]/div[2]/input').send_keys('0')  # 输入基数
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="html_2"]/div[2]/div/div[2]/div/div[18]/div[2]/input').send_keys('0')  # 输入基数
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="html_2"]/div[2]/div/div[2]/div/div[19]/div[2]/input').send_keys('0')  # 输入基数
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="html_2"]/div[1]/ul/li[3]/button').click()  # 点击保存人员
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="save"]').click()  # 点击保存
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击确定
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]').click()  # 选中单据
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="submitCheck"]').click()  # 点击提交
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()  # 点击确定
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()  # 点击确定
    time.sleep(0.5)

    # 切换到父frame
    time.sleep(0.5)
    driver.switch_to.parent_frame()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[4]/ul/li[1]/ul/li[2]/a').click()  # 点击转正审批
    time.sleep(0.5)

    # 切换到子frame
    driver.switch_to.frame(driver.find_element_by_name('a35'))
    time.sleep(0.5)

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