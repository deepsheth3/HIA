import pdfplumber
import io 


"""
Use this to extracted the text from all the pages of the PDF and return it.
Code Flow = main (pdf_btyes) -> extract_text (return str) -> main
"""
def extract_text_from_pdf(pdf_bytes:bytes) -> str:
    extracted_text = ''

    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_text += text

    return extracted_text