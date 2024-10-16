import os
import logging


# Custom Logging Class
class CustomLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CustomLogger, cls).__new__(cls)
            cls._instance._initialize_logger(*args, **kwargs)
        return cls._instance

    # Initialize the logger with logging file, level, format etc
    def _initialize_logger(self, config):
        try:
            self.config = config
            self.log_file = self.config.get('logging_file', 'default.log')
            # Extract the folder path from self.log_file
            folder_path = os.path.dirname(self.log_file)
            # Check if the folder exists, if not, create it
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            self.log_level = getattr(logging, self.config.get('logging_level', 'DEBUG')
                                     .upper())
            self.formatter = self.config.get('logging_format', '%(asctime)s :: %(levelname)s :: %(message)s')
            self.logger = logging.getLogger()
            self.logger.setLevel(self.log_level)
            if not self.logger.hasHandlers():
                # File handler
                file_handler = logging.FileHandler(self.log_file)
                file_handler.setLevel(self.log_level)

                # Formatter
                formatter = logging.Formatter(self.formatter)
                file_handler.setFormatter(formatter)

                # Add handlers to the logger
                self.logger.addHandler(file_handler)
        except Exception as e:
            msg = f"Error in logger initialization : \n {str(e)}"
            raise Exception(msg)

    # returns the initialized logger
    def get_logger(self):
        return self.logger
