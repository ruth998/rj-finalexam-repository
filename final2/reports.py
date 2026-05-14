def full_inventory_report(products):
    return [p.__dict__ for p in products]


def low_stock_report(products):
    return [p for p in products if p.quantity <= p.reorder_level]


def inventory_value_report(products):
    return sum(p.quantity * p.unit_price for p in products)


def vendor_report(vendors):
    return [v.__dict__ for v in vendors]


def purchase_order_report(purchase_orders):
    return [po.__dict__ for po in purchase_orders]