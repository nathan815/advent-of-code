from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Tuple

LineList = list[list[Tuple[int, int]]]
GridData = list[list[str]]

SAND_START_X = 500

ROCK = "█"
AIR = " "
SAND = "."
START_SAND = "+"


def fill_with_sand(grid: GridData, sand_start_x: int, output_file_prefix=None):
    if output_file_prefix:
        write_grid(grid, filename=f"{output_file_prefix}_0_start.txt")

    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    resting_sand_count = 0
    running = True
    while running:
        x = sand_start_x

        for y in range(1, len(grid)):
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
            elif down_left is None or down_right is None:
                running = False
                break
            elif down_left != AIR or down_right != AIR:
                grid[y][x] = SAND
                resting_sand_count += 1
                if output_file_prefix:
                    write_grid(
                        grid, filename=f"{output_file_prefix}_{resting_sand_count}.txt"
                    )
                break

    return resting_sand_count, grid


def write_grid(
    grid: GridData, filename="grid.txt", directory=Path(__file__).parent / "generated"
):
    with open(directory / filename, "w") as f:
        f.write("\n".join(["".join(row_chars) for row_chars in grid]))


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

    # Offset x values by the minimum x so we don't store unneeded array items
    for line in lines:
        for i in range(0, len(line)):
            x, y = line[i]
            line[i] = (x - min_x), y

    grid = []

    sand_start_x = SAND_START_X - min_x
    width = max(max_x - min_x + 1, sand_start_x)
    height = max_y + 1

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

    grid[0][sand_start_x] = START_SAND

    return grid, lines, sand_start_x


def run(
    file=sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / "input.txt",
):
    with open(file) as fp:
        input = fp.read()

    print("Day 14 Part 1 - Number of units of resting sand")
    grid, lines, sand_start_x = build_grid_from_input(input)
    write_grid(grid, "real_start.txt")
    answer, grid = fill_with_sand(grid, sand_start_x)
    write_grid(grid, "real_end.txt")
    # print(lines)
    print(answer)

    return answer


if __name__ == "__main__":
    run()
