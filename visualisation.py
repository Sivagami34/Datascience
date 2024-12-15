import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 11)
y = np.random.randint(10, 21, 10)

# line plot
plt.figure(figsize = (10, 6))
plt.title("Line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.axis([0, 10, 10, 20])
plt.xticks(ticks = x, labels = x, rotation = 20)
plt.plot(x, y, "r-^", label = "x vs random y", linewidth = 5)
plt.legend()
plt.show()

#multiple graphs on single plot
plt.xlabel("x value")
plt.ylabel("y val")
plt.plot(x, x**2, label = "x**2")
plt.plot(x, x**3, label = "x**3")
plt.legend()
plt.show()

#bar plot
plt.bar([1, 3, 5, 7], [45, 57, 67, 23])
plt.show()

#multiple bar graph
plt.bar([1, 3, 5, 7], [21, 43, 67, 34])
plt.bar([2, 4, 6, 8], [20, 34, 76, 44])
plt.show()

#categorical data with bar plot
plt.bar(["male", "female"], [12, 15])
plt.show()
