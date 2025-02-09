import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("supermarket_sales.csv")
df.info()
print(df.isnull().sum())
print(df["Invoice ID"].value_counts())
df["Date"] = pd.to_datetime(df["Date"])
df["Time"] = pd.to_datetime(df["Time"])
df.info()
#Number of customers of each type at the supermarket
nc = df["Customer type"].value_counts()
print(nc)
plt.bar(nc.index, nc.values)
plt.show()