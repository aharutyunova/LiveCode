from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from test_data import test_data
from config import config_data

class Registration(General_Helper):
    reg_btn = (By.XPATH,"//a[@href='/register']")
    name_field = (By.XPATH,"//input[@id='name']")
    email_field = (By.XPATH,"//input[@id='email']")
    username_field = (By.XPATH,"//input[@id='username']")
    password_field = (By.XPATH, "//input[@id='password']")
    confirm_pass_field = (By.XPATH,"//input[@id='confirm']")
    submit_btn = (By.XPATH,"//input[@value='Submit']")
    success_alert = (By.XPATH,"//div[@id='flashwrapper']")

    def register(self,name,email,username,password):
        self.find_and_click(self.reg_btn)
        self.find_and_send_keys(self.name_field,name)
        self.find_and_send_keys(self.email_field,email)
        self.find_and_send_keys(self.username_field,username)
        self.find_and_send_keys(self.password_field,password)
        self.find_and_send_keys(self.confirm_pass_field,password)
        self.find_and_click(self.submit_btn)