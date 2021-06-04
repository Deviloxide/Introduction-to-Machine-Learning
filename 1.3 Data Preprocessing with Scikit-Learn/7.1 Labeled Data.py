from sklearn.datasets import load_breast_cancer

# Class Labels
print("Class Labels:")

# A big part of data science is classifying observations in a dataset into
# separate categories, or classes. A popular use case of data classification
# is in separating a dataset into "good" and "bad" categories. For example,
# we can classify a dataset of breast tumors as either malignant or benign.

# The code below separates a breast cancer dataset into malignant and
# benign categories. The load_breast_cancer function is part of the
# scikit-learn library, and its data comes from the Breast Cancer Wisconsin
# dataset.

bc = load_breast_cancer()
print('{}\n'.format(repr(bc.data)))
print('Data shape: {}\n'.format(bc.data.shape))

# Class labels
print('{}\n'.format(repr(bc.target)))
print('Labels shape: {}\n'.format(bc.target.shape))

# Label names
print('{}\n'.format(list(bc.target_names)))

malignant = bc.data[bc.target == 0]
print('Malignant shape: {}\n'.format(malignant.shape))

benign = bc.data[bc.target == 1]
print('Benign shape: {}\n'.format(benign.shape))

# In the example above, the bc.data array contains all the dataset values,
# while the bc.target array contains the class ID labels for each row in
# bc.data. A class ID of 0 corresponds to a malignant tumor, while a class
# ID of 1 corresponds to a benign tumor.

# Using the bc.target class IDs, we separated the dataset into malignant
# and benign data arrays. In other words, the malignant array contains
# the rows of bc.data corresponding to the indexes in bc.target containing
# 0, while the benign array contains the rows of bc.data corresponding to
# the indexes in bc.target containing 1. There are 212 malignant data
# observations and 357 benign observations.
