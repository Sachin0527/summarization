from src.api import APIClient


# Base handler class
class BaseHandler:
    def __init__(self, logger, api_config):
        self.logger = logger
        self.api_config = api_config

    def summarize(self, input_file, output_file):
        pass

    def call_api(self, text):
        try:
            client = APIClient(self.api_config)
            self.logger.debug(f"API call started")
            summary = client.api_call(text)
            self.logger.debug(f"API call ended")
            return summary
        except Exception as e:
            msg = f"Error in API call: {str(e)}"
            self.logger.error(msg)
            raise Exception(msg)
