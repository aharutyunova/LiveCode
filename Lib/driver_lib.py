from selenium import webdriver

class Driver_Lib:

    def get_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
    
    def quit_driver(self):
        self.get_driver().quit()