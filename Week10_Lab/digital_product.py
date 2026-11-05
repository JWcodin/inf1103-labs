from product import Product

# Create a DigitalProduct class
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size, supplier):
        super().__init__(product_id, name, price, stock, supplier)
        # download_size: the size of the downloadable product in megabytes.
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print("Download Size:", self.__download_size, "MB")
        print("Fulfilment:", self.get_fulfilment_info())

    # DigitalProduct returns a message explaining that the product is delivered digitally.
    def get_fulfilment_info(self):
        return "This product is delivered digitally."