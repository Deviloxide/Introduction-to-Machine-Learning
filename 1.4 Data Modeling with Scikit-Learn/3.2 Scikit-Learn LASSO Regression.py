from sklearn import linear_model


# The coding exercise in this chapter uses the Lasso object of the
# linear_model module (imported in backend) to complete the lasso_reg
# function.

# The function will fit a LASSO regression model to the input data and
# labels. The α hyperparameter for the model is provided to the function
# via the alpha input argument.

# Set reg equal to linear_model.Lasso initialized with alpha for the alpha
# keyword argument.

# Call reg.fit with data and labels as the two input arguments. Then return
# reg.

def lasso_reg(data, labels, alpha):
    reg = linear_model.Lasso(alpha=alpha)
    reg.fit(data, labels)
    return reg
    pass
