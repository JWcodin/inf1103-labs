# 1. Initialize inventory to zero
inventory = 0
failed_entries = 0

stock_quantity = input("Enter stock quantity: ")

# 2. Run in a continuous loop asking user to enter a stock quantity, until the user types quit. 
while stock_quantity != "quit":

    # 4. and 5. Check whether the input contains positive whole numbers.
    if not stock_quantity.isdigit():
        print("Error: Invalid input. Please enter a positive valid number.")
        failed_entries = failed_entries + 1

    else:
        # 3. Accept stock values as integers
        stock_quantity = int(stock_quantity)
        # 6. Keep a running total of the inventory
        inventory = inventory + stock_quantity
        print ("Inventory updated. Current inventory: " + str(inventory))

        # 7. If the total inventory exceeds 500 units, print an alert and break the loop immediately. 
        if inventory > 500:
            print("Alert: Inventory is full.")
            break

    stock_quantity = input("Enter new stock quantity (or 'quit' to exit): ")

# 8. Reporting:When the user types quit, print the Total Units Processed and the Number of Failed/Rejected Entries.
print("\n--- Inventory Report ---")
print("Total Units Processed: " + str(inventory))
print("Number of Failed/Rejected Entries: " + str(failed_entries))