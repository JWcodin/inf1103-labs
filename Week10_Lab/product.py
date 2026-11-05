from abc import ABC, abstractmethod
from supplier import Supplier

# Product class: Responsible for managing one product
class Product(ABC): # Product inherits from ABC
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self._product_id = product_id 
        self._name = name 
        self._price = price
        self._stock = stock
        self._supplier = supplier # Product constructor should accept a Supplier object, not just the supplier's name or ID

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

        print("\nSupplier Information:")
        self._supplier.display_information()  # Display supplier information using the Supplier object

    @abstractmethod
    def get_fulfilment_info(self):
        pass
    

    