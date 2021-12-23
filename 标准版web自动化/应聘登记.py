import time
from 标准版web自动化.id_code import create_id_code
import win32gui,win32api,win32con
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

# 应聘登记:步骤1  进入应聘登记界面，点新增输入数据，点击保存，进入h5界面，登陆退出
def register1(driver):
    # 应聘登记
    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[2]/p').click()  # 点击招聘管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[2]/ul/li[1]/a').click()  # 点击招聘人员管理
    time.sleep(0.1)

    # 切换frame
    driver.switch_to.frame(driver.find_element_by_name("a64"))
    driver.find_element_by_xpath('//*[@id="create"]').click()  # 点击增加按钮
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="update"]').click()  # 点击手工修改
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="psnname"]').send_keys('测试1')  # 输入姓名
    time.sleep(0.1)

    driver.find_element_by_id('REG_DATE').send_keys('2021-03-01')  # 点击面试日期
    time.sleep(0.1)

    driver.find_element_by_id('reg_time').send_keys('15:41:00')  # 输入面试时间
    time.sleep(0.1)

    driver.find_element_by_id('positionname').send_keys("会计")  # 输入应聘岗位
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="h1"]/div[2]/div[2]/div/div[1]/span/input[1]').send_keys('男')  # 点击性别
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="h1"]/div[2]/div[2]/div/div[2]/span/span/a').click()  # 点击名族
    time.sleep(0.1)
    driver.find_element_by_id('_easyui_comboboxE_i2_0').click()  # 选择名族
    time.sleep(0.1)

    id_code = create_id_code()
    driver.find_element_by_id('ID').send_keys(id_code)  # 输入身份证号
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="h1"]/div[2]/div[4]/span/span/a').click()  # 点击渠道
    time.sleep(0.1)
    driver.find_element_by_id('_easyui_comboboxE_i6_4').click()  # 选择渠道
    time.sleep(0.1)

    driver.find_element_by_id('MOBILE').send_keys('17762538936')  # 输入手机
    time.sleep(0.1)

    driver.find_element_by_id('save').click()  # 点击保存
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击确定
    time.sleep(0.1)

    driver.find_element_by_id('getQRCode').click()  # 点击生成二维码
    time.sleep(0.1)

    url = driver.find_element_by_xpath('//*[@id="QRurl"]').get_attribute('value')  # 获取手机登录url
    time.sleep(0.1)

    driver.get(url)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="vm-login"]/a[1]/div[2]/div[2]/input').send_keys(id_code)  # 输入身份证号
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="vm-login"]/a[2]/div[2]/div[2]/input').send_keys('17762538936')  # 输入手机号
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="vm-login"]/div/button').click()  # 点击确定登陆
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="vm"]/div[1]/button[2]').click()  # 点击确定提交
    time.sleep(0.1)

    driver.back()  # 后退
    driver.back()  # 后退
    time.sleep(0.1)


#应聘登记：步骤2  进入界面，点击打印，点击录用申请
def register2(driver):
    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[2]/p').click()  # 点击招聘管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[2]/ul/li[1]/a').click()  # 点击招聘人员管理
    time.sleep(0.1)

    # 切换frame
    driver.switch_to.frame(driver.find_element_by_name("a64"))
    time.sleep(0.2)

    ActionChains(driver).double_click(driver.find_element_by_id('datagrid-row-r1-2-0')).perform()  # 双击打卡记录
    time.sleep(0.1)

    driver.find_element_by_xpath('/html/body/div[1]/ul/li[4]/button').click()  # 点击打印
    time.sleep(0.1)

    driver.switch_to.alert.accept()  # 点击确定
    time.sleep(1)

    # 点击取消打印
    handle_chrome = win32gui.FindWindow("Chrome_WidgetWin_1", "EHR人事管理系统 - Google Chrome")
    handle = win32gui.FindWindowEx(handle_chrome, None, "Chrome_RenderWidgetHostHWND", "Chrome Legacy Window")
    position = win32api.MAKELONG(1260, 828)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, position)
    win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, position)

    time.sleep(0.3)
    driver.find_element_by_xpath('//*[@id="viewback"]').click()  # 点击返回
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input').click()  # 勾选第一个数据
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="business"]').click()  # 点击业务操作
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="addEmploy"]').click()  # 点击申请录用
    time.sleep(0.1)


    #填写录用申请单据
    # 切换frame
    driver.switch_to.parent_frame()
    driver.switch_to.frame(driver.find_element_by_name("a65"))
    time.sleep(0.2)

    driver.find_element_by_xpath('//*[@id="employApply"]/div[1]/div[2]/input').send_keys('asd1234')  # 输入单据名称
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]').click()  # 编辑行
    time.sleep(0.3)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div/table/tbody/tr/td/span/input[1]').click()  # 点击计划报到日期
    time.sleep(0.1)

    driver.find_element_by_xpath('/html/body/div[6]').click()  # 选择计划报到日期
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[2]/div/table/tbody/tr/td/input').send_keys('2021-03-11')  # 输入录用日期
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[3]/div/table/tbody/tr/td/span/input[1]').click()  # 点击录用部门
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="_easyui_tree_7"]/span[4]').click()  # 选择录用部门
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[4]/div/table/tbody/tr/td/span/input[1]').click()  # 点击录用岗位
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="_easyui_comboboxE_i3_4"]').click()  # 选择录用岗位
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[8]/div/table/tbody/tr/td/span/input[1]').click()  # 点击人员类型
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="_easyui_comboboxE_i2_0"]').click()  # 选择人员类型
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[9]/div/table/tbody/tr/td/span/input[1]').send_keys('1')  # 输入工作数额
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[11]/div/table/tbody/tr/td/input').send_keys('1')  # 输入试用月数
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[12]/div/table/tbody/tr/td/input').send_keys('2021-03-11')  # 输入试用开始日期
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[13]/div/table/tbody/tr/td/input').send_keys('2021-03-11')  # 输入试用结束日期
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[14]/div/table/tbody/tr/td/span/input[1]').send_keys('2021-03-11')  # 输入试用期工资
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="save"]').click()  # 点击保存
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="continue"]').click()  # 点击继续
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击保存成功
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div').click()  # 选中单据
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="submitCheck"]').click()  # 点击提交
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()  # 点击确定
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()  # 点击操作成功
    time.sleep(0.1)


#录用审批
def approve_employ(driver):
    # 切换到父frame
    time.sleep(0.5)
    driver.switch_to.parent_frame()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[2]/p').click()  # 点击招聘管理
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[2]/ul/li[3]/a').click()  # 点击录用审批
    time.sleep(0.1)

    time.sleep(0.5)
    driver.switch_to.frame(driver.find_element_by_name('a66'))  # 切换到子frame
    time.sleep(0.5)

    ActionChains(driver).double_click(driver.find_element_by_id('datagrid-row-r1-2-0')).perform()  # 双击单据
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="audit"]').click()  # 点击审批操作
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="approveCheck"]').click()  # 点击批准
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="audit_submit"]').click()  # 点击确定
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击操作成功
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="audit"]').click()  # 点击审批操作
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="approveCheck"]').click()  # 点击批准
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="audit_submit"]').click()  # 点击确定
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击操作成功

#入职确认
def induction(driver):
    # 切换到父frame
    time.sleep(0.5)
    driver.switch_to.parent_frame()
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="sidebar-list"]/li[2]/ul/li[5]/a').click()  # 点击报到管理
    time.sleep(0.1)

    # 切换到子frame
    time.sleep(0.5)
    driver.switch_to.frame(driver.find_element_by_name('a67'))
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input').click()  # 勾选人员
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="create"]').click()  # 点击报到
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()  # 点击确定
    time.sleep(0.5)

    Select(driver.find_element_by_xpath('//*[@id="job_type_id"]')).select_by_index(1)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="save"]').click()  # 点击保存
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()  # 点击确定
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input').click()  # 勾选人员
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="entry"]').click()  # 点击入职确认
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()  # 点击确认
    time.sleep(0.5)

    driver.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()  # 点击确认
    time.sleep(0.1)

    psn_id = driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[9]/div').text

    return psn_id