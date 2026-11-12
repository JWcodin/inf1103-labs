from abc import ABC, abstractmethod

#DiscountStrategy class with one abstract method, apply(), that takes an order total and returns the discounted total.
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass
