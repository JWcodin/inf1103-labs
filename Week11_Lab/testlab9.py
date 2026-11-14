from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount
from physical_product import PhysicalProduct
from supplier import Supplier
from product_factory import ProductFactory
from inventory import Inventory
from Week11_OOP_inventory_manager import get_positive_float, load_products


# COMMON SETUP
supplier = Supplier(
    "S001",
    "ABC Technology",
    "abc@example.com"
)

product = PhysicalProduct(
    "P001",
    "Office Chair",
    125.00,
    10,
    supplier,
    2.5
)


# TEST 1: Bulk and Percentage Discounts
# Section 2.3
print("\n========== TEST 1: Bulk and Percentage Discounts ==========")

order = Order("O001", BulkDiscount(200, 20))

# Add two products: 125 x 2 = 250
order.add_order_line(product, 2)

print("Total with bulk discount:", order.calculate_total())

# Change discount to 10%
order.set_discount(PercentageDiscount(10))

print("Total with percentage discount:", order.calculate_total())


# TEST 2: Order and DiscountStrategy Relationship
# Section 2.4
print("\n========== TEST 2: Order and DiscountStrategy Relationship ==========")

# Create one shared discount object
shared_discount = PercentageDiscount(10)

# Create two orders using the same discount
order1 = Order("O002", shared_discount)
order2 = Order("O003", shared_discount)

order1.add_order_line(product, 2)
order2.add_order_line(product, 1)

print("Order 1 total:", order1.calculate_total())
print("Order 2 total:", order2.calculate_total())

print(
    "Both orders share the same discount:",
    order1.discount is order2.discount
)


# TEST 3: Student Discount
# Section 2.1
print("\n========== TEST 3: Student Discount ==========")

student_order = Order("O004", StudentDiscount())

student_order.add_order_line(product, 2)

print("Total with student discount:", student_order.calculate_total())


# TEST 4: ProductFactory Error Handling
# Section 3.2
print("\n========== TEST 4: ProductFactory Error Handling ==========")

try:
    invalid_product = ProductFactory.create(
        "service",
        "S002",
        "Installation Service",
        30.00,
        5,
        supplier
    )

except ValueError as error:
    print("Error:", error)

# Expected: Error: Unknown product type: service


# TEST 5: Product Stock Validation
# Section 4
print("\n========== TEST 5: Product Stock Validation ==========")

try:
    product.update_stock(-5)

except ValueError as error:
    print("Validation error:", error)


# TEST 6: Positive Number User Input
# Section 5.1
print("\n========== TEST 6: Positive Number User Input ==========")

# Test values:
# abc
# -5
# 12.50

price = get_positive_float("Enter product price: ")
print("Accepted price:", price)


# TEST 7: CSV Product Loading
# Section 5.2
print("\n========== TEST 7: CSV Product Loading ==========")

inventory = Inventory()

load_products("products.csv", inventory, supplier)


# TEST 8: CSV File Not Found
# Section 5.2
print("\n========== TEST 8: CSV File Not Found ==========")

missing_inventory = Inventory()

load_products("missing_products.csv", missing_inventory, supplier)


# TEST 9: Invalid Product Price - checks that the Product constructor rejects a zero or negative price.
print("\n========== TEST 9: Invalid Product Price ==========")

try:
    invalid_product = PhysicalProduct(
        "P002",
        "Invalid Product",
        -10.00,
        5,
        supplier,
        2.0
    )

except ValueError as error:
    print("Price validation error:", error)


# Test 10: Invalid stock quantity
print("\n========== TEST 10: Invalid Stock Quantity ==========")

try:
    invalid_product = PhysicalProduct(
        "P003",
        "Invalid Stock Product",
        50.00,
        -5,
        supplier,
        2.0
    )

except ValueError as error:
    print("Stock validation error:", error)


# Test 11: Invalid order quantity - Checks that an order line rejects zero or negative quantities.
print("\n========== TEST 11: Invalid Order Quantity ==========")

try:
    order.add_order_line(product, -2)

except ValueError as error:
    print("Order quantity validation error:", error)


# Test 12: Valid product creation through ProductFactory
print("\n========== TEST 12: Valid ProductFactory Creation ==========")

factory_product = ProductFactory.create(
    "physical",
    "P004",
    "Factory Created Chair",
    125.00,
    10,
    supplier,
    weight=2.5
)

print("Product created:", factory_product.name)
print("Product type:", type(factory_product).__name__)
