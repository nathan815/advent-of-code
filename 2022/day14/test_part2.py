from day14.part2 import build_grid_from_input, fill_with_sand, ROCK, AIR, SAND

sample_input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".strip()


def test_fill_with_sand():
    grid, _ = build_grid_from_input(sample_input)
    sand_count, grid = fill_with_sand(grid, output_file_prefix="sample")

    assert sand_count == 93


def test_build_grid_from_input():
    grid, line_segments = build_grid_from_input(sample_input)

    assert line_segments == [
        [(498, 4), (498, 6), (496, 6)],
        [(503, 4), (502, 4), (502, 9), (494, 9)],
    ]

    assert len(grid) == 11
    assert len(grid[0]) == 1000

    assert grid[0][0] == AIR
    assert grid[8][0] == AIR

    assert grid[9][503] == AIR
    assert grid[4][497] == AIR
    assert grid[4][498] == ROCK
    assert grid[5][498] == ROCK
    assert grid[5][499] == AIR
    assert grid[6][498] == ROCK
    assert grid[6][497] == ROCK
    assert grid[6][496] == ROCK
    assert grid[6][495] == AIR
    assert grid[4][503] == ROCK
    assert grid[4][502] == ROCK
    assert grid[5][502] == ROCK
    assert grid[6][502] == ROCK
    assert grid[7][502] == ROCK
    assert grid[8][502] == ROCK
    assert grid[9][502] == ROCK
    assert grid[9][501] == ROCK
    assert grid[9][500] == ROCK
    assert grid[9][499] == ROCK
    assert grid[9][498] == ROCK
    assert grid[9][497] == ROCK
    assert grid[9][496] == ROCK
    assert grid[9][495] == ROCK
    assert grid[9][494] == ROCK
    assert grid[9][493] == AIR
