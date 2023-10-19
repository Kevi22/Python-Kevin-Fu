
import math

class Shapes:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            print("ValueError: dx and dy must be numeric")
            return

        self.x += float(dx)
        self.y += float(dy)
    
    def __str__(self):
        return f"Position: ({self.x}, {self.y})"

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def distance_to_point(self, point_x, point_y):
        return math.sqrt((self.x - point_x) ** 2 + (self.y - point_y) ** 2)