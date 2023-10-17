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


def main():
    cirkel1 = Circle(x=0, y=0, radius=1)
    cirkel2 = Circle(x=1, y=1, radius=1)
    rektangel = Rectangle(x=0, y=0, side1=1, side2=1)

    print(cirkel1 == cirkel2)  # True
    print(cirkel2 == rektangel)  # False
    print(cirkel1.is_inside(0.5, 0.5))  # True
    cirkel1.translate(5, 5)
    print(cirkel1.is_inside(0.5, 0.5))  # False
    cirkel1.translate("TRE", 5)  # ValueError
    print(cirkel1)
    print(repr(cirkel2))
    print(rektangel)
    print(repr(rektangel))

if __name__ == "__main__":
   
    main()

