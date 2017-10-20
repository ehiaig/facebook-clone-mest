from user import User
from profile import display_posts, create_post
import os
import csv

class Index:
    def __init__(self):
        self.logged_in = None

    def sign_up(self, first_name, last_name, email, phone_number, password, date_of_birth, gender):
        file_exist = os.path.isfile('users.csv')
        with open('users.csv', 'a') as file:
            fieldname = ['First Name',
                         'Last Name',
                         'Email',
                         'Phone Number',
                         'Password',
                         'Gender',
                         'Date of Birth']
            writer = csv.DictWriter(file, fieldnames=fieldname)

            if not file_exist:
                writer.writeheader()
            writer.writerow({'First Name':first_name,
                             'Last Name':last_name,
                             'Email':email,
                             'Phone Number':phone_number,
                             'Password':password,
                             'Gender':gender,
                             'Date of Birth':date_of_birth })

            print('You have now joined Facebook')

    def sign_in(self, email):
        self.logged_in = email

    def sign_out(self):
        pass

indx = Index()

# class Home:
#     def login(self):
#         email = input("Enter your email: ")
#         password = input("Enter your password: ")
#
#         u = User()
#         is_logged_in = u.sign_in(email, password)
#         if is_logged_in:
#             display_posts(email)
#         else:
#             print("Doesnt")
#
#     def register(self):
#         first_name = input("Enter your firstname: ")
#         last_name = input("Enter your lastname: ")
#         email = input("Enter your email: ")
#         phone_number = input('Supply Phone Number:')
#         password = input("Enter your password: ")
#         date_of_birth = input("Enter your birthday: ")
#         gender = input("Enter your gender: ")
#
#         new_user = User()
#         new_user.sign_up(first_name, last_name, email, phone_number, password, date_of_birth, gender)

def main():
    start = True
    while start:

        choice = input(' 1. to Sign In\n 2. to Sign Up \n 3. to exit Facebook: ')

        if choice == '1':
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            with open('users.csv', 'r') as file:
                checker = csv.DictReader(file)
                for a_user in checker:
                    if a_user['Email'] == email and a_user['Password'] == password:
                        print("Welcome {}".format(a_user['First Name']))
                        fb_logic()
                    else:
                        print("Invalid email or password")
                        return False


        elif choice == '2':
            first_name = input("Enter your firstname: ")
            last_name = input("Enter your lastname: ")
            email = input("Enter your email: ")
            phone_number = input('Supply Phone Number:')
            password = input("Enter your password: ")
            date_of_birth = input("Enter your birthday: ")
            gender = input("Enter your gender: ")

            indx.sign_up(first_name, last_name, email, phone_number, password, date_of_birth, gender)

        elif choice == '3':
            start = False

        else:
            print('Invalid entry')

def fb_logic():
    begin = True
    while begin:
        option = input(' 1. to Create Post\n 2. to Update Profile \n 3. to exit Facebook: ')
        indx.logged_in.display_posts()

        if option == '1':
            indx.logged_in.create_post()
            pass
        elif option=='2':
            pass
        elif option == '3':
            pass

if __name__ == '__main__':
    main()






