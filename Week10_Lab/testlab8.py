from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from product import Product


# TEST 1: ASSOCIATION
print("\n========== TEST 1: ASSOCIATION ==========")

# 1. Create a Supplier object
supplier1 = Supplier(
    "S001",
    "ABC Technology",
    "abc@example.com"
)


# 2. Create a PhysicalProduct using that Supplier
physical_product = PhysicalProduct(
    "P001",
    "Laptop",
    1200.00,
    10,
    2.5,
    supplier1
)


# 3. Create a DigitalProduct using the same Supplier
digital_product = DigitalProduct(
    "P002",
    "E-book",
    25.00,
    100,
    50,
    supplier1
)

# 4. Display both products and their supplier information
print("\n--- PHYSICAL PRODUCT ---")
physical_product.display_information()

print("\n--- DIGITAL PRODUCT ---")
digital_product.display_information()


# 5. Confirm Supplier and Products are separate objects
print("\n--- CHECKING OBJECT RELATIONSHIPS ---")

print(
    "Supplier and PhysicalProduct are separate objects:",
    supplier1 is not physical_product
)

print(
    "Supplier and DigitalProduct are separate objects:",
    supplier1 is not digital_product
)

print(
    "Both Products share the same Supplier object:",
    physical_product.supplier is digital_product.supplier
)


# Predict what happens when supplier1 is deleted
print("\n--- DELETING SUPPLIER VARIABLE ---")

print("Deleting supplier1...")
# del supplier1 only removes the variable called supplier1. It does not destroy the supplier object because the products still refer to it.
del supplier1


# Check whether PhysicalProduct can still access Supplier
print("\n--- PHYSICAL PRODUCT AFTER DELETION ---")
physical_product.display_information()


# Check whether DigitalProduct can still access Supplier
print("\n--- DIGITAL PRODUCT AFTER DELETION ---")
digital_product.display_information()


# TEST 2: AGGREGATION
print("\n========== TEST 2: AGGREGATION ==========")

# 1. Create a Supplier
supplier2 = Supplier(
    "S002",
    "XYZ Electronics",
    "xyz@example.com"
)

# 2. Create a Product BEFORE adding it to any Inventory
product = PhysicalProduct(
    "P003",
    "Keyboard",
    80.00,
    20,
    0.8,
    supplier2
)

print("\n--- PRODUCT BEFORE ADDING TO INVENTORY ---")
product.display_information()

# 3. Create Inventory A and Inventory B
inventory_a = Inventory()
inventory_b = Inventory()

# 4. Add the Product to Inventory A
print("\n--- ADDING PRODUCT TO INVENTORY A ---")
inventory_a.add_product(product)

# 5. Remove the Product from Inventory A
print("\n--- REMOVING PRODUCT FROM INVENTORY A ---")
inventory_a.remove_product(product.product_id)

# 6. Check whether the Product can still be used
print("\n--- PRODUCT AFTER REMOVAL FROM INVENTORY A ---")
product.display_information()

# 7. Add the SAME Product object to Inventory B
print("\n--- ADDING SAME PRODUCT TO INVENTORY B ---")
inventory_b.add_product(product)

# 8. Check whether the Product exists in Inventory B
print("\n--- CHECKING INVENTORY B ---")
found_product = inventory_b.find_product("P003")

# 9. The same product has moved from one inventory to another.
print("Product successfully added to Inventory B:",
      found_product is product)

# 10. Check that Inventory A no longer contains the Product
print("\n--- CHECKING INVENTORY A ---")
removed_product = inventory_a.find_product("P003")

print("Product removed from Inventory A:",
      removed_product is None)

# 11. Check that the Product still works
print("\n--- FINAL PRODUCT CHECK ---")
product.display_information()


# TEST 3: COMPOSITION
print("\n========== TEST 3: COMPOSITION ==========")

# 1. Create two Products
supplier3 = Supplier(
    "S003",
    "Tech World",
    "tech@example.com"
)

product1 = PhysicalProduct(
    "P004", "Mouse", 30.00, 20, 0.5, supplier3
)

product2 = DigitalProduct(
    "P005", "Antivirus Software", 50.00, 100, 200, supplier3
)

# 2. Create the first Order
order1 = Order("O001")

# 3. Add two Products to the first Order using add_order_line()
order1.add_order_line(product1, 2)
order1.add_order_line(product2, 1)

# 4. Display the first Order's order lines and calculate the order total
print("\n--- ORDER 1 ---")

for line in order1.order_lines:
    print("Product:", line.product.name)
    print("Quantity:", line.quantity)
    print("Subtotal: $", line.calculate_subtotal())

print("Order 1 Total: $", order1.calculate_total())

# 5. Create a second Order
order2 = Order("O002")

# Add the SAME Product object to the second Order
order2.add_order_line(product1, 3)


# 7. Compare the OrderLine and Product objects
print("\n--- CHECKING OBJECT RELATIONSHIPS ---")

order1_line1 = order1.order_lines[0]
order2_line1 = order2.order_lines[0]

print(
    "Are the OrderLine objects different?",
    order1_line1 is not order2_line1
)
print(
    "Do both OrderLines refer to the same Product?",
    order1_line1.product is order2_line1.product
)
print(
    "Number of OrderLine objects:",
    len(order1.order_lines) + len(order2.order_lines)
)
print(
    "Number of distinct Product objects:",
    len({id(product1), id(product2)})
)

# 8. Remove Order 1 from the test scenario
print("\n--- REMOVING ORDER 1 ---")
del order1

# 9. Check that the Products still exist
print("\n--- CHECKING PRODUCTS AFTER DELETING ORDER 1 ---")

product1.display_information()
product2.display_information()

# 10. Check that Order 2 still exists and works
print("\n--- CHECKING ORDER 2 ---")

print("Order 2 remaining order lines:", len(order2.order_lines))
print("Order 2 total: $", order2.calculate_total())


# TEST 4: LISKOV SUBSTITUTION PRINCIPLE (LSP)
print("\n========== TEST 4: LSP ==========")

# Create a function that accepts a Product object
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


# TEST 4A: Test with PhysicalProduct
print("\n--- TESTING PHYSICAL PRODUCT ---")

show_product_details(physical_product)


# TEST 4B: Test with DigitalProduct
print("\n--- TESTING DIGITAL PRODUCT ---")

show_product_details(digital_product)


# TEST 4C: Add both product types to Inventory
print("\n--- ADDING BOTH PRODUCTS TO INVENTORY ---")

lsp_inventory = Inventory()

lsp_inventory.add_product(physical_product)
lsp_inventory.add_product(digital_product)


# TEST 4D: Display all products using the same Inventory method
print("\n--- DISPLAYING ALL INVENTORY PRODUCTS ---")
lsp_inventory.display_all()


# TEST 5: POLYMORPHISM

print("\n========== TEST 5: POLYMORPHISM ==========")

# Create a new Inventory
polymorphism_inventory = Inventory()

# Add one PhysicalProduct and one DigitalProduct
polymorphism_inventory.add_product(physical_product)
polymorphism_inventory.add_product(digital_product)

# Display information and fulfilment details for every Product
print("\n--- DISPLAYING PRODUCT INFORMATION AND FULFILMENT ---")

for product in polymorphism_inventory.products:
    product.display_information()
    print("Fulfilment Information:")
    print(product.get_fulfilment_info())
    print("-" * 48)
