import streamlit as st
import requests

st.title('PDF to Schema Extractor')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    files = {"file": uploaded_file}
    response = requests.post("http://localhost:5000/process_pdf", files=files)
    result = response.json()

    st.json(result['mapped_data'])
    st.json(result['missing_data'])