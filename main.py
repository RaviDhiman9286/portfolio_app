import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/mypic.jpg", width=650)
with col2:
    st.title("Ravi Dhiman")
    content = """
    Hi, I am Ravi Dhiman! I am Python programmer. I graduated in 2013 with B-Tech in ECE.
    I have worked with companies starting from Utopia Mobile India Pvt Ltd, then with Gemalto India Pvt ltd ,
    and now currently working with Thales DIS India Pvt Ltd"""
    st.info(content)

content2 = """
Below you can find the apps I have built in python. Feel Free to contact me."""
st.write(content2)

    

