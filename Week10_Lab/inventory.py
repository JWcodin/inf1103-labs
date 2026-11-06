from product import Product

# Inventory class: Responsible for managing a collection of products
class Inventory:
    def __init__(self):
        # self.products is the inventory's product collection.
        # # list means it is a list.
        # [Product] means the list is intended to contain Product objects.
        self.products: list[Product] = []

    # Add a product: adds an existing product to the inventory.
    # product: Product tells other developers that the function expects a Product object as an argument. -> None means that the function does not return any value.
    def add_product(self, product: Product) -> None:
        self.products.append(product)

    # Search for a product
    def find_product(self, product_id: str) -> Product | None: # Function can return either. A Product object, if found. None, if not found.
        for product in self.products:
            if product._product_id == product_id:
                return product
        return None

    # Remove the matching Product reference from the inventory.
    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)

        if product is not None:
            self.products.remove(product)

    # Display all products
    def display_all(self):
        print("\nCurrent Inventory")

        if not self.products:
            print("Inventory is empty.")
        else:
            for product in self.products:
                product.display_information()

        print("-" * 48)

    # Return all products for saving
    def get_products(self):
        return self.products.copy()

