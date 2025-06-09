from src.square import Square
import pytest


@pytest.mark.parametrize('type_of_number', ['integer', 'float'])
def test_square_area_positive(api_square, type_of_number):
    side_a, area = api_square(type_of_number=type_of_number)
    print(f'Testing Square with {side_a=}, {area=}')
    r = Square(side_a)
    assert r.area == area


@pytest.mark.parametrize(
    'side_a',
    (0, -1, '1', True),
    ids=['zero', 'negative', 'not number', 'boolean']
)
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)

