import datetime


class Contact:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.creation_time = datetime.datetime.now()
        self.updated_phone = None

    def update_phone(self, new_phone):
        self.updated_phone = datetime.datetime.now()
        self.phone = new_phone
