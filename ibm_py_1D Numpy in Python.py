# Import the libraries

import time
import sys
import numpy as np

import matplotlib.pyplot as plt
# %matplotlib inline


# Plotting functions

def Plotvec1(u, z, v):
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


def Plotvec2(a, b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

# Create numpy array
c = np.array([20, 1, 2, 3, 4])
print(c)

c[0] = 100
c[4] = 0
c[3:5] = 300, 400
print(c)


# Create the index list
select = [0, 2, 3]

# Use List to select elements
d = c[select]
print(d)

import numpy as np

aaa = np.array([[1,2,3,4,], [11,22,33,44], [10,20,30,40]])
print("Get the number of dimensions of numpy array", aaa.ndim)
print("Get the shape/size of numpy array", aaa.shape)
print("Get the mean of numpy array", aaa.mean())
print("Get the standard deviation of numpy array", aaa.std())

"""
Numpy Array Operations
"""
# Array Addition

u = np.array([1, 0])
v = np.array([0, 1])
z = u + v

# Plot numpy arrays
Plotvec1(u, z, v)

