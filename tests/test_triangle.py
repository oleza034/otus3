from src.triangle import Triangle
import pytest


@pytest.mark.parametrize('type_of_number', ['integer', 'float'])
def test_triangle_area_positive(api_triangle, type_of_number):
    side_a, side_b, side_c, area = api_triangle(type_of_number=type_of_number)
    print(f'Testing Square with {side_a=}, {side_b=}, {side_c=}, {area=}')
    r = Triangle(side_a, side_b, side_c)
    assert r.area == area


@pytest.mark.parametrize(
    'side_a,side_b,side_c',
    [(1, 2, 4), (0, 1, 2), (-1, 2, 3), ('1', 2, 3), (True, 2, 3)],
    ids=['incorrect triangle', 'zero', 'negative', 'not number', 'boolean']
)
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)

