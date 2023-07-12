from Lib.driver_lib import Driver_Lib
from Page.user_action import User_action
from Page.login import Login_Page
from Page.main_page import Main_Page
from test_data import test_data
import logging


def test():
    driver_lib = Driver_Lib()
    driver = driver_lib.get_driver()
    main_page = Main_Page(driver)
    login_page = Login_Page(driver)
    user_action = User_action(driver)

    main_page.open_page()
    main_page.pass_security()
    login_page.login(test_data["username"], test_data["password"])
    try:
        res_list = user_action.add_amount(test_data["price"])
        assert res_list[1] == res_list[0]+test_data["price"],logging.error("An amount isn't added.")
        logging.info("The test2 is successfully passed.")
    finally:
        driver_lib.quit_driver()


if __name__ == "__main__":
    test()