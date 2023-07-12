from selenium import webdriver

class Driver_Lib:

    def get_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver

    def quit_driver(self):
        self.driver.quit()

    def switch_to_main(self):
        self.driver.switch_to.window(self.driver.window_handles[0])