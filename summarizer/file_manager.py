import os
from summarizer.text_handler import summarize_txt
from summarizer.pdf_handler import summarize_pdf
from summarizer.word_handler import summarize_word
from summarizer.logger import logger  # Import the logger

def summarize_file(input_file_path, output_folder):
    extension = os.path.splitext(input_file_path)[1].lower()
    base_filename = os.path.splitext(os.path.basename(input_file_path))[0]
    output_file_path = os.path.join(output_folder, f"{base_filename}_summary{extension}")

    logger.info(f"Starting to summarize file: {input_file_path}")

    try:
        if extension == '.txt':
            summarize_txt(input_file_path, output_file_path)
        elif extension == '.pdf':
            summarize_pdf(input_file_path, output_file_path)
        elif extension == '.docx':
            summarize_word(input_file_path, output_file_path)
        else:
            logger.error(f"Unsupported file format: {extension}")
            raise ValueError(f"Unsupported file format: {extension}")

        logger.info(f"Summary written to: {output_file_path}")
    except Exception as e:
        logger.error(f"Error summarizing file: {input_file_path}, Error: {str(e)}")
        raise

    return output_file_path
