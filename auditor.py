# 1. Initialize inventory to zero
inventory = 0

stock_quantity = input("Enter stock quantity: ")

# 2. Run in a continuous loop asking user to enter a stock quantity, until the user types quit. 
while stock_quantity != "quit":
    inventory = inventory + int(stock_quantity)
    print("Current inventory: " + str(inventory))

    stock_quantity = input("Enter new stock quantity (or 'quit' to exit): ")