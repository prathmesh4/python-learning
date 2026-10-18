def circle_area(r):
    return 3.14159 * r * r

def rectangle_area(l, w):
    return l * w

def triangle_area(b, h):
    return 0.5 * b * h

shape = input("Shape (circle/rectangle/triangle): ").strip().lower()

if shape == "circle":
    r = float(input("Radius: "))
    area = circle_area(r)

elif shape == "rectangle":
    l = float(input("Length: "))
    w = float(input("Width: "))
    area = rectangle_area(l, w)

elif shape == "triangle":
    b = float(input("Base: "))
    h = float(input("Height: "))
    area = triangle_area(b, h)

else:
    area = None
    print("Invalid shape!")

if area is not None:
    print("Area:", area)
