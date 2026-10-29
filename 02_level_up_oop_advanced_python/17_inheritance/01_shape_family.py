import math

class Shape:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
    def display(self):
        print(f"{self.name} ({self.color}): area={self.area():.2f}")
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__("Circle",color)
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def display(self):
        print(f"{self.name} ({self.color}): "
              f"radius={self.radius}, area={self.area():.2f} "
              )  
class Rectangle(Shape):
    def __init__(self,  color, length, width):
        super().__init__("Rectangle", color)
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width                         
    def display(self):
        print(f"{self.name} ({self.color}): "
              f"{self.length} X {self.width} , area={self.area():.2f}")
class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__("Triangle", color)
        self.base=base
        self.height=height
    def area(self):
        return 0.5 * self.base * self.height 
    def display(self):
        print(f"{self.name} ({self.color}): "
              f"base={self.base}, height={self.height}"
              f"area={self.area():.2f}")

shapes=[Circle("Red",5),
        Rectangle("blue", 4,6),
        Triangle("Green", 3, 8),
        Circle("Yellow", 10)
        ]           
for shape in shapes:
    shape.display()                
    
"""Shape Family
Basic inheritance with shared base class and method overriding
Create a Shape base class with name and color attributes.

Create three subclasses:
- Circle(Shape) — additional attribute: radius. Implements area().
- Rectangle(Shape) — additional attributes: length, width. Implements area().
- Triangle(Shape) — additional attributes: base, height. Implements area().

Each subclass should:
- Call super().__init__() to handle name and color
- Override display() to print shape-specific info including area

Create a mixed list of shapes and loop through it, calling display() on each. This should work without checking what type each shape is — polymorphism.

Example output:

Circle (Red): radius=5, area=78.54
Rectangle (Blue): 4x6, area=24.00
Triangle (Green): base=3, height=8, area=12.00
Circle (Yellow): radius=10, area=314.16
"""    