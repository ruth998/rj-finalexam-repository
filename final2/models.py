class Product:
    def __init__(self, product_id, name, category, quantity, reorder_level, reorder_quantity, unit_price, vendor_id, active=True):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.reorder_level = reorder_level
        self.reorder_quantity = reorder_quantity
        self.unit_price = unit_price
        self.vendor_id = vendor_id
        self.active = active

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

    def to_dict(self):
        return self.__dict__


class PurchaseOrder:
    def __init__(self, po_number, vendor_id, date_created, items, total_cost, status="Pending"):
        self.po_number = po_number
        self.vendor_id = vendor_id
        self.date_created = date_created
        self.items = items
        self.total_cost = total_cost
        self.status = status

    def to_dict(self):
        return self.__dict__