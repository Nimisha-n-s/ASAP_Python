import pandas as pd
a=[1,7,2]

myvar=pd.Series(a,index=["a","b","c"])
print(myvar)
print(myvar["a"])