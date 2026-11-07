from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = [] # This creates an empty list that stores OrderLine objects.

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity) # Order creates its own OrderLine. The user does not need to create an OrderLine separately.
        self.order_lines.append(order_line) # The newly created order line is added to the order.

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return total