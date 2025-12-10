import gdown
import os
import pandas as pd
from sqlalchemy import create_engine
import logging
import time

# --- FIXING THE PATHS ---
# 1. Get the directory where this script is located (src)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Go UP one level to get the main project folder (synthea readmission analysis)
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# 3. Now define paths relative to the Project Root
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
DOWNLOAD_PATH = os.path.join(PROJECT_ROOT, "data", "raw_data")
LOG_PATH = os.path.join(LOG_DIR, "synthea_data_uploads.log")

# Create directories if they don't exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

# logging config
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder_url = "https://drive.google.com/drive/folders/1UHH9wmZ137_IK8zTSQbWcQd7dbXYEC1c?usp=drive_link"

logging.info("Downloading folder from Google Drive...")
start = time.time()
# Note: output is set to DOWNLOAD_PATH which is now correct
gdown.download_folder(folder_url, output=DOWNLOAD_PATH, quiet=False)
end = time.time()
time_taken = end - start
logging.info(f"Download completed. Time taken -> {round(time_taken,2)} seconds")

# Database connection (Be careful sharing code with your password in it!)
engine = create_engine("mysql+pymysql://root:7003890541@localhost:3306/synthea_medical_dataset")

# Loop through the files in the download path
for file in os.listdir(DOWNLOAD_PATH):
    if file.endswith(".csv"):
        filepath = os.path.join(DOWNLOAD_PATH, file)
        
        try:
            df = pd.read_csv(filepath)
            table = file.replace(".csv", "") # Table name based on file name

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