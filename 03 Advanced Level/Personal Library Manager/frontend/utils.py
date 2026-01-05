import requests
from config import settings


# --- Helper Functions to talk to the API ---
def get_books():
    """Fetches all books from the API."""
    try:
        response = requests.get(f"{settings.API_URL}/books/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # We'll let the calling page handle the error display
        return {"error": f"Error fetching books: {e}"}

def add_book(title, author, isbn):
    """Adds a new book via the API."""
    book_data = {"title": title, "author": author, "isbn": isbn}
    try:
        response = requests.post(f"{settings.API_URL}/books/", json=book_data)
        response.raise_for_status()
        return {"success": True, "message": "Book added successfully!"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "message": f"Error adding book: {e}"}

def update_book_status(book_id, new_status):
    """Updates a book's read status via the API."""
    update_data = {"read_status": new_status}
    try:
        response = requests.put(f"{settings.API_URL}/books/{book_id}", json=update_data)
        response.raise_for_status()
        return {"success": True, "message": "Book status updated!"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "message": f"Error updating book: {e}"}

def delete_book(book_id):
    """Deletes a book via the API."""
    try:
        response = requests.delete(f"{settings.API_URL}/books/{book_id}")
        response.raise_for_status()
        return {"success": True, "message": "Book deleted!"}
    except requests.exceptions.RequestException as e:
        return {"success": False, "message": f"Error deleting book: {e}"}
