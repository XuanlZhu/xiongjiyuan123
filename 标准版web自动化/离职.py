import time
from selenium.webdriver.common.action_chains import ActionChains

def resign(driver,psn_id):
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