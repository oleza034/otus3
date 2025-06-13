from src.figure import Figure, chk_positive


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        """Creates a rectangle figure with side_a and side_b."""

        for side in [side_a, side_b]:
            chk_positive(side, f'{self.__class__.__name__} sides')
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        """Calculates the area of the figure."""
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        """Calculates the sum of all sides of the figure."""
        return (self.side_a + self.side_b) * 2
