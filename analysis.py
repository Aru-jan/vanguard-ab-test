def tukeys_test_outliers(my_data, method="show"):
    data = my_data.copy()
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    # Define bounds for the outliers
    lower_bound = Q1 - 1.2 * IQR
    upper_bound = Q3 + 1 * IQR
    # Identify the outliers
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    if method == "show":
        return outliers
    elif method == "replace":
        median = data.median()
        data.loc[outliers.index] = median
        return data
    elif method == "delete":
        index_drop = outliers.index
        data_no_outliers = data.drop(index_drop)
        display(data_no_outliers)
        return data_no_outliers.index