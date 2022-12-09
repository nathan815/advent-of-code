from dataclasses import dataclass, field


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
    

