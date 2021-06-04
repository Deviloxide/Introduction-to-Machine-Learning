import numpy as np

import pandas as pd

df = pd.DataFrame({'HR': [49, 73, 46, 45, 45, 5, 26, 28],
                   'yearID': ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007"]},
                  index=['0', '1', '2', '3', '4', '5', '6', '7'])

# Basics
print("Basics")

# The main function used for plotting DataFrames is plot. This function is
# used in tandem with the show function from the pyplot API, to produce plot
# visualizations. We import the pyplot API with the line:

import matplotlib.pyplot as plt

print('{}\n'.format(df))

df.plot()
plt.show()

# After calling df.plot, which creates our line plot, we then use plt.show to open a separate
# window containing the visualization of the plot. You can also use plt.savefig to save the
# plot to a PNG or PDF file.

df.plot()
plt.savefig('df.png')  # save to PNG file

# The plot we created has no title or y-axis label. We can manually set the plot's title and
# axis labels using the pyplot API.

df.plot()
plt.title('HR vs. Year')
plt.xlabel('Year')
plt.ylabel('HR Count')
plt.show()

print("\n")
# Other Plots
print("Other Plots")

# In addition to basic line plots, we can create other plots like histograms or boxplots by
# setting the kind keyword argument in plot.

df.plot(kind='hist')
df.plot(kind='box')
plt.show()

# There are numerous different kinds of plots we can create by setting the kind keyword argument.
# A list of the accepted values for kind can be found in the documentation for plot.

print("\n")
# Multiple Features
print("Multiple Features")

df.plot()
df.plot(kind='box')
plt.show()

# These are a line plot and boxplot showing both hits (H) and walks (BB). Note that the circles
# in the boxplot represent outlier values.
