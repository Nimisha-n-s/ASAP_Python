import csv
import os

#create new csv file
def create_csv(filename, headers, rows):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"csv file '{filename}' created successfully")

filename = "sample_data.csv"
headers = ["ID", "Name", "Age", "Department"]
rows = [
    [1, "Alice", 30, "HR"],
    [2, "Bob", 56, "Software Developer"],
    [3, "Charlie", 25, "Sales"]
]

create_csv(filename, headers, rows)
