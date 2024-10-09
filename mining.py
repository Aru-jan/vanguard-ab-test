import yaml
import pandas as pd
from IPython.display import display
import requests
import os

# import data from txt file into pandas dataframe

def import_data(sources: list, separator: str = ',') -> list:
    data_frames = []
    
    for source in sources:
        path = source.get('path')
        url = source.get('url', None)
        
        if not (os.path.exists(path)):
            print(f"Downloading file from {url}")
            save_file_from_url(url, path)
            print(f"File saved to {path}")
        
        data = pd.read_csv(path, sep=separator)
        data_frames.append(data)
    
    return data_frames

def concat_dataframes(data_frames: list) -> pd.DataFrame:
    data = pd.concat(data_frames, axis=0)
    data = data.reset_index(drop=True)
    return data
    

# import data from config.yaml
def import_data_from_config(config, table_name: str) -> pd.DataFrame:
    dataframe = pd.DataFrame()
    table = config['tables'][table_name]
    sources = table['sources']
    separator = table.get('separator', ',')

    data = import_data(sources, separator)
  
    dataframe = concat_dataframes(data)
        
    return dataframe


def parse_config():
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        print(config)
    return config

def display_dataFrames(dataFrames, *args):
    # Dictionary to map args to corresponding DataFrame attributes or methods
    options = {
        'frame': lambda df: df,
        'head': lambda df: df.head(),
        'tail': lambda df: df.tail(),
        'shape': lambda df: df.shape,
        'info': lambda df: df.info(),  # Info prints directly so no need for display()
        'describe': lambda df: df.describe(),
        'columns': lambda df: df.columns,
        'dtypes': lambda df: df.dtypes,
        'isnull': lambda df: df.isnull().sum(),
        'value_counts': lambda df: df.apply(lambda col: col.value_counts()),
        'unique': lambda df: df.nunique(),
        'index': lambda df: df.index,
        'cat_count': lambda df: df.select_dtypes(include=['category']).apply(lambda col: col.value_counts())
    }
    
    for name, dataFrame in dataFrames.items():
        print(f'{name}:')
        for arg in args:
            if arg in options:
                print(f'{name} - {arg.capitalize()}:')
                result = options[arg](dataFrame)
                if arg != 'info':  # Avoid display for 'info' since it prints directly
                    display(result)
            else:
                print(f'Unknown option: {arg}')


def save_file_from_url(url: str, path: str):
    response = requests.get(url)
    with open(path, 'wb') as file:
        file.write(response.content)