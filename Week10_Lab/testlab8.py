from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


# TEST 1: ASSOCIATION
print("\n========== TEST 1: ASSOCIATION ==========")

# Create a Supplier object
supplier1 = Supplier(
    "S001",
    "ABC Technology",
    "abc@example.com"
)


# Create a PhysicalProduct using that Supplier
physical_product = PhysicalProduct(
    "P001",
    "Laptop",
    1200.00,
    10,
    2.5,
    supplier1
)


# Create a DigitalProduct using the same Supplier
digital_product = DigitalProduct(
    "P002",
    "E-book",
    25.00,
    100,
    50,
    supplier1
)

# Display both products and their supplier information
print("\n--- PHYSICAL PRODUCT ---")
physical_product.display_information()

print("\n--- DIGITAL PRODUCT ---")
digital_product.display_information()


# Confirm Supplier and Products are separate objects
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
    physical_product._supplier is digital_product._supplier
)


# Predict what happens when supplier1 is deleted
print("\n--- DELETING SUPPLIER VARIABLE ---")

print("Deleting supplier1...")
del supplier1


# Check whether PhysicalProduct can still access Supplier
print("\n--- PHYSICAL PRODUCT AFTER DELETION ---")
physical_product.display_information()


# Check whether DigitalProduct can still access Supplier
print("\n--- DIGITAL PRODUCT AFTER DELETION ---")
digital_product.display_information()


# TEST 2: AGGREGATION
print("\n========== TEST 2: AGGREGATION ==========")

# Create a Supplier
supplier2 = Supplier(
    "S002",
    "XYZ Electronics",
    "xyz@example.com"
)

# Create a Product BEFORE adding it to any Inventory
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

# Create Inventory A and Inventory B
inventory_a = Inventory()
inventory_b = Inventory()

# Add the Product to Inventory A
print("\n--- ADDING PRODUCT TO INVENTORY A ---")
inventory_a.add_product(product)

# Remove the Product from Inventory A
print("\n--- REMOVING PRODUCT FROM INVENTORY A ---")
inventory_a.remove_product(product._product_id)

# Check whether the Product can still be used
print("\n--- PRODUCT AFTER REMOVAL FROM INVENTORY A ---")
product.display_information()

# Add the SAME Product object to Inventory B
print("\n--- ADDING SAME PRODUCT TO INVENTORY B ---")
inventory_b.add_product(product)

# Check whether the Product exists in Inventory B
print("\n--- CHECKING INVENTORY B ---")
found_product = inventory_b.find_product("P003")

print("Product successfully added to Inventory B:",
      found_product is product)

# Check that Inventory A no longer contains the Product
print("\n--- CHECKING INVENTORY A ---")
removed_product = inventory_a.find_product("P003")

print("Product removed from Inventory A:",
      removed_product is None)

# Check that the Product still works
print("\n--- FINAL PRODUCT CHECK ---")
product.display_information()