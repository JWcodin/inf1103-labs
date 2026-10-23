import json
import os

# Product class: Responsible for managing one product
class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        if quantity < 0:
            print("Error: Stock cannot be negative.")
            return

        self.__stock = quantity

    def display_information(self):
        print("-" * 48)
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print(f"Price: ${self.__price:.2f}")
        print("Stock:", self.__stock)
        print("-" * 48)

# Inventory class: Responsible for managing a collection of products
class Inventory:
    def __init__(self):
        self.__products = {}

    # Add a product
    def add_product(self, product):
        product_id = product._Product__product_id
        self.__products[product_id] = product

    # Search for a product
    def search_product(self, product_id):
        return self.__products.get(product_id)

    # Display all products
    def display_all(self):
        print("\nCurrent Inventory")
        print("-" * 48)

        if not self.__products:
            print("Inventory is empty.")
        else:
            for product_id, product in self.__products.items():
                print(
                    f"ID: {product_id} | "
                    f"Name: {product._Product__name} | "
                    f"Price: ${product._Product__price:.2f} | "
                    f"Stock: {product._Product__stock}"
                )

        print("-" * 48)

    # Return product IDs for saving and checking inventory
    def get_product_ids(self):
        return list(self.__products.keys())

    # Return all products for saving
    def get_products(self):
        return self.__products.copy()
    

# Data Persistence: Check whether inventory.json exists. Create load_inventory() to load inventory.json if it exists. Otherwise, begin with an empty inventory.
def load_inventory():
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

        # Convert each saved product into a Product object
        for product_id, details in saved_data.items():
            product = Product(
                product_id,
                details["name"],
                details["price"],
                details["stock"]
            )

            inventory.add_product(product)

        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory

    except (json.JSONDecodeError, FileNotFoundError, KeyError, TypeError):
        print("Error reading inventory.json.")
        print("Starting with an empty inventory.")
        return Inventory()



# Create save_inventory() and save data to inventory.json.  
def save_inventory(inventory):
    saved_data = {}

    for product_id, product in inventory.get_products().items():
        # Use the Product object's display_information method
        # for displaying, but save its attributes below.
        # Name, price and stock are accessed internally here
        # using Python's name-mangled attribute names.
        saved_data[product_id] = {
            "name": product._Product__name,
            "price": product._Product__price,
            "stock": product._Product__stock
        }

    try:
        with open("inventory.json", "w") as file:
            json.dump(saved_data, file, indent=4)

        print("Inventory saved successfully to inventory.json.")

    except OSError as error:
        print(f"Error saving inventory: {error}")

# Add a new product to the inventory.
def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ")

    if not product_id:
        print("Error: Product ID cannot be empty.")
        return

    if inventory.search_product(product_id) is not None:
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

    product = Product(product_id, name, price, stock)

    inventory.add_product(product)
    print("Product added successfully!")


# Update product stock
def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

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
def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    product.display_information()


# Menu
def get_valid_input():
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
if not inventory.get_product_ids():
    product = Product("P001", "Laptop", 1200.00, 15)
    inventory.add_product(product)

    product = Product("P002", "Mouse", 25.50, 40)
    inventory.add_product(product)

    product = Product("P003", "Keyboard", 45.00, 25)
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
