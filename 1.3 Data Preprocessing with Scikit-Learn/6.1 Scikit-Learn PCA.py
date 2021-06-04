import numpy as np

from sklearn.impute import SimpleImputer

data = np.array([[ 1.5,  3. ,  9. , -0.5,  1. ],
       [ 2.2,  4.3,  3.5,  0.6,  2.7],
       [ 3. ,  6.1,  1.1,  1.2,  4.2],
       [ 8. , 16. ,  7.7, -1. ,  7.1]])

data = np.array([[ 1.,  2., np.nan,  2.],
       [ 5., np.nan,  1.,  2.],
       [ 4., np.nan,  3., np.nan],
       [ 5.,  6.,  8.,  1.],
       [np.nan,  7., np.nan,  0.]])

# Dimensionality Reduction
print("Dimensionality Reduction:")

# Most datasets contain a large number of features, some of which are
# redundant or not informative. For example, in a dataset of basketball
# statistics, the total points and points per game for a player will
# (most of the time) tell the same story about the player's scoring
# prowess.

# When a dataset contains these types of correlated numeric features, we
# can perform principal component analysis (PCA) for dimensionality
# reduction (i.e. reducing the number of columns in the data array).

# PCA extracts the principal components of the dataset, which are an
# uncorrelated set of latent variables that encompass most of the
# information from the original dataset. Using a smaller set of principal
# components can make it a lot easier to use the dataset in statistical
# or machine learning models (especially when the original dataset contains many correlated features).

print("\n")
# Dimensionality Reduction
print("Dimensionality Reduction:")

# Like every other data transformation, we can apply PCA to a dataset in
# scikit-learn with a transformer, in this case the PCA module. When
# initializing the PCA module, we can use the n_components keyword to
# specify the number of principal components. The default setting is to
# extract m - 1 principal components, where m is the number of features
# in the dataset.

# The code below shows examples of applying PCA with various numbers of
# principal components.

print('{}\n'.format(repr(data)))

from sklearn.decomposition import PCA
pca_obj = PCA() # The value of n_component will be 4. As m is 5 and default is always m-1
pc = pca_obj.fit_transform(data).round(3)
print('{}\n'.format(repr(pc)))

pca_obj = PCA(n_components=3)
pc = pca_obj.fit_transform(data).round(3)
print('{}\n'.format(repr(pc)))

pca_obj = PCA(n_components=2)
pc = pca_obj.fit_transform(data).round(3)
print('{}\n'.format(repr(pc)))

# In the code output above, notice that when PCA is applied with 4
# principal components, the final column (last principal component) is
# all 0's. This means that there are actually only a maximum of three
# uncorrelated principal components that can be extracted.
