from class_User import User
from datetime import date


def prepare_data():
    name = input("Enter user name: ")
    phone_number = input("Enter user phone number: ")
    creation_date = date.today()
    new_user = User(name, phone_number, creation_date)
    print(new_user.get_record())



prepare_data()

