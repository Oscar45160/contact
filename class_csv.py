import pandas as pd
from datetime import datetime
import os


class Contact:
    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.creation_time = datetime.today().date()
        self.updated_phone = None

        # convert the object to a DataFrame
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "creation_time": self.creation_time,
            "updated_phone": self.updated_phone
        }
        df = pd.DataFrame(data, index=[0])

        # if the file doesn't exist, create it and add the header
        if not os.path.isfile("data/contact_class.csv"):
            df.to_csv("data/contact_class.csv", header=True)
        else:  # else it exists so append without writing the header
            df.to_csv("data/contact_class.csv", mode='a', header=False, index=False)

    def update_phone(self, new_phone):
        self.updated_phone = datetime.today().date()
        self.phone = new_phone

        # convert the object to a DataFrame
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "creation_time": self.creation_time,
            "updated_phone": self.updated_phone
        }
        df = pd.DataFrame(data, index=[0])

        df.to_csv("data/contact_class.csv", mode='a', header=False, index=False)

    def show_contact(self):
        print(self.first_name)
        print(self.last_name)
        print(self.phone)
        print(self.creation_time)


Oscar = Contact("Oscar", "Pimpaud", "0647246556")
Oscar.show_contact()
