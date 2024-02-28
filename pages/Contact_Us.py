import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("your email address")
    message = st.text_area("your message")
    button = st.form_submit_button("submit")
    if button:
        print("I was pressed!")