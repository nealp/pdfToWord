import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import io

st.title('PDF to Word Converter')

st.write("Upload your PDF here:")

uploaded_file= st.file_uploader(" ", type = ["pdf"])
