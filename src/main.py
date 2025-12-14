import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.validators import validate_pdf_upload
from config.app_config import AppConfig

st.set_page_config(page_title=AppConfig.APP_TITLE)

st.title("HIA file uplaod test")
st.write('Upload your health report PDF here.')

uploaded_file = st.file_uploader('Upload a PDF file',
                                type='PDF')

if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = None

if uploaded_file:
    try:
        validate_pdf_upload(upoloaded_file=uploaded_file,
                            max_filesize_mb=AppConfig.MAX_FILESIZE_MB)
        st.success('File Uploaded Succesfully')

        if st.button('Analyse Report'):
            pdf_bytes = uploaded_file.getvalue()
            st.session_state.extracted_text = extract_text_from_pdf(pdf_bytes=pdf_bytes)

    except ValueError as e:
        st.error(str(e))

if st.session_state.extracted_text:
    st.subheader('Extracted Text')      
    st.text_area(
        'PDF Conent',
        st.session_state.extracted_text,
        height= 300
    )