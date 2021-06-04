import numpy as np

import pandas as pd

# The coding exercise for this chapter involves creating various pandas
# Series objects.

# The first Series we create will contain basic floating point numbers. The
# list we use to initialize the Series is [1, 3, 5.2].

# Set s1 equal to pd.Series with the specified list as the only argument.

s1 = pd.Series([1, 3, 5.2])
print(s1)

# The second Series we create comes from performing elemental multiplication
# on s1 using a separate list of floating point numbers.

# Set s2 equal to s1 multiplied by [0.1, 0.2, 0.3].

s2 = s1 * [0.1, 0.2, 0.3]
print(s2)

# We'll create another Series, this time with integers. The list we use to
# initialize this Series is [1, 3, 8, np.nan]. This Series will also have row
# labels, which will be ['a', 'b', 'c', 'd'].

# Set s3 equal to pd.Series with the specified list of integers as the first
# argument and the list of labels as the index keyword argument.

s3 = pd.Series([1, 3, 8, np.nan], index=['a', 'b', 'c', 'd'])
print(s3)

# The final Series we create will be initialized from a Python dictionary.
# The dictionary will have key-value pairs 'a':0, 'b':1, and 'c':2.
#
# Set s4 equal to pd.Series with a dictionary of the specified key-value
# pairs as the only argument.

s4 = pd.Series([0, 1, 2], index=['a', 'b', 'c'])
print(s4)
