from pathlib import Path
from part2 import run_day5_part2, parse_text_input, CargoShip, CrateMove


def test_CargoShip_add_crate_to_stack_from_bottom():
    ship = CargoShip()
    ship.add_crate_to_stack_from_bottom(0, 'A')
    ship.add_crate_to_stack_from_bottom(0, 'B')
    ship.add_crate_to_stack_from_bottom(0, 'C')
    assert ship.crate_stacks[0] == ['A', 'B', 'C']


def test_CargoShip_add_crate_to_stack():
    ship = CargoShip()
    ship.add_crate_to_stack(0, 'A')
    ship.add_crate_to_stack(0, 'B')
    ship.add_crate_to_stack(0, 'C')
    assert ship.crate_stacks[0] == ['C', 'B', 'A']

    ship.add_crate_to_stack(1, 'E')
    ship.add_crate_to_stack(1, 'F')
    ship.add_crate_to_stack(1, 'G')
    ship.add_crate_to_stack(1, 'H')
    assert ship.crate_stacks[1] == ['H', 'G', 'F', 'E']


def test_CargoShip_add_and_remove_crates():
    ship = CargoShip()
    ship.add_crate_to_stack(0, 'A')
    ship.add_crate_to_stack(0, 'B')
    ship.add_crate_to_stack(0, 'C')
    assert ship.crate_stacks[0] == ['C', 'B', 'A']

    ship.remove_crate_from_stack(0)
    assert ship.crate_stacks[0] == ['B', 'A']

    ship.remove_crate_from_stack(0)
    assert ship.crate_stacks[0] == ['A']

    ship.remove_crate_from_stack(0)
    assert ship.crate_stacks[0] == []


def test_CargoShip_move_crate():
    ship = CargoShip()
    ship.add_crate_to_stack(0, 'A')
    ship.add_crate_to_stack(0, 'B')
    ship.add_crate_to_stack(0, 'C')
    assert ship.crate_stacks[0] == ['C', 'B', 'A']

    ship.add_crate_to_stack(1, 'X')
    ship.add_crate_to_stack(1, 'Y')
    assert ship.crate_stacks[1] == ['Y', 'X']

    ship.add_crate_to_stack(2, 'T')
    assert ship.crate_stacks[2] == ['T']

    ship.move_crate(0, 1)
    assert ship.crate_stacks[0] == ['B', 'A']
    assert ship.crate_stacks[1] == ['C', 'Y', 'X']

    ship.move_crate(1, 2)
    assert ship.crate_stacks[1] == ['Y', 'X']
    assert ship.crate_stacks[2] == ['C', 'T']


def test_CargoShip_move_crates():
    ship = CargoShip()
    ship.add_crate_to_stack(0, 'A')
    ship.add_crate_to_stack(0, 'B')
    ship.add_crate_to_stack(0, 'C')
    assert ship.crate_stacks[0] == ['C', 'B', 'A']

    ship.add_crate_to_stack(1, 'X')
    ship.add_crate_to_stack(1, 'Y')
    assert ship.crate_stacks[1] == ['Y', 'X']

    ship.add_crate_to_stack(2, 'T')
    assert ship.crate_stacks[2] == ['T']

    ship.move_crates(3, 0, 1)
    assert ship.crate_stacks[0] == []
    assert ship.crate_stacks[1] == ['C', 'B', 'A', 'Y', 'X']

    ship.move_crates(2, 1, 2)
    assert ship.crate_stacks[1] == ['A', 'Y', 'X']
    assert ship.crate_stacks[2] == ['C', 'B', 'T']


def test_CargoShip_run_crate_moves():
    ship = CargoShip()
    ship.add_crate_to_stack(0, 'A')
    ship.add_crate_to_stack(0, 'B')
    ship.add_crate_to_stack(0, 'C')
    assert ship.crate_stacks[0] == ['C', 'B', 'A']

    ship.add_crate_to_stack(1, 'X')
    ship.add_crate_to_stack(1, 'Y')
    assert ship.crate_stacks[1] == ['Y', 'X']

    ship.add_crate_to_stack(2, 'T')
    assert ship.crate_stacks[2] == ['T']

    moves = [
        CrateMove(crate_count=1, from_stack=0, to_stack=1),
        CrateMove(crate_count=1, from_stack=0, to_stack=2),
        CrateMove(crate_count=2, from_stack=1, to_stack=0),
        CrateMove(crate_count=3, from_stack=0, to_stack=1),
    ]
    ship.run_crate_moves(moves)

    assert ship.crate_stacks == [
        [],
        ['C', 'Y', 'A', 'X'],
        ['B', 'T']
    ]


def test_CargoShip_get_top_crates_message():
    ship = CargoShip()
    ship.add_crate_to_stack(0, 'A')
    ship.add_crate_to_stack(0, 'B')
    ship.add_crate_to_stack(0, 'C')
    ship.add_crate_to_stack(1, 'X')
    ship.add_crate_to_stack(1, 'Y')
    ship.add_crate_to_stack(2, 'T')
    assert ship.get_top_crates_message() == 'CYT'


def test_parse_text_input():
    cargo_ship, moves = parse_text_input([
        '    [D]    ',
        '[N] [C]    ',
        '[Z] [M] [P]',
        '1   2   3 ',
        '',
        'move 1 from 1 to 3',
        'move 2 from 2 to 3',
        'move 4 from 3 to 1',
    ])
    assert cargo_ship.crate_stacks == [
        ['N', 'Z'],
        ['D', 'C', 'M'],
        ['P'],
    ]

    assert moves == [
        CrateMove(crate_count=1, from_stack=0, to_stack=2),
        CrateMove(crate_count=2, from_stack=1, to_stack=2),
        CrateMove(crate_count=4, from_stack=2, to_stack=0),
    ]


def test_run_with_sample_input():
    cur_dir = Path(__file__).parent
    assert run_day5_part2(str(cur_dir / 'sample_input.txt')) == 'MCD'
