from User import User
from datetime import datetime


def load_data_from_file(users, filepath):
    file = open(filepath, "r")
    for line in file:
        user_as_list_of_strings = line.split(" ")
        name = user_as_list_of_strings[0]
        surname = user_as_list_of_strings[1]
        phone_number = int(user_as_list_of_strings[2])
        date_time = datetime.strptime(user_as_list_of_strings[3] + " " + user_as_list_of_strings[4].rstrip(),
                                      '%Y-%m-%d %H:%M:%S')
        new_user = User(name, surname, phone_number, date_time)
        users.append(new_user)


def add_to_file(filepath, user):
    """Add new user to file.txt"""
    file = open(filepath, "a")
    file.writelines(user.to_string() + "\n")
    file.close()


def add_new_user(filepath, users):
    name = input("Enter user name: ")
    surname = input("Enter a surname: ")
    phone_number = input("Enter user phone number: ")
    creation_date = datetime.now()
    new_user = User(name, surname, phone_number, creation_date)
    users.append(new_user)
    add_to_file(filepath, new_user)


def show_all_users(users):
    for user in users:
        print(user.to_string())


"""def show_user(users):
    searching_filter = input("Enter searching filter:")
    for user in users:
        print(user)
"""


def search_user_by_name(users):
    name = input("Enter user name:")
    at_least_one_result_found = False
    for user in users:
        if user.name == name:
            print(user.to_string())
            at_least_one_result_found = True
    if not at_least_one_result_found:
        print("User does not exist")


def search_user_by_surname(users):
    surname = input("Enter user surname:")
    at_least_one_result_found = False
    for user in users:
        if user.surname == surname:
            print(user.to_string())
            at_least_one_result_found = True
    if not at_least_one_result_found:
        print("User does not exist")


def show_menu():
    print("----------------------MENU-----------------------------")
    print("""Choose what you'd like to do :
                        1. Add new user.
                        2. Display all users.
                        3. Display one user.
                        4. Close program. \n""")


def show_filtering_options_menu():
    print("-----------------Looking--For--A-User------------")
    print("""Choose what you'd like to do:
                  1. Search a user by a name.
                  2. Search a user by a surname. """)


def main_program_loop():
    users = []
    filepath = 'base.txt'
    load_data_from_file(users, filepath)
    while True:
        show_menu()
        option = int(input("Enter your choice:"))
        if option == 1:
            add_new_user(filepath, users)
        elif option == 2:
            show_all_users(users)
        elif option == 3:
            show_filtering_options_menu()
            option1 = int(input("Enter your choice:"))
            if option1 == 1:
                search_user_by_name(users)
            elif option1 == 2:
                search_user_by_surname(users)
            else:
                return
        elif option == 4:
            break
        else:
            print("Option was not recognized. Try again!")


main_program_loop()
