from Page.main_page import Main_Page
from Lib.general_lib import General_Helper
import Lib.driver_lib 
from Page.Registration import Register
import time


def Test():
   driverobj = Lib.driver_lib.Driver_Lib()
   driver = driverobj.get_driver()
   mainobj = Main_Page(driver)
   mainobj.open_page()
   mainobj.pass_security()
   regis = Register(driver)
   regis.register()
   
   
   

Test()

# Anna - don't use upper casers for funciton names. Also if you have several objects create all of objects then go on with steps. 
#  For example regis=Register(driver) object should be created in line 12 
