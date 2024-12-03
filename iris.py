import pandas as pd
#Read the csv file
d = pd.read_csv("iris.csv")
print(d)

#Display the complete information of the dataset
print(d.info())

#How many rows and columns are there in the dataset
print("number of rows: ", d.shape[0], "number of columns: ", d.shape[1])

#What is the mean sepal length, sepal width, petal length and petal width for iris flower
print(d["sepal_length"].mean())
print(d["sepal_width"].mean())
print(d["petal_length"].mean())
print(d["petal_width"].mean())

#What is the count of each species of the flower
print(d["species"].value_counts())

#Display the last 8 records from the dataset
print(d.tail(8))

#Create a new dataset with only the records of “setosa” species
seto = (d[d["species"] == "setosa"])
print(seto)

#Find the record where the petal length of the flowers is more than the mean value
print(d.loc[d["petal_length"] > d["petal_length"].mean()])

#Add a new column to the dataset having a numeric code to represent each species.
#setosa: 1, virginica: 2, versicolor: 3
d["nspecies"] = d["species"]
print(d.head(10))
d["nspecies"].replace({"setosa": 1, "virginica": 2, "versicolor": 3}, inplace = True)
print(d.head(10))

#Sort the dataset according to the petal lengths.
print(d.sort_values(by = "petal_length"))

#Find the mean, minimum and maximum of the petal length, petal width, sepal length and sepal width.
print(d.agg({"petal_length": ["mean", "min", "max", "count"], "petal_width": ["mean", "min", "max", "count"], "sepal_length": ["mean", "min", "max"], "sepal_width": ["mean", "min", "max"]}))

#Display the average petal length, petal width, sepal length and sepal width for each species of the iris flower
f = d.groupby("species")
print(f.mean()[["sepal_length", "sepal_width", "petal_length", "petal_width"]])

#Change the species names to uppercase.
d["species"] = d["species"].str.upper()
#print(d["species"].str.upper())
print(d.head(10))