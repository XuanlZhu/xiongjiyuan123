import time

def add_authority(driver):
    time.sleep(0.5)
    driver.switch_to.parent_frame()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[1]/p').click()  # 点击客户化
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[1]/ul/li[3]/p').click()  # 点击权限管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[1]/ul/li[3]/ul/li[1]/a').click()  # 点击用户权限管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[1]/ul/li[3]/ul/li[1]/a').click()  # 点击用户权限管理
    time.sleep(0.5)

    # 切换frame
    driver.switch_to.frame(driver.find_element_by_name('a12'))
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="username"]').click()  # 点输入用户姓名
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="username"]').send_keys('admin')  # 点输入用户姓名
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="search"]').click()  # 点击查询
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="search"]').click()  # 点击查询
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="_easyui_tree_2"]').click()  # 点击账号
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="assign"]').click()  # 点击委派角色
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="checkAll"]').click()  # 点击全选
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="saveAssign"]').click()  # 点击提交更改
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击确定
    time.sleep(0.1)