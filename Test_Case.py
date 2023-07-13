from Page.main_page import Main_Page
from Lib.general_lib import General_Helper
import Lib.driver_lib 
from Page.Registration import Register
import logging
import time


def test_registration():
   driverobj = Lib.driver_lib.Driver_Lib()
   driver = driverobj.get_driver()
   generalLib = General_Helper(driver)
   mainobj = Main_Page(driver)
   regis = Register(driver)
   mainobj.open_page()
   mainobj.pass_security()
   regis.register()
   
   

test_registration()
