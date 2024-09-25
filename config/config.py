import yaml

# Read the configuration from config.yaml
def load_config():
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_config()

API_KEY = config['api_key']
GENERATION_CONFIG = config['generation_config']
