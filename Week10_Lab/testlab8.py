from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# TEST 1: Association
# 1. Create one Supplier object
supplier1 = Supplier(
    "S001",
    "ABC Technology",
    "abc@example.com"
)

# 2. Create a PhysicalProduct using the Supplier
physical_product = PhysicalProduct(
    "P001",
    "Laptop",
    1200.00,
    10,
    2.5,
    supplier1
)

# 3. Create a DigitalProduct using the SAME Supplier
digital_product = DigitalProduct(
    "P002",
    "E-book",
    25.00,
    100,
    50,
    supplier1
)

# 4. Display PhysicalProduct information
print("\nPHYSICAL PRODUCT")
physical_product.display_information()

# 5. Display DigitalProduct information
print("\nDIGITAL PRODUCT")
digital_product.display_information()
