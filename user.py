from database import Connection
import csv
import os



class User:

    def sign_in(self, email, password):
        with open('users.csv', 'r') as file:
            checker = csv.DictReader(file)
            for a_user in checker:
                if a_user['Email'] == email and a_user['Password']==password:
                    print("Welcome {}".format(a_user['First Name']))
                    return True
                else:
                    print( "Invalid email or password")
                    return False


    def sign_up(self, first_name, last_name, email, phone_number, password, date_of_birth, gender):
        file_exist = os.path.isfile('users.csv')
        with open('users.csv', 'a') as file:
            fieldname = ['First Name', 'Last Name', 'Email', 'Phone Number', 'Password', 'Gender', 'Date of Birth']
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
