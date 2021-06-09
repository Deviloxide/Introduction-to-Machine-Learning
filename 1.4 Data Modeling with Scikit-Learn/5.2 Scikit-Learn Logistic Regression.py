import numpy as np

from sklearn import linear_model

# The coding exercise in this chapter uses the LogisticRegression object of
# the linear_model module (imported in backend) for multiclass
# classification.

# The function multiclass_lr will fit a logistic regression model to a
# dataset with multiclass labels.

# Set reg equal to linear_model.LogisticRegression with the solver and
# max_iter keyword arguments set as 'lbfgs' and max_iter, respectively. Also
# have the multi_class keyword argument set to 'multinomial'.

# Call reg.fit with data and labels as the two input arguments. Then return
# reg.

def multiclass_lr(data, labels, max_iter):
    reg = linear_model.LogisticRegression(solver="lbfgs", max_iter=max_iter, multi_class="multinomial")
    reg.fit(data, labels)
    return reg
    pass

