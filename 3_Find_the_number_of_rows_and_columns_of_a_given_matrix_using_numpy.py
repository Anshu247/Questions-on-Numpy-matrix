import numpy as np

arr1 = np.array([1, 2, 3, 4, 5]) # 1D array
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) # 2D array

x = np.shape(arr1) # for 1D array
y = np.shape(arr2) # for 2D array

rows1 = x 
rows2, columns2 = y

print(rows1)

print("Rows:",rows2)
print("Columns:",columns2)
