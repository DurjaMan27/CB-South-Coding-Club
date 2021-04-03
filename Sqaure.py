class Parallelogram:
    def __init__(self, base, side_length, height):
        self.base = base
        self.side_length = side_length
        self.height = height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return 2 * self.base + 2 * self.side_length


class Rectangle(Parallelogram):
    def __init__(self, length, width):
        super().__init__(length, width, width)

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
"""
class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.side_length
"""

rect = Rectangle(3,9)
print(rect.area())

square = Square(9)
print(square.perimeter())
