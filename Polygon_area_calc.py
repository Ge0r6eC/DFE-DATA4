# Create class and sub-class objects which represent different
# geometrical shapes, such as Rectanlges and Squares

from abc import ABC, abstractmethod
from math import tan

# import pdb
# pdb.set_trace()

class Polygon:
    
    def __init__(self):
        self.sides = 0
        self.sides_length = 0

    def perimeter(self):
        polygon_perimeter = (self.sides * self.sides_length)
        return polygon_perimeter 

    def apothem(self):
        polygon_apothem = (self.sides_length / 2*(tan(180/self.sides)))
        return int(polygon_apothem)
            
    def area(self):
        self.p = self.perimeter()
        self.a = self.apothem()
        polygon_area = 0.5 * self.p * self.a
        return polygon_area

class Three_sided_polygon(Polygon):
    def __init__(self, sides_length):
        self.sides = 3
        self.sides_length = sides_length

class Four_sided_polygon(Polygon):
        
    def __init__(self, sides_length):
        self.sides = 4
        self.sides_length = sides_length

class five_sided_polygon(Polygon):
    def __init__(self, sides_length):
        self.sides = 5
        self.sides_length = sides_length
    
class six_sided_polygon(Polygon):
    def __init__(self, sides_length):
        self.sides = 6
        self.sides_length = sides_length


shape1 = Four_sided_polygon(10)
shape2 = five_sided_polygon(10)


print(shape1.perimeter())
print(shape1.apothem())
print(shape1.area())

print(shape2.perimeter())
print(shape2.apothem())
print(shape2.area())

