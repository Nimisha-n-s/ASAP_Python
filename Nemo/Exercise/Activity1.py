#create a dataframe with student name,mark,and grade,filter students with mark>50
import pandas as pd

student = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Mark": [45, 67, 82, 50, 91],
    "Grade": ["C", "B", "A", "C", "A"]
}

df = pd.DataFrame(student)
print(df.to_string())
filtered = df[df["Mark"] > 50]


print(filtered)
