from sqlalchemy.orm import Session
from app.domain.ports.book_repository import BookRepository
from app.infrastructure.schemas.book import BookCreate, BookUpdate
from app.infrastructure.entities.book import BookEntity
from app.domain.models.book import Book

class SQLAlchemyBookRepository(BookRepository):
    def __init__(self, db: Session):
        self.db = db

    def _entity_to_model(self, entity: BookEntity) -> Book:
        return Book(
            id=entity.id,
            title=entity.title,
            author_id=entity.author_id,
            published_date=entity.published_date,
            isbn=entity.isbn,
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )

    async def get(self, id: int) -> Book:
        entity = self.db.query(BookEntity).filter(BookEntity.id == id).first()
        return self._entity_to_model(entity) if entity else None

    async def create(self, book: BookCreate) -> Book:
        db_book = BookEntity(**book.dict())
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return self._entity_to_model(db_book)

    async def update(self, id: int, book: BookUpdate) -> Book:
        db_book = self.db.query(BookEntity).filter(BookEntity.id == id).first()
        if db_book:
            update_data = book.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_book, key, value)
            self.db.commit()
            self.db.refresh(db_book)
        return self._entity_to_model(db_book) if db_book else None

    async def delete(self, id: int) -> Book:
        db_book = self.db.query(BookEntity).filter(BookEntity.id == id).first()
        if db_book:
            self.db.delete(db_book)
            self.db.commit()
        return self._entity_to_model(db_book) if db_book else None

    async def list(self, skip: int = 0, limit: int = 100) -> list[Book]:
        entities = self.db.query(BookEntity).offset(skip).limit(limit).all()
        return [self._entity_to_model(entity) for entity in entities]