import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def add_field(driver,c,n):
    actions = ActionChains(driver)
    # 如果第3个参数存在就双击增加下拉框，如果报错不存在就双击增加单文本
    #字段类型   1：自定义下拉框  2：自定义接口   3：tab页签   4：附件    5:多行文本
    try:
        c[2]
    except:
        element_001 = driver.find_element_by_xpath('//div[contains(text(),"单行文本")]')  # 双击增加单文本
    else:
        if c[2] in ['1', '2']:
            element_001 = driver.find_element_by_xpath('//div[contains(text(),"下拉框")]')  # 双击增加下拉框
        elif c[2] == "3":
            element_001 = driver.find_element_by_xpath('//div[contains(text(),"tab页签")]')  # 双击增加tab页签
        elif c[2] == "4":
            element_001 = driver.find_element_by_xpath('//div[contains(text(),"附件")]')  # 双击增加附件
        elif c[2] == "5":
            element_001 = driver.find_element_by_xpath('//div[contains(text(),"多行文本")]')     #双击增加多行文本
        else:
            pass
    actions.double_click(element_001).perform()
    time.sleep(0.2)

    e1 = f'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[{n}]'
    WebDriverWait(driver, 10, 0.5).until(expected_conditions.visibility_of_element_located((By.XPATH,e1)))

    time.sleep(0.2)
    driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[1]/div/div/input').send_keys(c[0])  # 输入标题
    driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[2]/div/div/input').send_keys(c[1])  # 输入字段
    time.sleep(0.2)

    # 如果第3个参数存在就进行else操作，报错不存在直接pass
    try:
        c[2]
    except:
        pass
    else:
        if c[2] == '1':  # 自定义==1
            table1 = c[3].split('.')
            for i in range(len(table1)):
                if i > 0:  # 添加选项
                    driver.find_element_by_xpath('//span[contains(text(),"添加")]').click()
                    time.sleep(0.2)
                table2 = table1[i].split(':')
                e1 = f'//label[text()="选项"]/../following-sibling::div[1]/ul/li[{i+1}]/div[1]/div/div/input'
                e2 = f'//label[text()="选项"]/../following-sibling::div[1]/ul/li[{i+1}]/div[2]/div/div/input'
                driver.find_element_by_xpath(e1).send_keys(table2[1])  # 填标签
                time.sleep(0.2)
                driver.find_element_by_xpath(e2).send_keys(table2[0])  # 填选择值
                time.sleep(0.2)
        elif c[2] == '2':  # 接口==2
            table3 = c[3].split('|')
            driver.find_element_by_xpath(
                '//*[@class="el-form custom-attr-form el-form--label-top"]/div[5]/div').click()  # 点击数据源选项框
            time.sleep(0.5)
            driver.find_element_by_xpath('//span[text()="接口"]').click()  # 选择接口
            time.sleep(0.5)
            driver.find_element_by_xpath('//label[contains(text(),"接口api")]/following-sibling::div[1]/div/input').send_keys(table3[0])  # 输入api
            time.sleep(0.2)
            driver.find_element_by_xpath('//label[contains(text(),"标签文本")]/following-sibling::div[1]/div/input').send_keys(table3[1])  # 输入标签文本
            time.sleep(0.2)
            driver.find_element_by_xpath('//label[contains(text(),"绑定值")]/following-sibling::div[1]/div/input').send_keys(table3[2])  # 输入绑定值
            time.sleep(0.2)

            # 输入子选项
            if table3[3] != '':
                driver.find_element_by_xpath('//label[contains(text(),"子选项")]/following-sibling::div[1]/div/input').send_keys(table3[3])  # 输入子选项
                time.sleep(0.2)

            # 输入接口查询参数
            if table3[4] != '':
                table4 = table3[4].split('.')
                for i in range(len(table4)):
                    if i > 0:  # 点击添加接口查询参数
                        driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[10]/button').click()
                        time.sleep(0.2)
                    table5 = table4[i].split(':')
                    e5 = f'//*[@class="el-form custom-attr-form el-form--label-top"]/div[{11 + i}]/div[1]/div/div/input'
                    e6 = f'//*[@class="el-form custom-attr-form el-form--label-top"]/div[{11 + i}]/div[2]/div/div/input'
                    driver.find_element_by_xpath(e5).send_keys(table5[0])  # 填标签
                    time.sleep(0.2)
                    driver.find_element_by_xpath(e6).send_keys(table5[1])  # 填选择值
                    time.sleep(0.2)

            # driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[9]/div/div/input').send_keys("4")    #输入子选项
            # driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[11]/div[1]/div/div/input').send_keys("5")    #输入接口参数key
            # driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[11]/div[2]/div/div/input').send_keys("6")    #输入接口参数值
            # driver.find_element_by_xpath('//*[@class="el-form custom-attr-form el-form--label-top"]/div[10]/button').click()    #点击添加接口查询参数
            # driver.find_element_by_xpath('//*[@class="custom-level"][2]/div/span').click()    #点击是否有默认值滑块
            # driver.find_element_by_xpath('//*[@class="custom-level"][2]/following-sibling::div[1]/div/div/input').send_keys("6")  # 输入默认值


        # 其他选项预留
        else:
            pass

    # 如果第4个参数存在，就点击默认值按钮，输入默认值,不存在就pass
    try:
        c[4]
    except:
        pass
    else:
        driver.find_element_by_xpath('//*[@class="custom-level"][2]/div/span').click()  # 点击是否有默认值滑块
        time.sleep(0.2)
        driver.find_element_by_xpath('//*[@class="custom-level"][2]/following-sibling::div[1]/div/div/input').send_keys(
            c[4])  # 输入默认值
        time.sleep(0.2)