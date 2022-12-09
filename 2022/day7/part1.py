from dataclasses import dataclass, field
from pathlib import Path
import sys


@dataclass(kw_only=True)
class Node:
    name: str
    parent: 'Node' = None

    def total_size():
        raise NotImplementedError()

    def path(self):
        if self.parent:
            parent = self.parent.path()
            if parent == "/":
                parent = ""
            return f"{parent}/{self.name}"
        else:
            return "/"


@dataclass(kw_only=True)
class File(Node):
    size: int

    def total_size(self):
        return self.size


@dataclass(kw_only=True)
class Directory(Node):
    children: list[Node] = field(default_factory=list)

    def total_size(self):
        size = 0
        for node in self.children:
            size += node.total_size()
        return size
    
    def find(self, name: str):
        for node in self.children:
            if name == node.name:
                return node

    def add(self, node: Node):
        if node.name in [c.name for c in self.children]:
            raise Exception(f"Node {node.name} already exists in directory {self.name}")

        node.parent = self
        self.children.append(node)

    def get_subdirs(self) -> list['Directory']:
        subdirs = []
        for child in self.children:
            if type(child) == Directory:
                subdirs.append(child)
                for subdir in child.get_subdirs():
                    subdirs.append(subdir)
        return subdirs
                

class FileSystem:
    def __init__(self):
        self.root = Directory(name="", parent=None)
        self.current_dir = self.root
    
    def change_dir(self, dir: str):
        if dir == '..':
            if self.current_dir.parent:
                self.current_dir = self.current_dir.parent
        elif dir == '/':
            self.current_dir = self.root
        else:
            found_dir = self.current_dir.find(dir)
            if type(found_dir) == Directory:
                self.current_dir = found_dir
            else:
                raise ValueError(f"Directory {dir} not found in {self.current_dir.name}")

    def create_file(self, file: File):
        self.current_dir.add(file)

    def create_dir(self, name: str):
        self.current_dir.add(Directory(name=name))
    


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
