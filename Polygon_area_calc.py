# Create class and sub-class objects which represent different
# geometrical shapes, such as Rectanlges and Squares

from abc import ABC, abstractmethod


class Polygon:
    @abstractmethod
    def sides(self):
        pass

    equal_sides = False
        
class Quadrilateral(Polygon):
    
    def __init__(self, name):
        self.name = name
    
    def sides(self):
        return 4


shape1 = Quadrilateral("Square")
shape2 = Quadrilateral("Rectangle")

