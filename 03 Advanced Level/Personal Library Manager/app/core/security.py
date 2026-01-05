from datetime import datetime, timedelta, timezone
from typing import Annotated, Optional

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel
from sqlalchemy.orm import Session

# --- Project Imports ---
from app.config import settings
from app.database import get_db
from app.crud import user as crud_user
# Import the SQLAlchemy User model so we can type-hint the return values correctly
from app.models import User

# --- 1. Configuration ---
password_hash = PasswordHash.recommended()

# Update tokenUrl to match your API structure
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/tokens")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# --- 2. Pydantic Models (Internal) ---
# These models help structure the data for tokens and auth flows

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


# --- 3. Password Helpers ---

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return password_hash.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Generates a JWT token.
    Updated to use timezone-aware datetime.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(db: Session, username: str, password: str) -> User | bool:
    """
    Verifies user credentials against the database.
    Returns the User object if valid, False otherwise.
    """
    user = crud_user.get_user_by_username(db, username=username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# 4. Dependencies

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Annotated[Session, Depends(get_db)]
) -> User:
    """
    Dependency that decodes the JWT, retrieves the user from DB, and returns it.
    Uses Annotated syntax for cleaner dependency injection.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    
    user = crud_user.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    """
    Dependency that ensures the user is active.
    Use this in your endpoints instead of get_current_user to enforce the check.
    """
    # Assuming your User model has 'is_active'. 
    # If you named it 'disabled' in the DB, invert the logic.
    if not current_user.is_active: 
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user