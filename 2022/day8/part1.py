from pathlib import Path
import sys


def count_visible_trees(grid: list[list[str]]):
    def check_row(idx: int, start: int, end: int):
        for i in range(start, end):
            if int(grid[idx][i]) >= cell:
                return True
        return False
    
    def check_col(idx: int, start: int, end: int):
        for i in range(start, end):
            if int(grid[i][idx]) >= cell:
                return True
        return False

    num_rows = len(grid)
    num_cols = len(grid[0])
    visible_trees = num_rows * 2 + (num_cols - 2) * 2  # all outside "trees" are visible

    for row_idx in range(1, num_rows-1):
        for col_idx in range(1, num_cols-1):
            cell = int(grid[row_idx][col_idx])

            hidden_left = check_row(row_idx, 0, col_idx)
            hidden_right = check_row(row_idx, col_idx+1, len(grid[row_idx]))
            hidden_above = check_col(col_idx, 0, row_idx)
            hidden_below = check_col(col_idx, row_idx+1, len(grid))

            is_hidden = hidden_left and hidden_right and hidden_above and hidden_below

            if not is_hidden:
                visible_trees += 1

    return visible_trees


def run_day8_part1(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file) as fp:
        lines = fp.read().splitlines()

    print('Day 7 Part 1 - Count Visible Trees in Grid')
    result = count_visible_trees(lines)
    print(result)

    return result


if __name__ == "__main__":
    run_day8_part1()
