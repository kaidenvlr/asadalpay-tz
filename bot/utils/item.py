import requests


def get_items():
    url = "http://localhost:8000/api/v1/item/"
    response = requests.get(url)
    items = response.json()
    return items
