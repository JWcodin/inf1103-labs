# Product class: Responsible for managing one product
class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        if quantity < 0:
            print("Error: Stock cannot be negative.")
            return

        self.__stock = quantity

    def display_information(self):
        print("-" * 48)
        print("ID:", self.__product_id)
        print("Name:", self.__name)
        print(f"Price: ${self.__price:.2f}")
        print("Stock:", self.__stock)
        print("-" * 48)
