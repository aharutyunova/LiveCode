from Lib.driver_lib import Driver_Lib   
from Page.registration import RegistrationPage
from config import config_data
import test_data


    
def new_user_registration():
    print("new_user_registration() started.")

    name, email, username, password, confirm_password = test_data.generate_random_user()
    
    driver = Driver_Lib().get_driver()
    registration_page = RegistrationPage(driver)
    
    registration_page.open_page()
       
    
    registration_page.enter_name(name)
    registration_page.enter_email(email)
    registration_page.enter_username(username)
    registration_page.enter_password(password)
    registration_page.enter_confirm_password(confirm_password)
    registration_page.click_submit()

    success_message = registration_page.get_success_message()

    assert "Your account has been successfully registered." in success_message

    driver.quit()


if __name__ == '__main__':
    new_user_registration()