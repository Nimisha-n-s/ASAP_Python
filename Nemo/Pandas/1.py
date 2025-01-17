import pandas as pd

df = pd.read_csv('/home/admin-/Desktop/AS/Pandas/data1.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())