from datetime import datetime


def create_contact():
    first_name = input("Veuillez entrer le prénom :")
    last_name = input("Veuillez entrer le nom :")
    phone = input("Veuillez entrer le numéro de mobile :")
    creation_date = datetime.today().date()
    dict_contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "creation_date": creation_date
    }
    return dict_contact


def show_contact(contact):
    for values in contact.values():
        print(values)


contact = create_contact()
show_contact(contact)
