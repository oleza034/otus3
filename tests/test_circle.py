from src.circle import Circle
from math import pi
import pytest


@pytest.mark.parametrize('type_of_number', ['integer', 'float'])
def test_circle_positive(api_figure, type_of_number):
    """Тестирование круга"""
    radius, area = api_figure(shape='circle', type_of_number=type_of_number)
    perimeter = 2 * pi * radius
    r = Circle(radius)
    assert r.area == area, f'Area of {r} must be {area}'
    assert r.perimeter == perimeter, f'Perimeter of {r} must be {perimeter}'


@pytest.mark.parametrize(
    'radius',
    (0, -1, '1'),
    ids=['zero value', 'negative value', 'not numbers']
)
def test_circle_negative(radius):
    """Создание круга с неверным радиусом"""
    with pytest.raises(ValueError):
        Circle(radius)
