from pathlib import Path
from day7.part1 import run_day7_part1

def test_run_with_sample():
    assert run_day7_part1(file=Path(__file__).parent / 'sample_input.txt') == 95437
