def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            # Read the total inventory
            total = int(lines[1])
            # Read the transaction history
            history = [int(value) for value in lines[3].split(",")]

            return total, history

    except FileNotFoundError:
        # No inventory file yet, so start with an empty inventory
        return 0, []

# get_valid_input(): Handles the prompt, handles input validation, and returns a valid integer or a "quit" signal. 
def get_valid_input():
    stock_quantity = input("Enter new stock quantity (or 'quit' to exit): ")

    if stock_quantity == "quit":
        return "quit"

    if not stock_quantity.isdigit():
        print("Error: Invalid input. Please enter a positive valid number.")
        return None
    else:
        return int(stock_quantity)

# process_delivery(current_total, new_value): Calculates the new total and returns it. 
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

# calculate_tax(amount): A new requirement! This function takes a delivery amount and returns the tax (10% of that specific delivery). 
def calculate_tax(amount):
    tax = amount * 0.1
    return tax

# generate_report(total_units, failed_attempts): A dedicated function to print the final summary. 
def generate_report(total_units, failed_attempts):
    print("\n--- Inventory Report ---")
    print("Total Units Processed: " + str(total_units))
    print("Number of Failed/Rejected Entries: " + str(failed_attempts))

# Initialize inventory to zero
inventory, transaction_history = load_inventory()
failed_entries = 0
deliveries_processed = 0

# Run in a continuous loop asking user to enter a stock quantity, until the user types quit. 
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

   # Keep track of the number of deliveries processed
   deliveries_processed = deliveries_processed + 1
   print("Number of deliveries processed: " + str(deliveries_processed))
   # Store the valid transaction in the transaction history
   transaction_history.append(stock_quantity)
   print("Inventory updated. Current inventory: " + str(inventory))
   print("Transaction History List: \n" + str(transaction_history) )

# Print the previously saved inventory information
print("Final Total:\n" + str(inventory))
print("Transaction History List:\n" + str(transaction_history))

# print the Total Units Processed and the Number of Failed/Rejected Entries
generate_report(inventory, failed_entries)