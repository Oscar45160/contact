import pandas as pd
from datetime import datetime
import os


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

    # convert the dictionary to a DataFrame
    df_contact = pd.DataFrame(dict_contact, index=[0])
    # if the file doesn't exist, create it and add the header
    if not os.path.isfile("contact.csv"):
        df_contact.to_csv("contact.csv", header=True, index=False)
    else:  # else it exists so append without writing the header
        df_contact.to_csv("contact.csv", mode='a', header=False, index=False)
    return dict_contact


dic = create_contact()
print(dic)
