from Lib.driver_lib import Driver_Lib  
from Page.main_page import Main_Page
from Page.registration import RegistrationPage
from config import config_data
import test_data


    
def new_user_registration():
    print("new_user_registration() started.")

    name, email, username, password, confirm_password = test_data.generate_random_user()

    driver = Driver_Lib().get_driver()
    
    main_page = Main_Page(driver)
    main_page.open_page()
    main_page.pass_security()
        
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

# Anna comments
# There is no need to write function in test_data.py, to return test data.
# You can keep test data in test_data.py file as dictionary
# example - {name: fake.name()}

# You don't neet init method in registration.py file - Changed by Anna

# Also in registration.py file no need to write self next to locators - Changed by Anna

#  You did't pass security pege with your class email and pass, so your screen is stopen on Unauthorized popup - Done