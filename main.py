import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    original_img = Image.open("images/photo.png")
    st.image(original_img)

with col2:
    st.title("Jessie Lyu")
    content = """
    Hi, I am Jessie, a recent software engineering bachelor's 
    graduate from San Jose State University with two years of experience in 
    software development. I am highly motivated and detail-oriented 
    entry-level Software engineer with a strong foundation in programming 
    and problem-solving. My proficiency lies in languages such as Python, 
    Java, C++, C, and Javascript. I possess a solid understanding of software 
    development principles, algorithms, and data structures. Alongside my 
    technical skills, I excel in collaboration and communication, and I have a 
    passion for learning and staying updated with emerging technologies. 
    My commitment lies in delivering high-quality code and continually 
    improving software solutions. I am now actively seeking an opportunity to 
    contribute to a dynamic software development team where I can further 
    enhance my skills in software engineering.
    """
    st.info(content)
