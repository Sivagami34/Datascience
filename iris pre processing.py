import pandas as pd
df = pd.read_csv("iris.csv")
df.info()
print(df)

print(df.isnull().sum())

X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]

print(y.value_counts())
y.replace({"setosa" : 0, "versicolor" : 1, "virginica" : 2}, inplace = True)
print(y)

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, train_size = 0.7, random_state = 50)

from sklearn.tree import DecisionTreeClassifier
t = DecisionTreeClassifier()
t.fit(Xtrain, ytrain)
p = t.predict(Xtest)
print(y[0:10])
print(p[0:10])

from sklearn import metrics
s = metrics.accuracy_score(ytest, p)
print(s)