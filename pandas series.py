import pandas as pd
import numpy as np
#convert list/numpy array to series
a = np.random.randint(1, 100, 10)
print(a)
print(type(a))
b = pd.Series(a)
print(b)
print(type(b))

#retrieve items
#print(b[3:8])

#statistical operation
print(b.min())
print(b.max())
print(b.mean())
print(b.median())
print(b.mode())