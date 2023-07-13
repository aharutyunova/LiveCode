from faker import Faker
import random
import logging
from Lib.general_lib import General_Helper

test_data = {
    "username": "projectuser",
    "password": "11111111"
    }

try: 
    fake = Faker()
    name = fake.first_name()
    random_number = str(fake.random_number(digits=3))
    username = name.lower() + random_number
    email = fake.email()
    password = fake.password(length=8, digits=True, upper_case=True, lower_case=True)
    confirmPass = password
except Exception as e:
    logging.error(f"Can't generate a fake Data {e}")
    
fake_data = {
        'name' : name,
        'username': username,
        'email': email,
        'password':password,
        'confirmPass': confirmPass
    }     
        
#  try:  
#         for _ in range(count):
#             first_name = fake.first_name()
#             random_number = str(fake.random_number(digits=3))
#             username = first_name.lower() + random_number
#             email = fake.email()
#             password = fake.password(length=8, digits=True, upper_case=True, lower_case=True)
#             confirmPass = password
            
#     except Exception as e: 
#         General_Helper(logging)
#         logging.error("Can't generate a data for registration")

