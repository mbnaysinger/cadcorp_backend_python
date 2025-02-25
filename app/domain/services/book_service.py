from app.domain.ports.book_repository import BookRepository
from app.infrastructure.schemas.book import BookCreate, BookUpdate, Book

class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    async def get_book(self, book_id: int) -> Book:
        return await self.book_repository.get(book_id)

    async def create_book(self, book: BookCreate) -> Book:
        return await self.book_repository.create(book)

    async def update_book(self, book_id: int, book: BookUpdate) -> Book:
        return await self.book_repository.update(book_id, book)

    async def delete_book(self, book_id: int) -> Book:
        return await self.book_repository.delete(book_id)

    async def list_books(self, skip: int = 0, limit: int = 100) -> list[Book]:
        return await self.book_repository.list(skip, limit)