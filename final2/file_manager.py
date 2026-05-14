import json
from models import Product, Vendor, PurchaseOrder


def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump([item.to_dict() for item in data], f, indent=4)


def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []