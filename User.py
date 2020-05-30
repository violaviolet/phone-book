class User:

    def __init__(self, name, phone_number, creation_date):
        """Initialization of attributes describing User profile """
        self.name = name
        self.phone_number = phone_number
        self.creation_date = creation_date

    def to_string(self):
        record = self.name + ' ' + str(self.phone_number) + ' ' + str(self.creation_date)
        return record
