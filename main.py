from summarizer.file_manager import choose_document_format, summarize_files

def main():
    # Ask the user to choose file formats
    input_format, output_format = choose_document_format()

    # Perform the summarization
    summarize_files(input_format, output_format)

if __name__ == "__main__":
    main()
