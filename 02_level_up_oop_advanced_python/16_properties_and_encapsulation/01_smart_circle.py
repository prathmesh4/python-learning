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

"""Smart Circle
Properties with validation and computed attributes
Create a Circle class where:

- radius is a property with a setter that validates: must be a positive number. Raise ValueError otherwise.
- area is a read-only computed property (π × r²). Use math.pi.
- circumference is a read-only computed property (2 × π × r).
- diameter is a property with BOTH getter and setter. Getting it returns radius * 2. Setting it should UPDATE the radius to diameter / 2.

Demonstrate:
1. Create a circle with radius 5
2. Print area, circumference, diameter
3. Change the diameter to 20 — verify radius is now 10
4. Try setting radius to -3 — should raise ValueError
5. Try setting radius to "hello" — should raise TypeError

Example output:

Circle(radius=5)
Area: 78.54
Circumference: 31.42
Diameter: 10

Setting diameter to 20...
New radius: 10
New area: 314.16

Setting radius to -3...
Error: Radius must be positive
"""    