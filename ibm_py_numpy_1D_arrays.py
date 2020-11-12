# Numpy 1D Arrays
import inline as inline
import numpy as np
a = np.array([0,1,2,3,4])

print(a)
print(type(a))

print(a.dtype)
print("size of a :", a.size, ",  dimension of a :", a.ndim, ",  shape of a :", a.shape)

# Vectors
print("------- Vectos ------")

u = [1, 0]
v = [0, 1]
z = []
for n,m in zip(u,v):
    z.append(n + m)
print(z)

print("------- with np ------")
u = np.array([1, 0])
v = np.array([0, 1])
z = v + u
print(z)

print("------  matplotlib inline -----")
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

import matplotlib.pyplot as plt
# %matplotlib inline
plt.plot(x, y)