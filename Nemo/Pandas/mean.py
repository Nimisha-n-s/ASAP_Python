import pandas as pd

df = pd.read_csv('/home/admin-/Desktop/AS/Pandas/data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True) 