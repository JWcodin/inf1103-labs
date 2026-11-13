from abc import ABC, abstractmethod
from supplier import Supplier

# Product class: Responsible for managing one product
class Product(ABC): # Product inherits from ABC

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock
        self._supplier = supplier # Product constructor should accept a Supplier object, not just the supplier's name or ID

    # Properties allow other classes to access Product information.
    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def name(self) -> str:
        return self._name

    # Allow other classes to access the product price
    @property
    def price(self) -> float:
        return self._price

    # Allow other classes to access the product stock.
    @property
    def stock(self) -> int:
        return self._stock

    # Allow other classes to access the Supplier object.
    @property
    def supplier(self) -> Supplier:
        return self._supplier

    def update_stock(self, quantity: int) -> None:
        # Because the class should reject invalid stock regardless of who calls it.
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")

        self._stock = quantity

    def display_information(self) -> None:
        print("-" * 48)
        print("ID:", self._product_id)
        print("Name:", self._name)
        print(f"Price: ${self._price:.2f}")
        print("Stock:", self._stock)

        print("\nSupplier Information:")
        self._supplier.display_information()  # Display supplier information using the Supplier object

    # This means every concrete child class must provide its own version of get_fulfilment_info().
    # PhysicalProduct explains physical delivery.
    # DigitalProduct explains digital delivery.
    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    

    