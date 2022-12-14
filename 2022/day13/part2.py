import functools
from itertools import zip_longest
from pathlib import Path
from pprint import pprint
import sys
from typing import Union

from day13.part1 import check_sides


RecursiveIntList = list[Union["RecursiveIntList", int]]
Packet = list[RecursiveIntList]


def find_decoder_key(packets: list[Packet]):
    """Returns correct packet pair indicies and the sum of them"""

    DIVIDER_PACKETS = [[[2]], [[6]]]

    def compare(a, b):
        # Comparator function for sorting items built from our existing comparison logic from part1.
        res = check_sides(a, b, debug=False)
        if res is True:
            return -1
        elif res is False:
            return 1
        else:
            return 0

    packets_with_dividers = packets + DIVIDER_PACKETS
    sorted_packets = sorted(packets_with_dividers, key=functools.cmp_to_key(compare))

    decoder_key = 1
    for idx, packet in enumerate(sorted_packets):
        if packet in DIVIDER_PACKETS:
            decoder_key = decoder_key * (idx + 1)

    return decoder_key, sorted_packets


def parse_input(input: str) -> list[Packet]:
    packets = []
    for line in input.splitlines():
        if line.strip() == "":
            continue
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

            elif char == "]":
                if len(stack) > 1:
                    stack.pop()

            elif char != ",":
                cur_value += char

        packets.append(stack[0])

    return packets


def run(
    file=sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / "input.txt",
):
    with open(file) as fp:
        input = fp.read()

    print("Day 13 Part 2 - Decoder Key (Product of control packet indices)")
    answer, packets = find_decoder_key(parse_input(input))
    # pprint(packets)
    print(answer)

    return answer


if __name__ == "__main__":
    run()
