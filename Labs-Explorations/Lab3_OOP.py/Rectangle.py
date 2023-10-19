
from Shapes import Shapes

class Rectangle(Shapes):
   
    def __init__(self, x, y, side1, side2):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2

    def is_inside(self, point_x, point_y):
        x_distance = abs(self.x - point_x)
        y_distance = abs(self.y - point_y)
        return x_distance <= self.side1 / 2 and y_distance <= self.side2 / 2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)

    def is_square(self):
        return self.side1 == self.side2
   
    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.x == other.x and self.y == other.y and self.side1 == other.side1 and self.side2 == other.side2
    def __str__(self):
        return f"Rectangle with center at ({self.x}, {self.y}), sides {self.side1} and {self.side2}"

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, side1={self.side1}, side2={self.side2})"
