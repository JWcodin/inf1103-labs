
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from physical_product import PhysicalProduct
from supplier import Supplier

print("\n========== TEST 1: Bulk and Percentage Discounts ==========")

# Create a supplier
supplier = Supplier("S001","ABC Technology","abc@example.com")

# Create a product worth $125
product = PhysicalProduct(
    "P001",
    "Office Chair",
    125.00,
    10,
    supplier,
    2.5
)

# Create an order with a bulk discount
order = Order("O001", BulkDiscount(200, 20))

# Add two products
order.add_order_line(product, 2)

# Calculate total with bulk discount
print("Total with bulk discount:", order.calculate_total())

# Change to 10% percentage discount
order.set_discount(PercentageDiscount(10))

# Calculate total with percentage discount
print("Total with percentage discount:", order.calculate_total())


print("\n========== TEST 2: Order and DiscountStrategy Relationship ==========")

# Create one discount strategy
shared_discount = PercentageDiscount(10)

# Create two separate orders using the same discount object
order1 = Order("O002", shared_discount)
order2 = Order("O003", shared_discount)

# Add the same product to both orders
order1.add_order_line(product, 2)
order2.add_order_line(product, 1)

# Display totals
print("Order 1 total:", order1.calculate_total())
print("Order 2 total:", order2.calculate_total())

# Check whether both orders share the same discount object
print("Both orders share the same discount:",
      order1.discount is order2.discount)