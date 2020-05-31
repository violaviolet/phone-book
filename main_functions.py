from User import User
from datetime import datetime



def load_data_from_file(users, filepath):
    file = open(filepath, "r")
    for line in file:
        user_as_list_of_strings = line.split(" ")
        name = user_as_list_of_strings[0]
        surname = user_as_list_of_strings[1]
        phone_number = int(user_as_list_of_strings[2])
        date_time = datetime.strptime(user_as_list_of_strings[3] + " " + user_as_list_of_strings[4].rstrip(), '%Y-%m-%d %H:%M:%S')
        new_user = User(name, surname, phone_number, date_time)
        users.append(new_user)


def add_to_file(filepath, users):
    """Add new user to file.txt"""
    file = open(filepath, "a")
    for user in users:
        g = user.to_string()
    file.writelines(str(g)+"\n")
    file.close()


def add_new_user(filepath, users):
    name = input("Enter user name: ")
    surname = input("Enter a surname: ")
    phone_number = input("Enter user phone number: ")
    creation_date = datetime.now()
    new_user = User(name, surname, phone_number, creation_date)
    users.append(new_user)
    add_to_file(filepath, users)


def show_all_users(users):
    for user in users:
        print(user.to_string())


def show_user(users):
    searching_filter = input("Enter searching filter:")
    for user in users:
        print(user)


def show_menu():
    print("----------------------MENU-----------------------------")
    print("""Choose what you'd like to do :
                        1. Add new user.
                        2. Display all users.
                        3. Display one user.
                        4. Close program. \n""")


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
            show_user(filepath)
        elif option == 4:
            break
        else:
            print("Option was not recognized. Try again!")


main_program_loop()

