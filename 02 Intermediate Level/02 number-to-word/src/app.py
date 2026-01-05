import streamlit as st
from src.number_to_word import number_to_word_english, number_to_word_farsi

st.title("Number to Word Converter")

col = st.columns(3)
num = col[0].number_input("Enter a number", value=0, step=1, max_value=999999999999, format="%d")
language = col[0].selectbox("Select Language", ["English", "Farsi"])


if language == "English":
    st.success(number_to_word_english(int(num)))
elif language == "Farsi":
    st.success(number_to_word_farsi(int(num)))
st.markdown("""
    **About**:
    - This app converts numbers to their word representation.
    - This app supports up to 12 digits""")

