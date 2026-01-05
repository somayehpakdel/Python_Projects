from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator
from typing import Optional
from datetime import datetime



class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    is_active: bool = True
    created_at: datetime 
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=8)
    confirm_password: Optional[str] = Field(None, min_length=8)
    old_password: Optional[str] = None

    @model_validator(mode='after')
    def validate_password_logic(self):
        # If user is trying to update password
        if self.password is not None:
            if self.password != self.confirm_password:
                raise ValueError("New passwords do not match")
            if self.old_password is None:
                raise ValueError("Old password is required to set a new password")
        return self

class UserStats(BaseModel):
    total_books: int
    books_read: int
    reading_percentage: float # e.g. 85.5

class Token(BaseModel):
    access_token: str
    token_type: str