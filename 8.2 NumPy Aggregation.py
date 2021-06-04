import numpy as np

arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])

arr2 = np.array([[54, 1, 3],
                 [43, 1, 7],
                 [90, 8, 0]])


# Each coding exercise in this chapter will be to complete a small function that takes
# in 2-D NumPy matrices as input. The first function to complete is get_sums, which
# returns the overall sum and column sums of data.

# Set total_sum equal to np.sum applied to data.

# Set col_sum equal to np.sum applied to data, with axis set to 0.

# Return a tuple of total_sum and col_sum, in that order.

def get_sums(data):
    total_sum = np.sum(data)
    col_sum = np.sum(data, axis=0)
    return total_sum, col_sum
    pass


print(get_sums(arr))


# The next function to complete is get_cumsum, which returns the cumulative sums for
# each row of data.

# Set row_cumsum equal to np.cumsum applied to data with axis set to 1.

# Then return row_cumsum.

def get_cumsum(data):
    row_cumsum = np.cumsum(data, axis=1)
    return row_cumsum
    pass


print(get_sums(arr))


# The final function, concat_arrays, takes in two 2-D NumPy arrays as input. It
# returns the column-wise and row-wise concatenations of the input arrays.

# Set col_concat equal to np.concatenate applied to a list of data1, data2, in that
# order.

# Set row_concat equal to np.concatenate applied to a list of data1, data2, in that
# order. The axis keyword argument should be set to 1.

# Return a tuple containing col_concat and row_concat, in that order.

def concat_arrays(data1, data2):
    col_concat = np.concatenate([data1, data2])
    row_concat = np.concatenate([data1, data2], axis=1)
    return (col_concat, row_concat)
    pass


print(concat_arrays(arr, arr2))
