import pandas as pd
#changing dictionary to dataframe
student = {"name": ["fgui", "asedr", "ergyh", "yghj"], "age": [10, 20, 10, 20], "city": ["london", "paris", "london", "paris"], "score": [23, 47, 23, 47]}
student_df = pd.DataFrame(student)
print(student_df)
print(type(student_df))

#number of rows and columns
print(student_df.shape)

#access columns
print(student_df["age"])
print(student_df["age"].max())
print(student_df["score"].mean())

#count of unique values
print(student_df["city"].value_counts())

#summary of data
print(student_df.info())

#statistical summary
print(student_df.describe())

#reading data from csv
titanicdf = pd.read_csv("titanic.csv")
print(titanicdf.info())
print(titanicdf)
#number of rows from the start, default is 5
print(titanicdf.head(2))
print(titanicdf.tail(4))
print(titanicdf["Name"])

#Find the maximum and the minimum age among the passengers.
print(titanicdf["Age"].max())
print(titanicdf["Age"].min())

#filtering records
print(titanicdf[titanicdf["Age"] < 10])
print(titanicdf[titanicdf["Pclass"] == 1])
print(titanicdf[(titanicdf["Pclass"] == 3) & (titanicdf["Age"] < 18)])
print(titanicdf[(titanicdf["Sex"] == "Female") | (titanicdf["Age"] > 13)])

#only few columns
print(titanicdf[["Age", "Pclass", "Survived"]])
