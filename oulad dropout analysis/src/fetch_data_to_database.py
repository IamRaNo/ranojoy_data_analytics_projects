import kagglehub
import pandas as pd
import os
import time
import logging
from sqlalchemy import create_engine

# --- FIXING THE PATHS ---
# 1. Get the directory where this script is located (src)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Go UP one level to get the main project folder (synthea readmission analysis)
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# 3. Now define paths relative to the Project Root
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
LOG_PATH = os.path.join(LOG_DIR, "oulad_data_upload.log")

# logging config
logging.basicConfig(
    filename=LOG_PATH,
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