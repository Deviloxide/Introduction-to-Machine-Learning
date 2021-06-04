from sklearn.datasets import load_breast_cancer

from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

# The coding exercise in this chapter involves completing the separate
# _components function, which will separate principal component data by
# class.

# To do this, we first need to complete a helper function, get_label_info,
# which returns the label name and data for an input class label.

# The component_data input represents the principal component data.

# The labels input is a 1-D array containing the class label IDs
# corresponding to each row of component_data. We can use it to separate
# the principle components by class.

# The class_label input represents a particular class label ID.

# The label_names input represents all the string names for the class
# labels.

# Set label_name equal to the string at index class_label of label_names.

# Set label_data equal to the rows of component_data corresponding to the
# indexes where labels equals class_label. Then return the tuple
# (label_name, label_data).

def get_label_info(component_data, labels,
                   class_label, label_names):
    label_name = label_names[class_label]
    label_data = component_data[labels == class_label]
    return label_name, label_data


# Now, inside the main separate_data function, we'll iterate through each
# label in the label_names list.

# Set separated_data equal to an empty list.

# Create a for loop that iterates variable class_label through
# range(len(label_names)).

# Inside the for loop, we can use our helper function to obtain the
# separated data for each class.

# Inside the for loop, call get_label_info with inputs component_data,
# labels, class_label, and label_names. Append the function's output to
# separated_data.

# After finalizing the list of principle components separated by class,
# we return it.

# Outside the for loop, return separated_data.

def separate_data(component_data, labels,
                  label_names):
    separated_data = []
    for class_label in range(len(label_names)):
        separated_data.append(get_label_info(
            component_data, labels, class_label, label_names))
    return separated_data


# The separate_data function is incredibly useful for visualizing the
# components. We can use matplotlib to create nice plots of the separated
# data (shown in the code below).

bc = load_breast_cancer()
pca_obj = PCA(n_components=2)
component_data = pca_obj.fit_transform(bc.data)
labels = bc.target
label_names = bc.target_names
# Using the completed separate_data function
separated_data = separate_data(component_data,
                               labels, label_names)

# Plotting the data
for label_name, label_data in separated_data:
    col1 = label_data[:, 0]  # 1st column (1st pr. comp.)
    col2 = label_data[:, 1]  # 2nd column (2nd pr. comp.)
    plt.scatter(col1, col2, label=label_name)  # scatterplot
plt.legend()  # adds legend to plot
plt.title('Breast Cancer Dataset PCA Plot')
plt.show()
