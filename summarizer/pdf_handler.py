import PyPDF2
from summarizer.summarization import summarize_large_text
from summarizer.logger import logger  # Import logger

def summarize_pdf(input_file_path, output_file_path):
    logger.info(f"Reading PDF file: {input_file_path}")
    
    try:
        with open(input_file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        
        if not text.strip():
            logger.error(f"Failed to extract text from the PDF file: {input_file_path}")
            raise ValueError("No text found in the PDF file.")
        
        logger.info(f"PDF text extracted successfully from {input_file_path}. Starting summarization.")
        summary = summarize_large_text(text)

        with open(output_file_path, 'w') as file:
            file.write(summary)

        logger.info(f"Summary written successfully to {output_file_path}")
    except Exception as e:
        logger.error(f"Error summarizing PDF file: {input_file_path}, Error: {str(e)}")
        raise
