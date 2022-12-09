from dataclasses import dataclass
from pathlib import Path
import sys
import re
from typing import Tuple


@dataclass
class CrateMove:
    crate_count: int
    from_stack: int
    to_stack: int

    def __post_init__(self):
        if self.from_stack < 0 or self.to_stack < 0:
            raise ValueError('from_stack or to_stack out of range')


class CargoShip:
    def __init__(self):
        self.crate_stacks: list[list[str]] = []

    def move_crate(self, from_stack: int, to_stack: int):
        crate = self.remove_crate_from_stack(from_stack)
        if crate is not None:
            self.add_crate_to_stack(to_stack, crate)

    def move_crates(self, count: int, from_stack: int, to_stack: int):
        crates = []
        for _ in range(0, count):
            crates.append(self.remove_crate_from_stack(from_stack))
        crates.reverse()
        for crate in crates:
            self.add_crate_to_stack(to_stack, crate)

    def add_crate_to_stack(self, stack: int, crate: str):
        self.get_stack(stack).insert(0, crate)

    def add_crate_to_stack_from_bottom(self, stack: int, crate: str):
        self.get_stack(stack).append(crate)

    def remove_crate_from_stack(self, stack: int):
        if len(self.get_stack(stack)) > 0:
            return self.get_stack(stack).pop(0)

    def run_crate_moves(self, moves: list[CrateMove]):
        for move in moves:
            self.move_crates(move.crate_count, move.from_stack, move.to_stack)
    
    def get_top_crates_message(self) -> str:
        top_crates = []
        for stack in self.crate_stacks:
            if len(stack) > 0:
                top_crates.append(stack[0])
        return ''.join(top_crates)

    def get_stack(self, idx):
        while idx > len(self.crate_stacks)-1:
            self.crate_stacks.append([])
        return self.crate_stacks[idx]


def parse_text_input(lines: list[str]) -> Tuple[CargoShip, list[CrateMove]]:
    ship = CargoShip()
    moves = []
    parsing_crates = True

    move_line_regex = re.compile(r'move (\d+) from (\d) to (\d)')

    for line in lines:
        if line == '':
            parsing_crates = False
            continue

        if parsing_crates:
            stack_num = None
            for char_idx, char in enumerate(line):
                if char == '[':
                    # each crate is 4 total chars: '[A] '
                    stack_num = int(char_idx / 4)
                elif char == ']' or char == ' ':
                    continue
                elif stack_num is not None:
                    ship.add_crate_to_stack_from_bottom(stack_num, char)
        else:
            matches = move_line_regex.findall(line)
            if len(matches) > 0:
                match = matches[0]
                moves.append(CrateMove(
                    crate_count = int(match[0]),
                    from_stack = int(match[1]) - 1,
                    to_stack = int(match[2]) - 1,
                ))

    return ship, moves


def run(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file, 'r') as fp:
        lines = fp.read().splitlines()

    print('Day 5 Part 2 - Message from top of cargo ship stacks after rearrangements. Multiple crates moved at once maintain order.')
    ship, moves = parse_text_input(lines)
    ship.run_crate_moves(moves)
    result = ship.get_top_crates_message()
    print(result)

    return result

if __name__ == "__main__":
    run()
