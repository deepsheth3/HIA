class FileValidator:
    @staticmethod
    def validate_pdf_upload(upoloaded_file, max_filesize_mb: int = 10):
            """
            Check if uploaded file is empty
            """
            if not upoloaded_file:
                raise ValueError('File Upload Failed')
            
            """
            Check if uploaded file is PDF
            """
            if not upoloaded_file.name.lower().endswith('.pdf'):
                raise ValueError('Only PDF files are allowed')
            
            """
            Check Max File size
            """
            file_size = len(upoloaded_file.getvalue())/(1024**2)
            if file_size > max_filesize_mb:
                raise ValueError(
                    f'File to large: {file_size} MB'
                    f'Maximum Upload Size: {max_filesize_mb} MB'
                )