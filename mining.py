import yaml
import pandas as pd

# import data from txt file into pandas dataframe
def import_data(path: str, separator: str = ',') -> pd.DataFrame:
    #if list : merge tables
    data = pd.read_csv(path, sep=separator)
    return data

# import data from config.yaml
def import_data_from_config(config, table_name: str) -> pd.DataFrame:

    table = config['tables'][table_name]
    print(table)
    path = table.get('path')
    separator = table.get('separator', ',')
    data = import_data(path, separator)
    return data

def parse_config():
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        print(config)
    return config