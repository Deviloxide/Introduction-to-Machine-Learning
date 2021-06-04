import pandas as pd

print((lambda x: x + 1)(2))

df = pd.DataFrame({'yearID': ["2017", "2015", "2016", "2015", "2016", "2016", "2015", "2017", "2017"],
                   'teamID': ["CLE", "CLE", "BOS", "DET", "DET", "CLE", "BOS", "BOS", "DET"],
                   'H': [1449, 1395, 1598, 1515, 1476, 1435, 1495, 1461, 1435],
                   'R': [818, 669, 878, 689, 750, 777, 748, 785, 735]},
                  index=['0', '1', '2', '3', '4', '5', '6', '7', '8'])

print("\n")
# Grouping by Column
print("Grouping by Column:")

# When dealing with large amounts of data, it is usually a good idea to group
# the data by common categories. For example, we could group a large dataset
# of MLB player statistics by year, so we can deal with each year's data
# separately.

# With pandas DataFrames, we can perform dataset grouping with the groupby
# function. A common usage of the function is to group a DataFrame by values
# from a particular column, e.g. a column representing years.

# The code below shows how to use the groupby function, with the example of
# grouping MLB data by year.

print('{}\n'.format(df))

groups = df.groupby('yearID')
for name, group in groups:
    print('Year: {}'.format(name))
    print('{}\n'.format(group))

print('{}\n'.format(groups.get_group('2016')))
print('{}\n'.format(groups.sum()))
print('{}\n'.format(groups.mean()))

# The grouping code example produced three DataFrames for the years 2015,
# 2016, and 2017. The three DataFrame groups are contained in the groups
# variable, and we used its sum and mean functions to retrieve the total
# and average per-year statistics.

# In addition to aggregation functions like sum and mean, we can also filter
# the groups using filter. The filter function takes in another function
# as its required argument, which specifies how we want to filter the groups.
# The output of filter is the concatenation of all the groups that pass
# the filter.

# The code below shows how to use the filter function.

no2015 = groups.filter(lambda x: x.name > "2015")
print(no2015)

# In the above code example, the lambda function passed into filter returns
# True if the group (represented as x) represents a year greater than 2015.
# The output is the concatenation of the 2016 and 2017 groups.

print("\n")
# Multiple Columns
print("Multiple Columns:")

# DataFrame grouping is not just limited to a single column. Rather than
# passing a single column label into groupby, we can use a list of column
# labels to specify grouping by multiple columns.
#
# Grouping by multiple columns can be useful when multiple data features
# have many different values. For example, if our dataset consisted of MLB
# players, grouping by both team and year would give us an organized way to
# view a team's roster throughout the years.

player_df = pd.DataFrame({'yearID': ["2016", "2016", "2016", "2016", "2016", "2017", "2017", "2017", "2017", "2017"],
                          'playerID': ["altuvjo01", "bettsmo01", "bogaexa01", "correca01", "pedrodu01", "altuvjo01",
                                       "bettsmo01", "bogaexa01", "correca01", "pedrodu01"],
                          'teamID': ["HOU", "BOS", "BOS", "HOU", "BOS", "HOU", "BOS", "BOS", "HOU", "BOS"],
                          'H': [216, 214, 192, 158, 201, 204, 166, 156, 133, 119]},
                         index=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

groups = player_df.groupby(['yearID', 'teamID'])

for name, group in groups:
    print('Year, Team: {}'.format(name))
    print('{}\n'.format(group))

print(groups.sum())

# In the code above, we grouped the MLB data by both year and team, resulting
# in each group's name being a tuple of year and team. Using the sum
# function, we obtained the annual total hits for each team.
