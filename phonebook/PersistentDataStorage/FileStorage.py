from datetime import datetime
from phonebook.User import User


class FileStorage:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        file = open(self.filepath, "r")
        users_from_file = []
        for line in file:
            user_as_list_of_strings = line.split(" ")
            if user_as_list_of_strings[0] == "\n":
                continue
            name = user_as_list_of_strings[0]
            surname = user_as_list_of_strings[1]
            phone_number = int(user_as_list_of_strings[2])
            date_time = datetime.strptime(user_as_list_of_strings[3] + " " + user_as_list_of_strings[4].rstrip(),
                                          '%Y-%m-%d %H:%M:%S')
            new_user = User(name, surname, phone_number, date_time)
            users_from_file.append(new_user)
        return users_from_file

    def save(self, user):
        """Add new user to file.txt"""
        file = open(self.filepath, "a")
        file.writelines(user.to_string() + "\n")
        file.close()