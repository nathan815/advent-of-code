from pathlib import Path
from day7.part2 import run

def test_run_with_sample():
    assert run(file=Path(__file__).parent / 'sample_input.txt') == 24933642
