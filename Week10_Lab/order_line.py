from product import Product

class OrderLine:
    # product: a reference to a Product object.
    # # quantity: the quantity of the product ordered.
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity # returns the product price multiplied by the quantity