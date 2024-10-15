from summarizer.summarization import summarize_large_text
from summarizer.logger import logger  # Import logger

def summarize_txt(input_file_path, output_file_path):
    logger.info(f"Reading TXT file: {input_file_path}")
    try:
        with open(input_file_path, 'r') as file:
            text = file.read()

        summary = summarize_large_text(text)

        with open(output_file_path, 'w') as file:
            file.write(summary)

        logger.info(f"Summary successfully written to: {output_file_path}")
    except Exception as e:
        logger.error(f"Failed to summarize TXT file: {input_file_path}, Error: {str(e)}")
        raise
