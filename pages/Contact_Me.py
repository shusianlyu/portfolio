import streamlit as st
import flask

st.header("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        message = message + user_email

