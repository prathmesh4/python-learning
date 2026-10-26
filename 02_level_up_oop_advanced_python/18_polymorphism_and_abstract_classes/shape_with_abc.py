from abc import ABC ,abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def describe(self):
        print(f"This is a {self.__class__.__name__} with area {self.area():.2f}")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return  math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self,length,width):
        self.lenght=length
        self.width=width
    def area(self):
        return  self.lenght * self.width
    def perimeter(self):
        return 2 * (self.lenght + self.width)
class Triangle(Shape):
    def __init__(self,a ,b, c):
        if  a<=0 or b<=0 or c<=0:
            raise ValueError("Side must be positive")
        if a+b<=c or a+c <=b or b+c<=a:
            raise ValueError("Invalid triangle side lengths")
        self.a=a
        self.b=b
        self.c=c 
    def area(self):
        s=self.perimeter()/2
        return  math.sqrt(s *( s - self.a)) * (s -self.b) * (s - self.c)
    def perimeter(self):
        return self.a + self.b + self.c
shapes = [
    Circle(5),
    Rectangle(6, 4),
    Triangle(3, 4, 5)
]
for shape in shapes:
    shape.describe()    
print("Trying shape()...")
try:
    Shape()
except TypeError as e:
    print(f"TypeError : {e}")
class BrokenShape(Shape):
    def area(self):
        return 10
print("Trying BrokenShape()...")    
try:
    BrokenShape()
except TypeError as e:
    print(f"TypeError : {e}")                         