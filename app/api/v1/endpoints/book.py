from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.infrastructure.schemas.book import Book, BookCreate, BookUpdate
from app.domain.services.book_service import BookService
from app.infrastructure.repositories.book_repository import SQLAlchemyBookRepository
from app.utils.pagination import paginate

router = APIRouter()

def get_book_service(db: Session = Depends(get_db)):
    return BookService(SQLAlchemyBookRepository(db))

@router.post("/", response_model=Book)
async def create_book(book: BookCreate, service: BookService = Depends(get_book_service)):
    return await service.create_book(book)

@router.get("/{book_id}", response_model=Book)
async def read_book(book_id: int, service: BookService = Depends(get_book_service)):
    book = await service.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=Book)
async def update_book(book_id: int, book: BookUpdate, service: BookService = Depends(get_book_service)):
    updated_book = await service.update_book(book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}", response_model=Book)
async def delete_book(book_id: int, service: BookService = Depends(get_book_service)):
    deleted_book = await service.delete_book(book_id)
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book

@router.get("/", response_model=list[Book])
async def list_books(
    service: BookService = Depends(get_book_service),
    page: int = 1,
    items_per_page: int = 10
):
    books = await service.list_books()
    return paginate(books, page, items_per_page)