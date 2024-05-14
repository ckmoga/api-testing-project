""" schema for book, cart
NOTE: For simplicity, we haven't added field constraints
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel, UUID4, Field
from .common_schemas import Status

""" book schema"""
class Book(BaseModel):
    id: UUID4
    isbn: str = Field(...)
    title: str = Field(...)
    subtitle: str = Field(...)
    description: str = Field(...)
    author: str = Field(...)
    status: Status
    price: float = Field(...)
    currency: str = Field(...)
    publisher: str = Field(...)
    publication_year: int = Field(...)
    availability: int = Field(...)


""" schema for cart item (a book in user's cart """
class CartItem(BaseModel):
    book_id: str = Field(...)
    title: str = Field(...)
    price: float = Field(...)
    currency: str = Field(...)
    quantity: int = Field(...)


""" schema for user's cart"""
class Cart(BaseModel):
    id: UUID4
    user_id: str = Field(...)
    price: float = Field(...)
    currency: str = Field(...)
    date_created: datetime
    expiry_date: datetime
    items: List[CartItem]


""" schema for adding items to user's cart"""
class CartInput(BaseModel):
    user_id: str
    book_ids: List[str]
