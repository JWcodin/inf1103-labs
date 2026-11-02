from product import Product

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
    