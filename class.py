from datetime import datetime


class Contact:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.creation_time = datetime.today().date()
        self.updated_phone = None

    def update_phone(self, new_phone):
        self.updated_phone = datetime.today().date()
        self.phone = new_phone

    def show_contact(self):
        print(self.first_name)
        print(self.last_name)
        print(self.phone)
        print(self.creation_time)


Oscar = Contact("Oscar", "Pimpaud", "0647246556")
Oscar.affiche_contact()
Oscar.update_phone("377288992")
Oscar.affiche_contact()
