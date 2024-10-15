import logging
import os
from config.config import load_config

config = load_config()
log_file_name = config.get("log_file", "summarization.log")

# Create a logger
logger = logging.getLogger('summarizer_logger')
logger.setLevel(logging.DEBUG)

# Create logs directory if it doesn't exist
log_dir = os.path.join(os.path.dirname(__file__), '../logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create file handler for logging
log_file_path = os.path.join(log_dir, log_file_name)
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)
