
from enum import Enum
from pathlib import Path
import sys
from typing import Tuple


class Direction(Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'


Position = Tuple[int, int]


def move_rope_head(direction: Direction, knot_positions: list[Position]) -> Tuple[Position, list[Position]]:
    head = knot_positions[0]
    head_x, head_y = head

    # Update head position

    if direction == Direction.UP:
        head_y += 1
    elif direction == Direction.DOWN:
        head_y -= 1
    elif direction == Direction.LEFT:
        head_x -= 1
    elif direction == Direction.RIGHT:
        head_x += 1

    new_head = (head_x, head_y)
    knot_positions[0] = new_head

    for knot_idx in range(1, len(knot_positions)):
        follow_x, follow_y = knot_positions[knot_idx-1]
        knot_x, knot_y = knot_positions[knot_idx]

        # Calculate distance to the knot the current one needs to follow
        if follow_x < 0 and knot_x > 0 or follow_x > 0 and knot_x < 0:
            x_dist = abs(follow_x) + abs(knot_x)
        else:
            x_dist = abs(follow_x - knot_x)

        if follow_y < 0 and knot_y > 0 or follow_y > 0 and knot_y < 0:
            y_dist = abs(follow_y) + abs(knot_y)
        else:
            y_dist = abs(follow_y - knot_y)

        # print('knot_idx', knot_idx, 'x_dist', x_dist, 'y_dist', y_dist, knot_positions)
        # print('comparing:', knot_positions[knot_idx-1], knot_positions[knot_idx])

        # Update knot position
        if knot_x == follow_x and knot_y != follow_y:
            if y_dist > 1 and knot_y < follow_y:
                knot_y += 1
            elif y_dist > 1 and knot_y > follow_y:
                knot_y -= 1

        elif knot_x != follow_x and knot_y == follow_y:
            if x_dist > 1 and knot_x < follow_x:
                knot_x += 1
            elif x_dist > 1 and knot_x > follow_x:
                knot_x -= 1

        elif x_dist > 1 or y_dist > 1:
            # left-below
            if knot_x < follow_x and knot_y < follow_y:
                knot_x += 1
                knot_y += 1
            
            # right-below
            elif knot_x > follow_x and knot_y < follow_y:
                knot_x -= 1
                knot_y += 1
            
            # right-above
            elif knot_x > follow_x and knot_y > follow_y:
                knot_x -= 1
                knot_y -= 1
            
            # left-above
            elif knot_x < follow_x and knot_y > follow_y:
                knot_x += 1
                knot_y -= 1
        
        knot_positions[knot_idx] = (knot_x, knot_y)

    return knot_positions


def move_head_by_distance(direction: Direction, distance: int, knot_positions: list[Position]):
    visited_tail_positions: set[Position] = set()

    cur_knot_positions = knot_positions
    for _ in range(0, distance):
        cur_knot_positions = move_rope_head(direction, cur_knot_positions)
        visited_tail_positions.add(cur_knot_positions[-1])

    return cur_knot_positions, visited_tail_positions


def get_tail_positions_after_moves(moves: list[str], knot_count: int = 10):
    knot_positions: list[Position] = [(0, 0) for i in range(0, knot_count)]
    visited_tail_positions: set[Position] = set([knot_positions[-1]])

    for move in moves:
        direction, distance = move.split(' ')
        # print('\n-----Move', move, knot_positions)
        knot_positions, tail_new_visited = move_head_by_distance(Direction(direction), int(distance), knot_positions)
        visited_tail_positions.update(tail_new_visited)

    return visited_tail_positions


def run(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file) as fp:
        lines = fp.read().splitlines()

    print('Day 9 Part 2 - Number of positions visited by the rope tail with variable-length knots (10)')
    result = len(get_tail_positions_after_moves(lines))
    print(result)

    return result


if __name__ == "__main__":
    run()
