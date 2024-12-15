import numpy as np
import matplotlib.pyplot as plt
exp = input("Linear (l) or quadratic (q): ").lower()
if exp == "l":
    print("ax + b")
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    eq = str(a) + "x + " + str(b)
    print(eq)
    x = np.arange(0, 11)
    y = (a * x) + b
    print(y)
elif exp == "q":
    print("ax^2 + bx + c")
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    eq = str(a) + "x^2 +" + str(b) + "x +" + str(c)
    print(eq)
    x = np.arange(0, 11)
    y = ((x**2) * a) + (b * x) + c
    print(y)

plt.title(eq)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
plt.show()