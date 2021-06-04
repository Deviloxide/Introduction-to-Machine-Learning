import numpy as np

import pandas as pd

df = pd.DataFrame({'HR': [15, 7, 33, 43, 39, 29],
                   'playerID': ["pedrodu01", "pedrodu01", "troutmi01", "cruzne02", "cruzne02", "troutmi01"],
                   'teamID': ["BOS", "BOS", "LAA", "SEA", "SEA", "LAA"],
                   'yearID': [2016, 2017, 2017, 2016, 2017, 2016]},
                  index=['0', '1', '2', '3', '4', '5'])

# The code exercises in this chapter involve sorting a DataFrame of yearly MLB
# player stats, yearly_stats_df.

# We'll sort yearly_stats_df using two different methods. The first method
# sorts by 'yearID' in ascending order.

# Set by_year equal to yearly_stats_df.sort_values with 'yearID' as the only
# argument.

by_year = yearly_stats_df.sort_values('yearID')

# The next sorting method will sort by 'HR' in descending order.

# Set best_hr equal to yearly_stats_df.sort_values with 'HR' as the first
# argument and the ascending keyword argument set to False.

best_hr = yearly_stats_df.sort_values('HR', ascending=False)

# The final sorting method will again sort yearly_stats_df by 'HR' in
# descending order, but this time we break ties with 'SO' in ascending order.

# Set best_hr_so equal to yearly_stats_df.sort_values with a list of the
# specified column labels, in the order provided. The ascending keyword
# argument should be set to [False, True].

best_hr_so = yearly_stats_df.sort_values(['HR', 'SO'], ascending=[False, True])
