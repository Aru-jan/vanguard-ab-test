def rename_columns(df, column_names_dict):
    df = df.rename(columns=column_names_dict)
    return df

