class TerminalUserInterface:

    def __init__(self):
        pass

    def get_new_user_data(self):
        name = input("Enter user name: ")
        surname = input("Enter a surname: ")
        phone_number = input("Enter user phone number: ")
        user = {
            "name": name,
            "surname": surname,
            "phone_number": phone_number,
        }
        return user

    def get_search_by_name_data(self):
        name = input("Enter user name:")
        return name

    def get_search_by_surname(self):
        surname = input("Enter user surname:")
        return surname

    def show_users(self, users):
        for user in users:
            print(user.to_string())

    def get_action(self):
        print("----------------------MENU-----------------------------")
        print("""Choose what you'd like to do :
                            1. Add new user.
                            2. Display all users.
                            3. Display one user.
                            4. Close program. \n""")
        option = int(input("Enter your choice:"))
        return option

    def get_search_action(self):
        print("-----------------Looking--For--A-User------------")
        print("""Choose what you'd like to do:
                      1. Search a user by a name.
                      2. Search a user by a surname. """)
        menu_choice = int(input("Enter your choice:"))
        return menu_choice