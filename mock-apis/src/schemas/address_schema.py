""" schema for address to be used for shipment and billing address
NOTE: For simplicity, we haven't added field constraints
"""
from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str = Field(...)
    city: str = Field(...)
    country: str = Field(...)
    post_code: str = Field(...)
    telephone: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
