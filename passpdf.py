from PyPDF2 import PdfReader, PdfWriter
import getpass

# Create PdfWriter instance
writer = PdfWriter()

# Ask user for the original file name
pdf_name = input("Please type in the name of the PDF file (with extension): ")

# Load original PDF
original_file = PdfReader(pdf_name)

# Copy all pages to writer
for page in original_file.pages:
    writer.add_page(page)

# Ask user for password
password = getpass.getpass(prompt="Enter password to secure the PDF: ")

# Encrypt the PDF
writer.encrypt(password)

# Save the secured PDF
with open("secure.pdf", "wb") as f:
    writer.write(f)

print("PDF secured successfully! Saved as 'secure.pdf'")
