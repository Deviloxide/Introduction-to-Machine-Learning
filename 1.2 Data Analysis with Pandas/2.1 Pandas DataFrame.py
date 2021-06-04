import pandas as pd

# One of the main purposes of pandas is to deal with tabular data, i.e. data
# that comes from tables or spreadsheets. Since tabular data contains rows
# and columns, it is 2-D. For working with 2-D data, we use the
# pandas.DataFrame object, which we'll refer to simply as a DataFrame.

# A DataFrame is created through the pd.DataFrame constructor, which takes
# in essentially the same arguments as pd.Series. However, while a Series
# could be constructed from a scalar (representing a single value Series),
# a DataFrame cannot.

# Furthermore, pd.DataFrame takes in an additional columns keyword argument,
# which represents the labels for the columns (similar to how index
# represents the row labels).

# The code below shows how to use the pd.DataFrame constructor.

# 2D Data
print('2D Data:')
df = pd.DataFrame()
# Newline added to separate DataFrames
print('{}\n'.format(df))

df = pd.DataFrame([5, 6])
print('{}\n'.format(df))

df = pd.DataFrame([[5, 6]])
print('{}\n'.format(df))

df = pd.DataFrame([[5, 6], [1, 3]],
                  index=['r1', 'r2'],
                  columns=['c1', 'c2'])
print('{}\n'.format(df))

df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4]},
                  index=['r1', 'r2'])
print('{}\n'.format(df))

# When we initialize a DataFrame of mixed types, upcasting occurs on a
# per-column basis. The dtypes property returns the types in each column as
# a Series of types.

# The code below shows how upcasting works in DataFrames. You'll notice
# that upcasting only occurs in the first column for the DataFrame below,
# because the second column's values are both integers.

# Upcasting
print("\n")
print('Upcasting:')
upcast = pd.DataFrame([[5, 6], [1.2, 3]])
print('{}\n'.format(upcast))
# Datatypes of each column
print(upcast.dtypes)

# We can append additional rows to a given DataFrame through the append
# function. The required argument for the function is either a Series or
# DataFrame, representing the row(s) we append.

# Note that the append function returns the modified DataFrame but doesn't
# actually change the original. Furthermore, when we append a Series to the
# DataFrame, we either need to specify the name for the series or use the
# ignore_index keyword argument. Setting ignore_index=True will change the
# row labels to integer indexes.

# The code below shows example usages of the append function.

# We can append additional rows to a given DataFrame through the append
# function. The required argument for the function is either a Series or
# DataFrame, representing the row(s) we append.

# Note that the append function returns the modified DataFrame but doesn't
# actually change the original. Furthermore, when we append a Series to the
# DataFrame, we either need to specify the name for the series or use the
# ignore_index keyword argument. Setting ignore_index=True will change the
# row labels to integer indexes.

# The code below shows example usages of the append function.

# Appending Rows
print("\n")
print('Appending Rows:')
df = pd.DataFrame([[5, 6], [1.2, 3]])
ser = pd.Series([0, 0], name='r3')

df_app = df.append(ser)
print('{}\n'.format(df_app))

df_app = df.append(ser, ignore_index=True)
print('{}\n'.format(df_app))

df2 = pd.DataFrame([[0, 0], [9, 9]])
df_app = df.append(df2)
print('{}\n'.format(df_app))

#  We can drop rows or columns from a given DataFrame through the drop
#  function. There is no required argument, but the keyword arguments of
#  the function gives us two ways to drop rows/columns from a DataFrame.

# The first way is using the labels keyword argument to specify the labels
# of the rows/columns we want to drop. We use this alongside the axis
# keyword argument (which has default value of 0) to drop from the rows
# or columns axis.

# The second method is to directly use the index or columns keyword
# arguments to specify the labels of the rows or columns directly, without
# needing to use axis.

# The code below shows examples on how to use the drop function.

# Dropping Data
print("\n")
print('Dropping Data:')
df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]},
                  index=['r1', 'r2'])
# Drop row r1
df_drop = df.drop(labels='r1')
print('{}\n'.format(df_drop))

# Drop columns c1, c3
df_drop = df.drop(labels=['c1', 'c3'], axis=1)
print('{}\n'.format(df_drop))

df_drop = df.drop(index='r2')
print('{}\n'.format(df_drop))

df_drop = df.drop(columns='c2')
print('{}\n'.format(df_drop))

df.drop(index='r2', columns='c2')
print('{}\n'.format(df_drop))
