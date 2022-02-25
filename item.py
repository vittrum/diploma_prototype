"""Module with an item to be used in GeneticAlgorithm."""

from typing import List, Optional, Tuple


class TwoDimensionalItem(object):
    """Item object which will be used as a base piece in genetic algorithm."""

    width: int
    length: int
    _is_placed: int

    def __init__(self, width: int, length: int):
        """
        Generate basic two-dimensional item for GenAlg.
        # noqa: width, length
        """
        self.width = width
        self.length = length

    @property
    def area(self) -> int:
        """
        Calculate area that will be possessed by the item.

        Returns:
            int: result of area that will be possessed by block
        """
        return self.width * self.length

    @property
    def is_placed(self) -> bool:
        """
        Use to exclude placed items from the pool.

        Returns:
            bool: result if item is placed
        """
        return self.is_placed

    def place(self) -> None:
        """Place item in the space."""
        self._is_placed = True

    def pick_up(self) -> None:
        """Pick up item if you want to place it elsewhere."""
        self._is_placed = False


class TwoDimensionalHold(object):
    _hold: List[List[int]]
    width: int  # X axis
    length: int  # Y axis

    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length
        row = [0 for _ in range(width)]
        self._hold = [row for _ in range(length)]

    def console_print(self):
        for i in self._hold:
            print(" ".join(str(j) for j in i))

    def find_empty_space(self) -> Optional[Tuple[int, int], bool]:
        for i, _ in enumerate(self._hold):
            for j, _ in enumerate(self._hold):
                if self._hold[i][j] == 0:
                    return tuple((i, j))
        return False
    def try_place_item(self, item: TwoDimensionalItem) -> bool:
        ...

    def place_item(self, item: TwoDimensionalItem):
        ...

hold = TwoDimensionalHold(3, 4)
hold.console_print()