from collections import defaultdict
from typing import Any, DefaultDict, Dict, Optional

from src.utils import validate_email, validate_phone_number


class ContactBook:
    """
    A class to represent a contact book.

    Attributes
    
        contacts (DefaultDict[str, Dict[str, Any]]) : A dictionary to store contacts with the contact name as the key.
        message (str) : A message attribute to store status messages. Specially for passing to streamlit.

    Methods
    
        add_contact(name, phone=None, email=None, address=None) : Adds a new contact to the contact book.
        remove_contact(name) : Removes a contact from the contact book.
        view_contacts(name) : Displays the details of a contact.
        update_contact(name, phone=None, email=None, address=None) : Updates the details of an existing contact.
    """

    def __init__(self) -> None:
        self.contacts: DefaultDict[str, Dict[str, Any]] = defaultdict(dict)
        self.message = ''  # To use in streamlit dashboard

    def add_contact(
        self,
        name: str,
        phone: Optional[str]=None,
        email: Optional[str]=None,
        address: Optional[str]=None,
        ) -> None:

        """
        Adds a new contact to the contact book.

        Args:
            name : The name of the contact.
            phone : The phone number of the contact (default is None).
            email : The email address of the contact (default is None).
            address : The address of the contact (default is None).

        Returns:
            None
        """
        if name in self.contacts:
            self.message = "Contact already exists"
            print(self.message)
            return

        if phone:
            phone_validated, message = validate_phone_number(phone)
            if not phone_validated:
                self.message = 'Contact not added.' + '\n' + message
                print(self.message)
                return

        if email and not validate_email(email) :
            self.message = 'Contact not added.' + '\n' + "Invalid email address."
            print(self.message)
            return

        self.contacts[name]["phone"] = phone
        self.contacts[name]["email"] = email
        self.contacts[name]["address"] = address
        print(self.contacts)
        self.message = "Contact added successfully"
        print(self.message)

    def remove_contact(self, name: str) -> None:
        """
        Removes a contact from the contact book.

        Args:
            name : The name of the contact to be removed.

        Returns:
            None
        """
        if name in self.contacts:
            del self.contacts[name]
            self.message = "Contact removed successfully"
            print(self.message)
        else:
            self.message = "Contact not found"
            print(self.message)

    def view_contacts(self, name: str) -> None:
        """
        Displays the details of a contact.

        Args:
            name : The name of the contact to be viewed.

        Returns:
            None
        """
        if name not in self.contacts:
            self.message = "Contact not found"
            print(self.message)
            return
        print(f'name: {name}')
        for key, item in self.contacts[name].items():
            print(f'{key}: {item}')

    def update_contact(
        self,
        name: str,
        phone: Optional[str]=None,
        email: Optional[str]=None,
        address: Optional[str]=None,
        ) -> None:
        """
        Updates the details of an existing contact.

        Args:
            name : The name of the contact to be updated.
            phone : The new phone number of the contact (default is None).
            email : The new email address of the contact (default is None).
            address : The new address of the contact (default is None).

        Returns:
            None
        """
        if name not in self.contacts:
            self.message = "Contact not found"
            print(self.message)
            return

        if phone:
            phone_validated, message = validate_phone_number(phone)
            if not phone_validated:
                self.message = 'Contact not updated.' + '\n' + message
                print(self.message)
                return
            self.contacts[name]["phone"] = phone

        if email:
            if not validate_email(email):
                self.message = 'Contact not updated.' + '\n' + "Invalid email address."
                print(self.message)
                return
            self.contacts[name]["email"] = email

        if address:
            self.contacts[name]["address"] = address
        print(self.contacts)
        self.message = "Contact updated successfully"
        print(self.message)


if __name__=='__main__':
    book = ContactBook()
    book.add_contact("John", '01234567890', "john@@example.com", "123 Main St")
    book.add_contact("Jane", '9876543210', "jane@example.com", "456 Oak Ave")
    book.view_contacts("John")
    print('---------------------')
    book.update_contact("John", phone='9876543210', email="newjohn@example.com")
    book.view_contacts("John")
    print('---------------------')
    book.remove_contact("Jane")
    print('---------------------')
    book.add_contact("John", phone='09876543210', email="newjohn@example.com")
    book.view_contacts("John")
    book.remove_contact("John")
