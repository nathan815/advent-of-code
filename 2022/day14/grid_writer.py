import copy
from pathlib import Path

AIR = " "
GridData = list[list[str]]


def write_grid(
    grid: GridData, filename: str, directory=Path(__file__).parent / "generated"
):
    fullpath = directory / Path(filename)
    fullpath.parent.mkdir(parents=True, exist_ok=True)
    with open(fullpath, "w") as f:
        f.write("\n".join(["".join(row_chars) for row_chars in grid]))


class QueuedGridWriter:
    """Queues writing of multiple grid output files. Cleans them up for presentation before writing."""

    def __init__(self) -> None:
        self.min_filled_x = float("inf")
        self.max_filled_x = float("-inf")
        self.pending_writes = {}

    def queue(self, grid: GridData, filename: str):
        self.pending_writes[filename] = copy.deepcopy(grid)

        # update the min/max x
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] != AIR:
                    if x < self.min_filled_x:
                        self.min_filled_x = x
                    break

            for x in range(len(grid[y]) - 1, 0, -1):
                if grid[y][x] != AIR:
                    if x > self.max_filled_x:
                        self.max_filled_x = x
                    break

    def _remove_grid_padding(self, grid: GridData):
        # Remove all outer air-only columns (left/right padding)
        for y in range(0, len(grid)):
            xmin = max(0, self.min_filled_x - 2)
            xmax = min(len(grid[y]) - 1, self.max_filled_x + 2)
            grid[y] = grid[y][xmin:xmax]
        return grid

    def write_all(self):
        for filename, grid in self.pending_writes.items():
            cleaned_grid = self._remove_grid_padding(grid)
            write_grid(cleaned_grid, filename)
        self.pending_writes = {}
