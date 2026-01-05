from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List

from app import models
from app.schemas import user as schemas_user
from app.database import get_db
from app.service import user as user_service
from app.core.security import get_current_user, create_access_token, Token

router = APIRouter()

# --- Auth Resource (Separated from User Resource) ---

@router.post("/tokens", response_model=Token, tags=["Auth"])
def login_for_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    RESTful: POST to a collection of tokens to 'create' a session.
    """
    user = user_service.authenticate_user_service(db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return Token(access_token=access_token, token_type="bearer")

# --- User Resource ---

@router.post("/", response_model=schemas_user.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_data: schemas_user.UserCreate, db: Session = Depends(get_db)):
    """
    RESTful: Creating a user is a POST to the /users collection.
    """
    return user_service.create_user_service(db, user_data)

@router.get("/me", response_model=schemas_user.UserResponse)
def read_current_user(current_user: models.User = Depends(get_current_user)):
    return current_user

@router.patch("/me", response_model=schemas_user.UserResponse)
def update_current_user(
    user_update: schemas_user.UserUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    RESTful: Changing password or email is a PATCH (partial update) to the user resource.
    """
    return user_service.update_user_service(db, db_user=current_user, update_data=user_update)

@router.get("/me/statistics", response_model=schemas_user.UserStats)
def read_user_statistics(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    RESTful: Stats is a sub-resource of the user.
    """
    return user_service.get_user_stats_service(db, current_user.id)

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_current_user(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_service.delete_user_service(db, current_user.id)
    return None