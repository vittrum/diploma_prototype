"""Container object that will represent storage in genetic algorythm."""

from copy import deepcopy

from typing import List, Tuple, Union

from core.placeable_item import TwoDimensionalItem


class TwoDimensionalContainer(object):
    """Class to represent a container that will ve filled with objects."""

    container: List[List[int]]
    width: int  # X axis
    length: int  # Y axis

    def __init__(self, width: int, length: int):
        """
        Creation of an empty hold.

        #noqa: width, length
        """
        self.width = width
        self.length = length
        row = [0 for _ in range(width)]
        self.container = [deepcopy(row) for _ in range(length)]

    def __str__(self) -> str:
        """Display the current state of the container in console."""
        for length_axis in self.container:
            return str(' '.join(str(width_axis) for width_axis in length_axis))

    def try_find_free_cell(self) -> Union[Tuple[int, int], bool]:
        """
        Find an empty cell in the container.

        Returns:
        Optional[Tuple[int, int], bool]: either coordinates of an empty cell or false
        """
        # for length_axis, _ in enumerate(self.container):
        #     for width_axis, _ in enumerate(self.container):
        #         if self.container[length_axis][width_axis] == 0:
        #             return tuple((length_axis, width_axis))
        for length_axis in range(self.length):
            for width_axis in range(self.width):
                if self.container[length_axis][width_axis] == 0:
                    return tuple((length_axis, width_axis))
        return False

    def try_place_item(self, item: TwoDimensionalItem, free_cell: Tuple[int, int]) -> bool:
        """Try to place item in the container. Starting point is the free cell."""
        if item.length + free_cell[0] > self.length or \
            item.width + free_cell[1] > self.width:
            return False
        for length_axis in range(item.length):
            for width_axis in range(item.width):
                if self.container[free_cell[0] + length_axis][free_cell[1] + width_axis] != 0:
                    return False
        return True

    def place_item(self, item: TwoDimensionalItem, cell: Tuple[int, int]) -> bool:
        for length_axis in range(item.length):
            for width_axis in range(item.width):
                self.container[cell[0] + length_axis][cell[1] + width_axis] = 1
        return True
