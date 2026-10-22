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