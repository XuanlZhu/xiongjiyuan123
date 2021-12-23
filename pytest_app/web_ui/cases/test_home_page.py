# _*_ coding: UTF-8 _*_
# # @Time :2020/1/6 4:48
# # @Author : Xuanl Zhu
# # @Site : 
# # @File :test_home_page.py
# # @Software : PyCharm

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pytest_app.web_ui.common.action import Action
from pytest_app.web_ui.pages.home_page import HomePage
import pytest
from pytest_app.web_ui.cases.csv_tuil import CsvUtil
from pytest_app.web_ui.cases.ui import Ui

class TestHomePage():
    def setup_class(self):
        self.driver = Action()


    @pytest.mark.parametrize("args", CsvUtil("data.csv").read_csv())
    def test_001(self,args):
        # self.driver.sendkeys(HomePage.element_search,'ni ma si le').click(HomePage.element_search_submit)
        print(args)
        Ui(self.driver,args).action()

    def teardown_class(self):
        pass


if __name__ == '__main__':
    pytest.main()
