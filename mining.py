import yaml
import pandas as pd

# import data from txt file into pandas dataframe
def import_data(paths: list, separator: str = ',') -> pd.DataFrame:
    
    print(paths)
    data = pd.concat([pd.read_csv(path, sep=separator) for path in paths], axis=1)
    #data = pd.read_csv(paths, sep=separator)
    return data

# import data from config.yaml
def import_data_from_config(config, table_name: str) -> pd.DataFrame:

    table = config['tables'][table_name]
    print(table)
    paths = table.get('paths')
    print(paths)
    
    separator = table.get('separator', ',')
    
    data = import_data(paths, separator)
    return data

def parse_config():
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        print(config)
    return config

def merge_dfs(*dataframes):
    return pd.concat(dataframes, axis=1)
