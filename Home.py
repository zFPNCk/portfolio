import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.gif", width=300)

with col2:
    st.title("Hello, My name is Nicolas")
    content = """
    I'm a student of computer science and a backend developer. I'm also a valorant player and a fan of the game. I'm also a big fan of TV shows and movies, and my favorite genre is mystery.
    """
    st.info(content)

content2 = """
Below you can find some of the app I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3 , col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], caption=row["title"])
        st.write(f"[Source Code]({row["url"]})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], caption=row["title"])
        st.write(f"[Source Code]({row["url"]})")