import os
import logging
from summarizer.text_handler import summarize_txt
from summarizer.pdf_handler import summarize_pdf
from summarizer.word_handler import summarize_word

def summarize_file(input_file_path, output_folder):
    extension = os.path.splitext(input_file_path)[1].lower()
    base_filename = os.path.splitext(os.path.basename(input_file_path))[0]  # Get the base file name without extension
    output_file_path = os.path.join(output_folder, f"{base_filename}_summary{extension}")

    logging.info(f"Processing file: {input_file_path}")

    if extension == '.txt':
        summarize_txt(input_file_path, output_file_path)
    elif extension == '.pdf':
        summarize_pdf(input_file_path, output_file_path)
    elif extension == '.docx':
        summarize_word(input_file_path, output_file_path)
    else:
        raise ValueError(f"Unsupported file format: {extension}")

    logging.info(f"Output written to: {output_file_path}")
    return output_file_path
