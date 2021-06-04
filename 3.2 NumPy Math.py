import numpy as np

# We'll create a couple of matrix arrays to perform our math operations on. The
# first array will represent the matrix:
# [-.5] [.8] [-.1]
# [0.0] [-1.2] [1.3]

# The second array will represent the matrix:
# [1.2] [3.1]
# [1.2] [0.3]
# [1.5] [2.2]

# Set arr equal to np.array applied to a list of lists representing the first
# matrix.

# Then set arr2 equal to np.array applied to a list of lists representing the
# second matrix.

arr = np.array([[-.5, .8, -.1], [0, -1.2, 1.3]])
arr2 = np.array([[1.2, 3.1], [1.2, .3], [1.5, 2.2]])

# Next we'll apply some arithmetic to arr. Specifically, we'll do
# multiplication, addition, and squaring.

# Set multiplied equal to arr multiplied by np.pi.

# Then set added equal to the result of adding arr and multiplied.

# Finally, set squared equal to added with each of its elements squared.

multiplied = arr * np.pi
added = arr + multiplied
squared = added ** 2

# After the arithmetic operations, we'll apply the base e exponential and
# logarithm to our array matrices.

# Set exponential equal to np.exp applied to squared.

# Then set logged equal to np.log applied to arr2.

exponential = np.exp(squared)
logged = np.log(arr2)

# Note that exponential has shape (2, 3) and logged has shape (3, 2). So we can
# perform matrix multiplication both ways.

# Set matmul1 equal to np.matmul with first argument logged and second argument
# exponential. Note that matmul1 will have shape (3, 3).

# Then set matmul2 equal to np.matmul with first argument exponential and
# second argument logged. Note that matmul2 will have shape (2, 2).

matmul1 = np.matmul(logged, exponential)
matmul2 = np.matmul(exponential, logged)
