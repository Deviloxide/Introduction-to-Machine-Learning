import numpy as np

from sklearn.preprocessing import RobustScaler

data = np.array([[1.2, 2.3],
                 [2.1, 4.2],
                 [-1.9, 3.1],
                [-2.5, 2.5],
                 [0.8, 3.],
                 [6.3, 2.1],
                 [-1.5, 2.7],
                 [1.4, 2.9],
                 [1.8, 3.2]])

# The coding exercise in this chapter uses RobustScaler (imported in
# backend) to complete the robust_scaling function.

# The function will apply outlier-independent scaling to the input NumPy
# array, data.

# Set robust_scaler equal to RobustScaler initialized without any
# parameters.

# Set scaled_data equal to robust_scaler.fit_transform applied with data
# as the only argument. Then return scaled_data.

def robust_scaling(data):
  robust_scaler = RobustScaler()
  scaled_data = robust_scaler.fit_transform(data)
  return scaled_data
  pass
