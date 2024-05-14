"""
This class contains dummy data that we will be returned to router
instead of implementing actual repository later
This code should eventually be moved to test folder and be used
for seeding database for testing purpose.
"""
from typing import List

from faker import Faker

from ..schemas.address_schema import Address
from ..schemas.book_schema import Book, Cart
from ..schemas.order_schema import Product, Order
from ..schemas.user_schema import UserOutput


class MockData:
    fake = Faker()
    # mocked user data
    mockedUserOutput: UserOutput = {
        "id": fake.uuid4(),
        "full_name": fake.name(),
        "token": fake.uuid4()
    }

    # mock single book data
    mockedBookOut: Book = {
        "id": fake.uuid4(),
        "isbn": fake.text(20),
        "title": fake.text(20),
        "subtitle": fake.text(20),
        "description": fake.text(20),
        "author": fake.name(),
        "status": {"status": 1, "status_description": "Available"},
        "price": fake.pyfloat(),
        "currency": "USD",
        "publisher": fake.company(),
        "publication_year": fake.year(),
        "availability": fake.pyint()
    }

    # mock cart data
    mockedCartItem: Cart = {
        "book_id": fake.uuid4(),
        "isbn": fake.text(20),
        "title": fake.text(20),
        "price": fake.pyfloat(),
        "currency": "USD",
        "quantity": fake.pyint(),
        "date_created": fake.date(),
        "expiry_date": fake.date()
    }

    # mocked user cart data
    def get_cart_data(self, user_id: str, book_ids: List[str]):
        results = []
        cart_id = self.fake.uuid4()
        for book_id in book_ids:
            item = self.mockedCartItem
            # overwrite automatically generated user_id and book_id
            item["user_id"] = user_id
            item["book_id"] = book_id
            # add cart_id to every item
            item["id"] = cart_id
            results.append(item)
        return results

    order_number = fake.uuid4()

    mockedAddress: Address = {
        "street": fake.street_name(),
        "city": fake.city(),
        "country": fake.country(),
        "post_code": fake.zipcode(),
        "telephone": fake.phone_number(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name()
    }

    mockedProduct: Product = {
        "description": fake.text(),
        "price": fake.pyfloat(),
        "quantity": fake.pyint()
    }

    mockedOrder: Order = {
        "sub_total": fake.pyfloat(),
        "delivery": fake.pyfloat(),
        "taxes": fake.pyfloat(),
        "total": fake.pyfloat()
    }

    def get_checkout_data(self):
        results = {}
        products = []
        for i in range(1, 6):
            products.append(self.mockedProduct)
        order = self.mockedOrder
        order["products"] = products
        results["order"] = order
        results["shipment"] = self.mockedAddress
        results["delivery"] = self.mockedAddress
        print(results)
        return results
