import streamlit as st
import pandas as pd
from utils import get_books, update_book_status, delete_book

st.set_page_config(layout="wide", page_title="Your Books")

st.header("📚 Your Books")

books_data = get_books()

if "error" in books_data:
    st.error(books_data["error"])
elif books_data:
    for book in books_data:
        col1, col2, col3, col4 = st.columns([4, 2, 2, 2])
        
        with col1:
            st.write(f"**{book['title']}** by *{book['author']}*")
        
        with col2:
            status_emoji = "✅ Read" if book['read_status'] == "read" else "📖 Unread"
            st.write(status_emoji)

        with col3:
            new_status = "unread" if book['read_status'] == "read" else "read"
            button_label = "Mark as Unread" if book['read_status'] == "read" else "Mark as Read"
            if st.button(button_label, key=f"status_{book['id']}"):
                result = update_book_status(book['id'], new_status)
                if result["success"]:
                    st.success(result["message"])
                    st.rerun()
                else:
                    st.error(result["message"])

        with col4:
            if st.button("Delete", key=f"delete_{book['id']}"):
                result = delete_book(book['id'])
                if result["success"]:
                    st.success(result["message"])
                    st.rerun()
                else:
                    st.error(result["message"])
        
        st.divider()
else:
    st.info("No books in your library. Add one using the 'Add Book' page!")