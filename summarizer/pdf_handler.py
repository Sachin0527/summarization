import logging
import PyPDF2
from summarizer.summarization import summarize_large_text

def summarize_pdf(input_file_path, output_file_path):
    logging.info(f"Summarizing PDF file: {input_file_path}")

    with open(input_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    summary = summarize_large_text(text)

    with open(output_file_path, 'w') as file:
        file.write(summary)

    logging.info(f"Summary for {input_file_path} written successfully.")
