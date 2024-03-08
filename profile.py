import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Website", page_icon="🔥", layout="wide")



st.subheader("Hi, my name is Zabrina Salau :wave:")
st.title("All About Me")
st.write("I am an enthusiastic and motivated student with a strong interest in Computer Science. I am currently in Year 12 studying Maths, Physics, Computer Science and Spanish at A-Level as well as an EPQ. In the future, I hope to study Computer Science at university")
st.write("[CLICK HERE To Learn More About Me](https://www.linkedin.com/in/zabrina-salau-a31202183/)")

st.write("---")
leftColumn, rightColumn = st.columns(2)
with leftColumn:
    st.header("Work Experience")
    st.write("##")
    st.write("Over the October Half-Term I had the privilege of participating in the Cisco Women’s Work Experience in which I gained valuable insight into the working culture of Cisco and well as the various jobs they have to offer.")
    st.write("I took part in the Springpod Software Development programme. During this course, I gained a profound understanding of the inner workings and concepts related to Software Development and the ability to successfully apply my knowledge of this sector by completing quizzes and interactive activities.")

with rightColumn:
    st.image("cisco.png")