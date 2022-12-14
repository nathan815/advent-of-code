from day14.part1 import build_grid_from_input, write_grid, fill_with_sand, ROCK, AIR, SAND

sample_input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".strip()


def test_fill_with_sand():
    grid, _, sand_start = build_grid_from_input(sample_input)
    sand_count, grid = fill_with_sand(grid, sand_start_x=sand_start, output_file_prefix="sample")

    assert sand_count == 24


def test_build_grid_from_input():
    grid, line_segments, _ = build_grid_from_input(sample_input)

    # write_grid(grid, filename="generated/sample_grid_parsed.txt")

    def x(v):
        return v - 494

    assert line_segments == [
        [(x(498), 4), (x(498), 6), (x(496), 6)],
        [(x(503), 4), (x(502), 4), (x(502), 9), (x(494), 9)],
    ]

    assert len(grid) == 10
    assert len(grid[0]) == 10

    assert grid[0][0] == AIR
    assert grid[8][0] == AIR

    assert grid[9][x(503)] == AIR
    assert grid[4][x(497)] == AIR
    assert grid[4][x(498)] == ROCK
    assert grid[5][x(498)] == ROCK
    assert grid[5][x(499)] == AIR
    assert grid[6][x(498)] == ROCK
    assert grid[6][x(497)] == ROCK
    assert grid[6][x(496)] == ROCK
    assert grid[6][x(495)] == AIR
    assert grid[4][x(503)] == ROCK
    assert grid[4][x(502)] == ROCK
    assert grid[5][x(502)] == ROCK
    assert grid[6][x(502)] == ROCK
    assert grid[7][x(502)] == ROCK
    assert grid[8][x(502)] == ROCK
    assert grid[9][x(502)] == ROCK
    assert grid[9][x(501)] == ROCK
    assert grid[9][x(500)] == ROCK
    assert grid[9][x(499)] == ROCK
    assert grid[9][x(498)] == ROCK
    assert grid[9][x(497)] == ROCK
    assert grid[9][x(496)] == ROCK
    assert grid[9][x(495)] == ROCK
    assert grid[9][x(494)] == ROCK
    assert grid[9][x(493)] == AIR
