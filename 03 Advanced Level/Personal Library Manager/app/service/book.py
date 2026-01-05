from sqlalchemy.orm import Session
from typing import List

from app import models
from app.schemas import book as schemas_book
from app.crud import book as book_crud

# Import the GENERIC exceptions (NOT HTTPException)
from app.core.exceptions import ResourceNotFoundError, AlreadyExistsError

def get_book_service(db: Session, book_id: int, owner_id: int) -> models.Book:
    """
    Retrieves a book by ID. 
    Raises ResourceNotFoundError if it doesn't exist or doesn't belong to the user.
    """
    db_book = book_crud.get_book(db, book_id=book_id, owner_id=owner_id)
    if not db_book:
        # The API layer will translate this to a 404 HTTP response
        raise ResourceNotFoundError(resource="Book", identifier=book_id)
    return db_book

def get_books_service(db: Session, owner_id: int, skip: int = 0, limit: int = 100) -> List[models.Book]:
    """
    Retrieves all books for a user. 
    Note: We don't raise an exception if the list is empty; an empty list is a valid response.
    """
    return book_crud.get_books(db, owner_id=owner_id, skip=skip, limit=limit)

def create_book_service(db: Session, book: schemas_book.BookCreate, owner_id: int) -> models.Book:
    """
    Creates a new book. 
    Business Rule: Checks if ISBN already exists for this user before creating.
    """
    # Check for existing book with same ISBN for this user
    existing_book = book_crud.get_book_by_isbn(db, isbn=book.isbn, owner_id=owner_id)
    if existing_book:
        # The API layer will translate this to a 409 Conflict HTTP response
        raise AlreadyExistsError(resource="Book", identifier=book.isbn)
    
    return book_crud.create_book(db=db, book=book, owner_id=owner_id)

def update_book_service(db: Session, book_id: int, book_update: schemas_book.BookUpdate, owner_id: int) -> models.Book:
    """
    Updates a book. 
    Raises ResourceNotFoundError if book not found.
    """
    db_book = book_crud.update_book(db, book_id=book_id, book_update=book_update, owner_id=owner_id)
    if not db_book:
        raise ResourceNotFoundError(resource="Book", identifier=book_id)
    return db_book

def delete_book_service(db: Session, book_id: int, owner_id: int) -> None:
    """
    Deletes a book. 
    Raises ResourceNotFoundError if book not found.
    """
    db_book = book_crud.delete_book(db, book_id=book_id, owner_id=owner_id)
    if not db_book:
        raise ResourceNotFoundError(resource="Book", identifier=book_id)