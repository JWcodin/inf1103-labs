from discount_strategy import DiscountStrategy


# BulkDiscount – takes a threshold and an amount, e.g. BulkDiscount(200, 20) takes 20 off any total of 200 or more. 
class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float):
        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        if total >= self.threshold: # Total more than or equal to threshold, apply discount
            return total - self.amount
        return total