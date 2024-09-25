import os
from .pdf_handler import summarize_pdf
from .docx_handler import summarize_docx
from .text_handler import summarize_txt

# Define input and output directories
INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

# Ensure directories exist
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def choose_document_format():
    print("Choose input file format:")
    print("1. PDF")
    print("2. DOCX")
    print("3. Plain Text (TXT)")
    input_choice = input("Enter the number corresponding to your choice: ")

    print("\nChoose output file format:")
    print("1. PDF")
    print("2. DOCX")
    print("3. Plain Text (TXT)")
    output_choice = input("Enter the number corresponding to your choice: ")

    file_type_map = {
        "1": "pdf",
        "2": "docx",
        "3": "txt"
    }

    input_format = file_type_map.get(input_choice, "txt")
    output_format = file_type_map.get(output_choice, "txt")

    return input_format, output_format

def summarize_files(input_format, output_format):
    input_file_path = os.path.join(INPUT_DIR, f"input.{input_format}")
    output_file_path = os.path.join(OUTPUT_DIR, f"summary.{output_format}")

    if input_format == "pdf":
        summarize_pdf(input_file_path, output_file_path)
    elif input_format == "docx":
        summarize_docx(input_file_path, output_file_path)
    else:
        summarize_txt(input_file_path, output_file_path)
