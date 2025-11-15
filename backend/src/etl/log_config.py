import logging
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),  
        logging.StreamHandler()               
    ]
)

def get_logger(name):
    return logging.getLogger(name)