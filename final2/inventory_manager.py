def add_product(products, product):
    products.append(product)


def search_product_by_id(products, pid):
    for p in products:
        if p.product_id == pid:
            return p
    return None


def search_product_by_name(products, name):
    return [p for p in products if name.lower() in p.name.lower()]


def edit_product(product, name=None, quantity=None):
    if name:
        product.name = name
    if quantity is not None:
        product.quantity = quantity


def deactivate_product(product):
    product.active = False


def low_stock_products(products):
    return [p for p in products if p.quantity <= p.reorder_level]