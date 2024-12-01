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

#slicing
#index based
print(titanicdf.iloc[2:4, 1:4])

#conditional slicing
print(titanicdf.loc[titanicdf["Age"] < 18, ["Name", "Sex"]])

#changing values
titanicdf.iloc[0:3, 2] = ["gvfr", "gtrf", "yhgtf"]
print(titanicdf.iloc[0:5, 0:5])

#add a column
titanicdf["f"] = 0.5 * titanicdf["Fare"]
print(titanicdf.head())

#renaming columns
print(titanicdf.columns)
titanicdf.rename(columns = {"Pclass": "Class", "f": "Discountfare"}, inplace = True)
print(titanicdf.columns)

#saving to csv file
titanicdf.to_csv("pandas dataframe.csv")

#sorting
print(titanicdf.sort_values(by = "Age")[["Name", "Age"]])

#replace values
titanicdf["Sex"].replace({"male": "M", "female": "F"}, inplace = True)
print(titanicdf["Sex"])

#Grouping data
c = titanicdf.groupby("Class")
print(c.count())
print(c["Fare"].mean())
f = titanicdf.groupby(["Class", "Sex"])
print(f.count())

#aggregation funtions on multiple columns
print(titanicdf.agg({"Age": ["min", "max"], "Fare": "mean", "Survived": "count"}))

#operations on text data
print(titanicdf["Name"].str.lower())
titanicdf["lastn"] = titanicdf["Name"].str.split().str.get(-1)
print(titanicdf.head(10))
