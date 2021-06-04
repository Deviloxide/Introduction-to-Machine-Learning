import numpy as np

data = np.array([[1.2, 2.3],
                 [2.1, 4.2],
                 [-1.9, 3.1],
                 [-2.5, 2.5],
                 [0.8, 3.],
                 [6.3, 2.1],
                 [-1.5, 2.7],
                 [1.4, 2.9],
                 [1.8, 3.2]])

# Data Outliers
print("Data Outliers")

# An important aspect of data that we have to deal with is outliers. In
# general terms, an outlier is a data point that is significantly further
# away from the other data points. For example, if we had watermelons of
# weights 5, 4, 6, 7, and 20 pounds, the 20 pound watermelon is an outlier.

# The data scaling methods from the previous two chapters are both affected
# by outliers. Data standardization uses each feature's mean and standard
# deviation, while ranged scaling uses the maximum and minimum feature
# values, meaning that they're both susceptible to being skewed by outlier
# values.

# We can robustly scale the data, i.e. avoid being affected by outliers,
# by using use the data's median and Interquartile Range (IQR). Since the
# median and IQR are percentile measurements of the data
# (50% for median, 25% to 75% for the IQR), they are not affected by
# outliers. For the scaling method, we just subtract the median from each
# data value then scale to the IQR.

print("\n")
# Robust Scaling with Scikit-Learn
print("Robust Scaling with Scikit-Learn")

# In scikit-learn, we perform robust scaling with the RobustScaler module.
# It is another transformer object, with the same fit, transform, and
# fit_transform functions described in the previous chapter.

# The code below shows how to use the RobustScaler.

print('{}\n'.format(repr(data)))

from sklearn.preprocessing import RobustScaler

robust_scaler = RobustScaler()
transformed = robust_scaler.fit_transform(data)
print('{}\n'.format(repr(transformed)))
