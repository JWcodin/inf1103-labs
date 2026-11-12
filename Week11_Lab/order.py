from product import Product
from order_line import OrderLine

from discount_strategy import DiscountStrategy
from no_discount import NoDiscount


class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy = None) -> None: # The discount is optional. If no discount is provided, the default is NoDiscount.
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = [] # This creates an empty list that stores OrderLine objects.

        if discount is None:
            self.discount = NoDiscount() # If no discount strategy is provided, use NoDiscount as the default.
        else:
            self.discount = discount # If a discount strategy is provided, use it.

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity) # Order creates its own OrderLine. The user does not need to create an OrderLine separately.
        self.order_lines.append(order_line) # The newly created order line is added to the order.

    # set_discount() method allows you to change the discount after the order has been created. It takes a DiscountStrategy object as an argument and sets the order's discount to that strategy.
    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    # calculate_total() adds up the order line subtotals and passes the result to the strategy’s apply() method. 
    def calculate_total(self) -> float:
        total = 0.0

        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()

        return self.discount.apply(total)