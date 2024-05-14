import pytest


# todo: use --env value to dynamically set base_url
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local", help="Environment name, local, dev or qa")
    parser.addoption("--base-url", action="store", default="http://127.0.0.1:8000")


def pytest_runtest_setup(item):
    print("setting up test")
    # great place to seed data and do other pre-test operations


# retrieve base url; so we can access in our tests from a single place
@pytest.fixture()
def base_url(request):
    return request.config.getoption("--base-url")

