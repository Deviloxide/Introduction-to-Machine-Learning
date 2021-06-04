import pandas as pd

# The coding exercises in this chapter reading from CSV files containing
# baseball data, manipulating the data, then writing the resulting data
# into a new CSV file.

# First, we'll read from the two CSV files 'stats.csv' and 'salary.csv'. These
# files contain the stats and salaries, respectively, of various baseball
# players.

# Set stats_df equal to pd.read_csv applied to 'stats.csv'.

# Set salary_df equal to pd.read_csv applied to 'salary.csv'.

stats_df = pd.read_csv('stats.csv')
salary_df = pd.read_csv('salary.csv')

# Rather than having two separate DataFrames, we want a single DataFrame
# that contains the yearly stats and salaries for each player. Therefore,
# we can just merge the stats_df and salary_df DataFrames.

# Set df equal to pd.merge with stats_df and salary_df as the first two
# arguments, in that order.

df = pd.merge(stats_df, salary_df)

# Finally, we write the merged DataFrame into the file named 'out.csv'. Since
# the original CSV files didn't label the rows, we'll make sure not to label
# the rows of 'out.csv'.

# Call df.to_csv with 'out.csv' as the first argument and False for the index
# keyword argument.

df.to_csv('out.csv', index=False)
