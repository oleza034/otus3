from src.figure import Figure, chk_positive
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        """Creates a circle with specified radius."""
        chk_positive(radius, 'Circle radius')
        self.radius = radius

    @property
    def area(self):
        """Calculates the area of the circle."""
        return self.radius ** 2 * pi

    @property
    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return self.radius * 2 * pi
