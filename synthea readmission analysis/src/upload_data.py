import gdown
import os
import pandas as pd
from sqlalchemy import create_engine
import logging
import time

# logging config
logging.basicConfig(
    filename=r"C:\Users\Rano's PC\Machine\github_repo_cloned\my-personal-projects\synthea readmission analysis\logs\synthea_data_uploads.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder_url = "https://drive.google.com/drive/folders/1UHH9wmZ137_IK8zTSQbWcQd7dbXYEC1c?usp=drive_link"
download_path = r"C:\Users\Rano's PC\Machine\github_repo_cloned\my-personal-projects\synthea readmission analysis\data\raw_data"

logging.info("Downloading folder from Google Drive...")
start = time.time()
gdown.download_folder(folder_url, output=download_path, quiet=False)
end = time.time()
time_taken = end - start
logging.info(f"Download completed. Time taken -> {round(time_taken,2)} seconds")

engine = create_engine("mysql+pymysql://root:7003890541@localhost:3306/synthea_medical_dataset")

for file in os.listdir(download_path):
    if file.endswith(".csv"):
        filepath = os.path.join(download_path, file)
        df = pd.read_csv(filepath)
        table = file.replace(".csv", "")

        try:
            start = time.time()
            logging.info(f"Loading table {table} with shape {df.shape}")
            df.to_sql(table,
                      engine,
                      index=False,
                      if_exists="replace",
                      chunksize=10000)
            end = time.time()
            time_taken = end - start
            logging.info(f"Loaded successfully: {table}, time taken {round(time_taken,2)} seconds")
        except Exception as e:
            logging.error(f"Failed loading {table}: {e}")
