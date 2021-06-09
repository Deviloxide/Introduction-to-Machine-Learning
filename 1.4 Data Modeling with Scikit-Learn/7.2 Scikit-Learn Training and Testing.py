import numpy as np

from sklearn.model_selection import train_test_split

# The coding exercise for this chapter will be to finish a utility function
# called dataset_splitter, which will be used in future chapters.

# The function will split the input dataset into training and testing sets,
# and then group the data and labels based on type of set.

# Set split_dataset equal to train_test_split applied with data and labels
# as required arguments, as well as test_size for the test_size keyword
# argument.

# Set train_set equal to a tuple containing the first and third elements
# of split_dataset. Also set test_set equal to a tuple containing the
# second and fourth elements of split_dataset.

# Return a tuple containing train_set and test_set, in that order.

def dataset_splitter(data, labels, test_size=0.25):
    split_dataset = train_test_split(data, labels, test_size=test_size)
    train_set = (split_dataset[0], split_dataset[2])
    test_set = (split_dataset[1], split_dataset[3])
    return (train_set, test_set)
    pass

