import logging
from summarizer.summarization import summarize_large_text

def summarize_txt(input_file_path, output_file_path):
    logging.info(f"Summarizing text file: {input_file_path}")
    
    with open(input_file_path, 'r') as file:
        text = file.read()

    summary = summarize_large_text(text)

    with open(output_file_path, 'w') as file:
        file.write(summary)

    logging.info(f"Summary for {input_file_path} written successfully.")
