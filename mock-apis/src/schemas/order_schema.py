"""
Schema for checkout operations.
A Checkout consists of an order, billing and shipment address.
The order object in turn has a list of products being purchased
"""
from typing import List

from pydantic import BaseModel

from ..schemas.address_schema import Address


class Product(BaseModel):
    description: str
    price: float
    quantity: int


class Order(BaseModel):
    products: List[Product]
    sub_total: float
    delivery: float
    taxes: float
    total: float


class Checkout(BaseModel):
    user_id: str
    shipment: Address
    billing: Address
    order: Order
