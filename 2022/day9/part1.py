
from enum import Enum
import math
from pathlib import Path
import sys
from typing import Tuple

class Direction(Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'


Position = Tuple[int, int]


def move_rope_head(direction: Direction, head: Position, tail: Position) -> Tuple[Position, Position]:
    head_x, head_y = head
    tail_x, tail_y = tail

    # Update head position

    if direction == Direction.UP:
        head_y += 1
    elif direction == Direction.DOWN:
        head_y -= 1
    elif direction == Direction.LEFT:
        head_x -= 1
    elif direction == Direction.RIGHT:
        head_x += 1


    # Calculate distances

    if head_x < 0 and tail_x > 0 or head_x > 0 and tail_x < 0:
        x_dist = abs(head_x) + abs(tail_x)
    else:
        x_dist = abs(head_x - tail_x)

    if head_y < 0 and tail_y > 0 or head_y > 0 and tail_y < 0:
        y_dist = abs(head_y) + abs(tail_y)
    else:
        y_dist = abs(head_y - tail_y)

    # print('x_dist', x_dist, 'y_dist', y_dist)


    # Update tail position

    if x_dist > 1 or y_dist > 1:
        tail_x, tail_y = head

    return (head_x, head_y), (tail_x, tail_y)


def get_tail_positions_after_moves(moves: list[str]):
    head = 0, 0
    tail = 0, 0
    tail_positions: set[Tuple[int, int]] = set([tail])

    for move in moves:
        direction, distance = move.split(' ')
        for _ in range(0, int(distance)):
            # print('current:', head, tail)
            head, tail = move_rope_head(Direction(direction), head, tail)
            # print('updated:', head, tail)
            tail_positions.add(tail)

    return tail_positions


def run(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file) as fp:
        lines = fp.read().splitlines()

    print('Day 9 Part 1 - Number of positions visited by the rope tail')
    result = len(get_tail_positions_after_moves(lines))
    print(result)

    return result


if __name__ == "__main__":
    run()
