class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        # supplier_id: a unique identifier for the supplier
        self.__supplier_id = supplier_id
        # name: supplier's name
        self.__name = name
        # contact_email: supplier's contact email
        self.__contact_email = contact_email

    # A supplier should be able to provide information about itself
    def display_information(self):
        print("Supplier ID:", self.__supplier_id)
        print("Supplier Name:", self.__name)
        print("Contact Email:", self.__contact_email)