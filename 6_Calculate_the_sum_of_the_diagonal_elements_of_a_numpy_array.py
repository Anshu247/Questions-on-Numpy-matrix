import numpy as np

arr1 = np.array([[1, 2, 3], [5, 6, 7], [9, 10, 11]])

# using trace method
trc = np.trace(arr1)
print(trc)

# using diagonal method
dig = np.diagonal(arr1)
print(sum(dig))