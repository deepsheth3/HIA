import streamlit as st
from utils.pdf_utils import PDF_Utils
from utils.validators import validate_pdf_upload
from config.app_config import AppConfig
import hashlib

st.set_page_config(page_title=AppConfig.APP_TITLE)

st.title(AppConfig.APP_TITLE)
st.write('Upload your health report PDF here.')

uploaded_file = st.file_uploader('Upload a PDF file',
                                type='PDF')

if 'extracted_text' not in st.session_state:
    st.session_state.extracted_text = None

if 'has_processed' not in st.session_state:
    st.session_state.has_processed = False

if 'file_hash' not in st.session_state:
    st.session_state.file_hash = None

# -------------------------
# Detect NEW file by content
# -------------------------
if uploaded_file is not None:
    pdf_bytes = uploaded_file.getvalue()
    current_hash = PDF_Utils.get_file_hash(pdf_bytes)

    if current_hash != st.session_state.file_hash:
        # New file content detected → reset state
        st.session_state.extracted_text = None
        st.session_state.has_processed = False
        st.session_state.file_hash = current_hash


# -------------------------
# Validate + Analyze
# -------------------------
if uploaded_file is not None:
    try:
        validate_pdf_upload(
            uploaded_file,
            max_filesize_mb=AppConfig.MAX_FILESIZE_MB
        )

        st.success("File validated successfully!")

        if st.button(
            "Analyze PDF",
            disabled=st.session_state.has_processed
        ):
            st.session_state.extracted_text = PDF_Utils.extract_text_from_pdf(pdf_bytes)
            st.session_state.has_processed = True
            st.rerun()

    except ValueError as e:
        st.error(str(e))

if st.session_state.extracted_text:
    st.subheader('Extracted Text')      
    st.text_area(
        'PDF Conent',
        st.session_state.extracted_text,
        height= 300
    )