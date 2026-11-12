from abc import ABC, abstractmethod


# CanBeShipped interface-style abstract base class
# Any class that promises to support shipping must provide a method for calculating the shipping cost.
# Any class that inherits from CanBeShipped must provide: calculate_shipping_cost()
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass