# Reduciremos el peso del archivo PDF con el método de compresión zlib/deflate

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("archivo3_combinado.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.compress_content_streams()  # This is CPU intensive!
    writer.add_page(page)

with open("archivo3_ligero.pdf", "wb") as f:
    writer.write(f)