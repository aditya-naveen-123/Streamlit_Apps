import streamlit as st
from PyPDF2 import PdfReader
from io import BytesIO
import google.generativeai as genai

genai.configure(api_key="AIzaSyDOEAQA3vOP9B_w1uP-AmJH2FvS9mr9hxs")


def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
   # response = model.generate_content([input, image[0], prompt])
    responses = model.generate_content(input, stream=False)
    return responses.candidates[0].content.parts[0].text
    #return response.text


def input_image_setup(file_content):
    file_io = BytesIO(file_content)
    pdf_reader = PdfReader(file_io)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text


st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose a PDF file...", type=["pdf"])

if uploaded_file is not None:
    st.write("File Uploaded!")

submit = st.button("Tell me about the image")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input document
               """

if submit:
    if uploaded_file is not None:
        # Read the content of the uploaded file
        file_content = uploaded_file.read()
        image_data = input_image_setup(file_content)
        input_prompt =  input_prompt+image_data+input_text
        response = get_gemini_response(input_prompt)
        st.subheader("The Response is")
        st.write(response)
