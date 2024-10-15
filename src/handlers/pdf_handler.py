import PyPDF2
from .base_handler import BaseHandler


class PDFHandler(BaseHandler):
    def summarize(self, input_file, output_file):
        try:
            self.logger.debug(f"Reading PDF file: {input_file}")
            with open(input_file, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()

            if not text.strip():
                self.logger.error(f"Failed to extract text from the PDF file: {input_file}")
                raise ValueError(f"Failed to extract text from the PDF file: {input_file}")

            self.logger.debug(f"PDF text extracted successfully from {input_file}. Starting summarization.")

            summary = self.call_api(text)

            self.logger.debug(f"Writing summary in PDF file: {output_file}")
            with open(output_file, 'w') as file:
                file.write(summary)

            self.logger.debug(f"Summary written successfully to {output_file}")
            return f"Summary written successfully to {output_file}"
        except Exception as e:
            msg = f"Error summarizing PDF file: {input_file}, Error: {str(e)}"
            self.logger.error(msg)
            raise Exception(msg)
