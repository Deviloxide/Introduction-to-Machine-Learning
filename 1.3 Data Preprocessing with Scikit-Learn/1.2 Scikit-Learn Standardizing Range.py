import numpy as np

import sklearn

# The coding exercise in this chapter is to complete a generic data
# standardization function, standardize_data.

# This function will standardize the input NumPy array, data, by using the
# scale function (imported in the backend).

# Set scaled_data equal to scale applied with data as the only argument.
# Then return scaled_data.

def standardize_data(data):
  scaled_data = scale(data)
  return scaled_data
  pass

print(standardize_data(pizza_data))
