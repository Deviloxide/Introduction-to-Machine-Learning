import numpy as np

from sklearn import tree

from sklearn.model_selection import cross_val_score


# The coding exercise for this chapter is to complete the aforementioned
# cv_decision_tree function. The function's first argument defines whether
# the decision tree is for classification/regression, the next two arguments
# represent the data/labels, and the final two arguments represent the
# tree's maximum depth and number of folds, respectively.

# First, we'll create the decision tree (using the tree module imported in
# the backend).

# Initialize d_tree with tree.DecisionTreeClassifier if is_clf is True,
# otherwise use tree.DecisionTreeRegressor. In either case, initialize with
# keyword argument max_depth set to max_depth.

# Then we'll use the cross_val_score function (imported in the backend) to
# obtain the CV scores.

# Set scores equal to cross_val_score applied with d_tree, data, and labels
# for the first three arguments. Use cv=cv for the keyword argument, then
# return scores.

def cv_decision_tree(is_clf, data, labels, max_depth, cv):
    if is_clf:
        d_tree = tree.DecisionTreeClassifier(max_depth=max_depth)
    else:
        d_tree = tree.DecisionTreeRegressor(max_depth=max_depth)
    scores = cross_val_score(d_tree, data, labels, cv=cv)
    return scores
    pass

