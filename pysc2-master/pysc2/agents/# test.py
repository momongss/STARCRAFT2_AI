import numpy as np

a = np.array([1,23,4,5,100,5])
b = np.array([[1,23,4,5,100,5]])

c = a.reshape(1, 6)
print(c)
print(a)