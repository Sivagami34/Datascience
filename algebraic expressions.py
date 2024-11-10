import numpy as np
exp = input("Linear (l) or quadratic (q): ").lower()
if exp == "l":
    print("ax + b")
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    print(a,"x + ", b)
    x = np.arange(0, 11)
    print(a * x + b)
elif exp == "q":
    print("ax^2 + bx + c")
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    print(a, "x^2 +", b, "x +", c)
    x = np.arange(0, 11)
    print(a * (x^2) + b * x + c)