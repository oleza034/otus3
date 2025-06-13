from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize('type_of_number', ['integer', 'float'])
def test_rectangle_area_positive(api_rectangle, type_of_number):
    side_a, side_b, area = api_rectangle(type_of_number=type_of_number)
    print(f'Testing Rectangle with {side_a=}, {side_b=}, {area=}')
    r = Rectangle(side_a, side_b)
    assert r.area == area


@pytest.mark.parametrize(
    ('side_a', 'side_b'),
    [
        (0, 5),
        (-1, 5.5),
        ('1', '2')
    ],
    ids=['zero value', 'negative value', 'not numbers']
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
