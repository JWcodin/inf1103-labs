from product import Product
from supplier import Supplier


# Create a DigitalProduct class
class DigitalProduct(Product):

    def __init__(self, product_id: str, name: str,
                 price: float, stock: int,
                 download_size: float, supplier: Supplier) -> None:

        super().__init__(product_id, name, price, stock, supplier)

        # download_size: the size of the downloadable product in megabytes.
        self.__download_size = download_size

    # Allow other classes to access the download size.
    @property
    def download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print("Download Size:", self.__download_size, "MB")
        print("Fulfilment:", self.get_fulfilment_info())

    # DigitalProduct returns a message explaining that the product is delivered digitally.
    def get_fulfilment_info(self) -> str:
        return "This product is delivered digitally."
