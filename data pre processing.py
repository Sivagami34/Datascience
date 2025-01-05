import pandas as pd
df = pd.read_csv("Data.csv")
df.info()
print(df)

#check for missing values
print(df.isnull().sum())

#remove missing values
df.dropna(inplace = True)
print(df)