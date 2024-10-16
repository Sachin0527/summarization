import os
import logging
from src.utils import CustomLogger, read_yaml
from src.handlers import PDFHandler, TextHandler, WordHandler


class Summarizer:
    def __init__(self, config_file):
        try:
            self.config = read_yaml(config_file)
            if 'logging' not in self.config:
                msg= f"The required key 'logging' is missing in the config '{config_file}'"
                raise KeyError(msg)
            else:
                logging_config = self.config['logging']
            self.logger = CustomLogger(logging_config).get_logger()
        except Exception as ex:
            msg = f"An error occurred during execution: {str(ex)}"
            # Set up a default logger if there's an issue
            logging.basicConfig(filename='default.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.error(msg)
            raise Exception(msg)

    def summarize(self, input_file):
        try:
            self.logger.debug("Summarization process started")
            output_folder = self.config.get('output_directory', 'output')
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            input_file_extension = os.path.splitext(input_file)[1].lower()
            input_file_name = os.path.splitext(os.path.basename(input_file))[0]
            output_file_path = os.path.join(output_folder, f"{input_file_name}_summary{input_file_extension}")

            self.logger.info(f"Starting to summarize file: {input_file}")
            handler = self.get_handler(input_file_extension)
            result = handler.summarize(input_file, output_file_path)
            self.logger.info(f"Summarization process result for file: {input_file} : {result}")
            return result
        except Exception as e:
            msg = f"Error in summarization process for file: '{input_file}' \n {str(e)}"
            self.logger.error(msg)
            raise Exception(msg)

    def get_handler(self, extension):
        if 'api' not in self.config:
            raise KeyError(f"The required key 'api' is missing from the config.")
        else:
            api_config = self.config['api']

        self.logger.debug(f"setting up handler for the file extension : {extension}")
        try:
            if extension == '.txt':
                handler = TextHandler(self.logger, api_config )
            elif extension == '.pdf':
                handler = PDFHandler(self.logger, api_config)
            elif extension == '.docx':
                handler = WordHandler(self.logger, api_config)
            else:
                msg = f"Unsupported file format: {extension}"
                self.logger.error(msg)
                raise ValueError(msg)
            self.logger.debug(f"Successfully setup handler for the file extension : {extension}")
            return handler
        except Exception as ex:
            msg = f"Error in setting file format handler : \n {str(ex)}"
            self.logger.error(msg)
            raise Exception(msg)
