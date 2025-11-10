from pydantic import BaseModel
from datetime import datetime, date
import uuid

class BookModel(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    genre: str
    publisher: str
    published_date: date
    language: str
    pages: int
    created_at: datetime
    updated_at: datetime

class CreateBookModel(BaseModel):
    title: str
    author: str
    genre: str
    publisher: str
    published_date: str
    language: str
    pages: int

class UpdateBookModel(BaseModel):
    title: str
    author: str
    genre: str
    pages: int