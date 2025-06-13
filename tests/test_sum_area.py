import pytest
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle
from random import choice


@pytest.fixture
def get_figures(api_figure):
    """returns random figures of specified shapes and their total area"""
    def _wrapper(shapes: str):
        # constructor for figures
        figure_set = {'rectangle': Rectangle, 'square': Square, 'triangle': Triangle, 'circle': Circle}

        # checking shapes param: must be string with 2 or more figures separated by "+"
        if not (isinstance(shapes, str) and '+' in shapes and all(f in figure_set for f in shapes.split('+'))):
            raise ValueError(f'Invalid {shapes=}. Must be string with 2 shapes or more separated by +')
        # transforming shapes param into a list
        shapes = shapes.split('+')
        # getting corresponded figures
        figures, total_area = [], 0
        for shape in shapes:
            # getting figure sides or radius, and area
            *sides, area = api_figure(shape=shape, type_of_number=choice(['integer', 'float']))
            # adding new figure and its area to figures and total_area
            figures.append(figure_set[shape](*sides))
            total_area += area
        return figures, total_area

    return _wrapper

@pytest.mark.parametrize(
    'shapes',
    [
        'rectangle+square',
        'square+circle',
        'circle+triangle',
        'triangle+rectangle',
        'rectangle+square+triangle+circle',
    ]
)
def test_sum_area(get_figures, shapes):
    """Тестирование общей площади набора фигур"""
    figures, area = get_figures(shapes)
    figure1, *other_figures = figures
    # checking sum of figure areas
    msg = ' and '.join([f'{figure}' for figure in figures])
    assert figure1.add_area(*other_figures) == area, f'Total area of {msg} must be {area}'
