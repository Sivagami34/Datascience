import matplotlib.pyplot as plt
import pandas as pd
#Create a pie chart to show the distribution of each type of species from Iris dataset.
df = pd.read_csv("iris.csv")
print(df.info())
p = df.groupby("species").count()
print(p)
plt.pie(p["sepal_length"], labels = p.index)
plt.show()