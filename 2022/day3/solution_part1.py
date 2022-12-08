from pathlib import Path
import sys
import math

def find_duplicate_items_in_rucksack(rucksack: str):
    mid = math.ceil(len(rucksack)/2)
    compartment1 = rucksack[0:mid]
    compartment2 = rucksack[mid:]
    # print(rucksack, compartment1, compartment2)
    duplicate_items = set()
    for item in compartment1:
        if item in compartment2:
            duplicate_items.add(item)
    return duplicate_items


def get_rucksack_item_priority(item: str):
    # Item priorities:
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.

    priority_a = 1
    priority_A = 27

    # ASCII codes: A-Z 65-90 a-z 97-122
    code_A = ord('A') # 65
    code_Z = ord('Z') # 90
    code_a = ord('a') # 97
    code_z = ord('z') # 122

    upper_priority_code_diff = priority_A - code_A
    lower_priority_code_diff = priority_a - code_a
    
    code = ord(item)

    if code >= code_A and code <= code_Z:
        return code + upper_priority_code_diff

    if code >= code_a and code <= code_z:
        return code + lower_priority_code_diff


def sum_duplicate_items_in_rucksack_compartments(lines: list[str]):
    sum = 0
    for line in lines:
        rucksack = line.strip()
        items = find_duplicate_items_in_rucksack(rucksack)
        # print('rucksack:', rucksack, 'Duplicate items:',items)
        for item in items:
            sum += get_rucksack_item_priority(item)
    return sum


def run_day3_part1(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file, 'r') as fp:
        lines = fp.readlines()

    print('Day 3 Part 1 - Sum of priorities of items appearing in both rucksack compartments')
    result = sum_duplicate_items_in_rucksack_compartments(lines)
    print(result)



def tests():
    assert find_duplicate_items_in_rucksack('abdezyxa') == {'a'}
    assert find_duplicate_items_in_rucksack('abdefzyxae') == {'a', 'e'}
    assert find_duplicate_items_in_rucksack('vJrwpWtwJgWrhcsFMMfFFhFp') == {'p'}

    assert get_rucksack_item_priority('a') == 1
    assert get_rucksack_item_priority('p') == 16
    assert get_rucksack_item_priority('z') == 26
    assert get_rucksack_item_priority('A') == 27
    assert get_rucksack_item_priority('L') == 38
    assert get_rucksack_item_priority('Z') == 52

    assert sum_duplicate_items_in_rucksack_compartments(['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn']) == 22
    assert sum_duplicate_items_in_rucksack_compartments(['abcxyz']) == 0
    assert sum_duplicate_items_in_rucksack_compartments(['AxYA']) == 27

    sample_input = [
        'vJrwpWtwJgWrhcsFMMfFFhFp\n',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n',
        'PmmdzqPrVvPwwTWBwg\n',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n',
        'ttgJtRGJQctTZtZT\n',
        'CrZsJsPPZsGzwwsLwLmpwMDw\n',
    ]
    assert sum_duplicate_items_in_rucksack_compartments(sample_input) == 157

if __name__ == "__main__":
    tests()
    run_day3_part1()
