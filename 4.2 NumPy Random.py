import numpy as np

# Note: it is important you do all the instructions in the order listed. We test
# your code by setting a fixed np.random.seed, so in order for your code to
# match the reference output, all the functions must be run in the correct
# order.

# We'll start off by obtaining some random integers. The first integer we get
# will be randomly chosen from the range [0, 5). The remaining integers will
# be part of a 3x5 NumPy array, each randomly chosen from the range [3, 10).

# Set random1 equal to np.random.randint with 5 as the only argument.

# Then set random_arr equal to np.random.randint with 3 as the first argument,
# 10 as the high keyword argument, and (3, 5) as the size keyword argument.

random1 = np.random.randint(5)
random_arr = np.random.randint(3, high=10, size=(3, 5))

# The next two arrays will be drawn randomly from distributions. The first will
# contain 5 numbers drawn uniformly from the range [-2.5, 1.5].

# Set random_uniform equal to np.random.uniform with the low and high keyword
# arguments set to -2.5 and 1.5, respectively. The size keyword argument
# should be set to 5.

random_uniform = np.random.uniform(low=-2.5, high=1.5, size=5)

# The second array will contain 50 numbers drawn from a normal distribution
# with mean 2.0 and standard deviation 3.5.

# Set random_norm equal to np.random.normal with the loc and scale keyword
# arguments set to 2.0 and 3.5, respectively. The size keyword argument should
# be set to (10, 5).

random_norm = np.random.normal(loc=2, scale=3.5, size=(10, 5))

# We'll now create our own distribution of strings and randomly select from it.
# The values for our distribution will be 'a', 'b', 'c', 'd'.

# To choose a value, we'll use a probability distribution of
# [0.5, 0.1, 0.2, 0.2], i.e. 'a' will have probability 0.5 of being chosen,
# 'b' will have a probability of 0.1, etc.

# Set choices equal to a list of the specified values, in the order given.

# Set choice equal to np.random.choice with choices as the first argument and
# the specified probability distribution as the p keyword argument.

choices = ['a', 'b', 'c', 'd']
choice = np.random.choice(choices, p=[0.5, 0.1, 0.2, 0.2])

# The last random operation we perform will be an in-place shuffle of a NumPy
# array.

# Set arr equal to a NumPy array containing the integers from 1 to 5, inclusive.

# Then apply np.random.shuffle to arr.

arr = np.arange(1, 6)
np.random.shuffle(arr)
