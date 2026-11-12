from discount_strategy import DiscountStrategy


# PercentageDiscount – takes a percentage when created and applies that percentage discount to the total.
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)