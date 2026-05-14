from models import Product, Vendor, PurchaseOrder
from inventory_manager import *
from file_manager import *
from reports import *


def load_default_products():
    return [
        Product("P1", "Rice", "Food", 20, 5, 10, 3.5, "V1"),
        Product("P2", "Beans", "Food", 15, 5, 10, 2.8, "V1"),
        Product("P3", "Milk", "Dairy", 10, 3, 5, 1.9, "V2")
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