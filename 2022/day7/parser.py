from day7.filesystem import FileSystem, File

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

    filesystem.change_dir('/')
    return filesystem
