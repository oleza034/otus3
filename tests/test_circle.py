from src.circle import Circle
import pytest


@pytest.mark.parametrize('type_of_number', ['integer', 'float'])
def test_circle_area_positive(api_circle, type_of_number):
    radius, area = api_circle(type_of_number=type_of_number)
    print(f'Testing circle with {radius=}, {area=}')
    r = Circle(radius)
    assert r.area == area


@pytest.mark.parametrize(
    'radius',
    (0, -1, '1', True),
    ids=['zero value', 'negative value', 'not numbers', 'boolean']
)
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)
