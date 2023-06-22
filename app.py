import streamlit as st
import base64
import os


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
st.write("<h1 style='text-align: center;'>Automated Speech Sythesis for low resource Indian language to English</h1>", unsafe_allow_html=True)

add_bg_from_local('ssound.jpg') 
col1, col2, col3 = st.columns(3)




with col1:
    st.write("<h2 style='text-align: center;'>source</h2>", unsafe_allow_html=True)
    # for i in os.listdir('comparision/clips/'):
    #     file_path = os.path.join('comparision/clips/', i)
    #     st.audio(file_path)
    st.audio("comparision/clips/5.mp3")
    st.audio("comparision/clips/1.mp3")
    st.audio("comparision/clips/2.mp3")
    st.audio("comparision/clips/3.mp3")
    st.audio("comparision/clips/4.mp3")
    


with col3:
    st.write("<h2 style='text-align: center;'>output</h2>", unsafe_allow_html=True)
    # for i in os.listdir('comparision/output/'):
    #     file_path = os.path.join('comparision/output/', i)
    #     st.audio(file_path)
    st.audio("comparision/output/5.wav")
    st.audio("comparision/output/1.wav")
    st.audio("comparision/output/2.wav")
    st.audio("comparision/output/3.wav")
    st.audio("comparision/output/4.wav")
    
    





