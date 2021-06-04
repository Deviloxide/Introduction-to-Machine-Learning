import numpy as np

import pandas as pd

# The coding exercises for this chapter involve getting metrics from a
# DataFrame of MLB players, player_df.

# First, we'll get a summary of all the statistics in player_df.

# Set summary_all equal to player_df.describe with no arguments.

summary_all = player_df.describe()

# Next, we want to get summaries specifically for the home run totals. The
# first summary will contain the default metrics from describe, while the
# second summary will contain the 10th and 90th percentiles.

# Set hr_df equal to player_df[] directly indexed with 'HR'.

# Set summary_hr equal to hr_df.describe with no arguments.

# Set low_high_10 equal to hr_df.describe with [.1,.9] as the percentiles
# keyword argument.

hr_df = player_df['HR']
summary_hr = hr_df.describe()
low_high_10 = hr_df.describe(percentiles=[.1,.9])

# Finally, we'll treat the 'HR' feature as a categorical variable, with each
# unique home run total as a separate category. We then get the frequency
# counts for each category.

# Set hr_counts equal to hr_df.value_counts with no arguments.

hr_counts = hr_df.value_counts()
