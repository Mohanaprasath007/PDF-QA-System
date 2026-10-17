from PyPDF2 import PdfReader


def extract_pdf_text(pdf_docs):

    text = ""

    for pdf in pdf_docs:

        reader = PdfReader(pdf)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text