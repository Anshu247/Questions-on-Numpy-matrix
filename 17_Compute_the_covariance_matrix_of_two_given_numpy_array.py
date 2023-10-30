import numpy as np

arr1 = np.array([1, 2, 1])
arr2 = np.array([0, 2, 2])

res = np.cov(arr1, arr2)
print(res)