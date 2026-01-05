import streamlit as st

st.set_page_config(layout="wide", page_title="Personal Library")

st.title("📚 Personal Library Manager")
st.sidebar.success("Select a demo above.")
st.markdown("""
Welcome to your personal library! Use the sidebar on the left to navigate:
- **Your Books:** View, update, and delete books in your collection.
- **Add Book:** Add a new book to your library.
""")