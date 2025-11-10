from pydantic import BaseModel

class BookModel(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    publishedYear: int
    pages: int

class UpdateBookModel(BaseModel):
    title: str
    author: str
    genre: str
    pages: int