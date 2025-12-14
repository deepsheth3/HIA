class TextUlits:
    @staticmethod
    def clean_extracted_text(extracted_text: str) -> str:
        if not extracted_text:
            return ''
        
        cleaned_text = ' '.join(extracted_text.split())

        return cleaned_text