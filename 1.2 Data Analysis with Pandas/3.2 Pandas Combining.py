import pandas as pd


# The coding exercises for this chapter involve completing small functions
# that take in two DataFrame objects as input.

# The first function, concat_rows will concatenate the rows of the two
# DataFrames.

# Set row_concat equal to pd.concat with [df1, df2] as the only argument.
# Then return row_concat.

def concat_rows(df1, df2):
    row_concat = pd.concat([df1, df2])
    return row_concat
    pass


# The next function, concat_cols will concatenate the columns of the two
# input DataFrames.

# Set col_concat equal to pd.concat with [df1, df2] as the required argument.
# Also set the axis keyword argument to 1.

# Then return col_concat.

def concat_cols(df1, df2):
    col_concat = pd.concat([df1, df2], axis=1)
    return col_concat
    pass


# The final function, merge_dfs will merge the two input DataFrames along
# their columns.

# Set merged_df equal to pd.merge with df1 and df2 as the first and second
# arguments, respectively.

# Then return merged_df.

def merge_dfs(df1, df2):
    merged_df = pd.merge(df1, df2)
    return merged_df
    pass
