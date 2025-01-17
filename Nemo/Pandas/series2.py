import pandas as pd

df=pd.read_csv('/home/admin-/Desktop/AS/Pandas/color_srgb.csv')
#pd.options.display.max_rows=10
#print(pd.options.display.max_rows)

#print(df.head(10)) # top 10
#print(df.tail(5)) # last 10
#new_df = df.dropna() #to clear a row  "cleaning empty cells"
#print(new_df.to_string())
#df.fillna(14, inplace =True)  #to fill the 
print(df.to_string())
#df[RGB].fillna(9,inplace=True) #to fill particular place
x = df["HEX"].mean()

df["HEX"].fillna(x, inplace = True) 