# Create an array with the radius of 10 cylinders randomly picked from a range of 20 to 80.
import numpy as np
radius = np.random.randint(20, 80, 10)
print(radius)
# Create another array with the height of 10 cylinders randomly picked in a range of 40 to 100.
height = np.random.randint(40, 100, 10)
print(height)
# Calculate the volume of all the 10 cylinders.
v = np.pi * radius**2 * height
print(v)

# select volumes lower than 800000
print(v[v < 800000])