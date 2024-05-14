import json
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from ..utils import test_utils
from pathlib import Path

# scenario files to bind to
scenarios('../features/user.feature')


# context for sharing data between
# we will use this to store API response
@pytest.fixture
def context():
    return {}


# login user and store API response in context
@when(parsers.parse("I login with email {email} and password {password}"))
def login_user(context, base_url, email, password):
    data = {
        "email": email if email != 'none' else None,
        "password": password if password != 'none' else None
    }
    response = test_utils.post_request(f"{base_url}/users/login", data)
    context['response'] = response
    return context


@then("I should receive invalid request message")
def invalid_login_error(context):
    response = context['response']
    assert response.status_code == 400
    assert response.content.decode("utf-8") == "Please provide all required values"


@then("I should receive a token")
def successful_user_login(context):
    response = context['response']
    content = response.json()
    assert response.status_code == 200
    assert content["id"] is not None
    assert content["full_name"] is not None
    assert content["token"] is not None


@then("I should receive invalid credentials error")
def invalid_credentials_error(context):
    response = context['response']
    assert response.status_code == 401
    assert response.content.decode("utf-8") == "Invalid credentials"


# register user and store API response in context
@when(parsers.parse("I register with {email}, {password}, {first_name} and {last_name}"))
def register_user(context, base_url, email, password, first_name, last_name):
    data = {
        "email": email if email != 'none' else None,
        "password": password if password != 'none' else None,
        "first_name": first_name if first_name != 'none' else None,
        "last_name": last_name if last_name != 'none' else None
    }
    response = test_utils.post_request(f"{base_url}/users/register", data)
    context['response'] = response
    return context


@given(parsers.parse('I have added these {book_ids} books to the cart'))
def add_book_to_cart(context, base_url, book_ids):
    books = json.loads(book_ids)
    context["books"] = books
    user_id = "user1234567"
    data = {
        "user_id": user_id,
        "book_ids": json.loads(book_ids)
    }
    response = test_utils.post_request(f"{base_url}/users/{user_id}/cart/", data)
    context['response'] = response
    context["user_id"] = user_id
    assert response.status_code == 200
    return context


@when("I view my cart contents")
def view_cart_contents(context, base_url):
    path = f"{base_url}/users/{context['user_id']}/cart/"
    response = test_utils.get_request(path)
    context['response'] = response
    return context


@then(parsers.parse("there should be {total:d} books"))
def verify_cart_contents(context, total):
    response = context['response']
    json = response.json()
    assert response.status_code == 200
    assert len(json["data"]) == total


@when("I checkout")
def checkout(context, base_url):
    path = f"{base_url}/users/{context['user_id']}/checkout/"
    dir_path = Path(__file__).parent
    f = open(dir_path / "../fixtures/checkout_data.json")
    data = json.load(f)
    response = test_utils.post_request(path, data)
    context['response'] = response
    return context


@then("I should receive order number")
def verify_order_number(context):
    response = context['response']
    assert response.status_code == 200
    json = response.json()
    assert json["data"] is not None


@when("I checkout without items in the cart")
def checkout(context, base_url):
    user_id = "user1234567"
    path = f"{base_url}/users/{user_id}/checkout/"
    response = test_utils.post_request(path, None)
    context['response'] = response
    print(response.content.decode("utf-8"))
    return context


@then('I should receive an error message')
def invalid_request_error(context):
    response = context['response']
    assert response.status_code == 400
