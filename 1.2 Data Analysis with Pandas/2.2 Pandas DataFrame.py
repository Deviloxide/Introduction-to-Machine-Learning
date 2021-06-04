import numpy as np

import pandas as pd

# The coding exercise for this chapter involves creating various pandas
# DataFrame objects.

# We'll first create a DataFrame from a Python dictionary. The dictionary
# will have key-value pairs 'c1':[0, 1, 2, 3] and 'c2':[5, 6, 7, 8], in that
# order.

# The index for the DataFrame will come from the list of row labels
# ['r1', 'r2', 'r3', 'r4'].

# Set df equal to pd.DataFrame with the specified dictionary as the first
# argument and the list of row labels as the index keyword argument.

df = pd.DataFrame({'c1':[0, 1, 2, 3], 'c2':[5, 6, 7, 8]},
                  index=['r1', 'r2', 'r3', 'r4'])
print(df)

# We'll create another DataFrame, this one representing a single row. Rather
# than a dictionary for the first argument, we use a list of lists, and
# manually set the column labels to ['c1, 'c2'].

# Since there is only one row, the row labels will be ['r5'].

# Set row_df equal to pd.DataFrame with [[9, 9]] as the first argument, and
# the specified column and row labels for the columns and index keyword
# arguments.

row_df = pd.DataFrame([[9, 9]], columns=['c1', 'c2'], index=['r5'])
print(row_df)

# After creating row_df, we append it to the end of df and drop row 'r2'.

# Set df_app equal to df.append with row_df as the only argument.

# Then set df_drop equal to df_app.drop with 'r2' as the labels keyword
# argument.

df_app = df.append(row_df)

df_drop = df_app.drop(labels='r2')

print(df_app)
print(df_drop)