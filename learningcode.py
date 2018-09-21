# Numpy arrays

import numpy as np

a = np.array[[1,2][3,4]]
print(a)

print(np.ndim(a))
print(np.shape(a))
print(np.size(a))
print(a.min())
print(a.sum())

b = np.array(range(20))
print(b.reshape(4,5))

c = np.zeros([4,3])
d = np.ones([2,5])
e = np.eye(5)

# Numpy arrays are mutable, such as lists
# Numpy has arange, which is like range, but for real numbers

print(np.arange(1.1,2.5,0.2))