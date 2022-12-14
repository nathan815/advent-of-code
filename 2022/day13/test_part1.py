from day13.part1 import parse_input, check_sides, check_packet_pairs

sample_input = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".strip()


def test_check_packet_pairs():
    assert check_packet_pairs(parse_input(sample_input)) == ([0, 1, 3, 5], 13)


def test_check_sides():
    assert check_sides([], []) == None  # undeterminable, need to check another input
    assert check_sides([1], [2]) == True
    assert check_sides(1, 2) == True
    assert check_sides(2, 1) == False
    assert check_sides([1, 2, 3], [5]) == True
    assert check_sides([1, 2, 3], [1, 2]) == False
    assert check_sides([1, [2, 3]], [1, [5, 6]]) == True
    assert check_sides([1], [1, 5, 6, 7]) == True
    assert check_sides([1, [[2]]], [1, 5, 6, 7]) == True

    # test with samples
    assert check_sides([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == True
    assert check_sides([[1], [2, 3, 4]], [[1], 4]) == True
    assert check_sides(9, [[8, 7, 6]]) == False
    assert check_sides([7, 7, 7, 7], [7, 7, 7]) == False
    assert check_sides([], [3]) == True
    assert check_sides([[[]]], [[]]) == False
    assert (
        check_sides(
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
        )
        == False
    )


def test_parse_input():
    assert parse_input(sample_input) == [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]),
        ([[1], [2, 3, 4]], [[1], 4]),
        ([9], [[8, 7, 6]]),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4]),
        ([7, 7, 7, 7], [7, 7, 7]),
        ([], [3]),
        ([[[]]], [[]]),
        ([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]),
    ]

    sample2 = """
[[0,[[4],1,4],[[9,0,7,1],[4],[0,2,2,3,2],2,4]],[9,10]]
[[0,[2,8,[2,9,3],3,[]],[10],4],[[6,[6,7,7],9,5],[[9]],[2,[0,8,1],[3,6,1]],[[2,6,0],8,[6,2],[0,10,5,8,1]],9]]
""".strip()
    assert parse_input(sample2) == [
        (
            [[0, [[4], 1, 4], [[9, 0, 7, 1], [4], [0, 2, 2, 3, 2], 2, 4]], [9, 10]],
            [
                [0, [2, 8, [2, 9, 3], 3, []], [10], 4],
                [
                    [6, [6, 7, 7], 9, 5],
                    [[9]],
                    [2, [0, 8, 1], [3, 6, 1]],
                    [[2, 6, 0], 8, [6, 2], [0, 10, 5, 8, 1]],
                    9,
                ],
            ],
        )
    ]

    sample3 = """
[[10,11,12]]
[[12],13,[15,16]]
""".strip()
    assert parse_input(sample3) == [([[10, 11, 12]], [[12], 13, [15, 16]])]
