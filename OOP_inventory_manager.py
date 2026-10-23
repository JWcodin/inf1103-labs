import json
import os

# 3. Data Persistence: Check whether inventory.json exists. Create load_inventory() to load inventory.json if it exists. Otherwise, begin with an empty inventory. Create save_inventory() and save data to inventory.json. 
def load_inventory():
    # Check if inventory.json exists
    if os.path.exists("inventory.json"):
        try:
            # Reads the JSON data from the file and converts it back into a Python dictionary
            with open("inventory.json", "r") as file:
                inventory = json.load(file)

            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return inventory

        # json.JSONDecodeError means the file exists but doesn't contain valid JSON.
        # FileNotFoundError means the file couldn't be found.
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error reading inventory.json.")
            print("Starting with an empty inventory.")
            # Begin with an empty inventory.
            return {} # {} represents an empty dictionary.

    else:
        print("inventory.json not found.")
        print("Starting with an empty inventory.")
        # Begin with an empty inventory.
        return {} # {} represents an empty dictionary.


# Create save_inventory() and save data to inventory.json.  
def save_inventory(inventory):
    # If the file doesn't exist, Python creates it. If it already exists, its contents are replaced with the new data.
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)  # indent=4 makes the JSON file more readable.
    print("Inventory saved successfully to inventory.json.")

# Add a new product to the inventory.
def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ")

    # Check whether ID already exists
    if product_id in inventory:
        print("Error: Product ID already exists.")
        return False

    # Get the product name.
    product_name = input("Product Name: ")

    # Validate price
    try:
        # Get the price and convert it to a float. If the input is not a valid number, it will raise a ValueError.
        price = float(input("Price: "))
    except ValueError:
        print("Error: Price must be a number.")
        return False

    # Validate stock
    try:
        # Get the stock quantity and convert it to an integer. If the input is not a valid integer, it will raise a ValueError.
        stock = int(input("Stock Quantity: "))
        if stock < 0:
            print("Error: Stock cannot be negative.")
            return False
    except ValueError:
        print("Error: Stock quantity must be an integer.")
        return False

    # Store product as a dictionary
    inventory[product_id] = { "name": product_name, 
                                 "price": price, 
                                 "stock": stock, 
                                 "transactions": [] }

    print("Product added successfully!")
    # Return True to indicate that the product was added successfully.
    return True


# Update product stock
def update_stock(inventory):
    print("\nUpdate Stock")
    # Get the product ID
    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        print("Product not found.")
        return False

    # Get the dictionary containing that product's information.
    product = inventory[product_id]

    print("Product Found:")
    print("Name:", product["name"])
    print("Current Stock:", product["stock"])

    try:
        # Asks the user for the new stock quantity and converts it to an integer.
        new_quantity = int(input("New Stock Quantity: "))

        # Check for negative stock.
        if new_quantity < 0:
            print("Error: Stock cannot be negative.")
            return False
    # Handles invalid input.
    except ValueError:
        print("Error: Stock quantity must be an integer.")
        return False

    # Record the stock transaction
    old_quantity = product["stock"]

    product["stock"] = new_quantity

    # Store transaction amount/history
    transaction_amount = new_quantity - old_quantity

    if "transactions" not in product:
        product["transactions"] = []

    product["transactions"].append(transaction_amount)

    print("Stock updated successfully!")
    return True


# Search for a product
def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")
    if product_id not in inventory:
        print("Product not found.")
        return False

    product = inventory[product_id]

    print("Product Found")
    print("-" * 48)
    print("ID:", product_id)
    print("Name:", product["name"])
    print(f"Price: ${product['price']:.2f}") # display the number as a floating-point number with exactly 2 decimal places.
    print("Stock:", product["stock"])
    print("-" * 48)

    return True


# Display all products
def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 48)

    if not inventory:
        print("Inventory is empty.")
        print("-" * 48)
        return
    # Looping through products 
    for product_id, product in inventory.items():
        print(
            f"ID: {product_id} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 48)


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

# If there is no saved inventory, create a dictonary and store at least 3 products
if not inventory:
    inventory = {
        "P001": {
            "name": "Laptop",
            "price": 1200.00,
            "stock": 15,
            "transactions": []
        },

        "P002": {
            "name": "Mouse",
            "price": 25.50,
            "stock": 40,
            "transactions": []
        },

        "P003": {
            "name": "Keyboard",
            "price": 45.00,
            "stock": 25,
            "transactions": []
        }
    }

# Main loop for the menu-driven program
while True:

    print("\n" + "=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    option = get_valid_input()

    if option == 1:
        display_all(inventory)

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

        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
