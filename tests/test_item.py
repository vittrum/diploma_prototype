from core.placeable_item import TwoDimensionalItem


def test_create_item():
    _width, _length = 2, 3
    _item = TwoDimensionalItem(_width, _length)
    assert _item.area == 6
