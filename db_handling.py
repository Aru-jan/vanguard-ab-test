from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd


def create_db(password, config):
    database_name = config['database_name']

    # Set Up Database Connection
    engine = create_engine(f'mysql+pymysql://root:{password}@localhost')

    # Create Database if it Doesn't Exist
    with engine.connect() as conn:
        conn.execute(text(f'CREATE DATABASE IF NOT EXISTS {database_name}'))

    # Connect to the Newly Created Database
    engine = create_engine(
        f'mysql+pymysql://root:{password}@localhost/{database_name}')
    return engine


def export_dataframes_to_sql(engine, dataframes, config):

    if config['refresh_db']:
        for table_name, df in dataframes.items():
            df.to_sql(name=table_name, con=engine,
                      if_exists='replace', index=False)

    else:
        print('Skipping export, set refresh_db to true in config.yaml to export to SQL.')


def import_data_from_sql(engine, table_name):
    data = pd.read_sql(f"SELECT * FROM {table_name}", engine)
    return data
