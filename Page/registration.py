from faker import Faker
from selenium.webdriver.common.by import By
from config import config_data
from Lib.general_lib import General_Helper


class RegistrationPage(General_Helper):

    name_input = (By.XPATH, '//input[@id="name"]')
    email_input = (By.XPATH, '//input[@id="email"]')
    username_input = (By.XPATH, '//input[@id="username"]')
    password_input = (By.XPATH, '//input[@id="password"]')
    confirm_password_input = (By.XPATH, '//input[@id="confirm"]')
    submit_button = (By.XPATH, '//input[@type="submit"]')
    success_message = (By.XPATH, '//div[@id="flashwrapper"]')

    def open_page(self):
        self.driver.get(config_data["url"] + "/register")

    def enter_name(self, name):
        self.find_and_send_keys(self.name_input, name)      

    def enter_email(self, email):
        self.find_and_send_keys(self.email_input, email)

    def enter_username(self, username):
        self.find_and_send_keys(self.username_input, username)

    def enter_password(self, password):
        self.find_and_send_keys(self.password_input, password)

    def enter_confirm_password(self, confirm_password):
        self.find_and_send_keys(self.confirm_password_input, confirm_password)

    def click_submit(self):
        self.find_and_click(self.submit_button)

    def get_success_message(self):
        sucess_message = self.find_text(self.success_message)
        return sucess_message


    
