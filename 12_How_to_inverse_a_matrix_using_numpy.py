# Import required package
import numpy as np

# Code 1
# Taking a 3 * 3 matrix
A = np.array([[6, 1, 1],
			[4, -2, 5],
			[2, 8, 7]])

# Calculating the inverse of the matrix
print(np.linalg.inv(A))

# Code 2
# Import required package
import numpy as np

# Inverses of several matrices can
# be computed at once
A = np.array([[[1., 2.], [3., 4.]],
			[[1, 3], [3, 5]]])

# Calculating the inverse of the matrix
print(np.linalg.inv(A))
