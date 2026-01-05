import streamlit as st
from utils import add_book

st.set_page_config(page_title="Add a New Book")

st.header("➕ Add a New Book")

with st.form("add_book_form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    isbn = st.text_input("ISBN")
    submitted = st.form_submit_button("Add Book")
    
    if submitted:
        if title and author and isbn:
            result = add_book(title, author, isbn)
            if result["success"]:
                st.success(result["message"])
                # Clear the form by resetting the session state variables
                st.session_state.title = ""
                st.session_state.author = ""
                st.session_state.isbn = ""
                st.rerun()
            else:
                st.error(result["message"])
        else:
            st.warning("Please fill in all fields.")
