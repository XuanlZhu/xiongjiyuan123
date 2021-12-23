from pytest_app.web_ui.common.action import Action
from pytest_app.web_ui.pages.home_page import HomePage

class Ui:
    def __init__(self,driver,args):
        self.args = args
        self.driver = driver


    def action(self):
        if self.args[0] == 'setup':
            self.driver.setup(eval(self.args[1]))

        elif self.args[0] == 'sendkeys':
            self.driver.sendkeys(eval(self.args[3]),self.args[1])

        elif self.args[0] == 'click':
            self.driver.click(eval(self.args[3]))

        else:
            pass


