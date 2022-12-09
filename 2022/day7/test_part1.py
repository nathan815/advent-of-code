from pathlib import Path
from day7.part1 import FileSystem, File, Directory, run_day7_part1

def test_run_with_sample():
    assert run_day7_part1(file=Path(__file__).parent / 'sample_input.txt') == 95437


class TestFileSystem:

    def test_create_file(self):
        filesystem = FileSystem()
        a = File(name="a", size=10)
        b = File(name="b", size=5)
        filesystem.create_file(a)
        filesystem.create_file(b)
        assert a in filesystem.current_dir.children
        assert b in filesystem.current_dir.children
    
    def test_create_and_change_dir(self):
        filesystem = FileSystem()

        assert filesystem.current_dir.path() == "/"

        a = File(name="a", size=1)
        filesystem.create_file(a)

        assert filesystem.current_dir.children == [a]

        filesystem.create_dir("sub1")
        filesystem.change_dir("sub1")
        sub1_file = File(name="zzz", size=100)
        filesystem.create_file(sub1_file)
        
        assert filesystem.current_dir.path() == "/sub1"
        assert filesystem.current_dir.children == [sub1_file]


class TestDirectory:

    def test_total_size(self):
        dir = Directory(name="a")
        dir.add(File(name="a1.jpg",size=1000))
        dir.add(File(name="a2.png",size=250))

        assert dir.total_size() == 1250

        subdir1 = Directory(name="b")
        dir.add(subdir1)
        subdir1.add(File(name="b1.gif", size=500))

        assert subdir1.total_size() == 500

        assert dir.total_size() == 1750

    def test_get_subdirs(self):
        a = Directory(name="a")
        b = Directory(name="b")
        c = Directory(name="c")
        d = Directory(name="d")
        
        a.add(b)
        a.add(c)
        b.add(d)

        assert c.get_subdirs() == []
        assert d.get_subdirs() == []
        assert [dir.name for dir in a.get_subdirs()] == ["b", "d", "c"]
        assert [dir.name for dir in b.get_subdirs()] == ["d"]
