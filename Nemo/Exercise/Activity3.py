import csv
import os


def create_csv(filename, headers, rows):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"csv file '{filename}' created successfully")

filename = "Employee.csv"
headers = ["ID", "Name", "Age", "Salary","Department","Experience"]
rows = [
    [0,"Alice",25,50000,"HR",2],
    [1,"Bob",30,60000 ,"Finance",5],
    [2,"Charlie",40,70000,"Tech",8],
    [3,"David",45,80000,"Tech",10],
    [4,"Eva",50,90000,"HR",12]
]

create_csv(filename, headers, rows)

import pandas as pd

df = pd.read_csv('/home/asietccf/Desktop/Nemo/ASAP_Python_Bootcamp-main/AS/Employee.csv')

sorted_by_department = df.sort_values(by='Department', ascending=True)
print("Sorted by Department (Ascending):")
print(sorted_by_department)


sorted_by_salary = df.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary (Descending):")
print(sorted_by_salary)
