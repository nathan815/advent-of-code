from day8.part1 import count_visible_trees

def test_count_visible_trees():
    input = [
        '30373',
        '25512',
        '65332',
        '33549',
        '35390',
    ]
    assert count_visible_trees(input) == 21
