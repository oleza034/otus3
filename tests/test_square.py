from src.square import Square
import pytest


@pytest.mark.parametrize('type_of_number', ['integer', 'float'])
def test_square_positive(api_figure, type_of_number):
    """Тестирование квадрата"""
    side_a, area = api_figure(shape='square', type_of_number=type_of_number)
    perimeter = 4 * side_a
    r = Square(side_a)
    assert r.area == area, f'Area of {r} must be {area=}'
    assert r.perimeter == perimeter, f'Perimeter of {r} must be {perimeter=}'


@pytest.mark.parametrize(
    'side_a',
    (0, -1, '1'),
    ids=['zero', 'negative', 'not number']
)
def test_square_negative(side_a):
    """Создание квадрата с неверным значением стороны"""
    with pytest.raises(ValueError):
        Square(side_a)

