from itertools import zip_longest
from pathlib import Path
from pprint import pprint
import sys


def check_sides(left, right, idx=0, debug=True, level=0):
    def iprint(*args):
        if debug:
            print(('  ' * level) + str(args[0]), *args[1:])

    iprint(f'Compare #{idx}', left, '  VS   ', right)
    if not isinstance(left, list):
        left = [left]
    if not isinstance(right, list):
        right = [right]

    if len(left) == 0 and len(right) == 0:
        iprint('Both empty - continue checking next input', left, right)
        return None

    for leftitem, rightitem in zip_longest(left, right):
        # print('leftitem', leftitem, 'rightitem', rightitem)
        if leftitem is None:
            iprint('OK - left ran out first. returning True', idx if level == 0 else '')
            return True

        if rightitem is None:
            iprint('BAD - right ran out first. returning False', idx if level == 0 else '')
            return False

        if isinstance(leftitem, int) and isinstance(rightitem, int):
            if leftitem == rightitem:
                continue
            else:
                iprint('Check', leftitem, '<', rightitem, 'returning', leftitem < rightitem, idx if level == 0 else '')
                return leftitem < rightitem
        else:
            check = check_sides(leftitem, rightitem, idx, level=level+1)
            if check is not None:
                iprint('returning', check, idx if level == 0 else '')
                return check

    return None


def check_packet_pairs(packet_pairs: list[tuple[int | list, int | list]]):
    """Returns correct packet pair indicies and the sum of them"""
    correct_pair_indices = []
    for pair_idx, pair in enumerate(packet_pairs):
        p1, p2 = pair
        if check_sides(p1, p2, pair_idx):
            correct_pair_indices.append(pair_idx)

    sum = 0
    for i in correct_pair_indices:
        sum += (i + 1)

    return correct_pair_indices, sum


def parse_input(input: str):
    packet_line_pairs = input.split("\n\n")
    pairs = []
    for line_pair in packet_line_pairs:
        line_pair = line_pair.splitlines()
        pair = ()
        for line in line_pair:
            # print('line', line)
            stack = []
            cur_list_idx = 0
            cur_value = ""
            for char in line:
                if cur_value != "" and (char == "]" or char == ","):
                    stack[-1].append(int(cur_value))
                    cur_value = ""

                if char == "[":
                    new_list = []
                    stack.append(new_list)
                    cur_list_idx = len(stack) - 1
                    if cur_list_idx > 0:
                        stack[cur_list_idx - 1].append(new_list)

                    # print('OPEN', 'cur_list_idx', cur_list_idx, stack)
                elif char == "]":
                    if len(stack) > 1:
                        stack.pop()

                elif char != ",":
                    cur_value += char

            # print('stack', stack)
            line_list = stack[0]
            pair += (line_list,)

        pairs.append(pair)

    print()
    pprint(pairs)

    return pairs


def run(
    file=sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / "input.txt",
):
    with open(file) as fp:
        input = fp.read()

    print("Day 12 Part 1 - Level of Monkey Business")
    indices, result = check_packet_pairs(parse_input(input))
    print(indices)
    print(result)

    return result


if __name__ == "__main__":
    run()
