from Lib.driver_lib import Driver_Lib
from Lib.general_lib import General_Helper
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class User_action(General_Helper):
    user_action_btn = (By.XPATH, "//a[@href='/user_action']")
    amount_field = (By.XPATH, "//input[@id='amount']")
    submit_btn = (By.XPATH, "//button[@id='Submit']")
    balance_field = (By.XPATH, "//input[@id='acc_balance']")

    def add_amount(self, amount):
        self.find_and_click(self.user_action_btn)
        value1 = self.get_element_value(self.balance_field)
        self.find_and_send_keys(self.amount_field, amount)
        self.find_and_click(self.submit_btn)
        value2 = self.get_element_value(self.balance_field)
        res = int(value1)+int(amount)

        if int(value2) == int(res):
            logging.info("Amount is added.")
        else:
            logging.error("Something went wrong!!!")

# Anna - checking of amount value will be better to do in test case
# Here would be better if add_amount method return res and in test case you will assert res with expected value

# Other parts good enough, driver_lib part also changed correctly