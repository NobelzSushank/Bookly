from fastapi import status, APIRouter, Depends
from src.books.schemas import BookModel, UpdateBookModel, CreateBookModel
from .models import Book
from src.db.main import get_session
from .service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException


book_router = APIRouter()
book_service = BookService()

@book_router.get("/", response_model= list[BookModel])
async def getAllBook(session:AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=BookModel)
async def createBook(book_data: CreateBookModel, session:AsyncSession = Depends(get_session)) -> dict:
    new_book =  await book_service.create_book(book_data, session)    
    return new_book;

@book_router.get("/{book_uid}", response_model=BookModel)
async def getBook(book_uid: str, session:AsyncSession = Depends(get_session)):
    book = await book_service.get_book(book_uid, session)

    if book is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= "Book not found"
        )
    else:
        return book
        
    

@book_router.patch("/{book_uid}")
async def updateBook(book_uid: str, book_data: UpdateBookModel, session:AsyncSession = Depends(get_session)):
    update_book = await book_service.update_book(book_uid, book_data, session)
    
    if update_book is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= "Book not found"
        )
        
    else:
        return update_book
        

@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteBook(book_uid: str, session:AsyncSession = Depends(get_session)):
    book_to_delete = await book_service.delete_book(book_uid, session)

    if book_to_delete is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail= "Book not found"
        )
    else:
        return {}
        