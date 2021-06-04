

# The code exercise for this chapter will be to convert a DataFrame of
# MLB statistics (df) into a NumPy matrix.

# We only want the data in df to be from the current century, so we need to
# first apply a filter.

# Filter df for rows where 'yearID' is at least 2000, then reset df equal
# to the filtered output.

df = df[df['yearID'] >= 2000]

# We also don't want any of the NaN values in our data. We can filter those
# out using the special dropna function.

# Set df equal to df.dropna applied with no arguments.

df = df.dropna()

# Finally, we want to convert each categorical feature into a set of
# indicator features for each of its categories.

# Then we can convert df into a NumPy matrix.

# Set df equal to pd.get_dummies with df as the only argument.

# Set matrix equal to df.values.

df = pd.get_dummies(df)
matrix = df.values
