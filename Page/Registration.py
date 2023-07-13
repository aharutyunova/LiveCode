from Lib.general_lib import General_Helper
import Lib.driver_lib 
import test_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import faker
import random
import time
import logging




class Register(General_Helper):
    
    fakes = test_data.fake_data
    successMess = "Your account has been successfully registered.\n×"
    registPath = (By.XPATH,'//a[@href="/register"]')
    namePath = (By.XPATH,'//input[@id="name"]')
    emailPath = (By.XPATH,'//input[@id="email"]')
    usernamePath = (By.XPATH,'//input[@id="username"]')
    passwordPath = (By.XPATH,'//input[@id="password"]')
    cpasswordPath = (By.XPATH,'//input[@id="confirm"]')
    submitPath = (By.XPATH,'//input[@type="submit"]')
    registerdMess = (By.XPATH,'//div[@role="alert"]')
    fake = faker.Faker()
    count = 10
    
    # Anna - Why you try 10 time input registration data in your page? In page you need have one methid which will fill registration data, 
    # If you need register with different data, you need orginaze it directly in test case
    
 
    def register(self):
        
            self.find_and_click(self.registPath)
            self.find_and_send_keys(self.namePath, self.fakes['name'])
            self.find_and_send_keys(self.emailPath, self.fakes['email'])
            self.find_and_send_keys(self.usernamePath, self.fakes['username'])
            self.find_and_send_keys(self.passwordPath, self.fakes['password'])
            self.find_and_send_keys(self.cpasswordPath, self.fakes['confirmPass'])
            self.find_and_click(self.submitPath)
            registered_message = self.find(self.registerdMess)
            text = registered_message.text
            assert text == self.successMess
            logging.info("Assertion successful: Text matches the expected value")

