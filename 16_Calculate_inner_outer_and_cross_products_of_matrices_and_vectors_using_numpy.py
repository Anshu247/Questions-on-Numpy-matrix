import numpy as np

# Python Program illustrating
# numpy.inner() method

# vectors
arr1 = np.array([2, 6])
arr2 = np.array([3, 10])

res = np.inner(arr1, arr2) # inner method
print(res)

# matrices
x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])

res = np.inner(x, y)
print(res)
# ---------------------------------------------------

# Python Program illustrating
# numpy.outer() method

# Vectors
a = np.array([2, 6])
b = np.array([3, 10])

# Outer product of vectors
print("\nOuter product of vectors a and b =")
print(np.outer(a, b))

print("------------------------------------")

# Matrices
x = np.array([[3, 6, 4], [9, 4, 6]])
y = np.array([[1, 15, 7], [3, 10, 8]])

# Outer product of matrices
print("\nOuter product of matrices x and y =")
print(np.outer(x, y))
# -----------------------------------------------------

# Python Program illustrating
# numpy.cross() method

# Vectors
a = np.array([3, 6])
b = np.array([9, 10])

# Cross product of vectors
print("\nCross product of vectors a and b =")
print(np.cross(a, b))

print("------------------------------------")

# Matrices
x = np.array([[2, 6, 9], [2, 7, 3]])
y = np.array([[7, 5, 6], [3, 12, 3]])

# Cross product of matrices
print("\nCross product of matrices x and y =")
print(np.cross(x, y))

