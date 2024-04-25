import dotenv
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

import streamlit as st
from google import generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input,image):
    if input:
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(['named fruits and vegetables in this image',image])
        # response=model.generate_content(image)
    return response.text

## initializing the streamlit app
st.set_page_config(page_title=" Fruits and Vegetables",page_icon='icon.png')

st.header("Fruits and Vegetables")
# st.write("upload any image to detect fruits and vegetable in it")

input=st.text_input("if you want to instruct any customize command then you can also write here:(Optional) ",key="input")
inp2 = "name only those fruits and vegetables in this image"
upload_file = st.file_uploader("upload any image to detect fruits and vegetable in it...", type=['jpg','png'])
image=''
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image,caption="uploaded image")

submit=st.button("submit")
if submit:
    response= get_gemini_response(input,image)
    # st.subheader("The response is ")
    st.write(response)

# to add background image
# import base64
# def set_bg_hack(main_bg):
#     '''
#     A function to unpack an image from root folder and set as bg.
 
#     Returns
#     -------
#     The background.
#     '''
#     # set bg name
# main_bg_ext = "jpg"
        
# st.markdown(
#      f"""
#      <style>
#      .stApp {{
#          background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open('bg.jpg', "rb").read()).decode()});
#          background-size:cover;
#          opacity:0.6;
         
#      }}
#      </style>
#      """,
#      unsafe_allow_html=True
#  )
