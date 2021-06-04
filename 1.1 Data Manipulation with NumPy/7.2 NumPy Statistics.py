import numpy as np

arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])

# Each coding exercise in this chapter will be to complete a small function that takes
# in a 2-D NumPy matrix (data) as input. The first function to complete is get_min_max,
# which returns the overall minimum and maximum element in data.

# Set overall_min equal to data.min applied with no arguments.

# Set overall_max equal to data.max applied with no arguments.

# Return a tuple of overall_min and overall_max, in that order.

def get_min_max(data):
    overall_min = data.min()
    overall_max = data.max()
    return (overall_min, overall_max)
    pass


print(get_min_max(arr))

# Next, we'll complete col_min, which returns the minimums across each column of data.

# Set min0 equal to data.min with the axis keyword argument set to 0.

# Then return min0.

def col_min(data):
    min0 = data.min(axis=0)
    return min0
    pass


print(col_min(arr))

# The final function to complete is basic_stats, which returns the mean, median, and
# variance of data.

# Set mean equal to np.mean applied to data.

# Set median equal to np.median applied to data.

# Set var equal to np.var applied to data.

# Return a tuple containing mean, median, and var, in that order.

def basic_stats(data):
    mean = np.mean(data)
    median = np.median(data)
    var = np.var(data)
    return (mean, median, var)
    pass


print(basic_stats(arr))
