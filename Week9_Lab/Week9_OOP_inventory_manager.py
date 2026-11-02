import json
import os
from abc import ABC, abstractmethod

# Product class: Responsible for managing one product
class Product(ABC): # Product inherits from ABC
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id 
        self._name = name 
        self._price = price
        self._stock = stock

    def update_stock(self, quantity):
        if quantity < 0:
            print("Error: Stock cannot be negative.")
            return

        self._stock = quantity

    def display_information(self):
        print("-" * 48)
        print("ID:", self._product_id)
        print("Name:", self._name)
        print(f"Price: ${self._price:.2f}")
        print("Stock:", self._stock)

    @abstractmethod
    def get_fulfilment_info(self):
        pass

# CanBeShipped interface-style abstract base class
# Any class that promises to support shipping must provide a method for calculating the shipping cost.
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

# Inventory class: Responsible for managing a collection of products
class Inventory:
    def __init__(self):
        self.__products = []

    # Add a product
    def add_product(self, product):
        self.__products.append(product)

    # Search for a product
    def search_product(self, product_id):
        for product in self.__products:
            if product._product_id == product_id:
                return product
        return None  

    # Display all products
    def display_all(self):
        print("\nCurrent Inventory")

        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products: 
                product.display_information() 

        print("-" * 48)

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
        for details in saved_data:  
            product_id = details["product_id"]  
            product_type = details.get("type", "PhysicalProduct") 

            if product_type == "DigitalProduct":
                product = DigitalProduct(
                    product_id,
                    details["name"],
                    details["price"],
                    details["stock"],
                    details.get("download_size", 0)
                )

            else:
                product = PhysicalProduct(
                    product_id,
                    details["name"],
                    details["price"],
                    details["stock"],
                    details.get("weight", 0)
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
    saved_data = []

    for product in inventory.get_products():
        # Use the Product object's display_information method
        # for displaying, but save its attributes below.
        # Name, price and stock are accessed internally here
        # using Python's name-mangled attribute names.

        product_data = {  
            "product_id": product._product_id, 
            "name": product._name,
            "price": product._price,
            "stock": product._stock
        }

        if isinstance(product, PhysicalProduct):
            product_data["type"] = "PhysicalProduct"  
            product_data["weight"] = product._PhysicalProduct__weight 

        elif isinstance(product, DigitalProduct):
            product_data["type"] = "DigitalProduct" 
            product_data["download_size"] = product._DigitalProduct__download_size

        saved_data.append(product_data)

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

        product = PhysicalProduct(product_id, name, price, stock, weight)  

    elif product_type == "2":  
        try:
            download_size = float(input("Download Size (MB): "))  

            if download_size < 0:  
                print("Error: Download size cannot be negative.") 
                return

        except ValueError:
            print("Error: Enter a valid download size.")
            return

        product = DigitalProduct(product_id, name, price, stock, download_size)

    else:
        print("Error: Please select 1 or 2.")
        return

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
if not inventory.get_products():
    product = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5)
    inventory.add_product(product)

    product = PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2)
    inventory.add_product(product)

    product = DigitalProduct("P003", "E-book", 45.00, 25, 5.0)
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