from pathlib import Path
import sys

from day7.common import FileSystem, File


def sum_directories_less_than_size(filesystem: FileSystem, max_size=100_000):
    dirs = filesystem.root.get_subdirs()
    sum = 0
    for dir in dirs:
        size = dir.total_size()
        if size <= max_size:
            sum += size
    return sum


def parse_input(lines: list[str]) -> FileSystem:
    filesystem = FileSystem()

    for line in lines:
        parts = line.split(" ")
        if parts[0] == "$":
            cmd = parts[1]
            if cmd == "ls":
                pass
            elif cmd == "cd":
                dir = parts[2]
                filesystem.change_dir(dir)
        else:
            if parts[0] == "dir":
                filesystem.create_dir(parts[1])
            else:
                size = int(parts[0])
                filesystem.create_file(File(name=parts[1], size=size))

    return filesystem


def run_day7_part1(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file, 'r') as fp:
        lines = fp.read().splitlines()

    filesystem = parse_input(lines)
    result = sum_directories_less_than_size(filesystem)

    print('Day 7 Part 1 - Sum of Directory Sizes where Size <= 100000')
    print(result)

    return result

if __name__ == "__main__":
    run_day7_part1()
