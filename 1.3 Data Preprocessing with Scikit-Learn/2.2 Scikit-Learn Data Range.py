from sklearn.preprocessing import MinMaxScaler


# The coding exercise in this chapter uses MinMaxScaler (imported in
# backend) to complete the ranged_data function.

# The function will compress the input NumPy array, data, into the range
# given by value_range.

# Set min_max_scaler equal to MinMaxScaler initialized with value_range
# for the feature_range keyword argument.

# Set scaled_data equal to min_max_scaler.fit_transform applied with data
# as the only argument. Then return scaled_data.

def ranged_data(data, value_range):
    min_max_scaler = MinMaxScaler(feature_range=value_range)
    scaled_data = min_max_scaler.fit_transform(data)
    return scaled_data
    pass
