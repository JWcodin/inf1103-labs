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