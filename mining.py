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
            print(f'{name} - Full DataFrame:')
            display(dataFrame)
        if 'head' in args:
            print(f'{name} - Head:')
            display(dataFrame.head())
        if 'tail' in args:
            print(f'{name} - Tail:')
            display(dataFrame.tail())
        if 'shape' in args:
            print(f'{name} - Shape:')
            display(dataFrame.shape)
        if 'info' in args:
            print(f'{name} - Info:')
            display(dataFrame.info())
        if 'describe' in args:
            print(f'{name} - Describe:')
            display(dataFrame.describe())
        if 'columns' in args:
            print(f'{name} - Columns:')
            display(dataFrame.columns)
        if 'dtypes' in args:
            print(f'{name} - Data Types:')
            display(dataFrame.dtypes)
        if 'isnull' in args:
            print(f'{name} - Null Values:')
            display(dataFrame.isnull().sum())
        if 'value_counts' in args:
            print(f'{name} - Value Counts:')
            display(dataFrame.value_counts())
        if 'unique' in args:
            print(f'{name} - Unique Values:')
            display(dataFrame.nunique())
        if 'index' in args:
            print(f'{name} - Index:')
            display(dataFrame.index)
        if 'cat_count' in args:
            print(f'{name} - Category Counts:')
            display(dataFrame.select_dtypes(include=['category']).value_counts())