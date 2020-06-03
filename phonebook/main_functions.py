from User import User
import data
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


def get_data_from_user():
    name = input("Enter user name: ")
    surname = input("Enter a surname: ")
    phone_number = input("Enter user phone number: ")
    user = {
        "name": name,
        "surname": surname,
        "phone_number": phone_number,
    }
    return user


def add_new_user(users, user_as_dictionary, filepath):
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


def get_searching_name():
    name = input("Enter user name:")
    return name


def get_searching_surname():
    surname = input("Enter user surname:")
    return surname


def search_user_by_name(name, users):
    searched_users = []
    for user in users:
        if user.name == name:
            searched_users.append(user)
    return searched_users


def search_user_by_surname(surname, users):
    searched_users = []
    for user in users:
        if user.surname == surname:
            searched_users.append(user)
    return searched_users


def search_user(user_data, users, type_of_searching):
    searched_users = []
    if type_of_searching == 1:
        for user in users:
            if user.name == user_data:
                searched_users.append(user)
        return searched_users
    elif type_of_searching == 2:
        for user in users:
            if user.surname == user_data:
                searched_users.append(user)
        return searched_users
    else:
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
            user_data = get_data_from_user()
            user = add_new_user(users, user_data, filepath)
            add_to_file(filepath, user)
        elif option == 2:
            show_users(users)
        elif option == 3:
            show_filtering_options_menu()
            menu_choice = int(input("Enter your choice:"))
            if menu_choice == 1:
                user_data = get_searching_name()
                searching_results = search_user(user_data, users, 1)
                show_users(searching_results)
            elif menu_choice == 2:
                user_data = get_searching_surname()
                searching_results = search_user(user_data, users, 2)
                show_users(searching_results)
            else:
                return
        elif option == 4:
            break
        else:
            print("Option was not recognized. Try again!")


main_program_loop()
