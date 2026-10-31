from dataclasses import dataclass,field

@dataclass
class Product:
    name:str
    price:float
    quantity:int
    category: str ="General"
    tags:list=field(default_factory=list)
    
notebook =Product("Notebook",45.0,100,"Stationary")
pen= Product("Pen",15.0,200,"Stationary")
laptop = Product("Laptop", 55000.0, 10, "Electronics")
mouse = Product("Mouse", 750.0, 50, "Electronics")
bottle = Product("Bottle", 250.0, 75)
print("Product Catalog:")
print(notebook)
print(pen)
print(laptop)
print(mouse)
print(bottle)
notebook_copy =Product("Notebook",45.0,100,"Stationary")
print("Equality Check:")
print("notebook == notebook_copy:",notebook == notebook_copy)
print("Adding tag to notebook...")
notebook.tags.append("bestseller")
print("notebook.tags",notebook.tags)
print("notebook_copy.tags",notebook_copy.tags)

"""Product Catalog
Basic dataclass usage with defaults and display
Create a Product dataclass with:
- name: str
- price: float
- quantity: int
- category: str with default "General"
- tags: list with default empty list (use field(default_factory=list))

Create 4-5 products. Demonstrate:
1. Print each product (auto-generated __repr__)
2. Check equality between two products with same values
3. Add a tag to one product, verify it doesn't appear on another (proving default_factory works correctly — no shared list bug)

Example output:

Product(name='Notebook', price=45.0, quantity=100, category='Stationery', tags=[])
Product(name='Pen', price=15.0, quantity=200, category='Stationery', tags=[])

notebook == notebook_copy: True
Adding tag to notebook...
notebook.tags: ['bestseller']
notebook_copy.tags: []  ← Not affected!
"""