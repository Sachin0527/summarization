from docx import Document

doc = Document()
doc.add_paragraph("Test Paragraph")
doc.save("test.docx")