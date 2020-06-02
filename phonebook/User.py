from datetime import datetime

class User:

    def __init__(self, name, surname, phone_number, creation_date):
        """Initialization of attributes describing User profile """
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.creation_date = creation_date

    def to_string(self):
        record = self.name + ' ' + self.surname + ' ' + str(self.phone_number) + ' ' + datetime.strftime(self.creation_date, '%Y-%m-%d %H:%M:%S')
        return record
