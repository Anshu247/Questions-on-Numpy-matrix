import numpy as np

arr1 = np.array([2 + 3j, 4 + 5j])
arr2 = np.array([6 + 7j, 8 + 9j])

res = np.vdot(arr1, arr2)
print(res)