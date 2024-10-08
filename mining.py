import yaml
import pandas as pd
from IPython.display import display

# import data from txt file into pandas dataframe
def import_data(paths: list, separator: str = ',') -> pd.DataFrame:
    
    data = pd.concat([pd.read_csv(path, sep=separator) for path in paths], axis=0)
    data = data.reset_index(drop=True)
    #data = pd.read_csv(paths, sep=separator)
    return data

# import data from config.yaml
def import_data_from_config(config, table_name: str) -> pd.DataFrame:

    table = config['tables'][table_name]
    paths = table.get('paths')
    
    separator = table.get('separator', ',')
    
    data = import_data(paths, separator)
    return data

def parse_config():
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        print(config)
    return config

def display_dataFrames(dataFrames, *args):
    for name, dataFrame in dataFrames.items():
        print(f'{name}:')
        if 'frame' in args:
            display(dataFrame)
        if 'head' in args:
            display(dataFrame.head())
        if 'tail' in args:
            display(dataFrame.tail())
        if 'shape' in args:
            display(dataFrame.shape)
        if 'info' in args:
            display(dataFrame.info())
        if 'describe' in args:
            display(dataFrame.describe())
        if 'columns' in args:
            display(dataFrame.columns)
        if 'dtypes' in args:
            display(dataFrame.dtypes)
        if 'isnull' in args:
            display(dataFrame.isnull().sum())
        if 'value_counts' in args:
            display(dataFrame.value_counts())
        if 'unique' in args:
            display(dataFrame.nunique())
        if 'index' in args:
            display(dataFrame.index)