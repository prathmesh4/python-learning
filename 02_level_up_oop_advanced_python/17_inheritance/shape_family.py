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