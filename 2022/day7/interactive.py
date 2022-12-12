from pathlib import Path
import sys
from day7.filesystem import Node, Directory
from day7.parser import parse_input


def format_line(node: Node):
    kind = 'dir ' if isinstance(node, Directory) else 'file'
    return f'{kind:5} {node.path():75} {round(node.total_size()/1_000_000, 2):5} MB'


def ls(node: Node, recurse=True, sort=True):

    def walk(node: Node, level=0):
        nodes = [node]
        if isinstance(node, Directory):
            for child in node.children:
                nodes.append(child)
                if recurse and isinstance(child, Directory):
                    nodes += walk(child, level + 1)
        return nodes

    nodes = walk(node)
    if sort:
        nodes.sort(key=lambda n: n.total_size())
    for node in nodes:
        print(format_line(node))


def run(start_cmd = ls):
    with open(Path(__file__).parent / 'input.txt') as fp:
        lines = fp.read().splitlines()

    filesystem = parse_input(lines)

    fullcmd = start_cmd
    while True:
        cwd = filesystem.current_dir.path()
        fullcmd = input(f'[{cwd}] $ ')

        p = fullcmd.split(' ')
        cmd = p[0]
        args = p[1:]
        path = args[len(args)-1] if len(args) > 0 else None

        try:
            if cmd == 'ls':
                if path == '/':
                    dir = filesystem.root
                elif path and path not in ['-r', '-s']:
                    dir = filesystem.current_dir.resolve(path)
                else:
                    dir = filesystem.current_dir
                ls(dir, recurse=any([a == '-r' for a in args]), sort=any([a == '-s' for a in args]))
            elif cmd == 'cd':
                if path:
                    if path == '/':
                        filesystem.change_dir('/')
                    elif path == '..' and filesystem.current_dir.parent:
                        filesystem.current_dir = filesystem.current_dir.parent
                    else:
                        if path != '' and path != '/':
                            parts = path.split('/')
                            for part in parts:
                                if part:
                                    filesystem.change_dir(part)
            elif cmd == 'pwd':
                print(cwd)
            elif cmd == 'exit':
                break
            elif cmd == 'help':
                print('ls [-s : sort] [-r : recursive]')
                print('cd <path>')
                print('pwd')
                print('help')
                print('exit')
            else:
                print('invalid command')
        except Exception as e:
            print(e)

if __name__ == "__main__":
    run()
