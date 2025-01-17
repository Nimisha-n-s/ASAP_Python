import csv
import os

# Create new csv file
def create_csv(filename, headers, num_rows):
    rows = []
    for roll_number in range(1, num_rows + 1):
        # Create a list of empty marks for each subject (same length as subject list)
        current_marks = [""] * (len(headers) - 2)  # Excluding RollNumber and CurrentMarks columns
        total_marks = 100  # CurrentMarks
        row = [roll_number] + current_marks + [total_marks]
        rows.append(row)
    
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"CSV file '{filename}' created successfully")

# Function to generate subject names
def generate_subject_names():
    return [
        "Maths", "Physics", "Chemistry", "Biology", "English", "Malayalam", "Hindi", 
        "Geography", "History", "Politics"
    ]

filename = "sample_data1.csv"
subjects = generate_subject_names()  # Get the subject names list
headers = ["RollNumber"] + subjects + ["CurrentMarks"]  # Build the header list
num_rows = 100  # Number of rows to generate

create_csv(filename, headers, num_rows)
