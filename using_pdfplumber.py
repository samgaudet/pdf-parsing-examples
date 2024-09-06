import pdfplumber

if __name__ == "__main__":

    PDF_FILEPATH = (
        r"C:\Users\sgaud\git\pdf-parsing-examples\sample_pdfs\minimal-document.pdf"
    )

    pdf = pdfplumber.open(PDF_FILEPATH)
    page = pdf.pages[0]

    # this prints the text from the document, including the page number, etc.
    print(page.extract_text())
