from pydantic import BaseModel
from datetime import datetime

class Book(BaseModel):
    id: int
    title: str
    author_id: int
    published_date: datetime
    isbn: str
    created_at: datetime
    updated_at: datetime