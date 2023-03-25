"""
LSA = perimeter of base * height
TSA = LSA + 2 * BASE AREA
Base types:
    circle
        area: pi * radius^2
        perimeter: Diameter * pi
    square
        area: side^2
        perimeter: 4*side
    rectangle
        area: length * width
        perimeter: length + width
"""
from math import pi
# functions
def Round(x, y):
    try:
        return round(x, y)
    except Exception:
        return None
# perimeter of base calculations
while True:
    try:
        base_type = int(input("What is the base type\n1.Circle\n2.Square\n3.Rectangle\n4.Quit\nChoose a number:\n"))
        if base_type == 1:
            # circle
            shape_type = int(input("What's the shape type\n1.Sphere\n2.Cylinder\n3.Cone\nChoose a number:\n"))
            if shape_type == 1:
                # sphere
                diameter = float(input("Diameter:"))
                perimeter = diameter * pi
                LSA = None
                radius = diameter / 2
                base_area = pi * radius**2
                TSA = 4 * pi * radius**2
                volume = 1.3333333333 * pi * radius**3
            elif shape_type == 2:
                # cylinder
                height = float(input("Height of\nobject:"))
                diameter = float(input("Diameter:"))
                perimeter = diameter * pi
                LSA = perimeter * height
                radius = diameter / 2
                base_area = pi * radius**2
                TSA = LSA + 2 * base_area
                volume = base_area * height
            elif shape_type == 3:
                # cone
                slant = float(input("Slant of\ncone\n(referred to as 'l')\n:"))
                diameter = float(input("Diameter:"))
                radius = diameter / 2
                perimeter = diameter * pi
                LSA = pi*slant*radius
                base_area = pi * radius**2
                TSA = LSA + pi * radius**2
                volume = 0.3333333333 * base_area * height

            print("""Results:
Perimeter:{0}
L.S.A:{1}
Radius:{2}
Base area:{3}
T.S.A:{4}""".format(Round(perimeter, 2),
                    Round(LSA, 2),
                    Round(radius, 2),
                    Round(base_area, 2),
                    Round(TSA, 2)))
            input("EXE TO PAGE2")
            print("""Results2:
Volume:{0}""".format(Round(volume,2)))
            input("EXE TO CONTINUE")
        elif base_type == 2:
            # Square
            input("Shape type not supported!\nEXE to continue")
        elif base_type == 3:
            # Rectangle
            input("Shape type not supported!\nEXE to continue")
        else:
            raise SystemExit(0)
    except ValueError:
        print("Only numbers please")
        continue
