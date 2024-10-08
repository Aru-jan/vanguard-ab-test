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

def display_categorical_value_counts(dataFrames):
    for dataFrame in dataFrames.values():
        for column in dataFrame.select_dtypes(include=['category']):
            display(dataFrame[column].value_counts())