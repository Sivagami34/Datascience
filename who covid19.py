import pandas as pd
df = pd.read_csv("WHO-COVID-19-global-data.csv")
df.info()
df["DateReported"] = pd.to_datetime(df["DateReported"])
df.info()
print(df.isnull().sum())
df = df[["DateReported", "Country", "New_cases", "Cumulative_cases", "New_deaths", "Cumulative_deaths"]]
#daily total cases worldwide
d = df.groupby("DateReported")
sum = d.sum()
print(sum)
print(sum.columns)
import matplotlib.pyplot as plt
plt.plot(sum.index, sum["Cumulative_cases"])
plt.title("daily total cases worldwide")
plt.show()
#daily new cases worldwide
plt.plot(sum.index, sum["New_cases"])
plt.show()

country = input("Enter country: ")
c = df.loc[df["Country"] == country]
print(c)
plt.plot(c["DateReported"], c["New_cases"])
plt.show()
