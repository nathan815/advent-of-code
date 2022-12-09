from pathlib import Path
import sys


def find_start_of_unique_message_marker(buffer: str, marker_length=14):
    seen_chars = []

    for i, char in enumerate(buffer):
        if len(seen_chars) == marker_length:
            seen_chars.pop(0)

        seen_chars.append(char)

        if len(set(seen_chars)) == marker_length:
            return i + 1


def run(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file, 'r') as fp:
        lines = fp.read().splitlines()

    signal_buffer = lines[0]

    result = find_start_of_unique_message_marker(signal_buffer)
    print('Day 6 Part 2 - Find Start of First Start-of-Message Marker')
    print(result)

    return result


if __name__ == "__main__":
    run()
