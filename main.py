import os
import logging
from summarizer.file_manager import summarize_file

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    input_file_path = input("Enter the path to the file you want to summarize: ")
    output_folder = 'output'

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info(f"Output folder '{output_folder}' created.")

    try:
        output_file_path = summarize_file(input_file_path, output_folder)
        logging.info(f"Summary has been written to {output_file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
