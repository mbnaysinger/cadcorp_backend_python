from pydantic import BaseModel
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author_id: int
    published_date: datetime
    isbn: str

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookInDBBase(BookBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Book(BookInDBBase):
    pass

class BookInDB(BookInDBBase):
    pass