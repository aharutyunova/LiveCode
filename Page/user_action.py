from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from test_data import test_data
from config import config_data

class User_Action(General_Helper):
    user_act_btn = (By.XPATH, "//a[text()='User_Action']") 
    acc_balance = (By.XPATH, "//input[@id='acc_balance']")
    added_amount = (By.XPATH, "//input[@id='amount']")
    checkout_btn = (By.XPATH, "//button[@id='Submit']")
    
    def open_user_action_page(self):
        self.find_and_click(self.user_act_btn)

    def add_amount(self):
        self.find_and_send_keys(self.added_amount, test_data["amount"])
        self.find_and_click(self.checkout_btn)
       
    def value_of_amount(self):
       return self.get_element_value(self.acc_balance)   