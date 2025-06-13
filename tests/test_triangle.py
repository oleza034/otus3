from src.triangle import Triangle
import pytest


@pytest.mark.parametrize('type_of_number', ['integer', 'float'])
def test_triangle_area_positive(api_figure, type_of_number):
    """Тестирование треугольника"""
    side_a, side_b, side_c, area = api_figure(shape='triangle', type_of_number=type_of_number)
    perimeter = side_a + side_b + side_c
    r = Triangle(side_a, side_b, side_c)
    assert r.area == area, f'Area of {r} should be {area}'
    assert r.perimeter == perimeter, f'Perimeter of {r} should be {perimeter}'


@pytest.mark.parametrize(
    'side_a,side_b,side_c',
    [(1, 2, 4), (0, 1, 2), (-1, 2, 3), ('1', 2, 3)],
    ids=['invalid sides', 'zero', 'negative', 'not number']
)
def test_triangle_negative(side_a, side_b, side_c):
    """Создание треугольника с неверными значениями сторон"""
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)

