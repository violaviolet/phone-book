from User import User
from datetime import datetime
from enum import Enum


class Search(Enum):
    NAME = 1
    SURNAME = 2
    PHONE_NUMBER = 3


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


def get_data_to_create_new_user():
    name = input("Enter user name: ")
    surname = input("Enter a surname: ")
    phone_number = input("Enter user phone number: ")
    user = {
        "name": name,
        "surname": surname,
        "phone_number": phone_number,
    }
    return user


def add_new_user(users, user_as_dictionary):
    creation_date = datetime.now()
    new_user = User(user_as_dictionary["name"], user_as_dictionary["surname"], user_as_dictionary["phone_number"], creation_date)
    users.append(new_user)
    return new_user


def add_to_file(filepath, user):
    """Add new user to file.txt"""
    file = open(filepath, "a")
    file.writelines(user.to_string() + "\n")
    file.close()


def show_users(users):
    for user in users:
        print(user.to_string())


def get_data_to_search_by_name():
    name = input("Enter user name:")
    return name


def get_data_to_search_by_surname():
    surname = input("Enter user surname:")
    return surname


def search_user(user_data, users, field):
    searched_users = []
    for user in users:
        if field == Search.NAME:
            if user.name == user_data:
                searched_users.append(user)
        elif field == Search.SURNAME:
            if user.surname == user_data:
                searched_users.append(user)
        else:
            return searched_users
    return searched_users


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
    filepath = r"C:\Users\wswist\PycharmProjects\Project_Python2020\Projekt_Phone_book\phone-book\data\base.txt"
    load_data_from_file(users, filepath)
    while True:
        show_menu()
        option = int(input("Enter your choice:"))
        if option == 1:
            user_data = get_data_to_create_new_user()
            user = add_new_user(users, user_data)
            add_to_file(filepath, user)
        elif option == 2:
            show_users(users)
        elif option == 3:
            show_filtering_options_menu()
            menu_choice = int(input("Enter your choice:"))
            if menu_choice == 1:
                user_data = get_data_to_search_by_name()
                searching_results = search_user(user_data, users, Search.NAME)
                show_users(searching_results)
            elif menu_choice == 2:
                user_data = get_data_to_search_by_surname()
                searching_results = search_user(user_data, users, Search.SURNAME)
                show_users(searching_results)
            else:
                return
        elif option == 4:
            break
        else:
            print("Option was not recognized. Try again!")


main_program_loop()
