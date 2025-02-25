from fastapi import HTTPException
from typing import List, TypeVar, Generic

T = TypeVar('T')


def paginate(items: List[T], page: int = 1, items_per_page: int = 10) -> List[T]:
    if page < 1:
        raise HTTPException(status_code=400, detail="Page number must be greater than 0")

    start = (page - 1) * items_per_page
    end = start + items_per_page

    return items[start:end]