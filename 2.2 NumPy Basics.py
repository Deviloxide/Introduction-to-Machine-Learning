import numpy as np

# First, set arr equal to np.arange with 12 as the only argument.

# Then, set reshaped equal to np.reshape with arr as the first argument and
# (2, 3, 2) as the second argument.
arr = np.arange(12)

arr = np.arange(12)
reshaped = np.reshape(arr, (2, 3, 2))

# Next we want to get a flattened version of the reshaped array (the flattened
# version is equivalent to arr), as well as a transposed version. For the
# transposed version of reshaped, we use a permutation of (1, 2, 0).

# Set flattened equal to reshaped.flatten().

# Then set transposed equal to np.transpose with reshaped as the first argument
# and the specified permutation for the axes keyword argument.

flattened = reshaped.flatten()
transposed = np.transpose(reshaped, (1, 2, 0))

# We'll create an array of 5 elements, all of which are 0. We'll also create
# an array with the same shape as transposed, but containing only 1 as the
# elements.

# Set zeros_arr equal to np.zeros with 5 as the lone argument.

# Then set ones_arr equal to np.ones_like with transposed as the lone argument.

zeros_arr = np.zeros(5)
ones_arr = np.ones_like(transposed)

# The final array will contain 101 evenly spaced numbers between -3.5 and 1.5,
# inclusive. Since they are evenly spaced, the difference between adjacent
# numbers is 0.05.

# Set points equal to np.linspace with -3.5 and 1.5 as the first two arguments,
# respectively, as well as 101 for the num keyword argument.

points = np.linspace(-3.5, 1.5, num=101)
