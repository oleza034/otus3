from math import sqrt
from src.figure import Figure, chk_positive


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        """Creates a triangle figure with side_a and side_b and side_c."""
        # checking that sides can form a valid triangle
        self.chk_valid_triangle(side_a, side_b, side_c)
        self.side_a, self.side_b, self.side_c = side_a, side_b, side_c

    @property
    def area(self):
        """Calculates the area of the triangle."""
        # Using Heron formula: s = semi-perimeter; abc = triangle sides
        s = self.perimeter / 2
        a, b, c = self.side_a, self.side_b, self.side_c
        return sqrt(s * (s - a) * (s - b) * (s - c))

    @property
    def perimeter(self):
        """Calculates the perimeter of the triangle."""
        return self.side_a + self.side_b + self.side_c

    @staticmethod
    def chk_valid_triangle(a: (int | float), b: (int | float), c: (int | float)):
        """Checks if three side lengths can form a valid triangle."""
        # first, check that all sides are positive numbers
        [chk_positive(num) for num in [a, b, c]]
        # then, validate triangle
        if not ((a + b > c) and (a + c > b) and (b + c > a)):
            raise ValueError(f'Cannot form a valid triangle with sides: {a}, {b}, {c}')
