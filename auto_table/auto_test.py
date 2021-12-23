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

es_01 = ["https://dms.t.hxqcgf.com/#/sso/","HD340400","A04L","aA3251002!"]   #测试线
es_02 = ["https://dms.hxqcgf.com/#/sso/",'HD420610','A0KJ','aA250252614!']     #预上线
es_03 = ["https://pacss.hxqcgf.com/",'HX420125',"GXTR",'aA250252614!']    #正式线
es = es_03  #环境配置

#初始化
table_001=table_para.考勤修改申请     #配置表单
f=csv.reader(open(table_001[2],encoding='utf-8'))

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

#进入界面
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[2]').click()  #点击平台管理
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="fir_ul"]/li[3]/p').click()   #点击人资行政管理
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="fir_ul"]/li[3]/ul/li[2]/ul/li[3]/p').click()  #点击表单管理
WebDriverWait(driver,8,0.2).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div/div[1]/div[1]/p')))
driver.find_element_by_xpath('//input[@placeholder="搜索关键字"]').send_keys(table_001[0])  #输入查询条件
time.sleep(0.1)
driver.find_element_by_xpath('//input[@placeholder="搜索关键字"]/following-sibling::div[1]/button').click()   #点击查询
time.sleep(0.1)
driver.find_element_by_xpath(table_001[1]).click()   #点击表单
time.sleep(0.2)

driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]').click()  #选中字段
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div[3]/button[2]').click()   #删字段
time.sleep(0.1)

n=0  #计数器

for i in f:
    n+=1
    c=i[0].split('\t')
    if not i[1]:   #如果第二个字段不存在，就不是子表单
        #根据列表c添加字段并填写内容
        add_field(driver,c,n)

    else:   #如果第二个字段存在，就创建子表单
        actions = ActionChains(driver)
        element_001 = driver.find_element_by_xpath('//div[contains(text(),"表格")]')
        actions.double_click(element_001).perform()  # 双击增加子表
        time.sleep(0.2)
        driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[1]/div/div/input').clear()
        driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[1]/div/div/input').send_keys(c[0])   #输入标题
        driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[3]/div/div/input').clear()
        driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[3]/div/div/input').send_keys(c[1])   #输入字段
        time.sleep(0.2)

        js = 'document.getElementsByClassName("form-layout-view custom-scrollbar")[0].scrollTop=10000'  # 滑动到底
        driver.execute_script(js)
        time.sleep(0.2)

        locator_001=f'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[{n}]'  #初始化子表定位器
        a=i[1].split('\n')   #拆解字符串a = [‘并发，jkf’,'空，sdlk']

        for j in a:
            b=j.split('\t')

            actions = ActionChains(driver)
            element_002 = driver.find_element_by_xpath(locator_001)
            actions.move_to_element_with_offset(element_002, 20, 20).click().perform()   #点击字表
            time.sleep(0.2)

            # 根据列表c添加字段并填写内容
            add_field(driver,b,n)




def add_deploy():
    f = csv.reader(open(r"D:\xiong\hello_world\auto_table\table_data\离职交接弹出框", encoding='utf-8'))
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