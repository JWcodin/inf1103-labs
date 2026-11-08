
import json
import os

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from supplier import Supplier


# Data Persistence: Check whether inventory.json exists. Create load_inventory() to load inventory.json if it exists. Otherwise, begin with an empty inventory.

def load_inventory() -> Inventory:

    # Create an empty Inventory object
    inventory = Inventory()

    # Check if inventory.json exists
    if not os.path.exists("inventory.json"):
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        return inventory

    try:
        # Read JSON data and convert it into a Python dictionary
        with open("inventory.json", "r") as file:
            saved_data = json.load(file)

        # Empty dictionary to store Supplier objects when loading your inventory from inventory.json
        suppliers = {}

        for supplier_id, details in saved_data["suppliers"].items():

            suppliers[supplier_id] = Supplier(
                supplier_id,
                details["name"],
                details["contact_email"]
            )

        # Convert each saved product into a Product object
        for details in saved_data["products"]:

            product_id = details["product_id"]
            product_type = details.get("type", "PhysicalProduct")

            # Retrieve the existing Supplier object.
            supplier = suppliers[details["supplier_id"]]

            if product_type == "DigitalProduct":

                product = DigitalProduct(
                    product_id,
                    details["name"],
                    details["price"],
                    details["stock"],
                    details.get("download_size", 0),
                    supplier
                )

            else:

                product = PhysicalProduct(
                    product_id,
                    details["name"],
                    details["price"],
                    details["stock"],
                    details.get("weight", 0),
                    supplier
                )

            inventory.add_product(product)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

        return inventory

    except (json.JSONDecodeError, FileNotFoundError,
            KeyError, TypeError, ValueError):

        print("Error reading inventory.json.")
        print("Starting with an empty inventory.")

        return Inventory()


# Create save_inventory() and save data to inventory.json.

def save_inventory(inventory: Inventory) -> None:
    saved_data = []
    #Store Supplier objects separately to avoid duplication.
    suppliers = {}

    for product in inventory.get_products():

        # Use the Product object's display_information method
        # for displaying, but save its attributes below.

        # Use Product properties instead of internal attributes.
        product_data = {
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock,

            # Store the Supplier ID as a reference.
            "supplier_id": product.supplier.supplier_id
        }

        # Save each Supplier once.
        supplier = product.supplier

        suppliers[supplier.supplier_id] = {
            "name": supplier.name,
            "contact_email": supplier.contact_email
        }

        if isinstance(product, PhysicalProduct):

            product_data["type"] = "PhysicalProduct"
            product_data["weight"] = product.weight

        elif isinstance(product, DigitalProduct):

            product_data["type"] = "DigitalProduct"
            product_data["download_size"] = product.download_size

        saved_data.append(product_data)

    # Save Suppliers and Products together.
    inventory_data = {
        "suppliers": suppliers,
        "products": saved_data
    }

    try:
        with open("inventory.json", "w") as file:

            json.dump(inventory_data, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    except OSError as error:

        print(f"Error saving inventory: {error}")


# Add a new product to the inventory.
def add_product(inventory: Inventory) -> None:

    print("\nAdd New Product")

    product_id = input("Product ID: ")

    if not product_id:
        print("Error: Product ID cannot be empty.")
        return

    # Use find_product() from the Lab 8 Inventory class.
    if inventory.find_product(product_id) is not None:
        print("Error: Product ID already exists.")
        return

    name = input("Product Name: ").strip()

    if not name:
        print("Error: Product name cannot be empty.")
        return

    try:
        price = float(input("Price: "))

        if price < 0:
            print("Error: Price cannot be negative.")
            return

        stock = int(input("Stock Quantity: "))

        if stock < 0:
            print("Error: Stock cannot be negative.")
            return

    except ValueError:
        print("Error: Enter a valid price and whole-number stock.")
        return

    # Create a Supplier object for the new Product.
    print("\nSupplier Information")

    supplier_id = input("Supplier ID: ").strip()
    supplier_name = input("Supplier Name: ").strip()
    contact_email = input("Supplier Email: ").strip()

    if not supplier_id or not supplier_name or not contact_email:
        print("Error: Supplier information cannot be empty.")
        return

    supplier = Supplier(
        supplier_id,
        supplier_name,
        contact_email
    )

    print("\nProduct Type:")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Select product type: ")

    if product_type == "1":
        try:
            weight = float(input("Weight (kg): "))

            if weight < 0:
                print("Error: Weight cannot be negative.")
                return

        except ValueError:
            print("Error: Enter a valid weight.")
            return

        # Pass the Supplier object to PhysicalProduct.
        product = PhysicalProduct(product_id, name, price, stock, weight, supplier)

    elif product_type == "2":
        try:
            download_size = float(input("Download Size (MB): "))

            if download_size < 0:
                print("Error: Download size cannot be negative.")
                return

        except ValueError:
            print("Error: Enter a valid download size.")
            return

        # Pass the Supplier object to DigitalProduct.
        product = DigitalProduct(product_id, name, price, stock, download_size, supplier)

    else:
        print("Error: Please select 1 or 2.")
        return

    inventory.add_product(product)
    print("Product added successfully!")


# Update product stock
def update_stock(inventory: Inventory) -> None:

    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()

    # Use find_product() from the Lab 8 Inventory class.
    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    product.display_information()

    try:
        new_quantity = int(input("New Stock Quantity: "))

        if new_quantity < 0:
            print("Error: Stock cannot be negative.")
            return

    except ValueError:
        print("Error: Stock quantity must be an integer.")
        return

    product.update_stock(new_quantity)
    print("Stock updated successfully!")


# Search for a product
def search_product(inventory: Inventory) -> None:

    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()

    # Use find_product() from the Lab 8 Inventory class.
    product = inventory.find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    product.display_information()


# Menu
def get_valid_input() -> int | None:

    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    option = input("Enter option: ")

    if not option.isdigit():
        print("Error: Please enter a number from 1 to 6.")
        return None

    option = int(option)

    if option < 1 or option > 6:
        print("Error: Please enter a number from 1 to 6.")
        return None

    return option


# Initial Inventry
inventory = load_inventory()

# If there is no saved inventory, create at least 3 products
if not inventory.get_products():

    # Create a Supplier object before creating the Products.
    supplier = Supplier(
        "S001",
        "ABC Technology",
        "abc@abctechnology.com"
    )

    product = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5, supplier)

    inventory.add_product(product)

    product = PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2, supplier)

    inventory.add_product(product)

    product = DigitalProduct("P003", "E-book", 45.00, 25, 5.0, supplier)

    inventory.add_product(product)


# Main loop for the menu-driven program
while True:

    print("\n" + "=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    option = get_valid_input()

    if option == 1:
        inventory.display_all()

    elif option == 2:
        add_product(inventory)

    elif option == 3:
        update_stock(inventory)

    elif option == 4:
        search_product(inventory)

    elif option == 5:
        print("\nSaving inventory...")
        save_inventory(inventory)

    elif option == 6:
        print("\nSaving inventory before exit...")
        save_inventory(inventory)

        print("\nThank you for using Inventory Management System.")
        print("Program terminated.")
        break
