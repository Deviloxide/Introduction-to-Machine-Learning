import numpy as np

# Each coding exercise in this chapter will be to complete a small function
# that takes in a 2-D NumPy matrix (data) as input. The first function to
# complete is direct_index.

# Set elem equal to the third element of the second row in data (remember that
# the first row is index 0). Then return elem.

# Sample array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


def direct_index(data):
    elem = data[1:2, 2:3]
    return elem
    pass


print(direct_index(arr))


# The next function, slice_data, will return two slices from the input data.

# The first slice will contain all the rows, but will skip the first element
# in each row. The second slice will contain all the elements of the first
# three rows except the last two elements.

# Set slice1 equal to the specified first slice. Remember that NumPy uses a
# comma to separate slices along different dimensions.

# Set slice2 equal to the specified second slice.

# Return a tuple containing slice1 and slice2, in that order.

def slice_data(data):
    slice1 = data[:, 1:]
    slice2 = data[0:3, 0:-2]
    return slice1, slice2
    pass


print(slice_data(arr))


# The next function, argmin_data, will find minimum indexes in the input data.

# We can use np.argmin to find minimum points in the data array. First, we'll
# find the index of the overall minimum element.

# We can also return the indexes of each row's minimum element. This is
# equivalent to finding the minimum column for each row, which means our
# operation is done along axis 1.

# Set argmin_all equal to np.argmin with data as the only argument.

# Set argmin1 equal to np.argmin with data as the first argument and the
# specified axis keyword argument.

# Return a tuple containing argmin_all and argmin1, in that order.

def argmin_data(data):
    argmin_all = np.argmin(data)
    argmin1 = np.argmin(data, axis=1)
    return argmin_all, argmin1
    pass

print(argmin_data(arr))


# The final function, argmax_data, will find the index of each row's maximum
# element in data. Since there are only 2 dimensions in data, we can
# the operation along either axis 1 or -1.

# Set argmax_neg1 equal to np.argmax with data as the first argument and -1 as
# the axis keyword argument. Then return argmax_neg1.

def argmax_data(data):
    argmax_neg1 = np.argmax(data, axis=-1)
    return argmax_neg1
    pass


print(argmax_data(arr))
