from IPython.display import display

def tukeys_test_outliers(my_data, method="show"):
    data = my_data.copy()
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    # Define bounds for the outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
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
    
def filter_visits_by_steps(
    df,
    start_step=None,
    end_step=None,
    exact_steps=None,
    exclude_exact_steps=None,
    include_steps=None,
    exclude_steps=None
):
    def condition(group):
        steps = list(group['process_step'])
        
        # Check for start step
        if start_step is not None and steps[0] != start_step:
            return False
        
        # Check for end step
        if end_step is not None and steps[-1] != end_step:
            return False
        
        # Check for exact sequence of steps
        if exact_steps is not None and steps != exact_steps:
            return False
        
        # Exclude specific exact sequence of steps
        if exclude_exact_steps is not None and steps == exclude_exact_steps:
            return False
        
        # Check for inclusion of specific steps
        if include_steps is not None:
            for step in include_steps:
                if step not in steps:
                    return False
        
        # Check for exclusion of specific steps
        if exclude_steps is not None:
            for step in exclude_steps:
                if step in steps:
                    return False
        
        return True
    
    df_filtered = df.groupby('visit_id').filter(condition)
    return df_filtered