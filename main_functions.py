from User import User
from datetime import date
import sys


def add_new_user(users):
    #argument inout
    name = input("Enter user name: ")
    phone_number = input("Enter user phone number: ")
    creation_date = date.today()
    new_user = User(name, phone_number, creation_date)
    print(new_user.to_string())
    users.append(new_user)

def show_all_users(users):
    for user in users:
        print(user.to_string())


def show_user():
    return


#def add_user_group():
#    return


def show_menu():
    print("----------------------MENU-----------------------------")
    print("""Choose what you'd like to do :
                        1. Add new user.
                        2. Display all users.
                        3. Display one user.
                        4. Close program. \n""")



def main_program_loop():
    users = []
    while True:
        show_menu()
        option = int(input("Enter your choice:"))
        if option == 1:
            add_new_user(users)
        elif option == 2:
            show_all_users(users)
        elif option == 3:
            show_user()
        elif option == 4:
            break
        else:
            print("Option was not recognized. Try again!")



main_program_loop()

