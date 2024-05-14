import requests


def get_request(path: str):
    response = requests.get(path)
    return response


def post_request(path: str, data):
    url = f"{path}"
    response = requests.post(url, None, data)
    return response


def get_cart_request(path: str):
    response = requests.get(path)
    return response
