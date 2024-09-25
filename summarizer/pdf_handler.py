import PyPDF2
from reportlab.pdfgen import canvas
from .summarization import summarize_large_text

def read_from_pdf(input_file_path):
    with open(input_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def write_to_pdf(output_file_path, summarized_text):
    pdf = canvas.Canvas(output_file_path)
    pdf.drawString(100, 750, "Summary:")
    text_object = pdf.beginText(100, 730)
    
    for line in summarized_text.split('\n'):
        text_object.textLine(line)

    pdf.drawText(text_object)
    pdf.save()

def summarize_pdf(input_file_path, output_file_path):
    input_text = read_from_pdf(input_file_path)
    summary = summarize_large_text(input_text)
    write_to_pdf(output_file_path, summary)
    print(f"Summary has been written to {output_file_path}")
