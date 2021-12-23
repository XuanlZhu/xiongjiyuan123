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

# driver=webdriver.Chrome()
# driver.implicitly_wait(8)
# driver.get("https://www.baidu.com/")
# driver.maximize_window()
#
# driver.find_element(By.ID,"kw").send_keys("123")
# driver.find_element(By.ID,"su").click()

from pytest_app.web_ui.common.action import Action
from pytest_app.web_ui.pages.home_page import HomePage

driver = Action()
driver.setup(HomePage.url).sendkeys(HomePage.element_search,'ni ma si le').click(HomePage.element_search_submit)
