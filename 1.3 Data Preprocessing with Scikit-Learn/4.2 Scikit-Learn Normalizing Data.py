import numpy as np

from sklearn.preprocessing import Normalizer

data = np.array([[4, 1, 2, 2],
       [3, 4, 0, 0],
       [7, 5, 9, 2]])

# The coding exercise in this chapter uses Normalizer (imported in backend)
# to complete the normalize_data function.

# The function will apply L2 normalization to the input NumPy array, data.

# Set normalizer equal to Normalizer initialized without any parameters.

# Set norm_data equal to normalizer.fit_transform applied with data as the
# only argument. Then return norm_data.

def normalize_data(data):
    normalizer = Normalizer()
    norm_data = normalizer.fit_transform(data)
    return norm_data
    pass

print(normalize_data(data))
