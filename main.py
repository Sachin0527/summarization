import os
from summarizer.file_manager import summarize_file
from summarizer.logger import logger  # Import logger

def main():
    try:
        input_file_path = input("Enter the path to the file you want to summarize: ")
        output_folder = 'output'

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file_path = summarize_file(input_file_path, output_folder)
        logger.info(f"Summary process completed for file: {input_file_path}")
        print(f"Summary has been written to {output_file_path}")
    except Exception as e:
        logger.error(f"Error in main function: {str(e)}")
        print("An error occurred during the summarization process. Check logs for details.")

if __name__ == '__main__':
    main()
