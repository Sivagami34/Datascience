import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("heart_attack_dataset.csv")
df.info()
print(df.isnull().sum())
#gender distribution
g = df["Gender"].value_counts()
print(g)

o = df["Outcome"].value_counts()
print(o)

#males and females in heart attack patients
n = df[df["Outcome"] == "Heart Attack"]
nc = n["Gender"].value_counts()
print(nc)
plt.bar(nc.index, nc)
plt.title("males and females in heart attack patients")
plt.show()

#age vs cholesterol, blood pressure, BMI, stress level
a = df[["Age", "Cholesterol", "BloodPressure", "BMI", "StressLevel"]].groupby("Age")
ma = a.mean()
print(ma)
plt.plot(ma.index, ma["Cholesterol"], label = "Cholesterol")
plt.plot(ma.index, ma["BloodPressure"], label = "Blood Pressure")
plt.legend()
plt.show()

lc = ["Smoker", "AlcoholConsumption", "PhysicalActivity", "Diet"]
for c in lc:
    s = df[c].value_counts()
    print(s)
    g = df.groupby([c, "Outcome"])
    gc = g.count()
    print(gc)
    labels = []
    for i in gc.index:
        labels.append(str(i[0]) + i[1])
    plt.bar(labels, gc["Age"])
    plt.title(c + "wise Outcome")
    plt.show()
