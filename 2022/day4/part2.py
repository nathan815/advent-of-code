from pathlib import Path
import sys
from typing import List, Tuple

IntRange = Tuple[int, int]

# Accidentally already solved part2 in part1 :D

def check_if_ranges_overlap(r1: IntRange, r2: IntRange):
    # Returns true if r1 overlaps r2 or vice-versa
    r1_start, r1_end = r1
    r2_start, r2_end = r2
    r1_overlaps_r2 = (r1_start >= r2_start and r1_start <= r2_end) or (r1_end >= r2_start and r1_end <= r2_end)
    r2_overlaps_r1 = (r2_start >= r1_start and r2_start <= r1_end) or (r2_end >= r1_start and r2_end <= r1_end)
    return r1_overlaps_r2 or r2_overlaps_r1


def count_overlapping_compartment_assignment_pairs(pairs: List[Tuple[IntRange, IntRange]]) -> int:
    result = 0
    for range1, range2 in pairs:
        if check_if_ranges_overlap(range1, range2):
            result += 1
    return result


def parse_lines_to_range_pairs(lines: list[str]) -> List[Tuple[IntRange, IntRange]]:
    pairs = []
    for line in lines:
        r1, r2 = line.split(',')
        r1_start, r1_end = r1.split('-')
        r2_start, r2_end = r2.split('-')
        r1 = int(r1_start), int(r1_end)
        r2 = int(r2_start), int(r2_end)
        pairs.append((r1, r2))
    return pairs


def run_day4_part2(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file, 'r') as fp:
        lines = fp.read().splitlines()

    print('Day 4 Part 2 - Count overlapping compartment assignment pairs')
    pairs = parse_lines_to_range_pairs(lines)
    result = count_overlapping_compartment_assignment_pairs(pairs)
    print(result)

    return result

def tests():
    assert check_if_ranges_overlap((1,2), (3,4)) == False
    assert check_if_ranges_overlap((1,2), (12,54)) == False
    assert check_if_ranges_overlap((1,2), (2,5)) == True
    assert check_if_ranges_overlap((3,8), (5,15)) == True
    assert check_if_ranges_overlap((20,24), (27,30)) == False
    assert check_if_ranges_overlap((20,24), (21,30)) == True
    assert check_if_ranges_overlap((6,43), (21,152)) == True

    assert check_if_ranges_overlap((2,4), (6,8)) == False
    assert check_if_ranges_overlap((2,3), (4,5)) == False
    assert check_if_ranges_overlap((5,7), (7,9)) == True
    assert check_if_ranges_overlap((2,8), (3,7)) == True
    assert check_if_ranges_overlap((6,6), (4,6)) == True
    assert check_if_ranges_overlap((2,6), (4,8)) == True

    assert parse_lines_to_range_pairs(['1-2,3-4', '10-14,12-95']) == [((1,2),(3,4)), ((10,14),(12,95))]
    assert parse_lines_to_range_pairs(['1-2,3-4']) == [((1,2),(3,4))]

    result = count_overlapping_compartment_assignment_pairs([
        ((1,2), (2,3)),
        ((2,4), (5,8)),
        ((5,11), (8,10)),
    ])
    assert result == 2, result

    sample = run_day4_part2('sample_input.txt')
    assert sample == 4, sample


if __name__ == "__main__":
    tests()
    run_day4_part2()
