import pytest
from core.container import TwoDimensionalHold
from core.placeable_item import TwoDimensionalItem


def test_container_creation():
    _width, _length = 2, 3
    _container = TwoDimensionalHold(_width, _length)
    assert _container.width == _width
    assert _container.length == _length
    assert _container.get_hold() == [[0, 0], [0, 0], [0, 0]]


def test_find_empty_space():
    _container = TwoDimensionalHold(3, 3)
    _free_cell = _container.find_empty_space()
    assert _free_cell == (0, 0)


def test_try_place_item():
    fitting_item = TwoDimensionalItem(2, 3)
    not_fitting_item = TwoDimensionalItem(5, 5)
    _container = TwoDimensionalHold(3, 3)
    free_cell = _container.find_empty_space()
    assert _container.try_place_item(not_fitting_item, free_cell)
    assert _container.try_place_item(fitting_item, free_cell)
    second_free_cell = _container.find_empty_space()
    assert _container.try_place_item(fitting_item, second_free_cell)
