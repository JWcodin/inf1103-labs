from discount_strategy import DiscountStrategy

# NoDiscount – returns the total unchanged. 
class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total