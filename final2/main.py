from models import Product


def load_default_products():
    return [
        Product("P1", "Rice", "Food", 20, 5, 10, 3.50, "V1"),
        Product("P2", "Beans", "Food", 15, 5, 10, 2.80, "V1"),
        Product("P3", "Milk", "Dairy", 10, 3, 5, 1.99, "V2")
    ]


def show_products(products):
    if len(products) == 0:
        print("No products available.")
        return

    for p in products:
        try:
            print(p.display())
        except:
            print(p.product_id, p.name, p.quantity)


def product_menu(products):
    while True:
        print("\nPRODUCT MENU")
        print("1 Add Product")
        print("2 View Products")
        print("3 Search Product by ID")
        print("4 Search Product by Name")
        print("5 Edit Product")
        print("6 Deactivate Product")
        print("7 Low Stock Products")
        print("8 Back")

        choice = input("Please make a choice so we know what you want: ")

        if choice == "1":
            pid = input("ID: ")
            name = input("Name: ")
            category = input("Category: ")
            quantity = int(input("Quantity: "))
            reorder_level = int(input("Reorder level: "))
            reorder_qty = int(input("Reorder qty: "))
            price = float(input("Price: "))
            vendor_id = input("Vendor ID: ")

            products.append(Product(pid, name, category, quantity, reorder_level, reorder_qty, price, vendor_id))
            print("Product added!")

        elif choice == "2":
            show_products(products)

        elif choice == "3":
            pid = input("Enter Product ID: ")
            found = None

            for p in products:
                if p.product_id == pid:
                    found = p
                    break

            if found:
                print(found.display())
            else:
                print("Product not found.")

        elif choice == "4":
            name = input("Enter Product Name: ")
            results = []

            for p in products:
                if name.lower() in p.name.lower():
                    results.append(p)

            if results:
                for p in results:
                    print(p.display())
            else:
                print("No products found.")

        elif choice == "5":
            pid = input("Enter Product ID: ")

            for p in products:
                if p.product_id == pid:
                    p.name = input("New Name: ")
                    p.quantity = int(input("New Quantity: "))
                    print("Product updated.")
                    break
            else:
                print("Product not found.")

        elif choice == "6":
            pid = input("Enter Product ID: ")

            for p in products:
                if p.product_id == pid:
                    p.active = False
                    print("Product deactivated.")
                    break
            else:
                print("Product not found.")

        elif choice == "7":
            found = False

            for p in products:
                if p.quantity <= p.reorder_level:
                    print(p.display())
                    found = True

            if not found:
                print("No low stock products.")

        elif choice == "8":
            break


def main():
    products = load_default_products()

    print("SYSTEM STARTED")

    while True:
        print("\nMAIN MENU")
        print("\n1 Add Product")
        print("2 View Products")
        print("3 Search Product by ID")
        print("4 Search Product by Name")
        print("5 Edit Product")
        print("6 Deactivate Product")
        print("7 Low Stock Products")
        print("8 Back")

        choice = input("Please make a choice so we know what you want: ")

        if choice == "1":
            product_menu(products)

        elif choice == "2":
            break


main()