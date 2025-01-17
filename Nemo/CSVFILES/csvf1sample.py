import csv
import os

#create new csv file
def create_csv(filename, headers, num_rows):
    rows=[]
    for i in range(1,num_rows+1):
        #current_marks =[""]*(len(headers)-2) 
        #total_marks = 100
        #row =[roll_number]+current_marks+[total_marks]
        #rows.append(row)   
        rows.append([i,"","","","","","","","","","",100])
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"csv file '{filename}' created successfully")
def generate_subject_names():
    return [
        "Maths", "Physics", "Chemistry", "Biology", "English", "Malayalam", "Hindi", 
        "Geography", "History", "Politics"
    ]


filename = "sample_data1.csv"
subjects = generate_subject_names() 
headers = ["RollNumber"] + subjects + ["CurrentMarks"]  
num_rows = 100  

create_csv(filename, headers, num_rows)
