from pathlib import Path
import sys


def find_max_scenic_score(grid: list[str]):
    def calculate_row(cell: int, idx: int, start: int, end: int):
        visible_trees = 0
        step = 1 if start < end else -1
        for i in range(start, end, step):
            visible_trees += 1
            if int(grid[idx][i]) >= cell:
                break
        return visible_trees
    
    def calculate_col(cell: int, idx: int, start: int, end: int):
        visible_trees = 0
        step = 1 if start < end else -1
        for i in range(start, end, step):
            visible_trees += 1
            if int(grid[i][idx]) >= cell:
                break
        return visible_trees

    num_rows = len(grid)
    num_cols = len(grid[0])
    max_cell_score = 0

    for row_idx in range(1, num_rows-1):
        for col_idx in range(1, num_cols-1):
            cell = int(grid[row_idx][col_idx])

            left = calculate_row(cell, row_idx, start=col_idx-1, end=-1)
            right = calculate_row(cell, row_idx, start=col_idx+1, end=len(grid[row_idx]))
            up = calculate_col(cell, col_idx, start=row_idx-1, end=-1)
            down = calculate_col(cell, col_idx, start=row_idx+1, end=len(grid))
            cell_score = left * right * up * down

            # print('row_idx', row_idx, 'col_idx', col_idx, 'cell', cell, 'left', left, 'right', right, 'up', up, 'down', down, 'cell_score', cell_score)

            if cell_score > max_cell_score:
                max_cell_score = cell_score

    return max_cell_score



def run_day8_part2(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file) as fp:
        lines = fp.read().splitlines()

    print('Day 8 Part 2 - Max Tree Scenic Score')
    result = find_max_scenic_score(lines)
    print(result)

    return result


if __name__ == "__main__":
    run_day8_part2()
