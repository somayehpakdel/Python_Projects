from sqlalchemy.orm import Session
from typing import Dict

from app import models
from app.schemas import user as schemas_user
from app.crud import user as user_crud
from app.crud import book as book_crud
from app.core.security import get_password_hash, verify_password

# IMPORT THE GENERIC EXCEPTIONS (NOT HTTPException)
from app.core.exceptions import ResourceNotFoundError, AlreadyExistsError, InvalidCredentialsError

# --- Authentication Logic ---

def authenticate_user_service(db: Session, username: str, password: str) -> models.User:
    """
    Returns User if valid.
    Raises InvalidCredentialsError if username or password is wrong.
    """
    user = user_crud.get_user_by_username(db, username=username)
    if not user:
        raise InvalidCredentialsError("Incorrect username")
    
    if not verify_password(password, user.hashed_password):
        raise InvalidCredentialsError("Incorrect password")
        
    return user

# --- User Management ---

def create_user_service(db: Session, user: schemas_user.UserCreate) -> models.User:
    # 1. Check Username
    db_user = user_crud.get_user_by_username(db, username=user.username)
    if db_user:
        # We raise a generic exception. The API layer will translate this to 409.
        raise AlreadyExistsError(resource="User", identifier=user.username)
    
    # 2. Check Email
    db_email = user_crud.get_user_by_email(db, email=user.email)
    if db_email:
        raise AlreadyExistsError(resource="User", identifier=user.email)
    
    hashed_password = get_password_hash(user.password)
    return user_crud.create_user(db=db, user=user, hashed_password=hashed_password)

# --- Password Logic ---

def update_user_service(db: Session, db_user: models.User, update_data: schemas_user.UserUpdate) -> models.User:
    update_dict = update_data.model_dump(exclude_unset=True)

    if "password" in update_dict:
        if not verify_password(update_data.old_password, db_user.hashed_password):
            raise InvalidCredentialsError("Incorrect current password")
        
        update_dict["hashed_password"] = get_password_hash(update_dict.pop("password"))
        update_dict.pop("confirm_password", None)
        update_dict.pop("old_password", None)

    if "email" in update_dict:
        existing_user = user_crud.get_user_by_email(db, email=update_dict["email"])
        if existing_user and existing_user.id != db_user.id:
            raise AlreadyExistsError(resource="User", identifier=update_dict["email"])

    if "username" in update_dict:
        existing_user = user_crud.get_user_by_username(db, username=update_dict["username"])
        if existing_user and existing_user.id != db_user.id:
            raise AlreadyExistsError(resource="User", identifier=update_dict["username"])
    
    return user_crud.update_user(db=db, db_user=db_user, update_dict=update_dict)

# --- Statistics Logic ---
# (No changes needed here, no exceptions raised)

def get_user_stats_service(db: Session, user_id: int) -> schemas_user.UserStats:
    stats_data = book_crud.get_book_stats(db, owner_id=user_id)
    total = stats_data.get('total', 0)
    read = stats_data.get('read', 0)
    percentage = (read / total * 100) if total > 0 else 0.0
    return schemas_user.UserStats(
        total_books=total,
        books_read=read,
        reading_percentage=round(percentage, 2)
    )

# --- Deletion Logic ---

def delete_user_service(db: Session, user_id: int) -> None:
    db_user = user_crud.get_user(db, user_id=user_id)
    if not db_user:
        # The API layer will turn this into a 404
        raise ResourceNotFoundError(resource="User", identifier=user_id)
    
    user_crud.delete_user(db, user_id=user_id)