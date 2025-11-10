from fastapi import status, APIRouter
from src.books.schemas import BookModel, UpdateBookModel
from src.books.book_data import books

book_router = APIRouter()

@book_router.get("/", response_model= list[BookModel])
async def getAllBook():
    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def createBook(book_data: BookModel) -> dict:
    new_book =  book_data.model_dump();
    books.append(new_book)
    return new_book;

@book_router.get("/{book_id}")
async def getBook(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book;
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail= "Book not found"
    )
    

@book_router.patch("/{book_id}")
async def updateBook(book_id: int, book_data: UpdateBookModel):
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_data.title
            book["author"] = book_data.author
            book["genre"] = book_data.genre
            book["pages"] = book_data.pages
            return book
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail= "Book not found"
    )

@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteBook(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail= "Book not found"
    )