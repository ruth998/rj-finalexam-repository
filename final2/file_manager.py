import json
from models import Product, Vendor, PurchaseOrder


def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump([item.to_dict() for item in data], f, indent=4)


def load_products(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Product(**p) for p in data]
    except:
        return []


def load_vendors(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Vendor(**v) for v in data]
    except:
        return []


def load_po(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [PurchaseOrder(**po) for po in data]
    except:
        return []