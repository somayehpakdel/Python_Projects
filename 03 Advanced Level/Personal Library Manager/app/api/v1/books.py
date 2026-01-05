from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app import models
from app.schemas import book as schemas_book
from app.database import get_db
from app.core.security import get_current_user
from app.service import book as book_service

router = APIRouter()

@router.post("/", response_model=schemas_book.Book, status_code=status.HTTP_201_CREATED)
def create_new_book(
    book: schemas_book.BookCreate, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Create a new book for the currently logged-in user.
    """
    return book_service.create_book_service(db=db, book=book, owner_id=current_user.id)

@router.get("/", response_model=List[schemas_book.Book])
def read_all_books(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Retrieve all books for the currently logged-in user.
    """
    return book_service.get_books_service(db, owner_id=current_user.id, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=schemas_book.Book)
def read_single_book(
    book_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Retrieve a specific book by ID (only if owned by user).
    """
    return book_service.get_book_service(db, book_id=book_id, owner_id=current_user.id)

@router.patch("/{book_id}", response_model=schemas_book.Book)
def update_book(
    book_id: int, 
    book_update: schemas_book.BookUpdate, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    RESTful: Use PATCH for partial updates. 
    PUT should only be used if you are replacing the entire book object.
    """
    return book_service.update_book_service(
        db, 
        book_id=book_id, 
        book_update=book_update, 
        owner_id=current_user.id
    )

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_book(
    book_id: int, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """
    Delete a specific book (only if owned by user).
    """
    book_service.delete_book_service(db, book_id=book_id, owner_id=current_user.id)
    return None