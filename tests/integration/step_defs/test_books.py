import pytest
from pytest_bdd import scenarios, when, then, parsers
from ..utils import test_utils

# scenario files to bind to
scenarios('../features/books.feature')


# context for sharing data between
# we will use this to store API response
@pytest.fixture
def context():
    return {}


# search book and store API response in context
@when(parsers.parse("I search books for {keyword} keyword"))
def search_books_for_keyword(context, base_url, keyword):
    path = f"{base_url}/books/?query={keyword}"
    response = test_utils.get_request(path)
    context['response'] = response
    return context


@then(parsers.parse("I should get {total:d} books"))
def search_book_results(context, total):
    response = context['response']
    json = response.json()
    assert response.status_code == 200
    assert len(json["data"]) == total


@when('I search books without keyword')
def search_books_without_keyword(context, base_url):
    path = f"{base_url}/books/?query="
    response = test_utils.get_request(path)
    context['response'] = response
    return context


@then('I should get invalid request error')
def invalid_request_error(context):
    response = context['response']
    assert response.status_code == 400
    assert response.content.decode("utf-8") == "Query string not provided"



