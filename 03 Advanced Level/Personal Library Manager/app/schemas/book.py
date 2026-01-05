from pydantic import BaseModel, ConfigDict
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    read_status: str = "To Read" 


class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    read_status: Optional[str] = None

class Book(BookBase):
    id: int
    owner_id: int
    model_config = ConfigDict(from_attributes=True)