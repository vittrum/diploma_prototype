from typing import List, Tuple, Union
from core.placeable_item import TwoDimensionalItem


class TwoDimensionalHold(object):
    """Class to represent a container that will ve filled with objects."""

    _hold: List[List[int]]
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
        self._hold = [row for _ in range(length)]

    def get_hold(self) -> List[List[int]]:
        return self._hold

    def console_print(self):
        """Display the current state of the container in console."""
        for i in self._hold:
            print(' '.join(str(j) for j in i))

    def find_empty_space(self) -> Union[Tuple[int, int], bool]:
        """
        Find an empty cell in the container.

        Returns:
        Optional[Tuple[int, int], bool]: either coordinates of an empty cell or false
        """
        for i, _ in enumerate(self._hold):
            for j, _ in enumerate(self._hold):
                if self._hold[i][j] == 0:
                    return tuple((i, j))
        return False

    def try_place_item(self, _item: TwoDimensionalItem, free_cell: Tuple[int, int]) -> bool:
        for i in range(_item.length):
            for j in range(_item.width):
                if self._hold[free_cell[0]+i][free_cell[1]+j] != 0:
                    return False
        return True

    def place_item(self, item: TwoDimensionalItem):
        ...
