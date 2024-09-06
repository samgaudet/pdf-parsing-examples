from PyPDF2 import PdfReader

if __name__ == "__main__":

    PDF_FILEPATH = (
        r"C:\Users\sgaud\git\pdf-parsing-examples\sample_pdfs\minimal-document.pdf"
    )

    reader = PdfReader(PDF_FILEPATH)
    page = reader.pages[0]

    # this prints the text from the document, including the page number, etc.
    print(page.extract_text())
