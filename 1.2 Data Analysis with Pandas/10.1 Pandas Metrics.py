import numpy as np

import pandas as pd

# When working with numeric features, we usually want to calculate metrics
# such as mean, standard deviation, etc. These metrics give us more insight
# into the type of data we're working with, which benefits our overall
# analysis of the dataset.

# Rather than calculating several different metrics separately, pandas
# provides the describe function to obtain a summary of a DataFrame's
# numeric data.

# The metrics included in the output summary of describe are

# count - The number of rows in the DataFrame
# mean - The mean value for a feature
# std -	The standard deviation for a feature
# min -	The minimum value in a feature
# 25% -	The 25th percentile of a feature
# 50% - The 50th percentile of a feature. Note that this is identical to the median
# 75% - The 75th percentile of a feature
# max - The maximum value in a feature

# The code below shows how to use the describe function.

# df is predefined
print('{}\n'.format(df))

metrics1 = df.describe()
print('{}\n'.format(metrics1))

hr_rbi = df[['HR','RBI']]
metrics2 = hr_rbi.describe()
print('{}\n'.format(metrics2))

# Using describe with a DataFrame will return a summary of metrics for each
# of the DataFrame's numeric features. In our example, df had three features
# with numerical values: yearID, HR, and RBI.

# Since we normally treat yearID as a categorical feature, the second time we
# used describe was with the hr_rbi DataFrame, which only included the HR and
# RBI features.

# To have describe return specific percentiles, we can use the percentiles
# keyword argument. The percentiles argument takes in a list of decimal
# percentages, representing the percentiles we want returned in the summary.

metrics1 = hr_rbi.describe(percentiles=[.5])
print('{}\n'.format(metrics1))

metrics2 = hr_rbi.describe(percentiles=[.1])
print('{}\n'.format(metrics2))

metrics3 = hr_rbi.describe(percentiles=[.2,.8])
print('{}\n'.format(metrics3))

# Note that the 50th percentile, i.e. the median, is always returned. The
# values specified in the percentiles list will replace the default 25th and
# 75th percentiles.

print("\n")
# Categorical Features
print("Categorical Features")

# With categorical features, we don't calculate metrics like mean, standard
# deviation, etc. Instead, we use frequency counts to describe a categorical
# feature.

# The frequency count for a specific category of a feature refers to how many
# times that category appears in the dataset. In pandas, we use the value
# _counts function to obtain the frequency counts for each category in a
# column feature.

# The code below uses the value_counts function to get frequency counts of
# the 'playerID' feature.

p_ids = df['playerID']
print('{}\n'.format(p_ids.value_counts()))

print('{}\n'.format(p_ids.value_counts(normalize=True)))

print('{}\n'.format(p_ids.value_counts(ascending=True)))

# Using value_counts without any keyword arguments will return the frequency
# counts for each category, sorted in descending order.

# Setting normalize=True returns the frequency proportions, rather than
# counts, for each category (note that the sum of all the proportions is 1).
# We can also set ascending=True to get the frequencies sorted in ascending
# order.

# If we just want the names of each unique category in a column, rather than
# the frequencies, we use the unique function.

unique_players = df['playerID'].unique()
print('{}\n'.format(repr(unique_players)))

unique_teams = df['teamID'].unique()
print('{}\n'.format(repr(unique_teams)))

#  So far we've focused on categorical features with string values. However,
#  categorical features can also have integer values. For example, we can
#  use yearID as a categorical feature with each unique year as a separate
#  category.

y_ids = df['yearID']
print('{}\n'.format(y_ids))

print('{}\n'.format(repr(y_ids.unique())))
print('{}\n'.format(y_ids.value_counts()))
