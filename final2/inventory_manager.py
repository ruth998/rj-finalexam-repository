def add_product(products, product):
    for p in products:
        if p.product_id == product.product_id:
            return products
    products.append(product)
    return products


def search_product_by_id(products, product_id):
    for p in products:
        if p.product_id == product_id:
            return p


def search_product_by_name(products, name):
    return [p for p in products if name.lower() in p.name.lower()]


def edit_product(product, name=None, category=None, quantity=None):
    if name:
        product.name = name
    if category:
        product.category = category
    if quantity is not None:
        product.quantity = quantity


def deactivate_product(product):
    product.active = False


def low_stock_products(products):
    return [p for p in products if p.quantity <= p.reorder_level]


def add_vendor(vendors, vendor):
    for v in vendors:
        if v.vendor_id == vendor.vendor_id:
            return vendors
    vendors.append(vendor)
    return vendors


def search_vendor(vendors, vendor_id):
    for v in vendors:
        if v.vendor_id == vendor_id:
            return v


def create_purchase_order(purchase_orders, po):
    purchase_orders.append(po)
    return purchase_orders


def receive_purchase_order(po, products):
    if po.status == "Received":
        return
    for item in po.items:
        for p in products:
            if p.product_id == item["product_id"]:
                p.quantity += item["quantity"]
    po.status = "Received"