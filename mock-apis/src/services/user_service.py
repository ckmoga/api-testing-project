"""
This class contains placeholder methods for handling user login, registration, cart and checkout operations
For testing, purpose, they return dummy data from the factory, hence the input parameters
have not been used
"""
from typing import List
from ..repository.mock_data import MockData
from ..schemas.user_schema import UserInput, LoginInput
from ..schemas.order_schema import Checkout
from faker import Faker


class UserService:
    mock = MockData()
    fake = Faker()

    def __init__(self):
        pass

    def login(self, user: LoginInput):
        return self.mock.mockedUserOutput

    def register(self, user: UserInput):
        return self.mock.mockedUserOutput

        # mock adding books to cart
    def add_books_to_cart(self, user_id: str, book_ids: List[str]):
        return self.mock.get_cart_data(user_id, book_ids)

    # mock user cart
    def get_user_cart(self, user_id: str):
        book_ids = []
        for i in range(1, 6):
            book_ids.append(self.fake.uuid4())
        return {"data": self.mock.get_cart_data(user_id, book_ids)}

    # mock checkout and return order number
    def checkout(self, order_input: Checkout):
        return {"data": self.mock.order_number}
