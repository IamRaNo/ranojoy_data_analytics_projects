
from sqlalchemy import create_engine,text
import pandas as pd
import numpy as np

def get_engine(
    user="root",
    password="7003890541",
    host="localhost",
    port=3306,
    database="oulad_university_dataset"
):
    """Returns a SQLAlchemy engine for the MySQL database."""
    return create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")


eng = get_engine(database="oulad_university_dataset")

def sql(query , engine = eng):
    if engine is None:
        engine = get_engine()
    else:
        try:
            df = pd.read_sql(text(query), engine)
            return df
        except Exception as e:
            print("SQL ERROR:", e)
            return None

def select(table_name):
    return pd.read_sql(f'select * from {table_name} limit 5',eng)


def run(query,engine = eng):
    if engine is None:
        engine = get_engine()
    with engine.connect() as con:
        con.execute(text(query))
        con.commit()

def fetch_all_cols(table):
    query = f'''
        select column_name from information_schema.columns
        where table_name = '{table}' and
        table_schema = database()
    '''
    df = pd.read_sql(query,eng)
    return df['COLUMN_NAME'].values.tolist()

def find_nulls(table):
    dict ={}
    for col in fetch_all_cols(table):
        query = f'''
            select sum({col} is null) as {col}_nulls from {table}
        '''
        df =sql(query)
        dict[col] = df.iloc[0].values.astype('int')
    return(pd.DataFrame.
            from_dict(dict,orient='index',columns=['null_values']).
            reset_index().
            rename(columns={'index':'column_names'}))

def get_project_root(project_name="ranojoy_data_analytics_projects"):
    """
    Universally finds the project root.
    1. Checks if we are inside the project (standard usage).
    2. Checks if we are above the project (your specific usage).
    """
    current_path = Path.cwd()
    # CASE 1: Standard Usage (Running from inside the repo)
    if project_name in str(current_path):
        while current_path.name != project_name:
            current_path = current_path.parent
        return current_path
    # We search specifically for the project folder inside the current directory
    # limiting depth to 4 levels to keep it fast.
    else:
        # rglob searches recursively for the folder name
        for path in current_path.rglob(project_name):
            if path.is_dir():
                return path
        raise FileNotFoundError(f"Could not find project: {project_name}")