from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from test_data import test_data
from config import config_data
import logging

class User_Action(General_Helper):
      
    acc_balance = (By.XPATH, "//input[@id='acc_balance']")
    added_amount = (By.XPATH, "//input[@id='amount']")
    checkout_btn = (By.XPATH, "//button[@id='Submit']")

    def first_amount(self):
        try:
            val1 = self.get_element_value(self.acc_balance)
            logging.info("Number exists")
            return val1
        except Exception as e:
            logging.error("No number")

    def add_amount(self):
        self.find_and_send_keys(self.added_amount, test_data['amount'])
        self.find_and_click(self.checkout_btn)

    def new_amount(self):
        try:
            new_val=self.get_element_value(self.acc_balance)
            logging.info("Number exists")
            return new_val
        except Exception as e:
             logging.error("No number")

# Anna - You could just have one function get_amount. and call this function before adding amount and after
