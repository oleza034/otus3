from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize('type_of_number', ['integer', 'float'])
def test_rectangle_positive(api_figure, type_of_number):
    """Тестирование прямоугольника"""
    side_a, side_b, area = api_figure(shape='rectangle', type_of_number=type_of_number)
    perimeter = 2 * (side_a + side_b)
    r = Rectangle(side_a, side_b)
    assert r.area == area, f'Area of {r} must be {area}'
    assert r.perimeter == perimeter, f'Perimeter of {r} must be {perimeter}'


@pytest.mark.parametrize(
    ('side_a', 'side_b'),
    [
        (0, 5),
        (5.5, -2.3),
        ('1', '2')
    ],
    ids=['zero value', 'negative value', 'not numbers']
)
def test_rectangle_negative(side_a, side_b):
    """Создание прямоугольника с неверными значениями сторон"""
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
