from day9.part1 import move_rope_head, get_tail_positions_after_moves, Direction

def test_move_rope_head__start_same_row():
    assert move_rope_head(Direction.RIGHT, head=(0, 0), tail=(0, 0)) == ((1, 0), (0, 0))
    assert move_rope_head(Direction.RIGHT, head=(1, 0), tail=(0, 0)) == ((2, 0), (1, 0))
    assert move_rope_head(Direction.LEFT, head=(2, 0), tail=(1, 0)) == ((1, 0), (1, 0))
    assert move_rope_head(Direction.LEFT, head=(1, 0), tail=(1, 0)) == ((0, 0), (1, 0))
    assert move_rope_head(Direction.DOWN, head=(0, 0), tail=(1, 0)) == ((0, -1), (1, 0))
    assert move_rope_head(Direction.DOWN, head=(0, -1), tail=(1, 0)) == ((0, -2), (0, -1)) ##
    assert move_rope_head(Direction.RIGHT, head=(0, -2), tail=(0, -1)) == ((1, -2), (0, -1))
    assert move_rope_head(Direction.RIGHT, head=(1, -2), tail=(0, -1)) == ((2, -2), (1, -2))

# ....
# ....
# ..T.
# ....H


def test_move_rope_head__start_different_row():
    assert move_rope_head(Direction.RIGHT, head=(0, 0), tail=(0, 1)) == ((1, 0), (0, 1))
    assert move_rope_head(Direction.RIGHT, head=(1, 0), tail=(0, 1)) == ((2, 0), (1, 0))
    assert move_rope_head(Direction.RIGHT, head=(2, 0), tail=(1, 0)) == ((3, 0), (2, 0))
    assert move_rope_head(Direction.LEFT, head=(3, 0), tail=(2, 0)) == ((2, 0), (2, 0))
    assert move_rope_head(Direction.LEFT, head=(2, 0), tail=(2, 0)) == ((1, 0), (2, 0))
    assert move_rope_head(Direction.DOWN, head=(1, 0), tail=(2, 0)) == ((1, -1), (2, 0))
    assert move_rope_head(Direction.DOWN, head=(1, -1), tail=(2, 0)) == ((1, -2), (1, -1))
    assert move_rope_head(Direction.RIGHT, head=(1, -2), tail=(1, -1)) == ((2, -2), (1, -1))
    assert move_rope_head(Direction.RIGHT, head=(2, -2), tail=(1, -1)) == ((3, -2), (2, -2))
    assert move_rope_head(Direction.DOWN, head=(3, -2), tail=(2, -2)) == ((3, -3), (2, -2))
    assert move_rope_head(Direction.DOWN, head=(3, -3), tail=(2, -2)) == ((3, -4), (3, -3))
    assert move_rope_head(Direction.LEFT, head=(3, -4), tail=(3, -3)) == ((2, -4), (3, -3))


def test_get_tail_positions_after_moves():
    assert get_tail_positions_after_moves(['R 1']) == {(0,0)}
    assert get_tail_positions_after_moves(['R 2']) == {(0,0), (1, 0)}
    assert get_tail_positions_after_moves(['R 3']) == {(0,0), (1, 0), (2,0)}
    assert get_tail_positions_after_moves(['R 2', 'D 1']) == {(0,0), (1, 0)}

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
    assert len(get_tail_positions_after_moves(sample_input)) == 13
