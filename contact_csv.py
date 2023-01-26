from datetime import date
import pandas as pd

list_first_name = []
list_last_name = []
list_phone_number = []
list_creation_date = []

first_name = input("First Name : \n")
list_first_name.append(first_name)
last_name = input("Last Name : \n")
list_last_name.append(last_name)
phone_number = input("Phone Number : \n")
list_phone_number.append(phone_number)
creation_date = date.today()
list_creation_date.append(creation_date)

data = {}
data['First Name'] = list_first_name
data['Last Name'] = list_last_name
data['Phone Number'] = list_phone_number
data['Creation Date'] = list_creation_date
data_frame = pd.DataFrame(data)

data_frame.to_csv('contact.csv', index=False)
contact_csv = pd.read_csv('contact.csv')
print(contact_csv)
