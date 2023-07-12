from POM_Code.Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from POM_Code.test_data import test_data
from POM_Code.config import config_data


class Login_Page(General_Helper):

    login_btn = (By.XPATH, "//a[text()='Login']")
    username_field = (By.XPATH, "//input[@name='username']")
    password_field = (By.XPATH, "//input[@name='password']")
    btn_signin = (By.XPATH, "//button[text()='Log in']")

    def login(self):
        self.find_and_click(self.login_btn)
        self.find_and_send_keys(self.username_field, test_data['username'])
        self.find_and_send_keys(self.password_field, test_data['password'])
        self.find_and_click(self.btn_signin)