# Go to app , Register user 
# Check that the suer is registered successfully

from Lib.driver_lib import Driver_Lib
from Page.registration import Registration
from Page.main_page import Main_Page
from test_data import test_data
from Page.temp_mail import Temp_Mail
import logging

def test():
    driver_lib=Driver_Lib()
    driver = driver_lib.get_driver()
    main_page = Main_Page(driver)
    registration = Registration(driver)
    temp_mail = Temp_Mail(driver)

    main_page.open_page()
    main_page.pass_security()
    temp_mail.open_page()
    email = temp_mail.get_email()
    print(type(email))
    print(email)
    driver_lib.switch_to_main()
    registration.register(test_data["reg_name"],"tet974@test.ru","tet974@test.ru",test_data["reg_pass"])

    msg2 = f"Your account has been successfully registered.\n×"
    assert registration.find_text(registration.success_alert) == msg2,logging.error("Registration isn't completed.")
    logging.info("The registration is successfully passed.")

if __name__ == "__main__":
    test()