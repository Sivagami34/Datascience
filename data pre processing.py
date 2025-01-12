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

#separate features and target
X = df[["Country","Age", "Salary"]]
y = df["Purchased"]

#encode categorical features
X = pd.get_dummies(X, columns = ["Country"], dtype = int)
print(X)
#encoding target value
#manual
#y.replace({"No": 0, "Yes": 1}, inplace = True)
#print(y)

#label encode
from sklearn.preprocessing import LabelEncoder
l = LabelEncoder()
y = l.fit_transform(y)
print(y)

#standard scaling
from sklearn.preprocessing import StandardScaler
sd = StandardScaler()
X["Salary"] = sd.fit_transform(X[["Salary"]])
print(X)

#split data into training set and test set
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest= train_test_split(X, y, train_size = 0.8, random_state = 60)
print("Xtrain\n", Xtrain)
print("Xtest\n", Xtest)
print("ytrain\n", ytrain)
print("ytest\n", ytest)
