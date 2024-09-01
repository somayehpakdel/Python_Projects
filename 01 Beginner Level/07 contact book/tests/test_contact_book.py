import pytest
from src.contact_book import ContactBook


@pytest.fixture()
def contact_book() -> ContactBook:
    """
    Fixture to provide a ContactBook instance for each test.

    Returns:
        ContactBook: An instance of ContactBook.
    """
    book: ContactBook = ContactBook()
    return book


def test_add_contact_success(contact_book: ContactBook, monkeypatch) -> None:
    """
    Test adding a contact successfully.

    Args:
        contact_book (ContactBook): The contact book instance.
        monkeypatch (MonkeyPatch): The monkeypatch fixture for modifying functions.

    Asserts:
        The contact is added to the contact book with the correct details.
    """

    def mock_validate_email(email):
        return True

    def mock_validate_phone_number(phone):
        return True, ""

    monkeypatch.setattr('src.utils.validate_email', mock_validate_email)
    monkeypatch.setattr('src.utils.validate_phone_number', mock_validate_phone_number)

    contact_book.add_contact("John Doe", "01234567890", "john@example.com", "123 Main St")
    
    assert "John Doe" in contact_book.contacts
    assert contact_book.contacts["John Doe"]["phone"] == "01234567890"
    assert contact_book.contacts["John Doe"]["email"] == "john@example.com"
    assert contact_book.contacts["John Doe"]["address"] == "123 Main St"
    assert contact_book.message == "Contact added successfully"


def test_add_contact_duplicate(contact_book: ContactBook, monkeypatch) -> None:
    """
    Test adding a duplicate contact.

    Args:
        contact_book (ContactBook): The contact book instance.
        monkeypatch (MonkeyPatch): The monkeypatch fixture for modifying functions.

    Asserts:
        The contact book message indicates the contact already exists.
    """

    def mock_validate_email(email):
        return True

    def mock_validate_phone_number(phone):
        return True, ""

    monkeypatch.setattr('src.utils.validate_email', mock_validate_email)
    monkeypatch.setattr('src.utils.validate_phone_number', mock_validate_phone_number)

    contact_book.add_contact("John Doe", "01234567890", "john@example.com", "123 Main St")
    contact_book.add_contact("John Doe", "0987654321", "john.doe@example.com", "456 Elm St")
    
    assert contact_book.message == "Contact already exists"


def test_add_contact_invalid_phone(contact_book: ContactBook, monkeypatch) -> None:
    """
    Test adding a contact with an invalid phone number.

    Args:
        contact_book (ContactBook): The contact book instance.
        monkeypatch (MonkeyPatch): The monkeypatch fixture for modifying functions.

    Asserts:
        The contact book message indicates the phone number is invalid.
    """

    def mock_validate_email(email):
        return True

    def mock_validate_phone_number(phone):
        return False, "Invalid phone number."

    monkeypatch.setattr('src.utils.validate_email', mock_validate_email)
    monkeypatch.setattr('src.utils.validate_phone_number', mock_validate_phone_number)

    contact_book.add_contact("John Doe", "invalid_phone", "john@example.com", "123 Main St")
    
    assert 'Invalid' in contact_book.message


def test_add_contact_invalid_email(contact_book: ContactBook, monkeypatch) -> None:
    """
    Test adding a contact with an invalid email address.

    Args:
        contact_book (ContactBook): The contact book instance.
        monkeypatch (MonkeyPatch): The monkeypatch fixture for modifying functions.

    Asserts:
        The contact book message indicates the email address is invalid.
    """
    def mock_validate_email(email):
        return False

    def mock_validate_phone_number(phone):
        return True, ""

    monkeypatch.setattr('src.utils.validate_email', mock_validate_email)
    monkeypatch.setattr('src.utils.validate_phone_number', mock_validate_phone_number)

    contact_book.add_contact("John Doe", "01234567890", "invalid_email", "123 Main St")
    
    assert 'Invalid' in contact_book.message


def test_remove_contact_success(contact_book: ContactBook, monkeypatch) -> None:
    """
    Test removing a contact successfully.

    Args:
        contact_book (ContactBook): The contact book instance.
        monkeypatch (MonkeyPatch): The monkeypatch fixture for modifying functions.

    Asserts:
        The contact is removed from the contact book and the message indicates success.
    """
    def mock_validate_email(email):
        return True

    def mock_validate_phone_number(phone):
        return True, ""

    monkeypatch.setattr('src.utils.validate_email', mock_validate_email)
    monkeypatch.setattr('src.utils.validate_phone_number', mock_validate_phone_number)

    contact_book.add_contact("Jane Doe", "01234567890", "jane@example.com", "123 Main St")
    contact_book.remove_contact("Jane Doe")
    
    assert "Jane Doe" not in contact_book.contacts
    assert contact_book.message == "Contact removed successfully"


def test_remove_contact_not_found(contact_book: ContactBook) -> None:
    """
    Test removing a contact that does not exist.

    Args:
        contact_book (ContactBook): The contact book instance.

    Asserts:
        The contact book message indicates the contact was not found.
    """
    contact_book.remove_contact("Nonexistent Contact")
    
    assert contact_book.message == "Contact not found"


def test_view_contacts_not_found(contact_book: ContactBook) -> None:
    """
    Test viewing a contact that does not exist.

    Args:
        contact_book (ContactBook): The contact book instance.

    Asserts:
        The contact book message indicates the contact was not found.
    """

    contact_book.view_contacts("Nonexistent Contact")
    
    assert contact_book.message == "Contact not found"


def test_update_contact_success(contact_book: ContactBook, monkeypatch) -> None:
    """
    Test updating a contact successfully.

    Args:
        contact_book (ContactBook): The contact book instance.
        monkeypatch (MonkeyPatch): The monkeypatch fixture for modifying functions.

    Asserts:
        The contact is updated in the contact book with the new details.
    """

    def mock_validate_email(email):
        return True

    def mock_validate_phone_number(phone):
        return True, ""

    monkeypatch.setattr('src.utils.validate_email', mock_validate_email)
    monkeypatch.setattr('src.utils.validate_phone_number', mock_validate_phone_number)

    contact_book.add_contact("John Doe", "01234567890", "john@example.com", "123 Main St")
    contact_book.update_contact("John Doe", phone="09876543210", email="newjohn@example.com")
    
    assert contact_book.contacts["John Doe"]["phone"] == "09876543210"
    assert contact_book.contacts["John Doe"]["email"] == "newjohn@example.com"
    assert contact_book.message == "Contact updated successfully"


def test_update_contact_not_found(contact_book: ContactBook):
    """
    Test updating a contact that does not exist.

    Args:
        contact_book (ContactBook): The contact book instance.

    Asserts:
        The contact book message indicates the contact was not found.
    """
    contact_book.update_contact("Nonexistent Contact", phone="0987654321")
    
    assert contact_book.message == "Contact not found"
