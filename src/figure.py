from abc import ABC, abstractmethod


def chk_positive(number, value_role: (str | None)=None):
    """checks that number is a positive number and raises ValueError otherwise"""
    if not ((isinstance(number, int) or isinstance(number, float)) and number > 0):
        # variables to form a correct error message
        value_role = value_role or 'Value'
        # 'us' -- means, 'radius' is not plural
        article, plural = ('', 's') if value_role[-1] == 's' and value_role[-2:] != 'us' else (' a', '')
        raise ValueError(f'{value_role} must be{article} positive number{plural}')


class Figure(ABC):
    """Abstract base class for figures."""
    @property
    @abstractmethod
    def area(self):
        """Calculates the area of the figure."""
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the figure."""
        pass

    def add_area(self, *other_figures):
        """Summarize areas of this and another figure."""
        if not all(isinstance(figure, Figure) for figure in other_figures):
            raise ValueError("all params must be of Figure class")
        return self.area + sum([f.area for f in other_figures])
