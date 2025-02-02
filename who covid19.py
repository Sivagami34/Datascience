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