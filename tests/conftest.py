from math import pi
import pytest


shape_data = {
    'rectangle': {
        'integer': (3, 5, 15),
        'float': (3.5, 5.5, 19.25)
    },
    'square': {
        'integer': (3, 9),
        'float': (3.5, 12.25),
    },
    'triangle': {
        'integer': (3, 4, 5, 6.0),
        'float': (6.0, 8.0, 10.0, 24.0)
    },
    'circle': {
        'integer': (1, pi),
        'float': (3.3, 34.21194399759284)
    }
}


@pytest.fixture
def api_figure():
    def _wrapper(shape: str, type_of_number: str):
        if shape in shape_data:
            if type_of_number in shape_data[shape]:
                return shape_data[shape][type_of_number]
            raise ValueError(f'Param {type_of_number=} is not supported for {shape=}')
        raise ValueError(f'Shape {shape} is not defined.')
    return _wrapper
