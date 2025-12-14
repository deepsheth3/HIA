import pdfplumber
import io 
import hashlib


"""
Use this to extracted the text from all the pages of the PDF and return it.
Code Flow = main (pdf_btyes) -> extract_text (return str) -> main
"""
class PDF_Utils:
    def extract_text_from_pdf(pdf_bytes:bytes) -> str:
        extracted_text = ''

        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text

        return extracted_text

    def get_file_hash(pdf_bytes:bytes) -> str:
        return hashlib.sha256(pdf_bytes).hexdigest()