import pandas as pd

df = pd.DataFrame({'c1': [1, 18, 19, 20], 'c2': [-9, 0, 0, 5],
                   'c3': [1, 2, 7, -2]}, index=['r1', 'r2', 'r3', 'r4'])

# The coding exercises for this chapter involve directly indexing into a
# predefined DataFrame, df.

# We'll initially use direct indexing to get the first column of df as well
# as the first two rows.

# Set col_1 equal to df directly indexed with 'c1' as the key.

# Set row_12 equal to df directly indexed with 0:2 as the key.

col_1 = df['c1']
row_12 = df[0:2]

print(col_1)
print(row_12)

# Next, we'll use iloc to retrieve the first and third rows of df.

# Set row_13 equal to df.iloc indexed with [0, 2] as the key.

row_13 = df.iloc[[0, 2]]
print(row_13)

# Finally, we use loc to set each value of the second column, in the third
# and fourth rows, equal to 12. The row key we use for indexing will be
# ['r3','r4'], while the column key will be 'c2'.

# Set df.loc, indexed with the specified row and column keys, equal to 12.

df.loc[['r3', 'r4'], 'c2'] = 12

print(df)
