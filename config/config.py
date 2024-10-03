import yaml
import os

# Load configuration from the YAML file
def load_config():
    config_file_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_file_path, 'r') as file:
        return yaml.safe_load(file)

config = load_config()

# API Key from config.yaml
API_KEY = config['api_key']

# Model name from config.yaml
MODEL_NAME = config['model_name']

# Generation config from config.yaml
GENERATION_CONFIG = config['generation_config']
