import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")
print(df.info())

#Plot a bar graph of count of passengers in different Pclass from titanic dataset
n = df["Pclass"].value_counts()
plt.bar(n.index, n)
plt.xticks(ticks = n.index, labels=n.index)
plt.show()

#Plot a histogram for age of passengers in intervals of 10 years.
age = df["Age"]
i = np.arange(0, age.max() + 1, 10)
plt.hist(age, i)
plt.show()

#Draw a pie chart to show the ratio of number of passengers that survived or didn’t survive
s = df["Survived"].value_counts()
plt.pie(s, labels = s.index)
plt.show()