import numpy as np

arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])

# Each coding exercise in this chapter will be to complete a small function that takes in a 2-D NumPy matrix
# (data) as input. The first function to complete is get_positives.

# Set a tuple of x_ind, y_ind equal to the output of np.where, applied with the condition data > 0.

# Then return data[x_ind, y_ind].

def get_positives(data):
    x_ind, y_ind = np.where(data > 0)
    return data[x_ind, y_ind]
    pass


print(get_positives(arr))


# Next, we'll complete the function replace_zeros. The function replaces each of the non-positive elements
# in data with 0. We first create an array of all 0's, with the same shape as data.

# Then we filter the data array and replace the non-positive elements with the corresponding element from
# zeros (which will be a 0).

# Set zeros equal to np.zeros_like with data as the lone argument.

# Set zero_replace equal to np.where with the condition of data > 0. The second argument will be data
# the third argument will be zeros.

# Return zero_replace.

def replace_zeros(data):
    zeros = np.zeros_like(data)
    zero_replace = np.where(data > 0, data, zeros)
    return zero_replace
    pass


print(replace_zeros(arr))


# The next function, replace_neg_one, will replace the non-positive elements of data with -1. Rather than
# creating a separate array, we'll use broadcasting.

# Set neg_one_replace equal to np.where with the condition of data > 0. The second argument will be data
# and the third will be -1.

# Return neg_one_replace.

def replace_neg_one(data):
    neg_one_replace = np.where(data > 0, data, -1)
    return neg_one_replace
    pass


print(replace_neg_one(arr))


# Our final function, coin_flip_filter will apply a filter using a boolean array as the condition. We'll
# first create a boolean coin flip array with the same shape as data.

# Then we filter data using bool_coin_flips as the condition. For the False values in bool_coin_flips, we
# replace the corresponding index in data with a 1.

# Set coin_flips equal to np.random.randint with 2 as the first argument and data.shape as the size keyword
# argument.

# Set bool_coin_flips equal to coin_flips, cast as np.bool (using the np.astype function).

# Set one_replace equal to np.where with bool_coin_flips, data, and 1 as the respective arguments.

# Return one_replace.

def coin_flip_filter(data):
    coin_flips = np.random.randint(2, size=data.shape)
    bool_coin_flips = coin_flips.astype(np.bool)
    one_replace = np.where(bool_coin_flips, data, 1)
    return one_replace
    pass


print(coin_flip_filter(arr))
