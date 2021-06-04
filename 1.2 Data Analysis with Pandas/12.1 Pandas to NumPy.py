import pandas as pd

indicator_df = pd.DataFrame({'blue': [0, 1, 0, 0, 0, 1],
                   'green': [0, 0, 1, 0, 0, 0],
                   'green': [1, 0, 0, 1, 1, 0]},
                   index=['r1', 'r2', 'r3', 'r4', 'r5', 'r6'])

# Machine Learning
print("Machine Learning")

# The DataFrame object is great for storing a dataset and performing data
# analysis in Python. However, most machine learning frameworks
# (e.g. TensorFlow), work directly with NumPy data. Furthermore, the NumPy
# data used as input to machine learning models must solely contain
# quantitative values.

# Therefore, to use a DataFrame's data with a machine learning model, we
# need to convert the DataFrame to a NumPy matrix of quantitative data.
# So even the categorical features of a DataFrame, such as gender and
# birthplace, must be converted to quantitative values.

print("\n")
# Indicator Features
print("Indicator Features")

# When converting a DataFrame to a NumPy matrix of quantitative data, we
# need to find a way to modify the categorical features in the DataFrame.

# The easiest way to do this is to convert each categorical feature into a
# set of indicator features for each of its categories. The indicator
# feature for a specific category represents whether or not a given data
# sample belongs to that category.

# The code below shows a DataFrame with indicator features.

print('{}\n'.format(indicator_df))

# In the code above, the DataFrame df has a single categorical feature
# called Color. The corresponding indicator features for Color are shown
# in indicator_df.

# Note that an indicator feature contains 1 when the row has that
# particular category, and 0 if the row does not.

print("\n")
# Converting to Indicators
print("Converting to Indicators")

# In pandas, we convert each categorical feature of a DataFrame to
# indicator features with the get_dummies function. The function takes in
# a DataFrame as its required argument, and returns the DataFrame with
# each of its categorical features converted to indicator features.

# The code below demonstrates how to use the get_dummies function.

converted = pd.get_dummies(df)
print('{}\n'.format(converted.columns))

print('{}\n'.format(converted[['teamID_BOS',
                               'teamID_PIT']]))
print('{}\n'.format(converted[['lgID_AL',
                               'lgID_NL']]))

# Note that the indicator features have the original categorical feature's
# label as a prefix. This makes it easy to see where each indicator
# feature originally came from.

print("\n")
# Converting to NumPy
print("Converting to NumPy")

# After converting all the categorical features to indicator features,
# the DataFrame should have all quantitative data. We can then convert
# to a NumPy matrix using the values function.

# The code below converts a DataFrame, df into a NumPy matrix.

n_matrix = df.values
print(repr(n_matrix))

# The rows and columns of the output matrix correspond to the rows and
# columns of the same position in the DataFrame. In the code above, the
# first column of the NumPy matrix represents HR, the second column
# represents teamID_BOS, and the third column represents teamID_PIT.
