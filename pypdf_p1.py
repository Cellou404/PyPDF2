from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_path = 'pooArticle.pdf'
pdf_enc = 'pooArticleCrypted.pdf'

pdfWriter = PdfFileWriter()
pdf = PdfFileReader(pdf_path)

for page_num in range(pdf.numPages):
    pdfWriter.addPage(pdf.getPage(page_num))

password = 'cisseu49kd'
pdfWriter.encrypt(password)

with open(pdf_enc, 'wb') as f:
    pdfWriter.write(f)
    f.close()
