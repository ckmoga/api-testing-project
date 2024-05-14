"""Schema for user object, login parameters and user data returned to the client"""
from typing import Optional
from pydantic import BaseModel, UUID4, Field


# we are defining all fields as optional, so we can provide cust error
# messages than default "missing" error
class UserInput(BaseModel):
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    password: Optional[str] = Field(None)


# we are defining all fields as optional, so we can provide custom error
# messages than default "missing" error
class LoginInput(BaseModel):
    email: Optional[str] = Field(None)
    password: Optional[str] = Field(None)


class UserOutput(BaseModel):
    id: UUID4
    email: str
    full_name: str
