from abc import ABC, abstractmethod
from app.domain.models.book import Book

class BookRepository(ABC):
    @abstractmethod
    async def get(self, id: int) -> Book:
        pass

    @abstractmethod
    async def create(self, book: Book) -> Book:
        pass