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
#Find the number of male and female members. Show them on a pie chart.
m = df[df["Customer type"] == "Member"]
gc = m["Gender"].value_counts()
print(gc)
plt.pie(gc, labels = gc.index, autopct='%1.1f%%')
plt.show()
#Create a line plot with day-wise total sales.
g = df.groupby("Date")
s = g["Total"].sum()
print(s)
plt.plot(s.index, s)
plt.show()

#per person purchase per day
m = g["Total"].mean()
print(m)
plt.plot(m.index, m)
plt.show()

#Find the different payment methods. 
#Show the percentage invoices settled with each of the payment method.
p = df.groupby("Payment")
c = p["Invoice ID"].count()
print(c)
plt.pie(c, labels = c.index, autopct='%1.1f%%')
plt.show()

#Find the quantity of items sold in each product line. Visualize the result.
pl = df.groupby("Product line")
q = pl["Quantity"].sum()
print(q)
plt.bar(q.index, q)
plt.show()
