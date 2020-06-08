from User import User
from phonebook.UI.TerminalUserInterface import TerminalUserInterface
from phonebook.PersistentDataStorage.FileStorage import FileStorage
from datetime import datetime
from enum import Enum


class Search(Enum):
    NAME = 1
    SURNAME = 2
    PHONE_NUMBER = 3


def add_new_user(users, user_as_dictionary):
    creation_date = datetime.now()
    new_user = User(user_as_dictionary["name"], user_as_dictionary["surname"], user_as_dictionary["phone_number"], creation_date)
    users.append(new_user)
    return new_user


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


def main_program_loop():
    tui = TerminalUserInterface()
    filepath = r"..\data\base.txt"
    file_storage = FileStorage(filepath)
    users = file_storage.load()
    while True:
        option = tui.get_action()
        if option == 1:
            user_data = tui.get_new_user_data()
            user = add_new_user(users, user_data)
            file_storage.save(filepath, user)
        elif option == 2:
            tui.show_users(users)
        elif option == 3:
            menu_choice = tui.get_search_action()
            if menu_choice == 1:
                user_data = tui.get_search_by_name_data()
                searching_results = search_user(user_data, users, Search.NAME)
                tui.show_users(searching_results)
            elif menu_choice == 2:
                user_data = tui.get_search_by_surname()
                searching_results = search_user(user_data, users, Search.SURNAME)
                tui.show_users(searching_results)
            else:
                return
        elif option == 4:
            break
        else:
            print("Option was not recognized. Try again!")


main_program_loop()
