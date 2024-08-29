import yaml

def load_config(config_file='config.yml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Load the configuration
config = load_config()

# Retrieve the API key and model generation configuration
API_KEY = config.get("google_api_key")
GENERATION_CONFIG = config.get("generation_config")
