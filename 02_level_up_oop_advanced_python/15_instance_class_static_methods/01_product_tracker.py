class Product:
    total_products = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        Product.total_products += 1
        print(f"Created: {self.name} (Rs {self.price})")

    @classmethod
    def get_count(cls):
        return cls.total_products

    @staticmethod
    def validate_price(price):
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            return False
        return price > 0

product1 = Product("Notebook", 45, 10)
product2 = Product("Pen", 15, 20)
product3 = Product("Eraser", 5, 15)
product4 = Product("Pencil", 10, 25)
product5 = Product("Ruler", 30, 8)
print(f"Total products created: {Product.get_count()}")

print(f"validate_price(45): {Product.validate_price(45)}")
print(f"validate_price(-10): {Product.validate_price(-10)}")
print(f"validate_price(0): {Product.validate_price(0)}")
print(f"validate_price('abc'): {Product.validate_price('abc')}")

"""Product Tracker
Class attributes and class methods for tracking shared state
Create a Product class with:

Class attributes:
- total_products — starts at 0, increments every time a new Product is created

Instance attributes (set in __init__):
- name, price, quantity

Class method:
- get_count() — returns the total number of products created

Static method:
- validate_price(price) — returns True if price is a positive number, False otherwise

Create 4-5 products. Print the total count using the class method. Test the static method with valid and invalid prices (negative, zero, string).

Example output:

Created: Notebook (Rs 45)
Created: Pen (Rs 15)
Created: Eraser (Rs 5)

Total products created: 3
validate_price(45): True
validate_price(-10): False
validate_price(0): False
"""