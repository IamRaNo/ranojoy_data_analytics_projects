import kagglehub
import pandas as pd
import os
import time
import logging
from sqlalchemy import create_engine

# logging config
logging.basicConfig(
    filename=r"C:\Users\Rano's PC\Machine\github_repo_cloned\my-personal-projects\oulad dropout analysis\logs\oulad_data_upload_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info('Importing data from kaggle API')
start = time.time()
path = kagglehub.dataset_download("anlgrbz/student-demographics-online-education-dataoulad")
end = time.time()
time_taken = end - start
logging.info(f'Import Done, Time taken {round(time_taken,2)} seconds')
print("Path to dataset files:", path)


for file in os.listdir(path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(path, file))
        print(file, df.shape)

user = 'root'
password = '7003890541'
port = 3306
host = 'localhost'
database = 'oulad_university_dataset'

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

for file in os.listdir(path):
    if file.endswith(".csv"):
        table = file.replace(".csv","")
        df = pd.read_csv(os.path.join(path, file))
        try:
            start = time.time()
            logging.info(f"Loading table {table} with shape {df.shape}")
            df.to_sql(table, engine, index=False, if_exists="replace")
            end = time.time()
            time_taken = end - start
            logging.info(f"Loaded successfully: {table}, time taken {round(time_taken,2)} seconds")
        except Exception as e:
             logging.error(f"Failed loading {table}: {e}")