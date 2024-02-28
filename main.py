import pandas
import streamlit as st
import pandas as pd

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

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

    

