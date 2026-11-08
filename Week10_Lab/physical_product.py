
from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier


# Create a PhysicalProduct class
class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, product_id: str, name: str, price: float, stock: int, 
                 weight: float, supplier: Supplier) -> None:

        super().__init__(product_id, name, price, stock, supplier)

        # weight: the weight of the product in kilograms.
        self.__weight = weight

    # Allow other classes to access the product weight.
    @property
    def weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print("Weight:", self.__weight, "kg")
        print("Fulfilment:", self.get_fulfilment_info())
        print(f"Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    # PhysicalProduct returns a message explaining that the product requires physical shipping.
    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        # Example: $5 per kilogram
        return self.__weight * 5
