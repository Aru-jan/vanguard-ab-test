
# rename columns
def rename_columns(dataFrames, config):
    for name, dataFrame in dataFrames.items():
        new_names = {values['original_name']: new_name for new_name,
                     values in config['tables'][name]['columns'].items()}

        dataFrames[name] = dataFrame.rename(columns=new_names)
    return dataFrames

# select columns
def select_columns(dataFrames, config):
    for name, dataFrame in dataFrames.items():
        selected_columns = config['tables'][name]['columns'].keys()
        dataFrames[name] = dataFrame[selected_columns]
    return dataFrames

def clean_categorical_data(dataFrames, config):
    #TODO : default values for categories if no valid_categories
    for table in config['tables']:
        for column in config['tables'][table]['columns']:

            column_config = config['tables'][table]['columns'][column]
            valid_categories = column_config.get('valid_categories')

            if valid_categories:
                dataFrames[table][column] = dataFrames[table][column].astype('category')
                dataFrames[table][column] = dataFrames[table][column].cat.set_categories(valid_categories)

                fallback = column_config.get('fallback_category')
                if fallback:
                    dataFrames[table][column] = dataFrames[table][column].fillna(fallback)
                else:
                    dataFrames[table][column] = dataFrames[table][column].dropna()
    return dataFrames
            
def convert_types(dataFrames, config):
    for table in config['tables']:
        for column in config['tables'][table]['columns']:
            column_config = config['tables'][table]['columns'][column]
            if column_config['pandas_dtype'] == 'int64':
                dataFrames[table][column] = dataFrames[table][column].fillna(0)  # or use dropna()
            dataFrames[table][column] = dataFrames[table][column].astype(column_config['pandas_dtype'])
    return dataFrames