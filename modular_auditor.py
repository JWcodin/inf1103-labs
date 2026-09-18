# 1. get_valid_input(): Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal. 
def get_valid_input():
    stock_quantity = input("Enter new stock quantity (or 'quit' to exit): ")

    if stock_quantity == "quit":
        return "quit"

    if not stock_quantity.isdigit():
        print("Error: Invalid input. Please enter a positive valid number.")
        return None
    else:
        return int(stock_quantity)

# 2. process_delivery(current_total, new_value): Calculates the new total and returns it. 
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

# 3. calculate_tax(amount): A new requirement! This function takes a delivery amount and returns the tax (10% of that specific delivery). 
def calculate_tax(amount):
    tax = amount * 0.1
    return tax

# Initialize inventory to zero
inventory = 0
failed_entries = 0

#Run in a continuous loop asking user to enter a stock quantity, until the user types quit. 
while True:

   stock_quantity = get_valid_input()
   
   if stock_quantity == "quit":
        break

   if stock_quantity is None:
        failed_entries = failed_entries + 1
        continue

   # Process the valid delivery
   inventory = process_delivery(inventory, stock_quantity)
   print ("Inventory updated. Current inventory: " + str(inventory))

   # Calculate the tax for this specifc delivery
   tax = calculate_tax(stock_quantity)
   print("Tax for this delivery: " + str(tax))

# 8. Reporting: When the user types quit, print the Total Units Processed and the Number of Failed/Rejected Entries.
print("\n--- Inventory Report ---")
print("Total Units Processed: " + str(inventory))
print("Number of Failed/Rejected Entries: " + str(failed_entries))