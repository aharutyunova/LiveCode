from Lib.driver_lib import Driver_Lib
from Lib.general_lib import General_Helper
from Page.login import Login_Page
from Page.main_page import Main_Page
from Page.user_action import User_Action
from test_data import test_data
import logging

def test():
    driver = Driver_Lib().get_driver()
    main_page = Main_Page(driver)
    login = Login_Page(driver)
    user_action = User_Action(driver)

    main_page.open_page()
    main_page.pass_security()
    login.login()
    user_action.add_amount()

    # assert test_data['error_message'] == result.get_result_text()
    # logging.info("Test case is successfully passed")
    # driver.quit_driver()

if __name__ == "__main__":
    test()