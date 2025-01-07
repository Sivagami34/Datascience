import pandas as pd
df = pd.read_csv("Data.csv")
df.info()
print(df)

#check for missing values
print(df.isnull().sum())

#remove missing values
#df.dropna(inplace = True)
#print(df)

#treating missing values
#manual

'''a = df["Age"].mean()
df.loc[df["Age"].isnull(),"Age"] = a
print(df)
'''

#imputing
from sklearn.impute import SimpleImputer
s = SimpleImputer(missing_values = pd.NA, strategy = "mean")
df[["Age", "Salary"]] = s.fit_transform(df[["Age", "Salary"]])
print(df)

#separate features
X = df[["Country","Age", "Salary"]]
y = df["Purchased"]

#encode categorical features
X = pd.get_dummies(X, columns = ["Country"], dtype = int)
print(X)
#encoding target value
#manual
y.replace({"No": 0, "Yes": 1}, inplace = True)
print(y)
