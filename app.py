import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import io

st.title('PDF to Word Converter')

st.write("Upload your PDF here:")

uploaded_file= st.file_uploader(" ", type = ["pdf"])

#if there is a file uploaded:
if uploaded_file is not None: 
    pdf = PdfReader(uploaded_file)

    'PDF succesfully uploaded!'

    