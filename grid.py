from cell import Cell
from random import randint, seed


class Grid:
    def __init__(self, rows: int = 25, cols: int = 25) -> None:
        seed(123)
        self._rows = rows
        self._cols = cols
        self._grid = self._fill_grid()
        self._set_start_state()
        self._set_neighbours_all()

    def _fill_grid(self) -> list[list[Cell]]:
        return [[Cell() for _ in range(self._rows)] for _ in range(self._cols)]

    def _set_start_state(self) -> None:
        for row in self._grid:
            for cell in row:
                if randint(0, 2) == 1:
                    cell.set_alive()

    def _set_neighbours(self, row: int, col: int) -> None:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 == j:
                    continue
                if row + i in [-1, self._rows] or col + j in [-1, self._cols]:
                    continue
                self._grid[row][col].add_neighbour(self._grid[row + i][col + j])

    def _set_neighbours_all(self) -> None:
        for i in range(self._rows):
            for j in range(self._cols):
                self._set_neighbours(row=i, col=j)

    def get_cell(self, row: int, column: int) -> Cell:
        return self._grid[row][column]

    def get_all_cells(self) -> list[Cell]:
        return [cell for row in self._grid for cell in row]

    def get_num_alive(self) -> int:
        return sum(1 for cell in self.get_all_cells() if cell.is_alive())

    def get_grid(self) -> list[list[Cell]]:
        return self._grid
