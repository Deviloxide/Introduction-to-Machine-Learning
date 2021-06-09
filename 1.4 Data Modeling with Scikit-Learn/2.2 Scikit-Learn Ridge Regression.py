import numpy as np

from sklearn import linear_model

# The coding exercise in this chapter uses the RidgeCV object of the
# linear_model module (imported in backend) to complete the cv_ridge_reg
# function.

# The function will fit a ridge regression model to the input data and
# labels. The model is cross-validated to choose the best α value from the
# input list alphas.

# Set reg equal to linear_model.RidgeCV initialized with the input list,
# alphas, for the alphas keyword argument.

# Call reg.fit with data and labels as the two input arguments. Then return
# reg.

def cv_ridge_reg(data, labels, alphas):
    reg = linear_model.RidgeCV(alphas=alphas)
    reg.fit(data, labels)
    return reg
    pass

