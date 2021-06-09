import numpy as np

data = np.array([[5.1, 3.5, 1.4, 0.2],
                 [4.9, 3., 1.4, 0.2],
                 [4.7, 3.2, 1.3, 0.2],
                 [4.6, 3.1, 1.5, 0.2],
                 [5., 3.6, 1.4, 0.2],
                 [5.4, 3.9, 1.7, 0.4],
                 [4.6, 3.4, 1.4, 0.3],
                 [5., 3.4, 1.5, 0.2],
                 [4.4, 2.9, 1.4, 0.2],
                 [4.9, 3.1, 1.5, 0.1],
                 [5.4, 3.7, 1.5, 0.2],
                 [4.8, 3.4, 1.6, 0.2],
                 [4.8, 3., 1.4, 0.1],
                 [4.3, 3., 1.1, 0.1],
                 [5.8, 4., 1.2, 0.2],
                 [5.7, 4.4, 1.5, 0.4],
                 [5.4, 3.9, 1.3, 0.4],
                 [5.1, 3.5, 1.4, 0.3],
                 [5.7, 3.8, 1.7, 0.3],
                 [5.1, 3.8, 1.5, 0.3],
                 [5.4, 3.4, 1.7, 0.2],
                 [5.1, 3.7, 1.5, 0.4],
                 [4.6, 3.6, 1., 0.2],
                 [5.1, 3.3, 1.7, 0.5],
                 [4.8, 3.4, 1.9, 0.2],
                 [5., 3., 1.6, 0.2],
                 [5., 3.4, 1.6, 0.4],
                 [5.2, 3.5, 1.5, 0.2],
                 [5.2, 3.4, 1.4, 0.2],
                 [4.7, 3.2, 1.6, 0.2],
                 [4.8, 3.1, 1.6, 0.2],
                 [5.4, 3.4, 1.5, 0.4],
                 [5.2, 4.1, 1.5, 0.1],
                 [5.5, 4.2, 1.4, 0.2],
                 [4.9, 3.1, 1.5, 0.1],
                 [5., 3.2, 1.2, 0.2],
                 [5.5, 3.5, 1.3, 0.2],
                 [4.9, 3.1, 1.5, 0.1],
                 [4.4, 3., 1.3, 0.2],
                 [5.1, 3.4, 1.5, 0.2],
                 [5., 3.5, 1.3, 0.3],
                 [4.5, 2.3, 1.3, 0.3],
                 [4.4, 3.2, 1.3, 0.2],
                 [5., 3.5, 1.6, 0.6],
                 [5.1, 3.8, 1.9, 0.4],
                 [4.8, 3., 1.4, 0.3],
                 [5.1, 3.8, 1.6, 0.2],
                 [4.6, 3.2, 1.4, 0.2],
                 [5.3, 3.7, 1.5, 0.2],
                 [5., 3.3, 1.4, 0.2],
                 [7., 3.2, 4.7, 1.4],
                 [6.4, 3.2, 4.5, 1.5],
                 [6.9, 3.1, 4.9, 1.5],
                 [5.5, 2.3, 4., 1.3],
                 [6.5, 2.8, 4.6, 1.5],
                 [5.7, 2.8, 4.5, 1.3],
                 [6.3, 3.3, 4.7, 1.6],
                 [4.9, 2.4, 3.3, 1.],
                 [6.6, 2.9, 4.6, 1.3],
                 [5.2, 2.7, 3.9, 1.4],
                 [5., 2., 3.5, 1.],
                 [5.9, 3., 4.2, 1.5],
                 [6., 2.2, 4., 1.],
                 [6.1, 2.9, 4.7, 1.4],
                 [5.6, 2.9, 3.6, 1.3],
                 [6.7, 3.1, 4.4, 1.4],
                 [5.6, 3., 4.5, 1.5],
                 [5.8, 2.7, 4.1, 1.],
                 [6.2, 2.2, 4.5, 1.5],
                 [5.6, 2.5, 3.9, 1.1],
                 [5.9, 3.2, 4.8, 1.8],
                 [6.1, 2.8, 4., 1.3],
                 [6.3, 2.5, 4.9, 1.5],
                 [6.1, 2.8, 4.7, 1.2],
                 [6.4, 2.9, 4.3, 1.3],
                 [6.6, 3., 4.4, 1.4],
                 [6.8, 2.8, 4.8, 1.4],
                 [6.7, 3., 5., 1.7],
                 [6., 2.9, 4.5, 1.5],
                 [5.7, 2.6, 3.5, 1.],
                 [5.5, 2.4, 3.8, 1.1],
                 [5.5, 2.4, 3.7, 1.],
                 [5.8, 2.7, 3.9, 1.2],
                 [6., 2.7, 5.1, 1.6],
                 [5.4, 3., 4.5, 1.5],
                 [6., 3.4, 4.5, 1.6],
                 [6.7, 3.1, 4.7, 1.5],
                 [6.3, 2.3, 4.4, 1.3],
                 [5.6, 3., 4.1, 1.3],
                 [5.5, 2.5, 4., 1.3],
                 [5.5, 2.6, 4.4, 1.2],
                 [6.1, 3., 4.6, 1.4],
                 [5.8, 2.6, 4., 1.2],
                 [5., 2.3, 3.3, 1.],
                 [5.6, 2.7, 4.2, 1.3],
                 [5.7, 3., 4.2, 1.2],
                 [5.7, 2.9, 4.2, 1.3],
                 [6.2, 2.9, 4.3, 1.3],
                 [5.1, 2.5, 3., 1.1],
                 [5.7, 2.8, 4.1, 1.3],
                 [6.3, 3.3, 6., 2.5],
                 [5.8, 2.7, 5.1, 1.9],
                 [7.1, 3., 5.9, 2.1],
                 [6.3, 2.9, 5.6, 1.8],
                 [6.5, 3., 5.8, 2.2],
                 [7.6, 3., 6.6, 2.1],
                 [4.9, 2.5, 4.5, 1.7],
                 [7.3, 2.9, 6.3, 1.8],
                 [6.7, 2.5, 5.8, 1.8],
                 [7.2, 3.6, 6.1, 2.5],
                 [6.5, 3.2, 5.1, 2.],
                 [6.4, 2.7, 5.3, 1.9],
                 [6.8, 3., 5.5, 2.1],
                 [5.7, 2.5, 5., 2.],
                 [5.8, 2.8, 5.1, 2.4],
                 [6.4, 3.2, 5.3, 2.3],
                 [6.5, 3., 5.5, 1.8],
                 [7.7, 3.8, 6.7, 2.2],
                 [7.7, 2.6, 6.9, 2.3],
                 [6., 2.2, 5., 1.5],
                 [6.9, 3.2, 5.7, 2.3],
                 [5.6, 2.8, 4.9, 2.],
                 [7.7, 2.8, 6.7, 2.],
                 [6.3, 2.7, 4.9, 1.8],
                 [6.7, 3.3, 5.7, 2.1],
                 [7.2, 3.2, 6., 1.8],
                 [6.2, 2.8, 4.8, 1.8],
                 [6.1, 3., 4.9, 1.8],
                 [6.4, 2.8, 5.6, 2.1],
                 [7.2, 3., 5.8, 1.6],
                 [7.4, 2.8, 6.1, 1.9],
                 [7.9, 3.8, 6.4, 2.],
                 [6.4, 2.8, 5.6, 2.2],
                 [6.3, 2.8, 5.1, 1.5],
                 [6.1, 2.6, 5.6, 1.4],
                 [7.7, 3., 6.1, 2.3],
                 [6.3, 3.4, 5.6, 2.4],
                 [6.4, 3.1, 5.5, 1.8],
                 [6., 3., 4.8, 1.8],
                 [6.9, 3.1, 5.4, 2.1],
                 [6.7, 3.1, 5.6, 2.4],
                 [6.9, 3.1, 5.1, 2.3],
                 [5.8, 2.7, 5.1, 1.9],
                 [6.8, 3.2, 5.9, 2.3],
                 [6.7, 3.3, 5.7, 2.5],
                 [6.7, 3., 5.2, 2.3],
                 [6.3, 2.5, 5., 1.9],
                 [6.5, 3., 5.2, 2.],
                 [6.2, 3.4, 5.4, 2.3],
                 [5.9, 3., 5.1, 1.8]])

labels = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                   2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])


# Bayesian Techniques
print("Bayesian Techniques:")

# So far, we've discussed hyperparameter optimization through
# cross-validation. Another way to optimize the hyperparameters of a
# regularized regression model is with Bayesian techniques.

# In Bayesian statistics, the main idea is to make certain assumptions about
# the probability distributions of a model's parameters before being fitted
# on data. These initial distribution assumptions are called priors for the
# model's parameters.

# In a Bayesian ridge regression model, there are two hyperparameters to
# optimize: α and λ. The α hyperparameter serves the same exact purpose as
# it does for regular ridge regression; namely, it acts as a scaling factor
# for the penalty term.

# The λ hyperparameter acts as the precision of the model's weights.
# Basically, the smaller the λ value, the greater the variance between the
# individual weight values.

print("\n")
# Hyperparameter Priors
print("Hyperparameter Priors:")

# Both the α and λ hyperparameters have gamma distribution priors, meaning
# we assume both values come from a gamma probability distribution.

# There's no need to know the specifics of a gamma distribution, other than
# the fact that it's a probability distribution defined by a shape parameter
# and scale parameter.

# Specifically, the α hyperparameter has prior:

# Γ(α_1,α_2)

# and the λ hyperparameter has prior:

# Γ(λ_1,λ_2)

# where Γ(k,θ) represents a gamma distribution with shape parameter k and
# scale parameter θ.

print("\n")
# Tuning the Model
print("Tuning the Model:")

# When finding the optimal weight settings of a Bayesian ridge regression
# model for an input dataset, we also concurrently optimize the α and λ
# hyperparameters based on their prior distributions and the input data.

# This can all be done with the BayesianRidge object (part of the
# linear_model module). Like all the previous regression objects, this one
# can be initialized with no required arguments.

print('Data shape: {}\n'.format(data.shape))
print('Labels shape: {}\n'.format(labels.shape))

from sklearn import linear_model
reg = linear_model.BayesianRidge()
reg.fit(data, labels)
print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))
print('R2: {}\n'.format(reg.score(data, labels)))
print('Alpha: {}\n'.format(reg.alpha_))
print('Lambda: {}\n'.format(reg.lambda_))

# We can manually specify the α1 and α2 gamma parameters for α with the
# alpha_1 and alpha_2 keyword arguments when initializing BayesianRidge.
# Similarly, we can manually set λ1 and λ2 with the lambda_1 and lambda_2
# keyword arguments. The default value for each of the four gamma
# parameters is 10-6.
