from models import Product, Vendor, PurchaseOrder
from inventory_manager import *
from file_manager import *
from reports import *


def load_default_products():
    return [
        Product("P1", "Rice", "Food", 20, 5, 10, 3.5, "V1"),
        Product("P2", "Beans", "Food", 15, 5, 10, 2.8, "V1"),
        Product("P3", "Milk", "Dairy", 10, 3, 5, 1.9, "V2"),
        Product("P4", "Bread", "Food", 25, 5, 10, 2.0, "V1"),
        Product("P5", "Cheese", "Dairy", 12, 3, 5, 3.0, "V2"),
        Product("P6", "Yogurt", "Dairy", 18, 4, 8, 1.5, "V2"),
        Product("P7", "Eggs", "Food", 30, 6, 12, 2.5, "V3"),
        Product("P8", "Chicken", "Food", 22, 5, 10, 5.0, "V3"),
        Product("P9", "Soap", "Cleaning", 40, 10, 20, 1.2, "V4"),
        Product("P10", "Detergent", "Cleaning", 35, 8, 15, 4.5, "V4"),
        Product("P11", "Shampoo", "Cleaning", 28, 6, 12, 3.8, "V4"),
        Product("P12", "Toothpaste", "Cleaning", 50, 10, 20, 2.2, "V4"),
        Product("P13", "TV", "Electronics", 8, 2, 4, 250.0, "V5"),
        Product("P14", "Phone", "Electronics", 15, 3, 6, 500.0, "V5"),
        Product("P15", "Laptop", "Electronics", 10, 2, 5, 900.0, "V5"),
        Product("P16", "Juice", "Beverage", 30, 5, 10, 2.5, "V6"),
        Product("P17", "Water", "Beverage", 60, 10, 20, 1.0, "V6"),
        Product("P18", "Soda", "Beverage", 45, 8, 15, 1.8, "V6"),
        Product("P19", "Coffee", "Beverage", 20, 4, 8, 4.0, "V6"),
        Product("P20", "Tea", "Beverage", 22, 5, 10, 3.0, "V6"),
        Product("P21", "Sugar", "Food", 38, 8, 15, 2.0, "V1"),
        Product("P22", "Flour", "Food", 26, 6, 12, 2.8, "V1"),
        Product("P23", "Butter", "Dairy", 14, 3, 6, 3.5, "V2"),
        Product("P24", "Towels", "Cleaning", 19, 4, 8, 2.3, "V4"),
        Product("P25", "Headphones", "Electronics", 12, 3, 6, 45.0, "V5")
    ]


def load_default_vendors():
    return [
        Vendor("V1", "Fresh Foods Inc", "John Doe", "111-111-1111", "fresh@food.com", "USA"),
        Vendor("V2", "Dairy Best", "Jane Smith", "222-222-2222", "dairy@best.com", "USA"),
        Vendor("V3", "Farm Supply Co", "Mike Brown", "333-333-3333", "farm@supply.com", "USA"),
        Vendor("V4", "Clean House Supplies", "Anna Lee", "444-444-4444", "clean@house.com", "USA"),
        Vendor("V5", "Tech World", "Chris Kim", "555-555-5555", "tech@world.com", "USA"),
        Vendor("V6", "Beverage Plus", "Sarah Green", "666-666-6666", "beverage@plus.com", "USA")
    ]


def load_default_orders():
    return [
        PurchaseOrder("O1", "V1", [{"product_id": "P1", "quantity": 10}]),
        PurchaseOrder("O2", "V1", [{"product_id": "P2", "quantity": 8}]),
        PurchaseOrder("O3", "V2", [{"product_id": "P3", "quantity": 5}]),
        PurchaseOrder("O4", "V3", [{"product_id": "P7", "quantity": 12}]),
        PurchaseOrder("O5", "V4", [{"product_id": "P9", "quantity": 20}]),
        PurchaseOrder("O6", "V5", [{"product_id": "P14", "quantity": 4}]),
        PurchaseOrder("O7", "V6", [{"product_id": "P16", "quantity": 10}]),
        PurchaseOrder("O8", "V2", [{"product_id": "P5", "quantity": 6}])
    ]


def product_menu(products):
    while True:
        print("\nPRODUCT MENU")
        print("1 Add Product")
        print("2 View Products")
        print("3 Search by ID")
        print("4 Search by Name")
        print("5 Edit Product")
        print("6 Deactivate Product")
        print("7 Low Stock")
        print("8 Back")

        choice = input("Choice: ")

        if choice == "1":
            pid = input("ID: ")
            name = input("Name: ")
            cat = input("Category: ")
            qty = int(input("Qty: "))
            rl = int(input("Reorder Level: "))
            rq = int(input("Reorder Qty: "))
            price = float(input("Price: "))
            vid = input("Vendor ID: ")
            add_product(products, Product(pid, name, cat, qty, rl, rq, price, vid))

        elif choice == "2":
            for p in products:
                print(p.display())

        elif choice == "3":
            pid = input("ID: ")
            p = search_product_by_id(products, pid)
            print(p.display() if p else "Not found")

        elif choice == "4":
            name = input("Name: ")
            for p in search_product_by_name(products, name):
                print(p.display())

        elif choice == "5":
            pid = input("ID: ")
            p = search_product_by_id(products, pid)
            if p:
                p.name = input("New name: ")
                p.quantity = int(input("New qty: "))

        elif choice == "6":
            pid = input("ID: ")
            p = search_product_by_id(products, pid)
            if p:
                deactivate_product(p)

        elif choice == "7":
            for p in low_stock_products(products):
                print(p.display())

        elif choice == "8":
            break


def reports_menu(products):
    print("\nREPORTS")
    print("1 Full Inventory")
    print("2 Low Stock")
    print("3 Inventory Value")

    c = input("Choice: ")

    if c == "1":
        print(full_inventory_report(products))
    elif c == "2":
        print(low_stock_report(products))
    elif c == "3":
        print(inventory_value_report(products))


def main():
    products = load_default_products()
    vendors = load_default_vendors()
    orders = load_default_orders()

    while True:
        print("\nMAIN MENU")
        print("1 Products")
        print("2 Reports")
        print("3 Exit")

        choice = input("Choice: ")

        if choice == "1":
            product_menu(products)
        elif choice == "2":
            reports_menu(products)
        elif choice == "3":
            break


main()
