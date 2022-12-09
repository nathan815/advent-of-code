from pathlib import Path
import sys

from day7.filesystem import FileSystem, File, Directory


def find_smallest_directory_to_delete(
    filesystem: FileSystem,
    max_disk_size=70_000_000,
    update_required_space=30_000_000,
):
    current_total_usage = filesystem.root.total_size()
    space_remaining = max_disk_size - current_total_usage
    free_space_needed = update_required_space - space_remaining

    dirs = filesystem.root.get_subdirs()
    def sort_key(dir: Directory):
        return dir.total_size()
    dirs = sorted(dirs, key=sort_key)

    for dir in dirs:
        size = dir.total_size()
        if size >= free_space_needed:
            return dir

    return None


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


def run_day7_part2(file = sys.argv[1] if len(sys.argv) >= 2 else Path(__file__).parent / 'input.txt'):
    with open(file, 'r') as fp:
        lines = fp.read().splitlines()

    filesystem = parse_input(lines)
    smallest_dir_to_delete = find_smallest_directory_to_delete(filesystem)
    result = smallest_dir_to_delete.total_size()

    print('Day 7 Part 2 - Size of Smallest Directory to Delete')
    print(result)

    return result

if __name__ == "__main__":
    run_day7_part2()
