import pdfplumber
import io
import hashlib

class PDFUtils:
    # Extract text from all pages of a PDF (in-memory)
    @staticmethod
    def extract_text_from_pdf(pdf_bytes: bytes) -> str:
        extracted_text = ""

        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n\n"
        return extracted_text

    # Generate a content-based hash to detect file changes
    @staticmethod
    def get_file_hash(pdf_bytes: bytes) -> str:
        return hashlib.sha256(pdf_bytes).hexdigest()
