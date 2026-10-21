class Rectangle:
    def __init__(self,length,witdh):
        self.length = length
        self.width = witdh
        
    def area(self):
        return self.length * self.width   
    def perimeter(self):
        return 2 * (self.length + self.width)
    def is_square(self):
        return self.length == self.width  
    def display(self):
        print(f"Rectangle: {self.length} x {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter : {self.perimeter()}")
        print(f"Is Square : {self.is_square()}")
        
rt1=Rectangle(5, 3)        
rt2=Rectangle(4, 4)        
rt3=Rectangle(7, 2)

rectangles=[rt1, rt2, rt3]

for rt in rectangles:
    rt.display()        