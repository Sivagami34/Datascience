import numpy as np
prime = [1,2,3,5,7]
print(prime)
print(type(prime))

array = np.array(prime)
print(array)
print(type(array))

for num in prime:
    num = num * 2
    print(num)

print(array * 2)

#array of 0
n = np.zeros(5, int)
print(n)

m = np.zeros((3,4))
print(m)

#array of 1
o = np.ones((2, 3), int)
print(o)

#dimension
print(n.ndim)
print(o.ndim)

#shape
print(n.shape)
print(o.shape)

#size
print(n.size)
print(o.size)

#arrays in range
r = np.arange(1, 11, 2)
print(r)

#change arrangement
print(np.random.permutation(r))
print(np.random.permutation(r))
print(np.random.permutation(r))

#array of random numbers
nu = np.random.randint(0, 10, 10)
print(nu)

anu = np.random.randint(1, 50, (2,4))
print(anu)

anum = np.random.randint(50, 100, (2,4))
print(anum)
#opperation between arrays
print(anu + anum)

#reshape array
print(anu.reshape(8, 1))
print(anu.reshape(8))

#slicing array
print(nu)
print(nu[2:8])
print(nu[:8])
print(nu[2:])
print(nu[0::2])
print(nu[::-1])

#slicing with selected index
print(nu[[0,2,6,8]])

#conditional slicing
print(nu[nu % 2 == 0])
print(nu[nu > 5])

#2D array slicing
an = np.random.randint(1, 50, (5,4))
print(an)
print(an[1: 4, 1: 4])

print(an[an % 2 != 0])
