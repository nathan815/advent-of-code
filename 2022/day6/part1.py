from pathlib import Path
import sys

def find_start_of_packet_market(buffer: str):
    seen_chars = []

    for i, char in enumerate(buffer):
        if len(seen_chars) == 4:
            seen_chars.pop(0)

        seen_chars.append(char)

        if len(set(seen_chars)) == 4:
            return i + 1


def run_day6_part1(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file, 'r') as fp:
        lines = fp.read().splitlines()

    signal_buffer = lines[0]

    result = find_start_of_packet_market(signal_buffer)
    print('Day 6 Part 1 - Find Start of First Packet Marker')
    print(result)

    return result

if __name__ == "__main__":
    run_day6_part1()
