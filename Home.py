import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    img = Image.open("images/photo.png")
    st.image(img)

with col2:
    st.title("Jessie Lyu")
    content = """
    Hi, I am Jessie, a recent computer science bachelor's 
    graduate from San Jose State University with two years of experience in 
    software development. I am highly motivated and detail-oriented 
    entry-level Software engineer with a strong foundation in programming 
    and problem-solving. My proficiency lies in languages such as Python, 
    Java, C++, C, and Javascript. I possess a solid understanding of software 
    development principles, algorithms, and data structures. I have a 
    passion for learning and staying updated with emerging technologies. 
    My commitment lies in delivering high-quality code and continually 
    improving software solutions. I am now actively seeking an opportunity to 
    contribute to a dynamic software development team where I can further 
    enhance my skills in software engineering.
    """
    st.info(content)

st.write(
    """<style>
    [data-testid="stHorizontalBlock"] {
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

content2 = """
Below you can find some of the apps I have built in Python. 
Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

data = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")