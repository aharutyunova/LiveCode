from Lib.driver_lib import Driver_Lib
from Lib.general_lib import General_Helper
from Page.login import Login_Page
from Page.main_page import Main_Page
from Page.user_action import User_Action
from test_data import test_data
import logging
import pytest

def test_f():
    driver = Driver_Lib().get_driver()
    main_page = Main_Page(driver)
    login = Login_Page(driver)
    user_action = User_Action(driver)

    main_page.open_page()
    main_page.pass_security()
    login.login()
    user_action.open_user_action_page()
    old_balance = user_action.value_of_amount()
    user_action.add_amount()
    new_balance = user_action.value_of_amount()
    #calculate the old and after adding amount balance difference
    difference_after_addamount = float(new_balance) - float(old_balance)
    #check if added amount succesfully is added on balance or not

    assert float(test_data['amount']) == difference_after_addamount
    logging.info("Test case is successfully passed")
    Driver_Lib().quit_driver(driver)

# if __name__ == "__main__":
    # test()py