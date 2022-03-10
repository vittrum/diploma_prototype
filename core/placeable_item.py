from typing import List, Tuple, Union


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