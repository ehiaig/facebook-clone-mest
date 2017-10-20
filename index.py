from user import User
from profile import display_posts, create_post, update_bio, create_pg

print('Welcome to Facebook Clone')
# is_logged_in = False

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    u = User()
    is_logged_in = u.sign_in(email, password)
    if is_logged_in:
        display_posts(email)

        while True:
            opt = input(' 1. to Create Post\n 2. to Update Bio \n 3 Create Page \n 4 to Logout ')
            if opt == '1':
                create_post(email)
            elif opt == '2':
                update_bio(email)
            elif opt == '3':
                create_pg()
            elif opt == '4':
                return 'False'

    else:
        print("Doesnt")

def register():
    first_name = input("Enter your firstname: ")
    last_name = input("Enter your lastname: ")
    email = input("Enter your email: ")
    phone_number = input('Supply Phone Number:')
    password = input("Enter your password: ")
    date_of_birth = input("Enter your birthday: ")
    gender = input("Enter your gender: ")

    new_user = User()
    new_user.sign_up(first_name, last_name, email, phone_number, password, date_of_birth, gender)

# def profile_logic():
#     while True:
#         opt = input(' 1. to Create Post\n 2. to Update Bio \n 3 Create Page \n 4 to Logout ')
#         if opt == '1':
#             pass
#         elif opt == '2':
#             pass
#         elif opt == '3':
#             pass
#         elif opt == '4':
#             pass
#     pass

start = True
while start:

    choice = input(' 1. to Sign In\n 2. to Sign Up \n 3. to exit Facebook: ')

    if choice == '1':
        login()

    elif choice == '2':
        register()

    elif choice == '3':
        start = False

    else:
        print('Invalid entry')