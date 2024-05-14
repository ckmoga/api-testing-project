"""
This service class represents the business logic performed to books.
It uses the persistence layer to read/write data from the database
and reports results back to the controller/router.
For simplicity, we have stubbed the persistence layer with data factory.
NOTE: some functions may have unused parameters; this is because
we are stubbing the persistence layer and simply feed data back to the router
without any precession.
"""
from ..repository.mock_data import MockData


class BookService:
    mock = MockData()

    def __init__(self):
        pass

    # respond to book search request by feeding back a mock of 5 books
    def search_books(self, query: str):
        books = []
        for i in range(1, 6):
            books.append(self.mock.mockedBookOut)
        return {"data": books}


