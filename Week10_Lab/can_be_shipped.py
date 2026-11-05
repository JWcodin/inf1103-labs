from abc import ABC, abstractmethod


# CanBeShipped interface-style abstract base class
# Any class that promises to support shipping must provide a method for calculating the shipping cost.
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass