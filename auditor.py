# 1. Initialize inventory to zero
inventory = 0
failed_entries = 0

stock_quantity = input("Enter stock quantity: ")

# 2. Run in a continuous loop asking user to enter a stock quantity, until the user types quit. 
while stock_quantity != "quit":

    # 4. and 5. Check whether the input contain positive whole number digits
    if not stock_quantity.isdigit():
        print("Error: Invalid input. Please enter a positive valid number.")
        failed_entries = failed_entries + 1

    else:
        # 3. Accept stock values as integers
        stock_quantity = int(stock_quantity)
        inventory = inventory + stock_quantity
        print("Current inventory: " + str(inventory))


    stock_quantity = input("Enter new stock quantity (or 'quit' to exit): ")