import numpy as np

# 1. using np.append()
ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])

# printing initial array
print("initial_array : ", str(ini_array))

# Array to be added as column
column_to_be_added = np.array([[1], [2], [3]])

# Adding column to array using append() method
arr = np.append(ini_array, column_to_be_added, axis=1)

# printing result
print ("1. resultant array", str(arr))
print('\r')
# -----------------------------------------------------------------

# 2. using np.concatenate()
import numpy as np

ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])

# Array to be added as column
column_to_be_added = np.array([[1], [2], [3]])

# Adding column to array using append() method
arr = np.concatenate([ini_array, column_to_be_added], axis=1)

# printing result
print ("2. resultant array", str(arr))
print('\r')
# -----------------------------------------------------------------

# 3. np.insert()
import numpy as np

ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])

# Array to be added as column
column_to_be_added = np.array([[1], [2], [3]])

# Adding column to array using append() method
arr = np.insert(ini_array, 0, column_to_be_added, axis=1)

# printing result
print ("3. resultant array", str(arr))
print('\r')
# ------------------------------------------------------------------

# 4. np.hstack()
import numpy as np

ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])

# Array to be added as column
column_to_be_added = np.array([1, 2, 3])

# Adding column to numpy array
result = np.hstack((ini_array, np.atleast_2d(column_to_be_added).T))

# printing result
print ("4. resultant array", str(result))
print('\r')
# ------------------------------------------------------------------

# 5. np.column_stack()
import numpy as np

ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])

# Array to be added as column
column_to_be_added = np.array([1, 2, 3])

# Adding column to numpy array
result = np.column_stack((ini_array, column_to_be_added))

# printing result
print ("5. resultant array", str(result))
print('\r')
# ------------------------------------------------------------------

# 6. np.r_
import numpy as np

ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])

# printing initial array
print("initial_array : ", str(ini_array));

# Array to be added as row
row_to_be_added = np.array([1, 2, 3])

# Adding row to numpy array
result = np.r_[ini_array,[row_to_be_added]]

# printing result
print ("6. resultant array", str(result))
print('\r')
# -----------------------------------------------------------------

# 7. np.insert
import numpy as np

ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])

# Array to be added as row
row_to_be_added = np.array([1, 2, 3])

#last row
row_n = arr.shape[0]
arr = np.insert(ini_array,row_n,[row_to_be_added],axis= 0)

# printing result
print ("7. resultant array", str(arr))
print('\r')
# ---------------------------------------------------------------

# 8. np.vstack()
import numpy as np

ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])

# Array to be added as row
row_to_be_added = np.array([1, 2, 3])

# Adding row to numpy array
result = np.vstack ((ini_array, row_to_be_added) )

# printing result
print ("8. resultant array", str(result))
print('\r')
# --------------------------------------------------------------

# 9. numpy.append()
# importing Numpy package
import numpy as np

# creating an empty 2d array of int type
empt_array = np.empty((0,2), int)
print("Empty array:")
print(empt_array)

# adding two new rows to empt_array
# using np.append()
empt_array = np.append(empt_array, np.array([[10,20]]), axis=0)
empt_array = np.append(empt_array, np.array([[40,50]]), axis=0)

print("\n9. Now array is:")
print(empt_array)

