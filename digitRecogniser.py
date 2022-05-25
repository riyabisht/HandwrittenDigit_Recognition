import streamlit as st
import predict as predict
from PIL import Image, ImageOps

st.title('Handwritten digit Recognition')
uploaded_file = st.file_uploader("choose a file")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    result= predict.predictDigit(image)
    st.write("digit is ",result)