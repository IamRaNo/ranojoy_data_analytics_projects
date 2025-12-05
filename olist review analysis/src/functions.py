from sqlalchemy import create_engine,text
import pandas as pd
import numpy as np

def get_engine(
    user="root",
    password="7003890541",
    host="localhost",
    port=3306,
    database="olist_shopping_dataset"
):
    """Returns a SQLAlchemy engine for the MySQL database."""
    return create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

def sql(query , engine = None):
    if engine in None:
        engine = get_engine()
    return pd.read_sql(query,engine)

def select(table_name):
    return sql(f'select * from {table_name} limit 5')

def run(query,engine = None):
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
    df = sql(query)
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