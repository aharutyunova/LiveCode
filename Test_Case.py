from Page.main_page import Main_Page
from Lib.general_lib import General_Helper
import Lib.driver_lib 
from Page.Registration import Register
import logging
import time


def test():
   driverobj = Lib.driver_lib.Driver_Lib()
   driver = driverobj.get_driver()
   generalLib =  General_Helper(logging)
   mainobj = Main_Page(driver)
   regis = Register(driver)
   mainobj.open_page()
   mainobj.pass_security()
   # regis.generate_registration_data()
   regis.register()
   assert regis.text == regis.successMess
   logging.info("Assertion successful: Text matches the expected value")
   
   

test()

# Anna - don't use upper casers for funciton names. Also if you have several objects create all of objects then go on with steps. 
#  For example regis=Register(driver) object should be created in line 12 
