""" End points for book operations"""
from fastapi import APIRouter, status
from fastapi.responses import PlainTextResponse
from ..services.book_service import BookService

router = APIRouter()
book_service = BookService()


@router.get("/books/", tags=["books"], status_code=status.HTTP_200_OK)
async def search_books(query: str):
    if query is None or len(query) <= 0:
        return PlainTextResponse("Query string not provided", status_code=400)
    return book_service.search_books(query)

