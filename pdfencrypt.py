from PyPDF2 import PdfWriter, PdfReader
from urllib3.filepost import writer

writer=PdfWriter()
file="Assignment 4.pdf"
reader=PdfReader(file)
for page in range(len(reader.pages)):
    writer.add_page(reader.pages[page])
writer.encrypt("password")
with open("Assignment 4.pdf","wb") as file:
    writer.write(file)
print("PDF encrypted")