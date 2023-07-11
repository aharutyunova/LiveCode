from Lib.general_lib import General_Helper
import Lib.driver_lib 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import faker
import random
import time
import logging




class Register(General_Helper):
    
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
    
    
    try:  
        for _ in range(count):
            first_name = fake.first_name()
            random_number = str(fake.random_number(digits=3))
            username = first_name.lower() + random_number
            email = fake.email()
            password = fake.password(length=8, digits=True, upper_case=True, lower_case=True)
            confirmPass = password
            
    except Exception as e: 
        General_Helper(logging)
        logging.error("Can't generate a data for registration")

 
    def register(self):
        
        try:
            self.find_and_click(self.registPath)
            self.find_and_send_keys(self.namePath, self.first_name)
            self.find_and_send_keys(self.emailPath, self.email)
            self.find_and_send_keys(self.usernamePath, self.username)
            self.find_and_send_keys(self.passwordPath, self.password)
            self.find_and_send_keys(self.cpasswordPath, self.confirmPass)
            self.find_and_click(self.submitPath)
            registered_message = self.find(self.registerdMess)
            text = registered_message.text
       
        except Exception as e:
            logging.error(f"An exception occurred: {e}")

        try:
         assert text == self.successMess
         logging.info("Assertion successful: Text matches the expected value")
       
        except AssertionError:
         logging.error(f"Assertion failed: Text does not match the expected value {e}")
 
