import numpy as np

from sklearn.impute import SimpleImputer

# The coding exercise in this chapter uses PCA (imported in backend) to
# complete the pca_data function.

# The function will apply principal component analysis (PCA) to the input
# NumPy array, data.

# Set pca_obj equal to PCA initialized with n_components for the
# n_components keyword argument.

# Set component_data equal to pca_obj.fit_transform applied with data as
# the only argument. Then return component_data.

def pca_data(data, n_components):
  pca_obj = PCA(n_components=n_components)
  component_data = pca_obj.fit_transform(data)
  return component_data
  pass
