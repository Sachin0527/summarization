import os
from src.utils import CustomLogger, read_yaml
from src.handlers import PDFHandler, TextHandler, WordHandler


class Summarizer:
    def __init__(self, config_file):
        self.config = read_yaml(config_file)
        print(self.config)
        self.logger = CustomLogger(self.config['logging']).get_logger()

    def summarize(self, input_file):
        self.logger.debug("Summarization process started")
        try:
            output_folder = self.config['output_directory']
            input_file_extension = os.path.splitext(input_file)[1].lower()
            input_file_name = os.path.splitext(os.path.basename(input_file))[0]
            output_file_path = os.path.join(output_folder, f"{input_file_name}_summary{input_file_extension}")

            self.logger.info(f"Starting to summarize file: {input_file}")
            handler = self.get_handler(input_file_extension)
            result = handler.summarize(input_file, output_file_path)
            self.logger.info(f"Summarization process result for file: {input_file} : {result}")
        except Exception as e:
            msg = f"Error summarizing file: {input_file}, Error: {str(e)}"
            self.logger.error(msg)
            raise Exception(msg)

    def get_handler(self, extension):
        self.logger.debug(f"setting up handler for the file extension : {extension}")
        try:
            if extension == '.txt':
                handler = TextHandler(self.logger, self.config['api'])
            elif extension == '.pdf':
                handler = PDFHandler(self.logger, self.config['api'])
            elif extension == '.docx':
                handler = WordHandler(self.logger, self.config['api'])
            else:
                msg = f"Unsupported file format: {extension}"
                self.logger.error(msg)
                raise ValueError(msg)
            self.logger.debug(f"Successfully setup handler for the file extension : {extension}")
            return handler
        except Exception as ex:
            raise Exception(str(ex))
