from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# self.driver = webdriver.Chrome()
# self.driver.maximize_window()
# self.driver.get('https://www.baidu.com/')


class Action:
    def __init__(self):
        pass

    def setup(self,url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        return self

    def find_element(self,element):
        self.driver.find_element(*element)
        return self

    def find_elements(self,elements):
        self.driver.find_element(*elements)
        return self

    def click(self,element):
        self.driver.find_element(*element).click()
        return self

    def sendkeys(self,element,value):
        self.driver.find_element(*element).send_keys(value)
        return self