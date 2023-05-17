# Import required libraries
import PyPDF2

# Open the PDF file
with open('Australia_cybersecuritystrategy.pdf', mode='rb') as file:
    
    # Read the PDF file
    reader = PyPDF2.PdfReader(file)
    
    # Get the number of pages in the PDF file
    num_pages = len(reader.pages)
    
    # Extract text from each page of the PDF file
    text = ""
    for i in range(num_pages):
        page = reader.pages[i]
        text += page.extract_text()
#print(text)