import PyPDF2

with open("Some_BrandNew_Doc.pdf", 'rb') as f:
    # Create a PdfReader object
    pdf_reader = PyPDF2.PdfReader(f)
    
    # Get the number of pages
    num_pages = len(pdf_reader.pages)
    print(f'The PDF has {num_pages} pages.')

    # Get the first page
    page_one = pdf_reader.pages[0]
    print(page_one.extract_text())  # Example of extracting text from the first page
