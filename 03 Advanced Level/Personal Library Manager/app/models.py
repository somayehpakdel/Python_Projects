# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    isbn = Column(String, index=True)
    read_status = Column(String, default="unread")
    # This links the book to a user in the DB
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # This relationship gives us: book.owner
    owner = relationship("User", back_populates="books")
    __table_args__ = (
        UniqueConstraint('isbn', 'owner_id', name='unique_book_owner'),
    )

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # This relationship gives us: user.books
    books = relationship("Book", back_populates="owner")