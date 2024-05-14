""" schema for book and user status"""
from pydantic import BaseModel, Field


class Status(BaseModel):
    status: int = Field(min_length=1, max_length=1)
    status_description: str = Field(min_length=1, max_length=20)
