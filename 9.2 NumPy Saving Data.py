import numpy as np

# The coding exercise in this chapter will require you to complete the save_points
# function, which will save some randomly generated 2-D points in a file.

# You'll generate 100 (x, y) points from a uniform distribution in the range
# [-2.5, 2.5), then save the points to save_file.

# Set points equal to np.random.uniform, with the low and high keyword arguments
# representing the lower and upper ends of the range. The size keyword argument
# should be set to (100, 2).

# Call np.save with save_file as the first argument and points as the second argument.

def save_points(save_file):
    points = np.random.uniform(low=-2.5, high=2.5, size=(100, 2))
    np.save(save_file, points)
    pass
