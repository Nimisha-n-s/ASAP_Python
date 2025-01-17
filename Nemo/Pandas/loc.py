#to change value of specefic location
import pandas as pd

df=pd.read_csv('/home/admin-/Desktop/AS/Pandas/data1.csv')
#df.loc[7,'Duration']=45
for x in df.index:
    if df.loc[x,"Pulse"]>100:
        df.loc[x,"Pulse"]=777

print(df.to_string())