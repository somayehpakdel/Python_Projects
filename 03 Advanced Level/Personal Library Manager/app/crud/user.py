from sqlalchemy.orm import Session
from app import models
from app.schemas import user as schemas_user

def get_user_by_username(db: Session, username: str):
    """
    Get a user by their username.
    Used for: Login and Registration checks.
    """
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    """
    Get a user by their ID.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas_user.UserCreate, hashed_password: str):
    """
    Create a new user.
    Note: We expect the hashed_password to be passed from the Service layer.
    """
    db_user = models.User(
        username=user.username, 
        hashed_password=hashed_password,
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: models.User, update_dict: dict):
    """
    CRUD: Physically updates the database record.
    Accepts a pre-processed dictionary of fields to update.
    """
    for key, value in update_dict.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """
    Delete a user.
    Note: Ensure your DB Model has 'cascade' relationships set up or delete associated books manually.
    """
    db_user = get_user(db, user_id=user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user