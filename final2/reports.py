def full_inventory_report(products):
    return [p.display() for p in products]


def low_stock_report(products):
    return [p.display() for p in products if p.quantity <= p.reorder_level]


def inventory_value_report(products):
    total = sum(p.quantity * p.unit_price for p in products)
    return f"Total Inventory Value: ${total:.2f}"


def products_by_category(products, category):
    return [p.display() for p in products if p.category == category]