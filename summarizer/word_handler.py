import logging
from docx import Document
from summarizer.summarization import summarize_large_text

def summarize_word(input_file_path, output_file_path):
    logging.info(f"Summarizing Word file: {input_file_path}")

    doc = Document(input_file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"

    summary = summarize_large_text(text)

    summary_doc = Document()
    summary_doc.add_paragraph(summary)
    summary_doc.save(output_file_path)

    logging.info(f"Summary for {input_file_path} written successfully.")
