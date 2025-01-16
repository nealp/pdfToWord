import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import io

pdf= None

st.title('PDF to Word Converter')

st.image(image="images/image.jpg", width=200)

st.write("Upload your PDF here:")

uploaded_file= st.file_uploader(" ", type = ["pdf"])

#if there is a file uploaded:
if uploaded_file is not None: 
    pdf = PdfReader(uploaded_file)


    'PDF succesfully uploaded!'
#pdf.pages gives a list of all pages
    st.write(f"Number of pages {len(pdf.pages)}")


    doc = Document()

    #for each page in the pdf
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num] #single page
        text = page.extract_text() #extracted text
        doc.add_paragraph(text) #extracted text gets added to doc

    #repositioning new doc file
    word_io =io.BytesIO()
    doc.save(word_io)
    word_io.seek(0)
#create new download button with metadata
    st.download_button(
        label= "Download Converted File",
        data= word_io,
        file_name= "Converted.docx",
        mime = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        
    )