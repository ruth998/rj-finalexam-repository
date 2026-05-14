import datetime


class Product:
    def __init__(self, product_id, name, category, quantity, reorder_level, reorder_qty, unit_price, vendor_id, active=True):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.reorder_level = reorder_level
        self.reorder_qty = reorder_qty
        self.unit_price = unit_price
        self.vendor_id = vendor_id
        self.active = active

    def display(self):
        return f"{self.product_id} | {self.name} | {self.category} | Qty: {self.quantity} | Price: {self.unit_price}"

    def to_dict(self):
        return self.__dict__


class Vendor:
    def __init__(self, vendor_id, name, contact, phone, email, address):
        self.vendor_id = vendor_id
        self.name = name
        self.contact = contact
        self.phone = phone
        self.email = email
        self.address = address

    def display(self):
        return f"{self.vendor_id} | {self.name} | {self.phone}"

    def to_dict(self):
        return self.__dict__


class PurchaseOrder:
    def __init__(self, po_number, vendor_id, items):
        self.po_number = po_number
        self.vendor_id = vendor_id
        self.items = items
        self.status = "Pending"
        self.date = str(datetime.date.today())
        self.total_cost = 0

    def calculate_total(self, products):
        total = 0
        for item in self.items:
            for p in products:
                if p.product_id == item["product_id"]:
                    total += p.unit_price * item["quantity"]
        self.total_cost = total
        return total

    def to_dict(self):
        return self.__dict__