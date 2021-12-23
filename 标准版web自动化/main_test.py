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
from 标准版web自动化.id_code import create_id_code
import win32gui,win32con,win32api
from 标准版web自动化.应聘登记 import *
from 标准版web自动化.init import init
from 标准版web自动化.增加权限 import add_authority
from 标准版web自动化.check import *
from 标准版web自动化.转正 import *
from 标准版web自动化.调配 import *
from 标准版web自动化.离职 import *

#初始化
driver = init()

# 应聘登记:步骤1  进入应聘登记界面，点新增输入数据，点击保存，进入h5界面，登陆退出
register1(driver)

#应聘登记：步骤2  进入界面，点击打印，点击录用申请
register2(driver)

#增加权限
add_authority(driver)

#录用审批
approve_employ(driver)

#入职确认
psn_id = induction(driver)

#校验应聘
check_register(driver,psn_id)

#转正
regular(driver,psn_id)

#校验转正
check_regular(driver,psn_id)

#调配
deploy(driver,psn_id)

#离职
resign(driver,psn_id)