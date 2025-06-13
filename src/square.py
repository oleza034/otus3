from src.rectangle import Rectangle
from src.figure import chk_positive


class Square(Rectangle):
    def __init__(self, side_a):
        """Creates a square figure with sides equal to side_a."""
        chk_positive(side_a, 'Square sides')
        super().__init__(side_a, side_a)
