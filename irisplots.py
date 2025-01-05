import matplotlib.pyplot as plt
import pandas as pd
#Create a pie chart to show the distribution of each type of species from Iris dataset.
df = pd.read_csv("iris.csv")
print(df.info())
p = df.groupby("species").count()
print(p)
plt.pie(p["sepal_length"], labels = p.index)
plt.show()

#Create subplots with 4 scatter plots between: petal length and petal width, 
#petal length and sepal width, sepal length and sepal width, petal wodth and sepal width
plt.subplot(2, 2, 1)
plt.scatter(df["petal_length"], df["petal_width"])
plt.subplot(2, 2, 2)
plt.scatter(df["petal_length"], df["sepal_width"])
plt.subplot(2, 2, 3)
plt.scatter(df["sepal_length"], df["sepal_width"])
plt.subplot(2, 2, 4)
plt.scatter(df["petal_width"], df["sepal_width"])
plt.show()
