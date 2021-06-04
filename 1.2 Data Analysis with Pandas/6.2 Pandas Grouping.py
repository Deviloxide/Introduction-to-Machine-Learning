import pandas as pd

df = pd.DataFrame({'yearID': ["2017", "2015", "2016", "2015", "2016", "2016", "2015", "2017", "2017"],
                   'teamID': ["CLE", "CLE", "BOS", "DET", "DET", "CLE", "BOS", "BOS", "DET"],
                   'H': [1449, 1395, 1598, 1515, 1476, 1435, 1495, 1461, 1435],
                   'R': [818, 669, 878, 689, 750, 777, 748, 785, 735]},
                  index=['0', '1', '2', '3', '4', '5', '6', '7', '8'])

# The coding exercises for this chapter involve performing grouping
# operations on df, which contains all MLB batting data from 1871-2017. Using
# df, our goal is to retrieve home run (HR) statistics for 2017.

# To do this, we need to calculate the total number of home runs hit each
# year. This involves first grouping df by year.

# Set year_group equal to df.groupby with 'yearID' as the lone argument.

year_group = df.groupby("yearID")
print(year_group)

# The yearly stats can be obtained from summing the values across the
# year-separated groups.

# Set year_stats equal to year_group.sum applied with no arguments.

year_stats = year_group.sum()
print(year_stats)

# The year_stats DataFrame represents the total value for each stat per
# year. The row labels are the years and the column labels are the stat
# categories, e.g. home runs. Using the loc property, we'll retrieve the
# home run total for 2017.

# Set hr_2017 equal to year_stats.loc with 2017 as the row index and 'HR'
# as the column index.

hr_2017 = year_stats.loc[2017, 'HR']
print(hr_2017)

# Next we want to get the yearly totals for each batting statistic per team.
# To do this, we group the data by both the year and team.
#
# Set year_team_group equal to df.groupby applied with the list
# ['yearID', 'teamID'].

year_team_group = df.groupby(['yearID', 'teamID'])
print(year_team_group)

# Once again, to obtain the yearly stats we just sum over all the groups.

# Set year_team_stats equal to year_team_group.sum applied with no arguments.

year_team_stats = year_team_group.sum()
print(year_stats)
