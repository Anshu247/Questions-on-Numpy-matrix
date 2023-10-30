import numpy as np

# Code 1
mat1 = np.matrix('[1, 2; 3, 4]')
res1 = mat1.sum()

print(res1)

# Code 2
mat2 = np.matrix('[1, 2, 3; 4, 5, 6; 7, 8, 9]')
res2 = mat2.sum(axis = 0)
res1 = mat2.sum(axis = 1)

print(res1)
print(res2)
