# app/crud.py
from sqlalchemy.orm import Session
from app import models
from app.schemas import book as schemas_book

# Standard CRUD operations
def get_book(db: Session, book_id: int, owner_id: int):
    return db.query(models.Book)\
        .filter(models.Book.id == book_id, models.Book.owner_id == owner_id)\
        .first()

def get_book_by_isbn(db: Session, isbn: str, owner_id: int):
    return db.query(models.Book)\
        .filter(models.Book.isbn == isbn, models.Book.owner_id == owner_id)\
        .first()

def get_books(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Book)\
        .filter(models.Book.owner_id == owner_id)\
        .offset(skip)\
        .limit(limit)\
        .all()

def create_book(db: Session, book: schemas_book.BookCreate, owner_id: int):
    # Convert input to dict
    book_data = book.model_dump()
    
    # Inject the owner_id into the data
    book_data["owner_id"] = owner_id
    
    db_book = models.Book(**book_data)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_update: schemas_book.BookUpdate, owner_id: int):
    db_book = db.query(models.Book)\
        .filter(models.Book.id == book_id, models.Book.owner_id == owner_id)\
        .first()
    if db_book:
        update_data = book_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int, owner_id: int):
    db_book = db.query(models.Book)\
        .filter(models.Book.id == book_id, models.Book.owner_id == owner_id)\
        .first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def get_book_stats(db: Session, owner_id: int):
    """
    Returns a dictionary with counts of book statuses.
    """
    # Count total books
    total = db.query(models.Book).filter(models.Book.owner_id == owner_id).count()
    
    # Count read books (Assuming 'read_status' has a specific value like 'Read' or 'Completed')
    # Adjust "Read" string to match whatever value you use in your Enum or DB
    read = db.query(models.Book).filter(models.Book.owner_id == owner_id, models.Book.read_status == "Read").count()
    
    return {
        "total": total,
        "read": read
    }
