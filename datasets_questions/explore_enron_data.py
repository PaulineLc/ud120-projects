#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print(len(enron_data))
print(len(enron_data[enron_data.keys()[0]]))

num_poi = 0

for person in enron_data:
    if enron_data[person]['poi']:
        num_poi += 1

print(num_poi)

print(enron_data["Prentice james".upper()]["total_stock_value"])

print(enron_data["Colwell Wesley".upper()]["from_this_person_to_poi"])

print(enron_data["Skilling Jeffrey K".upper()]["exercised_stock_options"])

print("total payments")
print(enron_data["skilling jeffrey k".upper()]["total_payments"])
print(enron_data["lay kenneth l".upper()]["total_payments"])
print(enron_data["fastow andrew s".upper()]["total_payments"])

num_valid_salary = 0
num_valid_email = 0

for person in enron_data:
    if str(enron_data[person]["salary"]) != "NaN":
        num_valid_salary += 1
    if str(enron_data[person]["email_address"]) != "NaN":
        num_valid_email += 1

print("Num valid salary:", num_valid_salary)
print("Num valid email:", num_valid_email)

num_invalid_total_payment = 0
for person in enron_data:
    if str(enron_data[person]["total_payments"]) == "NaN":
        num_invalid_total_payment += 1

print("Invalid total payment:", num_invalid_total_payment)
print("%:", float(num_invalid_total_payment) / len(enron_data.keys()))

num_invalid_total_payment_poi = 0

for person in enron_data:
    if enron_data[person]["poi"] and str(enron_data[person]["total_payments"]) == "NaN":
        num_invalid_total_payment_poi += 1

print("Invalid total payments for poi %:", float(num_invalid_total_payment_poi) / num_poi)