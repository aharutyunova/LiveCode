from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from test_data import test_data
from config import config_data

class User_Action(General_Helper):
      
    acc_balance = (By.XPATH, "//input[@id='acc_balance']")
    added_amount = (By.XPATH, "//input[@id='amount']")
    checkout_btn = (By.XPATH, "//button[@id='Submit']")

    def add_return_amount(self, amount):
        self.find_and_send_keys(self.added_amount, amount)
        self.find_and_click(self.checkout_btn)
        newval=self.get_element_value(self.acc_balance)
        return newval