from .base_handler import BaseHandler


class TextHandler(BaseHandler):
    def summarize(self, input_file, output_file):
        try:
            self.logger.debug(f"Reading TXT file: {input_file}")
            with open(input_file, 'r') as file:
                text = file.read()

            summary = self.call_api(text)

            self.logger.debug(f"Writing summary in TXT file: {output_file}")
            with open(output_file, 'w') as file:
                file.write(summary)
            self.logger.debug(f"Summary written successfully to {output_file}")
            return f"Summary written successfully to {output_file}"
        except Exception as e:
            msg = f"Error in Text Handler: \n {str(e)}"
            self.logger.error(msg)
            raise Exception(msg)