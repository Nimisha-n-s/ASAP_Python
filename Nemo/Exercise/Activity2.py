#create a data frame employee
#fliter the dataframe:
  #1)have salary greater than 60000
 #2)have more than five years of experience
#3)belong to the tech department
#4)after filtering display only the name,salary,and experience colum

import pandas as pd

Employee = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 40, 45, 50],
    "Salary": [50000, 60000, 70000, 80000, 90000],
    "Department": ["HR", "Finance", "Tech", "Tech", "HR"],
    "Experience": [2, 5, 8, 10, 12]  
}

df = pd.DataFrame(Employee)
print(df.to_string())

filtered = df[(df['Salary'] > 60000) & 
              (df['Experience'] > 5) & 
              (df['Department'] == 'Tech')]

filtered = filtered[['Name', 'Salary', 'Experience']]
print("filterd")
print(filtered.to_string())

