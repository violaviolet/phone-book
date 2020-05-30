from User import User
import datetime



def add_to_file(filepath, users):
    """Add new user to file.txt"""
    f = open(filepath, "a")
    for user in users:
        g = user.to_string()
    f.writelines(str(g)+"\n")


def add_new_user(users):
    name = input("Enter user name: ")
    phone_number = input("Enter user phone number: ")
    creation_date = datetime.datetime.now()
    new_user = User(name, phone_number, creation_date)
    print(new_user.to_string())
    users.append(new_user)


def show_all_users(filepath):
    with open(filepath) as file:
        for line in file:
            print(line)
    file.close()


def show_user(filepath):
    choice = input("Enter single user name.")
    with open(filepath) as file:
        for line in file:
            if line.startswith(choice):
                print(line)



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
    while True:
        show_menu()
        option = int(input("Enter your choice:"))
        if option == 1:
            add_new_user(users)
            add_to_file(filepath, users)
        elif option == 2:
            show_all_users(filepath)
        elif option == 3:
            show_user(filepath)
        elif option == 4:
            break
        else:
            print("Option was not recognized. Try again!")


main_program_loop()

