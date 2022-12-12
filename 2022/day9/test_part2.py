from day9.part2 import move_rope_head, get_tail_positions_after_moves, move_head_by_distance, Direction


def test_get_tail_positions_after_moves():
    assert get_tail_positions_after_moves(['R 1']) == {(0,0)}
    assert get_tail_positions_after_moves(['R 2']) == {(0,0)}
    assert get_tail_positions_after_moves(['R 3']) == {(0,0)}
    assert get_tail_positions_after_moves(['R 9']) == {(0,0)}
    assert get_tail_positions_after_moves(['R 10']) == {(0,0), (1,0)}

    assert get_tail_positions_after_moves(['R 11']) == {(0,0), (1,0), (2,0)}

    assert get_tail_positions_after_moves(['R 2', 'D 1']) == {(0,0)}


def test_move_head_by_distance__with_sample():
    # R 4
    # U 4
    # L 3
    # D 1
    # R 4
    # D 1
    # L 5
    # R 2

    knot_positions = [(0, 0) for _ in range(0, 10)]

    knot_positions, _ = move_head_by_distance(Direction.RIGHT, 4, knot_positions)
    assert knot_positions == [
        (4, 0),
        (3, 0),
        (2, 0),
        (1, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ]

    knot_positions, _ = move_head_by_distance(Direction.UP, 4, knot_positions)
    assert knot_positions == [
        (4, 4),
        (4, 3),
        (4, 2),
        (3, 2),
        (2, 2),
        (1, 1),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ]

    knot_positions, _ = move_head_by_distance(Direction.LEFT, 3, knot_positions)
    assert knot_positions == [
        (1, 4),
        (2, 4),
        (3, 3),
        (3, 2),
        (2, 2),
        (1, 1),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ]

    knot_positions, _ = move_head_by_distance(Direction.DOWN, 1, knot_positions)
    assert knot_positions == [
        (1, 3),
        (2, 4),
        (3, 3),
        (3, 2),
        (2, 2),
        (1, 1),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ]


def test_get_tail_positions_after_moves__with_sample():
    sample_input = [
        'R 4',
        'U 4',
        'L 3',
        'D 1',
        'R 4',
        'D 1',
        'L 5',
        'R 2',
    ]
    assert len(get_tail_positions_after_moves(sample_input)) == 1
