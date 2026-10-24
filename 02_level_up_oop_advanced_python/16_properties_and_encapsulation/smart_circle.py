import math

class Circle:
    def __init__(self,redius):
        self.redius=redius
    @property
    def redius(self):
        return self._redius
    @redius.setter
    def redius(self,value):
        if not isinstance(value,(int,  float)):
            raise TypeError("Radius must be number")    
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._redius=value
    @property
    def area(self):
        return math.pi * self.redius ** 2    
    @property
    def circumference(self):
        return 2 * math.pi * self.redius
    @property
    def diameter(self):
        return self.redius *2
    @diameter.setter
    def diameter(self,value):
        self.redius = value / 2
        
    def __repr__(self):
        return f"Circle(radius={self.redius})"
circle=Circle(5)            
print(circle)

print(f"Area: {circle.area:.2f}")
print(f"Circumference: {circle.circumference:.2f}")
print(f"Diameter : {circle.diameter}")

print("setting diameter to 20")
circle.diameter=20
print(f"New Radius: {circle.redius}")
print(f"New Area: {circle.area:.2f}")

print("setting radius to -3")
try:
    circle.redius=-3
except ValueError as e:
    print(f"Error {e}")    

print("setting radius to 'hello'..")
try:
    circle.redius="Hello"
except TypeError as e:
    print(f"Error {e}")    