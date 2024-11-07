from __future__ import annotations
from typing import override


class Cell:
    def __init__(self) -> None:
        self._alive = False
        self._symbol = "."
        self._neighbours: list[Cell] = []
        self._num_living_neighbours = 0

    @override
    def __repr__(self) -> str:
        return self.get_symbol()

    @override
    def __str__(self) -> str:
        return self.get_symbol()

    def is_alive(self) -> bool:
        return self._alive

    def get_symbol(self) -> str:
        return self._symbol

    def set_dead(self) -> None:
        self._alive = False
        self._symbol = "."

    def set_alive(self) -> None:
        self._alive = True
        self._symbol = "O"

    def live_neighbours(self) -> None:
        self._num_living_neighbours = sum([1 for x in self._neighbours if x.is_alive()])

    def update(self) -> None:
        (
            self.set_alive()
            if (
                self._num_living_neighbours == 3
                or (self.is_alive() and self._num_living_neighbours == 2)
            )
            else self.set_dead()
        )

    def add_neighbour(self, cell: Cell) -> None:
        self._neighbours.append(cell)
