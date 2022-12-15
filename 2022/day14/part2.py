import copy
from pathlib import Path
import sys
from typing import Tuple

from day14.grid_writer import QueuedGridWriter

from day14.part1 import (
    GridData,
    LineList,
    AIR,
    SAND,
    START_SAND,
    ROCK,
    SAND_START_X,
)


def fill_with_sand(grid: GridData, output_file_prefix=None):
    writer = QueuedGridWriter()
    if output_file_prefix:
        writer.queue(grid, filename=f"part2/{output_file_prefix}_0_start.txt")

    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    resting_sand_count = 0
    while grid[0][SAND_START_X] != SAND:
        x = SAND_START_X

        for y in range(0, len(grid)):
            under = grid[y + 1][x] if y < max_y else None
            if under == AIR:
                continue

            down_left = grid[y + 1][x - 1] if y < max_y and x > 0 else None
            down_right = grid[y + 1][x + 1] if y < max_y and x < max_x else None

            # print('x', x, 'y', y, 'under', under, 'down_left', down_left, 'down_right', down_right, 'resting_sand_count',)

            if down_left == AIR:
                x -= 1
            elif down_right == AIR:
                x += 1
            elif (
                down_left is None
                or down_right is None
                or down_left != AIR
                or down_right != AIR
            ):
                grid[y][x] = SAND
                resting_sand_count += 1
                if output_file_prefix:
                    writer.queue(
                        grid,
                        filename=f"part2/{output_file_prefix}_{resting_sand_count}.txt",
                    )
                break

    writer.write_all()

    return resting_sand_count, grid


def build_grid_from_input(input: str) -> Tuple[LineList, GridData]:
    lines = []
    min_x = None
    max_x = None
    max_y = None

    for line_txt in input.splitlines():
        points = []
        points_txt = line_txt.split("->")
        for point_txt in points_txt:
            x, y = point_txt.strip().split(",")
            x = int(int(x))
            y = int(y)

            if min_x is None or x < min_x:
                min_x = x
            if max_x is None or x > max_x:
                max_x = x
            if max_y is None or y > max_y:
                max_y = y

            points.append((x, y))

        lines.append(points)

    width = min(max_x + 1, SAND_START_X) * 2
    height = max_y + 2

    grid = []

    # fill with air
    for _ in range(0, height):
        grid.append([])
        for _ in range(0, width):
            grid[-1].append(AIR)

    # draw rock lines
    for line in lines:
        prev_point = None
        for point in line:
            x, y = point

            if prev_point:
                prev_x, prev_y = prev_point
                if x == prev_x:
                    for i in range(prev_y, y, -1 if prev_y > y else 1):
                        grid[i][x] = ROCK
                elif y == prev_y:
                    for i in range(prev_x, x, -1 if prev_x > x else 1):
                        grid[y][i] = ROCK

            grid[y][x] = ROCK
            prev_point = point

    grid[0][SAND_START_X] = START_SAND

    return grid, lines


def run(
    file=sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / "input.txt",
):
    with open(file) as fp:
        input = fp.read()

    print(
        "Day 14 Part 2 - Number of units of resting sand. Sand no longer falls into the abyss as there is a floor."
    )
    writer = QueuedGridWriter()
    grid, lines = build_grid_from_input(input)
    writer.queue(grid, "part2/real_start.txt")
    answer, grid = fill_with_sand(grid)
    writer.queue(grid, "part2/real_end.txt")
    writer.write_all()
    # print(lines)
    print(answer)

    return answer


if __name__ == "__main__":
    run()
