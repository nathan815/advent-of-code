from pathlib import Path
import sys


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


def find_badge_item_for_elf_group(elf_rucksacks: list[str]):
    item_counts = {}

    for rucksack in elf_rucksacks:
        current_rucksack_set = set()
        for item in rucksack:
            if item not in current_rucksack_set:
                item_counts[item] = item_counts.get(item, 0) + 1
            current_rucksack_set.add(item)
    
    for key, count in item_counts.items():
        if count == len(elf_rucksacks):
            return key


def sum_priority_of_elf_group_badges(lines, group_size=3):
    priority_sum = 0
    current_group = []
    
    for line in lines:
        rucksack = line.strip()
        current_group.append(rucksack)
        # print(rucksack, len(current_group))
        if len(current_group) == group_size:
            badge_item = find_badge_item_for_elf_group(current_group)
            item_priority = get_rucksack_item_priority(badge_item)
            # print('current_group', current_group, 'badge_item', badge_item, 'item_priority', item_priority)
            priority_sum += item_priority
            current_group = []

    return priority_sum


def run_day3_part2(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file, 'r') as fp:
        lines = fp.readlines()

    print('Day 3 Part 2 - Sum of priorities of elf rucksack group badges')
    result = sum_priority_of_elf_group_badges(lines)
    print(result)


def tests():
    assert get_rucksack_item_priority('a') == 1
    assert get_rucksack_item_priority('p') == 16
    assert get_rucksack_item_priority('z') == 26
    assert get_rucksack_item_priority('A') == 27
    assert get_rucksack_item_priority('L') == 38
    assert get_rucksack_item_priority('Z') == 52

    assert find_badge_item_for_elf_group([
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
    ]) == 'r'

    sample_input = [
        'vJrwpWtwJgWrhcsFMMfFFhFp\n',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n',
        'PmmdzqPrVvPwwTWBwg\n',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n',
        'ttgJtRGJQctTZtZT\n',
        'CrZsJsPPZsGzwwsLwLmpwMDw\n',
    ]
    assert sum_priority_of_elf_group_badges(sample_input) == 70


if __name__ == "__main__":
    tests()
    run_day3_part2()
