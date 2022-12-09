from day8.part2 import find_max_scenic_score

def test_find_max_scenic_score():
    input = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390',
    ]
    assert find_max_scenic_score(input) == 8
