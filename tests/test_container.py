import pytest
from core.container import TwoDimensionalContainer
from core.placeable_item import TwoDimensionalItem


def test_container_creation():
    _width, _length = 2, 3
    _container = TwoDimensionalContainer(_width, _length)
    assert _container.width == _width
    assert _container.length == _length
    assert _container.container == [[0, 0], [0, 0], [0, 0]]


def test_find_empty_space():
    _container = TwoDimensionalContainer(3, 3)
    _free_cell = _container.try_find_free_cell()
    assert _free_cell == (0, 0)


def test_try_place_item_correct():
    fitting_item = TwoDimensionalItem(2, 3)
    not_fitting_item = TwoDimensionalItem(5, 5)
    container = TwoDimensionalContainer(3, 3)
    free_cell = container.try_find_free_cell()
    assert not container.try_place_item(not_fitting_item, free_cell)
    assert container.try_place_item(fitting_item, free_cell)


def test_place_item():
    fitting_item = TwoDimensionalItem(2, 3)
    container = TwoDimensionalContainer(3, 3)
    free_cell = (0, 0)
    container.place_item(fitting_item, free_cell)
    assert container.container == [[1, 1, 0],
                                   [1, 1, 0],
                                   [1, 1, 0]]


def test_try_place_item_no_space():
    fitting_item = TwoDimensionalItem(2, 3)
    container = TwoDimensionalContainer(3, 3)
    free_cell = (0, 0)
    container.place_item(fitting_item, free_cell)
    assert container.container == [[1, 1, 0],
                                   [1, 1, 0],
                                   [1, 1, 0]]
    free_cell = container.try_find_free_cell()
    assert free_cell == (0, 2)
    assert not container.try_place_item(fitting_item, free_cell)


def test_place_multiple_items():
    small_item = TwoDimensionalItem(2, 2)
    big_item = TwoDimensionalItem(3, 3)
    container = TwoDimensionalContainer(length=5, width=3)
    free_cell = container.try_find_free_cell()
    assert free_cell == (0, 0)
    assert container.try_place_item(big_item, free_cell)
    assert container.place_item(big_item, free_cell)
    assert container.container == [[1, 1, 1],
                                   [1, 1, 1],
                                   [1, 1, 1],
                                   [0, 0, 0],
                                   [0, 0, 0]]
    free_cell = container.try_find_free_cell()
    assert free_cell == (3, 0)
    assert not container.try_place_item(big_item, free_cell)
    assert container.try_place_item(small_item, free_cell)
    assert container.place_item(small_item, free_cell)
    assert container.container == [[1, 1, 1],
                                   [1, 1, 1],
                                   [1, 1, 1],
                                   [1, 1, 0],
                                   [1, 1, 0]]