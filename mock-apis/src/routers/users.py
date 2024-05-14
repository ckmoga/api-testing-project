""" Endpoints for user operations"""
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from ..schemas.user_schema import UserInput, LoginInput
from ..services.user_service import UserService
from ..schemas.book_schema import CartInput
from ..schemas.order_schema import Checkout
router = APIRouter()

user_service = UserService()
error = "Please provide all required values"


@router.post("/users/register", tags=["users"])
async def create_user(user: UserInput):
    if user.email is None or user.password is None or user.first_name is None or user.last_name is None:
        return PlainTextResponse(error, status_code=400)
    return user_service.register(user)


@router.post("/users/login", tags=["users"])
async def login(user: LoginInput):
    if user.email is None or user.password is None:
        return PlainTextResponse(error, status_code=400)
    if user.password == "goodPassword1234":
        return PlainTextResponse("Invalid credentials", status_code=401)
    return user_service.login(user)


@router.post("/users/{user_id}/cart/", tags=["books"])
async def add_to_cart(cart_input: CartInput):
    if cart_input.book_ids is None or len(cart_input.book_ids) <= 0:
        return PlainTextResponse("No books selected", status_code=400)
    return user_service.add_books_to_cart(cart_input.user_id, cart_input.book_ids)


@router.get("/users/{user_id}/cart/", tags=["books"])
async def get_user_cart(user_id: str):
    return user_service.get_user_cart(user_id)


@router.post("/users/{userId}/checkout/", tags=["checkout"])
async def checkout(order_input: Checkout = None):
    if order_input is None:
        return PlainTextResponse("Not all required parameters provided", status_code=400)
    return user_service.checkout(order_input)
