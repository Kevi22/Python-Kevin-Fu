import math
from Shapes import Shapes

class Circle(Shapes):
   
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def is_inside(self, point_x, point_y):
        distance = self.distance_to_point(point_x, point_y)
        return distance <= self.radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_unit_circle(self):
        return self.radius == 1

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        
        return False

    def __str__(self):
        return f"Circle with center at ({self.x}, {self.y}) and radius {self.radius}"

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, radius={self.radius})"
    