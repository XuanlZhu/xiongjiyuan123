import csv
from itertools import islice
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from pytest_app.web_ui.common.action import Action
from pytest_app.web_ui.pages.home_page import HomePage

# with open('data.csv') as f:
#     f = list(csv.reader(f))
#     f.pop(0)
#     print(f)

a ="123"

Action().setup("https://www.baidu.com/")