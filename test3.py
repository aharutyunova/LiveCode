from Lib.driver_lib import Driver_Lib
from Page.new_courses import New_Courses
from Page.login import Login_Page
from Page.main_page import Main_Page
from test_data import test_data
import logging


def test():
    driver_lib = Driver_Lib()
    driver = driver_lib.get_driver()
    main_page = Main_Page(driver)
    login_Page = Login_Page(driver)
    new_courses = New_Courses(driver)

    main_page.open_page()
    main_page.pass_security()
    login_Page.login(test_data["admin_username"], test_data["password"])
    new_courses.add_new_course(test_data["title"], test_data["price"])
    try:
        assert new_courses.find_text(
            new_courses.success_msg) == "Course is added", logging.error("The course isn't added")
        logging.info("The test3 is successfully passed.")
    finally:
        driver_lib.quit_driver()


if __name__ == "__main__":
    test()
