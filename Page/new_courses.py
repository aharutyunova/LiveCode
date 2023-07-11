from Lib.driver_lib import Driver_Lib
from Lib.general_lib import General_Helper
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class New_Courses(General_Helper):
    home_btn = (By.XPATH, "//a[@href='/home']")
    add_course_btn = (By.XPATH, "//a[@href='/add_course']")
    title_field = (By.XPATH, "//input[@id='title']")
    price_field = (By.XPATH, "//input[@id='price']")
    type_dropdown = (By.XPATH, "//select[@id='coursetype']")
    description_field = (By.XPATH, "//textarea[@id='description']")
    submit_btn = (By.XPATH, "//button[@id='Submit']")
    success_msg = (By.XPATH, "//span[@id='successmessage']")

    def add_new_course(self, title, price, type="Advanced", description=""):
        self.find_and_click(self.home_btn)
        self.find_and_click(self.add_course_btn)
        self.find_and_send_keys(self.title_field, title)
        self.find_and_send_keys(self.price_field, price)
        self.find_and_send_keys(self.description_field, description)
        try:
            select = Select(self.find(self.type_dropdown))
            select.select_by_visible_text(type)
            self.find_and_click(self.submit_btn)
            logging.info("The new course is successfully added")
        except Exception as e:
            logging.error(e)
