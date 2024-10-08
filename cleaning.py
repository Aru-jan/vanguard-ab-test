from IPython.display import display
import pandas as pd


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

def display_categorical_value_counts(dataFrames, config):
    for table in config['tables']:
        for column in config['tables'][table]['columns']:
            column_config = config['tables'][table]['columns'][column]
            if column_config.get('pandas_dtype') == 'category':
                print(f"Value counts for {table}.{column}:")
                display(dataFrames[table][column].value_counts())
                print("\n")