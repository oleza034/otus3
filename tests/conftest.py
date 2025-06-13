from math import pi

import pytest


@pytest.fixture
def api_rectangle(request):
    def _wrapper(type_of_number: str):
        if type_of_number == 'integer':
            return 3, 5, 15
        if type_of_number == 'float':
            return 3.5, 5.5, 19.25

    yield _wrapper


@pytest.fixture
def api_square(request):
    def _wrapper(type_of_number: str):
        if type_of_number == 'integer':
            return 3, 9
        if type_of_number == 'float':
            return 3.5, 12.25

    yield _wrapper

@pytest.fixture
def api_triangle(request):
    def _wrapper(type_of_number: str):
        if type_of_number == 'integer':
            return 3, 4, 5, 6.0
        if type_of_number == 'float':
            return 6.0, 8.0, 10.0, 24.0

    yield _wrapper

@pytest.fixture
def api_circle(request):
    def _wrapper(type_of_number: str):
        if type_of_number == 'integer':
            return 1, pi
        if type_of_number == 'float':
            return 3.3, 34.21194399759284

    yield _wrapper
