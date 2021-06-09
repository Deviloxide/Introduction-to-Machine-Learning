import numpy as np

from sklearn import linear_model

# The coding exercise in this chapter uses the BayesianRidge object of the
# linear_model module (imported in backend) to complete the bayes_ridge
# function.

# The function will fit a Bayesian ridge regression model to the input data
# and labels.

# Set reg equal to linear_model.BayesianRidge, initialized with no input
# arguments.

# Call reg.fit with data and labels as the two input arguments. Then return
# reg.

def bayes_ridge(data, labels):
    reg = linear_model.BayesianRidge()
    reg.fit(data, labels)
    return reg
    pass

