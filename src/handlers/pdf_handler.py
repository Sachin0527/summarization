import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.enums import TA_JUSTIFY
from .base_handler import BaseHandler


def create_pdf_with_text(output_file, text):
    # Create a SimpleDocTemplate for layout control
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    # Get default styles and create a custom justified style
    styles = getSampleStyleSheet()
    justified_style = ParagraphStyle(
        'Justified',
        parent=styles['Normal'],  # Base it on the 'Normal' style
        alignment=TA_JUSTIFY,  # Justify text
        spaceBefore=12,  # Space before paragraphs
        spaceAfter=12,  # Space after paragraphs
        leading=15,  # Line spacing
    )
    # Split the text into paragraphs based on double new lines to maintain structure
    paragraphs = text.split("\n\n")
    # Add each paragraph separately and apply justified formatting
    story = []
    for para in paragraphs:
        story.append(Paragraph(para.replace("\n", "<br />"), justified_style))
    # Build the PDF with the content
    doc.build(story)


class PDFHandler(BaseHandler):
    def summarize(self, input_file, output_file):
        try:
            self.logger.debug(f"Reading PDF file: {input_file}")
            with open(input_file, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()

            if not text.strip():
                self.logger.error(f"Failed to extract text from the PDF file: {input_file}")
                raise ValueError(f"Failed to extract text from the PDF file: {input_file}")

            self.logger.debug(f"PDF text extracted successfully from {input_file}. Starting summarization.")

            summary = self.call_api(text)

            self.logger.debug(f"Writing summary in PDF file: {output_file}")

            create_pdf_with_text(output_file, summary)

            self.logger.debug(f"Summary written successfully to {output_file}")
            return f"Summary written successfully to {output_file}"
        except Exception as e:
            msg = f"Error in PDF Handler: \n {str(e)}"
            self.logger.error(msg)
            raise Exception(msg)
