import requests


def get_items():
    url = "http://localhost:8000/api/v1/item/"
    response = requests.get(url)
    items = response.json()
    return items


def get_item_title(item_id, items):
    for item in items:
        if item["id"] == item_id:
            return item["title"]
