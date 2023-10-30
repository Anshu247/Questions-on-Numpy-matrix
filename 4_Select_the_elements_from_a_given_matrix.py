import numpy as np

mat1 = np.matrix('[1, 2, 3, 4, 5]')
mat2 = np.matrix('[1, 2, 3; 4, 5, 6; 7, 8, 9]')

res1 = mat1.take(2, axis = 1)
res2 = mat2.take(0, 1)

print(res1)
print(res2)