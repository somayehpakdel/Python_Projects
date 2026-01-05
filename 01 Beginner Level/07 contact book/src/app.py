import streamlit as st
from src.contact_book import ContactBook
import pandas as pd
from src.utils import validate_phone_number, validate_email

# Initialize session.state
if "contact_book" not in st.session_state:
    st.session_state["contact_book"] = ContactBook()

book: ContactBook = st.session_state["contact_book"]


for bv in ['name_backup', 'phone_backup', 'email_backup', 'address_backup']:
    if bv not in st.session_state:
        st.session_state[bv] = ""

# Define utility functions
def clear_field(*args): # clear field on actions clicking

    """
    Clears the specified fields in the session state.

    Args:
        args: The fields to be cleared.
    """

    for field in args:
        if field in st.session_state:
            st.session_state[field] = ""


def show_message(book_message): # show message after actions

    """
    Displays a success or error message based on the book message.

    Args:
        book_message (str): The message from the ContactBook.
    """

    if 'successfully' in book_message:
        st.success(f'✅ {book_message}')
    else:
        st.error(f'⚠️ {book_message}')



st.image('images/banner.png')
st.title("Contact Book")
st.markdown("""
    This is a contact book application that you can use to organize your contacts.
    To view the instructions, scroll down to the **‘Instructions’** section.
    """)
st.markdown("---")

st.header("Add Contact")

# Get information from user
name = st.text_input("Name", key="name")
if name:
    st.session_state["name_backup"] = name        #save information to use after field cleaning

phone = st.text_input("Phone", key='phone')
if phone :
    st.session_state["phone_backup"] = phone #save information to use after field cleaning
    if not validate_phone_number(phone)[0]:      #validate phone number format (if not valid, show error message
        st.error(f'⚠️ {validate_phone_number(phone)[1]}')

email = st.text_input("Email", key='email')
if email:
    st.session_state["email_backup"] = email      #save information to use after field cleaning
    if not validate_email(email):
        st.error(f'⚠️ Invalid email')

address = st.text_input("Address", key='address')
if address:
    st.session_state["address_backup"] = address  #save information to use after field cleaning

col1, col2, col3 = st.columns(3)

#Add Contact
if col1.button("Add Contact", on_click=clear_field, args=('name', 'phone', 'email', 'address')):

    book.add_contact(
        name=st.session_state['name_backup'], 
        phone=st.session_state['phone_backup'],
        email=st.session_state['email_backup'],
        address= st.session_state['address_backup'])
    show_message(book.message)
    clear_field('name_backup', 'phone_backup', 'email_backup', 'address_backup')  # To make fields optional

# Remove Contact
if col2.button("Remove Contact", on_click=clear_field, args=('name')):
    book.remove_contact(name=st.session_state['name_backup'])
    show_message(book.message)


# Update Contact
if col3.button("Update Contact", args=('name', 'phone', 'email', 'address')):

    book.update_contact(
        name=st.session_state['name_backup'], 
        phone=st.session_state['phone_backup'],
        email=st.session_state['email_backup'],
        address= st.session_state['address_backup'])
    show_message(book.message)
    clear_field('name_backup', 'phone_backup', 'email_backup', 'address_backup')     # To make fields optional



# Show contacts
st.markdown("---")
st.markdown("## Contacts")
df_contacts = pd.DataFrame(book.contacts).T
if not df_contacts.empty:
    df_contacts.index.rename('Name', inplace=True)
    df_contacts.columns = ['Phone', 'Email', 'Address']
# st.table(df_contacts)
st.dataframe(df_contacts)

st.markdown("---")
st.markdown("## Instructions:")
st.markdown("""
            - Fill out the form and click "Add Contact" to add a contact.
            - You can fill in any fields you want and leave some fields blank, except for the name field.”
            - Fill in the name and information you want to update, then click "Update Contact" to update the contact.
            - Fill in the name and click "Remove Contact" to remove a contact.
            - Please note that the name field is required for any action, while other fields are optiona""")
