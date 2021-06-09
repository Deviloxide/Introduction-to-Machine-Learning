import numpy as np

from sklearn import linear_model


# The coding exercise in this chapter uses the LinearRegression object of
# the linear_model module (imported in backend) to complete the linear_reg function.

# The function will fit a basic least squares regression model to the input
# data and labels.

# Set reg equal to linear_model.LinearRegression initialized with no input
# arguments.

# Call reg.fit with data and labels as the two input arguments. Then return
# reg.

def linear_reg(data, labels):
    reg = linear_model.LinearRegression()
    reg.fit(data, labels)
    return reg
    pass

