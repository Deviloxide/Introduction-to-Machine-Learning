# The code exercises for this chapter involves calculating various baseball
# statistics based on the values of other statistics. The mlb_df DataFrame
# is predefined, and contains all historic MLB hitting statistics.

# We also provide a col_list_sum function. This is a utility function to
# calculate the sum of multiple columns across a DataFrame.

def col_list_sum(df, col_list, weights=None):
    col_df = df[col_list]
    if weights is not None:
        col_df = col_df.multiply(weights)
    return col_df.sum(axis=1)


# The df argument is the input DataFrame, while the col_list argument is a
# list of column labels representing the columns we want to sum in df.

# The weights keyword argument represents the weight coefficients we use for
# a weighted column sum. Note that if weights is not None, it must have the
# same length as col_list.

# The mlb_df doesn't contain one of the key stats in baseball, batting
# average. Therefore, we'll calculate the batting average and add it as a
# column in mlb_df.

# To calculate the batting average, simply divide a player's hits ('H') by
# their number of at-bats ('AB').

# Set mlb_df['BA'] equal to mlb_df['H'] divided by mlb_df['AB'].

mlb_df['BA'] = mlb_df['H'] / mlb_df['AB']

# Though mlb_df contains columns for doubles, triples, and home runs
# (labeled '2B', '3B', 'HR'), it does not contain a column for singles.

# However, we can calculate singles by subtracting doubles, triples, and
# home runs from the total number of hits. We'll label the singles column
# as '1B'.

# Set other_hits equal to col_list_sum with mlb_df as the first argument.
# The second argument should be a list of the column labels for doubles,
# triples, and home runs.

# Set mlb_df['1B'] equal to mlb_df['H'] subtracted by other_hits.

other_hits = col_list_sum(mlb_df, ['2B', '3B', 'HR'])
mlb_df['1B'] = mlb_df['H'] - other_hits

# Now that mlb_df contains columns for all four types of hits, we can
# calculate slugging percentage (column label 'SLG'). The formula for
# slugging percentage is: SLG = (1B + 2 * 2B + 3 * 3B + 4 * HR)/AB

# Therefore, the numerator represents a weighted sum with column labels
# '1B', '2B', '3B', 'HR'.

# Set weighted_hits equal to col_list_sum with mlb_df as the first argument
# and a list of numerator column labels as the second argument. The weights
# keyword argument should be a list of integers from 1 to 4, inclusive.

weighted_hits = col_list_sum(mlb_df, ['1B', '2B', '3B', 'HR'], weights=[1, 2, 3, 4])

# We can now calculate the slugging percentage by dividing the weighted sum
# by the number of at-bats.

# Set mlb_df['SLG'] equal to weighted_hits divided by mlb_df['AB'].

mlb_df['SLG'] = weighted_hits / mlb_df['AB']
