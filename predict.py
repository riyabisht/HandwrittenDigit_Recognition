# -*- coding: utf-8 -*-
"""predict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-h1ttJEQGC_gltJaiwJ-7ROYtoi6wEp1
"""

#from matplotlib import image
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_drawable_canvas import st_canvas
# App
def predictDigit(image):

    model = tf.keras.models.load_model("./handwritten.h5")
    # image = Image.open(uploaded_file)
    image = ImageOps.grayscale(image)
    img = image.resize((28,28))
    img = np.array(img, dtype='float32')
    img = img/255
    plt.imshow(img)
    plt.show()
    img = img.reshape((1,28,28,1))
    pred= model.predict(img)
    #st.write(np.argmax(result[0]))
    result = np.argmax(pred[0])
    return result

# Steamlit 

st.title('Handwritten digit Recognition')
uploaded_file = st.file_uploader("choose a file")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    result= predictDigit(image)
    st.write("digit is ",result)

# Specify canvas parameters in application
#""" drawing_mode = st.sidebar.selectbox(
    #"Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
#) """
drawing_mode = "freedraw"
#stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_width =15
stroke_color ="#FFFFFF"
bg_color = "#000000"
#""" if drawing_mode == 'point':
#    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3) 
#stroke_color = st.sidebar.color_picker("Stroke color hex: ")
#bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
#bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
#"""
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    #background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=200,
    width=200,
    drawing_mode=drawing_mode,
    #point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

# Do something interesting with the image data and paths
st.markdown("""
<style>
.big-font{
    font-size:300px !important;
}
</style>""",unsafe_allow_html=True)
path = "/media/riya/riya/BTech/6/miniproject/images"
if canvas_result.image_data is not None:
    input_numpy_array = np.array(canvas_result.image_data)
    input_image = Image.fromarray(input_numpy_array.astype('uint8'),'RGBA')
    input_image.save('user_input.png')
    img = Image.open("./user_input.png")
    res = predictDigit(img)
    st.header(res)
    st.balloons()


    #image= Image.open(canvas_result.image_data)
    #result = predictDigit(image)
    #st.write("digit is",result)
    #st.image(canvas_result.image_data)

#result.json_data["objects"]) # need to convert obj to str because PyArrow
#clude=['object']).columns:
#ype("str")
