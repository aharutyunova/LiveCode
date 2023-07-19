from faker import Faker

test_data = {
    "username": "projectuser",
    "password": "11111111"
    }

def generate_random_user():
         fake = Faker()
         name = fake.name()
         email = fake.email()
         username = fake.user_name()
         password = generate_random_password(fake, 8)
         confirm_password = password

         return name, email, username, password, confirm_password

def generate_random_password(fake, min_length=8):
    
    while True:
        password = fake.password()
        if len(password) >= min_length:
            return password