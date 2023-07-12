from Lib.general_lib import General_Helper
from Lib.driver_lib import Driver_Lib
from selenium.webdriver.common.by import By
from test_data import test_data
from config import config_data
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Temp_Mail(General_Helper):

    email=(By.XPATH,"//input[@id='mail']")
    copy_email = (By.XPATH,"//button[@class='btn-rds icon-btn bg-theme click-to-copy copyIconGreenBtn']")
    click_to_refresh = (By.XPATH,"//a[@id='click-to-refresh']")
    
    def open_page(self):
        # action_chains = ActionChains(self.driver)
        # action_chains.key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(config_data["temp_mail_url"])
    
    def get_email(self):
        mail = self.get_element_value(self.email)
        #self.find_and_click(self.copy_email)
        #email = (Keys.CONTROL + 'v') # paste
        return mail
    
    def refresh_email(self):
        self.find_and_click(self.click_to_refresh)

